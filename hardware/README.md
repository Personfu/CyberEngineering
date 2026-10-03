# VOYAGER · Hardware learning bench

Treat a device as a measurement system: **input → front end → firmware → host interpretation → evidence**. Record the exact model, firmware revision, client version, units, acquisition conditions and uncertainty. The diagrams in the site are conceptual illustrations, not manufacturer engineering drawings or measurements of owned equipment.

## Choose by the question

| Device | What it does | How it does it | What an observation cannot prove | Primary resource |
|---|---|---|---|---|
| Flipper Zero | Portable interface for supported radio, RFID/NFC, infrared and hardware functions | Dedicated front ends and firmware applications expose different physical interfaces | A decoded value does not establish identity, authority or protocol security | [Flipper documentation](https://docs.flipper.net/) |
| Proxmark3 | RFID research and signal/protocol analysis platform | Antennas, configurable signal processing, device firmware and a host client cooperate | Decoding success does not establish reliable operation across tag populations | [Maintainer wiki](https://github.com/RfidResearchGroup/proxmark3/wiki) |
| Chameleon Ultra | Configurable RFID emulation/research platform | Device firmware and a compatible host interface configure supported modes | An emulated object is not equivalent to an authorized credential | [Maintainer repository and documentation](https://github.com/RfidResearchGroup/ChameleonUltra) |
| WiFi Pineapple Pager | Portable Wi-Fi administration and assessment device | Radios, firmware, local controls and a management interface provide observations and configured behavior | A visible network name does not identify its operator; radio observation does not measure every client | [Pager documentation](https://documentation.hak5.org/wifi-pineapple-pager) |
| WiFi Pineapple Mark VII | Wi-Fi assessment appliance with a browser management interface | Hardware radios and software services support network observation and management | A router-like enclosure does not make this equivalent to an ordinary home router | [Mark VII documentation](https://documentation.hak5.org/wifi-pineapple) |
| WiFi Pineapple Enterprise | Separate Pineapple hardware/product family | Model-specific firmware and management services expose its supported features | Instructions and specifications for Pager or Mark VII cannot be assumed compatible | [Enterprise documentation](https://documentation.hak5.org/wifi-pineapple-enterprise) |
| Ordinary Wi-Fi router | Provides routing and, commonly, local wireless access | IP forwarding, radio access, addressing and firewall functions connect networks | Association is not proof of end-to-end service availability | Use the manual for the exact vendor, model and firmware; no model was supplied |

Resources reviewed on **2026-10-03**. Capabilities and availability depend on model and installed firmware. No equipment inventory, performance measurement or purchase recommendation is implied.

## First bench session

1. Write an inventory row: model, asset label, firmware, host/client version, documentation URL, review date and intended measurement. Leave unknown fields unknown.
2. Read the manufacturer's power, connection and recovery documentation. Compare the hardware revision with the page you are reading.
3. Draw the data path. Distinguish antenna, analog front end, decoder, storage and host display. Mark where a timestamp or identifier is created.
4. Use the synthetic timing dataset below to learn evidence analysis before hardware acquisition. Verify that every row remains labeled synthetic.
5. Write a result with a scope sentence, a comparison, uncertainty and a counterexample. Keep personal identifiers out of bench records.

## Six graduate challenges

**V01 · Timing uncertainty.** Given synthetic repeated timestamps, estimate mean and standard deviation with `s² = Σ(xᵢ − x̄)²/(n − 1)`. Compare two firmware groups with a bootstrap interval. State whether independence is plausible; repeated samples from one fixture are not independent devices. Report a small-sample t interval or bootstrap interval with the assumptions that justify it.

**V02 · Decoder quality.** Create a confusion matrix from fictional class labels. Estimate precision and recall; explicitly handle a zero denominator. Vary the prevalence of the positive class while keeping conditional error rates fixed. Explain why precision changes. A classifier's confidence score needs separate calibration.

**V03 · Field variability.** Model `y = β₀ + β₁ distance + β₂ orientation + u_device + ε`. Specify units and a held-out-device split. Describe a calibration reference and the measurement floor. The model is a proposal; no range, sensitivity or antenna result has been measured here.

**V04 · Version compatibility.** Build a matrix of device firmware, client version and document revision using supplied fictional records. Distinguish “tested,” “documented,” “unsupported” and “unknown.” An installation that succeeds is not sufficient evidence of measurement correctness.

**V05 · Protocol integrity.** Analyze a supplied, harmless toy record with length and checksum fields. Measure malformed-record rejection without reproducing a credential, access-control protocol or radio transmission. Separate accidental-error detection from cryptographic authentication.

**V06 · Privacy budget.** Compare aggregate counts with record-level identifiers. Formulate a retention policy and a minimization experiment using fictional rows. Evaluate utility loss and identification risk separately. Do not turn a source-map review into tracking people, cameras or aircraft.

## Reproducible data

[`data/hardware/timing.csv`](../data/hardware/timing.csv) contains **60 synthetic timing rows**: two fictional firmware groups, three fixtures and ten repeated observations per fixture. `latency_ms` is generated arithmetic, not hardware performance. [`scripts/build_site.py`](../scripts/build_site.py) produces this fixture deterministically and draws the associated conceptual visuals. It does not connect to radios or hardware.

Connect this bench to [RF vocabulary](../foundations/RF-AND-MAPS.md), [manual-reading](../foundations/MANUALS.md), [source hygiene](../community/SOURCES.md), and [graduate experiment contracts](../research/EXPERIMENTS.md).
