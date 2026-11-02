# Elecrow ThinkNode M6

**Independent documentation review · 2026-11-02**

A model-specific mesh-node choice with a documented integration target.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| MCU | nRF52840 | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |
| LoRa transceiver | SX1262 | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |
| Model features | L76K GNSS; waterproof I²C/UART expansion connectors | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |
| Power / connections | 6 W solar panel; two 18650 cells; IP65 enclosure is documented | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |
| Bands | Check the region-specific 868/915 MHz hardware options in the source | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |

## Our review

M6 belongs in a fixed outdoor-node comparison, not a pocket-handheld comparison. The integrated solar and protected expansion connectors can reduce enclosure work substantially. We would choose it when the deployment can support a proper mounting, sunlight and maintenance plan; a larger panel is not a substitute for a measured energy budget. Judge complete system fit before comparing enclosure size or an advertised range figure.

## Choose it when

The goal is an outdoor fixed node with a maintainable solar installation.

## Skip it when

You need an indoor PoE gateway or a carried messaging interface.

## Compatibility and limitations

The published environmental rating and operating range are manufacturer/integration documentation claims. Continuous winter operation and radio coverage remain site-specific questions. Check the actual included cells and regional model before comparing it with a solar-node bundle.

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
