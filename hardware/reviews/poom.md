# POOM platform

**Independent documentation review · 2026-11-02**

An ESP-IDF application platform with maker, capture and interaction domains.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Framework | The retrieved README specifies ESP-IDF v6.1.0 | [poom](https://raw.githubusercontent.com/The-POOM/the_poom/HEAD/README.md) |
| Primary targets | ESP32-C5 and ESP32-C6; the documented default is C6 | [poom](https://raw.githubusercontent.com/The-POOM/the_poom/HEAD/README.md) |
| Architecture | Separate applications, modules, drivers, kernel and third-party components | [poom](https://raw.githubusercontent.com/The-POOM/the_poom/HEAD/README.md) |
| Maker interfaces | I²C discovery, sensor streaming and dataset collection integrations are described | [poom](https://raw.githubusercontent.com/The-POOM/the_poom/HEAD/README.md) |
| Interaction | Controller, gaming and NFC-related workflows are documented | [poom](https://raw.githubusercontent.com/The-POOM/the_poom/HEAD/README.md) |

## Our review

POOM is best understood as a maintained embedded software platform to evaluate, not as proof that an unspecified handheld has every feature. Its split into applications and reusable modules is promising for an engineer who wants to add a well-defined acquisition or interaction workflow. We would begin with a supported C5/C6 target and a small maker-mode application before relying on the broader toolkit.

## Choose it when

You want to develop within its documented IDF and modular application structure.

## Skip it when

You need an independently benchmarked finished product based only on its multipurpose description.

## Compatibility and limitations

A README capability list is not a measured compatibility matrix for a shipping enclosure. Default target C6 does not make a C5 binary interchangeable. The reviewed source establishes architecture and documented targets; hardware packaging, current supply and real-time performance need separate evidence.

## Alternatives

Compare the individually reviewed Bruce, Marauder, GhostESP, HaleHound, Porkchop or Meshtastic workflows against the actual task.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/esp32-firmware.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Pin source/release and board target, preserve a recovery image, and verify one benign owned-fixture task with an inspectable output before extending the system.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Poom](https://raw.githubusercontent.com/The-POOM/the_poom/HEAD/README.md) — retrieved 2026-11-02; SHA-256 `a0c70c6cc51d638109d08756fc7c7704590ae3a09b50ce2aca0e8a0278b2e90c`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
