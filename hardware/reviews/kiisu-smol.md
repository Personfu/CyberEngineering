# KIISU SMOL

**Independent documentation review · 2026-11-02**

A modular STM32WB55 platform with published schematics and a deliberately limited scope of open CAD material.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Main MCU | STM32WB55, Cortex-M4 at 64 MHz, 1 MB flash and 256 KB RAM | [kiisu-smol](https://raw.githubusercontent.com/kiisu-io/kiisu-smol/HEAD/README.md) |
| Interfaces | CC1101 Sub-GHz, ST25R3916 NFC, LF RFID, IR and Bluetooth are documented | [kiisu-smol](https://raw.githubusercontent.com/kiisu-io/kiisu-smol/HEAD/README.md) |
| Display / storage | 128×64 OLED and soldered 512 MB SD | [kiisu-smol](https://raw.githubusercontent.com/kiisu-io/kiisu-smol/HEAD/README.md) |
| Expansion | Maker describes Flipper-compatible GPIO and separate Wi-Fi/GNSS/LoRa modules | [kiisu-smol](https://raw.githubusercontent.com/kiisu-io/kiisu-smol/HEAD/README.md) |
| Published design | Mainboard PDF schematic/3D model; complete CAD is published only for the sample extension board | [kiisu-smol](https://raw.githubusercontent.com/kiisu-io/kiisu-smol/HEAD/README.md) |

## Our review

SMOL is interesting when modular interfaces and a Flipper-related software lineage match the intended embedded project. Its published schematic and extension example provide more concrete evidence than a “Flipper killer” comparison. We would evaluate it as a distinct hardware/firmware ecosystem: compatible GPIO and related firmware do not guarantee binary compatibility, equivalent RF performance or the same accessory behavior.

## Choose it when

You want to develop against the documented modular architecture and accept its current support/supply questions.

## Skip it when

You need a verified shipping/support history or editable native CAD for the mainboard.

## Compatibility and limitations

The retrieved README still describes crowdfunding and does not establish current fulfillment or production reliability. It explicitly says original mainboard CAD sources are not published, so a claim that every design file is open would be inaccurate. Optional modules remain separate purchases and compatibility checks.

## Alternatives

Flipper Zero for its own ecosystem; Monstatek M1 for a separately documented architecture.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/esp32-firmware.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Identify production revision and firmware source, reconcile the schematic with attached modules and validate one owned fixture per required interface.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Kiisu Smol](https://raw.githubusercontent.com/kiisu-io/kiisu-smol/HEAD/README.md) — retrieved 2026-11-02; SHA-256 `014e7e426a0474dad5916d1a1af19134993b2876a0f299e16d3cb213840599ef`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
