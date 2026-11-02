# PINGEQUA Hydra RF 424 Cap

**Independent documentation review · 2026-11-02**

A 433 MHz-oriented dual-radio expansion specifically for Cardputer ADV.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Host | Cardputer ADV only, via its 18-pin expansion header | [pingequa](https://raw.githubusercontent.com/pingequalab/cardputer-adv-hydra-rf/HEAD/README.md) |
| Radios | CC1101 plus nRF24L01 | [pingequa](https://raw.githubusercontent.com/pingequalab/cardputer-adv-hydra-rf/HEAD/README.md) |
| Variant | 424 Cap is the maker’s 433 MHz version | [pingequa](https://raw.githubusercontent.com/pingequalab/cardputer-adv-hydra-rf/HEAD/README.md) |
| Switching | Maker documents hardware mutual exclusion between radio chips | [pingequa](https://raw.githubusercontent.com/pingequalab/cardputer-adv-hydra-rf/HEAD/README.md) |
| Firmware | Bruce with model-specific pin configuration | [pingequa](https://raw.githubusercontent.com/pingequalab/cardputer-adv-hydra-rf/HEAD/README.md) |
| Cross-source discrepancy | Hydra maker describes an 18-pin host interface; M5Stack lists a 14-pin EXT port plus Grove. Verify the exact connector/pin map before purchase. | [official-cardputer-adv](https://docs.m5stack.com/en/core/Cardputer-Adv) |

## Our review

Choose the 424 Cap if you already own a Cardputer ADV and need this particular pair of interfaces in a compact attachment. The important buying advantage is integration, not a claim that two radios make a general-purpose spectrum analyzer. Hardware mutual exclusion also means the board is not a simultaneous two-radio measurement system. We would prefer this documented module to an unspecified generic add-on when avoiding a wiring project is worth the cost.

## Choose it when

You have an ADV and a defined 433 MHz plus nRF24 experiment.

## Skip it when

You own an original non-ADV Cardputer, require LoRa, or need simultaneous independent reception.

## Compatibility and limitations

The original Cardputer lacks the required ADV header and is explicitly not supported. The module is not a LoRa radio merely because a regional band overlaps. Maker claims about output power and antenna optimization are specifications/marketing, not our measured RF results. Current manufacturer and accessory descriptions disagree on connector count. This discrepancy is recorded rather than resolved by guessing.

## Alternatives

Hydra 824/924 for the maker’s other regional variants; a dedicated SDR for general signal analysis.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/esp32-firmware.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Check host revision and configured pins, then validate one owned reference fixture per radio and record which interface is active.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Pingequa](https://raw.githubusercontent.com/pingequalab/cardputer-adv-hydra-rf/HEAD/README.md) — retrieved 2026-11-02; SHA-256 `6a2dab07787c6c88e5996d22458efe516bae745ad95b4c478f2ef80065d137b7`.
- [Manufacturer: Cardputer Adv](https://docs.m5stack.com/en/core/Cardputer-Adv) — retrieved 2026-11-02; SHA-256 `079e25371ad55b25fa967dde7efee735674aa464f621439d171767f972296ac1`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
