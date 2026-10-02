# 14 · Authorized exposure and intelligence governance

**Research status:** proposed governance systems. The listed tools and feeds are potential *authorized inputs*, not instructions to inspect anyone else's systems or personal identifiers. No external target, phone number, IP address, or service has been queried for this chapter.

CISA's [asset-visibility directive](https://www.cisa.gov/news-events/directives/bod-23-01-improving-asset-visibility-and-vulnerability-detection-federal-networks), which applies to federal civilian executive branch systems, motivates accurate ownership and inventory as a design example; NIST's [threat-information-sharing guide](https://csrc.nist.gov/pubs/sp/800/150/final) motivates provenance, scope, and handling rules. The following ideas focus on what an organization is allowed to know about itself, how confidently it knows it, and how evidence becomes remediation.

```mermaid
flowchart LR
    A[Approved scope registry] --> B[Owned inventory and permitted feeds]
    B --> C[Evidence with freshness and provenance]
    C --> D[Ownership and mission relevance]
    D --> E[Reviewed action]
    E --> F[Closure evidence]
    F --> G[Scope-safe metrics]
```

| Governance question | Ideas | Principal output |
|---|---|---|
| What is exposed and for how long? | 131–136 | Scoped inventory and change receipts |
| Which claims and owners are credible? | 137–140 | Evidence graph and reviewed response |

<a id="m131"></a>

## 131 · Owned-Asset Exposure Census

**Thesis.** Reconciliation of an organization's approved inventory with permitted external observations can reveal forgotten owned services. **Proposed system.** A scope registry stores approved domains, ranges, legal owner, data sources, observation dates, and collection limits. Compare internal CMDB/API inventory with licensed or public service metadata, retaining raw-source freshness and confidence. **Evidence and test.** On a synthetic portfolio or explicitly owned assets, measure precision/recall of owner matching, unknown-service review time, and stale-record rate against manual inventory. **Boundary.** The project must never infer authorization from mere internet visibility; do not scan third-party systems. Any Shodan-like source is read only within registered ownership and license terms. Anchors: [CISA BOD 23-01](https://www.cisa.gov/news-events/directives/bod-23-01-improving-asset-visibility-and-vulnerability-detection-federal-networks), [NIST CSF 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20).

<a id="m132"></a>

## 132 · Exposure Half-Life Tracker

**Thesis.** The elapsed time from confirmed exposure to verified closure is a better operational measure than the number of raw findings. **Proposed system.** Each case has discovery, ownership confirmation, risk acceptance or fix decision, remediation, and independent verification timestamps. Model survival curves by exposure class with censored cases, rather than treating open findings as zero-duration. **Evidence and test.** Use a consented internal backlog or synthetic event history; report median and upper-tail closure time, re-open rate, and missing-verification fraction. Compare before and after one workflow intervention. **Boundary.** Closure can mean risk acceptance or mitigation, so labels must distinguish them; fast closure alone cannot prove lower mission risk. Anchors: [CISA BOD 23-01](https://www.cisa.gov/news-events/directives/bod-23-01-improving-asset-visibility-and-vulnerability-detection-federal-networks), [NIST SP 800-55 Vol. 1](https://csrc.nist.gov/pubs/sp/800/55/v1/final).

<a id="m133"></a>

## 133 · External-Signal Confidence Broker

**Thesis.** Requiring corroboration and age checks before action should reduce mistakes caused by a single stale external feed. **Proposed system.** Normalize permitted exposure notices into claims with source, observation time, asset match, confidence, and contradiction links. A policy engine proposes human review when evidence is weak and never treats a vendor score as ground truth. **Evidence and test.** Seed a synthetic feed with outdated, duplicated, and contradictory records; measure false action rate, valid finding retention, review burden, and time to verified closure against a single-feed rule. **Boundary.** Corroboration may be impossible for rare urgent cases, so preserve an exception path with documented uncertainty and scope. Anchors: [NIST SP 800-150](https://csrc.nist.gov/pubs/sp/800/150/final), [CISA BOD 23-01](https://www.cisa.gov/news-events/directives/bod-23-01-improving-asset-visibility-and-vulnerability-detection-federal-networks).

<a id="m134"></a>

## 134 · Identifier Privacy Watch

**Thesis.** An opt-in audit of organizational contact identifiers can find unnecessary public disclosure while minimizing the audit's own privacy impact. **Proposed system.** Collect only consented, organization-owned identifiers, stated purpose, approved public use, observation source, retention limit, and an owner review decision. Report categories and remediation paths without publishing identifiers. **Evidence and test.** On synthetic examples and a voluntary pilot, measure accurate exposure classification, false personal-identifier matches, and deletion compliance. **Boundary.** No collection of third-party phone numbers or profiling of individuals. Phone-lookup tools are not necessary to demonstrate this concept, and their output cannot establish consent or identity. Anchors: [NIST Privacy Framework](https://www.nist.gov/privacy-framework), [NIST SP 800-150](https://csrc.nist.gov/pubs/sp/800/150/final).

<a id="m135"></a>

## 135 · Vulnerability-to-Mission Relevance

**Thesis.** A vulnerability's priority should reflect deployed exposure and mission dependency in addition to advisory severity. **Proposed system.** Join approved asset inventory, installed component/version evidence, reachability class, compensating controls, business function, and authoritative advisory metadata. A transparent score shows missing evidence and produces a review queue, not an automatic patch command. **Evidence and test.** Compare prioritization against expert review on a synthetic fleet; measure top-k recall of mission-critical cases, analyst time, and sensitivity to missing inventory. **Boundary.** Catalog presence and software-version matching do not prove exploitability on a specific system. Use CISA's exploited-vulnerability information as one input among others. Anchors: [CISA KEV catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog), [NIST SP 800-40 Rev. 4](https://csrc.nist.gov/pubs/sp/800/40/r4/final).

<a id="m136"></a>

## 136 · Internet-Facing Change Receipt

**Thesis.** Linking an approved change to a later observed exposure state should make unexpected internet-facing drift easier to resolve. **Proposed system.** Issue a signed receipt with asset owner, change ticket, intended public endpoint, configuration hash, window, and rollback plan. After deployment, reconcile approved inventory and permitted external metadata; retain mismatches for human review. **Evidence and test.** In a lab with synthetic service changes, measure unmatched-exposure detection, false alerts for planned changes, and time to identify the responsible change. **Boundary.** The design cannot assume immediate feed freshness or that absence in an external index means absence on the internet. It operates only over registered owned assets. Anchors: [CISA BOD 23-01](https://www.cisa.gov/news-events/directives/bod-23-01-improving-asset-visibility-and-vulnerability-detection-federal-networks), [NIST CSF 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20).

<a id="m137"></a>

## 137 · Threat-Intel Contradiction Graph

**Thesis.** Connecting intelligence claims to evidence and to contradicting claims should expose weak conclusions before they shape defense. **Proposed system.** Represent each claim with source, date, handling restriction, confidence rationale, supporting observations, and counterevidence. The graph highlights stale, circular, and unsupported claims for analyst review. **Evidence and test.** Build a synthetic intelligence corpus with planted contradictions; measure contradiction recall, analyst agreement, and the rate of unsupported recommendations compared with unstructured notes. **Boundary.** The graph cannot infer an adversary's identity from sparse indicators; confidence is conditional on source access and reporting bias. Follow sharing agreements and minimize personal data. Anchors: [NIST SP 800-150](https://csrc.nist.gov/pubs/sp/800/150/final), [NIST SP 800-55 Vol. 1](https://csrc.nist.gov/pubs/sp/800/55/v1/final).

<a id="m138"></a>

## 138 · Exposure-to-Owner Resolver

**Thesis.** An explainable owner-matching model can reduce orphaned remediation tasks without silently assigning responsibility to the wrong team. **Proposed system.** Join approved domain/asset registries, infrastructure-as-code ownership, service tags, certificate records, and change history. Output top candidate owners, evidence links, and abstention when confidence is low. **Evidence and test.** On a synthetic fleet and consented historical cases, score top-1 owner accuracy, abstention calibration, and median triage delay relative to manual routing. **Boundary.** Ownership changes and shared services make labels ambiguous; sensitive administrator identities should not be exposed in the output. Never claim ownership of a third-party service from a superficial hostname match. Anchors: [CISA BOD 23-01](https://www.cisa.gov/news-events/directives/bod-23-01-improving-asset-visibility-and-vulnerability-detection-federal-networks), [NIST CSF 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20).

<a id="m139"></a>

## 139 · Responsible Disclosure Workflow Twin

**Thesis.** Rehearsing vulnerability-report intake and escalation should reveal preventable delay before a real report arrives. **Proposed system.** A process simulator models report receipt, acknowledgment, validity review, owner assignment, remediation decision, disclosure coordination, and closure communication. Synthetic reports vary ambiguity, product ownership, and reporting channel. **Evidence and test.** Compare time to acknowledgment, unresolved handoffs, quality of status updates, and fair treatment of reporters across the current and revised workflow. **Boundary.** This is process design, not a vulnerability-finding or exploitation exercise; real disclosure requires policy, legal review, and safe communication. Anchors: [NIST SP 800-216](https://csrc.nist.gov/pubs/sp/800/216/final), [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final).

<a id="m140"></a>

## 140 · Owned-Decoy Value Study

**Thesis.** A narrowly scoped, isolated decoy may provide useful early-warning evidence, but its value should be measured against cost and privacy exposure. **Proposed system.** Deploy only within an approved test network or owned address space with no production privileges; record aggregate interaction counts, alert routing, maintenance cost, and data retention. **Evidence and test.** Compare detection time and false analyst effort in a synthetic exercise with and without the decoy. Include a privacy review of accidental third-party data capture and a shutdown procedure. **Boundary.** No lure distribution, third-party monitoring, attribution claims, or instructions for offensive deception. Unsolicited real traffic is not a controlled outcome and must be handled under organizational policy. Anchors: [NIST SP 800-150](https://csrc.nist.gov/pubs/sp/800/150/final), [NIST Privacy Framework](https://www.nist.gov/privacy-framework).
