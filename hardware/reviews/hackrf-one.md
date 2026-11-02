# HackRF One

**Independent documentation review · 2026-11-02**

A broad-frequency SDR for experimentation, with explicit conversion and input-power limits.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| RF coverage | 1 MHz–6 GHz | [hackrf-one](https://raw.githubusercontent.com/greatscottgadgets/hackrf/master/docs/source/hackrf_one.rst) |
| Duplex | Half-duplex transmit or receive, not simultaneous full duplex | [hackrf-one](https://raw.githubusercontent.com/greatscottgadgets/hackrf/master/docs/source/hackrf_one.rst) |
| Sampling | 2–20 million quadrature samples per second; 8-bit conversion | [hackrf-one](https://raw.githubusercontent.com/greatscottgadgets/hackrf/master/docs/source/hackrf_one.rst) |
| Host connection | High-Speed USB | [hackrf-one](https://raw.githubusercontent.com/greatscottgadgets/hackrf/master/docs/source/hackrf_one.rst) |
| Input limit | Upstream specifies a maximum input level of −5 dBm | [hackrf-one](https://raw.githubusercontent.com/greatscottgadgets/hackrf/master/docs/source/hackrf_one.rst) |

## Our review

HackRF One is a useful first serious general-purpose SDR when wide tuning coverage, open hardware and host-side signal processing matter. It is a less convincing purchase if the requirement is simply to receive one narrow class of signals: a simpler receiver can reduce cost and complexity. The important trade is broad coverage versus 8-bit dynamic range and half-duplex operation. A higher sample-rate setting is not automatically a better measurement; it changes the bandwidth and host/storage demands.

## Choose it when

You need flexible host-controlled SDR experiments across several bands.

## Skip it when

You require full duplex, calibrated amplitude accuracy or high dynamic range as a primary requirement.

## Compatibility and limitations

Do not treat it as a calibrated spectrum analyzer or a simultaneous transmit/receive instrument. The −5 dBm input limit is a concrete front-end constraint: a nearby strong source or direct connection requires a properly designed attenuation/protection path. Published range and application sensitivity need their own measurements.

## Alternatives

A receive-only SDR for listening; a suitable higher-resolution/full-duplex SDR for those specific requirements; PortaPack for local controls.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/sdr-bench.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Use a controlled reference input with an appropriate level/protection budget, document gains and sample rate, and inspect clipping before interpreting signal amplitude.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Hackrf One](https://raw.githubusercontent.com/greatscottgadgets/hackrf/master/docs/source/hackrf_one.rst) — retrieved 2026-11-02; SHA-256 `c8befe71936c4bef153ba5aff2a976bfd9c45d38cb6ea9094fa9fa49abc4fef5`.
- [Hackrf](https://raw.githubusercontent.com/greatscottgadgets/hackrf/master/Readme.md) — retrieved 2026-11-02; SHA-256 `dd72fde6951b106f4db029707a84bd317e9a417fb8d3ac93738952f8b996558d`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
