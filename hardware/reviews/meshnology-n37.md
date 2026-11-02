# Meshnology N37

**Independent documentation review · 2026-11-02**

A packaged Wio Tracker L1-based node whose bill of materials is the useful buying distinction.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Base platform | Maker identifies the Seeed Wio Tracker L1 | [meshnology-n37](https://raw.githubusercontent.com/Meshnology/meshnology_doc/HEAD/N37_Series/Meshnology%20N37/index.html) |
| Controller / radio | nRF52840 and SX1262 | [meshnology-n37](https://raw.githubusercontent.com/Meshnology/meshnology_doc/HEAD/N37_Series/Meshnology%20N37/index.html) |
| Location / display | L76K GNSS and 1.3-inch 128×64 OLED | [meshnology-n37](https://raw.githubusercontent.com/Meshnology/meshnology_doc/HEAD/N37_Series/Meshnology%20N37/index.html) |
| Listed kit | Board, antenna, GPS module, 3000 mAh battery and N37 printed enclosure | [meshnology-n37](https://raw.githubusercontent.com/Meshnology/meshnology_doc/HEAD/N37_Series/Meshnology%20N37/index.html) |
| Firmware | Maker directs the L1/Lite/Pro packages to the Seeed Wio Tracker L1 target | [meshnology-n37](https://raw.githubusercontent.com/Meshnology/meshnology_doc/HEAD/N37_Series/Meshnology%20N37/index.html) |

## Our review

N37 should be compared with a self-assembled L1 kit, not assumed to be an unrelated new radio architecture. Its benefit is the bundled enclosure and power/accessory integration. We would choose it when that assembly work is the obstacle, while checking the exact seller package rather than assuming every N37 listing includes identical parts. The primary documentation is specific enough to trace the underlying board, which is more useful than a renamed enclosure.

## Choose it when

You want an L1-based portable kit with the documented enclosure and battery bundle.

## Skip it when

You already have the board/accessories or expect a distinct radio architecture from the N37 name.

## Compatibility and limitations

The maker’s document mixes general L1-family instructions with N37 packaging information. Use the exact base-board firmware guidance and inspect the delivered power connections. No certification, charging performance or runtime was independently verified.

## Alternatives

Wio Tracker L1 Pro; a self-assembled L1 kit.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/mesh-node.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Reconcile the delivered contents with the base-board identity and test charging, boot recovery and a repeated owned-node route.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Meshnology N37](https://raw.githubusercontent.com/Meshnology/meshnology_doc/HEAD/N37_Series/Meshnology%20N37/index.html) — retrieved 2026-11-02; SHA-256 `d35bb07a7de066f164ce6858fb3cd6834ab11f14b17f3be4834a4cbccf601f01`.
- [Mesh Wio](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/seeed-studio/wio-series/wio-tracker-l1.mdx) — retrieved 2026-11-02; SHA-256 `b5cbb490598cb51b4fcea31c9712c1c1837c7605c0f9732b76511cece3319c53`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
