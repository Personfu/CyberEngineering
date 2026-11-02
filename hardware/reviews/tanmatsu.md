# Tanmatsu

**Independent documentation review · 2026-11-02**

An embedded terminal with a substantial display and keyboard, rather than a conventional Linux laptop.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Application processor | ESP32-P4NRW32, dual-core RISC-V up to 400 MHz; 32 MB RAM and 16 MB flash are documented | [tanmatsu-specs](https://raw.githubusercontent.com/Nicolai-Electronics/tanmatsu-documentation/HEAD/src/hardware/specifications/index.md) |
| Wireless coprocessor | ESP32-C6 with 2.4 GHz Wi-Fi 6, BLE and IEEE 802.15.4 | [tanmatsu-specs](https://raw.githubusercontent.com/Nicolai-Electronics/tanmatsu-documentation/HEAD/src/hardware/specifications/index.md) |
| Display | 3.97-inch 480×800 MIPI-DSI panel | [tanmatsu-specs](https://raw.githubusercontent.com/Nicolai-Electronics/tanmatsu-documentation/HEAD/src/hardware/specifications/index.md) |
| Input | 69-key backlit keyboard | [tanmatsu-specs](https://raw.githubusercontent.com/Nicolai-Electronics/tanmatsu-documentation/HEAD/src/hardware/specifications/index.md) |
| Expansion | USB host/device, microSD, I²C/I³C, personality module and LoRa options | [tanmatsu-specs](https://raw.githubusercontent.com/Nicolai-Electronics/tanmatsu-documentation/HEAD/src/hardware/specifications/index.md) |

## Our review

Tanmatsu is compelling for engineers who want to build an embedded terminal application with room for meaningful text and controls. The P4/C6 split separates application processing from radio duties, while a management coprocessor handles keyboard and power functions. That architecture offers more insight than a generic “cyberdeck” description. Choose it for ESP-IDF applications and hardware integration; choose a CM5 handheld when installing ordinary Linux packages is the main requirement.

## Choose it when

You want a large embedded UI, a physical keyboard and extensible hardware.

## Skip it when

Your project requires a general-purpose desktop Linux software stack without porting.

## Compatibility and limitations

The specification page explicitly warns that it is being worked on and may contain errors. It also distinguishes display hardware capability from current software color support. LoRa is a selected module/band, not a universal radio. The source still contains some shipment-era wording, so present availability and spare-part stock remain unverified.

## Alternatives

HackberryPi CM5 or uConsole for Linux; Tab5 for a touch-oriented embedded interface.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/linux-cyberdeck.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Pin the hardware and firmware documentation, validate a minimal keyboard/display application and check which expansion functions share pins or buses.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Tanmatsu Specs](https://raw.githubusercontent.com/Nicolai-Electronics/tanmatsu-documentation/HEAD/src/hardware/specifications/index.md) — retrieved 2026-11-02; SHA-256 `1f4bfc2950b56403b44276d9d07745719412e08f206909b8b6cab35327500db3`.
- [Tanmatsu](https://raw.githubusercontent.com/Nicolai-Electronics/tanmatsu-hardware/HEAD/README.md) — retrieved 2026-11-02; SHA-256 `59518191336a74fc495d3254251225f3b1fe9284ff16090460a5022cc998f8d2`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
