# 15 · Measurement, governance, and futures

**Research status:** proposed measurement programs and investment experiments. Numeric results, cost savings, maturity levels, and capability claims are intentionally absent until validated with declared data and uncertainty.

NIST [SP 800-55 Vol. 1](https://csrc.nist.gov/pubs/sp/800/55/v1/final) addresses selecting useful security measures; [Vol. 2](https://csrc.nist.gov/pubs/sp/800/55/v2/final) addresses the measurement program. The ten concepts below distinguish the object measured, the counterfactual, and the decision the measure should improve. A number without provenance or a decision use is not evidence.

```mermaid
flowchart LR
    A[Decision and mission outcome] --> B[Measurement definition]
    B --> C[Provenanced observation]
    C --> D[Uncertainty and bias analysis]
    D --> E[Counterfactual or baseline]
    E --> F[Reviewed investment decision]
    F --> G[Longitudinal retest]
    G -. revise measure .-> B
```

| Research band | Ideas | Intended artifact |
|---|---|---|
| Measures and evidence | 141–145 | Reproducible, interpretable assurance claims |
| Resource allocation and time | 146–150 | Transparent decisions under uncertainty |

<a id="m141"></a>

## 141 · Cyber Quality Unit

**Thesis.** A defined unit of security and reliability quality should enable comparisons across releases without collapsing distinct harms into one opaque score. **Proposed system.** Define a measure vector: mission availability under specified stress, integrity violations per test-hour, recovery time, and evidence coverage. Attach workload, environment, sample size, and uncertainty to every observation; compare vectors with explicit mission weights. **Evidence and test.** Apply the measure to several blinded synthetic versions across varied workloads and fault scenarios. Test whether known orderings remain stable under resampling, missing evidence, and reasonable changes in mission weights; report disagreement rather than forcing a rank. **Boundary.** No universal scalar can capture every mission or threat; the unit is valid only within its stated operating envelope and may change when objectives change. Anchors: [NIST SP 800-55 Vol. 1](https://csrc.nist.gov/pubs/sp/800/55/v1/final), [NIST SP 800-160 Vol. 2](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final).

<a id="m142"></a>

## 142 · Control Calibration Curve

**Thesis.** A control's predicted protection should be compared with observed behavior, just as a probabilistic forecast is calibrated against outcomes. **Proposed system.** For each bounded test scenario, record the control's predicted success probability, actual success, operating condition, and competing failure modes. Aggregate by probability bin and compute calibration error with confidence bands. **Evidence and test.** Run repeatable synthetic exercises and compare an expert prior against measured frequencies; test whether recalibration improves future predictions on held-out scenarios. **Boundary.** Exercises sample only a narrow environment; even a well-calibrated laboratory control may fail under untested field conditions. Do not convert sparse data into unjustified certainty. Anchors: [NIST SP 800-55 Vol. 1](https://csrc.nist.gov/pubs/sp/800/55/v1/final), [NIST SP 800-160 Vol. 1](https://www.nist.gov/publications/engineering-trustworthy-secure-systems).

<a id="m143"></a>

## 143 · Benchmark Provenance Passport

**Thesis.** A benchmark is trustworthy only when its origin, transformations, exclusions, and limits travel with every result. **Proposed system.** Specify a machine-readable passport with dataset source/permission, collection interval, label method, preprocessing code hash, split rule, missingness, known bias, license, and checksum. A validator refuses to publish a performance number without its matching passport. **Evidence and test.** Reproduce a public or synthetic benchmark from the passport on a clean environment; measure exact-data recovery, result variance, and hidden-leakage findings compared with an undocumented baseline. **Boundary.** Provenance does not guarantee representative data or correct labels; sensitive datasets may require a privacy-preserving abstract passport. Anchors: [NIST SP 800-55 Vol. 2](https://csrc.nist.gov/pubs/sp/800/55/v2/final), [NIST CSF 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20).

<a id="m144"></a>

## 144 · Counterfactual Defense Study

**Thesis.** A control should be credited only for outcome differences that survive a plausible comparison with what would have happened without it. **Proposed system.** Build matched synthetic scenarios with identical workload, fault schedule, and resource budget; vary one control while recording mission loss, detection delay, and collateral effects. Pre-register endpoints and repeat randomized scenario order. **Evidence and test.** Estimate effect size with uncertainty intervals and sensitivity to unmatched factors; include null and failure cases. **Boundary.** Synthetic counterfactuals can establish model-conditional effects, not field effectiveness. Ethical constraints may prohibit withholding a known protective control from production, so deployment studies need observational methods. Anchors: [NIST SP 800-55 Vol. 1](https://csrc.nist.gov/pubs/sp/800/55/v1/final), [NIST SP 800-160 Vol. 2](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final).

<a id="m145"></a>

## 145 · Capability Maturity Evidence Graph

**Thesis.** A graph of requirements, tests, observations, and unresolved exceptions provides a more defensible capability picture than a self-rated maturity score. **Proposed system.** Each claim links to a bounded system, control owner, test method, result, date, environment, and expiry condition. The graph distinguishes design intent, implemented control, verified operation, and unknown status. **Evidence and test.** Give independent reviewers the same fictional program with either the evidence graph or a conventional questionnaire; compare agreement, unsupported-claim rate, and time to locate a gap. **Boundary.** A dense graph can appear authoritative while hiding poor evidence; reviewer sampling and source quality remain necessary. Anchors: [NIST CSF 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20), [NIST SP 800-55 Vol. 2](https://csrc.nist.gov/pubs/sp/800/55/v2/final).

<a id="m146"></a>

## 146 · Security Cost Frontier

**Thesis.** Plotting security outcome against implementation and operating cost can reveal dominated options and diminishing returns. **Proposed system.** Record acquisition cost, labor, compute, latency, maintenance, and a mission-relevant loss metric for each candidate architecture. Use a Pareto frontier with confidence intervals; let mission owners state acceptable tradeoffs rather than hiding them in a weighted score. **Evidence and test.** Evaluate several synthetic architectures under the same scenarios; test whether the frontier changes when cost estimates or mission weights vary. **Boundary.** Monetized risk estimates are uncertain and can obscure rare catastrophic loss; include nonnumeric safety constraints and disclose excluded costs. Anchors: [NIST SP 800-55 Vol. 1](https://csrc.nist.gov/pubs/sp/800/55/v1/final), [NIST SP 800-160 Vol. 1](https://www.nist.gov/publications/engineering-trustworthy-secure-systems).

<a id="m147"></a>

## 147 · Assurance Carbon Budget

**Thesis.** Security verification should be measured for energy and compute demand so expensive pipelines can be made more efficient without losing defect-detection value. **Proposed system.** Instrument test jobs for runtime, compute-hours, estimated energy, test coverage, fault discovery, and cache reuse. Compare scheduling and selection policies against a fixed full-test baseline, retaining required release gates. **Evidence and test.** On a local or consented CI workload, measure energy per useful finding, missed known defects, wall-clock delay, and variance across hardware. **Boundary.** Energy estimates from cloud bills are indirect and location-dependent; do not claim environmental benefit without a declared measurement model. Safety-critical checks stay mandatory even if costly. Anchors: [NIST SP 800-55 Vol. 2](https://csrc.nist.gov/pubs/sp/800/55/v2/final), [NIST SP 800-160 Vol. 1](https://www.nist.gov/publications/engineering-trustworthy-secure-systems).

<a id="m148"></a>

## 148 · Uncertainty Reserve

**Thesis.** An explicit budget for uncertainty can identify where another measurement is more valuable than another control. **Proposed system.** Model each mission risk estimate with a range, evidence quality, dependence between inputs, and decision threshold. Compute the expected value of information for candidate tests, then fund the highest-value measurement that fits time and cost constraints. **Evidence and test.** On a synthetic portfolio with hidden ground truth, compare decision loss and measurement spending with fixed testing and intuition-based selection. **Boundary.** Prior distributions and utility functions are governance assumptions; expose sensitivity and abstain when evidence is too weak. Anchors: [NIST SP 800-55 Vol. 1](https://csrc.nist.gov/pubs/sp/800/55/v1/final), [NIST CSF 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20).

<a id="m149"></a>

## 149 · Strategic Option Portfolio

**Thesis.** Small reversible experiments can reveal which emerging defenses merit investment before an organization commits to a large rollout. **Proposed system.** Maintain an option register with hypothesis, small-scope experiment, maximum cost, stop condition, scale condition, safety guardrail, and owner. Update belief in each option only from traceable results; archive abandoned options with the reason. **Evidence and test.** In a simulated investment cycle, compare regret, sunk cost, and time to identify a useful candidate against a one-shot procurement decision. **Boundary.** A portfolio is not permission to expose production to experiments; use isolated pilots and separate approval for deployment. Anchors: [NIST CSF 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20), [NIST SP 800-55 Vol. 2](https://csrc.nist.gov/pubs/sp/800/55/v2/final).

<a id="m150"></a>

## 150 · Cyber Mission Observatory

**Thesis.** Longitudinal outcome measurement can reveal whether engineering changes improve resilience after the initial launch period. **Proposed system.** Combine versioned architecture decisions, control evidence, approved telemetry, incident and near-miss categories, mission availability, and environmental changes in a time-series register. Use interrupted-series or matched-comparison designs where defensible, with a clear causal uncertainty statement. **Evidence and test.** Start with a synthetic multi-year dataset; measure whether the analysis detects known planted effects without confusing seasonality or reporting changes for improvement. **Boundary.** Observational data are confounded, and greater reporting can look like worsening security. Publish definitions, missingness, privacy limits, and uncertainty with every trend. Anchors: [NIST SP 800-55 Vol. 2](https://csrc.nist.gov/pubs/sp/800/55/v2/final), [NIST SP 800-160 Vol. 2](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final).
