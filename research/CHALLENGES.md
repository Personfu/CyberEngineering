# Graduate qualifying challenges

These 45 tasks turn the fifteen domain models into research questions. Deliver a derivation, an executable or formal counterexample where appropriate, and a falsifiable evaluation. No task is marked completed by the current extension.

## 01 · APOLLO

1. **Derive and challenge the model.** Starting from `L = sum_f w_f integral_0^T [1-q_f(t)] dt`, define every state, unit and assumption. Construct a counterexample involving missing dependencies. Identify what extra observation would make the relevant latent parameter identifiable.
2. **Make the experiment discriminate.** Compare an applicable baseline from Static asset tiers; independent-component availability; graph with no common-cause node with the original mission mechanism. Use shared power or identity failure; delayed failover; demand burst; undocumented edge. Freeze a primary endpoint from recovery loss difference, time to essential function, 95% interval, model calibration, declare the independent sampling unit and explain leakage, uncertainty and a negative control.
3. **Defend external validity.** Audit LANL against this domain's schema. List missing fields and restrictions, estimate memory/storage/personnel cost, and state which conclusion cannot transfer to a new environment. Show an adverse case in which the proposed mechanism loses to a simple baseline.

## 02 · DART

1. **Derive and challenge the model.** Starting from `G(authorized AND fresh AND valid -> permitted) AND G(NOT authorized -> NOT permitted)`, define every state, unit and assumption. Construct a counterexample involving state explosion. Identify what extra observation would make the relevant latent parameter identifiable.
2. **Make the experiment discriminate.** Compare an applicable baseline from Unit tests alone; syntax-only change gate; unbounded optimistic state machine with the original mission mechanism. Use concurrent revocation; crash during transition; overflow at schema boundary; reordered benign events. Freeze a primary endpoint from reachable invariant violations, explored states, trace length, proof coverage, runtime overhead, declare the independent sampling unit and explain leakage, uncertainty and a negative control.
3. **Defend external validity.** Audit TLA against this domain's schema. List missing fields and restrictions, estimate memory/storage/personnel cost, and state which conclusion cannot transfer to a new environment. Show an adverse case in which the proposed mechanism loses to a simple baseline.

## 03 · ORION

1. **Derive and challenge the model.** Starting from `P_safe = sum_s P(s) I[invariant holds after recovery(s)]`, define every state, unit and assumption. Construct a counterexample involving atomicity across reset. Identify what extra observation would make the relevant latent parameter identifiable.
2. **Make the experiment discriminate.** Compare an applicable baseline from Single-slot update; checksums without versioned state; no cross-sensor redundancy with the original mission mechanism. Use reset at every update boundary; loss of metadata write; benign sensor drift; recovery image unavailable. Freeze a primary endpoint from recoverability fraction, boot latency, flash wear, energy and independent trusted-image availability, declare the independent sampling unit and explain leakage, uncertainty and a negative control.
3. **Defend external validity.** Audit OPENTITAN against this domain's schema. List missing fields and restrictions, estimate memory/storage/personnel cost, and state which conclusion cannot transfer to a new environment. Show an adverse case in which the proposed mechanism loses to a simple baseline.

## 04 · VOYAGER

1. **Derive and challenge the model.** Starting from `E(a,t) = sum_j alpha_j I[e_j binds artifact a AND is current at t]`, define every state, unit and assumption. Construct a counterexample involving namespace collisions. Identify what extra observation would make the relevant latent parameter identifiable.
2. **Make the experiment discriminate.** Compare an applicable baseline from Flat component count; unsigned inventory; latest package name match with the original mission mechanism. Use stale sbom; missing build link; renamed package; optional dependency; identical name in different ecosystems. Freeze a primary endpoint from evidence completeness, false acceptance, reproducibility rate, remediation lead time, declare the independent sampling unit and explain leakage, uncertainty and a negative control.
3. **Defend external validity.** Audit SLSA against this domain's schema. List missing fields and restrictions, estimate memory/storage/personnel cost, and state which conclusion cannot transfer to a new environment. Show an adverse case in which the proposed mechanism loses to a simple baseline.

## 05 · KEPLER

1. **Derive and challenge the model.** Starting from `z_t = (x_t-median(x_train))/(1.4826 MAD(x_train)); alert = I[z_t>tau]`, define every state, unit and assumption. Construct a counterexample involving nonrandom missingness. Identify what extra observation would make the relevant latent parameter identifiable.
2. **Make the experiment discriminate.** Compare an applicable baseline from Fixed global threshold; rolling mean/std; single-sensor detector with the original mission mechanism. Use drop sensor blocks; change benign mean; burst legitimate demand; skew clocks; lower anomaly prevalence. Freeze a primary endpoint from precision-recall, false alerts per sensor-hour, event detection delay, missingness-conditioned recall, declare the independent sampling unit and explain leakage, uncertainty and a negative control.
3. **Defend external validity.** Audit LANL against this domain's schema. List missing fields and restrictions, estimate memory/storage/personnel cost, and state which conclusion cannot transfer to a new environment. Show an adverse case in which the proposed mechanism loses to a simple baseline.

## 06 · OSIRIS

1. **Derive and challenge the model.** Starting from `t_i in [observed_i-offset_bound_i, observed_i+offset_bound_i]`, define every state, unit and assumption. Construct a counterexample involving unsynchronized clocks. Identify what extra observation would make the relevant latent parameter identifiable.
2. **Make the experiment discriminate.** Compare an applicable baseline from Sort timestamps directly; assume absent record means event absent with the original mission mechanism. Use known clock offsets; partial acquisitions; duplicate records; missing log interval; parser version changes. Freeze a primary endpoint from ordering accuracy, indeterminate fraction, evidence reproducibility, traceable inference rate, declare the independent sampling unit and explain leakage, uncertainty and a negative control.
3. **Defend external validity.** Audit CFREDS against this domain's schema. List missing fields and restrictions, estimate memory/storage/personnel cost, and state which conclusion cannot transfer to a new environment. Show an adverse case in which the proposed mechanism loses to a simple baseline.

## 07 · ARTEMIS

1. **Derive and challenge the model.** Starting from `min sum_p c_p x_p subject to required_actions subseteq authorized(x)`, define every state, unit and assumption. Construct a counterexample involving context drift. Identify what extra observation would make the relevant latent parameter identifiable.
2. **Make the experiment discriminate.** Compare an applicable baseline from Role template; permission union; periodic access review with the original mission mechanism. Use revoked delegator; expired exception; changing task; partial federation outage; stale cache. Freeze a primary endpoint from excess permissions, task success, denial rate, revocation latency p95, explanation completeness, declare the independent sampling unit and explain leakage, uncertainty and a negative control.
3. **Defend external validity.** Audit SYNTHETIC against this domain's schema. List missing fields and restrictions, estimate memory/storage/personnel cost, and state which conclusion cannot transfer to a new environment. Show an adverse case in which the proposed mechanism loses to a simple baseline.

## 08 · GEMINI

1. **Derive and challenge the model.** Starting from `J = sum_f w_f downtime_f + lambda sum_r recovery_cost_r`, define every state, unit and assumption. Construct a counterexample involving eventual consistency. Identify what extra observation would make the relevant latent parameter identifiable.
2. **Make the experiment discriminate.** Compare an applicable baseline from Single-region restore; periodic snapshot success; configuration diff without resource lineage with the original mission mechanism. Use stale snapshot; identity unavailable; region unavailable; inconsistent dependency checkpoint. Freeze a primary endpoint from restore success, data-loss window, recovery loss, state-diff precision, recovery resource demand, declare the independent sampling unit and explain leakage, uncertainty and a negative control.
3. **Defend external validity.** Audit BORG against this domain's schema. List missing fields and restrictions, estimate memory/storage/personnel cost, and state which conclusion cannot transfer to a new environment. Show an adverse case in which the proposed mechanism loses to a simple baseline.

## 09 · HUBBLE

1. **Derive and challenge the model.** Starting from `Brier = mean_i (p_i-y_i)^2; utility = TP b - FP c - abstentions a`, define every state, unit and assumption. Construct a counterexample involving temporal leakage. Identify what extra observation would make the relevant latent parameter identifiable.
2. **Make the experiment discriminate.** Compare an applicable baseline from Rule-based queue; uncalibrated model; always-abstain policy; same model without evidence check with the original mission mechanism. Use missing evidence; contradictory sources; benign drift; unseen channel; reduced prevalence. Freeze a primary endpoint from brier score, risk vs coverage, unsupported assertion rate, false-alert budget, human correction cost, declare the independent sampling unit and explain leakage, uncertainty and a negative control.
3. **Defend external validity.** Audit TELEMANOM against this domain's schema. List missing fields and restrictions, estimate memory/storage/personnel cost, and state which conclusion cannot transfer to a new environment. Show an adverse case in which the proposed mechanism loses to a simple baseline.

## 10 · PIONEER

1. **Derive and challenge the model.** Starting from `x_(t+1)=A x_t+B u_t+w_t; y_t=C x_t+v_t; r_t=y_t-C xhat_t`, define every state, unit and assumption. Construct a counterexample involving model mismatch. Identify what extra observation would make the relevant latent parameter identifiable.
2. **Make the experiment discriminate.** Compare an applicable baseline from Range limits; independent sensor thresholds; persistence predictor with the original mission mechanism. Use sensor loss; biased calibration; changed load; delayed sample; infeasible recovery state. Freeze a primary endpoint from residual calibration, false alarms per hour, safe-set violations, essential throughput, declare the independent sampling unit and explain leakage, uncertainty and a negative control.
3. **Defend external validity.** Audit SYNTHETIC against this domain's schema. List missing fields and restrictions, estimate memory/storage/personnel cost, and state which conclusion cannot transfer to a new environment. Show an adverse case in which the proposed mechanism loses to a simple baseline.

## 11 · LUNAR GATEWAY

1. **Derive and challenge the model.** Starting from `A_(t+1)=0 if verified contact else A_t+dt; delivery iff contact AND evidence_valid`, define every state, unit and assumption. Construct a counterexample involving availability vs freshness. Identify what extra observation would make the relevant latent parameter identifiable.
2. **Make the experiment discriminate.** Compare an applicable baseline from Always-connected policy; transmit-at-every-step scheduler; unverified receipt with the original mission mechanism. Use missed contact; delayed receipt; key expiry in blackout; storage full; reset during staging. Freeze a primary endpoint from verified delivery fraction, age p95, energy proxy, recovery latency, evidence storage, declare the independent sampling unit and explain leakage, uncertainty and a negative control.
3. **Defend external validity.** Audit CFS against this domain's schema. List missing fields and restrictions, estimate memory/storage/personnel cost, and state which conclusion cannot transfer to a new environment. Show an adverse case in which the proposed mechanism loses to a simple baseline.

## 12 · MERCURY

1. **Derive and challenge the model.** Starting from `E[cost]=sum_k P(outcome_k) cost_k; workload = arrival_rate * handling_time`, define every state, unit and assumption. Construct a counterexample involving learning carryover. Identify what extra observation would make the relevant latent parameter identifiable.
2. **Make the experiment discriminate.** Compare an applicable baseline from Existing interface; unprioritized queue; single handoff template with the original mission mechanism. Use high alert load; shift turnover; ambiguous evidence; accessible alternative needed. Freeze a primary endpoint from decision accuracy, severe error fraction, task time, cognitive workload, handoff loss, declare the independent sampling unit and explain leakage, uncertainty and a negative control.
3. **Defend external validity.** Audit SYNTHETIC against this domain's schema. List missing fields and restrictions, estimate memory/storage/personnel cost, and state which conclusion cannot transfer to a new environment. Show an adverse case in which the proposed mechanism loses to a simple baseline.

## 13 · PHOENIX

1. **Derive and challenge the model.** Starting from `L(order)=sum_f w_f completion_time_f(order)`, define every state, unit and assumption. Construct a counterexample involving unknown prerequisites. Identify what extra observation would make the relevant latent parameter identifiable.
2. **Make the experiment discriminate.** Compare an applicable baseline from FIFO repair; shortest-repair-first; static asset criticality with the original mission mechanism. Use unavailable backup; hidden dependency; staff loss; interrupted restore; false-positive containment. Freeze a primary endpoint from weighted loss, repair regret, rollback success, recovery time, resource utilization, declare the independent sampling unit and explain leakage, uncertainty and a negative control.
3. **Defend external validity.** Audit SYNTHETIC against this domain's schema. List missing fields and restrictions, estimate memory/storage/personnel cost, and state which conclusion cannot transfer to a new environment. Show an adverse case in which the proposed mechanism loses to a simple baseline.

## 14 · NEOWISE

1. **Derive and challenge the model.** Starting from `h(t|z)=h0(t) exp(beta^T z); time_origin = first_relevant_observation`, define every state, unit and assumption. Construct a counterexample involving selection bias. Identify what extra observation would make the relevant latent parameter identifiable.
2. **Make the experiment discriminate.** Compare an applicable baseline from Age-only prioritization; severity-only ranking; manual owned inventory join with the original mission mechanism. Use ambiguous inventory match; unknown remediation date; late publication; vendor naming variation. Freeze a primary endpoint from relevance precision, exposure-days, matched-record coverage, right-censor fraction, declare the independent sampling unit and explain leakage, uncertainty and a negative control.
3. **Defend external validity.** Audit KEV against this domain's schema. List missing fields and restrictions, estimate memory/storage/personnel cost, and state which conclusion cannot transfer to a new environment. Show an adverse case in which the proposed mechanism loses to a simple baseline.

## 15 · JAMES WEBB

1. **Derive and challenge the model.** Starting from `ATE = E[Y(1)-Y(0)]; VOI = expected_loss_without_info - expected_loss_with_info`, define every state, unit and assumption. Construct a counterexample involving confounding. Identify what extra observation would make the relevant latent parameter identifiable.
2. **Make the experiment discriminate.** Compare an applicable baseline from Unadjusted before/after comparison; maturity self-rating; point-estimate budget with the original mission mechanism. Use changed collection pipeline; concurrent intervention; lower event rate; adverse subgroup. Freeze a primary endpoint from effect interval, calibration, cost per retained service-minute, sensitivity to assumptions, declare the independent sampling unit and explain leakage, uncertainty and a negative control.
3. **Defend external validity.** Audit SYNTHETIC against this domain's schema. List missing fields and restrictions, estimate memory/storage/personnel cost, and state which conclusion cannot transfer to a new environment. Show an adverse case in which the proposed mechanism loses to a simple baseline.

## Thesis contribution test

A thesis contribution must be narrower than a platform name: a new identifiable model, a validated uncertainty method, an experimentally supported mechanism, a counterexample that changes an engineering decision, or a reproducible negative finding. Distinguish implementation effort from scientific novelty. Compare with original research in the chosen specialty before claiming novelty; this extension provides a research agenda, not an exhaustive literature review.

For examination, score correctness of derivation, relevance of the comparator, provenance, independence of the test partition, quality of uncertainty analysis, resource realism and clarity of the falsifier. Independent examiner review and scored results remain pending.
