# JCMK ESP32 Dual Band Wardriver

**Independent documentation review · 2026-11-02**

A documented C5 survey/logging platform with meaningful board-variant and clean-install/update distinctions.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Base platform | ESP32-C5-DevKitC-1 v1.2; JCMK host board and T-Dongle C5 are separate targets | [dualband-wardriver](https://raw.githubusercontent.com/justcallmekoko/ESP32DualBandWardriver/HEAD/README.md) |
| Observation | 2.4/5 GHz Wi-Fi and BLE logging | [dualband-wardriver](https://raw.githubusercontent.com/justcallmekoko/ESP32DualBandWardriver/HEAD/README.md) |
| Storage | WiGLE-formatted logs on SD; web/admin dock workflows are documented | [dualband-wardriver](https://raw.githubusercontent.com/justcallmekoko/ESP32DualBandWardriver/HEAD/README.md) |
| Installer | Official Web Serial installer supports clean installation and compatible-layout update modes | [dualband-wardriver](https://raw.githubusercontent.com/justcallmekoko/ESP32DualBandWardriver/HEAD/README.md) |
| Peripheral detail | Display, GPS, SD, fuel gauge and button wiring are documented by target | [dualband-wardriver](https://raw.githubusercontent.com/justcallmekoko/ESP32DualBandWardriver/HEAD/README.md) |

## Our review

This is a better-defined survey-system candidate than a generic list of wireless screens. Its installer documentation makes a particularly useful distinction: a new/unknown flash layout needs a clean installation, while preserving settings assumes a compatible existing layout. The same C5 chip cannot tell the installer whether the attached board is the JCMK host or the T-Dongle. We would choose it for a recorded, privacy-minimized survey task with an inspectable log format.

## Choose it when

You need a supported C5 logging platform with documented exports and recovery choices.

## Skip it when

You need a general SDR or assume every C5 carrier can use the same binary.

## Compatibility and limitations

Chip detection is not board detection; the maker explicitly warns that the two variants configure different pins and peripherals. Log identifiers do not establish owner identity or a precise position. Use a controlled owned-network fixture first, retain only the data needed and review upload destinations separately.

## Alternatives

A supported Linux survey adapter for a host workflow; a simpler development board for a custom logger.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/esp32-firmware.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Confirm the selected board and layout, use an owned access point/GNSS fixture and inspect export timestamps, missing positions and duplicate records.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Dualband Wardriver](https://raw.githubusercontent.com/justcallmekoko/ESP32DualBandWardriver/HEAD/README.md) — retrieved 2026-11-02; SHA-256 `8837b9899e1e5ecaa4792293c8eeac4c7458e8801bcaa7fc6da46b7104b4eea6`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
