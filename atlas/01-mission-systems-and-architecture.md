# 01 · Mission Systems & Architecture

**Research status:** proposed concepts and evaluation designs. No operational results are claimed. This chapter treats security as a property of a mission: an essential function may depend on people, power, software, suppliers, and procedures at once. The candidate systems below make those dependencies, assumptions, and tradeoffs inspectable. Experiments belong in synthetic environments or systems the evaluator owns or is expressly authorized to assess.

```mermaid
flowchart LR
    G[Mission goal] --> F[Essential function]
    F --> D[Dependencies and trust boundaries]
    D --> C[Controls and evidence]
    C --> V[Measured mission outcome]
    V --> G
```

<a id="m001"></a>

## 001 · Function-First Risk Atlas

**Hypothesis.** Mapping mission functions to dependencies predicts outage consequence better than asset criticality labels. **Design.** Build a typed graph with functions, service dependencies, recovery paths, control owners, and confidence intervals on each edge. Estimate consequence as the expected fraction of mission demand unmet over time, not a single asset score. **Evidence.** Start with an authorized service inventory and dependency interviews; synthesize failures rather than interrupt production. **Test.** Compare graph predictions against tabletop adjudications and historical outage timelines using rank correlation and calibrated prediction intervals. A useful prototype must outperform a blinded asset-tier baseline across held-out scenarios. **Boundary.** Unknown dependencies remain explicit and enlarge uncertainty; the atlas must not imply that a diagram is complete. Sources: [NIST CSF 2.0](https://www.nist.gov/cyberframework), [NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final).

<a id="m002"></a>

## 002 · Living Assurance Constellation

**Hypothesis.** A claim/evidence graph updated by CI flags expired security claims before deployment. **Design.** Represent each assurance claim as a node connected to requirements, tests, build identity, architecture revision, and evidence expiry date. A release gate evaluates whether every critical claim has current supporting evidence and records why a claim failed. **Evidence.** Use an owned repository's test reports, signed build metadata, and synthetic change histories; retain immutable links to the exact evaluated revision. **Test.** Seed controlled regressions, stale test artifacts, and changed dependencies, then measure detection recall, false gate failures, and time to explain each decision. **Boundary.** Passing CI establishes evidence freshness, not security truth; human review remains necessary for assumptions outside executable checks. Sources: [NIST SP 800-218 SSDF](https://csrc.nist.gov/pubs/sp/800/218/final), [SLSA specification](https://slsa.dev/spec/v1.2/).

<a id="m003"></a>

## 003 · Blast-Radius Digital Twin

**Hypothesis.** Interdependency simulation predicts which service failures propagate to mission loss. **Design.** Couple a directed dependency graph to a discrete-event simulator whose nodes have capacity, failover delay, and recovery-state variables. Inject synthetic service outages and compare resulting mission throughput and recovery time against simpler single-node assumptions. **Evidence.** Ingest only approved topology exports and sanitized incident timings; use synthetic load traces when production demand is sensitive. **Test.** Hold out known outage scenarios, report prediction error for lost service-minutes and time-to-recovery, and rank the most consequential unknown edges for review. **Boundary.** Correlated failures and operator actions may dominate graph structure, so the twin reports uncertainty and never drives automatic production shutdown. Sources: [NIST SP 800-160 Vol. 2 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final), [NIST CSF 2.0 Profiles](https://www.nist.gov/cyberframework/profiles).

<a id="m004"></a>

## 004 · Graceful-Degradation Architect

**Hypothesis.** Pre-designed reduced modes retain more essential service during partial compromise. **Design.** Model system modes as a state machine with permitted functions, dependency budgets, entry conditions, and safe exit criteria. Optimize for retained essential throughput subject to isolation and safety constraints; generate a transition playbook from the model. **Evidence.** Exercise approved digital twins or test environments with synthetic failed components, expired credentials, and unavailable network segments. **Test.** Compare ad hoc incident response with rehearsed mode switching using service retained, transition time, and operator error rate. **Boundary.** A reduced mode must have explicit safety authority and rollback; the concept does not justify bypassing interlocks or silently weakening access controls. Sources: [NIST cyber-resilient systems guidance](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final), [NIST SP 800-82 Rev. 3 for OT constraints](https://csrc.nist.gov/pubs/sp/800/82/r3/final).

<a id="m005"></a>

## 005 · Executable Trust Boundaries

**Hypothesis.** Machine-checked data-flow contracts detect architectural drift before runtime exposure. **Design.** Describe each service interface with producer, consumer, data class, authorization predicate, retention rule, and permitted destination. Compile that contract into architecture tests and deployment-policy checks; flag newly observed flows that lack a reviewed edge. **Evidence.** Use test traffic, approved configuration exports, and synthetic sensitive-data markers in place of live content. **Test.** Introduce controlled policy and routing changes, then measure how many unauthorized paths are rejected before deployment and how many authorized paths are incorrectly blocked. **Boundary.** Runtime encryption and dynamic discovery can hide context; report unclassified paths rather than assuming they are safe or malicious. Sources: [NIST SP 800-207 Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final), [NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final).

<a id="m006"></a>

## 006 · Security–Safety Trade-Space Explorer

**Hypothesis.** Joint optimization finds architectures with lower mission risk at the same cost and latency. **Design.** Define a Pareto search over controls with variables for residual risk, safety hazard severity, cost, delay, and power. Generate only designs that satisfy hard safety constraints, then present the remaining trade space and sensitivity to uncertain threat assumptions. **Evidence.** Begin with approved architecture alternatives, published component specifications, and synthetic mission loads; keep threat likelihood estimates labeled as judgments. **Test.** Ask multidisciplinary reviewers to compare candidate choices with their normal decision process; measure dominated choices avoided and whether experts agree on constraint violations. **Boundary.** A numeric score cannot replace safety certification or risk acceptance by accountable owners. Sources: [NIST systems security engineering](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final), [NIST cyber resiliency guidance](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final).

<a id="m007"></a>

## 007 · Assumption Expiry Ledger

**Hypothesis.** Monitoring conditions behind design assumptions exposes risk earlier than periodic reassessment. **Design.** Give each assumption a statement, owner, evidence source, validity condition, observation cadence, and expiry trigger. An event stream marks assumptions at risk when supplier support, identity topology, load, or physical environment crosses a defined threshold. **Evidence.** Use authorized configuration and inventory changes; synthetic event replay exercises rare conditions without exposing real assets. **Test.** Compare time-to-detection and alert precision with calendar-based risk reviews across a blinded set of seeded changes. **Boundary.** Missing telemetry is its own state, not evidence that an assumption still holds; reviewers must resolve ambiguous alerts. Sources: [NIST CSF 2.0](https://www.nist.gov/cyberframework), [NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final).

<a id="m008"></a>

## 008 · Policy Across Domains

**Hypothesis.** Formal information-flow constraints make cross-domain transfers auditable end to end. **Design.** Specify source classification, destination eligibility, transformation, release authority, and audit event for each transfer. Treat policy as a finite-state relation and prove that every allowed path has an authorized release step; use test records to exercise denials and exception handling. **Evidence.** Use synthetic labeled messages and an isolated reference architecture; production classifications and content remain outside the prototype. **Test.** Seed contradictory policies and undocumented transfer routes; measure detection recall and whether an independent reviewer can reconstruct each permitted decision from evidence. **Boundary.** Formal validity depends on accurate labels and enforcement points; false or missing labels remain a governance problem. Sources: [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final), [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final).

<a id="m009"></a>

## 009 · Defense Energy Budget

**Hypothesis.** Resource-aware protective controls preserve security under constrained power and compute. **Design.** For a battery or edge node, allocate CPU cycles, storage writes, radio airtime, and joules among sensing, authentication, logging, and recovery. A scheduling model selects control frequency while enforcing minimum coverage and mission endurance constraints. **Evidence.** Gather measurements from owned development boards or published component data; create synthetic duty cycles and attack-free stress workloads. **Test.** Plot the Pareto frontier of energy per protected mission hour against missed benign fault-detection cases and service latency. **Boundary.** The optimizer cannot quietly drop mandatory controls; it must declare infeasibility when resource limits prevent minimum requirements. Sources: [NIST cyber-resilient systems guidance](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final), [NIST SP 800-193 firmware resiliency](https://csrc.nist.gov/pubs/sp/800/193/final).

<a id="m010"></a>

## 010 · Mission Thread Witness

**Hypothesis.** A trace from user goal through hardware/software controls makes assurance gaps measurable. **Design.** Create a versioned trace graph from stakeholder need to system requirement, interface, implementation component, test, and acceptance record. Report coverage separately for existence, current evidence, and verified behavior; weight gaps by mission consequence. **Evidence.** Use owned requirements and test artifacts, or a complete synthetic exemplar with deliberate omissions. **Test.** Have reviewers locate seeded broken links and compare detection time and agreement with manual document review; publish the unresolved-edge count with uncertainty. **Boundary.** Link density is not assurance: irrelevant tests must not count, and claims that require human judgment stay visibly unverified. Sources: [NIST SP 800-160 Vol. 1 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v1/r1/final), [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final).
