# SDR bench: a controlled signal before a sweeping claim

**Outcome:** a documented receive path and an interpretable sample record.

## 1. Define the measurement

Choose one known reference signal, receiver configuration and expected observation. Write down frequency, modulation, sample rate, gain, antenna/cabled path, attenuation and recording duration. For a synthetic or shielded bench exercise, use a known signal source or previously recorded harmless samples rather than unrelated live traffic.

## 2. Respect the actual instrument architecture

HackRF One is documented as a 1 MHz–6 GHz half-duplex SDR with 8-bit conversion and 2–20 Msps quadrature sample rates. It cannot transmit and receive simultaneously as a full-duplex device. PortaPack changes the operating interface; it does not remove the base radio’s conversion limits. Seller-specific SDR/PortaPack bundles need exact compatibility verification.

## 3. Budget the input before connecting

The HackRF One manual specifies a maximum input of −5 dBm. A direct source connection requires a properly calculated attenuation/protection path, not an assumption that low software gain protects the front end. Record source level, attenuation, cable loss and uncertainty. A nearby strong source can also overload the receive path.

## 4. Record a small baseline

Begin receive-only with a known controlled input. Keep the original sample bytes and settings. Check for clipping and expected bandwidth before interpreting a spectrum image. Estimate storage before capture: complex I/Q with signed 8-bit I and Q uses approximately `2 × sample_rate × seconds` bytes, excluding metadata. At 2 Msps for 10 seconds that is about 40 MB.

## 5. Compare one variable

Change sample rate, gain or antenna position one at a time. A wider display is not automatically higher resolution or sensitivity. Keep signal-processing settings and software versions with the recording. Do not turn uncalibrated amplitude into a power measurement or an image peak into a device identity.

## 6. Decide whether this is the right tool

Choose a simpler receive-only SDR for a narrow listening requirement, a higher-resolution/full-duplex instrument if those are hard requirements, or a calibrated analyzer when amplitude accuracy is the task. General coverage is useful, but it is not a substitute for specifying the measurement.

**Sources:** [HackRF One hardware documentation](https://github.com/greatscottgadgets/hackrf/blob/master/docs/source/hackrf_one.rst), [Mayhem compatibility guidance](https://github.com/portapack-mayhem/mayhem-firmware), and [the SDR reviews](../../site/reviews.html).
