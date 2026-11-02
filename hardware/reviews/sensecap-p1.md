# Seeed SenseCAP Solar Node P1

**Independent documentation review · 2026-11-02**

A fixed outdoor solar node, with an important P1 versus P1 Pro package distinction.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Controller / radio | nRF52840 and SX1262 | [mesh-solar](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/seeed-studio/sensecap/solar-node.mdx) |
| Solar panel | 5 W is documented | [mesh-solar](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/seeed-studio/sensecap/solar-node.mdx) |
| Package | Four 18650 slots; cells are not included | [mesh-solar](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/seeed-studio/sensecap/solar-node.mdx) |
| Expansion | Internal Grove, USB-C and RP-SMA antenna connection | [mesh-solar](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/seeed-studio/sensecap/solar-node.mdx) |

## Our review

P1 makes sense when you want to choose the cells yourself and can budget an outdoor installation properly. It removes panel/enclosure fabrication work, but it is not a complete battery-equipped package. Include cells, mounting and maintenance access in the actual project cost. The node is better matched to a deliberately installed repeater/sensor role than to carried text entry. Panel orientation, shading and radio workload are engineering inputs, so evaluate the whole installation rather than treating the panel wattage as an endurance result.

## Choose it when

You have a fixed outdoor deployment with a documented sunlight and maintenance plan.

## Skip it when

You need a pocket handset, an indoor PoE gateway or a guaranteed winter autonomy figure.

## Compatibility and limitations

The primary page publishes an open-area range claim, but no such range was tested here. Regional hardware, cells, charge conditions and mounting still require validation. Four cell ratings cannot be turned into a runtime estimate without the pack arrangement and measured energy budget.

## Alternatives

ThinkNode M6 for another solar package; M7 when wired indoor infrastructure is available.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/mesh-node.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Log daily charging and load energy, delivery counts, brownouts and weather over a representative period before relying on unattended service.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Mesh Solar](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/seeed-studio/sensecap/solar-node.mdx) — retrieved 2026-11-02; SHA-256 `3ced29bc0cec7b9aad38168cf7e7edc803d50535adf0a947248dddce12a27c8b`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
