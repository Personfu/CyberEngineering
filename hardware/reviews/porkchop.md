# Porkchop for Cardputer

**Independent documentation review · 2026-11-02**

A keyboard-oriented firmware whose memory budget and optional C5 coprocessor materially shape capabilities.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Host described | M5Cardputer/ADV with ESP32-S3, 8 MB flash and no PSRAM in the documented configuration | [porkchop](https://raw.githubusercontent.com/0ct0sec/M5Porkchop/HEAD/README.md) |
| Interface | 240×135 ST7789V2 screen and 56-key keyboard are described | [porkchop](https://raw.githubusercontent.com/0ct0sec/M5Porkchop/HEAD/README.md) |
| Optional dual-band path | M5MonsterC5 coprocessor is separately documented | [porkchop](https://raw.githubusercontent.com/0ct0sec/M5Porkchop/HEAD/README.md) |
| Optional location/radio | CapLoRa868 is a separate module | [porkchop](https://raw.githubusercontent.com/0ct0sec/M5Porkchop/HEAD/README.md) |
| Memory discipline | README calls out the limited usable internal heap | [porkchop](https://raw.githubusercontent.com/0ct0sec/M5Porkchop/HEAD/README.md) |

## Our review

Porkchop is a useful choice when physical text input and a focused Cardputer workflow matter more than a touchscreen interface. The important architectural fact is that dual-band work in the documented configuration uses another C5 processor; it is not a newly discovered capability of the S3 alone. Similarly, GNSS and LoRa depend on the attached module. That separation makes the full hardware inventory more informative than a feature roundup.

## Choose it when

You want this documented keyboard-first firmware and understand its optional-module architecture.

## Skip it when

You expect all branded ports or a bare S3 host to provide identical dual-band features.

## Compatibility and limitations

The retrieved README describes a particular current configuration, not interchangeable behavior across every port named Porkchop, Panchetta or Hamlet. Its memory constraints and partition choices are part of the software fit. We did not execute or validate the project’s wireless/security claims.

## Alternatives

Compare the individually reviewed Bruce, Marauder, GhostESP, HaleHound, Porkchop or Meshtastic workflows against the actual task.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/esp32-firmware.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Pin source/release and board target, preserve a recovery image, and verify one benign owned-fixture task with an inspectable output before extending the system.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Porkchop](https://raw.githubusercontent.com/0ct0sec/M5Porkchop/HEAD/README.md) — retrieved 2026-11-02; SHA-256 `d02f97ed4dcd862444476a55aae7890bdff5fb2cdd55429119e583ac78b8fa08`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
