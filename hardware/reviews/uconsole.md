# ClockworkPi uConsole

**Independent documentation review · 2026-11-02**

A modular handheld whose exact core and operating-system image matter more than the shared enclosure name.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Documented core variants | CM4, A06 and R01 have separate images | [clockwork](https://raw.githubusercontent.com/clockworkpi/uConsole/master/README.md) |
| Current CM4 image | The retrieved table lists a 64-bit v3.1 image with Linux 6.12.62, dated April 2026 | [clockwork](https://raw.githubusercontent.com/clockworkpi/uConsole/master/README.md) |
| Hardware documentation | Mainboard, core adapters and optional 4G extension schematics are linked | [clockwork](https://raw.githubusercontent.com/clockworkpi/uConsole/master/README.md) |
| Keyboard | Firmware update tooling is documented separately | [clockwork](https://raw.githubusercontent.com/clockworkpi/uConsole/master/README.md) |
| A06 | Gearbox controls big.LITTLE CPU/GPU operating profiles | [clockwork](https://raw.githubusercontent.com/clockworkpi/uConsole/master/README.md) |

## Our review

uConsole is a sensible research platform if you want a modular handheld and are willing to treat the operating-system image as part of the product. Its public schematics and core-specific image table make it more inspectable than an unspecified assembled cyberdeck. We would choose a clearly documented core/image combination and resist applying upgrade instructions from another variant. The A06 power-profile tooling is an example of why ownership experience differs between cores even when the enclosure looks the same.

## Choose it when

You want a documented modular Linux handheld and can maintain its image and peripherals.

## Skip it when

You need a universal plug-and-play image across all uConsole cores or prefer conventional laptop ergonomics.

## Compatibility and limitations

The official image links include historical releases; newest is not synonymous with verified for your attached hardware. A 4G board, storage upgrade or alternative compute module has its own compatibility requirements. We did not reproduce keyboard flashing or verify a battery-runtime claim.

## Alternatives

HackberryPi CM5 for its CM5-only design; Raspberry Pi 500+ for fixed use.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/linux-cyberdeck.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Record core, mainboard and image revisions; verify keyboard, storage recovery and one representative local workload before adding an expansion board.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Clockwork](https://raw.githubusercontent.com/clockworkpi/uConsole/master/README.md) — retrieved 2026-11-02; SHA-256 `435e79dcfafbae4d23401bfd6f8cd7a707819e531bd05ce896be6bb4bbe334ad`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
