# Seeed XIAO ESP32-C5

**Independent documentation review · 2026-11-02**

A small dual-band Wi-Fi board with a different architecture and pin map from XIAO S3.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Processor | Single-core 32-bit RISC-V ESP32-C5 up to 240 MHz | [xiao-c5](https://raw.githubusercontent.com/Seeed-Studio/wiki-documents/HEAD/sites/en/docs/Sensor/SeeedStudio_XIAO/SeeedStudio_XIAO_ESP32C5/XIAO_ESP32C5_Getting_Started.md) |
| Radio | 2.4/5 GHz Wi-Fi 6 and Bluetooth 5 LE | [xiao-c5](https://raw.githubusercontent.com/Seeed-Studio/wiki-documents/HEAD/sites/en/docs/Sensor/SeeedStudio_XIAO/SeeedStudio_XIAO_ESP32C5/XIAO_ESP32C5_Getting_Started.md) |
| Memory | 8 MB PSRAM and 8 MB flash | [xiao-c5](https://raw.githubusercontent.com/Seeed-Studio/wiki-documents/HEAD/sites/en/docs/Sensor/SeeedStudio_XIAO/SeeedStudio_XIAO_ESP32C5/XIAO_ESP32C5_Getting_Started.md) |
| I/O | Up to 11 GPIO, five ADC channels, I²C, SPI and two UART interfaces | [xiao-c5](https://raw.githubusercontent.com/Seeed-Studio/wiki-documents/HEAD/sites/en/docs/Sensor/SeeedStudio_XIAO/SeeedStudio_XIAO_ESP32C5/XIAO_ESP32C5_Getting_Started.md) |
| Size | 21×17.8 mm; external RF antenna is documented | [xiao-c5](https://raw.githubusercontent.com/Seeed-Studio/wiki-documents/HEAD/sites/en/docs/Sensor/SeeedStudio_XIAO/SeeedStudio_XIAO_ESP32C5/XIAO_ESP32C5_Getting_Started.md) |

## Our review

Choose XIAO C5 when 5 GHz Wi-Fi is a real project requirement and a small board is useful. It is not simply a faster S3: the processor architecture and pin map differ, so existing code and carrier assumptions deserve a fresh check. The onboard battery-management circuitry and published battery-sensing pins make it a plausible compact logger, but they do not establish a particular battery life. We would prioritize a working SDK/driver combination before optimizing the physical package.

## Choose it when

You specifically need documented 5 GHz support in a compact programmable board.

## Skip it when

Your existing S3 application depends on its exact peripherals or you need a ready-made camera/display kit.

## Compatibility and limitations

Do not infer firmware compatibility from the shared XIAO outline. The documentation recommends reserving JTAG pads for debugging rather than repurposing them for sleep wakeup. Board-level pin multiplexing, antenna placement and actual radio workload determine the final design.

## Alternatives

XIAO S3/Sense/Plus for their different interfaces; a full-size C5 dev kit for easier bench access.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/esp32-firmware.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Use a board-specific build and a known owned dual-band access point; validate both bands, debugging access and power sensing before packaging.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Xiao C5](https://raw.githubusercontent.com/Seeed-Studio/wiki-documents/HEAD/sites/en/docs/Sensor/SeeedStudio_XIAO/SeeedStudio_XIAO_ESP32C5/XIAO_ESP32C5_Getting_Started.md) — retrieved 2026-11-02; SHA-256 `8b751b96086e5cd8159d32c44770ed98f7ebd77d09478c6166e8b96533e2c55d`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
