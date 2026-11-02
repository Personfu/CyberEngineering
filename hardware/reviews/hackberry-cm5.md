# HackberryPi CM5

**Independent documentation review · 2026-11-02**

A genuine Linux handheld built around CM5, with a useful keyboard and real expansion tradeoffs.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Compute module | Raspberry Pi CM5 only; the maintainer says the module is not included | [hackberry](https://raw.githubusercontent.com/ZitaoTech/HackberryPiCM5/HEAD/README.md) |
| Display | 4-inch 720×720 multitouch TFT | [hackberry](https://raw.githubusercontent.com/ZitaoTech/HackberryPiCM5/HEAD/README.md) |
| Expansion | 2242 NVMe slot, two USB 3.0 ports and full-size HDMI | [hackberry](https://raw.githubusercontent.com/ZitaoTech/HackberryPiCM5/HEAD/README.md) |
| Input | Repurposed BlackBerry Q10/Q20/9900 keyboard options with VIAL key mapping | [hackberry](https://raw.githubusercontent.com/ZitaoTech/HackberryPiCM5/HEAD/README.md) |
| Power | Documented 5000 mAh LiPo; runtime claims have not been independently tested | [hackberry](https://raw.githubusercontent.com/ZitaoTech/HackberryPiCM5/HEAD/README.md) |

## Our review

Hackberry is a better fit than an ESP32 multitool when the actual requirement is Linux packages, local compilation or a real terminal session. The square screen and thumb keyboard favor focused tasks over long-form desktop work. Its combination of NVMe, USB and HDMI makes it more versatile than its size suggests, but the complete purchase must include a compatible CM5 and cooling. The designer also documents repairable mechanical parts and keyboard configuration, which improves its value as an engineering platform.

## Choose it when

You want a pocket Linux workspace with a physical keyboard and inspectable construction.

## Skip it when

You need comfortable extended typing, guaranteed radio performance through the enclosure or a ready-to-run price that ignores the compute module.

## Compatibility and limitations

The maintainer explicitly notes antenna limitations associated with the metal enclosure/heatsink and documents an external-antenna option. The NVMe slot can also host an accelerator, so those uses compete for that expansion resource. Battery-life figures in the README are maker claims, not our measured results.

## Alternatives

uConsole for a different modular handheld workflow; Raspberry Pi 500+ for a fixed keyboard workstation.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/linux-cyberdeck.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Use the same local edit/build/logging task on battery and external power, recording temperatures, storage configuration and keyboard usability.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Hackberry](https://raw.githubusercontent.com/ZitaoTech/HackberryPiCM5/HEAD/README.md) — retrieved 2026-11-02; SHA-256 `2cd0b60e1a60c2c34fec1c760d10442a0a83e510ce1921dedc5ba3cebf47e647`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
