# HELIOS Red-Team Assessment Flightbook

150 distinct modules progress from fundamentals to graduate assessment research. This companion track preserves the original 150 missions and the 30 frontier proposals. The RT identifiers denote assessment modules, not an extra 150 completed products.

[Beginner IT, Kali and tool tutorials](../foundations/README.md) · [Engagement and evaluation protocol](PROTOCOL.md) · [Graduate research](../research/README.md) · [Public intelligence cards](../intelligence/README.md) · [Applicable datasets](../research/RESOURCES.md)

| Phase | NASA orbit | Modules | Focus |
|---|---|---|---|
| 1 | MERCURY | RT001–RT025 | Security foundations |
| 2 | GEMINI | RT026–RT050 | Authorized assessment engineering |
| 3 | ARTEMIS | RT051–RT075 | Identity, application and cloud lab assessment |
| 4 | KEPLER | RT076–RT100 | Adversary-informed detection and intelligence |
| 5 | PIONEER | RT101–RT125 | Mission-scale red-blue tabletop research |
| 6 | JAMES WEBB | RT126–RT150 | Graduate red-team measurement and assurance |

## MERCURY · Security foundations

| Module | Engineering question |
|---|---|
| [RT001 · MERCURY · Trust Boundary Sketch](modules/RT001.md) | Which crossing requires a separately authorized decision? |
| [RT002 · MERCURY · Credential Custody Notebook](modules/RT002.md) | Can a reviewer identify every legitimate custodian without retaining a secret? |
| [RT003 · MERCURY · MFA Assurance Review](modules/RT003.md) | Which fallback removes the intended assurance property? |
| [RT004 · MERCURY · Patch State Receipt](modules/RT004.md) | Can installed, applicable and verified-fixed states be distinguished? |
| [RT005 · MERCURY · Backup Restore Baseline](modules/RT005.md) | Does a successful backup imply a working restored service? |
| [RT006 · MERCURY · Endpoint Health Evidence](modules/RT006.md) | Can monitoring failure be separated from a clean endpoint? |
| [RT007 · MERCURY · Network Layer Map](modules/RT007.md) | Where does an encrypted connection remain observable without content inspection? |
| [RT008 · MERCURY · DNS Provenance Card](modules/RT008.md) | Can a naming change be dated without inferring ownership from it? |
| [RT009 · MERCURY · Certificate Lifecycle Lens](modules/RT009.md) | Does certificate validity establish legitimacy of the service behind it? |
| [RT010 · MERCURY · Permission Matrix Primer](modules/RT010.md) | Which permission is unnecessary for the declared task? |
| [RT011 · MERCURY · Log Time Fundamentals](modules/RT011.md) | Which order is genuinely known when clock bounds overlap? |
| [RT012 · MERCURY · Hash and Signature Distinction](modules/RT012.md) | What does integrity establish that authenticity does not, and vice versa? |
| [RT013 · MERCURY · Encryption Context Review](modules/RT013.md) | Who can see plaintext at each boundary even when the link is encrypted? |
| [RT014 · MERCURY · Data Classification Budget](modules/RT014.md) | Which fields are necessary for the research decision? |
| [RT015 · MERCURY · Safe Lab Isolation](modules/RT015.md) | Can any action in the plan reach an undeclared environment? |
| [RT016 · MERCURY · Versioned Lab Inventory](modules/RT016.md) | Can the same input be reconstructed after a dependency changes? |
| [RT017 · MERCURY · Benign Process Baseline](modules/RT017.md) | Which normal maintenance event resembles the scenario under evaluation? |
| [RT018 · MERCURY · Account Lifecycle Clock](modules/RT018.md) | Where does permission outlive the task that justified it? |
| [RT019 · MERCURY · Update Authenticity Review](modules/RT019.md) | What happens when transport succeeds but verification is unknown? |
| [RT020 · MERCURY · Service Dependency Primer](modules/RT020.md) | Why is component availability insufficient to predict mission availability? |
| [RT021 · MERCURY · Alert Base-Rate Lesson](modules/RT021.md) | Can a high-recall detector still produce mostly false alarms? |
| [RT022 · MERCURY · Evidence Label Practice](modules/RT022.md) | Can observed, derived and proposed statements be labeled consistently? |
| [RT023 · MERCURY · Research Citation Hygiene](modules/RT023.md) | Does each source support the exact claim beside it? |
| [RT024 · MERCURY · Incident Note Discipline](modules/RT024.md) | Can another analyst reproduce the conclusion without guessing? |
| [RT025 · MERCURY · Security Value Definition](modules/RT025.md) | What measurable outcome makes this control useful? |

## GEMINI · Authorized assessment engineering

| Module | Engineering question |
|---|---|
| [RT026 · GEMINI · Scope Passport](modules/RT026.md) | Are target ownership, permitted actions and expiry unambiguous? |
| [RT027 · GEMINI · Rules of Engagement Ledger](modules/RT027.md) | Can a stop condition override an otherwise permitted exercise? |
| [RT028 · GEMINI · Mission Objective Interview](modules/RT028.md) | Is the assessment answering a mission question rather than counting findings? |
| [RT029 · GEMINI · Evidence Collection Ceiling](modules/RT029.md) | Can the endpoint be measured without collecting content or credentials? |
| [RT030 · GEMINI · Consent and Contact Plan](modules/RT030.md) | Who can pause a human-involved exercise and how is withdrawal handled? |
| [RT031 · GEMINI · Test Fixture Acceptance](modules/RT031.md) | Which fixture assumption could invalidate the claimed coverage? |
| [RT032 · GEMINI · Baseline Equality Contract](modules/RT032.md) | Did the candidate receive labels or resources withheld from the baseline? |
| [RT033 · GEMINI · White-Cell Decision Journal](modules/RT033.md) | Can scenario control and evaluated analyst decisions be separated? |
| [RT034 · GEMINI · Stop-Condition Rehearsal](modules/RT034.md) | Does every participant know who authorizes resumption? |
| [RT035 · GEMINI · Safety and Availability Review](modules/RT035.md) | Can the exercise fail a service even when no security control changes? |
| [RT036 · GEMINI · Red-Blue Handoff Schema](modules/RT036.md) | Does the defender receive enough context to judge an alert independently? |
| [RT037 · GEMINI · Finding Severity Model](modules/RT037.md) | Does the grade reflect actual prerequisite and mission consequence? |
| [RT038 · GEMINI · Finding Reproduction Packet](modules/RT038.md) | Can a reviewer validate the observation without an exploit or a live target? |
| [RT039 · GEMINI · False Positive Adjudication](modules/RT039.md) | How often does a reviewer reject a legitimate operation? |
| [RT040 · GEMINI · Remediation Owner Receipt](modules/RT040.md) | Does ownership include authority and evidence to resolve the finding? |
| [RT041 · GEMINI · Retest Planning Matrix](modules/RT041.md) | Does the retest examine the changed behavior or merely repeat the old test? |
| [RT042 · GEMINI · Exception Authority Map](modules/RT042.md) | Can a temporary exemption remain invisible after expiry? |
| [RT043 · GEMINI · Assessment Data Retention](modules/RT043.md) | Can results remain reproducible after unnecessary detail is removed? |
| [RT044 · GEMINI · Time and Cost Capture](modules/RT044.md) | What benefit survives normalization by staff time? |
| [RT045 · GEMINI · Evidence Chain Receipt](modules/RT045.md) | Can every conclusion be tied to one evaluated input revision? |
| [RT046 · GEMINI · Coverage Gap Register](modules/RT046.md) | Which missing observation matters most to the mission claim? |
| [RT047 · GEMINI · Negative Finding Report](modules/RT047.md) | Can a lack of improvement be distinguished from insufficient data? |
| [RT048 · GEMINI · Executive Decision Brief](modules/RT048.md) | Which decision is supported and which uncertainty remains unresolved? |
| [RT049 · GEMINI · Technical Annex Contract](modules/RT049.md) | Can a second engineer independently check the main result? |
| [RT050 · GEMINI · Engagement Closure Review](modules/RT050.md) | Can the owner establish that the exercise left no persistent change? |

## ARTEMIS · Identity, application and cloud lab assessment

| Module | Engineering question |
|---|---|
| [RT051 · ARTEMIS · Authorization Decision Witness](modules/RT051.md) | Does every permitted request have a task and grant witness? |
| [RT052 · ARTEMIS · Revocation Blackout Study](modules/RT052.md) | What bound on stale permission can actually be supported? |
| [RT053 · ARTEMIS · Session Expiry Edge Cases](modules/RT053.md) | What happens to a legitimate task at an expiry boundary? |
| [RT054 · ARTEMIS · Break-Glass Accountability](modules/RT054.md) | Can necessary emergency work remain accountable without silently granting permanent access? |
| [RT055 · ARTEMIS · Service Identity Rotation](modules/RT055.md) | Can old and new identities overlap without losing attribution? |
| [RT056 · ARTEMIS · Delegation Provenance](modules/RT056.md) | Does revoking an upstream grant invalidate derived authority? |
| [RT057 · ARTEMIS · Task-Minimal Role Design](modules/RT057.md) | Which feasible role set minimizes excess authority at equal task success? |
| [RT058 · ARTEMIS · API Contract State Map](modules/RT058.md) | Does a valid input in the wrong state violate the business contract? |
| [RT059 · ARTEMIS · Parser Boundary Specification](modules/RT059.md) | Which rejected input should be benign and which acceptance is unsupported? |
| [RT060 · ARTEMIS · Exception Handling Evidence](modules/RT060.md) | Does a failed operation still preserve the declared authorization invariant? |
| [RT061 · ARTEMIS · Rate and Resource Budget](modules/RT061.md) | At what demand is the availability claim infeasible without blaming an adversary? |
| [RT062 · ARTEMIS · Data-Flow Destination Contract](modules/RT062.md) | Can every declared destination be justified by purpose and authority? |
| [RT063 · ARTEMIS · Configuration Semantic Difference](modules/RT063.md) | Does a small text change materially alter authorization? |
| [RT064 · ARTEMIS · Cloud Desired-State Reconciliation](modules/RT064.md) | Can delayed observation be distinguished from configuration drift? |
| [RT065 · ARTEMIS · Ephemeral Resource Attribution](modules/RT065.md) | What survives when an identifier is reused? |
| [RT066 · ARTEMIS · Backup Key Dependency](modules/RT066.md) | Can a valid backup be restored if its identity provider is unavailable? |
| [RT067 · ARTEMIS · Cluster Admission Evidence](modules/RT067.md) | Can an admission decision explain every missing trust requirement? |
| [RT068 · ARTEMIS · Storage Residency Constraint](modules/RT068.md) | Is a relocation decision both authorized and consistent with the data contract? |
| [RT069 · ARTEMIS · Serverless Permission Scope](modules/RT069.md) | Can ephemeral execution retain unintended authority between tasks? |
| [RT070 · ARTEMIS · Secret-Free Diagnostics](modules/RT070.md) | Can the failure be explained without emitting authentication material? |
| [RT071 · ARTEMIS · Component Identity Join](modules/RT071.md) | How often does name-only matching misidentify the component? |
| [RT072 · ARTEMIS · SBOM Change Provenance](modules/RT072.md) | Is a dependency addition supported by the evaluated build artifact? |
| [RT073 · ARTEMIS · Build Evidence Freshness](modules/RT073.md) | Does current metadata bind the exact deployed revision? |
| [RT074 · ARTEMIS · Restore Consistency Certificate](modules/RT074.md) | Which individually valid snapshot combination cannot support a consistent mission state? |
| [RT075 · ARTEMIS · Control Rollback Accounting](modules/RT075.md) | Can rollback restore both behavior and evidence lineage? |

## KEPLER · Adversary-informed detection and intelligence

| Module | Engineering question |
|---|---|
| [RT076 · KEPLER · Public Persona Evidence Card](modules/RT076.md) | Does the source connect a publication persona, an operator or only reused tooling? |
| [RT077 · KEPLER · Community Claim Provenance](modules/RT077.md) | Which assertion is self-published rather than independently established? |
| [RT078 · KEPLER · Tool Author Versus Intruder](modules/RT078.md) | Can shared tooling justify attributing an intrusion to its author? |
| [RT079 · KEPLER · Report Chronology Discipline](modules/RT079.md) | Is a historical patch statement incorrectly presented as current status? |
| [RT080 · KEPLER · KEV Membership Interpretation](modules/RT080.md) | What does a positive listing establish that an absent listing does not? |
| [RT081 · KEPLER · Advisory Observation Matrix](modules/RT081.md) | Which behavior is actually documented versus generalized by the analyst? |
| [RT082 · KEPLER · Behavior Versus Indicator Study](modules/RT082.md) | Can a detector remain useful after incidental identifiers change? |
| [RT083 · KEPLER · Coverage Matrix with Unknowns](modules/RT083.md) | Can an unobserved technique be mistaken for a covered one? |
| [RT084 · KEPLER · Telemetry Dropout Challenge](modules/RT084.md) | How much detection depends on the missing observation rather than the rule? |
| [RT085 · KEPLER · Benign Administration Confounder](modules/RT085.md) | Can the same visible action have a legitimate explanation? |
| [RT086 · KEPLER · Endpoint Protection Health Study](modules/RT086.md) | Can status disagreement be investigated without changing or disabling protections? |
| [RT087 · KEPLER · VPN Identity Evidence Review](modules/RT087.md) | Does a suspicious login establish compromised credentials or only demand review? |
| [RT088 · KEPLER · Timeline Correlation Limits](modules/RT088.md) | Which apparent sequence remains temporally indeterminate? |
| [RT089 · KEPLER · Source Independence Audit](modules/RT089.md) | Are five reports five observations or five copies of one observation? |
| [RT090 · KEPLER · Alias Collision Review](modules/RT090.md) | Can similar handles be kept separate without a supported linkage? |
| [RT091 · KEPLER · Intelligence Confidence Calibration](modules/RT091.md) | Is analyst confidence calibrated at the claim level? |
| [RT092 · KEPLER · Disclosure Ethics Casebook](modules/RT092.md) | Can stakeholder perspectives be documented without treating a grievance as motive proof? |
| [RT093 · KEPLER · Historical Indicator Decay](modules/RT093.md) | When does an old match stop supporting the original hypothesis? |
| [RT094 · KEPLER · ATT&CK Mapping Review](modules/RT094.md) | Does a tactic label add evidence or only organize it? |
| [RT095 · KEPLER · D3FEND Countermeasure Study](modules/RT095.md) | Which observable effect would validate the chosen countermeasure? |
| [RT096 · KEPLER · Detection Rule Fixture Contract](modules/RT096.md) | Can every expected alert be explained by declared input fields? |
| [RT097 · KEPLER · Detection Latency Denominator](modules/RT097.md) | Where does the detection clock begin when telemetry is delayed? |
| [RT098 · KEPLER · Rare-Event Precision Budget](modules/RT098.md) | How does benign drift defeat a high-recall success claim? |
| [RT099 · KEPLER · Contradictory Report Adjudication](modules/RT099.md) | Can conflicting assessments remain visible rather than being averaged into certainty? |
| [RT100 · KEPLER · Adversary Case Evidence Export](modules/RT100.md) | Can the reader distinguish public reporting, local inference and unknown identity? |

## PIONEER · Mission-scale red-blue tabletop research

| Module | Engineering question |
|---|---|
| [RT101 · PIONEER · Identity Failure Campaign](modules/RT101.md) | Can essential functions survive a common identity failure? |
| [RT102 · PIONEER · Segmentation Policy Witness](modules/RT102.md) | Do the declared isolation claims follow from the policy model? |
| [RT103 · PIONEER · Lateral Consequence Model](modules/RT103.md) | Which loss is caused by shared dependence rather than mere adjacency? |
| [RT104 · PIONEER · Data Egress Purpose Review](modules/RT104.md) | Is the information transfer justified by mission purpose? |
| [RT105 · PIONEER · Recovery Escrow Reachability](modules/RT105.md) | Can recovery succeed when the primary trust service is unavailable? |
| [RT106 · PIONEER · Multi-Sensor Timeline Exercise](modules/RT106.md) | How does sensor correlation change evidence without overclaiming cause? |
| [RT107 · PIONEER · Delayed Evidence Courier](modules/RT107.md) | Can remote evidence remain fresh enough for the decision? |
| [RT108 · PIONEER · Battery-Limited Assurance](modules/RT108.md) | Which mandatory coverage makes a proposed schedule infeasible? |
| [RT109 · PIONEER · Ground-Station Change Receipt](modules/RT109.md) | Can a mission command policy be tied to its reviewed revision? |
| [RT110 · PIONEER · CubeSat Update Tabletop](modules/RT110.md) | Which reset state has no independently available approved image? |
| [RT111 · PIONEER · Payload Partition Review](modules/RT111.md) | Can a payload fault affect authority outside its intended boundary? |
| [RT112 · PIONEER · Ephemeris Integrity Notebook](modules/RT112.md) | What check distinguishes data consistency from source authenticity? |
| [RT113 · PIONEER · Clock Trust Ensemble](modules/RT113.md) | What temporal conclusion survives loss of the reference clock? |
| [RT114 · PIONEER · Radiation and Trust-State Review](modules/RT114.md) | Can recovered health coexist with invalid authorization? |
| [RT115 · PIONEER · Receive-Only RF Evidence](modules/RT115.md) | Can observation reliability be assessed without active transmission? |
| [RT116 · PIONEER · Physical Residual Confounding](modules/RT116.md) | Does changed physical demand explain the apparent fault? |
| [RT117 · PIONEER · Maintenance Mode Authority](modules/RT117.md) | Can elevated maintenance authority expire reliably? |
| [RT118 · PIONEER · Safety Interlock Evidence](modules/RT118.md) | Is the digital exercise invalid if it assumes an unreviewed physical transition? |
| [RT119 · PIONEER · Sensor Calibration Lineage](modules/RT119.md) | Can common calibration bias defeat sensor agreement? |
| [RT120 · PIONEER · Island-Mode Service Contract](modules/RT120.md) | Which service can be retained while declared protections remain mandatory? |
| [RT121 · PIONEER · Command Plausibility Model](modules/RT121.md) | Can a digitally authorized command still violate the physical safe set? |
| [RT122 · PIONEER · Legacy Device Boundary](modules/RT122.md) | Which assumed control cannot actually be enforced by that device? |
| [RT123 · PIONEER · Recovery Prerequisite Experiment](modules/RT123.md) | When does a simple feasible heuristic match an optimized plan? |
| [RT124 · PIONEER · Cross-Site Common Cause](modules/RT124.md) | Are independent sites actually dependent on the same supplier, key or operator? |
| [RT125 · PIONEER · Operator Handoff Under Loss](modules/RT125.md) | Can safe coordination survive a shift change and reduced communications? |

## JAMES WEBB · Graduate red-team measurement and assurance

| Module | Engineering question |
|---|---|
| [RT126 · JAMES WEBB · Partial Observability Thesis](modules/RT126.md) | Which state cannot be inferred from the chosen telemetry? |
| [RT127 · JAMES WEBB · Sequential Decision Calibration](modules/RT127.md) | Does threshold selection leak future outcomes? |
| [RT128 · JAMES WEBB · Event-Level Benchmark Geometry](modules/RT128.md) | Does point-adjusted scoring hide missed parts of an event? |
| [RT129 · JAMES WEBB · Domain Shift Identifiability](modules/RT129.md) | Which improvement survives an unseen operating mode? |
| [RT130 · JAMES WEBB · Negative-Evidence Bounds](modules/RT130.md) | What conclusion survives nonrandom missingness? |
| [RT131 · JAMES WEBB · Causal Control Effect Study](modules/RT131.md) | Is the intervention effect identifiable from observational incidents? |
| [RT132 · JAMES WEBB · Common-Cause Tail Risk](modules/RT132.md) | How much does assumed independence understate mission loss? |
| [RT133 · JAMES WEBB · Temporal Refinement Proof](modules/RT133.md) | Which implementation trace violates the declared abstract authorization? |
| [RT134 · JAMES WEBB · Proof Assumption Expiry](modules/RT134.md) | Can a valid proof become inapplicable after an environment change? |
| [RT135 · JAMES WEBB · Resource-Normalized Detection](modules/RT135.md) | Does accuracy improvement survive analyst-time and compute normalization? |
| [RT136 · JAMES WEBB · Privacy Utility Frontier](modules/RT136.md) | What contribution and composition assumptions support the guarantee? |
| [RT137 · JAMES WEBB · Operator Intervention Bias](modules/RT137.md) | Does the observed label set reflect triage decisions rather than event truth? |
| [RT138 · JAMES WEBB · Cognitive Load Crossover](modules/RT138.md) | Can faster decisions increase severe errors? |
| [RT139 · JAMES WEBB · Accessible Assessment Instrument](modules/RT139.md) | Is apparent usability improvement compatible with all included participants? |
| [RT140 · JAMES WEBB · Evidence Graph Reproducibility](modules/RT140.md) | Can an independent reviewer reproduce a conclusion under pinned inputs? |
| [RT141 · JAMES WEBB · Uncertain Recovery Optimization](modules/RT141.md) | Does a tail-optimal schedule generalize beyond the optimization scenarios? |
| [RT142 · JAMES WEBB · Formal State-Space Limits](modules/RT142.md) | Which unmodeled state invalidates the bounded proof claim? |
| [RT143 · JAMES WEBB · Synthetic Fidelity Discrimination](modules/RT143.md) | Can the benchmark preserve useful statistics without copying personal records? |
| [RT144 · JAMES WEBB · Attribution Hypothesis Competition](modules/RT144.md) | What independent observation could distinguish authorship from tool adoption? |
| [RT145 · JAMES WEBB · Intelligence Selection Bias](modules/RT145.md) | Can reporting changes mimic changes in threat prevalence? |
| [RT146 · JAMES WEBB · Benchmark Contamination Audit](modules/RT146.md) | Where has the supposedly untouched test set influenced a decision? |
| [RT147 · JAMES WEBB · Multiplicty and Novelty Review](modules/RT147.md) | Are many hypotheses generating false confidence or an actual narrow contribution? |
| [RT148 · JAMES WEBB · Energy and Carbon Trade Study](modules/RT148.md) | Which savings can be measured rather than assumed from invocation count? |
| [RT149 · JAMES WEBB · Independent Assurance Panel](modules/RT149.md) | Which claim survives review by someone outside the implementer team? |
| [RT150 · JAMES WEBB · Longitudinal Mission Observatory](modules/RT150.md) | Can changes in measurement be separated from changes in cyber risk? |
