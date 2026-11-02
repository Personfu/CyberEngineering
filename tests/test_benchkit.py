import contextlib
import functools
import hashlib
import http.server
import io
import json
from pathlib import Path
import struct
import tempfile
import threading
import unittest
from unittest.mock import patch

from labtools import benchkit as b


class Benchkit(unittest.TestCase):
    def setUp(self):
        self.directory=tempfile.TemporaryDirectory();self.addCleanup(self.directory.cleanup)
        self.root=Path(self.directory.name)
        self.artifact=self.root/'image.bin';self.artifact.write_bytes(b'\xe9fixture-artifact-not-physical-firmware')
        self.manifest=self.root/'manifest.json'
        self.data={'board':'cardputer','chip':'esp32s3','kind':'merged-factory','offset':'0x0','file':'image.bin','sha256':b.digest(self.artifact),'source_url':'https://github.com/pr3y/Bruce/releases'}
        self.save()

    def save(self):self.manifest.write_text(json.dumps(self.data))

    def test_digest_mismatch_is_a_failure(self):
        self.assertTrue(b.verify(self.artifact,self.data['sha256'])['verified'])
        with self.assertRaisesRegex(ValueError,'mismatch'):b.verify(self.artifact,'0'*64)
        with self.assertRaisesRegex(ValueError,'hexadecimal'):b.verify(self.artifact,'abc')

    def test_plan_is_explicit_dry_run_and_never_executes(self):
        plan=b.flash_plan(self.manifest,'cardputer','/dev/ttyACM0')
        self.assertTrue(plan['dry_run']);self.assertFalse(plan['executed'])
        self.assertEqual(plan['command_argv'][-3:],['write_flash','0x0',str(self.artifact)])
        self.assertIn('--chip',plan['command_argv'])

    def test_wrong_board_and_chip_are_rejected(self):
        with self.assertRaisesRegex(ValueError,'board/chip'):b.flash_plan(self.manifest,'cardputer-adv','COM3')
        self.data['chip']='esp32';self.save()
        with self.assertRaisesRegex(ValueError,'board/chip'):b.flash_plan(self.manifest,'cardputer','COM3')

    def test_ota_and_arbitrary_offsets_are_not_factory_plans(self):
        for key,value in [('kind','ota'),('offset','0x10000')]:
            original=self.data[key];self.data[key]=value;self.save()
            with self.assertRaisesRegex(ValueError,'merged factory'):b.flash_plan(self.manifest,'cardputer','COM3')
            self.data[key]=original

    def test_example_only_fixture_is_never_a_flash_plan(self):
        self.data['example_only']=True;self.save()
        with self.assertRaisesRegex(ValueError,'Example-only'):b.flash_plan(self.manifest,'cardputer','COM3')

    def test_manifest_cannot_hide_credentials_or_a_port_option(self):
        self.data['source_url']='https://user:password@example.com/image.bin';self.save()
        with self.assertRaisesRegex(ValueError,'credential-free'):b.flash_plan(self.manifest,'cardputer','COM3')
        self.data['source_url']='https://example.com/image.bin';self.save()
        with self.assertRaisesRegex(ValueError,'device path'):b.flash_plan(self.manifest,'cardputer','--bad-option')

    def test_changed_artifact_invalidates_a_prepared_manifest(self):
        self.artifact.write_bytes(b'different')
        with self.assertRaisesRegex(ValueError,'mismatch'):b.flash_plan(self.manifest,'cardputer','COM3')

    def test_loopback_boundary_includes_redirects(self):
        for url in ['http://127.0.0.1:8765','http://localhost/','http://[::1]/']:
            self.assertEqual(b.loopback_url(url),url)
        for url in ['https://example.com','http://127.0.0.1.example.com','file:///tmp/a','http://user:pass@localhost']:
            with self.assertRaises(ValueError):b.loopback_url(url)
        with self.assertRaises(ValueError):
            b.LocalRedirect().redirect_request(None,None,302,'redirect',{},'https://example.com/')

    def test_local_http_records_real_success_and_not_found(self):
        (self.root/'health.json').write_text('{"status":"ok"}')
        class Quiet(http.server.SimpleHTTPRequestHandler):
            def log_message(self,*args):pass
        handler=functools.partial(Quiet,directory=str(self.root))
        server=http.server.ThreadingHTTPServer(('127.0.0.1',0),handler)
        thread=threading.Thread(target=server.serve_forever,daemon=True);thread.start()
        try:
            base='http://127.0.0.1:'+str(server.server_port)
            self.assertEqual(b.http_check(base+'/health.json')['status'],200)
            missing=b.http_check(base+'/missing');self.assertEqual(missing['status'],404);self.assertFalse(missing['http_success'])
        finally:server.shutdown();server.server_close();thread.join()

    def test_message_fixture_distinguishes_loss_and_latency(self):
        result=b.telemetry(b.ROOT/'labs/fixtures/messages.csv')
        self.assertEqual((result['sent'],result['received'],result['missing']),(10,8,2))
        self.assertEqual(result['delivery_fraction'],.8);self.assertEqual(result['median_latency_ms'],60)

    def test_timing_duplicates_clock_errors_and_nan_fail(self):
        for rows in ['1,10,9\n','1,0,1\n1,2,3\n','1,nan,2\n','1,0,inf\n']:
            p=self.root/'messages.csv';p.write_text('sequence,sent_ms,received_ms\n'+rows)
            with self.assertRaises(ValueError):b.telemetry(p)

    def test_unobserved_messages_have_no_invented_latency(self):
        p=self.root/'messages.csv';p.write_text('sequence,sent_ms,received_ms\n1,0,\n')
        result=b.telemetry(p);self.assertIsNone(result['median_latency_ms']);self.assertEqual(result['received'],0)

    def test_ble_decodes_a_fictional_name_without_identity_inference(self):
        result=b.ble_decode('02010605094c414231')
        self.assertEqual(result['fields'][1]['text'],'LAB1');self.assertFalse(result['identity_inferred'])
        for value in ['0509ff','zz','0001']:
            with self.assertRaises(ValueError):b.ble_decode(value)

    def uf2(self,number=0,total=1):
        value=bytearray(512);struct.pack_into('<8I',value,0,0x0A324655,0x9E5D5157,0x2000,0x2000,256,number,total,0xADA52840);struct.pack_into('<I',value,508,0x0AB16F30);return value

    def test_uf2_structural_integrity_is_not_compatibility(self):
        p=self.root/'synthetic.uf2';p.write_bytes(self.uf2())
        result=b.uf2_inspect(p);self.assertEqual(result['family_ids'],['ada52840']);self.assertFalse(result['compatible_board_verified'])
        for value in [self.uf2()[:300],self.uf2(0,2),self.uf2()+self.uf2()]:
            p.write_bytes(value)
            with self.assertRaises(ValueError):b.uf2_inspect(p)

    def test_pin_nets_allow_explicit_sharing_but_not_collisions(self):
        result=b.pincheck(b.ROOT/'labs/fixtures/pins-good.json')
        self.assertEqual(result['unique_pins'],3);self.assertEqual(result['explicit_shared_signals'],['18'])
        with self.assertRaisesRegex(ValueError,'conflicts'):b.pincheck(b.ROOT/'labs/fixtures/pins-conflict.json')

    def test_power_estimate_and_invalid_assumptions(self):
        result=b.power(1200,80,5,.1,.8)
        self.assertAlmostEqual(result['average_current_ma'],12.5);self.assertAlmostEqual(result['estimated_hours'],76.8)
        for values in [(0,1,1,.1,.8),(1,1,1,2,.8),(1,0,0,.1,.8),(float('nan'),1,1,.1,.8)]:
            with self.assertRaises(ValueError):b.power(*values)

    def test_cli_preserves_nonzero_exit_and_stderr(self):
        stderr=io.StringIO()
        with contextlib.redirect_stderr(stderr):
            result=b.main(['ble-decode','0509ff'])
        self.assertEqual(result,1);self.assertIn('Truncated',stderr.getvalue())


if __name__=='__main__':unittest.main()
