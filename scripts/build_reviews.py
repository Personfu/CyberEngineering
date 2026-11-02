"""Build independent primary-source reviews, product manuals and research receipts."""
import collections
import hashlib
import html
import json
from pathlib import Path
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
def esc(value):
    return html.escape(str(value), quote=True)


def load():
    catalog = json.loads((ROOT/'data/reviews/catalog.json').read_text())
    sources = json.loads((ROOT/'data/reviews/sources.json').read_text())
    by_id = {s['id']: s for s in sources['sources']}
    if len(by_id) != len(sources['sources']):
        raise ValueError('Duplicate primary source')
    for source in sources['sources']:
        url = urlsplit(source['url'])
        if url.scheme != 'https' or not url.hostname or url.username or url.password or 'youtube' in url.hostname or url.hostname == 'youtu.be':
            raise ValueError('Primary documentation URL required')
        if not re.fullmatch('[a-f0-9]{64}',source['sha256']) or source['bytes'] <= 0:
            raise ValueError('Retrieval receipt required')
    ids = set()
    for entry in catalog['entries']:
        if not re.fullmatch('[a-z0-9-]+',entry['id']) or entry['id'] in ids:
            raise ValueError('Invalid or duplicate guide identity')
        ids.add(entry['id'])
        if not entry['source_ids'] or not set(entry['source_ids']) <= by_id.keys():
            raise ValueError('Unbound primary source')
        if len(entry['specs']) < 3 or any(f['source_id'] not in entry['source_ids'] for f in entry['specs']):
            raise ValueError('Unbound feature claim')
        if any(not entry[k].strip() for k in ['assessment','tradeoff','choose_if','skip_if','bench_check']):
            raise ValueError('Incomplete review')
        if entry['doc'] != f'hardware/reviews/{entry["id"]}.md':
            raise ValueError('Invalid documentation path')
    return catalog,sources


def mixed_entries(entries):
    groups=collections.defaultdict(list)
    for entry in entries:
        groups[entry['category']].append(entry)
    buckets=[sorted(groups[c],key=lambda e:hashlib.sha256(e['id'].encode()).hexdigest()) for c in sorted(groups)]
    result=[]
    while any(buckets):
        for bucket in buckets:
            if bucket:result.append(bucket.pop(0))
    return result


def workflow(entry):
    if entry['category']=='LoRa & navigation':return 'mesh-node'
    if entry['id'].startswith(('proxmark','chameleon')):return 'rfid-bench'
    if entry['id']=='flipper-zero':return 'flipper-development'
    if entry['category']=='Cyberdecks & compute' or entry['id'] in {'armbian','raspyjack'}:return 'linux-cyberdeck'
    if entry['category']=='SDR & signals':return 'sdr-bench'
    return 'esp32-firmware'


def content():
    catalog,sources=load();entries=catalog['entries'];by_id={s['id']:s for s in sources['sources']}
    categories=sorted({e['category'] for e in entries});kinds=sorted({e['kind'] for e in entries})
    body=f'''<section class="review-intro panel"><span class="eyebrow">INDEPENDENT RESEARCH / {esc(catalog['updated_on'])}</span><h1>Know your tools.</h1><p class="lead">Capabilities. Compatibility. A reason to choose.</p><p>{len(entries)} individual reviews, full product documentation and original recommendations, researched from {len(by_id)} retrieved manufacturer and maintainer documents.</p><div class="review-metrics"><span><strong>{len(entries)}</strong> researched reviews</span><span><strong>{len(categories)}</strong> engineering categories</span><span><strong>{len(by_id)}</strong> primary documents</span></div><p class="review-disclosure">Documented specifications and our own analysis. Hands-on measurements are identified separately; none are invented.</p><div class="hero-actions"><a class="button" href="#review-library">Find a product</a><a class="button ghost" href="labs.html">Open the workbench</a><a href="#primary-sources">Inspect the research ↓</a></div></section><section class="panel" id="review-library"><div class="panel-head"><h2>Choose by the work</h2><span>RESEARCH / FEATURES / COMPARE</span></div><div class="review-controls"><div><label for="review-search">Product, feature or use case</label><input id="review-search" type="search" placeholder="Try PSRAM, Cardputer, GNSS or PoE"></div><div><label for="review-category">Engineering category</label><select id="review-category"><option value="">All categories</option>{''.join(f'<option>{esc(c)}</option>' for c in categories)}</select></div><div><label for="review-kind">Tool type</label><select id="review-kind"><option value="">All types</option>{''.join(f'<option>{esc(k)}</option>' for k in kinds)}</select></div><div><label for="review-order">Browse order</label><select id="review-order"><option value="mixed">Mixed bench</option><option value="name">Name A–Z</option><option value="category">By category</option></select></div></div><div class="review-actions"><button id="review-shuffle" type="button">Shuffle the bench</button><button id="review-reset" type="button">Reset filters</button><a href="#comparison">Compare selected ↓</a></div><p id="review-result-count" role="status">{len(entries)} reviews. Enable JavaScript for filters and comparison.</p><div class="review-grid" id="review-cards">'''
    for entry in mixed_entries(entries):
        search=' '.join([entry['name'],entry['category'],entry['kind'],entry['purpose'],entry['assessment'],entry['alternatives'],*[f['label']+' '+f['value'] for f in entry['specs']]])
        facts=''.join(f'<div><dt>{esc(f["label"])}</dt><dd>{esc(f["value"])} <a href="#source-{esc(f["source_id"])}" aria-label="Source {esc(f["source_id"])}">↗</a></dd></div>' for f in entry['specs'])
        refs=''.join(f'<li><a href="{esc(by_id[i]["url"])}" rel="noreferrer">{esc(by_id[i]["title"])}</a></li>' for i in entry['source_ids'])
        body+=f'''<article class="review-card" id="review-{esc(entry['id'])}" data-id="{esc(entry['id'])}" data-name="{esc(entry['name'])}" data-category="{esc(entry['category'])}" data-kind="{esc(entry['kind'])}" data-search="{esc(search)}"><div class="review-card-meta"><span>{esc(entry['category'])}</span><span>{esc(entry['kind'])}</span></div><h3><a href="reader.html?doc={esc(entry['doc'])}">{esc(entry['name'])}</a></h3><p class="review-purpose">{esc(entry['purpose'])}</p><dl class="product-facts">{facts}</dl><details><summary>Our verdict &amp; tradeoffs</summary><p>{esc(entry['assessment'])}</p><h4>Choose it when</h4><p>{esc(entry['choose_if'])}</p><h4>Skip it when</h4><p>{esc(entry['skip_if'])}</p><h4>Compatibility &amp; limits</h4><p>{esc(entry['tradeoff'])}</p><h4>Alternatives</h4><p>{esc(entry['alternatives'])}</p><ul class="review-refs">{refs}</ul></details><p><a href="reader.html?doc={esc(entry['doc'])}">Read the full documentation →</a></p><p class="review-basis">{esc(entry['basis'])}</p><label class="compare-choice"><input type="checkbox" data-compare="{esc(entry['id'])}" aria-describedby="compare-status"> Add to comparison</label></article>'''
    body+='''</div><p id="review-empty" hidden>No products match. Try a broader term or reset filters.</p></section><section class="panel" id="comparison"><div class="panel-head"><h2>Your bench shortlist</h2><span>UP TO THREE TOOLS</span></div><p id="compare-status" role="status">Select two or three products to compare capabilities and tradeoffs.</p><button id="compare-clear" type="button">Clear comparison</button><div id="compare-table" class="compare-scroll" tabindex="0" role="region" aria-label="Selected tool comparison"></div></section>'''
    body+=f'<section class="panel" id="primary-sources"><div class="panel-head"><h2>The research behind the reviews</h2><span>{len(by_id)} PRIMARY DOCUMENTS</span></div><p>Sources were read independently. Citations identify documented capabilities; verdicts are our analysis. Retrieval receipts make the research inspectable.</p><ol class="primary-source-list">'
    for source in sources['sources']:
        body+=f'<li id="source-{esc(source["id"])}"><a href="{esc(source["url"])}" rel="noreferrer">{esc(source["title"])}</a><small>{esc(urlsplit(source["url"]).hostname)} · retrieved {esc(source["retrieved_at"][:10])}</small><details><summary>Retrieval receipt</summary><p>{source["bytes"]:,} bytes · SHA-256</p><code>{esc(source["sha256"])}</code></details></li>'
    return body+'</ol><p><a href="reader.html?doc=hardware/RESEARCH-COVERAGE.md">Research coverage and remaining targets →</a></p></section>'


def review_document(entry,by_id):
    lines=[f'# {entry["name"]}','','**Independent documentation review · 2026-11-02**','',entry['purpose'],'','## Documented features','','| Feature | Finding | Primary source |','| --- | --- | --- |']
    for fact in entry['specs']:
        lines.append(f'| {fact["label"]} | {fact["value"].replace("|","/")} | [{fact["source_id"]}]({by_id[fact["source_id"]]["url"]}) |')
    for heading,key in [('Our review','assessment'),('Choose it when','choose_if'),('Skip it when','skip_if'),('Compatibility and limitations','tradeoff'),('Alternatives','alternatives')]:
        lines+=['','## '+heading,'',entry[key]]
    lines+=['','## Setup and firmware route','',f'Use the [model-appropriate installation and recovery guide](../../labs/guides/{workflow(entry)}.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.','', 'The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.','','## First evaluation','',entry['bench_check'],'','Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.','','## Sources read','']
    for ident in entry['source_ids']:
        s=by_id[ident];lines.append(f'- [{s["title"]}]({s["url"]}) — retrieved {s["retrieved_at"][:10]}; SHA-256 `{s["sha256"]}`.')
    lines+=['','[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)','']
    return '\n'.join(lines)


def generated_files():
    catalog,sources=load();entries=catalog['entries'];by_id={s['id']:s for s in sources['sources']}
    files={Path(e['doc']):review_document(e,by_id) for e in entries}
    lines=['# Primary research sources','','Independently retrieved manufacturer and project-maintainer documents. Hashes identify the exact response bytes; mutable pages may change. Original responses are retained in the research workspace rather than republished here.','']
    for s in sources['sources']:
        lines += [f'## {s["id"]}','',f'[{s["title"]}]({s["url"]})','',f'- Retrieved: {s["retrieved_at"]}',f'- Response bytes: {s["bytes"]}',f'- SHA-256: `{s["sha256"]}`','']
    files[Path('hardware/PRIMARY-SOURCES.md')]='\n'.join(lines)
    pending=json.loads((ROOT/'data/reviews/coverage.json').read_text())['pending']
    lines=['# Research coverage','',f'{len(entries)} individual reviews are backed by {len(by_id)} retrieved primary documents. Each reviewed product has its own documentation page. Unverified targets are not counted as reviews.','','## Remaining targets','','These are evidence gaps, not completed reviews. They are not filled using video titles or generic specifications.','','| Product | Evidence still needed |','| --- | --- |']
    lines += [f'| {p["name"]} | {p["reason"]} |' for p in pending if p['name'] not in {e['name'] for e in entries}]
    files[Path('hardware/RESEARCH-COVERAGE.md')]='\n'.join(lines)+'\n'
    begin,end='<!-- TOOL_REVIEWS_START -->','<!-- TOOL_REVIEWS_END -->'
    lines=[begin,'## Research, tools & practical engineering','',f'**{len(entries)} independently researched reviews · {len(by_id)} primary documents · full product pages, firmware routes, walkthroughs and runnable labs.**','','[Review and compare tools](site/reviews.html) · [Practical workbench](site/labs.html) · [Flashing and recovery](labs/FLASHING.md) · [Scripts and tests](labs/SCRIPTS.md) · [Source ledger](hardware/PRIMARY-SOURCES.md)','','Each review contains cited features, our original assessment, choose/skip guidance, compatibility limits and alternatives. Walkthroughs connect tools to concrete tasks and expected results. The existing 150 missions, 180 research dossiers and 150 assessment modules remain intact.','']
    for category in sorted({e['category'] for e in entries}):
        lines += ['### '+category,'','| Product / workflow | Documentation and review |','| --- | --- |']
        for e in sorted((e for e in entries if e['category']==category),key=lambda e:e['name'].casefold()):
            lines.append(f'| [{e["name"]}]({e["doc"]}) | {e["purpose"].replace("|","/")} |')
        lines.append('')
    lines += ['[Research coverage](hardware/RESEARCH-COVERAGE.md) · [Review method](hardware/REVIEW-METHOD.md)','',end]
    readme=(ROOT/'README.md').read_text();start=readme.index(begin);stop=readme.index(end)+len(end)
    files[Path('README.md')]=readme[:start]+'\n'.join(lines)+readme[stop:]
    return files
