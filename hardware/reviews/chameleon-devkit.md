# Chameleon Ultra Devkit

**Independent documentation review · 2026-11-02**

A distinct Chameleon hardware version, reviewed separately from the Ultra.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| HF reader scope | Includes the Ultra-style reader capability with exposed SWD and test points | [chameleon-hardware](https://github.com/RfidResearchGroup/ChameleonUltra/wiki/hardware) |
| RF design | The hardware guide distinguishes HF and LF antenna arrangements by model | [chameleon-hardware](https://github.com/RfidResearchGroup/ChameleonUltra/wiki/hardware) |
| Control | Documented buttons, slot indicators and USB interface | [chameleon-hardware](https://github.com/RfidResearchGroup/ChameleonUltra/wiki/hardware) |
| Comparison basis | Maintainer hardware guide explicitly separates Lite, Ultra and Devkit | [chameleon-hardware](https://github.com/RfidResearchGroup/ChameleonUltra/wiki/hardware) |

## Our review

Choose the Devkit when access to the electronics, debugging and modification is more important than the smallest enclosure. Its exposed development connections make the hardware architecture easier to investigate. It is not the better everyday keychain simply because it offers more space; the design is optimized for different work.

## Choose it when

This specific emulation-only or development-board role matches the project.

## Skip it when

You need a different model’s reader function or assume the three versions have the same mechanical/service properties.

## Compatibility and limitations

The Lite guide describes a smaller soldered battery and a housing not designed for repeated disassembly. The Devkit is an uncased development PCB with a different physical package. Actual tag modes remain firmware/application-specific; hardware possibility is not completed feature support.

## Alternatives

Chameleon Ultra for a compact reader/emulation combination; Proxmark3 RDV4 for a host-driven analysis bench.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/rfid-bench.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Confirm the hardware version and supported tag mode, then use an owned reference reader and a pinned client/firmware pair.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Chameleon Hardware](https://github.com/RfidResearchGroup/ChameleonUltra/wiki/hardware) — retrieved 2026-11-02; SHA-256 `0d982c75c5f08f6ff109e0d575be8c61c2b4f7796bb8014aed4ee6daa23a660f`.
- [Chameleon Whitepaper](https://github.com/RfidResearchGroup/ChameleonUltra/wiki/technical_whitepaper) — retrieved 2026-11-02; SHA-256 `6f93b8da07a9cc5a9753f9a58aff0fd9e8b3db195fc6ea5e40b11db117226745`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
