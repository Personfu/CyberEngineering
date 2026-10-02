# Contributing to Project HELIOS

The first edition deliberately contains **exactly 150 missions in 15 ordered chapters**. Improve an existing mission when possible. For a new proposal, open a discussion or pull request that explains where it fits and whether it replaces or extends an existing mission; do not silently renumber the atlas.

A useful contribution gives the mission outcome, proposed mechanism, testable hypothesis, authorized data source, baseline, measurable endpoint, adverse case, safety/privacy limit, and primary-source citations. Distinguish an engineering idea from an implemented prototype and a measured result. If you report measurements, add the test protocol, dataset provenance, sample size, uncertainty, and known exclusions.

Please do not commit credentials, live targets, sensitive logs, captures, memory images, exploit payloads, personal records, or material copied from a private source packet. The [research method](editorial/RESEARCH_METHOD.md) and [input boundary](editorial/INPUT_BOUNDARY.md) explain the evidence and safety standards. Run `python scripts/build_atlas.py` after editing atlas chapters, then `python scripts/build_atlas.py --check` before proposing a change.
