# Practical lab index

Each lesson is an original exercise with prerequisites, a procedure, expected output and failure cases. Offline fixtures, optional tools and physical-device work are distinct. A documented hardware step is not reported as an executed hardware test.

| Lab | Mode | Outcome |
| --- | --- | --- |
| [WB01 · Record a bench inventory](lessons/WB01.md) | Offline fixture | Separate host/tool evidence from an assumed board identity. |
| [WB02 · Verify firmware bytes](lessons/WB02.md) | Offline fixture | Match an artifact to a separately recorded expected SHA-256. |
| [WB03 · Refuse an invalid flash plan](lessons/WB03.md) | Offline fixture | Demonstrate that metadata and example-only checks occur before any hardware action. |
| [WB04 · Inspect a UF2 structure](lessons/WB04.md) | Offline fixture | Distinguish a valid block structure from authenticated, board-compatible firmware. |
| [WB05 · Find pin-map conflicts](lessons/WB05.md) | Offline fixture | Separate a legitimate shared signal from conflicting functions assigned to one pin. |
| [WB06 · Read a local HTTP response](lessons/WB06.md) | Offline fixture | Distinguish HTTP 200, HTTP 404 and a transport failure. |
| [WB07 · Decode a fictional BLE advertisement](lessons/WB07.md) | Offline fixture | Inspect length/type/value fields without inferring a device identity. |
| [WB08 · Measure message delivery](lessons/WB08.md) | Offline fixture | Keep missing observations separate from observed latency. |
| [WB09 · Calculate an energy budget](lessons/WB09.md) | Offline fixture | Turn explicit duty/current assumptions into a planning estimate. |
| [WB10 · Build an exact ESP32 target](lessons/WB10.md) | Physical device | Match MCU, display, keyboard, partitions and peripherals to a supported build. |
| [WB11 · Write a Flipper external app](lessons/WB11.md) | Physical device | Build a harmless logging application and understand FAP API/RAM constraints. |
| [WB12 · Set up a role-specific mesh node](lessons/WB12.md) | Physical device | Choose tracker, keyboard node, solar node or PoE gateway by its actual role. |
| [WB13 · Build an owned RFID fixture](lessons/WB13.md) | Physical device | Separate model capability, implemented mode and repeated observation. |
| [WB14 · Budget an SDR receive path](lessons/WB14.md) | Physical device | Record sample/gain settings and a safe input-level budget before interpreting data. |
| [WB15 · Recover a Linux handheld](lessons/WB15.md) | Physical device | Prove a complete carrier/image/peripheral combination and a separate recovery medium. |
| [WB16 · Write a harmless YARA rule](lessons/WB16.md) | Optional tool | Explain a match using authored marker text and a negative fixture. |
| [WB17 · Inspect a binary you wrote](lessons/WB17.md) | Optional tool | Connect source, compiled behavior and decompiler reconstruction. |
| [WB18 · Cross-check a cryptographic digest](lessons/WB18.md) | Optional tool | Compare two implementations on the same harmless bytes. |
| [WB19 · Observe a local web application passively](lessons/WB19.md) | Optional tool | Pair a request/response with a passive finding without generating attack traffic. |
| [WB20 · Read protocol evidence offline](lessons/WB20.md) | Optional tool | Trace a decoded field back to stored bytes and capture context. |
| [WB21 · Model an update state machine](lessons/WB21.md) | Offline fixture | Define transitions that exclude unverified or mismatched artifacts. |
| [WB22 · Review hardware/software provenance](lessons/WB22.md) | Offline fixture | Distinguish physical revision, firmware artifact and source-document identity. |
| [WB23 · Design a detector negative control](lessons/WB23.md) | Physical device | Test whether a detector label follows evidence or a loose identifier heuristic. |
| [WB24 · Test the recovery path](lessons/WB24.md) | Physical device | Demonstrate restoration rather than only normal startup. |
