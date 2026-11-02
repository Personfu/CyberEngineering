"""Render a source-bound practical workbench and original walkthrough index."""
import html
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
def esc(value):return html.escape(str(value),quote=True)


def load():
    entries=json.loads((ROOT/'data/labs/catalog.json').read_text())['labs']
    ids=set();sources={s['id'] for s in json.loads((ROOT/'data/reviews/sources.json').read_text())['sources']}
    for lab in entries:
        if lab['id'] in ids or not lab['steps'] or not set(lab['source_ids'])<=sources:
            raise ValueError('Duplicate/incomplete lab or unbound source')
        ids.add(lab['id'])
        if not (ROOT/lab['guide']).is_file():raise ValueError('Missing walkthrough')
    return entries


def generated_files():
    entries=load();files={}
    index=['# Practical lab index','','Each lesson is an original exercise with prerequisites, a procedure, expected output and failure cases. Offline fixtures, optional tools and physical-device work are distinct. A documented hardware step is not reported as an executed hardware test.','','| Lab | Mode | Outcome |','| --- | --- | --- |']
    for lab in entries:
        path=Path('labs/lessons')/(lab['id']+'.md')
        index.append(f'| [{lab["id"]} · {lab["title"]}](lessons/{lab["id"]}.md) | {lab["mode"]} | {lab["goal"]} |')
        lines=[f'# {lab["id"]} · {lab["title"]}','','**'+lab['mode']+' · '+lab['category']+' · '+lab['level']+'**','',lab['goal'],'','## Materials','',lab['inputs'],'','## Procedure','']
        lines += [f'{i}. {step}' for i,step in enumerate(lab['steps'],1)]
        if lab['commands']:lines += ['','## Commands','','Run from the repository root unless the walkthrough gives a different checkout/directory.','','```bash',*lab['commands'],'```']
        lines += ['','## Expected result','',lab['expected'],'','## Failure cases and interpretation','',lab['failures'],'','## Record','', 'Keep the input/source version, command, relevant output and interpretation together. Label a fixture synthetic. Physical-device work needs the actual model, firmware and conditions. Do not report an unrun exercise as passed.','','## Full walkthrough','',f'[Read the complete method](../../{lab["guide"]}) · [Workbench index](../README.md) · [Custom scripts](../SCRIPTS.md)','','## Sources','']
        lines += [f'- [Primary source: {s}](../../hardware/PRIMARY-SOURCES.md#{s})' for s in lab['source_ids']]
        files[path]='\n'.join(lines)+'\n'
    files[Path('labs/CATALOG.md')]='\n'.join(index)+'\n'
    return files


def content(panel):
    entries=load();categories=sorted({e['mode'] for e in entries})
    body=f'''<section class="review-intro panel"><span class="eyebrow">THE NIGHTSHIFT WORKBENCH / LEARN BY BUILDING</span><h1>Make it work.<br>Know why it works.</h1><p class="lead">Walkthroughs, original scripts and tests that connect the tool to the result.</p><p>{len(entries)} practical exercises cover firmware, radio nodes, protocols, evidence, software and recovery. Start with the offline fixtures, then use an exact model guide for hardware.</p><div class="hero-actions"><a class="button" href="reader.html?doc=labs/README.md">Start the local examples</a><a class="button ghost" href="reader.html?doc=labs/FLASHING.md">Firmware &amp; recovery</a><a href="reader.html?doc=labs/SCRIPTS.md">Custom helper reference →</a></div></section>'''
    body+=panel('Your local toolkit','<pre><code>python -m labtools.benchkit inventory\npython -m labtools.benchkit telemetry labs/fixtures/messages.csv\npython -m labtools.benchkit ble-decode 02010605094c414231\npython -m unittest discover -s tests -v</code></pre><p>Python standard library. No connected device is needed for these fixture checks. A flash plan is a dry run; it never executes a hardware write.</p>','RUN / READ / EXPLAIN')
    body+='<section class="panel"><div class="panel-head"><h2>Pick an experiment</h2><span>INPUT → OBSERVATION → EVIDENCE</span></div><label for="search">Search labs</label><input id="search" type="search" placeholder="Try firmware, BLE, recovery or power"><label for="kind">Equipment requirement</label><select id="kind"><option value="">All exercises</option>'+''.join(f'<option>{esc(c)}</option>' for c in categories)+'</select><p id="result-count" role="status"></p><div class="cards searchable" id="lab-cards">'
    for lab in entries:
        search=' '.join([lab['id'],lab['title'],lab['category'],lab['goal']])
        body+=f'<article class="card" data-kind="{esc(lab["mode"])}" data-search="{esc(search)}"><span class="eyebrow">{esc(lab["id"])} / {esc(lab["mode"])}</span><h3>{esc(lab["title"])}</h3><p>{esc(lab["goal"])}</p><p class="lab-level">{esc(lab["level"])} · {esc(lab["category"])}</p><a href="reader.html?doc=labs/lessons/{esc(lab["id"])}.md">Open the exercise →</a></article>'
    body+='</div></section>'
    body+=panel('A route through the whole system','<p>Start with artifact identity and an exact hardware target. Validate a local interface, inspect its evidence, measure with a known fixture, then test recovery. The same discipline connects the atlas domains: formal assurance, hardware trust, network observability, privacy, cloud systems and resilience.</p><a href="reader.html?doc=labs/guides/assurance.md">Assurance and recovery walkthrough →</a><p><a href="reviews.html">Compare the tools behind the work →</a></p>','DEVELOP / OBSERVE / RECOVER')
    return body
