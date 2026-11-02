# RaspyJack

**Independent documentation review · 2026-11-02**

A Raspberry Pi/Linux toolkit with local controls and web interfaces, not an ESP32 firmware image.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Host | Raspberry Pi OS Lite workflow; Zero 2 WH is a documented compact option | [raspyjack](https://raw.githubusercontent.com/7h30th3r0n3/Raspyjack/main/README.md) |
| Displays | Waveshare 1.44-inch ST7735 and 1.3-inch ST7789 HATs have distinct configurations | [raspyjack](https://raw.githubusercontent.com/7h30th3r0n3/Raspyjack/main/README.md) |
| Interfaces | Local LCD controls, web UI and browser-based application editor | [raspyjack](https://raw.githubusercontent.com/7h30th3r0n3/Raspyjack/main/README.md) |
| Wireless dependency | Maintainer calls for a compatible external USB adapter for monitor/injection workflows | [raspyjack](https://raw.githubusercontent.com/7h30th3r0n3/Raspyjack/main/README.md) |
| Headless mode | README documents an Ethernet-equipped path | [raspyjack](https://raw.githubusercontent.com/7h30th3r0n3/Raspyjack/main/README.md) |

## Our review

RaspyJack is a stronger fit than an ESP32 firmware when Linux packages and a web-oriented development workflow are the actual requirement. The small display is a control surface over a larger software stack, not the whole product. We would use it as an inspectable lab host only after reviewing its installer, services and required peripherals; the breadth of its included applications increases maintenance and review work rather than automatically increasing value.

## Choose it when

You need a small Linux host and can maintain the stack and peripherals.

## Skip it when

You want a narrow fixed-purpose instrument with minimal services or assume an ESP32 board can run this image.

## Compatibility and limitations

The README makes broad security-tool claims that were not reproduced here. Its adapter table includes a chipset labeling inconsistency, so confirm the physical adapter chipset against its own vendor documentation. Do not assume the built-in Pi radio substitutes for every external-adapter workflow. No toolkit was installed or operated against third-party systems.

## Alternatives

A conventional Raspberry Pi terminal for a smaller custom stack; Cardputer firmware for an embedded-only interface.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/linux-cyberdeck.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Audit a pinned image/installer and use a local benign application first; inventory every enabled service and required adapter.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Raspyjack](https://raw.githubusercontent.com/7h30th3r0n3/Raspyjack/main/README.md) — retrieved 2026-11-02; SHA-256 `31b379934966ccbf3977240956dbf5761b6405d9c341c5ec6b02255f32bc2ef3`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
