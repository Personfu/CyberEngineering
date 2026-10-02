# 02 · Formal Software Assurance

**Research status:** proposed concepts and evaluation designs. This chapter starts with an owned software system and asks where behavior can be expressed precisely enough to test. The projects focus on interfaces, exceptional states, build transformations, and configuration. Quantitative gates below are research criteria, not claims of achieved defect reduction; experiments use synthetic inputs or code under the evaluator's control.

| Engineering layer | Question the model must answer |
|---|---|
| Protocol | Which state transitions are legal? |
| Implementation | Which inputs and failures preserve invariants? |
| Build | Which source, toolchain, and policy produced this binary? |
| Deployment | Which runtime settings preserve the proven assumptions? |

<a id="m011"></a>

## 011 · State-Machine API Sentinel

**Hypothesis.** Protocol state models catch invalid transitions missed by schema validation. **Design.** Define an API as states, transition guards, and postconditions; generate test sequences from the model and compare them with observed response codes and state changes. Include authentication expiry, duplicate requests, and cross-account ownership as explicit states. **Evidence.** Use a local service or approved staging endpoint with synthetic accounts and records, never third-party endpoints. **Test.** Seed incorrect transitions and compare defect recall, precision, and test-runtime cost with schema-only testing. A result is credible only if held-out sequences reveal failures that the baseline misses. **Boundary.** The model may omit real business rules, so a passing run certifies only its stated state space. Sources: [OWASP API Security Top 10](https://api-security.owasp.org/editions/2023/en/0x11-t10/), [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final).

<a id="m012"></a>

## 012 · Parser Boundary Proofbench

**Hypothesis.** Typed parsers plus property tests reduce malformed-input ambiguity at critical interfaces. **Design.** Specify a grammar and canonicalization rules for an owned parser, then test properties such as round-trip stability, deterministic rejection, bounded memory, and agreement between producer and consumer. Track ambiguity as the count of inputs accepted with different interpretations. **Evidence.** Generate benign malformed examples from the grammar and public standards; avoid weaponized payload collections or uncontrolled targets. **Test.** Compare the original parser with a typed reference implementation over the same corpus, reporting disagreement rate and crash-free coverage. **Boundary.** A grammar can be wrong or incomplete; independent protocol review and versioned corpus provenance are required before relying on it. Sources: [MITRE CWE-20 input validation](https://cwe.mitre.org/data/definitions/20.html), [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final).

<a id="m013"></a>

## 013 · Memory-Safety Migration Optimizer

**Hypothesis.** Risk-weighted module migration yields greater defect reduction per engineering hour. **Design.** Score modules by reachable input surface, privilege, parser complexity, known fault history, coupling, and estimated rewrite effort. Solve a constrained portfolio problem that chooses candidates for memory-safe replacement, isolation, or hardening. **Evidence.** Use owned source, issue history, and synthetic defect injection; keep uncertain scores as intervals. **Test.** Compare the selected migration order with a size-based or age-based baseline using independently triaged defect findings per developer-hour and regression rate. **Boundary.** The optimizer must include integration and performance costs; language choice alone does not prove safety, and legacy interfaces can preserve old hazards. Sources: [CISA Secure by Design](https://www.cisa.gov/sites/default/files/2023-10/Shifting-the-Balance-of-Cybersecurity-Risk-Principles-and-Approaches-for-Secure-by-Design-Software.pdf), [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final).

<a id="m014"></a>

## 014 · Exceptional-Path Cartography

**Hypothesis.** Systematic modeling of timeouts, retries, and failover finds more latent faults than happy-path testing. **Design.** Build an event graph for each request with timeout budgets, retry limits, idempotency keys, and compensation steps. Model-check whether every reachable state terminates safely or is explicitly recoverable. **Evidence.** Exercise an owned test service with injected delay, partial responses, and component unavailability; keep customer data out of the harness. **Test.** Compare seeded fault discovery and false alarms against normal integration tests, and measure whether the system duplicates work or violates a stated invariant. **Boundary.** State-space explosion requires declared abstractions and bounded schedules; no proof should be claimed beyond those bounds. Sources: [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final), [NIST SP 800-160 Vol. 2 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final).

<a id="m015"></a>

## 015 · Compiler-Decision Attestation

**Hypothesis.** Tracing compiler decisions locates behavior-changing build divergence earlier than a final binary hash comparison. **Design.** Attest the input and output digest of each compiler stage—preprocessing, intermediate representation, optimization, code generation, and linking—together with tool identity and flags. A comparison tool identifies the earliest changed stage and its affected functions, then ties that difference to the reviewed source revision. **Evidence.** Use an owned reference program with deliberately varied flags and toolchain versions; publish synthetic build logs without secrets. **Test.** Seed transformation changes and measure first-divergence localization accuracy and reviewer time against whole-binary comparison. **Boundary.** An attested transformation trace describes what the compiler did; it cannot prove that compiler behavior or generated code is correct. Sources: [SLSA specification](https://slsa.dev/spec/v1.2/), [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final).

<a id="m016"></a>

## 016 · Temporal Authorization Checker

**Hypothesis.** Time-aware policy models uncover privilege windows invisible in static access reviews. **Design.** Express authorization as a predicate over subject, resource, action, device state, delegated role, and time. Simulate role changes, token expiry, emergency access, and revocation propagation; identify intervals where a principal can act beyond the current intent. **Evidence.** Use synthetic identities in an owned policy engine and approved audit schema, never real credentials. **Test.** Seed policy timing defects and compare detected unauthorized-access minutes and false positives with snapshot-based review. **Boundary.** System clocks and delayed logs limit precision; report interval uncertainty and do not treat a policy-model pass as proof of enforcement at every endpoint. Sources: [NIST SP 800-207 Zero Trust](https://csrc.nist.gov/pubs/sp/800/207/final), [OWASP API authorization risks](https://api-security.owasp.org/editions/2023/en/0x11-t10/).

<a id="m017"></a>

## 017 · Semantic Diff Gate

**Hypothesis.** Behavior-focused change analysis predicts security regressions better than line-based diff size. **Design.** Compute a semantic change graph of altered data flows, permissions, validation rules, and exposed interfaces; rank required review depth by reachable behavior rather than changed lines. Treat generated code and configuration as first-class nodes. **Evidence.** Mine an owned repository's change history and synthetic regression commits with blinded labels. **Test.** Compare area under the precision-recall curve and reviewer time with a baseline using file count and line count. **Boundary.** Program analysis can miss reflection and runtime policy; publish unknown edges and retain human review for high-consequence changes. Sources: [NIST SP 800-218 SSDF](https://csrc.nist.gov/pubs/sp/800/218/final), [OWASP ASVS](https://owasp.org/projects/asvs?tab=main).

<a id="m018"></a>

## 018 · Contract Fuzzing Laboratory

**Hypothesis.** Generated benign edge cases expose inconsistent component assumptions without attack payloads. **Design.** Derive test cases from shared contracts for lengths, encodings, order, duplicate fields, optional values, and schema versions. Compare each owned component's parse, normalize, and reject behavior, then minimize disagreements into reproducible fixtures. **Evidence.** Use synthetic records and isolated services with rate limits; store only test inputs and observed outcomes. **Test.** Measure unique contract disagreements found per thousand cases and the proportion fixed without breaking valid traffic. **Boundary.** Generated cases cannot prove absence of defects; any live test requires explicit scope and must avoid service disruption. Sources: [MITRE CWE-20](https://cwe.mitre.org/data/definitions/20.html), [NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final).

<a id="m019"></a>

## 019 · Proof-Carrying Configuration

**Hypothesis.** Deployment settings accompanied by machine-checkable invariants reduce unsafe configuration drift. **Design.** Package each configuration change with assertions about exposed ports, identity scopes, encryption modes, logging, and rollback. Validate the assertions against rendered manifests and a disposable environment before promotion; record the exact artifact hash. **Evidence.** Use owned infrastructure-as-code and synthetic secrets, with policy tests that cannot access production credentials. **Test.** Seed misconfigurations and compare predeployment rejection recall and false blockers against linting alone. **Boundary.** A proven configuration file can still be applied incorrectly or changed at runtime; include a postdeployment observation step and label any unobserved state. Sources: [NIST SP 800-53 Rev. 5](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final), [NIST SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final).

<a id="m020"></a>

## 020 · Resource-Exhaustion Model

**Hypothesis.** Bounding legitimate workload envelopes exposes denial-of-service fragility before production. **Design.** Model queue depth, arrival rate, service time, memory pressure, and backpressure policy for each owned service. Generate lawful synthetic demand within an agreed laboratory limit and predict the point where latency or availability violates the service objective. **Evidence.** Use sanitized capacity counters and approved benchmark fixtures; do not load-test external or production systems without a separately approved test plan. **Test.** Compare predicted saturation and recovery against measured results, reporting error bands and whether graceful shedding protects essential requests. **Boundary.** Models are workload-specific; a lab benchmark is not permission for stress testing elsewhere and cannot predict every adversarial traffic shape. Sources: [OWASP API Security Top 10 resource consumption](https://api-security.owasp.org/editions/2023/en/0xa4-unrestricted-resource-consumption/), [NIST SP 800-160 Vol. 2 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final).
