# ESP32 firmware: identify, build, recover

**Outcome:** a repeatable installation record for an exact board and firmware release. Hardware writing is a device exercise; the local preparation checks can run without a board.

## 1. Define the whole target

Write down the board/model/revision, MCU, display controller, keyboard/input hardware, flash/PSRAM, peripherals, power arrangement and desired firmware release. A Cardputer and Cardputer ADV both use ESP32-S3, but the manufacturer library selects different keyboard readers. Heltec V4 and V4-R8 have distinct images and pinouts. Tab5 splits application processing on P4 from wireless on C6. A chip-family match alone is insufficient.

## 2. Identify the artifact

Use the publisher release or official flasher. Record whether it is a merged factory image, app-only/OTA binary, filesystem image or source build. Record the independent digest and install layout. Do not guess flash offsets from a filename. The [route index](../FLASHING.md) explains the distinctions.

```bash
python -m labtools.benchkit inventory
python -m labtools.benchkit verify path/to/download.bin --sha256 PUBLISHER_SHA256
```

A mismatch is a stopping result for that artifact, not an invitation to replace the expected digest with the observed one. A candidate `/dev/ttyACM0` path does not prove the board model.

## 3. Choose a supported development route

- Arduino/PlatformIO: use the project’s board environment and pinned library versions, not a generic target selected by appearance.
- ESP-IDF: initialize the documented SDK version and build the checked-out project in its documented directory.
- Official web flasher/M5Burner: choose the exact target and read the artifact/release notes.

For a simple application you own, begin with serial output, one button and a static display. Add storage, radio and external modules separately. Keep each known-good stage recoverable.

## 4. Plan before writing

The [benchkit manifest](../SCRIPTS.md) can bind an artifact to an explicit board/chip and produce a dry-run argument list. It does not discover or authenticate hardware and never executes writes. The example-only fixture deliberately refuses to create a hardware-write plan:

```bash
python -m labtools.benchkit flash-plan labs/fixtures/example-manifest.json --board cardputer --port /dev/ttyACM0
```

Expected: exit 1, explaining that example fixtures cannot produce a board-write plan.

## 5. Recovery is model-specific

Use the vendor’s download-mode sequence and recovery artifact. StickS3’s current manual describes holding its side reset button until the internal green LED flashes. PaperS3 describes its own power-button/red-light sequence. Those instructions must not be generalized to every ESP32 enclosure. Preserve configuration and the previous partition layout before changing firmware managers.

## 6. Demonstrate readiness

Record boot/version output, correct display and key operation, storage access and one desired peripheral function. For an attached radio/NFC module, record the actual component and configured pins. A menu entry is not a detected peripheral. Compare an expected result with a negative fixture case, then test the documented recovery route.

**Sources:** [Espressif esptool](https://docs.espressif.com/projects/esptool/en/latest/esp32s3/esptool/basic-commands.html), [M5Stack manuals](https://docs.m5stack.com/), [manufacturer Cardputer keyboard implementation](https://github.com/m5stack/M5Cardputer/blob/master/src/utility/Keyboard/Keyboard.cpp), and [the primary-source ledger](../../hardware/PRIMARY-SOURCES.md).
