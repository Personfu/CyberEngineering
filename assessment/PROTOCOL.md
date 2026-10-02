# HELIOS authorized red-team assessment protocol

This track gives 150 distinct ideas a progression from basic security to graduate research. It emphasizes adversary-informed assessment design, controlled evidence, defense validation and useful reporting. Red-team work has a mission objective and a bounded permission contract; it is not defined by the volume of intrusive actions. The modules use fictional inventories, paper models, harmless event fixtures, offline interpreters and consented tabletop decisions. They do not supply exploit reproduction, malware execution, credential theft, endpoint-protection bypass or autonomous offensive workflows.

## Engagement record

| Field | Required record | Stop condition |
|---|---|---|
| Authority | Named owner, exact fictional/lab scope, expiry, permitted operations | Authority absent, ambiguous or expired |
| Mission | Essential function, consequence, decision and success floor | Exercise cannot answer the stated decision |
| Environment | Fixture ID, revision, offline boundary and resource budget | Unexpected contact with an undeclared system |
| Human participation | Consent, withdrawal, accessible format and independent adjudicator | Withdrawal, distress or unapproved interaction |
| Observation | Sensor coverage, missingness, clock bounds and label basis | Necessary evidence unavailable or collection exceeds scope |
| Integrity | Input/output hashes, transformation version and reversible changes | Evidence cannot be bound to the evaluated revision |
| Recovery | Known initial state, approved rollback and closure witness | Intended state cannot be restored |

## Red, blue and white-cell roles

The red cell formulates a plausible abstract failure hypothesis and a benign fixture that should expose a coverage or control weakness. The blue cell evaluates observations without access to the hidden fixture truth. The white cell manages scope, stop conditions, ground truth and blinded adjudication. Separate scenario authors from outcome graders where feasible. Human roleplay is opt-in and transparent; this track includes no deceptive contact campaigns.

| Decision | Red-cell artifact | Blue-cell artifact | White-cell evidence |
|---|---|---|---|
| Is the control observable? | Expected artifact/coverage map | Available observations and gaps | Fixture truth and withheld fields |
| Is a decision justified? | Rival hypotheses and constraints | Fact/inference/unknown ledger | Blinded evaluation rubric |
| Is improvement real? | Paired scenario intervention | Resource-normalized comparator | Preregistered split and endpoint |
| Is the system recoverable? | Abstract failure schedule | Feasible restore order | Prerequisite and closure record |

## Evaluation model

For every module, the question is whether the proposed artifact supports a better engineering decision than an equally informed baseline. Match labels, access, compute, observation windows and analyst time. A fixture-selected hypothesis cannot use the same fixture as proof of generalization. Record a final untouched partition; use scenario, channel, artifact or team as the independent unit.

For binary decisions, retain TP, FP, TN, FN, unknown and excluded counts. Unknown evidence is not a true negative. Report precision and recall together with realistic prevalence and false alerts per observed sensor-hour. For evidence cards, assess supported-claim fraction and unsupported identity/attribution links. For mission exercises, integrate unmet weighted service over time and retain safety constraints. For proofs, document finite bounds, abstraction and assumptions separately from implementation conformance.

## Model and implementation ladder

1. **Basic:** state the boundary, trace one decision, and explain what is unobserved.
2. **Applied:** define the typed fixture, label semantics and simple baseline.
3. **Assessment:** run a harmless offline replay or paper adjudication; preserve expected versus observed outcomes.
4. **Research:** freeze tuning, introduce an adverse case, quantify uncertainty and explain a rival mechanism.
5. **Graduate:** justify identifiability and external validity; independently review negative findings and resource cost.

All numerical floors are owner-selected design choices, not invented performance results. Six earlier mechanics remain executable reference examples; the 150 modules are proposals and assessment specifications rather than completed tools.

## Applicable resources

[NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final) provides assessment planning and finding-analysis context; its 2008 date does not make it a current exploit catalog. [NIST NICE Framework](https://csrc.nist.gov/pubs/sp/800/181/r1/final) provides workforce/learning vocabulary; current component definitions require their separately versioned source. [MITRE ATT&CK resources](https://attack.mitre.org/resources/) organize behavior knowledge, while [MITRE D3FEND](https://d3fend.mitre.org/about/) organizes defensive mechanisms. Neither taxonomy proves prevalence, attribution or achieved coverage.

Use the [existing resource contracts](../research/RESOURCES.md) for LANL, public telemetry, KEV, forensic fixtures, formal examples and engineering resources. Use the [intelligence claim ledger](../data/intelligence/claims.json) for public-persona documentation. No field is populated merely because a report implies it might exist.
