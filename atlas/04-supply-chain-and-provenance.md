# 04 · Supply Chain & Provenance

**Research status:** proposed concepts and evaluation designs. A supply chain is a sequence of claims about where components came from, how they were built, and which product release contains them. These ideas make gaps and contradictions measurable without treating a supplier declaration as independent proof. Experiments use public packages, original build artifacts, or supplier records shared for an authorized evaluation.

```mermaid
flowchart LR
    S[Supplier claim] --> C[Component identity]
    C --> B[Build provenance]
    B --> P[Product release]
    P --> D[Deployed device]
    D --> R[Recovery evidence]
    S -. evidence gap .-> R
```

<a id="m031"></a>

## 031 · Dependency Trust Graph

**Hypothesis.** Provenance-weighted edges prioritize supplier risks better than component counts. **Design.** Connect products, direct and transitive dependencies, maintainers, build services, signatures, and evidence sources in a typed graph. Assign each edge an uncertainty interval based on provenance strength, update cadence, and reachability to essential functions. **Evidence.** Use public package metadata and owned build manifests; distinguish inferred relationships from attested ones. **Test.** Blindly seed outdated, unmaintained, and unverified dependency paths, then compare risk-priority precision and analyst effort with a simple component-count baseline. **Boundary.** Provenance is a confidence signal, not a measure of code quality; missing data must raise uncertainty rather than imply a compromised supplier. Sources: [NIST SP 800-161 Rev. 1](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final), [SLSA specification](https://slsa.dev/spec/v1.2/).

<a id="m032"></a>

## 032 · SBOM Drift Observatory

**Hypothesis.** Comparing declared and observed components detects divergence across releases. **Design.** Normalize software bill of materials records, package-lock data, and resolved binary dependencies into a release-by-release timeline. Separate version change, replacement, disappearance, and unresolvable identity; preserve the source and confidence of each observation. **Evidence.** Use owned builds or public reproducible examples, never private supplier inventories without permission. **Test.** Seed omitted transitive components and mislabeled versions, then measure mismatch recall, false matches, and time required to explain a diff. **Boundary.** An SBOM can omit dynamically loaded or hosted components; the observatory reports coverage limits and does not equate a mismatch with malicious change. Sources: [CISA SBOM minimum elements](https://www.cisa.gov/sites/default/files/2025-08/2025_CISA_SBOM_Minimum_Elements.pdf), [NIST SP 800-161 Rev. 1](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final).

<a id="m033"></a>

## 033 · Reproducibility Dividend

**Hypothesis.** Deterministic builds reduce uncertainty when investigating disputed binaries. **Design.** Build the same owned source and pinned dependencies in independent clean environments operated by separate reviewers. Compare final artifact digests and signed provenance, then model investigation cost as the number of plausible origin hypotheses and analyst-hours needed to resolve a disputed release. **Evidence.** Use public toolchains, owned source, documented dependencies, and synthetic disputes; keep production signing keys outside the study. **Test.** Compare root-cause time, unresolved origin hypotheses, and attribution agreement for reproducible versus intentionally nondeterministic pipelines across seeded release changes. **Boundary.** Byte identity does not establish benign source or compiler correctness; it narrows uncertainty about how a distributed artifact relates to a declared build. Sources: [SLSA specification](https://slsa.dev/spec/v1.2/), [NIST SP 800-218 SSDF](https://csrc.nist.gov/pubs/sp/800/218/final).

<a id="m034"></a>

## 034 · Opaque Artifact Risk Ledger

**Hypothesis.** Evidence gaps around closed components can be quantified and mitigated explicitly. **Design.** For each opaque firmware or library component, record origin, versionability, update channel, interface privileges, available test evidence, and replacement options. Compute an evidence-coverage vector and model which controls reduce exposure when source access is impossible. **Evidence.** Use approved supplier disclosures, public documentation, and integration tests on owned systems; avoid reverse engineering beyond license and authorization. **Test.** Give reviewers a blinded set of components and measure agreement on unverified claims and mitigation priorities before and after using the ledger. **Boundary.** A score must not masquerade as proof of absence of hidden behavior; residual uncertainty remains visible. Sources: [NIST SP 800-161 Rev. 1](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final), [NIST SP 1800-34 device integrity](https://csrc.nist.gov/pubs/sp/1800/34/final).

<a id="m035"></a>

## 035 · Component End-of-Life Forecast

**Hypothesis.** Joint patchability and obsolescence modeling predicts future security debt. **Design.** Build a scenario model with end-of-support date, supplier concentration, patch lead time, spare availability, qualification cost, and mission replacement window. Report the probability of an unsupported critical component over a planning horizon under explicit assumptions. **Evidence.** Use public lifecycle notices and approved procurement data; publish only aggregate or synthetic examples if prices or contracts are sensitive. **Test.** Backtest forecasts on retired components and compare calibration and decision value with a fixed-age replacement policy. **Boundary.** Supplier plans can change abruptly; forecasts should trigger review, not automatically force substitutions that create safety or compatibility risk. Sources: [NIST SP 800-161 Rev. 1](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final), [NIST cyber-resilient systems guidance](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final).

<a id="m036"></a>

## 036 · Signed Design-Bundle Passport

**Hypothesis.** Linking CAD, firmware, schematic, and test records reveals inconsistent product revisions. **Design.** Define a release passport containing hashes and semantic versions for PCB source, fabrication data, BOM, bootloader, application, calibration, and acceptance tests. Sign the passport and verify it at manufacturing handoff and device enrollment. **Evidence.** Use an owned demonstrator with test signing keys and synthetic mismatched bundles. **Test.** Seed stale firmware, swapped layouts, and wrong test reports; measure detection recall and false rejection of legitimate rework. **Boundary.** A passport only protects artifacts included in its scope; physical inspection and chain-of-custody still matter, and signing keys require separate governance. Sources: [NIST IR 8536 supply-chain traceability](https://csrc.nist.gov/pubs/ir/8536/final), [NIST digital thread for manufacturing](https://www.nist.gov/programs-projects/digital-thread-manufacturing).

<a id="m037"></a>

## 037 · Update Lineage Verifier

**Hypothesis.** Release-to-device traceability exposes deployment gaps and rollback ambiguity. **Design.** Record each device's approved update lineage as a graph of release signatures, eligibility rules, install acknowledgments, rollback limits, and recovery state. Compare intended fleet state with privacy-preserving device attestations. **Evidence.** Use synthetic device identifiers and test-key updates on owned hardware or a simulator. **Test.** Inject missed updates, duplicate acknowledgments, and out-of-order rollbacks; measure discrepancies found before the next maintenance cycle and false alert rate. **Boundary.** Offline devices create observation gaps; the verifier must say “unknown” rather than “healthy” until fresh evidence arrives. Sources: [NIST SP 800-193 firmware resiliency](https://csrc.nist.gov/pubs/sp/800/193/final), [NIST IR 8536 traceability](https://csrc.nist.gov/pubs/ir/8536/final).

<a id="m038"></a>

## 038 · Transitive Impact Simulator

**Hypothesis.** A dependency graph estimates which missions a compromised supplier could affect. **Design.** Join supplier and component relationships to deployed product and mission-function graphs, then simulate bounded supplier failure or integrity-loss scenarios. Report reachability, confidence, alternative suppliers, and expected service loss rather than a single dramatic blast-radius number. **Evidence.** Work with public component data and owned inventories; use fictional suppliers in shareable examples. **Test.** Compare predicted affected systems with adjudicated tabletop injects and measure missed critical paths and analyst-hours saved. **Boundary.** Graph incompleteness and hidden subcontractors can dominate error; every result should expose unknown edges and scenario assumptions. Sources: [NIST SP 800-161 Rev. 1](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final), [NIST SP 800-160 Vol. 2 Rev. 1](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final).

<a id="m039"></a>

## 039 · Supplier Evidence Contract

**Hypothesis.** Standardized evidence requests improve comparison without treating self-attestation as proof. **Design.** Publish a machine-readable acquisition contract for component identity, support horizon, build provenance, vulnerability disclosure route, update policy, and independent test artifacts. Add evidence dates, scope, and verification method so reviewers can compare unlike suppliers fairly. **Evidence.** Pilot with consenting suppliers or synthetic bids; keep confidential commercial terms out of public artifacts. **Test.** Have two review teams evaluate identical submissions with and without the contract, then measure agreement, missing-evidence detection, and time spent. **Boundary.** Smaller suppliers may lack formal artifacts; the method should allow proportionate alternatives and mark unverified claims explicitly. Sources: [NIST SP 1326 due diligence guide](https://csrc.nist.gov/pubs/sp/1326/final), [NIST SP 800-161 Rev. 1](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final).

<a id="m040"></a>

## 040 · Recovery Escrow Architecture

**Hypothesis.** Tested source, build, and key custody plans reduce dependence on a single unavailable supplier. **Design.** Specify an escrow package for authorized emergency maintenance: source or reproducible binaries, toolchains, interface documents, test vectors, custodians, activation conditions, and revocation procedure. Rehearse rebuilding and signing in an isolated environment using test keys. **Evidence.** Use fictional contracts or an owned open-source prototype; never place live signing material in the repository. **Test.** Measure time to restore a patched service after a simulated supplier outage and the fraction of required artifacts available and current. **Boundary.** Escrow raises legal, IP, and key-management questions; activation requires prearranged authority and independent custody review. Sources: [NIST SP 800-161 Rev. 1](https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final), [NIST cyber-resilient systems guidance](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final).
