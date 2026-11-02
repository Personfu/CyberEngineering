# Proxmark3 RDV4

**Independent documentation review · 2026-11-02**

The more conservative host-driven RFID choice when reproducible analysis matters more than the newest silicon.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Software | RfidResearchGroup/Iceman client and firmware | [proxmark](https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/master/README.md) |
| Workflow | Separate compilation, client validation and first-use verification documentation | [proxmark](https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/master/README.md) |
| Platform distinction | RDV4 and generic PM3 boards use different build choices | [proxmark](https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/master/README.md) |
| Memory caveat | Some generic PM3 boards have 256 KB flash and need reduced builds; this is not a blanket RDV4 limitation | [proxmark](https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/master/README.md) |

## Our review

RDV4 is the better default than Proxmark5 for a bench that needs a known software path today. Its value is the surrounding client, configuration and verification documentation: a researcher can connect a result to an identifiable build instead of relying on a device screen. Buy the exact board and supported accessories rather than the cheapest product carrying the Proxmark name. The current repository supports several generic platforms, but explicitly identifies unsupported and experimental ones.

## Choose it when

You want inspectable RFID records and a maintained desktop workflow.

## Skip it when

Your main requirement is pocket-sized emulation without a host, or you need a genuinely different radio interface.

## Compatibility and limitations

Keep the client and firmware aligned and distinguish genuine RDV4 hardware from generic PM3 listings. The upstream 256 KB warning applies to particular generic boards, and should not be used to describe every PM3. Signal quality still depends on antennas and the fixture.

## Alternatives

Chameleon Ultra for emulation; Proxmark5 for development on the newer architecture.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/rfid-bench.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Record the exact build and antenna configuration and repeat reads of known owned LF/HF reference tags, including failures.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Proxmark](https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/master/README.md) — retrieved 2026-11-02; SHA-256 `0bf0f282c5c4af818e0b958c5c11b8049df614fa93b3bedc984ef53c745fc130`.
- [Proxmark Platforms](https://raw.githubusercontent.com/RfidResearchGroup/proxmark3/HEAD/doc/md/Use_of_Proxmark/4_Advanced-compilation-parameters.md) — retrieved 2026-11-02; SHA-256 `4687d90d6adf823b307e284b07a3f8d9369ea14c8716eabcbc0948684466b13d`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
