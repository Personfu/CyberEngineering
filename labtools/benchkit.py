"""Reproducible bench records and diagnostics. Flash plans never execute writes."""
import argparse
import csv
import hashlib
import ipaddress
import json
import math
from pathlib import Path
import statistics
import struct
import sys
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def digest(path):
    h = hashlib.sha256()
    with Path(path).open('rb') as stream:
        for block in iter(lambda: stream.read(1024*1024), b''):
            h.update(block)
    return h.hexdigest()


def verify(path, expected):
    if not Path(path).is_file():raise ValueError('Artifact must be a regular file')
    expected = expected.lower()
    if len(expected) != 64 or any(c not in '0123456789abcdef' for c in expected):
        raise ValueError('Expected SHA-256 must contain 64 hexadecimal characters')
    actual = digest(path)
    if actual != expected:
        raise ValueError(f'SHA-256 mismatch: expected {expected}, received {actual}')
    return {'verified': True, 'file': str(path), 'bytes': Path(path).stat().st_size, 'sha256': actual}


def inventory():
    ports = sorted({str(p) for pattern in ['ttyACM*','ttyUSB*','cu.usb*','serial/by-id/*'] for p in Path('/dev').glob(pattern)})
    return {'python': sys.version.split()[0], 'platform': sys.platform, 'serial_candidates': ports, 'devices_opened': False, 'note': 'Paths are candidates, not proof of board identity. On Windows use the OS device manager for COM ports.'}


def flash_plan(manifest_path, board, port):
    profiles = json.loads((ROOT/'labs/fixtures/board-profiles.json').read_text())
    if board not in profiles:
        raise ValueError('Unknown board profile')
    profile = profiles[board]
    manifest_path = Path(manifest_path)
    manifest = json.loads(manifest_path.read_text())
    if manifest.get('board') != board or manifest.get('chip') != profile['chip']:
        raise ValueError('Manifest board/chip does not match selected profile')
    if manifest.get('kind') != 'merged-factory' or manifest.get('offset') != '0x0':
        raise ValueError('Only explicitly identified merged factory images at 0x0 can be planned; OTA/app/bootloader files are different')
    source = urllib.parse.urlsplit(manifest.get('source_url',''))
    if source.scheme != 'https' or not source.hostname or source.username or source.password:
        raise ValueError('A credential-free official HTTPS artifact reference is required')
    if not port or port.startswith('-') or any(c in port for c in '\r\n\0'):
        raise ValueError('Specify the device path or COM port explicitly')
    artifact = (manifest_path.parent/manifest['file']).resolve()
    if artifact.suffix.lower() != '.bin':
        raise ValueError('ESP merged image must be a .bin; UF2/images use a different workflow')
    if not artifact.is_file() or artifact.stat().st_size == 0:
        raise ValueError('Artifact is missing or empty')
    if manifest.get('example_only'):
        raise ValueError('Example-only fixtures cannot produce a board-write plan')
    receipt = verify(artifact, manifest['sha256'])
    return {'dry_run': True, 'executed': False, 'board': board, 'chip': profile['chip'], 'artifact': receipt,
            'command_argv': [sys.executable,'-m','esptool','--chip',profile['chip'],'--port',port,'write_flash','0x0',str(artifact)],
            'requirements': ['Confirm the publisher actually identifies this exact artifact as a merged factory image at 0x0.', 'Confirm the physical board and recovery procedure independently.', 'A matching digest identifies bytes; it does not authenticate the publisher or detect hardware automatically.']}


def loopback_url(url):
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme not in {'http','https'} or parsed.username or parsed.password:
        raise ValueError('Use a credential-free loopback HTTP(S) URL')
    try:
        local = parsed.hostname == 'localhost' or ipaddress.ip_address(parsed.hostname or '').is_loopback
    except ValueError:
        local = False
    if not local:
        raise ValueError('This lab helper accepts loopback destinations only')
    return url


class LocalRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        loopback_url(newurl)
        return super().redirect_request(req,fp,code,msg,headers,newurl)


def http_check(url):
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}),LocalRedirect())
    try:
        response = opener.open(loopback_url(url), timeout=5)
    except urllib.error.HTTPError as error:
        response = error
    with response:
        body = response.read(1024*1024+1)
        if len(body) > 1024*1024:
            raise ValueError('Lab response exceeds 1 MiB')
        return {'status': response.code, 'content_type': response.headers.get('Content-Type'), 'bytes': len(body), 'body_sha256': hashlib.sha256(body).hexdigest(), 'http_success': 200 <= response.code < 300}


def telemetry(path):
    with Path(path).open(newline='') as stream:
        reader = csv.DictReader(stream)
        if not {'sequence','sent_ms','received_ms'} <= set(reader.fieldnames or []):
            raise ValueError('Required columns: sequence,sent_ms,received_ms')
        rows = list(reader)
    if not rows or len({r['sequence'] for r in rows}) != len(rows):
        raise ValueError('Input must contain unique message sequences and at least one sent message')
    latency = []
    for row in rows:
        sent = float(row['sent_ms'])
        if not math.isfinite(sent):raise ValueError('Timestamp must be finite')
        if row['received_ms'].strip():
            delay = float(row['received_ms'])-sent
            if not math.isfinite(delay) or delay < 0:
                raise ValueError('Receive time precedes send time; check clocks')
            latency.append(delay)
    return {'sent': len(rows), 'received': len(latency), 'missing': len(rows)-len(latency), 'delivery_fraction': len(latency)/len(rows), 'median_latency_ms': statistics.median(latency) if latency else None, 'max_latency_ms': max(latency) if latency else None, 'interpretation': 'Missing receive time means not observed in this fixture; synchronized timestamps are assumed.'}


def ble_decode(value):
    try:
        data = bytes.fromhex(value)
    except ValueError as error:
        raise ValueError('Advertisement must be hexadecimal bytes') from error
    fields=[];offset=0
    names={1:'Flags',8:'Shortened local name',9:'Complete local name',255:'Manufacturer data'}
    while offset < len(data):
        length=data[offset];offset+=1
        if length == 0:
            if any(data[offset:]):raise ValueError('Nonzero bytes follow advertisement terminator')
            break
        if offset+length > len(data):raise ValueError('Truncated BLE advertising structure')
        kind=data[offset];payload=data[offset+1:offset+length]
        field={'type':kind,'label':names.get(kind,'Other AD type'),'data_hex':payload.hex()}
        if kind in [8,9]:field['text']=payload.decode('utf-8',errors='replace')
        fields.append(field);offset+=length
    return {'fields':fields,'identity_inferred':False,'scope':'Offline TLV decoding only; no radio operation or device attribution.'}


def uf2_inspect(path):
    data=Path(path).read_bytes()
    if not data or len(data)%512:raise ValueError('UF2 must contain whole 512-byte blocks')
    blocks=set();families=set();totals=set();addresses=[]
    for pos in range(0,len(data),512):
        block=data[pos:pos+512];a,b,flags,address,size,number,total,family=struct.unpack_from('<8I',block)
        if (a,b,struct.unpack_from('<I',block,508)[0]) != (0x0A324655,0x9E5D5157,0x0AB16F30):raise ValueError('Invalid UF2 block magic')
        if size>476 or size==0 or number in blocks or total==0:raise ValueError('Invalid or duplicate UF2 block')
        blocks.add(number);totals.add(total);addresses.append(address)
        if flags&0x2000:families.add(f'{family:08x}')
    if totals != {len(blocks)} or blocks != set(range(len(blocks))):raise ValueError('Incomplete UF2 block sequence')
    return {'blocks':len(blocks),'family_ids':sorted(families),'lowest_target_address':hex(min(addresses)),'compatible_board_verified':False,'note':'Structural validation is not a signature, complete bootability or board compatibility check.'}


def pincheck(path):
    rows=json.loads(Path(path).read_text());used={};shared=[]
    for row in rows:
        pin=str(row['pin']);signal=row['signal'].strip()
        if not signal:raise ValueError('Signal name required')
        if pin in used:
            if used[pin] != signal:raise ValueError(f'Pin {pin} conflicts: {used[pin]} versus {signal}')
            shared.append(pin)
        used[pin]=signal
    return {'valid':True,'unique_pins':len(used),'explicit_shared_signals':sorted(set(shared)),'note':'Only declared net-name collisions are checked. This is not an electrical design-rule check.'}


def power(capacity, active, idle, duty, usable):
    if not all(math.isfinite(v) for v in [capacity,active,idle,duty,usable]) or capacity<=0 or active<0 or idle<0 or not 0<=duty<=1 or not 0<usable<=1:
        raise ValueError('Invalid capacity, current, duty fraction or usable fraction')
    average=active*duty+idle*(1-duty)
    if average<=0:raise ValueError('Average current must be positive')
    return {'average_current_ma':average,'estimated_hours':capacity*usable/average,'assumptions':'Planning estimate using battery-side currents and one consistent voltage. Ignores temperature, aging and nonlinear discharge; not measured product runtime.'}


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__);sub=parser.add_subparsers(dest='action',required=True)
    sub.add_parser('inventory')
    p=sub.add_parser('verify');p.add_argument('file',type=Path);p.add_argument('--sha256',required=True)
    p=sub.add_parser('flash-plan');p.add_argument('manifest',type=Path);p.add_argument('--board',required=True);p.add_argument('--port',required=True)
    p=sub.add_parser('http');p.add_argument('url')
    p=sub.add_parser('telemetry');p.add_argument('file',type=Path)
    p=sub.add_parser('ble-decode');p.add_argument('hex')
    p=sub.add_parser('uf2-inspect');p.add_argument('file',type=Path)
    p=sub.add_parser('pincheck');p.add_argument('file',type=Path)
    p=sub.add_parser('power');p.add_argument('--capacity-mah',type=float,required=True);p.add_argument('--active-ma',type=float,required=True);p.add_argument('--idle-ma',type=float,required=True);p.add_argument('--duty',type=float,required=True);p.add_argument('--usable',type=float,default=.8)
    args=parser.parse_args(argv)
    try:
        result={'inventory':lambda:inventory(),'verify':lambda:verify(args.file,args.sha256),'flash-plan':lambda:flash_plan(args.manifest,args.board,args.port),'http':lambda:http_check(args.url),'telemetry':lambda:telemetry(args.file),'ble-decode':lambda:ble_decode(args.hex),'uf2-inspect':lambda:uf2_inspect(args.file),'pincheck':lambda:pincheck(args.file),'power':lambda:power(args.capacity_mah,args.active_ma,args.idle_ma,args.duty,args.usable)}[args.action]()
    except (ValueError,KeyError,OSError,json.JSONDecodeError,urllib.error.URLError) as error:
        print(f'benchkit: {error}',file=sys.stderr);return 1
    print(json.dumps(result,indent=2,allow_nan=False));return 0


if __name__=='__main__':
    raise SystemExit(main())
