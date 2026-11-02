# PINGEQUA Hydra RF 824 Pro

**Independent documentation review · 2026-11-02**

A 868 MHz-oriented Cardputer ADV expansion, distinct from the 433 MHz Cap variant.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Host | Cardputer ADV 18-pin header only | [pingequa](https://raw.githubusercontent.com/pingequalab/cardputer-adv-hydra-rf/HEAD/README.md) |
| Variant | The maker identifies 868 MHz as this variant’s primary Sub-GHz band | [pingequa](https://raw.githubusercontent.com/pingequalab/cardputer-adv-hydra-rf/HEAD/README.md) |
| Radios | CC1101 and nRF24L01 | [pingequa](https://raw.githubusercontent.com/pingequalab/cardputer-adv-hydra-rf/HEAD/README.md) |
| Control | Hardware mutual exclusion; Bruce pin configuration | [pingequa](https://raw.githubusercontent.com/pingequalab/cardputer-adv-hydra-rf/HEAD/README.md) |
| Power | Host-powered with onboard regulation and bulk capacitance | [pingequa](https://raw.githubusercontent.com/pingequalab/cardputer-adv-hydra-rf/HEAD/README.md) |
| Cross-source discrepancy | Hydra maker describes an 18-pin host interface; M5Stack lists a 14-pin EXT port plus Grove. Verify the exact connector/pin map before purchase. | [official-cardputer-adv](https://docs.m5stack.com/en/core/Cardputer-Adv) |

## Our review

Choose this Pro variant when 868 MHz is the relevant documented hardware band and the ADV is already your intended controller. The product is an integration accessory, not an upgrade to the host’s core Wi-Fi chipset. Its two interfaces give a specific combination of Sub-GHz and nRF24 work; they do not make it an all-protocol radio. The manufacturer’s host restriction and variant table are more important than the shared Hydra name.

## Choose it when

An ADV-based project needs the documented 868 MHz variant and nRF24 interface.

## Skip it when

Your host lacks the ADV header or your actual requirement is a LoRa node or general SDR.

## Compatibility and limitations

Not compatible with the original Cardputer or Stick devices without the ADV header. Do not infer LoRa support from a matching frequency band. The documentation ties behavior to Bruce configuration and flags firmware-specific troubleshooting, so retain the exact release with the hardware inventory. Current manufacturer and accessory descriptions disagree on connector count. This discrepancy is recorded rather than resolved by guessing.

## Alternatives

Hydra 424 for a 433 MHz-focused build; a dedicated radio module for a single interface.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/esp32-firmware.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Validate host identity, band variant and pin configuration before comparing local reference observations across modules.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Pingequa](https://raw.githubusercontent.com/pingequalab/cardputer-adv-hydra-rf/HEAD/README.md) — retrieved 2026-11-02; SHA-256 `6a2dab07787c6c88e5996d22458efe516bae745ad95b4c478f2ef80065d137b7`.
- [Manufacturer: Cardputer Adv](https://docs.m5stack.com/en/core/Cardputer-Adv) — retrieved 2026-11-02; SHA-256 `079e25371ad55b25fa967dde7efee735674aa464f621439d171767f972296ac1`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
