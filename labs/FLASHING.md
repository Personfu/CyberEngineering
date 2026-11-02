# Firmware installation and recovery routes

The first decision is **what artifact you have**, not which flash button to press. A factory/merged ESP image, OTA application image, UF2 file, Linux disk image and a desktop client are different things. Identify the exact board revision, firmware release, artifact kind, publisher digest and recovery route before writing hardware.

## Route index

| Route | Targets | Installation path | Recovery and verification |
| --- | --- | --- | --- |
| FL-01 · ESP factory image | Supported S3/C5/P4 board and exact firmware target | Publisher’s official web flasher, M5Burner or a publisher-documented merged image layout | Model-specific download mode; verify target, boot log and one real function |
| FL-02 · ESP source build | A supported board configuration in the selected project | Pinned ESP-IDF/Arduino/PlatformIO environment; build before using its own flash task | Preserve original config/partition layout; recover using that board’s instructions |
| FL-03 · nRF52 UF2 | Exact Meshtastic nRF52840 target | Enter documented DFU mode and copy the matching UF2 to the bootloader volume | Confirm actual bootloader/family, then application version, region and node operation |
| FL-04 · ESP mesh BIN | ThinkNode ESP32 / correct Heltec variant | Meshtastic flasher with exact board and display selection | V4 and V4-R8 are separate; OLED/TFT images may differ |
| FL-05 · Flipper firmware | Flipper Zero | Official update tools or firmware build tool; application packages use their own API metadata | Use the upstream hardware recovery procedure; external app API major version must match |
| FL-06 · Proxmark | RDV4, PM5 or a supported generic platform | Matching host client, bootloader and firmware built for the exact platform | Run upstream client/device validation; PM5 is currently described as unstable |
| FL-07 · Chameleon | Ultra, Lite or Devkit | Current upstream client/GUI and exact device firmware instructions | Confirm model, firmware/client pair and supported reader/emulation mode |
| FL-08 · Linux disk image | Exact uConsole core, CM5 carrier or Pi computer | Verify the official image; write only to the explicitly identified removable target | Preserve a known-good removable image and configuration; test fresh boot and restoration |
| FL-09 · HackRF / PortaPack | Base SDR plus exact add-on | Matched vendor/upstream host, device and Mayhem release instructions | Identify both boards; do not substitute seller-custom images for another revision |

## Build examples supported by the retrieved sources

These are preparation/build steps, not a claim that hardware was flashed in this environment.

### Flipper application/firmware development

```bash
git clone --recursive https://github.com/flipperdevices/flipperzero-firmware.git
cd flipperzero-firmware
./fbt
```

Pin a release/commit for reproducibility before the build. Use `./fbt build APPSRC=applications_user/your_app` for an application you wrote. FAPs are ELF-based application packages with metadata; they are copied into RAM and checked against the exported API. See [the Flipper walkthrough](guides/flipper-development.md).

### Tab5 official demo

The [official demo](https://github.com/m5stack/M5Tab5-UserDemo) documents dependency retrieval and ESP-IDF v5.4.2:

```bash
python fetch_repos.py
cd platforms/tab5
idf.py build
```

Run inside a pinned checkout with the documented SDK initialized. Its desktop build is a separate SDL/CMake route; a successful desktop UI does not validate the physical display, camera or radio coprocessor.

### Monstatek M1

The [current source](https://github.com/Monstatek/M1) documents `./build.sh --release`, CMake, Ninja, Arm GCC 14.2 and `srec_cat`, with a clean working tree required for release artifacts. Use its hardware-revision documentation. An STM32 artifact is not an ESP32 image and must not be given to an ESP installer.

## Use benchkit before a write

```bash
python -m labtools.benchkit inventory
python -m labtools.benchkit verify path/to/official.bin --sha256 PUBLISHER_SHA256
python -m labtools.benchkit flash-plan path/to/manifest.json --board cardputer-adv --port /dev/ttyACM0
```

Replace `PUBLISHER_SHA256` with the independently obtained publisher digest. A matching digest identifies bytes; it does not authenticate a source by itself. A manifest needs `board`, `chip`, `kind`, `offset`, `file`, `sha256` and `source_url`. The helper only plans an explicitly declared merged factory `.bin` at `0x0` for one of its supported profiles. It **never executes** the generated argument list, erases flash, writes a serial port or chooses a disk. OTA/app-only images must use their own documented route. A declaration in your manifest is not proof that a binary is valid for the board.

The repository’s `example.bin` is synthetic text, not firmware. Its example-only manifest is intentionally rejected by `flash-plan`. This gives a repeatable failure case without writing hardware.

## After installation

1. Read and record the version and board target from a reliable device/client view.
2. Verify display, input and storage before testing attached peripherals.
3. Restore only configuration compatible with the current firmware and partition scheme.
4. Use an owned fixture for one expected function and one negative case.
5. Keep the artifact digest, config backup, output and recovery notes together.

## Primary references

- [Espressif esptool commands](https://docs.espressif.com/projects/esptool/en/latest/esp32s3/esptool/basic-commands.html)
- [UF2 format specification](https://github.com/microsoft/uf2)
- [Flipper build and external applications](https://github.com/flipperdevices/flipperzero-firmware/tree/dev/documentation)
- [Meshtastic model-specific hardware documentation](https://github.com/meshtastic/meshtastic/tree/master/docs/hardware/devices)
- [RRG Proxmark client/platform documentation](https://github.com/RfidResearchGroup/proxmark3)
- [Research source receipts](../hardware/PRIMARY-SOURCES.md)
