# 07 · Identity, Consent and Authority

This chapter models authorization as a time-dependent claim about a person, workload or device and a specific resource. The research aim is to make grants, exceptions and revocations explainable and measurable without expanding surveillance.

```mermaid
flowchart LR
 I[Verified identity or workload assertion] --> P[Policy and consent state]
 P --> D[Decision with reason and expiry]
 D --> R[Scoped resource use]
 R --> A[Minimal audit proof]
 A --> V[Revocation and re-evaluation]
```

| Evaluation axis | Representative measure | Boundary |
|---|---|---|
| Authority | Granted actions minus necessary actions | Ground truth must be defined per task |
| Revocation | Time from policy change to effective denial | Include caches and offline clients |
| Privacy | Re-identification and data-linkability risk | Test with consent and synthetic subjects |
| Explainability | Correctness of stated policy reason | Avoid revealing protected policy internals |

<a id="m061"></a>

## 061 · Permission Origin Graph

**Thesis.** A role label rarely tells an operator why a subject can reach a resource. **System.** Construct a graph of principals, groups, delegated roles, service identities, policy rules and resource paths. For each permitted action, compute the shortest and all materially distinct authorization paths, plus the grant owner and expiry. Mark inherited and direct grants differently. **Inputs.** Authorized IAM policy exports and synthetic organizations containing known transitive grants. **Falsifiable metric.** Recall of all effective privileges and precision of the reported origin path against policy-engine decisions; measure graph-update latency after change. **Limitation.** Application-local permissions or undocumented side channels can invalidate completeness. See [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final) and [NIST SP 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final).

<a id="m062"></a>

## 062 · Least-Privilege Solver

**Thesis.** Permission reduction should be optimized against real tasks and safety constraints, not arbitrary role size. **System.** Define a binary policy matrix `A(subject, action, resource)` and an observed task matrix `T`; solve for the smallest authorized `A` that covers approved `T`, preserves emergency workflows and obeys separation-of-duty rules. Generate a proposed change set and counterexample traces, never auto-apply. **Inputs.** Synthetic task logs and organization-approved, de-identified access traces. **Falsifiable metric.** Removed excess grants while maintaining task success in replay and avoiding prohibited privilege combinations. **Limitation.** Rare legitimate tasks may be absent from historical traces; human owners must review the result. See [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final) and [NIST SP 800-53A](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final).

<a id="m063"></a>

## 063 · Consent Lifecycle Auditor

**Thesis.** Consent is an evolving state with scope, expiration and withdrawal, not a one-time checkbox. **System.** Represent consent as a versioned purpose–data–recipient–duration tuple and trace each processing event to the consent state valid at event time. Test renewal, withdrawal, downstream deletion and exceptions in a deterministic policy simulator. **Inputs.** Synthetic consent histories first; real records only with an approved privacy basis and minimization plan. **Falsifiable metric.** Detection rate of planted post-withdrawal use and false flags on valid transitions, with a timed deletion-completion measure. **Limitation.** Technical traces cannot establish that consent was informed, freely given or legally sufficient. See [NIST Privacy Framework](https://www.nist.gov/privacy-framework) and [NIST SP 800-63 Rev. 4](https://pages.nist.gov/800-63-4/).

<a id="m064"></a>

## 064 · Break-Glass Accountability

**Thesis.** Emergency access can remain available while becoming narrow, time-limited and independently reviewable. **System.** Issue a scoped emergency grant bound to an incident, approving actor, resource, start/end time and immutable reason record. A policy engine enforces expiry and a separate reviewer receives a minimal use transcript after the incident. **Inputs.** Synthetic incident drills and policy configurations, with no production privilege issuance in the prototype. **Falsifiable metric.** Median time to gain necessary emergency access, number of excess resources reachable and fraction of grants expired by the specified deadline. **Limitation.** Logs and reviewers may fail during the same crisis; offline procedures must be designed. See [NIST SP 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) and [NIST incident response](https://csrc.nist.gov/pubs/sp/800/61/r3/final).

<a id="m065"></a>

## 065 · Service-Identity Expiration Clock

**Thesis.** Credential rotation must be measured against the time during which a stolen credential would remain useful. **System.** Build an identity inventory linking workload, issuer, certificate/token lifetime, rotation path and relying parties. Simulate issuer loss, stale caches and clock skew; compute an effective exposure window rather than trusting configured time-to-live alone. **Inputs.** Synthetic workload identities and authorized metadata from identity services; never ingest secrets. **Falsifiable metric.** Maximum observed acceptance time after revocation and recovery time under planted rotation faults. **Limitation.** Identity proves a workload claim, not whether its actions are allowed. See [SPIFFE](https://spiffe.io/docs/latest/spiffe-about/overview/) and [NIST SP 800-207A](https://csrc.nist.gov/pubs/sp/800/207/a/final).

<a id="m066"></a>

## 066 · Private Correlation Token

**Thesis.** Cross-system incident correlation need not expose durable personal identifiers to every analyst. **System.** Derive short-lived, purpose-bound correlation tokens in a trusted service with explicit rotation and access logging. Match events over a defined investigation window while keeping re-identification in a separately governed workflow. Model token collision, linkage and compromise risk, then compare utility with plain identifiers. **Inputs.** Synthetic identities and consenting test accounts; no public or scraped personal data. **Falsifiable metric.** Correct event joins, unauthorized linkage success rate and recovery from token-key rotation. **Limitation.** Pseudonymization is not anonymity, especially when auxiliary fields expose identity. See [NIST Privacy Framework](https://www.nist.gov/privacy-framework) and [NIST SP 800-226](https://csrc.nist.gov/pubs/sp/800/226/final).

<a id="m067"></a>

## 067 · Device-Bound Session Assurance

**Thesis.** Session trust should change when the device, authenticator or environment changes. **System.** Bind a session to a phishing-resistant authentication event and a privacy-minimized device assurance signal; re-evaluate when risk signals change or the binding expires. Use a state machine for normal, step-up, degraded and revoked modes, with clear user recovery paths. **Inputs.** Lab devices and synthetic session traces, not fingerprinting of public users. **Falsifiable metric.** Successful rejection of planted session replay and false step-up rate during legitimate device changes. **Limitation.** Device binding may exclude users with shared or inaccessible devices; usability must be measured. See [NIST SP 800-63 Rev. 4](https://pages.nist.gov/800-63-4/) and [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final).

<a id="m068"></a>

## 068 · Access Decision Explainer

**Thesis.** A deny/allow result is harder to trust and repair when the controlling rule is opaque. **System.** Produce a minimal explanation tuple: decision, evaluated policy version, relevant attributes, precedence path and safe remediation. Verify the explanation by replaying the same input against the policy engine and comparing the stated rule to the actual evaluation trace. **Inputs.** Synthetic policy bundles and authorized test requests; redact sensitive attributes in operator views. **Falsifiable metric.** Explanation fidelity, median time to resolve legitimate denials and leakage of protected policy details under test. **Limitation.** Revealing every policy condition may help misuse; explanation depth must be role-aware. See [NIST SP 800-207A](https://csrc.nist.gov/pubs/sp/800/207/a/final) and [OWASP ASVS 5.0](https://owasp.org/projects/asvs?tab=main).

<a id="m069"></a>

## 069 · Revocation Latency Observatory

**Thesis.** A revocation command is only successful when all relevant enforcement points stop accepting the identity. **System.** Instrument issuer, cache, gateway, application and offline client acknowledgments. Define latency as the interval from an approved revoke event to the last successful unauthorized acceptance in a controlled probe, stratified by failure mode. **Inputs.** Lab identity fabric and synthetic clients with injected disconnection, cache staleness and clock skew. **Falsifiable metric.** Worst-case and 99th-percentile revocation latency, plus missed-enforcement rate. **Limitation.** A test probe cannot sample every possible relying party; inventory completeness bounds the claim. See [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final) and [SPIFFE](https://spiffe.io/docs/latest/spiffe-about/overview/).

<a id="m070"></a>

## 070 · Data-Minimization Twin

**Thesis.** Teams need to see the functional cost and privacy benefit of collecting less. **System.** Mirror a data-processing workflow using synthetic records, then vary fields, retention periods and aggregation levels. Model service utility, privacy exposure and incident-investigation coverage as separate objectives; display the Pareto frontier rather than collapsing them to one score. **Inputs.** Generated datasets with explicitly controlled sensitive attributes and approved workflow descriptions. **Falsifiable metric.** Utility loss and re-identification/attribute-inference risk at each minimization setting, with confidence intervals. **Limitation.** A synthetic twin may miss rare real-world harms or correlations; privacy review remains necessary. See [NIST Privacy Framework](https://www.nist.gov/privacy-framework) and [NIST SP 800-226](https://csrc.nist.gov/pubs/sp/800/226/final).
