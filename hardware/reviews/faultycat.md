# FaultyCat v2.x hardware

**Independent documentation review · 2026-11-02**

A specialist electromagnetic/voltage fault-research tool with explicit hardware and firmware scope limits.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Hardware | Electronic Cats’ RP2040-based design derived from PicoEMP | [faultycat](https://raw.githubusercontent.com/ElectronicCats/faultycat/HEAD/README.md) |
| Repositories | Hardware, firmware and faultycmd host tooling now live in separate repositories | [faultycat](https://raw.githubusercontent.com/ElectronicCats/faultycat/HEAD/README.md) |
| Revision features | Hardware v2.1 lists additional trigger and voltage-fault-related support | [faultycat](https://raw.githubusercontent.com/ElectronicCats/faultycat/HEAD/README.md) |
| Maturity detail | Upstream distinguishes publicly exposed SWD scan from other work-in-progress debug functions | [faultycat](https://raw.githubusercontent.com/ElectronicCats/faultycat/HEAD/README.md) |
| Handling | Maker says the protective shield is essential and disclaims professional/educational safety certification | [faultycat](https://raw.githubusercontent.com/ElectronicCats/faultycat/HEAD/README.md) |

## Our review

FaultyCat belongs on a specialist hardware-research bench, not on a beginner’s general-purpose tool list. Its open hardware and separated host/firmware documentation are useful for studying the complete instrument, but electrical handling and version matching are major ownership costs. We would buy a traceable supported unit only for a defined supervised research requirement, and select a different certified instrument where institutional safety requirements demand it.

## Choose it when

You have a defined specialist research setup and can meet the maker’s handling requirements.

## Skip it when

You want a casual beginner multitool or need safety certification the maker does not claim.

## Compatibility and limitations

The maker’s current documentation is explicit about exposed high voltage and the need for its protective shield. It also separates hardware revision from firmware feature availability; a broad JTAG/SWD label does not establish every debug verb is implemented. We did not operate the device or reproduce a fault experiment.

## Alternatives

An appropriately certified fault-research instrument or a lower-risk simulation/benign training fixture.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/esp32-firmware.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Review the exact hardware, firmware and host-tool documentation with the bench owner before any powered evaluation; use an owned noncritical reference target.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Faultycat](https://raw.githubusercontent.com/ElectronicCats/faultycat/HEAD/README.md) — retrieved 2026-11-02; SHA-256 `534ed7f625b349532d695abeb5d57d16d1d8615e84b1d507f528f8b801943b12`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
