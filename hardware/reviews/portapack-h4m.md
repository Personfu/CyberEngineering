# PortaPack H4M with Mayhem

**Independent documentation review · 2026-11-02**

An on-device SDR interface whose usefulness depends on exact hardware and upstream firmware compatibility.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Architecture | PortaPack is an add-on for HackRF, with Mayhem derived from the earlier PortaPack/Havoc firmware | [mayhem](https://raw.githubusercontent.com/portapack-mayhem/mayhem-firmware/HEAD/README.md) |
| Maintainer recommendation | Mayhem explicitly recommends H4M packages and upgrade paths | [mayhem](https://raw.githubusercontent.com/portapack-mayhem/mayhem-firmware/HEAD/README.md) |
| Release choices | The project distinguishes stable releases from nightly builds | [mayhem](https://raw.githubusercontent.com/portapack-mayhem/mayhem-firmware/HEAD/README.md) |
| Compatibility | Maintainers caution that visually different seller variants may require their own unsupported firmware | [mayhem](https://raw.githubusercontent.com/portapack-mayhem/mayhem-firmware/HEAD/README.md) |

## Our review

H4M is worth considering when local controls and standalone operation remove a real obstacle in your SDR workflow. Buy into a supported hardware/firmware combination, not just a familiar screen layout. We would favor a bundle explicitly matched to current upstream releases over a cheaper seller-custom variant whose updates depend on one vendor. The add-on changes how you operate the radio; it does not by itself improve the underlying receiver conversion or turn it into a calibrated instrument.

## Choose it when

You need a supported local interface for a documented SDR task.

## Skip it when

Your work is primarily host-based analysis or requires a seller-specific fork with no clear maintenance path.

## Compatibility and limitations

The documentation warns about divergent clones and old/custom firmware instructions. Do not transfer a review of H4M to H4R, H3 or every H2-style enclosure. The HackRF base unit, storage and firmware version remain part of the system being reviewed.

## Alternatives

HackRF One with host software for deeper processing and easier record keeping.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/sdr-bench.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Identify both base-radio and PortaPack revisions, install a known upstream release, and compare a controlled receive task with the host-driven baseline.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Mayhem](https://raw.githubusercontent.com/portapack-mayhem/mayhem-firmware/HEAD/README.md) — retrieved 2026-11-02; SHA-256 `03c44f5dd1e962d75fc5c2641cfaeaf6866d2f9d33d119100f9c3a42ccb8f093`.
- [Portapack Versions](https://github.com/portapack-mayhem/mayhem-firmware/wiki/PortaPack-Versions) — retrieved 2026-11-02; SHA-256 `e09cda426cc5f8aabfc981d98709f46ab9f6d353c460e89f768fb984f6de91e1`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
