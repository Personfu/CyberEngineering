# Linux cyberdeck: make the image and peripherals reproducible

**Outcome:** a recoverable Linux workspace on an exact compute-module/carrier combination.

## 1. Inventory the complete machine

Write down compute module, RAM, carrier, display, keyboard, storage, power, cooling and optional radios. HackberryPi CM5 is documented as CM5-only and normally excludes the compute module. uConsole publishes separate CM4/A06/R01 images. A shared enclosure name does not imply one OS image fits all cores.

## 2. Verify image provenance and target storage

Use the exact vendor or maintained distribution image and its independent checksum/signature instructions. Keep a second known-good removable image. Identify the intended storage device through the operating system’s disk inventory before using a writer; this guide deliberately supplies no guessed destructive disk command.

Use `benchkit verify` for a publisher-provided SHA-256. An old source offering only MD5 is not equivalent to a modern authenticated release path; consult current distribution guidance rather than treating any matching hash as authenticity.

## 3. Validate before customizing

On first boot, record OS/kernel versions, storage identity and peripheral behavior. Check keyboard/modifiers, display orientation, charging, suspend/resume and storage access. Then run one local task you care about: edit a small file, run a unit suite or serve the local fixture.

```bash
python -m http.server 8765 --bind 127.0.0.1 --directory labs/fixtures
```

In another terminal:

```bash
python -m labtools.benchkit http http://127.0.0.1:8765/health.json
```

Expected: HTTP 200 and a content/body receipt. Stop the server when done.

## 4. Add one integration at a time

Add an SSD, GNSS, SDR, NFC or external Wi-Fi adapter only after the base image is recorded. Check bus/power conflicts and driver support. A port physically accepting an adapter is not evidence of supported functionality. Hackberry’s maker documents metal-case/antenna considerations; uConsole’s image/core differences affect power and kernel support.

## 5. Test recovery and ownership cost

Reboot from the known-good medium and confirm you can restore configuration without relying on the experimental storage. Record dependency versions and the complete bill of materials. For Armbian, inspect the exact board support status: standard, community-maintained, work in progress and end of life are distinct.

**Sources:** [ClockworkPi uConsole](https://github.com/clockworkpi/uConsole), [HackberryPi CM5](https://github.com/ZitaoTech/HackberryPiCM5), [Armbian build framework](https://github.com/armbian/build), and [product reviews](../../site/reviews.html).
