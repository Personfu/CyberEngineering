# Nightmare-Eclipse

**Entity type:** Public research persona. **Review date:** 2026-10-02.

## Claim receipts

**CL01:** Huntress describes Nightmare-Eclipse / Chaotic Eclipse as a vulnerability-publication persona.

Evidence class: Publisher-reported alias association. Source: [Huntress — Nightmare-Eclipse Tooling Seen in Real-World Intrusion](https://www.huntress.com/blog/nightmare-eclipse-intrusion). Publication date: 2026-04-20; retrieved: 2026-10-02.

Limitation: This does not establish a real name or that the persona conducted the investigated intrusion.

**CL02:** Huntress reports tool activity in a customer intrusion and states the observed tools appeared unsuccessful.

Evidence class: First-party reported observation. Source: [Huntress — Nightmare-Eclipse Tooling Seen in Real-World Intrusion](https://www.huntress.com/blog/nightmare-eclipse-intrusion). Publication date: 2026-04-20; retrieved: 2026-10-02.

Limitation: Tool adoption does not identify the developer as the intruder; this is a historical April case.

**CL04:** The pinned KEV row lists Microsoft Defender, addition date 2026-04-22, and ransomware-use value Known.

Evidence class: Observed public catalog metadata. Source: [CISA — KEV issuer metadata snapshot](https://github.com/cisagov/kev-data). Publication date: 2026-10-01; retrieved: 2026-10-02.

Limitation: Catalog metadata does not identify any operator or victim and does not date exploitation onset.

**CL05:** NVD describes a local privilege-escalation issue in Microsoft Defender.

Evidence class: Official record description. Source: [NIST NVD — CVE-2026-33825](https://nvd.nist.gov/vuln/detail/cve-2026-33825). Publication date: unknown/not established; retrieved: 2026-10-02.

Limitation: No affected-build enumeration, exploit verification or current endpoint patch assessment was performed.

## Attribution boundary

Keep publication authorship, vulnerability record and observed tool adoption as separate entities. Identity and intrusion attribution remain unresolved.

## Assessment research question

Evidence-preserving endpoint-health review, privileged-operation audit coverage, source chronology and patch applicability in an owned inventory.

This is a proposed question, not a finding about the named entity. Use synthetic or consented fixtures under the [assessment protocol](../../assessment/PROTOCOL.md). No hosted tools were acquired or run.

[Evidence method](../METHOD.md) · [Card index](../README.md)
