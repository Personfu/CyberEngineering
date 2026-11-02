# RFID bench: separate a reader, emulator and evidence trail

**Outcome:** a model/client/firmware matrix and an owned reference fixture. This is an engineering workflow, not a credential-copying procedure.

## 1. Choose the instrument for the question

Use a host-driven Proxmark workflow when the result needs detailed client-side records and analysis. Consider Chameleon for a defined supported emulation task. Ultra and Devkit include the documented MFRC522 HF reader hardware; Lite does not. The Chameleon whitepaper separates hardware capability, firmware support and implemented application behavior—those columns must not be collapsed into one “supported” label.

Proxmark5 is also not an automatic production-ready upgrade. The currently retrieved maintainer README describes its firmware as unstable, warns against its BWM add-on and identifies UHF as not developed. Use the exact present release notes when making a purchase or migration decision.

## 2. Record compatibility before connecting a fixture

Create an inventory containing model/revision, antenna, host OS, client build, bootloader/firmware, documented tag mode and expected observation. Keep the reference tag and reader owned and labeled. A decoded identifier is not an identity or authorization conclusion.

| Check | Expected evidence |
| --- | --- |
| Physical model | Board/label and source manual agree |
| Host/device versions | Matching supported client/firmware record |
| Mode support | Current implemented mode, not only potential silicon support |
| Reference fixture | Known type, ownership, orientation and distance |
| Repeatability | Repeated observations and explicitly failed cases |

## 3. Prepare software using upstream validation

Use the RRG platform-specific compilation and client-validation documentation. Generic PM3 builds and RDV4 are not the same target. Some generic boards have 256 KB flash and require reduced builds; do not project that warning onto every PM3. For Chameleon, choose a currently maintained client and its supported firmware route.

## 4. Make the first experiment modest

Confirm that the client identifies the device and correctly classifies a known owned reference tag. Repeat under fixed conditions and retain negative observations. Change only one thing—client version, antenna position or fixture—before repeating. If investigating emulation, use an owned development reader and a fictional fixture dataset rather than a live access credential.

## 5. Preserve provenance

Hash the exported non-sensitive logs and keep a fixture description, device versions and conditions with them. Do not treat an emulated response as proof of general reader compatibility or a vulnerability. Define what would falsify the interpretation before expanding the test.

**Sources:** [RRG Proxmark](https://github.com/RfidResearchGroup/proxmark3), [Chameleon hardware](https://github.com/RfidResearchGroup/ChameleonUltra/wiki/hardware), [Chameleon technical whitepaper](https://github.com/RfidResearchGroup/ChameleonUltra/wiki/technical_whitepaper), and [individual reviews](../../site/reviews.html).
