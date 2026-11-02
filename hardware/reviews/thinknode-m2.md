# Elecrow ThinkNode M2

**Independent documentation review · 2026-11-02**

A model-specific mesh-node choice with a documented integration target.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| MCU | ESP32-S3 | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |
| LoRa transceiver | SX1262 | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |
| Model features | 1.3-inch OLED; no GNSS listed in this model’s specification | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |
| Power / connections | 1000 mAh; USB-C; U.FL/IPEX LoRa connector | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |
| Bands | Check the region-specific 868/915 MHz hardware options in the source | [mesh-thinknode](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/elecrow/thinknode/index.mdx) |

## Our review

M2 fits a small status node when an ESP32-S3 platform and OLED suit the task better than the M1’s GNSS/e-paper package. We would select it for its documented hardware combination, not as a cheaper equivalent of every ThinkNode. If location is essential, first establish a supported location source instead of assuming one is built in. Judge complete system fit before comparing enclosure size or an advertised range figure.

## Choose it when

You want a compact OLED/ESP32-based node and have no requirement for a documented onboard GNSS.

## Skip it when

Your purchase depends on included GNSS or on an unverified Bluetooth-version claim.

## Compatibility and limitations

The integration page has an inconsistent vendor-link label and Bluetooth-version wording, so we do not adopt those fields as verified specifications. The MCU, display and radio are the unambiguous documented model distinctions. M2 uses its own BIN firmware target.

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
