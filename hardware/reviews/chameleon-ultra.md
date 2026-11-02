# Chameleon Ultra

**Independent documentation review · 2026-11-02**

A dedicated RFID research/emulation candidate with several documented client choices.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Controller | nRF52840 with BLE and USB, described in the technical whitepaper | [chameleon-whitepaper](https://github.com/RfidResearchGroup/ChameleonUltra/wiki/technical_whitepaper) |
| RF hardware | 125 kHz LF and 13.56 MHz HF antennas; Ultra includes an MFRC522 reader chip | [chameleon-hardware](https://github.com/RfidResearchGroup/ChameleonUltra/wiki/hardware) |
| Physical design | Two PCB structure, ferrite spacer, USB-C and eight slot indicators | [chameleon-hardware](https://github.com/RfidResearchGroup/ChameleonUltra/wiki/hardware) |
| Scope distinction | Ultra and Devkit can read/write supported HF 14a tags; Lite lacks that reader chip | [chameleon-hardware](https://github.com/RfidResearchGroup/ChameleonUltra/wiki/hardware) |

## Our review

Chameleon Ultra is the portable choice when a supported RFID emulation workflow is the main task and you also need the Ultra’s HF reader hardware. Its architecture uses the nRF52840 NFC peripheral for emulation and a separate MFRC522 for reader duties, which is more informative than calling it a universal NFC tool. We would choose it over Lite when reader capability is required, and over the larger Devkit when carrying the finished device matters more than probing its electronics.

## Choose it when

You have a defined RFID emulation experiment and a documented compatible client.

## Skip it when

You expect a universal credential emulator or want to infer authenticity from a marketplace photograph.

## Compatibility and limitations

The whitepaper separates hardware, software and application-layer support; possible silicon functions are not all implemented user features. It also contains comparative performance claims and historical tables that we have not independently reproduced. Do not infer broad DESFire or every LF protocol support from the presence of antennas. Confirm the exact tag mode against current firmware/client documentation.

## Alternatives

Proxmark3 RDV4 for detailed host-driven work; Flipper Zero for a broader portable interface set.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/rfid-bench.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Build a client/firmware compatibility record using your own reference reader and tags; distinguish successful emulation from general protocol security.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Chameleon Hardware](https://github.com/RfidResearchGroup/ChameleonUltra/wiki/hardware) — retrieved 2026-11-02; SHA-256 `0d982c75c5f08f6ff109e0d575be8c61c2b4f7796bb8014aed4ee6daa23a660f`.
- [Chameleon Whitepaper](https://github.com/RfidResearchGroup/ChameleonUltra/wiki/technical_whitepaper) — retrieved 2026-11-02; SHA-256 `6f93b8da07a9cc5a9753f9a58aff0fd9e8b3db195fc6ea5e40b11db117226745`.
- [Chameleon](https://raw.githubusercontent.com/RfidResearchGroup/ChameleonUltra/main/README.md) — retrieved 2026-11-02; SHA-256 `5c2866282450d276b0042611a244e81eb516d5c22ca61c7478ae71b858f9b1e1`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
