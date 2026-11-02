# Flipper: write a small application and understand its limits

**Outcome:** a buildable application structure, a pinned SDK/API record and a documented recovery path. The example logs a message; it does not use radios or credentials.

## 1. Establish the official development checkout

Follow the [official firmware requirements](https://github.com/flipperdevices/flipperzero-firmware). Clone with submodules and pin the release/commit used for your device. Use the repository’s build tool rather than assembling an unrelated compiler environment.

```bash
git clone --recursive https://github.com/flipperdevices/flipperzero-firmware.git
cd flipperzero-firmware
./fbt
```

## 2. Add an application you own

Copy this repository’s [example](../../examples/flipper_hello/nightshift_hello.c) and [manifest](../../examples/flipper_hello/application.fam) into `applications_user/nightshift_hello` in that official checkout. The manifest identifies the external application and entry point; the C file logs a harmless startup line and returns.

```bash
./fbt build APPSRC=applications_user/nightshift_hello
```

Expected: the pinned SDK produces a FAP application artifact or reports a specific manifest/API/build error. This repository has not compiled that example against every firmware SDK; build/launch on a physical Flipper is a hardware-track check, not a claimed local test pass.

## 3. Know what a FAP is

The [upstream application documentation](https://github.com/flipperdevices/flipperzero-firmware/blob/dev/documentation/AppsOnSDCard.md) describes FAPs as ELF-based executables with metadata/resources. The loader checks compatibility, copies code/data into RAM and relocates imported symbols. Consequently:

- SD capacity is not application runtime memory.
- External code/data consumes heap that a built-in application would use differently.
- Compatibility follows exported API metadata, including a major-version check; a filename alone does not prove compatibility.
- Debug/release firmware and application builds need to match the debugging setup.

## 4. Run only after the build is understood

Use the official tool’s documented deployment/launch route and your owned device. Retain the firmware revision, API version and application artifact digest. Verify the logged message through the documented debug/serial path. Do not describe a successful compile as proof of physical peripheral behavior.

## 5. Extend one feature at a time

Add a display view, then button handling, then a local data file before considering an external interface. Name the input and expected output for each step. Keep the original example as a recovery/build reference and follow the official firmware recovery instructions if an update fails.

**Continue:** [Flipper review](../../hardware/reviews/flipper-zero.md), [flashing routes](../FLASHING.md), and [benchkit verification](../SCRIPTS.md).
