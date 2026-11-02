# Meshnology N39

**Independent documentation review · 2026-11-02**

A Heltec WiFi LoRa 32 V4 package that needs careful base-board and revision verification.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Base board | Maker lists Heltec WiFi LoRa 32 V4 | [meshnology-n39](https://raw.githubusercontent.com/Meshnology/meshnology_doc/HEAD/N39/Meshnology%20N39/index.html) |
| Documented controller | ESP32-S3R2 | [meshnology-n39](https://raw.githubusercontent.com/Meshnology/meshnology_doc/HEAD/N39/Meshnology%20N39/index.html) |
| Memory | Maker lists 16 MB flash and 2 MB PSRAM | [meshnology-n39](https://raw.githubusercontent.com/Meshnology/meshnology_doc/HEAD/N39/Meshnology%20N39/index.html) |
| Display / radio | 0.96-inch OLED and SX1262 | [meshnology-n39](https://raw.githubusercontent.com/Meshnology/meshnology_doc/HEAD/N39/Meshnology%20N39/index.html) |
| Kit | Maker lists 3000 mAh battery, antenna and printed protective case | [meshnology-n39](https://raw.githubusercontent.com/Meshnology/meshnology_doc/HEAD/N39/Meshnology%20N39/index.html) |

## Our review

N39 is attractive if you want a packaged ESP32-based development node and do not want to assemble the enclosure and battery yourself. Its actual value is the package and documented base-board lineage. We would compare it directly with the same Heltec board plus equivalent accessories, and verify the delivered chip marking before choosing an image. The current existence of a different V4-R8 target makes that last step essential.

## Choose it when

You want the documented V4-based kit and will confirm the base revision.

## Skip it when

You need included GNSS, a V4-R8-specific interface or an unverified endurance guarantee.

## Compatibility and limitations

The maker’s setup section uses V3 as an example even though the product is V4-based. Treat it as a workflow illustration, not proof that any V3 image is right. GNSS is described as an expansion option, not universally included. The maker’s power figures and ratings were not reproduced.

## Alternatives

Bare Heltec V4 plus accessories; Wio L1 Pro for an nRF52840-based package.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/mesh-node.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Inspect the chip/board and accessories, use the matching target, and repeat a local delivery/power test with optional GNSS explicitly recorded.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Meshnology N39](https://raw.githubusercontent.com/Meshnology/meshnology_doc/HEAD/N39/Meshnology%20N39/index.html) — retrieved 2026-11-02; SHA-256 `88f1da16c47fe50d05c54029c840b057fc7616ed1be8a6fa89ac462b21b883e2`.
- [Mesh Heltec](https://raw.githubusercontent.com/meshtastic/meshtastic/HEAD/docs/hardware/devices/heltec-automation/lora32/index.mdx) — retrieved 2026-11-02; SHA-256 `f78635fa46bd268e7f759010586816cfa6e3cb29c2419571509c2cab514fe16e`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
