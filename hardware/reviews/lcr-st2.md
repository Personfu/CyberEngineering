# FNIRSI LCR-ST2

**Independent documentation review · 2026-11-02**

A tweezer/Kelvin-capable component meter with selectable frequency and excitation rather than one universal accuracy figure.

## Documented features

| Feature | Finding | Primary source |
| --- | --- | --- |
| Test frequencies | 100 Hz, 120 Hz, 1 kHz, 10 kHz and 100 kHz | [official-fnirsi](https://www.fnirsi.com/products/lcr-st2) |
| Excitation | 0.1, 0.3, 0.6 and 1.0 V RMS are listed | [official-fnirsi](https://www.fnirsi.com/products/lcr-st2) |
| Models | R/L/C and ESR-related parameters; series/parallel equivalent comparison | [official-fnirsi](https://www.fnirsi.com/products/lcr-st2) |
| Interface | 1.47-inch auto-rotating display and USB-C charging | [official-fnirsi](https://www.fnirsi.com/products/lcr-st2) |
| Package | Kelvin clip is listed in the Plus package, not the standard package | [official-fnirsi](https://www.fnirsi.com/products/lcr-st2) |

## Our review

LCR-ST2 is a sensible bench convenience when small-component handling and repeated sorting are the actual bottleneck. The useful capability is choosing frequency, test level and equivalent model; automatically printing a component value is not enough. We would compare readings on known references at the frequency relevant to the circuit and include contact/fixture repeatability. The Kelvin accessory can be a real reason to choose the Plus package if larger parts are part of the workflow.

## Choose it when

You need compact repeated component checks with explicit frequency/model settings.

## Skip it when

You need a traceably calibrated instrument or assume the standard package contains the Kelvin accessory.

## Compatibility and limitations

The manufacturer publishes different ranges/accuracy conditions rather than a single blanket specification. The page also contains inconsistent operating-environment wording, so consult the supplied current manual before relying on limits. No calibration, electrical protection or runtime result was independently measured.

## Alternatives

A calibrated LCR meter for uncertainty-critical work; a suitable multimeter for simpler measurements.

## Setup and firmware route

Use the [model-appropriate installation and recovery guide](../../labs/guides/esp32-firmware.md) and the [firmware route index](../../labs/FLASHING.md). Record model/revision, current firmware, required peripherals, artifact source and digest before a write. Preserve configuration and establish the vendor recovery route first.

The [benchkit helper](../../labs/SCRIPTS.md) can record inventory, verify artifact bytes and prepare an explicit dry-run flash plan. A successful boot is only a prerequisite: verify the actual function you need.

## First evaluation

Use known passive reference components, record frequency/excitation/model and compare repeated tweezer contacts with the documented Kelvin fixture.

Keep the firmware version, fixture and failed/skipped/unobserved cases with the result. Documented ratings are not measurements performed by this project.

## Sources read

- [Manufacturer: Fnirsi](https://www.fnirsi.com/products/lcr-st2) — retrieved 2026-11-02; SHA-256 `6e221ce2482f0ce45801cc8b9504ca724395c14b8ec9a57c6fdaa8cf85c220b1`.

[Compare products](../../site/reviews.html) · [Practical workbench](../../labs/README.md) · [Primary sources](../PRIMARY-SOURCES.md)
