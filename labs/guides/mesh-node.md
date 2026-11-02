# LoRa mesh: choose the role, measure the result

**Outcome:** an exact firmware target, a role-appropriate node and an interpretable delivery/power record. No claimed radio range is inferred from an enclosure or video.

## 1. Pick a deployment role

| Need | Concrete candidates | Why it changes the design |
| --- | --- | --- |
| Carried tracker | ThinkNode M3, Heltec T1 | Size, charging, GNSS and enclosure matter |
| Text entry without a phone | ThinkNode M9 | Keyboard and larger display are real input features |
| Indoor fixed gateway | ThinkNode M7 | Ethernet/PoE, not a handheld battery package |
| Outdoor solar | SenseCAP P1/P1 Pro, ThinkNode M6 | Mounting, energy balance and maintenance dominate |
| Sensor development | Wio L1, Heltec V4 variants | Exposed buses and recovery are useful |

## 2. Bind hardware, region and image

Match the regional RF hardware to the legal configuration for the installation. Confirm the antenna band. Then select the exact firmware target. nRF52840 nodes commonly use UF2; ESP32 nodes use different binary/flasher paths. M1 and M5 are not interchangeable because they have similarly sized e-paper screens. V4-R8 is not original V4; its OLED/TFT targets are separate. Wio L1 e-paper also has its own image.

## 3. Establish a controlled pair

Use two owned nodes, a recorded firmware/configuration pair, a fixed initial placement and a small numbered-message sequence. Record sent time, observed receive time, missing messages, resets, power source and GNSS availability. Do not substitute phone position for a board GNSS observation without labeling it.

```csv
sequence,sent_ms,received_ms
1,0,50
2,100,170
3,200,
```

Use synchronized timestamps if computing one-way latency. Otherwise report round-trip observations or clock uncertainty instead.

## 4. Analyze the provided synthetic example

```bash
python -m labtools.benchkit telemetry labs/fixtures/messages.csv
```

Expected: 10 sent, 8 observed, 2 missing, delivery fraction 0.8 and median observed latency 60 ms. These are arithmetic fixture results, not measured Meshtastic performance. Missing messages have no invented latency.

## 5. Budget energy separately

```bash
python -m labtools.benchkit power --capacity-mah 1200 --active-ma 80 --idle-ma 5 --duty 0.1 --usable 0.8
```

Expected planning estimate: 12.5 mA average and 76.8 hours. Use battery-side currents at a consistent voltage; include conversion loss and actual GNSS/display workload in a real design. A solar panel rating is not daily energy and cell capacity is not measured winter autonomy.

## 6. Repeat and retain failures

Only after the stationary baseline should you change one variable: placement, obstruction, antenna, firmware or workload. Keep the negative cases and topology with the result. Track configuration recovery, not just a successful first message. For outdoor nodes, include maintenance access and charge/brownout logs over representative conditions.

**Sources:** [Meshtastic hardware manuals](https://github.com/meshtastic/meshtastic/tree/master/docs/hardware/devices), the individually reviewed [product library](../../site/reviews.html), and [source receipts](../../hardware/PRIMARY-SOURCES.md).
