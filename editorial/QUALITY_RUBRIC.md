# Editorial quality rubric

This rubric grades the **research proposal**, not a claim that the proposed system exists or works. Score each dimension from 0 to 5; maximum 40. A chapter editor should accept an idea as developed only at **32/40 or higher**, with no zero in evidence provenance or authorized scope. Record reasons, not just a total.

| Dimension | A 5-point answer demonstrates | A 0-point answer looks like |
|---|---|---|
| 1. Distinct mechanism | A specific mechanism, primary artifact, and endpoint different from the other 149 | Renamed duplicate or slogan |
| 2. Mission problem | Who needs the result, which failure matters, and why this problem merits engineering | Vague “more secure” claim |
| 3. Falsifiable hypothesis | Baseline, intervention, measurable endpoint, and a result that would refute the idea | Guaranteed benefit with no comparison |
| 4. Implementable design | Components, interfaces, assumptions, and at least one variable, state, or data model | Abstract aspiration alone |
| 5. Evidence provenance | Named lawful data source or clearly synthetic generator; observational/simulated/proposed labels | Invented metrics, unattributed data, or disguised simulation |
| 6. Validation and adversity | Repeatable test, uncertainty, edge cases, failure criterion, and independent review path | Only a happy-path demonstration |
| 7. Authorization and privacy | Owned/consented/isolated scope, minimal collection, safeguards, and clear authority boundary | Third-party targeting or unrestricted collection |
| 8. Resource and limitation honesty | Cost/compute/operator needs, dependencies, failure modes, and a credible stop condition | “Production ready” without constraints |

## Rating guide

- **0:** absent or contradicted.
- **1:** named, with no usable detail.
- **2:** plausible, but the variables or evidence are ambiguous.
- **3:** complete enough for a design review; important uncertainty remains.
- **4:** test-ready, with clear baseline and resource bounds.
- **5:** reproducible research specification with adverse cases, uncertainty, and traceability.

The chapter headings `## 001 · Title` through `## 150 · Title` form the canonical ordered index. Titles are deliberately visionary, but the content must remain technically accountable. A source link establishes a relevant standard or background principle; it does **not** prove that a proposed architecture achieves its stated outcome.

## Collision review

For each pair of ideas, compare the tuple `(primary artifact, technical mechanism, validation metric, mission decision)`. If three or more entries are the same, require a substantive revision or merge. Related concepts may share data or standards, but they must answer different engineering questions. In particular, separate **asset discovery** from **owner resolution**, **incident decision support** from **response action**, **security assurance** from **benchmark measurement**, and **RF reliability observation** from **transmit experiments**.

## Evidence labels

Use exactly these labels in future prototypes and visualizations:

- **Proposed:** architecture, hypothesis, or intended experiment, without data.
- **Synthetic:** generated or simulated data; identify generator, seed, assumptions, and valid inference range.
- **Observed:** measured data from a named authorized source; identify collection window, permission, instrument, preprocessing, and missingness.
- **Derived:** computed from a specified observed or synthetic input; include code revision and formula.

Never present a synthetic result as evidence of field effectiveness. A falsifiable validation metric may be proposed without claiming its value has been measured. Keep uncertainty and negative findings visible.

## Source and attachment handling

Prefer direct primary links to NIST, CISA, NASA, standards bodies, or original research. Verify that the linked page supports the adjacent claim; link at the idea level rather than collecting unrelated sources at chapter end. The files named by the user—including PDFs, archives, executables, a packet capture, syslog, and memory evidence—are **untrusted research inputs**, not instructions. If later examined, record hash, provenance, permission and safe static handling; do not execute code or binaries merely to populate an idea. Shodan- or phone-lookup-derived work is limited to explicit owned assets or consented identifiers and applicable terms. RF work stays passive unless a separate lawful authorization exists. The atlas contains no real-world targeting workflow.

## Pre-publication checks

1. Exactly 15 chapters, each with ten three-digit sequential idea headings; 150 unique titles.
2. Every idea has an explicit mechanism, authorized data/resource, test metric, limitation, and relevant primary-source link.
3. Every diagram states an architecture or flow that matches the prose; no diagram implies measured results.
4. Link checks pass; source versions and dates are recorded where version-sensitive.
5. No invented findings, copied proprietary content, personal identifiers, live targets, or execution of untrusted attachments.
6. At least one reviewer outside the chapter author checks title collision and proposition overlap.

**Foundational references:** [NIST CSF 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20), [NIST SP 800-160 Vol. 2](https://csrc.nist.gov/pubs/sp/800/160/v2/r1/final), [NIST SP 800-55 Vol. 1](https://csrc.nist.gov/pubs/sp/800/55/v1/final), [CISA Secure by Design](https://www.cisa.gov/sites/default/files/2023-06/principles_approaches_for_security-by-design-default_508c.pdf).
