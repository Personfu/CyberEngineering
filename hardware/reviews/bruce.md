# Bruce

**Independent documentation review · 2026-11-02**

A broad ESP32 firmware ecosystem with an explicit board/peripheral compatibility table.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Platforms | Upstream lists Cardputer/ADV, Stick, Core and multiple LILYGO/other targets | [bruce](https://raw.githubusercontent.com/pr3y/Bruce/main/README.md) |
| Installation | Official web flasher, release binaries and Launcher/M5Burner paths are documented | [bruce](https://raw.githubusercontent.com/pr3y/Bruce/main/README.md) |
| Hardware dependency | The compatibility table separates built-in features and external hardware | [bruce](https://raw.githubusercontent.com/pr3y/Bruce/main/README.md) |
| Custom board | Upstream documents its RF Reaper dev kit separately | [bruce](https://raw.githubusercontent.com/pr3y/Bruce/main/README.md) |

## Our review

Bruce is the stronger choice when a supported handheld and a broad set of integrations reduce the amount of firmware you would otherwise write. The useful starting point is its compatibility table, not its menu. Choose the exact target first and count external modules as real parts of the system. We would prefer one well-supported board configuration over attempting to make every listed feature appear on arbitrary hardware.

## Choose it when

A maintained build explicitly covers your exact board and required peripherals.

## Skip it when

You need deep control over one custom measurement path and cannot tolerate a broad application stack.

## Compatibility and limitations

A firmware entry cannot establish a connected peripheral or verify it works. Supported functionality varies by carrier. A vendor board and an old third-party build are separate support decisions.

## Alternatives

Compare the individually reviewed Bruce, Marauder, GhostESP, HaleHound, Porkchop or Meshtastic workflows against the actual task.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/esp32-firmware.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Pin source/release and board target, preserve a recovery image, and verify one benign owned-fixture task with an inspectable output before extending the system.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Bruce](https://raw.githubusercontent.com/pr3y/Bruce/main/README.md) — retrieved 2026-11-02; SHA-256 `1628dc0783d9b3ab5608bd1de478d5bcd04ff73d70f082ac17282c928d1af7f4`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
