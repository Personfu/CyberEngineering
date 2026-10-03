# MERCURY · Read RF and map projects without confusing their evidence

The [ORION source directory](../community/README.md) connects the beginner track to RocketGod's public project links and ProtoPirate's public credits. Start with vocabulary and provenance before interpreting a device tool or a map.

## RF vocabulary

| Term | Meaning | Interpretation boundary |
|---|---|---|
| RF signal | Electromagnetic activity measured through a receiver and observation chain | A measurement depends on receiver settings, environment and coverage |
| Sample | A discrete measurement used to represent a varying signal | Sampling is a representation with finite resolution |
| Modulation | A way information influences a carrier signal | Recognizing modulation is different from identifying a sender |
| Encoding | A representation of information using defined symbols or timing | Encoding does not imply secrecy |
| Decoder | Logic that interprets a representation under assumptions | A plausible decoded field can still have an uncertain interpretation |
| Checksum/CRC | A consistency check intended to detect certain data changes | It is different from cryptographic authentication |
| Encryption | A key-dependent transformation protecting information under a scheme | Recognizing an encrypted format does not reveal its key |
| Protocol | Rules for message structure and interaction | A named protocol is not proof of a device's identity or authorization |

This table is an authored terminology primer, not an evaluation of ProtoPirate or a recipe for interacting with a vehicle, access system or transmitter. The [ProtoPirate review](../community/PROTOPIRATE.md) records the publisher's description and the exact README used.

## Ask the IT and blue-team questions first

- What device and software revision are being discussed?
- Is the evidence a publisher statement, a saved example, a synthetic fixture or an observed measurement?
- Which observation settings and uncertainties are known?
- Which interpretation follows from the bytes, and which needs corroboration?
- What authority and service-owner decision would be required for any device interaction?

For browser-device references such as WebSerial or WebUSB, separate a link label from inspected behavior. The listed applications were not accessible to this retrieval environment; no device access was granted. A future evaluation must define the chosen owned device, permission state and evidence collection before measuring behavior.

## Map vocabulary

| Term | Meaning | Common analytical mistake |
|---|---|---|
| Feature | A source record representing an object or area | Treating a record as proof of current operation |
| Layer | A selected source/category rendered in a view | Treating several layers as independent corroboration automatically |
| Observation time | When the source says the event/state was observed | Replacing it with retrieval time |
| Retrieval time | When the application obtained a record | Calling a freshly downloaded old record a fresh observation |
| Coverage | Where and under what conditions a source can provide records | Inferring absence from an incomplete source |
| Positional uncertainty | Limits on the reported geographic location | Treating the displayed point as an exact surveyed position |

Use the [infrastructure-map source review](../community/MAP-SOURCE-REVIEW.md) for the supplied map. Its publisher describes multiple providers, but their current feeds were not independently observed in this release.

## Beginner handoff exercise

Choose one source from [the directory](../community/README.md). Fill in the [finding template](fixtures/finding-template.md) with its URL, review date, evidence class, stated purpose, actual inspection state and one unsupported inference to avoid. A blocked source can still produce a useful access receipt; it cannot produce a validated functionality claim.

Continue with [manual navigation](MANUALS.md), [local labs](LABS.md) and [versioned input discipline](../assessment/modules/RT016.md).
