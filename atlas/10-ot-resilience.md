# 10 · Cyberphysical and Operational Resilience

Safety, continuity and physical process constraints govern every proposed control in this chapter. Experiments belong in a simulator or approved testbed until engineers validate fail-safe behavior, maintenance procedures and operator workload. A cyber alert is not authority to change a live controller.

```mermaid
flowchart LR
 P[Physical process and safety envelope] --> T[Read-only telemetry mirror]
 T --> M[Physics and cyber state estimate]
 M --> O[Operator decision with uncertainty]
 O --> D[Approved control or recovery plan]
 D --> V[Simulation and staged validation]
```

| Operating constraint | Question for every prototype |
|---|---|
| Safety invariant | Could this action violate a physical limit? |
| Availability | What is the worst interruption during failure? |
| Determinism | Is latency bounded under load and loss? |
| Recovery | Is the safe sequence state-dependent and tested? |

<a id="m091"></a>

## 091 · Physics-Informed Integrity Monitor

**Thesis.** Telemetry can be syntactically valid but physically impossible. **System.** Couple a simplified process model with sensor and actuator constraints; compare observed state transitions against conservation laws, rate limits and measured uncertainty. Output a residual vector and alternative explanations such as calibration drift, process disturbance or data manipulation. Run the monitor read-only and isolate it from the control loop. **Inputs.** Public or synthetic process models and an authorized testbed with bounded disturbances. **Falsifiable metric.** Detection delay and false alarms across planted sensor faults and simulated integrity anomalies, stratified by operating regime. **Limitation.** Model mismatch can mimic an attack; a residual alone cannot attribute cause. See [NIST OT Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) and [MITRE D3FEND](https://d3fend.mitre.org/about/).

<a id="m092"></a>

## 092 · Maintenance Window Risk Planner

**Thesis.** Security maintenance scheduling should account for the physical process, staffing and exposure window together. **System.** Optimize patch or inspection timing under hard safety constraints, capacity forecasts, fallback availability, exploit evidence and recovery duration. Produce a Pareto set of candidate windows with uncertainty bounds, rather than a single opaque date. **Inputs.** Synthetic schedules and engineering-approved maintenance metadata; live control changes remain out of scope. **Falsifiable metric.** Compare exposure time, service interruption and missed safety constraints against existing scheduling on historical or simulated scenarios. **Limitation.** Unexpected plant conditions or supply-chain delays can invalidate a recommended window. See [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) and [CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog).

<a id="m093"></a>

## 093 · Safety Controller Evidence Mirror

**Thesis.** Security investigators need visibility into safety-controller state without risking its operation. **System.** Design a physically and logically read-only mirror that records approved status signals, configuration digests, timestamp uncertainty and health checks on a separate evidence plane. Validate one-way data flow and predictable load in a hardware-in-the-loop lab. **Inputs.** Simulator or vendor-approved test controllers; no live connection before a safety review. **Falsifiable metric.** Completeness of mirrored safety transitions, maximum added controller latency and absence of outbound control messages under fault injection. **Limitation.** A mirror can miss internal controller state and must not be treated as the safety system itself. See [NIST OT Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) and [NIST control assessment](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final).

<a id="m094"></a>

## 094 · Sensor Calibration Attestation

**Thesis.** A sensor value is meaningful only with its calibration state, firmware and uncertainty. **System.** Bind each reading stream to a signed calibration record containing instrument ID, reference standard, valid interval, firmware digest and uncertainty model. Mark readings after expiry or suspected tampering as degraded, then propagate that uncertainty through higher-level process estimates. **Inputs.** Synthetic sensor streams and authorized calibration certificates with sensitive details redacted. **Falsifiable metric.** Correct rejection of planted stale or mismatched calibration records and bounded downstream error in a known physical test. **Limitation.** A valid signature does not prove the original calibration was correct or the sensor has not drifted since. See [NIST SP 800-213](https://csrc.nist.gov/pubs/sp/800/213/final) and [NIST OT Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final).

<a id="m095"></a>

## 095 · Island-Mode Mission Test

**Thesis.** Critical operations must behave predictably when identity, cloud or network services vanish. **System.** Define a local safe operating envelope and minimal cached authority for disconnected mode; simulate loss of upstream services, stale commands and reconnection conflicts. The test produces a state-transition trace, operator decision points and explicit conditions for returning to normal. **Inputs.** Digital twins or isolated operational testbeds with synthetic users and events. **Falsifiable metric.** Safe service duration, invariant violations and time to coherent resynchronization over repeated outage patterns. **Limitation.** A digital twin cannot capture all physical failure modes; site engineers must approve real drills. See [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) and [NIST CSF 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20).

<a id="m096"></a>

## 096 · Command Plausibility Envelope

**Thesis.** Authorized commands can still be unsafe in the current physical state. **System.** Compute a state-dependent set of permitted command values from process limits, interlocks, actuator rate bounds and operating mode. In research mode, compare proposed commands with this envelope and explain violations; never insert an unvalidated filter into the live control path. **Inputs.** Synthetic command streams and engineering-approved plant models. **Falsifiable metric.** Detection of planted unsafe commands, false rejection of legitimate transients and worst-case decision time under testbed load. **Limitation.** Incorrect plant models can reject safe actions or accept dangerous ones; safety certification is separate. See [NIST OT Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) and [MITRE D3FEND](https://d3fend.mitre.org/about/).

<a id="m097"></a>

## 097 · Cyberphysical Digital Twin

**Thesis.** A useful twin connects process dynamics, controller logic and cyber dependencies rather than simulating only one layer. **System.** Model plant state `x`, control command `u`, sensor observation `y`, communication delay `τ` and trust state `z`. Co-simulate routine operations, lost messages, configuration drift and component failure; emit physical and cyber traces with known ground truth. **Inputs.** Open process models and synthetic topology; protected engineering parameters require explicit approval. **Falsifiable metric.** Prediction error on held-out normal operation and fidelity of fault outcomes in a hardware-in-the-loop comparison. **Limitation.** Poorly modeled rare modes can produce persuasive but misleading exercise results. See [NIST SP 800-82 Rev. 3](https://csrc.nist.gov/pubs/sp/800/82/r3/final) and [NIST control assessment](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final).

<a id="m098"></a>

## 098 · Legacy Device Containment Architecture

**Thesis.** An unpatchable device can sometimes be protected by shaping the environment around it. **System.** Build a least-privilege communication graph, protocol-aware gateway, maintenance-access path and passive monitoring plan for one legacy device class. Include physical fail-safe behavior and a bypass procedure if containment threatens operations. **Inputs.** Vendor documentation and an authorized lab replica; no active probes against production equipment. **Falsifiable metric.** Reduction in reachable services and unauthorized command paths while meeting an explicit uptime and latency budget in tests. **Limitation.** A gateway cannot correct intrinsic device flaws or unknown physical interfaces. See [NIST OT Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) and [NIST Zero Trust Architecture](https://csrc.nist.gov/pubs/sp/800/207/final).

<a id="m099"></a>

## 099 · State-Aware Recovery Sequencer

**Thesis.** Restoring services in the wrong order can damage an industrial process even when every system starts successfully. **System.** Encode dependencies and physical preconditions as a directed graph: power, safety controller, instrumentation, command authority, process controller and external connectivity. Generate candidate recovery sequences that satisfy invariants and require operator sign-off at gates. **Inputs.** Synthetic process states and site-approved recovery procedures in a simulator. **Falsifiable metric.** Time to safe production, number of violated preconditions and rate of successful recovery across planted faults compared with a fixed checklist. **Limitation.** Actual incident state may be partially unknown; the sequencer must be able to stop and request inspection. See [NIST OT Security](https://csrc.nist.gov/pubs/sp/800/82/r3/final) and [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final).

<a id="m100"></a>

## 100 · Cross-Site Recovery Lattice

**Thesis.** Several facilities may share hidden dependencies that make simultaneous recovery impossible. **System.** Represent sites, spare parts, identity services, communication links and crews as a capacity-constrained dependency graph. Optimize staged recovery for safety and essential-service delivery under correlated regional outages; show multiple feasible sequences and the assumptions behind each. **Inputs.** Synthetic site topology, anonymized asset classes and authorized continuity plans. **Falsifiable metric.** Essential-service restoration over time and the number of safety constraints met under stress scenarios, compared with site-by-site planning. **Limitation.** Regional disruptions change travel, staffing and supplies rapidly; human incident command retains authority. See [NIST CSF 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20) and [NIST IR 8374 Rev. 1](https://csrc.nist.gov/pubs/ir/8374/r1/final).
