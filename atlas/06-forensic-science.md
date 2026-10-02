# 06 · Forensic Science and Evidence Integrity

These ten concepts treat incident evidence as an uncertain measurement system. The goal is to make collection, correlation and interpretation reproducible for authorized investigations. Every method needs a documented scope, acquisition authority and evidence-preservation plan before use on a real system.

```mermaid
flowchart LR
 A[Authorized source and clock model] --> B[Immutable acquisition manifest]
 B --> C[Parser with uncertainty annotations]
 C --> D[Causal and provenance graph]
 D --> E[Analyst conclusion with alternatives]
 E --> F[Independent replay and challenge]
```

| Design variable | Meaning | Required output |
|---|---|---|
| `t ± δt` | Event timestamp and bounded clock uncertainty | Intervals, not false precision |
| `H(x)` | Cryptographic digest of acquired bytes | Manifest plus repeatable verification |
| `P(hypothesis | evidence)` | Calibrated hypothesis estimate when a valid model exists | Assumptions and alternatives |
| `coverage` | Fraction of expected evidence actually acquired | Explicit missingness |

<a id="m051"></a>

## 051 · Memory Snapshot Confidence Map

**Thesis.** A memory image is a snapshot with blind spots, not a complete account of a host. **System.** Build a page-level map that records acquisition time, unreadable ranges, symbol/version compatibility, parser confidence and whether each claimed artifact is supported by one or several independent structures. Derive confidence from measurable acquisition and parsing checks, with “unknown” as a first-class outcome. **Inputs.** Authorized memory images and acquisition logs; synthetic images containing known processes and deliberate gaps for baseline tests. **Falsifiable metric.** On the synthetic ground truth, report artifact recall, false discoveries and calibration error separately by corrupted-page rate. **Limitation.** A passed parser check cannot establish that volatile state was unchanged during acquisition. See [NIST incident response](https://csrc.nist.gov/pubs/sp/800/61/r3/final) and [NIST assessment methods](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final).

<a id="m052"></a>

## 052 · Multi-Source Causal Timeline

**Thesis.** An ordered list of timestamps is weaker than a defensible explanation of which events could have caused others. **System.** Normalize each source into event, observer, clock interval and provenance fields; create a directed graph only when temporal order, system dependency and an explicit causal rule are satisfied. Preserve competing explanations and confidence intervals rather than forcing a single story. **Inputs.** Authorized host, identity, application and network logs, plus synthetic clocks with planted drift. **Falsifiable metric.** Measure recovery of planted causal edges and the rate of impossible edges across controlled drift and dropped-log trials. **Limitation.** Correlation does not establish causation, and retrospective logs may be incomplete or manipulated. See [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) and [OASIS STIX 2.1](https://www.oasis-open.org/standard/stix-version-2-1/).

<a id="m053"></a>

## 053 · PCAP–Syslog Reconciliation Engine

**Thesis.** Packet and syslog views can disagree because of capture loss, NAT, sampling, delayed writes and clock drift. **System.** Join records on bounded flow identifiers and event intervals, then produce four classes: corroborated, packet-only, log-only and unresolved. Estimate capture/drop rates before interpreting a missing match as suspicious. Keep all transformations and redaction rules in a versioned recipe. **Inputs.** Only owned or explicitly authorized captures and logs; synthetic traffic with planted loss, NAT remapping and time skew. **Falsifiable metric.** Precision and recall of true cross-source matches, plus correct classification of planted missingness. **Limitation.** Encrypted traffic and partial captures limit semantics; a mismatch is a question, not proof of intrusion. See [NIST incident response](https://csrc.nist.gov/pubs/sp/800/61/r3/final) and [MITRE ATT&CK](https://attack.mitre.org/tactics/).

<a id="m054"></a>

## 054 · Artifact Provenance Probability

**Thesis.** Analysts need to distinguish “observed” from “likely derived from” without hiding assumptions. **System.** Represent a file or log artifact as a provenance graph linking source, acquisition operation, transformation, analyst action and digest. Use probabilistic scoring only for uncertain links such as clock association; keep cryptographic identity checks as deterministic predicates. Publish calibration curves and abstain when the model has no valid basis. **Inputs.** Authorized evidence manifests and synthetic provenance chains with planted swaps or omissions. **Falsifiable metric.** Link-prediction calibration, swap detection and correct abstention under missing metadata. **Limitation.** A high model score cannot replace chain-of-custody records or a verified hash. See [NIST SP 800-53A](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final) and [Sigstore](https://docs.sigstore.dev/).

<a id="m055"></a>

## 055 · Reproducible Evidence Laboratory

**Thesis.** A defensible conclusion should survive independent replay from the same inputs. **System.** Package read-only artifacts, checksums, parser versions, environment locks, analysis notebooks and expected output hashes in an isolated lab. Each run creates a new signed result manifest and a difference report; the original evidence never becomes a writable workspace. **Inputs.** Synthetic fixtures by default and restricted authorized evidence via access-controlled staging. **Falsifiable metric.** Percentage of analyses reproduced byte-for-byte or within declared numerical tolerance on a second machine, with unexplained differences counted as failures. **Limitation.** Reproducing a parser’s output does not validate its interpretation or data source. See [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) and [SLSA provenance](https://slsa.dev/spec/v1.2/).

<a id="m056"></a>

## 056 · Evidence Retention Optimizer

**Thesis.** Retaining everything can increase privacy risk and investigation cost, while discarding key context can destroy recoverability. **System.** Formulate retention as a constrained optimization problem: minimize storage and privacy exposure subject to legal holds, incident hypotheses, recovery objectives and an auditable evidence-coverage floor. Log every deletion candidate, policy and approval; never allow an automated optimizer to override a hold. **Inputs.** Synthetic retention scenarios and organization-approved policy metadata, not unrestricted personal records. **Falsifiable metric.** Compare preserved investigation coverage and byte-years retained against a fixed baseline across simulated incidents. **Limitation.** Legal obligations and future investigative relevance cannot be inferred from model scores alone. See [NIST Privacy Framework](https://www.nist.gov/privacy-framework) and [NIST incident response](https://csrc.nist.gov/pubs/sp/800/61/r3/final).

<a id="m057"></a>

## 057 · Negative-Evidence Logic

**Thesis.** “No alert” is useful only when a sensor was capable of observing the event and was healthy at the time. **System.** Attach detection rules, coverage windows, sampling rates and health telemetry to every negative claim. Use three-valued logic—observed, absent-under-coverage, unknown—rather than binary true/false. Propagate unknowns through the event graph so that missing sensors do not silently strengthen a conclusion. **Inputs.** Authorized detection logs and synthetic outages with known attack-free and event-present windows. **Falsifiable metric.** The rate at which the engine correctly refuses to assert absence when coverage is deliberately removed. **Limitation.** Sensor health reports may themselves be compromised; independence must be tested. See [NIST control assessment](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final) and [MITRE ATT&CK](https://attack.mitre.org/tactics/).

<a id="m058"></a>

## 058 · Cross-Host Chain of Custody

**Thesis.** Cross-host reconstruction fails when transfers and transforms are undocumented. **System.** Define a custody event schema with artifact digest, owner, authorized purpose, source/destination, time interval, tool version and transformation parent. Use an append-only manifest and verify the directed acyclic graph before analysis; flag cycles, missing parents and digest changes. **Inputs.** Synthetic multi-host incident material and separately authorized evidence collections. **Falsifiable metric.** Detect every planted custody break and report the false-alarm rate on valid transfers. **Limitation.** The graph proves only what its authenticated participants recorded; it cannot prove collection was complete. See [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final) and [SLSA provenance](https://slsa.dev/spec/v1.2/).

<a id="m059"></a>

## 059 · Volatile-State Acquisition Planner

**Thesis.** The safest collection order depends on volatility, impact and the possibility that acquisition changes the system. **System.** Build a decision model that ranks candidate observations by expected evidentiary gain minus service disruption, contamination and privacy costs, under an investigator-defined authority boundary. The output is a proposed sequence with explicit stop conditions and expected state changes; human approval governs execution. **Inputs.** Synthetic host states, known acquisition times and operations-team constraints; no live collection is performed by the model. **Falsifiable metric.** Compare recovered ground-truth facts and induced service impact with a fixed collection order in a lab. **Limitation.** Real incidents can invalidate the prior probabilities and require immediate safety action. See [NIST incident response](https://csrc.nist.gov/pubs/sp/800/61/r3/final) and [NIST CSF 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20).

<a id="m060"></a>

## 060 · Investigator Uncertainty Console

**Thesis.** Investigators should see how much of a conclusion rests on assumptions, missing sensors or stale signatures. **System.** Create a claim ledger that links each narrative assertion to primary observations, transformations, alternative hypotheses and confidence bounds. A visualization shows contradiction paths and how the conclusion changes when a single evidence source is removed. **Inputs.** Synthetic cases and authorized, redacted case metadata. **Falsifiable metric.** In a blinded review, measure whether investigators find planted gaps faster and whether unsupported certainty statements fall without reducing detection of supported facts. **Limitation.** A dashboard can cause false confidence if uncertainty indicators are interpreted as objective probabilities without calibration. See [NIST SP 800-53A](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final) and [NIST AI RMF](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10).
