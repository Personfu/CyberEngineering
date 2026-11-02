# ESP32-S31-Function-CoreBoard-1

**Independent documentation review · 2026-11-02**

An Espressif development-board candidate for connected audio/AIoT prototyping, not a generic substitute for every ESP32.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Module | ESP32-S31-WROOM-3 | [espressif](https://raw.githubusercontent.com/espressif/esp-dev-kits/HEAD/README.md) |
| Connectivity | Official board overview lists Wi-Fi 6, IEEE 802.15.4 and Bluetooth 5.4 LE/BR-EDR | [espressif](https://raw.githubusercontent.com/espressif/esp-dev-kits/HEAD/README.md) |
| Wired network | Gigabit Ethernet is listed | [espressif](https://raw.githubusercontent.com/espressif/esp-dev-kits/HEAD/README.md) |
| Audio | Onboard microphone and speaker output | [espressif](https://raw.githubusercontent.com/espressif/esp-dev-kits/HEAD/README.md) |
| Documentation | Espressif provides board-specific user guides and ESP-IDF target links | [espressif](https://raw.githubusercontent.com/espressif/esp-dev-kits/HEAD/README.md) |

## Our review

This board belongs on the shortlist when audio interaction and its documented mix of network interfaces match the application. It should not be bought solely because S31 is a newer name: the useful comparison is driver support and a reproducible end-to-end application against an established board. The official development-kit overview identifies the exact module and peripherals, which is a much firmer foundation than a first-look title.

## Choose it when

You are developing for this specific new platform and its documented audio/network interfaces.

## Skip it when

You need a drop-in board for existing firmware or measured accelerator performance.

## Compatibility and limitations

The retrieved overview is not a performance benchmark or confirmation that an arbitrary S3/C5 binary will run. Memory configurations and all electrical details need the exact board manual; those details are not established by this retrieved overview. No throughput or AI model-rate claim is made.

## Alternatives

A mature S3/C5 board for a simpler wireless project; Tab5 for an integrated touch interface.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/esp32-firmware.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Pin the ESP-IDF target and board revision and prove a minimal audio/network application before relying on higher-level AI demos.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Espressif](https://raw.githubusercontent.com/espressif/esp-dev-kits/HEAD/README.md) — retrieved 2026-11-02; SHA-256 `e7bbfd8b1066fcf2b018da3c50f47dd75a9893ecf0b73ca3056c81d3f5de4e9a`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
