# Benchkit: custom engineering helpers

All commands run from the repository root with Python 3.12 and its standard library. Source: [`labtools/benchkit.py`](../labtools/benchkit.py). Outputs are JSON; a detected invalid input returns exit status 1 and an explanation on stderr. Use shell redirection to retain a report, for example `python -m labtools.benchkit telemetry labs/fixtures/messages.csv > /tmp/message-report.json`.

| Command | Input | What it checks / produces | Scope |
| --- | --- | --- | --- |
| `inventory` | None | Python/platform and candidate serial device paths | Opens no device; identifies no board automatically |
| `verify FILE --sha256 HEX` | Artifact and expected digest | Streamed SHA-256 comparison and byte count | Integrity check, not publisher authentication |
| `flash-plan MANIFEST --board PROFILE --port PORT` | Explicit manifest/profile/port | Dry-run esptool argument list after board/chip/type/digest checks | Never executes; only declared merged factory ESP images |
| `uf2-inspect FILE` | UF2 bytes | Block magic, block sequence, family identifiers and address summary | Not a signature, bootability or compatibility verdict |
| `telemetry FILE` | Message CSV | Sent, observed, missing, delivery fraction and observed latency | Assumes synchronized fixture timestamps |
| `ble-decode HEX` | An offline BLE advertisement | Length/type/value structures and local-name text | No radio operations or device identity inference |
| `pincheck FILE` | JSON pin/signal records | Conflicting net assignments and explicitly shared signals | Not an electrical or voltage check |
| `http URL` | Loopback HTTP(S) URL | Status, content type, byte count and body digest | Rejects external targets and redirects to them |
| `power --capacity-mah N --active-ma N --idle-ma N --duty F` | Consistent battery-side current assumptions | Weighted average current and estimated hours | Planning calculation, not a product test |

## Firmware manifest

```json
{
  "board": "cardputer-adv",
  "chip": "esp32s3",
  "kind": "merged-factory",
  "offset": "0x0",
  "file": "official-release.bin",
  "sha256": "REPLACE_WITH_64_HEX_PUBLISHER_DIGEST",
  "source_url": "https://github.com/pr3y/Bruce/releases"
}
```

The artifact path is relative to the manifest. Use the schema only if the publisher actually identifies the artifact and layout this way. Supported profiles are in [board-profiles.json](fixtures/board-profiles.json). The standard Cardputer and ADV are separate profiles even though both use S3. Tab5’s application processor is P4; its radio coprocessor is not the same flash target. This example is a template and is not valid until real metadata is supplied.

## Reproduce successful and failed cases

```bash
python -m labtools.benchkit telemetry labs/fixtures/messages.csv
python -m labtools.benchkit pincheck labs/fixtures/pins-good.json
python -m labtools.benchkit pincheck labs/fixtures/pins-conflict.json
python -m labtools.benchkit ble-decode 02010605094c414231
python -m labtools.benchkit ble-decode 0509ff
```

The third and fifth commands must fail. A test that treats their nonzero exit as success would hide the error being demonstrated. A missing receive time stays missing; it is not silently replaced with zero latency. A pin may be shared only when both records declare the same signal name.

## Scope and extension

The helpers inspect inputs and prepare records; they do not scan public networks, transmit RF, clone credentials, install firmware or launch third-party payloads. Add a new board profile only after checking its chip and publisher installation format. Extend tests alongside any parser or validation change. See [the walkthrough index](README.md) for when to use each helper and [the tests](../tests/test_benchkit.py) for executable edge cases.
