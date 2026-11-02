# M5Stack StickS3

**Independent documentation review · 2026-11-02**

A compact S3 controller with an audio/IR feature set whose power and interface constraints matter.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Processor / memory | ESP32-S3-PICO-1-N8R8, 8 MB flash and 8 MB PSRAM | [official-sticks3](https://docs.m5stack.com/en/core/StickS3) |
| Display | 1.14-inch 135×240 ST7789P3 LCD | [official-sticks3](https://docs.m5stack.com/en/core/StickS3) |
| Audio | ES8311 codec, MEMS microphone and amplified speaker | [official-sticks3](https://docs.m5stack.com/en/core/StickS3) |
| Sensing / IR | BMI270 IMU; infrared transmitter and receiver | [official-sticks3](https://docs.m5stack.com/en/core/StickS3) |
| Power / expansion | 250 mAh battery, Grove-style port and Hat2 bus | [official-sticks3](https://docs.m5stack.com/en/core/StickS3) |

## Our review

StickS3 is a useful choice for a small audio, motion or remote-control prototype when the integrated peripherals eliminate several separate boards. Its constraints make it a more interesting engineering product than a simple “new Stick” label. The manufacturer specifies that IR reception uses RMT and requires the speaker amplifier off; it also documents external-power direction and IR power-enable behavior. Those are concrete reasons an application can fail even after a successful firmware flash.

## Choose it when

You need compact integrated audio/IR/motion features and can follow the exact power/input rules.

## Skip it when

You need extensive text entry, arbitrary old Stick Hat compatibility or a large battery.

## Compatibility and limitations

The maker recommends reducing speaker volume on battery to avoid power-related reboot, and names Hat products that do not mechanically fit. Treat those as current manufacturer guidance, not an independently reproduced fault. Do not transfer Plus/Plus2 images, accessories or power assumptions to StickS3.

## Alternatives

Cardputer for keyboard input; Tab5 for a richer display; a bare S3 board for a custom interface.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/esp32-firmware.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Verify board target, input power direction, audio level, IR receiver mode and amplifier state with a known owned remote fixture.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Manufacturer: Sticks3](https://docs.m5stack.com/en/core/StickS3) — retrieved 2026-11-02; SHA-256 `66220a8a39de679f9f9d4c84fe132a495242d479812b8e91f10921b26ba2ef39`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
