# Elecrow ThinkNode M4

**Independent documentation review · 2026-11-02**

A model-specific mesh-node choice with a documented integration target.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| MCU | nRF52840 | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |
| LoRa transceiver | LR1110 | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |
| Model features | Multi-constellation GNSS; built-in ceramic GNSS antenna | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |
| Power / connections | 7000 mAh / 25.2 Wh documented pack; USB-C and Qi charging output | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |
| Bands | Check the region-specific 868/915 MHz hardware options in the source | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |

## Our review

M4 is worth considering when a power bank and mesh node would otherwise be separate carried items. That integration can reduce cables and duplicated hardware, but it couples two energy budgets: charging another device takes energy away from node operation. We would choose it for a deliberately combined kit, rather than treating the large capacity number as a runtime guarantee. Judge complete system fit before comparing enclosure size or an advertised range figure.

## Choose it when

You intentionally want combined mesh and portable-power functions.

## Skip it when

You need an independently budgeted fixed relay or a small card-shaped tracker.

## Compatibility and limitations

Published capacity and output features do not establish usable energy under your load or days of mesh operation. It is not equivalent to the weather-oriented M6. Its UF2 target and exact hardware band still need to match the unit.

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
