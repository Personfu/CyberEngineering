# 08 · Cloud, Workload and Recovery Systems

Cloud security is a moving target because infrastructure, identities and code change at different rates. These ideas use evidence from configuration, deployment and runtime to find gaps between intended and actual controls. The designs remain provider-neutral and should be tested in isolated accounts.

```mermaid
flowchart LR
 S[Versioned desired state] --> B[Attested build and deployment]
 B --> R[Observed runtime graph]
 R --> D[Semantic security diff]
 D --> P[Reviewed policy change]
 P --> S
```

| State plane | Typical evidence | Uncertainty to retain |
|---|---|---|
| Source | IaC, policy, dependencies | Unapplied changes |
| Deployment | Build attestations, admission decision | Manual exceptions |
| Runtime | Cloud inventory, identity, network flow | Ephemeral resource gaps |
| Recovery | Restore drills, exported artifacts | Provider-specific coupling |

<a id="m071"></a>

## 071 · Desired-State Security Diff

**Thesis.** A line-by-line infrastructure diff misses the security meaning of a change. **System.** Translate an infrastructure plan into a resource-and-policy graph, then compare before and after effective permissions, reachable paths, encryption boundaries and data location. Rank changes by affected trust boundary and show the exact cause. **Inputs.** Synthetic infrastructure-as-code and isolated cloud account exports, never unapproved production mutations. **Falsifiable metric.** Detection of planted high-impact policy changes and false positives on harmless reformatting or renaming. **Limitation.** Provider semantics and inherited policies can change; conclusions require versioned provider models and runtime confirmation. See [NIST SP 800-207A](https://csrc.nist.gov/pubs/sp/800/207/a/final) and [Kubernetes security](https://kubernetes.io/docs/concepts/security/).

<a id="m072"></a>

## 072 · Ephemeral Resource Lineage

**Thesis.** Short-lived workloads can disappear before an incident investigation begins. **System.** Assign every resource a lineage edge from source revision through build, deployment controller, runtime identity and termination record. Emit compact, signed birth/death events to an independent audit plane and link them to the resource’s policy at the time. **Inputs.** Synthetic autoscaling and authorized metadata from test clusters; omit payload data. **Falsifiable metric.** Fraction of terminated resources whose complete lineage can be reconstructed after planned event loss and clock drift. **Limitation.** A compromised control plane may forge or suppress events; external witnessing should be evaluated. See [SLSA v1.2](https://slsa.dev/spec/v1.2/) and [Kubernetes security concepts](https://kubernetes.io/docs/concepts/security/).

<a id="m073"></a>

## 073 · Secret Journey Map

**Thesis.** A secret’s risk is determined by every copy, delivery and exposure point over time. **System.** Model generation, storage, injection, use, rotation and revocation as a graph of secret *metadata*; record identities and systems that can read each stage without storing secret values. Test delivery mechanisms for accidental persistence in logs, images and debug dumps using synthetic canary secrets. **Inputs.** Isolated build and runtime environments with fabricated keys. **Falsifiable metric.** Number of unauthorized secret copies detected and time from canary revoke to last observed acceptance. **Limitation.** Passive mapping cannot prove absence of an undiscovered copy. See [NIST SP 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final) and [Kubernetes security](https://kubernetes.io/docs/concepts/security/).

<a id="m074"></a>

## 074 · Federated Service-Identity Lattice

**Thesis.** Workload identities need scoped trust across clouds without turning every federation into universal authority. **System.** Express trust as a partial order of issuing domain, workload selector, allowed resource, assurance evidence and expiration. Federation is permitted only when a signed assertion maps to an equal or narrower scope; model name collision and compromised issuer scenarios. **Inputs.** Synthetic SPIFFE trust domains and lab gateways. **Falsifiable metric.** Zero unauthorized cross-domain grants in a generated policy corpus, while required legitimate calls remain available; record counterexamples. **Limitation.** Identity mapping cannot establish workload integrity after compromise. See [SPIFFE](https://spiffe.io/docs/latest/spiffe-about/overview/) and [NIST SP 800-207A](https://csrc.nist.gov/pubs/sp/800/207/a/final).

<a id="m075"></a>

## 075 · Runtime-to-Template Reconciler

**Thesis.** A secure deployment template is weak evidence if the running workload has changed. **System.** Reconcile declared manifests and attested images with observed process, volume, network and service-account state. Produce a typed deviation record: expected, approved exception, accidental drift or unexplained change. Keep observation read-only and avoid placing a privileged agent inside every workload. **Inputs.** Synthetic clusters with planted admission bypass, configuration drift and operator overrides. **Falsifiable metric.** Drift detection time, false-positive rate and percentage of running instances with a complete source-to-runtime trace. **Limitation.** Some observations are impossible without invasive instrumentation; the coverage map must be shown. See [SLSA v1.2](https://slsa.dev/spec/v1.2/) and [Kubernetes security](https://kubernetes.io/docs/concepts/security/).

<a id="m076"></a>

## 076 · Storage Residency Proof

**Thesis.** A location setting does not show where all copies and backups of data actually reside. **System.** Build a lineage record for object creation, replication, snapshotting, export and deletion across regions, with signed provider events when available. Check each path against an organization-defined residency policy and surface unknown destinations explicitly. **Inputs.** Synthetic objects and controlled storage-account audit logs; do not access user data content. **Falsifiable metric.** Detection of intentionally misplaced replicas and correctness of deletion-completion claims after a bounded waiting period. **Limitation.** Provider logs cannot independently prove physical storage location; the result is an evidence-backed policy assessment. See [NIST Privacy Framework](https://www.nist.gov/privacy-framework) and [NIST SP 800-53A](https://csrc.nist.gov/pubs/sp/800/53/a/r5/final).

<a id="m077"></a>

## 077 · Security Failure-Domain Design

**Thesis.** Independent services can share a hidden failure point such as one issuer, logging plane or control account. **System.** Model trust dependencies as a multiplex graph and compute minimal cut sets for loss of confidentiality, command authority or recovery. Propose isolation changes that reduce common-mode exposure while preserving operation. **Inputs.** Synthetic multi-region architectures and authorized configuration inventories. **Falsifiable metric.** Simulated incident blast radius and service availability before and after proposed partitioning, including correlated component failures. **Limitation.** Graph edges rely on accurate inventories and fault assumptions; live resilience needs staged drills. See [NIST CSF 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20) and [NIST SP 800-207A](https://csrc.nist.gov/pubs/sp/800/207/a/final).

<a id="m078"></a>

## 078 · Serverless Permission Sandbox

**Thesis.** Event-driven functions often receive broad cloud permissions for a narrow task. **System.** Execute a function against synthetic events in an isolated account; collect required API calls and data scopes, then synthesize a candidate policy constrained by approved workflows and emergency behaviors. Replay fault and boundary cases before presenting the narrowed policy for human review. **Inputs.** Synthetic events and test-cloud traces; no production tokens. **Falsifiable metric.** Reduction in effective privilege graph size while maintaining task completion and rejecting planted out-of-scope calls. **Limitation.** Dynamic rare paths may be missed by traces, so the candidate policy requires controlled rollout. See [NIST SP 800-207](https://csrc.nist.gov/pubs/sp/800/207/final) and [NIST SP 800-53](https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final).

<a id="m079"></a>

## 079 · Cluster Admission Evidence Gate

**Thesis.** Admission should depend on evidence about artifact origin and workload policy, with a clear exception path. **System.** Validate image digest, signed provenance, approved source revision, SBOM availability and pod security requirements as separate claims. Produce a signed decision explaining which claim passed or failed; fail closed for high-risk workloads and route exceptions to an accountable review process. **Inputs.** Synthetic images and manifests with planted invalid signatures and missing metadata. **Falsifiable metric.** Rejection rate for planted provenance failures, legitimate deployment acceptance and decision latency under load. **Limitation.** Signed malicious source can still pass provenance checks; runtime controls remain necessary. See [SLSA v1.2](https://slsa.dev/spec/v1.2/) and [Kubernetes security](https://kubernetes.io/docs/concepts/security/).

<a id="m080"></a>

## 080 · Cloud Recovery Portability Test

**Thesis.** Backup claims should be measured by the ability to restore critical service outside its usual control plane. **System.** Export versioned data, policy, identity mapping and infrastructure recipes into an isolated recovery account; run a scripted restore with dependency checks and synthetic transactions. Define recovery point `RPO`, recovery time `RTO` and correctness of service outputs as distinct metrics. **Inputs.** Synthetic datasets and authorized disaster-recovery artifacts in a controlled environment. **Falsifiable metric.** Pass/fail against declared RPO/RTO and data-integrity checks across repeated provider-failure drills. **Limitation.** A lab restore cannot model every contractual or network dependency. See [NIST IR 8374 Rev. 1](https://csrc.nist.gov/pubs/ir/8374/r1/final) and [NIST SP 800-61 Rev. 3](https://csrc.nist.gov/pubs/sp/800/61/r3/final).
