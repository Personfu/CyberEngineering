"""Deterministically build 150 authorized-assessment modules and evidence-bounded cards."""
import argparse,json
from pathlib import Path
R=Path(__file__).resolve().parents[1]

def read(p):return json.loads((R/p).read_text())

SPECS={
1:('Boundary and knowledge correctness','coverage = witnessed required decisions / declared required decisions','A labeled fictional record; no system or account access','Unlabeled informal review','A missing owner, ambiguous timestamp, or necessary field absent','Explain one invalid inference; give an observation that would make it valid'),
2:('Scope, evidence and decision quality','supported_fraction = evidence_bound_findings / reviewed_findings','A fictional scope and signed-by-role paper decision record','Ordinary narrative engagement notes','Expired authority, missing recovery witness, or collection beyond the declared endpoint','Specify the independent reviewer and a reversible closure proof'),
3:('Policy and state correctness','error = false_allow + cost_ratio * false_deny; unknown tracked separately','Synthetic requests/configuration and expected policy labels','A static documented policy or simple reference interpreter','Concurrent revocation, stale metadata, missing grant, or changed legitimate task','Distinguish reachable invariant failure, bounded model truth and implementation conformance'),
4:('Detection and intelligence evidence quality','precision = TP/(TP+FP); unsupported_claim_rate = unsupported/total','Public-source claim receipts or harmless synthetic telemetry','Single-source or frozen simple rule with the same evidence budget','Benign maintenance, lost sensor blocks, alias collision, or delayed labels','Test source independence, realistic prevalence, calibration and rival attribution'),
5:('Mission consequence and recoverability','L = sum_f w_f integral [1-q_f(t)] dt','Offline fictional mission states and harmless scenario timelines','Feasible existing recovery or static control assumptions','Common cause, unavailable operator, contact loss, or unknown physical state','Define demand, units, independent scenario and hard safety prerequisites'),
6:('Identifiability, uncertainty and external validity','effect = E[Y(1)-Y(0)] only under defended identification assumptions','Preregistered synthetic/public/owned fixture with provenance','A credible resource-matched simpler estimator or mechanism','Nonrandom missingness, confounding, dependence, or an untouched environment','Derive assumptions, quantify uncertainty, preregister falsifier and document a negative result')}

def render():
 x=read('data/assessment/modules.json');items=x['modules']
 if len(items)!=150 or [m['id'] for m in items]!=[f'RT{i:03d}' for i in range(1,151)]:raise ValueError('assessment catalog order')
 missions={m['id'] for m in read('data/ideas.json')['ideas']}
 if len({m['title'].casefold() for m in items})!=150:raise ValueError('duplicate module title')
 out={};index=['# HELIOS Red-Team Assessment Flightbook','',
 '150 distinct modules progress from fundamentals to graduate assessment research. This companion track preserves the original 150 missions and the 30 frontier proposals. The RT identifiers denote assessment modules, not an extra 150 completed products.','',
 '[Beginner IT, Kali and tool tutorials](../foundations/README.md) · [Engagement and evaluation protocol](PROTOCOL.md) · [Graduate research](../research/README.md) · [Public intelligence cards](../intelligence/README.md) · [Applicable datasets](../research/RESOURCES.md)','',
 '| Phase | NASA orbit | Modules | Focus |','|---|---|---|---|']
 for p in x['phases']:index.append(f"| {p['number']} | {p['orbit']} | RT{(p['number']-1)*25+1:03d}–RT{p['number']*25:03d} | {p['title']} |")
 for p in x['phases']:
  index += ['',f"## {p['orbit']} · {p['title']}",'','| Module | Engineering question |','|---|---|']
  for m in [m for m in items if m['phase']==p['number']]:
   if m['related_mission'] not in missions:raise ValueError('mission reference')
   focus,equation,data,baseline,stress,graduate=SPECS[m['phase']]
   s=f"""# {m['id']} · {m['title']}

**Status:** Proposed authorized assessment research. **Phase:** {p['title']}.

## Distinct idea and mission question

{m['question']}

Build **{m['artifact']}**. This is the primary review artifact; its value is whether an independent analyst can answer the stated question with less unsupported inference and an equal observation/resource budget. Connect the work to [{m['related_mission']} in the preserved research catalog](../../research/missions/{m['related_mission']}.md).

## State and evidence model

Focus: {focus}. A candidate model is:

```text
{equation}
```

This author-proposed model is illustrative, not a reported result or a standards requirement. Define all variables, units, denominators, unknown states and applicability. If the equation does not fit the artifact, derive the appropriate mission-specific endpoint before implementing a test.

**Data contract:** {data}. Bind input ID, revision/hash, event and retrieval time, label basis, coverage and missingness. The unique required content is the artifact specified above; the general schema does not claim that an external dataset already contains it. Consult the [resource ledger](../../research/RESOURCES.md) before importing any data.

## Red-blue-white evaluation

The red cell constructs a paper or harmless fixture-backed hypothesis for this question. The blue cell reviews the resulting observations without hidden truth labels. The white cell maintains scope and adjudicates against the frozen fixture. Use **{baseline.lower()}** as a candidate comparator, then justify its suitability for this module. Match access, information, tuning and personnel-hours.

**Adverse challenge:** {stress}. Choose the case that can actually discriminate this idea, and state why. Include a null scenario in which the artifact should not change the decision. Report errors, unknowns, reviewer disagreement, observation gaps and cost; numerical acceptance floors require design review before final testing.

## Graduate extension and falsifier

{graduate}. The thesis fails if its supported decision quality does not improve against the comparator on an untouched scenario/partition, if the artifact depends on an unavailable observation, or if a declared permission/safety constraint fails. Explain which conclusion cannot transfer to another environment. Distinguish fixture correctness from field effectiveness and implementation work from scientific novelty.

## Deliverables and resources

Deliver the concrete artifact named above, a typed fixture contract, a baseline, expected/observed results, a limitation ledger and an independent review record. Start with local Markdown/JSON, Python's standard library and the existing offline mechanics; add a model checker or consented tabletop only when justified. These are specifications, not executed assessments. No live target, exploit reproduction, credential collection or protective-control bypass is supplied.

[Assessment protocol and primary planning references](../PROTOCOL.md) · [All 150 modules](../README.md)
"""
   out[R/f'assessment/modules/{m["id"]}.md']=s
   index.append(f"| [{m['id']} · {m['title']}](modules/{m['id']}.md) | {m['question']} |")
 out[R/'assessment/README.md']='\n'.join(index)+'\n'
 sources={s['id']:s for s in read('data/intelligence/sources.json')};claims={c['id']:c for c in read('data/intelligence/claims.json')};profiles=read('data/intelligence/profiles.json')
 ledger=['# Public intelligence and research-persona cards','',
 'Eight source-bounded cards separate government-described threat clusters, a research persona, a self-described community and public homepage bylines. No real identity or criminal role is inferred from a handle.','',
 '[Claim method](METHOD.md) · [Source ledger](../data/intelligence/sources.json) · [Claim records](../data/intelligence/claims.json) · [Assessment track](../assessment/README.md)','',
 '| Entity | Type | Evidence records |','|---|---|---|']
 for p in profiles:
  card=f"# {p['display_name']}\n\n**Entity type:** {p['entity_type']}. **Review date:** 2026-10-02.\n\n## Claim receipts\n\n"
  for cid in p['claim_ids']:
   c=claims[cid];src=sources[c['source_id']]
   card+=f"**{cid}:** {c['claim']}\n\nEvidence class: {c['evidence_type']}. Source: [{src['publisher']} — {src['title']}]({src['url']}). Publication date: {src['publication_date'] or 'unknown/not established'}; retrieved: {src['retrieved_date']}.\n\nLimitation: {c['limitation']}\n\n"
  card+=f"## Attribution boundary\n\n{p['uncertainty']}\n\n## Assessment research question\n\n{p['assessment_question']}\n\nThis is a proposed question, not a finding about the named entity. Use synthetic or consented fixtures under the [assessment protocol](../../assessment/PROTOCOL.md). No hosted tools were acquired or run.\n\n[Evidence method](../METHOD.md) · [Card index](../README.md)\n"
  out[R/f'intelligence/profiles/{p["slug"]}.md']=card
  ledger.append(f"| [{p['display_name']}](profiles/{p['slug']}.md) | {p['entity_type']} | {', '.join(p['claim_ids'])} |")
 ledger+=['','## Provenance limits','', 'The six-source registry records first-party investigation reporting, official vulnerability/catalog metadata, a joint government advisory, an FBI statement and a self-published homepage. Eleven narrow claims retain their source and limitation. Historical report conditions are not current endpoint state. Community membership, nonprofit registration, real identities, complete malware capability and intrusion attribution were not independently established.','', 'The four homepage handles are documented only as public bylines or attributions; they are not labeled threat actors. The Nightmare-Eclipse and Church of Malware cards remain distinct and do not assert a verified membership relationship.']
 ledger += ['', '[Public forge source review: user-selected Explore listing and 50 bounded metadata records](CHURCH-FORGE.md) · [Beginner tool explanations and actual screenshots](../foundations/README.md)']
 out[R/'intelligence/README.md']='\n'.join(ledger)+'\n'
 return out

def main():
 p=argparse.ArgumentParser();p.add_argument('--check',action='store_true');a=p.parse_args()
 for path,s in render().items():
  if a.check:
   if not path.exists() or path.read_text()!=s:raise SystemExit('Stale output: '+str(path.relative_to(R)))
  else:path.parent.mkdir(parents=True,exist_ok=True);path.write_text(s)
 print('Verified 150 staged assessment modules, eight typed intelligence cards and eleven source-bounded claims.')
if __name__=='__main__':main()
