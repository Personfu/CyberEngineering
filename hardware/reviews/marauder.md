# ESP32 Marauder

**Independent documentation review · 2026-11-02**

A Wi-Fi/Bluetooth firmware and hardware ecosystem with explicit module-level hardware distinctions.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Scope | Upstream describes Wi-Fi/Bluetooth offensive and defensive tools | [marauder](https://raw.githubusercontent.com/justcallmekoko/ESP32Marauder/master/README.md) |
| Distribution | Official firmware releases and project wiki | [marauder](https://raw.githubusercontent.com/justcallmekoko/ESP32Marauder/master/README.md) |
| Newer hardware | Marauder v8, Mini v3 and C5 Wardriver are listed with ESP32-C5-WROOM-U | [marauder](https://raw.githubusercontent.com/justcallmekoko/ESP32Marauder/master/README.md) |
| Legacy distinction | Older board groups list ESP32-WROOM-32U or 32E | [marauder](https://raw.githubusercontent.com/justcallmekoko/ESP32Marauder/master/README.md) |
| Certification scope | README explicitly distinguishes a radio-module FCC ID from end-product certification | [marauder](https://raw.githubusercontent.com/justcallmekoko/ESP32Marauder/master/README.md) |

## Our review

Marauder is a sensible first comparison for an ESP32-based wireless lab because the project identifies its hardware lineage and points to releases and a maintained wiki. The recent C5 boards should not be conflated with older ESP32 boards: module identity can change the available radio platform. Its explicit certification wording is also useful engineering documentation, because a module identifier is not a blanket assurance for every enclosure and carrier.

## Choose it when

You want a documented ESP32 wireless workflow on a supported board.

## Skip it when

You require calibrated RF measurements or infer certification/feature parity from a shared firmware name.

## Compatibility and limitations

Third-party boards are deliberately left to hardware-label verification. A module table is not a complete supported-feature matrix or a performance result. Use the matching firmware and board documentation rather than assuming all Marauder products are equivalent.

## Alternatives

Compare the individually reviewed Bruce, Marauder, GhostESP, HaleHound, Porkchop or Meshtastic workflows against the actual task.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/esp32-firmware.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Pin source/release and board target, preserve a recovery image, and verify one benign owned-fixture task with an inspectable output before extending the system.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Marauder](https://raw.githubusercontent.com/justcallmekoko/ESP32Marauder/master/README.md) — retrieved 2026-11-02; SHA-256 `baf57f50dfb2eb103218674e30d91f8a9541aa4d659b42e91638a1c71cc84f7c`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
