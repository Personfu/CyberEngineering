# Applicable datasets and engineering resources

Reviewed 2026-10-02. Only the filtered, version-pinned KEV metadata was acquired from an external source. Six local benchmark fixtures are generated synthetically. Other entries are acquisition plans or design resources, not downloaded or validated training datasets.

[Machine-readable ledger](../data/research/resources.json) · [KEV snapshot](../data/research/kev_snapshot.json) · [Protocol](METHOD.md)

## LANL · LANL Comprehensive Multi-Source Cyber-Security Events

[Primary resource](https://csr.lanl.gov/data/cyber1/)

**Evidence and acquisition:** Observed enterprise event data; access form; not downloaded.
**Applicable question:** Authentication/process/DNS/flow correlation and missing-observation studies.
**Fields:** De-identified identifiers, relative seconds, authentication outcomes and flows.
**Evaluation hazards:** Split chronologically and by entity; the small red-team label set is incomplete; absence of a label is not a negative truth. Failed-auth inclusion is conditional on at least one successful auth.
**Resources:** 58 days, approximately 12 GB compressed; plan streaming aggregation rather than full RAM loading.
**Rights:** CC0 waiver stated by publisher; human-subject and public-release approvals documented.
**Inspection:** landing page and schema inspected.

## TELEMANOM · Telemanom SMAP/MSL anomaly data and original study

[Primary resource](https://github.com/khundman/telemanom)

**Evidence and acquisition:** Public telemetry benchmark; not downloaded.
**Applicable question:** Spacecraft anomaly detection; benign operational anomalies do not label cyber compromise.
**Fields:** Channel arrays and labeled anomaly intervals; inspect README preprocessing before use.
**Evaluation hazards:** Hold out channels/time; avoid random overlapping window splits and inflated point-adjusted recall; report per-event as well as per-timestamp scoring.
**Resources:** Array data and Python ecosystem; size and dependencies must be checked at pinned revision.
**Rights:** Repository license and dataset terms require review before redistribution.
**Inspection:** author repository inspected; NASA paper https://ntrs.nasa.gov/citations/20210008188.

## KEV · CISA KEV issuer-maintained data mirror

[Primary resource](https://github.com/cisagov/kev-data)

**Evidence and acquisition:** Observed public catalog metadata; 1731 selected records downloaded.
**Applicable question:** Descriptive catalog timing and owned-inventory relevance.
**Fields:** CVE identifier, vendor, product, addition date, ransomware-use indicator.
**Evaluation hazards:** Snapshot SHA and date; addition date is not exploitation onset; missing KEV membership does not mean unexploited. No exploit descriptions or target records are included.
**Resources:** Small JSON metadata; offline processing.
**Rights:** CC0 per issuer README and LICENSE.
**Inspection:** repository and license inspected; pinned source commit in kev_snapshot.json.

## BORG · Google Borg cluster and power traces

[Primary resource](https://github.com/google/cluster-data)

**Evidence and acquisition:** Observed workload/power resource; not downloaded.
**Applicable question:** Cloud scheduling, resource-budget and correlated workload sensitivity.
**Fields:** Task and machine events, usage; 2019 power trace is separately documented.
**Evaluation hazards:** Temporal and cell holdouts; workload failures are not attacks; job identities and workload mix may not transfer to another environment.
**Resources:** Potentially large trace/query workflow; choose fields and downsample with declared policy.
**Rights:** CC-BY per publisher; retain attribution and inspect exact license.
**Inspection:** publisher repository inspected.

## CFREDS · NIST Computer Forensic Reference Data Sets

[Primary resource](https://cfreds.nist.gov/)

**Evidence and acquisition:** Forensic reference fixtures; not downloaded.
**Applicable question:** Known-ground-truth acquisition/parser and inference evaluation.
**Fields:** Fixture-specific artifacts, hashes, descriptions and truth labels.
**Evaluation hazards:** Pin fixture and documented truth; tool behavior on one fixture does not establish evidentiary validity in all cases.
**Resources:** Fixture-specific storage and read-only tooling.
**Rights:** Review each dataset terms; portal license is not automatically fixture license.
**Inspection:** portal resolved but text not retrievable; fixture contents unverified.

## TLA · TLA+ specification examples

[Primary resource](https://github.com/tlaplus/Examples)

**Evidence and acquisition:** Formal specifications/tool examples; not empirical field data.
**Applicable question:** Revocation, concurrency, refinement and proof-assumption studies.
**Fields:** Specification, configuration, invariants and state bounds.
**Evaluation hazards:** Document abstraction and fairness; finite model checking is not an unbounded proof; use a separate implementation trace refinement check.
**Resources:** TLC/Java or equivalent; state space can dominate RAM.
**Rights:** Inspect per-project licensing before reuse.
**Inspection:** maintainer repository inspected.

## OPENTITAN · OpenTitan device life-cycle specification

[Primary resource](https://opentitan.org/book/doc/security/specs/device_life_cycle/)

**Evidence and acquisition:** Hardware design resource; not measured board data.
**Applicable question:** Firmware recovery and device-state trust review.
**Fields:** Declared device states, transition permissions, implementation constraints.
**Evaluation hazards:** Project-specific architecture; does not validate a derivative device or certify physical fault resistance.
**Resources:** Emulator first; optional owned low-voltage dev board, qualified hardware review.
**Rights:** Documentation/source terms require review before copying implementation.
**Inspection:** primary device-lifecycle documentation inspected.

## SLSA · SLSA specification v1.2

[Primary resource](https://slsa.dev/spec/v1.2/)

**Evidence and acquisition:** Versioned provenance requirements; not a labeled dataset.
**Applicable question:** Artifact identity, source/build provenance and freshness study.
**Fields:** Provenance predicate, subject digests, builder and source identity.
**Evaluation hazards:** Evidence validity differs from software correctness; a claimed level requires all actual evidence requirements.
**Resources:** Owned build artifacts, local verifier, snapshot statements.
**Rights:** Follow specification/documentation license and upstream verifier license.
**Inspection:** v1.2 primary specification inspected.

## CFS · NASA Core Flight System

[Primary resource](https://github.com/nasa/cFS)

**Evidence and acquisition:** Flight-software architecture resource; not live mission command access.
**Applicable question:** Offline remote-operation state models and assurance traceability.
**Fields:** Framework interfaces, tests, versioned build and configuration.
**Evaluation hazards:** Do not infer flight readiness or certification from source availability; study command handling and scheduling in an emulator.
**Resources:** Pinned framework checkout and toolchain; submodules separately pinned.
**Rights:** Check each component license and export/distribution notes.
**Inspection:** NASA-maintained repository inspected.

## OTEL · OpenTelemetry documentation

[Primary resource](https://opentelemetry.io/docs/)

**Evidence and acquisition:** Instrumentation schemas/tooling; no third-party telemetry downloaded.
**Applicable question:** Owned-system trace, metric and log correlation.
**Fields:** Trace IDs, spans, event time, service/resource attributes and collection loss.
**Evaluation hazards:** Sampling and asynchronous export create partial observation; exclude secrets and personal attributes from synthetic fixtures.
**Resources:** Optional owned collector and local workload; benchmark supplied here is offline.
**Rights:** Review implementation license and data handling separately.
**Inspection:** primary documentation inspected.

## SYNTHETIC · HELIOS deterministic local fixtures

[Primary resource](../experiments/benchmark.py)

**Evidence and acquisition:** Synthetic; generated locally with declared seed 20261002.
**Applicable question:** Reproducible model mechanics and failure-case evaluation.
**Fields:** Six benchmark fixtures, model assumptions, summary, output hashes.
**Evaluation hazards:** Demonstrates reference algorithms only; neither population realism nor deployed defensive effectiveness follows.
**Resources:** Python standard library; no network or cloud services.
**Rights:** New author-generated fixture data; no imported private telemetry.
**Inspection:** implemented and tested in this change.

## Acquisition record

For any future imported dataset, retain the exact URL/DOI, immutable revision or object ID, source hash, UTC acquisition time, declared rights, collection window, schema, units, missingness and label semantics. Never submit contact information or agree to additional terms merely to complete this ledger. Respect gated access; use a documented synthetic fixture while data access is pending.

The KEV projection keeps five metadata fields and deliberately excludes descriptions, remediation prose and external links. Its source SHA-256 binds the full upstream input; the retained subset has its own repository identity. Descriptive aggregates count catalog entries and addition dates, not attacks or exploitation rates.
