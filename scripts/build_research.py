"""Generate deeper dossiers and a separate 180-mission research catalog.

The original 150-mission catalog and reading order remain authoritative and intact.
"""
import argparse
import html
import json
import re
from pathlib import Path
import sys

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import build_atlas


def load(name):return json.loads((ROOT/'data/research'/name).read_text())


def source_lines(urls):return '\n'.join(f'- [{url}]({url})' for url in sorted(set(urls)))


def render():
    _,old=build_atlas.parse()
    profiles=load('domain_specs.json');frontier=load('frontier.json');resources=load('resources.json')
    resource_map={r['id']:r for r in resources}
    if len(profiles)!=15 or len(frontier)!=30 or len(old)!=150:raise ValueError('unexpected portfolio shape')
    if [x['id'] for x in frontier]!=[f'{i:03d}' for i in range(151,181)]:raise ValueError('frontier order')
    titles=[x['title'].casefold() for x in old+frontier]
    if len(set(titles))!=180:raise ValueError('title collision')
    out={};catalog=[];index=['# HELIOS Research Flightbook · all 180 missions','',
        'All 150 original missions retain their identifiers and titles. Thirty new NASA-inspired missions extend the portfolio. Dossiers are research specifications; six separate experiments demonstrate reference mechanics using synthetic data.','',
        '[Protocol](METHOD.md) · [Datasets and resource contracts](RESOURCES.md) · [Executable experiments](EXPERIMENTS.md) · [Graduate qualifying challenges](CHALLENGES.md) · [Validation record](VALIDATION.md)','',
        '| Domain | Original missions | New missions | Research model |','|---|---|---|---|']
    for profile in profiles:
        n=profile['number'];subset=[i for i in old if i['chapter']==n];new=[i for i in frontier if i['chapter']==n]
        resource=resource_map[profile['dataset']]
        rp='experiments/benchmark.py' if resource['id']=='SYNTHETIC' else resource['url']
        dataset_link='../../'+rp if resource['id']=='SYNTHETIC' else rp
        domainpath=f'research/domains/{n:02d}.md'
        sources=sorted(set(u for i in subset for u in i['source_urls']))
        index.append(f"| {n:02d} · {profile['domain']} | {subset[0]['id']}–{subset[-1]['id']} | {new[0]['id']}–{new[-1]['id']} | [{profile['codename']}](domains/{n:02d}.md) |")
        domain=f"""# {profile['codename']} · {profile['domain']}

**Evidence:** Proposed domain research framework. The equations below are author-defined candidate models, not measured findings or requirements quoted from standards.

**Research focus:** {profile['research_focus']}.

## Governing model

```text
{profile['equation']}
```

{profile['interpretation']}

**Competing models:** {profile['baselines']}.

**Required record schema:** {profile['schema']}. Extend the schema with provenance digest, units, coverage window, collection permission, missingness reason and transformation revision. Use explicit null values for missing observations; do not turn missing into zero.

## Evaluation contract

Measure {profile['metrics']}. Freeze a mission-specific primary endpoint and acceptable resource cost before tuning. Compare the candidate and baseline on the same scenario/partition. Include a no-intervention or null fixture to detect accidental leakage. Report uncertainty at the independent unit—scenario, channel, device or team—and analyze the worst-performing subgroup rather than relying on a portfolio average.

**Adverse cases:** {profile['stress_tests']}.

**Graduate challenges:** {profile['graduate_challenges']}. For each challenge, distinguish a limitation of the estimator from a limitation of available evidence. Ask whether the parameter is identifiable, whether the mechanism transfers to a new environment and which observation could distinguish rival explanations.

**Resource plan:** {profile['resources']}. Before implementation, produce a concrete bill of materials, input size, memory/storage estimate, runtime bound and personnel-hours estimate. No universal cost or readiness claim is made here.

## Applicable data and its limits

[{resource['title']}]({dataset_link}). {resource['applicability']}. {resource['limitations']} Resource budget: {resource['resource_budget']}. Current status: {resource['inspection']}. Access/rights: {resource['rights']}.

## Research trace

"""
        domain+='\n'.join(f"- [{i['id']} · {i['title']}](../{'missions' if i in subset else 'frontier'}/{i['id']}.md)" for i in subset+new)
        domain+='\n\n## Primary design references\n\n'+source_lines(sources)+'\n\n[Shared evaluation protocol](../METHOD.md) · [Resource ledger](../RESOURCES.md)\n'
        out[ROOT/domainpath]=domain
        for item in subset:
            text=(ROOT/item['path']).read_text()
            match=re.search(rf'(?ms)^## {item["id"]} · .*?\n(.*?)(?=\n<a id="m\d{{3}}"></a>|\Z)',text)
            if not match:raise ValueError('missing original section')
            original=match.group(1).strip()
            # Add a durable link to the shared domain model and keep original mechanism intact.
            dossier=f"""# {item['id']} · {item['title']}

**Status:** Proposed research mission; no field effectiveness established. **Research orbit:** {profile['codename']}.

[Original proposal](../../{item['path']}#{item['anchor']}) · [Domain model](../domains/{n:02d}.md) · [Protocol](../METHOD.md)

## Preserved thesis and mechanism

{original}

## Expanded experiment specification

Treat the statement “{item['thesis']}” as a hypothesis with a comparator and a population, not as a demonstrated benefit. Implement the precise mechanism described above; preserve the original evidence boundary and endpoint. Use the domain model to state variables and units, but justify which assumptions apply to this particular mechanism rather than copying the model mechanically.

**Observation contract:** collect only the fields needed to estimate this mission's endpoint. Candidate domain fields are {profile['schema']}. Bind every record to source/version, valid-time interval, missingness reason and a fixture or collection permission. The domain resource is {resource['title']}; its applicability is a candidate starting point, not an assertion that every field required by this mission exists there. When fields or labels are absent, design a synthetic or owned-system fixture and report the gap.

**Baseline and falsification:** use the original comparison stated above and at least one applicable simple baseline from {profile['baselines']}. Match information, tuning, observation and resource budgets. Define an absolute acceptance floor and minimum meaningful improvement before collecting the final test results. Reject the thesis if the benefit disappears on an untouched partition, if the resource-normalized baseline dominates it or if a declared invariant fails. Choose numerical floors with the mission owner; this dossier does not invent measured thresholds.

**Adverse-case matrix:** {profile['stress_tests']}. Choose the cases relevant to this mechanism and explain any exclusion. Add a negative control in which the intervention should have no effect. Preserve ambiguous outcomes instead of assigning unsupported truth labels.

**Graduate investigation:** {profile['graduate_challenges']}. Write a rival explanation for any apparent improvement; identify the smallest additional observation that distinguishes it from the proposed mechanism. Perform a sensitivity analysis over uncertain assumptions and a leave-one-environment/scenario-out evaluation. A performance difference within a synthetic fixture establishes only behavior of that fixture.

**Review artifacts:** model/assumption ledger; versioned input contract; baseline implementation; preregistered endpoint; adverse-case results with uncertainty; resource-use record; negative findings; independent review notes. The practical starting budget is {profile['resources']}. Independent reviewer sign-off remains pending.

[Domain references and data caveats](../domains/{n:02d}.md) · [Applicable resource ledger](../RESOURCES.md)
"""
            path=f'research/missions/{item["id"]}.md';out[ROOT/path]=dossier
            catalog.append(dict(item,research_path=path,orbit=profile['codename'],domain_spec=domainpath,resource_id=profile['dataset'],evidence_class='Proposed'))
        for item in new:
            refs=sources[:2]+([resource['url']] if resource['id']!='SYNTHETIC' else [])
            dossier=f"""# {item['id']} · {item['title']}

**Evidence class:** Proposed. No operational benefit or complete implementation is claimed. **Domain:** {profile['domain']}.

## Thesis

{item['hypothesis']}

## Model and mechanism

{item['model']}

Record variables, units and validity limits in a typed schema. Start from the [domain specification](../domains/{n:02d}.md), while keeping this mission's distinct mechanism and endpoint. Separate observable variables from latent assumptions; explain which parameters can actually be estimated from the data. Models are original proposals rather than formulas attributed to the references.

## Experiment and applicable data

{item['experiment']}

Candidate resource: {resource_map[item['dataset']]['title']}. Follow its exact [acquisition and rights contract](../RESOURCES.md). Data not acquired in this extension cannot be described as a measured result. Establish at least one simple baseline and equalize its information/tuning budget. Use independent time, entity, artifact, team or scenario partitions; preregister the primary endpoint before final evaluation.

## Challenges and rival explanations

{item['challenges']}

A successful graduate study must test a rival explanation and a null control, quantify parameter sensitivity and document a failure outside the original environment. Report operating cost, missing observations and uncertainty at the independent unit. Distinguish a small-model correctness result from full-system assurance.

## Falsifier

{item['falsifier']}

## Delivery and resources

{profile['resources']}. Deliver a reference state/schema, a pinned lawful fixture, baseline code, held-out results, a resource ledger and an independent review record. Numerical performance floors and compute ceilings are proposed by the accountable mission owner at design review; no budget or readiness level is invented here.

## Primary references and their role

These sources ground engineering context, data provenance or design constraints; they do not establish this thesis or endorse the project.

{source_lines(refs)}

[Graduate protocol](../METHOD.md) · [All missions](../README.md)
"""
            path=f'research/frontier/{item["id"]}.md';out[ROOT/path]=dossier
            catalog.append(dict(item,research_path=path,orbit=profile['codename'],domain_spec=domainpath,resource_id=item['dataset'],evidence_class='Proposed',source_urls=refs))
    catalog.sort(key=lambda x:x['id'])
    if [i['id'] for i in catalog]!=[f'{i:03d}' for i in range(1,181)]:raise ValueError('catalog IDs')
    out[ROOT/'data/research/catalog.json']=json.dumps({'project':'HELIOS Research Flightbook','count':180,'original_count':150,'new_count':30,'evidence':'180 proposed missions; six separately tested mechanics; one observed metadata snapshot','missions':catalog},indent=2,ensure_ascii=False)+'\n'
    index+=['','## Full mission register','','| ID | Mission | Orbit |','|---|---|---|']
    for i in catalog:index.append(f"| {i['id']} | [{i['title']}]({'missions' if int(i['id'])<=150 else 'frontier'}/{i['id']}.md) | {i['orbit']} |")
    out[ROOT/'research/README.md']='\n'.join(index)+'\n'
    ledger=['# Applicable datasets and engineering resources','','Reviewed 2026-10-02. Only the filtered, version-pinned KEV metadata was acquired from an external source. Six local benchmark fixtures are generated synthetically. Other entries are acquisition plans or design resources, not downloaded or validated training datasets.','','[Machine-readable ledger](../data/research/resources.json) · [KEV snapshot](../data/research/kev_snapshot.json) · [Protocol](METHOD.md)','']
    for r in resources:
        url='../experiments/benchmark.py' if r['id']=='SYNTHETIC' else r['url']
        ledger+=[f"## {r['id']} · {r['title']}",'',f"[Primary resource]({url})",'',f"**Evidence and acquisition:** {r['evidence']}.",f"**Applicable question:** {r['applicability']}.",f"**Fields:** {r['schema']}.",f"**Evaluation hazards:** {r['limitations']}",f"**Resources:** {r['resource_budget']}.",f"**Rights:** {r['rights']}.",f"**Inspection:** {r['inspection']}.",'']
    ledger+=['## Acquisition record','','For any future imported dataset, retain the exact URL/DOI, immutable revision or object ID, source hash, UTC acquisition time, declared rights, collection window, schema, units, missingness and label semantics. Never submit contact information or agree to additional terms merely to complete this ledger. Respect gated access; use a documented synthetic fixture while data access is pending.','','The KEV projection keeps five metadata fields and deliberately excludes descriptions, remediation prose and external links. Its source SHA-256 binds the full upstream input; the retained subset has its own repository identity. Descriptive aggregates count catalog entries and addition dates, not attacks or exploitation rates.']
    out[ROOT/'research/RESOURCES.md']='\n'.join(ledger)+'\n'
    return out


def main():
    ap=argparse.ArgumentParser();ap.add_argument('--check',action='store_true');args=ap.parse_args()
    for p,s in render().items():
        if args.check:
            if not p.exists() or p.read_text()!=s:raise SystemExit(f'Stale research output: {p.relative_to(ROOT)}')
        else:p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s)
    print('Verified 180 research dossiers, 15 domain models, 11 resource contracts and preserved 150 original missions.')

if __name__=='__main__':main()
