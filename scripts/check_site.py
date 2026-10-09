"""Check the static learning site's actual content and relative references."""
import csv
import hashlib
import json
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlparse, unquote, parse_qs

ROOT=Path(__file__).resolve().parents[1]
SITE=ROOT/'site'
class Links(HTMLParser):
    def __init__(self):super().__init__();self.links=[];self.ids=set()
    def handle_starttag(self,tag,attrs):
        a=dict(attrs)
        if 'id' in a:self.ids.add(a['id'])
        for key in ['href','src']:
            if key in a:self.links.append(a[key])

docs=json.loads((SITE/'data/documents.json').read_text(encoding='utf-8'))
missions=json.loads((SITE/'data/missions.json').read_text(encoding='utf-8'))
talks=json.loads((SITE/'data/talks.json').read_text(encoding='utf-8'))
assert len(missions)==180
assert len({m['id'] for m in missions})==180
for m in missions:assert m['doc'] in docs,m
for i in range(1,151):assert f'assessment/modules/RT{i:03}.md' in docs
for path,body in docs.items():assert (ROOT/path).read_text(encoding='utf-8')==body,path
assert len(talks['records'])==32
assert len({r['id'] for r in talks['records']})==32
assert sum(r['kind']=='Workshop' for r in talks['records'])==6
assert all(r['edition']>=34 and r['source_id'] in {'DC02','DC03'} for r in talks['records'])
assert all(r['video_url'] is None and r['slides_url'] is None for r in talks['records'])
assert talks['video_files_retrieved']==0 and talks['slide_files_retrieved']==0
assert talks==json.loads((ROOT/'data/conferences/defcon.json').read_text(encoding='utf-8'))
rows=list(csv.DictReader((ROOT/'data/hardware/timing.csv').open()))
assert len(rows)==60 and all(r['provenance']=='synthetic_arithmetic_not_hardware' for r in rows)
for p in SITE.glob('*.html'):
    parser=Links();parser.feed(p.read_text(encoding='utf-8'))
    assert 'main' in parser.ids,p
    for href in parser.links:
        parsed=urlparse(href)
        if parsed.scheme or parsed.netloc:continue
        if not parsed.path:
            assert parsed.fragment in parser.ids,(p,href)
            continue
        resolved=(p.parent/unquote(parsed.path)).resolve()
        assert resolved.is_relative_to(SITE.resolve()) and resolved.is_file(),(p,href)
        if resolved.name=='reader.html':
            key=parse_qs(parsed.query).get('doc',[None])[0]
            if key:assert key in docs,(p,key)
    assert '<html lang="en">' in p.read_text(encoding='utf-8')
assert len(list((SITE/'media').glob('*.svg')))==14 # Eleven conceptual diagrams, two 3D references, and favicon.
assert len(list((SITE/'media/research').glob('*.svg')))==7
assert (SITE/'vendor/LICENSE.marked').is_file()
visuals=json.loads((ROOT/'data/visuals/assets.json').read_text(encoding='utf-8'))
assert len(visuals['assets'])==3
for image in visuals['assets']:
    content=(ROOT/image['path']).read_bytes()
    assert hashlib.sha256(content).hexdigest()==image['sha256']
    assert hashlib.sha1(content).hexdigest()==image['sha1']
    assert len(content)==image['bytes']
    assert image['license']=='CC BY-SA 4.0' and image['source_url'].startswith('https://commons.wikimedia.org/')
assert 'site/IMAGE-CREDITS.md' in docs
print(f'Site integrity passed: 9 pages, {len(docs)} documents, 180 missions, 32 source-backed sessions, 60 synthetic timing rows.')
