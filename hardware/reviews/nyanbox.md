# nyanBOX

**Independent documentation review · 2026-11-02**

A packaged ESP32/nRF24 wireless toolkit whose device-detection claims need their own validation.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Maker | README identifies Nyan Devices and maintainers jbohack/zr_crackiin | [nyanbox](https://raw.githubusercontent.com/jbohack/nyanBOX/HEAD/README.md) |
| Hardware | ESP32 WROOM-32U, triple nRF24 modules and OLED are documented | [nyanbox](https://raw.githubusercontent.com/jbohack/nyanBOX/HEAD/README.md) |
| Power | 2500 mAh rechargeable battery is listed | [nyanbox](https://raw.githubusercontent.com/jbohack/nyanBOX/HEAD/README.md) |
| Observations | BLE advertising inspection and passive Wi-Fi packet monitoring with serial CSV export are described | [nyanbox](https://raw.githubusercontent.com/jbohack/nyanBOX/HEAD/README.md) |

## Our review

nyanBOX may be useful when a packaged small display and several radio interfaces reduce assembly work for a wireless-learning task. Our strongest reason to consider it is an inspectable raw observation/export workflow, not an unqualified claim to find a particular camera or tracker. A device label generated from OUI, names or heuristics is an inference and should be tested against known positive and negative fixtures before it drives a decision.

## Choose it when

You want a packaged wireless-learning interface and will validate the particular observation workflow.

## Skip it when

Your purchase depends on guaranteed surveillance-device identification or unverified vulnerability claims.

## Compatibility and limitations

The maker lists many identification and vulnerability-related features; this review does not confirm their accuracy, coverage or exploitability. Battery capacity is documented, while “all day” runtime is not independently established. Do not treat a confidence label as calibrated evidence or a signal-strength display as a precise location instrument.

## Alternatives

A documented BLE development kit or raw packet-analysis workflow for narrower evidence questions.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/esp32-firmware.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Use owned labeled devices, inspect exported/raw fields and report false positives, missed detections and the effect of changing identifiers.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Nyanbox](https://raw.githubusercontent.com/jbohack/nyanBOX/HEAD/README.md) — retrieved 2026-11-02; SHA-256 `1c85a033c2c65dbcc1de819fcf54a00bc48b0a210eb319fd5263b5e703e0dc5d`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
