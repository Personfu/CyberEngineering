# Cifertech ESP32-DIV

**Independent documentation review · 2026-11-02**

A touchscreen multi-interface ESP32-S3 project whose broad functions depend on a complete hardware build.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Platform | ESP32-S3 with touch interface | [esp32-div](https://raw.githubusercontent.com/cifertech/ESP32-DIV/HEAD/README.md) |
| Interface families | Wi-Fi/BLE, nRF24 2.4 GHz, Sub-GHz, IR, RFID/NFC and GPS are described | [esp32-div](https://raw.githubusercontent.com/cifertech/ESP32-DIV/HEAD/README.md) |
| Evidence outputs | Packet-monitor PCAP logging and saved IR/profile workflows are documented | [esp32-div](https://raw.githubusercontent.com/cifertech/ESP32-DIV/HEAD/README.md) |
| Distribution | Maintainer links a project wiki and official browser flasher | [esp32-div](https://raw.githubusercontent.com/cifertech/ESP32-DIV/HEAD/README.md) |

## Our review

ESP32-DIV is best understood as a buildable multi-peripheral platform, not a bare ESP32 magically gaining every radio. Its useful engineering role is to make the interaction between screen, storage, software and attached interfaces inspectable. We would select one required workflow and verify that hardware path before spending time on the whole application menu. The documented logging options are more useful for a review than dramatic feature names.

## Choose it when

You want to build and understand the documented S3 multi-interface project.

## Skip it when

You expect one firmware flash on an arbitrary screen board to establish all capabilities.

## Compatibility and limitations

The feature list includes active security-testing modes and detection claims that have not been reproduced here. Their presence is not a compatibility or accuracy benchmark. Source/board revisions, actual external modules and power design must be recorded independently.

## Alternatives

HaleHound for its CYD-specific integration; Bruce/GhostESP for their own board/app ecosystems.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/esp32-firmware.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Use a pinned build and one local, owned reference fixture; retain actual logs, configured pins and failed observations.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Esp32 Div](https://raw.githubusercontent.com/cifertech/ESP32-DIV/HEAD/README.md) — retrieved 2026-11-02; SHA-256 `df415fdefe20a509a4479d4a779aa4614f82657b74acf8a9e4375b2e946363d5`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
