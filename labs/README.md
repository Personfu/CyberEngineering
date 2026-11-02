# NIGHTSHIFT practical workbench

Use the tools to answer a concrete engineering question. Each walkthrough names the required inputs, commands, expected result, failure cases and evidence to retain. Offline fixtures are deliberately synthetic; hardware steps are marked as requiring a device.

## Start with runnable local examples

From the repository root with Python 3.12:

```bash
python -m labtools.benchkit inventory
python -m labtools.benchkit telemetry labs/fixtures/messages.csv
python -m labtools.benchkit ble-decode 02010605094c414231
python -m labtools.benchkit pincheck labs/fixtures/pins-good.json
python -m labtools.benchkit power --capacity-mah 1200 --active-ma 80 --idle-ma 5 --duty 0.1
python -m unittest discover -s tests -v
```

Expected highlights: eight of ten synthetic messages were observed; median latency is 60 ms. The advertisement decodes a flags structure and the fictional local name `LAB1`. The pin fixture has three unique pins and one explicitly shared signal. The power calculation gives 12.5 mA average and a 76.8-hour planning estimate under its stated assumptions—not a device battery-life result.

## Walkthroughs

| Track | Full walkthrough | Outcome |
| --- | --- | --- |
| Embedded software | [ESP32 firmware](guides/esp32-firmware.md) | Identify target, artifact type, installer and recovery route |
| Mesh communication | [LoRa node](guides/mesh-node.md) | Separate hardware role, region, firmware target, delivery and power |
| Portable applications | [Flipper development](guides/flipper-development.md) | Build an application and understand API/RAM constraints |
| RFID | [RFID bench](guides/rfid-bench.md) | Choose reader/emulator and a versioned reference fixture |
| Linux devices | [Cyberdeck setup](guides/linux-cyberdeck.md) | Preserve an image, validate the complete host and keep a recovery path |
| RF signals | [SDR bench](guides/sdr-bench.md) | Set an input budget and inspect a controlled receive path |
| Network/application evidence | [Local network lab](guides/local-network.md) | Distinguish HTTP response, transport error and passive observation |
| Detection and forensics | [Evidence lab](guides/evidence-analysis.md) | Write a harmless detection rule, inspect a toy binary and preserve evidence |
| Engineering assurance | [Assurance and recovery](guides/assurance.md) | Model states, validate configuration and test restoration |

See [firmware routes and recovery](FLASHING.md), [helper script reference](SCRIPTS.md), and [the lab index](CATALOG.md) for the individual exercises. Use [the product documentation](../site/reviews.html) to choose equipment; a method that works on one model is not automatically valid on another.

## What has actually been tested

The Python helper tests exercise hashes, manifest/board mismatch, example-only artifact refusal, pin collisions, malformed BLE structures, UF2 structure, timing errors, loopback-only requests and power assumptions. The browser suite tests site interactions. These are software tests of this repository. Physical flashes, RF trials, instrument calibration and device-specific endurance remain hardware exercises and are not reported as passed.
