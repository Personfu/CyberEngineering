# HaleHound-CYD

**Independent documentation review · 2026-11-02**

A touchscreen-focused CYD firmware whose expansion and power requirements are central to the build.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Retrieved version | README identifies v4.0 | [halehound](https://raw.githubusercontent.com/JesseCHale/HaleHound-CYD/HEAD/README.md) |
| Boards | ESP32-2432S028, QDtech E32R28T/E32R35T and an NM-RF-Hat target are listed separately | [halehound](https://raw.githubusercontent.com/JesseCHale/HaleHound-CYD/HEAD/README.md) |
| External interfaces | CC1101, nRF24, PN532 and GNSS modules are separate hardware | [halehound](https://raw.githubusercontent.com/JesseCHale/HaleHound-CYD/HEAD/README.md) |
| Power | Maintainer specifies independent suitable 3.3 V supply for certain amplified radio modules | [halehound](https://raw.githubusercontent.com/JesseCHale/HaleHound-CYD/HEAD/README.md) |
| Storage | FAT32 microSD is documented | [halehound](https://raw.githubusercontent.com/JesseCHale/HaleHound-CYD/HEAD/README.md) |

## Our review

Choose HaleHound if the goal is to understand and assemble a touchscreen multi-peripheral platform. The real work is not flashing an image; it is matching the display target, allocating shared buses and powering external modules properly. A board with no attached radio does not gain that radio because the menu contains it. We would favor this project for an engineer who wants to inspect the integration, while choosing a finished appliance for a less hands-on ownership model.

## Choose it when

You want a documented CYD assembly and can work through its peripheral/power inventory.

## Skip it when

You expect a cheap screen alone to deliver every radio/NFC function.

## Compatibility and limitations

Board-specific pin and backlight differences are explicitly documented. The source contains broad capability claims that have not been independently reproduced; this review relies on documented architecture and integration requirements rather than adopting every attack/detection claim.

## Alternatives

Compare the individually reviewed Bruce, Marauder, GhostESP, HaleHound, Porkchop or Meshtastic workflows against the actual task.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/esp32-firmware.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Pin source/release and board target, preserve a recovery image, and verify one benign owned-fixture task with an inspectable output before extending the system.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Halehound](https://raw.githubusercontent.com/JesseCHale/HaleHound-CYD/HEAD/README.md) — retrieved 2026-11-02; SHA-256 `86ff29da080b03d292a63d55b128ef5387a54c18a2b3e91857f20310b6f1cc3b`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
