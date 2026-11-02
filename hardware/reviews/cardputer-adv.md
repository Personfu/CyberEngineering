# M5Stack Cardputer ADV

**Independent documentation review · 2026-11-02**

A physical-keyboard embedded handheld with a model-specific input implementation.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Processor / flash | ESP32-S3FN8 at 240 MHz; 8 MB flash | [official-cardputer-adv](https://docs.m5stack.com/en/core/Cardputer-Adv) |
| Display / keys | 1.14-inch 240×135 ST7789V2; 56 keys | [official-cardputer-adv](https://docs.m5stack.com/en/core/Cardputer-Adv) |
| Storage / connectivity | microSD and 2.4 GHz Wi-Fi | [official-cardputer-adv](https://docs.m5stack.com/en/core/Cardputer-Adv) |
| Audio / motion | ES8311 codec, speaker, MEMS microphone and BMI270 | [official-cardputer-adv](https://docs.m5stack.com/en/core/Cardputer-Adv) |
| Power | 1500 mAh battery is documented | [official-cardputer-adv](https://docs.m5stack.com/en/core/Cardputer-Adv) |
| Expansion discrepancy | Manufacturer specification lists EXT 2.54-14P plus Grove; Hydra vendor describes an 18-pin interface. Reconcile exact connector/pin map before attaching hardware. | [official-cardputer-adv](https://docs.m5stack.com/en/core/Cardputer-Adv) |

## Our review

ADV earns consideration when the required expansion uses its documented 18-pin header or your firmware explicitly supports its revised keyboard hardware. That is a concrete compatibility benefit over the original, not a universal promise that every old binary will behave correctly. We would choose the supported host/firmware/accessory combination as a system rather than independently buying the newest names. The manufacturer’s library is direct evidence that the original and ADV are different input targets. For custom applications, that separation matters more than a generic feature list.

## Choose it when

You need a programmable pocket keyboard/display and have matched the exact target and accessories.

## Skip it when

You want to run normal Linux packages or assume original and ADV are identical hardware.

## Compatibility and limitations

The current manufacturer manual is now retrieved. Original and ADV still have distinct keyboard drivers and accessory support. On ADV, the manufacturer and Hydra accessory descriptions use inconsistent connector counts; verify the actual pin map/mechanical fit instead of silently assuming agreement. Neither is a Linux computer, and added interfaces require real documented hardware.

## Alternatives

Tab5 for touch-first interaction; Hackberry CM5 for Linux; the other Cardputer revision only when its compatibility advantage is real.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/esp32-firmware.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Use the correct manufacturer library and firmware target; test modifier keys, text input and each attached peripheral before adopting an old binary.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Manufacturer: Cardputer Adv](https://docs.m5stack.com/en/core/Cardputer-Adv) — retrieved 2026-11-02; SHA-256 `079e25371ad55b25fa967dde7efee735674aa464f621439d171767f972296ac1`.
- [M5 Keyboard](https://raw.githubusercontent.com/m5stack/M5Cardputer/HEAD/src/utility/Keyboard/Keyboard.cpp) — retrieved 2026-11-02; SHA-256 `bcdef6ae246d88f0a441d03b21f711f6886f16fce738750298e04edd3fec49de`.
- [M5 Cardputer Header](https://raw.githubusercontent.com/m5stack/M5Cardputer/HEAD/src/M5Cardputer.h) — retrieved 2026-11-02; SHA-256 `e290a5eac38a274977ed63bfb911e149d694b6822e8b4b128d2aa5e3e37d7b91`.
- [Porkchop](https://raw.githubusercontent.com/0ct0sec/M5Porkchop/HEAD/README.md) — retrieved 2026-11-02; SHA-256 `d02f97ed4dcd862444476a55aae7890bdff5fb2cdd55429119e583ac78b8fa08`.
- [Pingequa](https://raw.githubusercontent.com/pingequalab/cardputer-adv-hydra-rf/HEAD/README.md) — retrieved 2026-11-02; SHA-256 `6a2dab07787c6c88e5996d22458efe516bae745ad95b4c478f2ef80065d137b7`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
