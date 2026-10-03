# MERCURY · Tool field guide

For each tool, ask: **What input does it use? What transformation or measurement does it perform? What output can it justify?** These twenty core entries cover both everyday IT and security work. Availability and syntax depend on installed versions; the links point to inspected project or publisher documentation. [Source ledger](SOURCES.md).

## Local IT and protocol basics

### 01 · ip

**Does:** reports or changes Linux interfaces, routes and related network state. **How:** communicates with the local kernel's networking interfaces. **Read:** address, interface and route records. For learning, use the read-only examples in [IT.md](IT.md). A configured route does not establish end-to-end delivery. Useful to both IT and assessment teams. [Manual](https://man7.org/linux/man-pages/man8/ip.8.html).

### 02 · ss

**Does:** reports socket state. **How:** asks the kernel about local sockets and applies selection criteria. **Read:** transport, state, local address and peer address. A listening socket and an established session are different observations; an address alone does not identify a user. [Manual](https://man7.org/linux/man-pages/man8/ss.8.html).

### 03 · dig

**Does:** asks a DNS server for records. **How:** constructs a DNS query and decodes the answer and status. **Read:** response code, answer, TTL and resolver. A cached answer can be correct for the cache while differing from current authoritative data. Use it for naming questions, not ownership or personal attribution. [BIND/Kali reference](https://www.kali.org/tools/bind9/).

### 04 · curl

**Does:** transfers data using supported protocols. **How:** implements client-side protocol exchanges with configurable request behavior. **Read:** headers, body, transfer status and exit code. An HTTP error response and a failed transport are different outcomes. [Local HTTP lab](LABS.md#lab-3--observe-your-own-http-service) · [Manual](https://curl.se/docs/manpage.html).

### 05 · OpenSSL

**Does:** provides cryptographic and certificate utilities. **How:** dispatches subcommands to cryptographic implementations and parsers. **Read:** algorithm names, digests or certificate fields, depending on the command. A displayed certificate field does not itself establish a valid trust chain. It can calculate a digest of the harmless fixture in [Lab 5](LABS.md#lab-5--verify-file-integrity). [Manual](https://docs.openssl.org/master/man1/openssl/).

## Network and application observation

### 06 · Nmap

**Does:** discovers network hosts/services and reports observed state. **How:** sends selected probes and interprets responses or their absence; discovery and service classification depend on the technique and vantage point. **Read:** scope, timestamp, port state and evidence for any service label. A service label is not proof of a vulnerability. This guide uses help/version reading rather than a scanning recipe. [Official reference](https://nmap.org/book/man.html).

### 07 · Wireshark and TShark

**Does:** decodes captured network traffic; TShark exposes analysis through a CLI. **How:** dissectors interpret packet bytes and may reconstruct higher-level conversations. **Read:** packet list, decoded fields, raw bytes and capture context. A display filter changes the view of stored packets; it does not recover packets absent from the capture. [GUI screenshot](SCREENSHOTS.md#wireshark--read-the-three-panes) · [TShark manual](https://www.wireshark.org/docs/man-pages/tshark.html).

### 08 · tcpdump

**Does:** captures or reads packets and prints selected information. **How:** uses packet-capture facilities and capture-filter expressions. **Read:** timestamps, endpoints and protocol summaries. Capture filters and Wireshark display filters use different syntax and act at different stages. Reading an existing file is different from collecting live traffic. [Kali package reference](https://www.kali.org/tools/tcpdump/).

### 09 · Burp Suite Proxy

**Does:** makes browser HTTP exchanges inspectable. **How:** a configured browser routes requests through a proxy; interception can pause them, while HTTP history records them. **Read:** method, path, request headers and matching response. “Intercept off” does not mean history is disabled. Start with the normal localhost page in Lab 3; choose observation rather than modifying requests. [Official Proxy docs](https://portswigger.net/burp/documentation/desktop/tools/proxy) · [Actual screenshots](SCREENSHOTS.md#burp-suite--read-http-history).

### 10 · ZAP passive analysis

**Does:** analyzes HTTP messages for configured issues. **How:** passive scan rules inspect traffic already passing through ZAP without generating their own attack requests. **Read:** rule, evidence, confidence and applicability. Passive analysis differs from active scanning; an alert still needs contextual review. [Official passive-scan guide](https://www.zaproxy.org/docs/desktop/start/features/pscan/).

## Host evidence and defensive detection

### 11 · journalctl

**Does:** queries systemd journal records. **How:** selects stored entries by fields, time and other criteria. **Read:** timestamp, unit, priority, message and boot context. Access and retention influence what appears. An empty query may mean missing records or an unsuitable filter. [Upstream manual rendered by man7](https://www.man7.org/linux/man-pages/man1/journalctl.1.html).

### 12 · PowerShell Get-WinEvent

**Does:** reads Windows event-log records. **How:** queries supported event sources and returns objects that can be selected or filtered. **Read:** provider, event ID, time and event-specific fields. Event IDs must be interpreted with their provider; the same number is not a universal diagnosis. [Microsoft reference](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent).

### 13 · Sysmon

**Does:** records configured endpoint activity on Windows. **How:** a service and driver supply events to the Windows event log under a chosen configuration. **Read:** event type, process identifiers, timing and related context. It provides telemetry, not automatic proof of malicious intent; coverage depends on configuration. [Microsoft Sysinternals docs](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon).

### 14 · YARA

**Does:** matches file or memory content against rules. **How:** evaluates declared patterns and Boolean conditions over the input. **Read:** matched rule and the reason its condition was true. A content match can be a useful lead without proving malware identity. A harmless classroom rule can match a marker you put in a text file. [Project documentation](https://yara.readthedocs.io/en/stable/).

### 15 · Sigma

**Does:** expresses detections in a structured, portable rule format. **How:** declares a log source, selections and a condition; supported tooling translates the rule to a backend query. **Read:** required fields, rule condition, status and known false positives. Sigma is a format, not a standalone sensor, and translation does not guarantee equivalent field mappings. [Official rules guide](https://sigmahq.io/docs/basics/rules.html).

### 16 · Zeek

**Does:** turns observed network activity into structured evidence. **How:** protocol analysis and event-driven logic emit connection and application records. **Read:** protocol-specific logs and their shared identifiers. It supports investigation differently from a simple alert list. Its logs reflect the traffic and vantage point supplied to it. [Official monitoring guide](https://docs.zeek.org/en/master/about/monitoring.html).

### 17 · Suricata

**Does:** supports network intrusion detection/prevention and security monitoring. **How:** decodes traffic and applies configured detection logic; deployment mode determines whether it can enforce actions. **Read:** alerts and associated network evidence. An alert is a rule match requiring triage, and an IDS deployment is different from inline prevention. [Official introduction](https://docs.suricata.io/en/latest/what-is-suricata.html).

## Audit and evidence work

### 18 · Lynis

**Does:** audits supported Unix-like hosts for security and configuration concerns. **How:** runs applicable checks against the available local configuration. **Read:** warnings, suggestions and check applicability. Its score is not proof that a host is secure; a suggestion may require the service owner's context. [Publisher documentation](https://cisofy.com/documentation/lynis/).

### 19 · Ghidra

**Does:** helps analyze compiled software. **How:** disassembly, analysis and decompilation reconstruct useful representations from executable bytes. **Read:** functions, references and proposed types. Decompiled output is a reconstruction, not the original source code. Begin with a benign program you wrote; this release does not download or run malware. [NSA project](https://github.com/NationalSecurityAgency/ghidra).

### 20 · Autopsy

**Does:** provides a digital-forensics interface and analysis workflow. **How:** ingest modules examine supplied evidence and expose artifacts for review. **Read:** artifact source, extraction method, timestamps and case context. An artifact requires provenance and interpretation; a GUI label is not an independent conclusion. [Publisher overview](https://www.autopsy.com/about/).

## Advanced Kali tools: recognition guide

These five entries explain vocabulary encountered in reports. Their exercise counterpart is an offline defender question, not an execution tutorial.

| Tool | What it does and how | Beginner defender question | Official package reference |
|---|---|---|---|
| Metasploit Framework | Organizes modular security testing, with modules performing distinct tasks | Which observed behavior supports a report's conclusion? | [Kali](https://www.kali.org/tools/metasploit-framework/) |
| sqlmap | Automates SQL-injection assessment using generated requests and response interpretation | How do developers separate SQL instructions from user-supplied data? | [Kali](https://www.kali.org/tools/sqlmap/) |
| Hydra | Automates authentication attempts through protocol-specific modules | Can the service detect repeated failures without blocking ordinary users? | [Kali](https://www.kali.org/tools/hydra/) |
| Hashcat | Tests candidate passwords against supported password representations using compute backends | What do salts and costly password-hashing functions change? | [Kali](https://www.kali.org/tools/hashcat/) |
| John the Ripper | Tests password candidates against supported stored representations | Why should compromised credentials be revoked even if their plaintext is unknown? | [Kali](https://www.kali.org/tools/john/) |

Tool possession does not establish someone's role in an intrusion. See the [public forge review](../intelligence/CHURCH-FORGE.md) for source attribution and uncertainty.
