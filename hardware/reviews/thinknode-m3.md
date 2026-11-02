# Elecrow ThinkNode M3

**Independent documentation review · 2026-11-02**

A model-specific mesh-node choice with a documented integration target.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| MCU | nRF52840 | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |
| LoRa transceiver | LR1110 | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |
| Model features | ATGM336H GNSS; temperature, humidity and accelerometer sensors | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |
| Power / connections | 770 mAh; magnetic charging cable; IP66 enclosure is documented | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |
| Bands | Check the region-specific 868/915 MHz hardware options in the source | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |

## Our review

M3 is the clearest tracker-style choice in the group: a card-shaped device with GNSS and environmental sensing rather than a large user interface. It makes sense when carried-object telemetry matters more than typing messages on the device. The four pogo contacts also make the supplied cable part of the ownership story, not a disposable accessory. Judge complete system fit before comparing enclosure size or an advertised range figure.

## Choose it when

A compact carried tracker with integrated sensors matches the project.

## Skip it when

You want a keyboard, an always-visible large status display or standard USB-C charging on the device.

## Compatibility and limitations

A water-resistance rating is a documented product claim, not an independently repeated ingress test. Budget for cable availability and the relatively small battery before using it as a fixed relay. The LR1110 differentiates it from SX1262 models; do not assume identical firmware.

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
