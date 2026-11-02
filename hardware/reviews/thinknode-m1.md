# Elecrow ThinkNode M1

**Independent documentation review · 2026-11-02**

A model-specific mesh-node choice with a documented integration target.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| MCU | nRF52840 | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |
| LoRa transceiver | SX1262 | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |
| Model features | L76K GNSS; 1.54-inch e-paper | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |
| Power / connections | 1200 mAh; USB-C; RP-SMA antenna connection | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |
| Bands | Check the region-specific 868/915 MHz hardware options in the source | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |

## Our review

M1 is the straightforward handheld choice when you want location, a persistent small display and an nRF52-based firmware target in one package. It is a more focused mesh purchase than a general ESP32 multitool. The e-paper screen favors occasional status changes rather than a live dashboard. Judge complete system fit before comparing enclosure size or an advertised range figure.

## Choose it when

A compact self-contained mesh handset with GNSS and a low-update-rate display is the goal.

## Skip it when

Wi-Fi-based integration or a full keyboard is a requirement.

## Compatibility and limitations

The M1 UF2 firmware is distinct from the M5 BIN target. Do not infer that their similar screens or battery capacities make their MCU and update workflows interchangeable. No delivery range or runtime was measured.

## Alternatives

Compare the other individually documented ThinkNode models, Heltec Mesh Node T1 and Seeed Wio Tracker L1 Pro by deployment role.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/mesh-node.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Use the correct model target and owned peer nodes; log delivery counts, delays, configuration recovery and actual power conditions on a repeatable fixture.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Mesh Thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) — retrieved 2026-11-02; SHA-256 `62b934fbeb13631f77bc20e8a736f1a8956c9f6320493a3b09f24ab3e9bae004`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
