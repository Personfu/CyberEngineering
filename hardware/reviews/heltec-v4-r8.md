# Heltec WiFi LoRa 32 V4-R8

**Independent documentation review · 2026-11-02**

A development-board mesh node whose exact V4 variant is critical.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| MCU | ESP32-S3R8 | [mesh-heltec](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/heltec-automation/lora32/index.mdx) |
| Memory | 16 MB flash and 8 MB PSRAM | [mesh-heltec](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/heltec-automation/lora32/index.mdx) |
| Display | OLED or TFT variant | [mesh-heltec](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/heltec-automation/lora32/index.mdx) |
| LoRa | SX1262 with region-specific hardware options | [mesh-heltec](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/heltec-automation/lora32/index.mdx) |
| Firmware target | heltec-v4-r8-oled / heltec-v4-r8-tft | [mesh-heltec](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/heltec-automation/lora32/index.mdx) |

## Our review

V4-R8 is the better-defined option when additional PSRAM or a richer interface is the real requirement. Treat it as a separate hardware target rather than an incidental memory upgrade: the integration maintainer explicitly says the pinout and firmware differ from the original V4. We would buy on the exact chip marking and required firmware image before comparing advertised transmit power. Neither a higher output setting nor more PSRAM guarantees a better route through a real mesh.

## Choose it when

You want an exposed, documented development board and can supply a suitable enclosure/power system.

## Skip it when

You need a finished weatherproof tracker or cannot identify which V4 hardware you are buying.

## Compatibility and limitations

V4-R8 is not pin/firmware compatible with original V4. The integration manual calls for Meshtastic 2.7.25 or newer for V4-R8 and separates OLED/TFT images. Antenna, region, power and thermal conditions remain part of the system; no radio range was independently measured.

## Alternatives

Heltec Mesh Node T1 for a packaged tracker; Wio Tracker L1 for an nRF52840-based board.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/mesh-node.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Check the chip marking and display variant, pin the correct image, and validate boot, location source and a repeatable message/power test.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Mesh Heltec](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/heltec-automation/lora32/index.mdx) — retrieved 2026-11-02; SHA-256 `f78635fa46bd268e7f759010586816cfa6e3cb29c2419571509c2cab514fe16e`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
