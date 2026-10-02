# 12 · Human factors and security learning

**Research status:** proposed learning systems, measurement designs, and controlled exercises. No employee performance, behavioral, or training outcomes have been measured. The design treats people as participants in an engineered system, with consent and privacy safeguards.

NIST's [NICE Workforce Framework](https://csrc.nist.gov/pubs/sp/800/181/r1/final) gives a task/knowledge/skill vocabulary; [SP 800-50 Rev. 1](https://csrc.nist.gov/pubs/sp/800/50/r1/final) frames learning as a lifecycle that should be evaluated and improved. These ideas pursue better decisions and clearer teamwork, rather than simplistic completion scores.

```mermaid
flowchart LR
    A[Role and task model] --> B[Safe exercise design]
    B --> C[Observed decisions]
    C --> D[Privacy-aware feedback]
    D --> E[Workflow and learning changes]
    E --> F[Retest on held-out scenarios]
    F --> A
```

| Design layer | Ideas | Primary evidence |
|---|---|---|
| Individual decisions and interfaces | 111–115 | Decision quality, workload, accessibility |
| Team knowledge and capability | 116–120 | Handoff fidelity, learning, coordination |

<a id="m111"></a>

## 111 · Decision-Centered Incident Exercise

**Thesis.** Exercise success should reflect evidence interpretation and the consequences of decisions, not whether a participant clicked through a scripted checklist. **Proposed system.** Build fictional incident cards with ambiguous but controlled evidence, branching options, time pressure, and a scoring rubric for uncertainty handling, escalation, privacy, and service continuity. Map each decision to a NICE task/skill statement. **Evidence and test.** Compare novice and experienced groups on blinded scenario scoring, inter-rater agreement, decision latency, and retention in a later scenario. Pre-register scoring rules before participants see the cards. **Boundary.** Exercises must be opt-in and development-oriented; scores must not become uncontextualized employee surveillance or claims of real-incident competence. Anchors: [NIST NICE Framework](https://csrc.nist.gov/pubs/sp/800/181/r1/final), [NIST SP 800-50 Rev. 1](https://csrc.nist.gov/pubs/sp/800/50/r1/final).

<a id="m112"></a>

## 112 · Cognitive Load Alert Budget

**Thesis.** Reducing simultaneous choices in an operator console should improve correct prioritization during simulated high-volume events. **Proposed system.** Represent each alert by evidence quality, mission impact, freshness, required decision, and reversible actions. A configurable interface batches related alerts and exposes the reason for each priority without hiding raw records. **Evidence and test.** Run a randomized crossover study with synthetic alert streams; measure correct decisions, missed high-impact events, completion time, and subjective workload. Report performance separately for novices and experts. **Boundary.** Interface design must allow users to inspect suppressed context and correct the ranking; laboratory task speed is not equivalent to operational safety. Anchors: [NIST SP 800-50 Rev. 1](https://csrc.nist.gov/pubs/sp/800/50/r1/final), [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final).

<a id="m113"></a>

## 113 · Security Documentation as Control

**Thesis.** A tested task guide can prevent security errors as measurably as a technical control. **Proposed system.** Turn operational instructions into versioned decision aids with purpose, prerequisites, stop conditions, evidence to collect, escalation contact, and rollback. Associate each guide with the task it supports and log revisions after near misses. **Evidence and test.** In a safe laboratory exercise, compare error frequency, completion time, and recovery from ambiguous cases using the current guide versus a revised guide. Use independent observers and include a no-guide baseline where ethical. **Boundary.** Documentation cannot replace enforced access controls; a polished guide is only useful if current, findable, and usable under pressure. Anchors: [NIST SP 800-50 Rev. 1](https://csrc.nist.gov/pubs/sp/800/50/r1/final), [NIST NICE Framework](https://csrc.nist.gov/pubs/sp/800/181/r1/final).

<a id="m114"></a>

## 114 · Accessibility-Preserving Defense UI

**Thesis.** Interfaces designed for varied visual, motor, and cognitive needs should increase decision accuracy across a broader operator population. **Proposed system.** Produce equivalent keyboard, screen-reader, high-contrast, and low-distraction paths through an incident dashboard. Make severity and provenance legible without relying on color alone; retain the same evidence and authorization checks in every mode. **Evidence and test.** Conduct consented usability sessions using synthetic cases and assistive technology; measure task completion, error rate, navigation burden, and perceived confidence across interface modes. **Boundary.** Accessibility tests must avoid collecting unnecessary disability information, and one tested configuration cannot guarantee universal access. Anchors: [NIST SP 800-50 Rev. 1](https://csrc.nist.gov/pubs/sp/800/50/r1/final), [NIST NICE Framework](https://csrc.nist.gov/pubs/sp/800/181/r1/final).

<a id="m115"></a>

## 115 · Opt-In Reporting Rehearsal

**Thesis.** Rehearsing the decision to report ambiguous evidence may shorten reporting delay without pressuring people to make confident accusations. **Proposed system.** Create a transparent, consented exercise with fictional suspicious events, simple reporting paths, immediate supportive feedback, and explicit permission to say “unsure.” Record only task-level timing and whether relevant context was preserved. **Evidence and test.** Compare report quality and delay before and after instruction using randomized synthetic scenarios, while tracking false reports and willingness to seek help. **Boundary.** No deceptive social-engineering messages, real-world victim targeting, punitive ranking, or collection of private communications. The metric is an exercise result, not evidence of actual organizational risk reduction. Anchors: [NIST SP 800-50 Rev. 1](https://csrc.nist.gov/pubs/sp/800/50/r1/final), [NIST CSF 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20).

<a id="m116"></a>

## 116 · Shift-Handoff Memory

**Thesis.** A structured handoff that preserves uncertainty and pending decisions should reduce evidence loss between response shifts. **Proposed system.** Use a case-state schema for confirmed facts, disputed interpretations, missing data, owner, next action, time constraint, and evidence link. The outgoing team signs the state; the incoming team acknowledges and can challenge it. **Evidence and test.** In multi-team tabletop exercises, seed the same incident state into free-form versus structured handoffs. Score information retention, unnecessary repeated work, contradictory actions, and time to the next justified decision. **Boundary.** A form can create false completeness; the interface must make unknowns visible and permit verbal clarification for complex cases. Anchors: [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), [NIST NICE Framework](https://csrc.nist.gov/pubs/sp/800/181/r1/final).

<a id="m117"></a>

## 117 · Learning from Near Misses

**Thesis.** A low-friction, non-punitive record of near misses can reveal system design problems before they become incidents. **Proposed system.** Offer a privacy-preserving submission channel that captures task context, barrier that caught the problem, contributing interface/process conditions, and an improvement proposal. Aggregate at workflow level and separate learning review from performance management. **Evidence and test.** Pilot with synthetic cases first, then a consented organization; evaluate report quality, time to corrective action, recurrence of the same condition, and participant trust. **Boundary.** Higher report count may mean stronger reporting culture rather than worsening safety; the project must avoid naming individuals or presenting causal conclusions without review. Anchors: [NIST SP 800-50 Rev. 1](https://csrc.nist.gov/pubs/sp/800/50/r1/final), [NIST SP 800-160 Vol. 2](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final).

<a id="m118"></a>

## 118 · Role-Specific Skill Telemetry

**Thesis.** Observed task performance can target learning more precisely than generic course attendance. **Proposed system.** Map fictional practice tasks to NICE knowledge/skill statements and capture outcome, evidence reasoning, uncertainty management, and help-seeking. Report aggregated competency gaps with a minimum group size; show each participant their own detailed feedback. **Evidence and test.** Compare targeted practice with generic modules on held-out task performance after several weeks, not just immediate quiz scores. Examine whether improvement differs across experience levels. **Boundary.** These are simulated tasks and cannot certify real-world authority; minimize retention of person-level data and prohibit covert employee monitoring. Anchors: [NIST NICE Framework](https://csrc.nist.gov/pubs/sp/800/181/r1/final), [NIST SP 800-50 Rev. 1](https://csrc.nist.gov/pubs/sp/800/50/r1/final).

<a id="m119"></a>

## 119 · Multilingual Incident Vocabulary

**Thesis.** A controlled glossary that preserves uncertainty, severity, and action state across languages should reduce coordination errors. **Proposed system.** Define canonical incident concepts with approved translations, examples, forbidden ambiguities, and machine-readable identifiers. Place the glossary in handoff forms and response guides while keeping human review for consequential messages. **Evidence and test.** Use bilingual reviewers and fictional incident messages; measure semantic agreement, action-state errors, and clarification time against unconstrained translation. **Boundary.** Language varies by region and profession; no glossary replaces a qualified interpreter where misunderstanding could affect safety or legal duties. Avoid storing participants' linguistic profiles beyond consented evaluation needs. Anchors: [NIST NICE Framework](https://csrc.nist.gov/pubs/sp/800/181/r1/final), [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final).

<a id="m120"></a>

## 120 · Team Coordination Simulator

**Thesis.** Communication structure, not only individual skill, determines containment and restoration quality. **Proposed system.** A tabletop simulator assigns operations, engineering, legal/privacy, and communications roles distinct partial views of a fictional event. Experimental conditions vary escalation paths and meeting cadence while holding scenario difficulty constant. **Evidence and test.** Measure decisions per unit time, duplicated effort, incompatible actions, evidence gaps, and mission restoration quality; analyze communication graphs for bottlenecks. **Boundary.** Simulation findings are conditional on scenario and culture; obtain consent, anonymize reporting, and resist treating group rankings as personnel evaluation. Anchors: [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final), [NIST NICE Framework](https://csrc.nist.gov/pubs/sp/800/181/r1/final).
