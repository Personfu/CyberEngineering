# GhostESP Revival

**Independent documentation review · 2026-11-02**

An ESP-IDF-native platform with capture export, multiple front ends and an application ecosystem.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Retrieved release description | README identifies v2.2 and ESP-IDF v6.1 | [ghostesp](https://raw.githubusercontent.com/GhostESP-Revival/GhostESP/HEAD/README.md) |
| Capture | Maintainer documents Wireshark streaming and on-device capture/export formats | [ghostesp](https://raw.githubusercontent.com/GhostESP-Revival/GhostESP/HEAD/README.md) |
| Control paths | On-device UI, serial CLI, web UI, Android and GhostLink are described | [ghostesp](https://raw.githubusercontent.com/GhostESP-Revival/GhostESP/HEAD/README.md) |
| Apps | Native SD applications and a sandboxed Lua scripting layer are documented | [ghostesp](https://raw.githubusercontent.com/GhostESP-Revival/GhostESP/HEAD/README.md) |
| Radio dependency | 802.15.4 and dual-band functions are tied to suitable chip targets | [ghostesp](https://raw.githubusercontent.com/GhostESP-Revival/GhostESP/HEAD/README.md) |

## Our review

GhostESP is worth considering when inspectable capture/export and a programmable app platform are more important than a simple appliance menu. Its IDF-native design and shared command paths give an engineer a coherent way to connect a display action with a host-side record. We would shortlist it for an exact supported board and an explicit export workflow rather than choosing it solely on its number of targets or advertised features.

## Choose it when

You want documented export and app interfaces on a supported ESP32 target.

## Skip it when

You need a turnkey validated instrument or assume every supported board has every radio.

## Compatibility and limitations

The README is a maintainer description, not independent proof that every capture/detection claim works. Features vary with chip, PSRAM and peripheral configuration. Its own documentation asks users to use official artifacts, so provenance and target selection belong in the setup record.

## Alternatives

Compare the individually reviewed Bruce, Marauder, GhostESP, HaleHound, Porkchop or Meshtastic workflows against the actual task.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/esp32-firmware.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Pin source/release and board target, preserve a recovery image, and verify one benign owned-fixture task with an inspectable output before extending the system.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Ghostesp](https://raw.githubusercontent.com/GhostESP-Revival/GhostESP/HEAD/README.md) — retrieved 2026-11-02; SHA-256 `52bfb09c46c3431b9f70716aa0c2d02c85b5412888373756aa4c3a153ca3be59`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
