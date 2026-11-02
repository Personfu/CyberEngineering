# Assurance and recovery: test the failure path

**Outcome:** a configuration record, a small state model and an executed recovery result.

## 1. State what must remain true

For a firmware-update workflow, define states such as `known_good`, `downloaded`, `verified`, `staged`, `booted` and `recovered`. State invariants before writing code: an unverified artifact cannot be staged; the recovery path must not depend only on the image being replaced; a successful boot must still be followed by a functional check.

Use the [firmware helper](../SCRIPTS.md) as a small example: it rejects a board/chip mismatch, unsupported artifact layout and example-only fixture before producing a dry-run plan. Those checks do not prove every state transition of a physical bootloader.

## 2. Validate the configuration graph

```bash
python -m labtools.benchkit pincheck labs/fixtures/pins-good.json
python -m labtools.benchkit pincheck labs/fixtures/pins-conflict.json
```

The first input deliberately shares one SPI clock net. The second assigns two different chip-select signals to the same pin and must fail. This is a graph/net-name check, not a validation of voltage, current, pull-ups, timing or bus arbitration. Extend the design review with the actual schematic and source manual.

## 3. Separate requirement from observation

Build a compatibility table with explicit statuses: documented, locally software-tested, physically tested, failed and unknown. Include exact versions and conditions. Do not promote “the parser accepts the record” into “the hardware works,” or “the container starts” into “the service is ready.”

## 4. Exercise a reversible restoration

For a local learning service, create a small owned configuration and a known-good copy, change a noncritical setting, restore it and make the same functional request again. Keep the before/after digest and observed response. For a Linux device, boot the recovery medium independently. For a microcontroller, use only its documented download/recovery path and a noncritical fixture.

## 5. Design negative tests

Try a wrong board target, mismatched checksum, truncated UF2, malformed BLE length, duplicate message sequence and receive-before-send timestamp. The expected outcome is a specific refusal or error, with no silent fallback. The [benchkit tests](../../tests/test_benchkit.py) implement these software cases; hardware recovery is separately recorded.

## 6. Connect the result to system engineering

Use the [formal assurance domain](../../atlas/02-formal-software-assurance.md) for invariant thinking, [supply-chain provenance](../../atlas/04-supply-chain-and-provenance.md) for artifact identity, [cloud systems](../../atlas/08-cloud-systems.md) for service readiness and [response/resilience](../../atlas/13-response-resilience.md) for restoration. These share a method: define a falsifier, preserve evidence and test the path that matters when the normal path fails.
