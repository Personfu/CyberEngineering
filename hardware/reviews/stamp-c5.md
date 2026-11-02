# M5Stack Stamp-C5

**Independent documentation review · 2026-11-02**

A compact dual-band wireless module with a much smaller memory configuration than some C5 boards.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Controller | ESP32-C5HF4 single-core RISC-V up to 240 MHz | [official-stampc5](https://docs.m5stack.com/en/core/Stamp-C5) |
| Memory | 4 MB flash and 384 KB SRAM are documented | [official-stampc5](https://docs.m5stack.com/en/core/Stamp-C5) |
| Radio | 2.4/5 GHz Wi-Fi 6, BLE 5 and IEEE 802.15.4 | [official-stampc5](https://docs.m5stack.com/en/core/Stamp-C5) |
| Expansion | 11 pad GPIO plus 8 FPC GPIO; 2.54 mm pad pitch | [official-stampc5](https://docs.m5stack.com/en/core/Stamp-C5) |
| Power | USB-C, 3.7 V battery input and charging IC | [official-stampc5](https://docs.m5stack.com/en/core/Stamp-C5) |

## Our review

Stamp-C5 makes sense when the objective is to integrate a small dual-band module into your own hardware. Its exposed pads and FPC resources are more relevant than a screen or preinstalled application. We would choose it over a larger development kit only when size and integration justify harder probing and tighter resource planning. It is not a memory-equivalent replacement for an 8 MB PSRAM XIAO C5.

## Choose it when

A small, pad/FPC-connected wireless controller fits a custom design.

## Skip it when

You need a ready-made UI or assume every C5 board has the same flash/PSRAM.

## Compatibility and limitations

The maker separates bare and DIP package contents, including whether the FPC connector is fitted. The manual also specifies output-load decoupling guidance and warns about FPC pin sequence. Read the exact schematic before attaching a carrier. Radio-band support does not establish a specific protocol application is implemented in your firmware.

## Alternatives

XIAO C5 for its documented memory/features; a full C5 dev kit for easier access.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/esp32-firmware.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Confirm package/connector population, pin sequence and power budget, then test a minimal application on an owned dual-band access point.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Manufacturer: Stampc5](https://docs.m5stack.com/en/core/Stamp-C5) — retrieved 2026-11-02; SHA-256 `2ed4afe47f8248602e7f072a7e23b4d721425527afe3d791d0b732e7381150a7`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
