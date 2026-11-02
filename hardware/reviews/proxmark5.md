# Proxmark5

**Independent documentation review · 2026-11-02**

An advanced RFID platform whose current software maturity makes it a developer purchase, not an automatic RDV4 upgrade.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Processor | AT32F435 Cortex-M4 at 288 MHz | [proxmark](https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/master/README.md) |
| Programmable logic | Gowin FPGA | [proxmark](https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/master/README.md) |
| Antennas | Swappable LF and 13.56 MHz HF; the listed UHF add-on is not developed yet | [proxmark](https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/master/README.md) |
| Current maturity | Maintainers label firmware unstable and advise against installing the BWM add-on | [proxmark](https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/master/README.md) |

## Our review

Our recommendation is to buy for firmware development or deliberate early-adopter work, and keep a proven RDV4 available for routine bench tasks. The new MCU, FPGA and expansion connector create engineering headroom, but they do not establish that an existing workflow has already been ported and validated. The most important specification today is the maintainer support warning, not the generation number. A listing that bundles UHF or wireless expansion should not be read as proof those functions are ready.

## Choose it when

You can build, flash and debug evolving firmware and accept feature gaps.

## Skip it when

You need a stable daily RFID workflow or are buying specifically for UHF or the BWM add-on.

## Compatibility and limitations

This assessment follows the live maintainer documentation, which is actively changing. The UHF entry is a roadmap item. The wireless/battery add-on warning is separate from the presence of an ESP32-C2 in the proposed architecture. No reliability or protocol-coverage benchmark was run.

## Alternatives

Proxmark3 RDV4 for an established host-driven bench; Chameleon Ultra for a narrower emulation workflow.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/rfid-bench.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Pin hardware and firmware revisions; validate a small owned reference-tag set against an RDV4 before replacing an established workflow.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Proxmark](https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/master/README.md) — retrieved 2026-11-02; SHA-256 `0bf0f282c5c4af818e0b958c5c11b8049df614fa93b3bedc984ef53c745fc130`.
- [Pm5 Start](https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/HEAD/doc/md/PM5_Start_Here/Getting_Started_With_PM5.md) — retrieved 2026-11-02; SHA-256 `fa9aa19e9d91767d44da1419096db8a92db338dc8258d6a5f5948ffce603ba42`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
