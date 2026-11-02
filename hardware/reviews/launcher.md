# Launcher (M5Stick-Launcher lineage)

**Independent documentation review · 2026-11-02**

A firmware/partition manager that changes the ownership workflow rather than adding a new radio.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Inputs | Install binaries through documented OTA, web UI and SD-card paths | [m5launcher](https://raw.githubusercontent.com/bmorcelli/M5Stick-Launcher/HEAD/README.md) |
| Partition management | Inspect, back up, restore and resize supported partitions | [m5launcher](https://raw.githubusercontent.com/bmorcelli/M5Stick-Launcher/HEAD/README.md) |
| Storage guidance | FAT32/MBR and smaller SDHC cards are recommended; newer versions also support larger/exFAT media | [m5launcher](https://raw.githubusercontent.com/bmorcelli/M5Stick-Launcher/HEAD/README.md) |
| Boot behavior | The installed application starts normally unless Launcher is invoked | [m5launcher](https://raw.githubusercontent.com/bmorcelli/M5Stick-Launcher/HEAD/README.md) |
| Targeting | Project spans M5Stack, LILYGO, CYD and other explicit targets | [m5launcher](https://raw.githubusercontent.com/bmorcelli/M5Stick-Launcher/HEAD/README.md) |

## Our review

Launcher can be the most useful software purchase decision even though it is not an extra device: it makes switching and managing firmware less cumbersome. Choose it when experimentation between known applications is the actual workflow. Its partition and backup tools deserve more attention than the convenience of one-click flashing, because installing an application and preserving its data are different operations.

## Choose it when

You regularly switch supported firmware and want an inspectable management layer.

## Skip it when

You need one fixed-purpose device and have no reason to add a partition-management layer.

## Compatibility and limitations

Partition changes can invalidate a previous application’s storage assumptions. A binary appearing in an online catalog does not establish its compatibility or authenticity. Follow the exact device target and retain recovery artifacts; no installation was executed on real hardware here.

## Alternatives

Compare the individually reviewed Bruce, Marauder, GhostESP, HaleHound, Porkchop or Meshtastic workflows against the actual task.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/esp32-firmware.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Pin source/release and board target, preserve a recovery image, and verify one benign owned-fixture task with an inspectable output before extending the system.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [M5Launcher](https://raw.githubusercontent.com/bmorcelli/M5Stick-Launcher/HEAD/README.md) — retrieved 2026-11-02; SHA-256 `7cc30b064056c34f1e19557767affab15d76c9eb196d3daba91b780b14dbb3e8`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
