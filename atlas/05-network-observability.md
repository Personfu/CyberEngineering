# 05 · Network Observability

**Research status:** proposed concepts and evaluation designs. These projects use network metadata to answer operational questions about owned services: what talks to what, how sure we are, and what response preserves mission service. Collection plans begin with authorization, retention limits, and privacy review. No packet capture supplied with this project is assumed safe to publish or representative of a real environment.

| Evidence plane | Minimum useful observation | Typical uncertainty |
|---|---|---|
| Flow | Endpoints, protocol, volume, time | Shared addresses and sampling |
| Control | Approved route, policy, DNS change | Intent may lag actual deployment |
| Service | Owner, function, identity | Inventory can be stale |
| Time | Clock offset and drift estimate | Events may reorder within error bars |

<a id="m041"></a>

## 041 · Packet-to-Service Atlas

**Hypothesis.** Fusing flow records with service inventories explains unknown traffic without payload inspection. **Design.** Link IPFIX-like flow tuples to authorized CMDB entries, workload identities, DNS names, and change tickets. Score a flow's likely service owner with explicit evidence weights and an “unknown” outcome when identifiers disagree. **Evidence.** Use an owned lab network or privacy-reviewed aggregate flow records; synthetic services exercise address reuse and NAT. **Test.** Compare correct owner attribution, unknown-rate, and analyst minutes per unexplained flow with an address-only baseline. **Boundary.** Flow metadata can still reveal sensitive behavior; minimize fields, retention, and access, and never attribute a person from a shared network endpoint. Sources: [IETF IPFIX RFC 7011](https://www.rfc-editor.org/info/rfc7011/), [NIST SP 800-215](https://csrc.nist.gov/pubs/sp/800/215/final).

<a id="m042"></a>

## 042 · Privacy-Preserving Flow Lens

**Hypothesis.** Coarse traffic features retain incident utility while limiting sensitive-content collection. **Design.** Compare several feature sets—full flow records, bucketed volumes, service-level aggregates, and rotating pseudonyms—under a fixed retention window. Measure incident-classification utility and re-identification risk separately; avoid collecting payloads. **Evidence.** Generate synthetic enterprise service traces or use consented, approved operational metadata with documented governance. **Test.** Report detection precision-recall and reconstruction risk for each feature tier, then select a Pareto point under predeclared privacy limits. **Boundary.** Hashing alone is not de-identification, and aggregated traffic may still expose rare users; require disclosure review before sharing datasets. Sources: [IETF Network Telemetry Framework RFC 9232](https://www.rfc-editor.org/info/rfc9232/), [NIST SP 800-188 de-identification](https://csrc.nist.gov/pubs/sp/800/188/final).

<a id="m043"></a>

## 043 · Clock-Coherence Monitor

**Hypothesis.** Time-offset estimates improve cross-device event ordering and forensic confidence in enterprise telemetry. **Design.** For packet sensors, gateways, DNS servers, and service logs, estimate offset, drift, and uncertainty against an authenticated time reference; store event time as an interval. A correlator refuses to order two enterprise events whose uncertainty intervals overlap unless protocol sequence evidence resolves them. **Evidence.** Use an owned test network with synthetic transactions and intentionally skewed sensors; do not alter production time sources. **Test.** Compare event-order error, correctly unresolved event pairs, and false causal links with and without correction. **Boundary.** Clock coherence does not establish causation; untrusted time sources or missing health checks must widen uncertainty. Sources: [IETF Network Time Security RFC 8915](https://www.rfc-editor.org/info/rfc8915/), [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final).

<a id="m044"></a>

## 044 · Control-Plane Change Witness

**Hypothesis.** Tracking intended versus observed routing and configuration changes surfaces hidden connectivity drift. **Design.** Store approved network intent as versioned route, ACL, DNS, and segmentation constraints. Compare it with observed control-plane state and limited reachability checks; relate each difference to a change record and owner. **Evidence.** Use a simulated topology or authorized configuration exports, avoiding credentials and raw proprietary configs in published examples. **Test.** Seed accidental route leaks and stale ACLs; measure time to detect, false differences caused by normal convergence, and missed affected services. **Boundary.** Observation gaps can mimic compliance; report collection freshness and require operators to review before any corrective action. Sources: [NIST SP 800-215](https://csrc.nist.gov/pubs/sp/800/215/final), [IETF NETCONF RFC 6241](https://www.rfc-editor.org/info/rfc6241/).

<a id="m045"></a>

## 045 · Weak-Signal Correlator

**Hypothesis.** Combining several low-confidence benign indicators reduces false positives at a fixed detection rate. **Design.** Fuse service ownership mismatch, rare flow direction, clock-adjusted event order, and change-context features in a calibrated model. Require multiple independent evidentiary paths before escalating; preserve explanations and abstain when coverage is weak. **Evidence.** Build from synthetic incident exercises and approved aggregate telemetry, with privacy-reviewed labels. **Test.** On a held-out dataset, compare false alerts per week at a fixed recall with single-rule baselines and report calibration error. **Boundary.** Correlated sensors can make evidence look independent; document dependencies and prohibit automatic punitive action from model scores alone. Sources: [IETF RFC 9232 telemetry framework](https://www.rfc-editor.org/info/rfc9232/), [NIST SP 800-61 Rev. 3 incident response](https://csrc.nist.gov/pubs/sp/800/61/r3/final).

<a id="m046"></a>

## 046 · Capture Sufficiency Planner

**Hypothesis.** Modeling sensor placement reveals evidence blind spots before an incident. **Design.** Represent the network as a graph of observation points, encrypted tunnels, NAT boundaries, and mission-critical paths. Solve a constrained placement problem that maximizes question-answering coverage per cost, storage, and privacy budget. **Evidence.** Use synthetic topologies or approved network diagrams; model flow metadata only unless a separate lawful capture plan exists. **Test.** Hide a set of simulated incidents and ask whether available sensors can distinguish their candidate causes; report answerable-case fraction and marginal sensor value. **Boundary.** More collection is not automatically better; retention and collection scope must be justified by a specific operational question. Sources: [IETF RFC 9232](https://www.rfc-editor.org/info/rfc9232/), [NIST Privacy Framework](https://www.nist.gov/privacy-framework).

<a id="m047"></a>

## 047 · Adaptive Baseline with Change Memory

**Hypothesis.** Separating planned change from anomalies lowers alert churn during deployments. **Design.** Maintain a baseline conditioned on service owner, deployment version, maintenance window, and approved change record. Use a robust update rule so an unexplained burst cannot immediately become the new normal; keep the previous baseline available for rollback. **Evidence.** Use synthetic traffic plus an owned deployment calendar, or sanitized operational data with explicit access approval. **Test.** Compare false alerts per planned deployment and detection recall for seeded unexplained changes against an unconditioned baseline. **Boundary.** A change ticket is contextual evidence, not a blanket allowlist; significant deviations still require review. Sources: [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), [IETF RFC 9232](https://www.rfc-editor.org/info/rfc9232/).

<a id="m048"></a>

## 048 · Segmentation Proof Harness

**Hypothesis.** Authorized reachability tests verify that network policies match documented trust boundaries. **Design.** Turn a reviewed policy matrix into harmless connection probes between controlled endpoints, plus static route and ACL analysis. Record permitted, denied, and unobserved paths with timestamps and configuration hashes. **Evidence.** Run only inside owned or explicitly authorized networks at agreed rates; use simulated topology for public demonstrations. **Test.** Seed unintended paths and compare detected policy violations and false alarms with configuration review alone. **Boundary.** A successful TCP handshake does not prove application authorization, and absent reachability may reflect transient faults; recheck before changing policy. Sources: [NIST SP 800-207 Zero Trust](https://csrc.nist.gov/pubs/sp/800/207/final), [NIST SP 800-215](https://csrc.nist.gov/pubs/sp/800/215/final).

<a id="m049"></a>

## 049 · Name-to-Destination Integrity Map

**Hypothesis.** DNS, inventory, and service ownership reconciliation catches stale or misrouted dependencies. **Design.** Compare expected service names, DNS records, certificate identity, resolved destinations, and owner records across environments. Mark relationships as consistent, explainable migration, or unresolved drift; account for load balancers and short-lived addresses. **Evidence.** Use owned DNS zones and synthetic service identities; do not scan third-party networks. **Test.** Seed stale aliases, expired owners, and wrong environment bindings, then measure detection recall and false alarms under normal failover. **Boundary.** DNSSEC proves record origin under a valid trust chain, not that the destination is operationally correct; owner evidence remains essential. Sources: [IETF DNSSEC RFC 4035](https://www.rfc-editor.org/info/rfc4035/), [NIST SP 800-215](https://csrc.nist.gov/pubs/sp/800/215/final).

<a id="m050"></a>

## 050 · Containment Cost Simulator

**Hypothesis.** Simulating network containment consequences improves route and segmentation choices during response. **Design.** Apply candidate ACL, route, or segment changes to a service-and-flow graph; estimate which approved communications would be lost, which suspicious paths remain reachable, and how convergence time affects essential traffic. Present only actions an authorized network operator can review and roll back. **Evidence.** Use tabletop incidents, synthetic flow records, and a virtual topology; never execute network changes from the simulator. **Test.** Compare predicted lost service-minutes and residual reachability with measured simulator outcomes, then compare operator decisions against unmodeled network isolation. **Boundary.** Flow records omit application semantics and transient paths; the model is advisory and must preserve emergency communications and human change authority. Sources: [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), [NIST SP 800-215 secure enterprise networks](https://csrc.nist.gov/pubs/sp/800/215/final).
