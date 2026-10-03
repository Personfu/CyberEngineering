# MERCURY · Official documentation ledger

Reviewed on **2026-10-03**. These references support tool purpose, documented mechanics and manual navigation. They do not prove that a tool was installed or that a screenshot shows the latest release. Local syntax should be checked against the installed version. The practical lab design and team exercises are authored for this repository.

| Reference | Publisher/source | Used for | Inspection |
|---|---|---|---|
| [What is Kali Linux?](https://www.kali.org/docs/introduction/what-is-kali-linux/) | Kali / OffSec | Distribution purpose and Linux prerequisite | Page reviewed |
| [Official Kali images and verification](https://www.kali.org/docs/introduction/download-official-kali-linux-images/) | Kali / OffSec | Image and verification workflow | Page reviewed |
| [Kali VirtualBox guest guide](https://www.kali.org/docs/virtualization/install-virtualbox-guest-vm/) | Kali / OffSec | VM installation reference | Page reviewed; no VM installed |
| [Kali tool directory](https://www.kali.org/tools/) | Kali / OffSec | Package context | Directory reviewed; not a complete installation inventory |
| [ip](https://man7.org/linux/man-pages/man8/ip.8.html), [ss](https://man7.org/linux/man-pages/man8/ss.8.html) | iproute2 manuals rendered by man7 | Local networking state | Pages reviewed |
| [BIND tools](https://www.kali.org/tools/bind9/) | Kali package documentation | dig purpose and documented interface | Page reviewed |
| [curl manual](https://curl.se/docs/manpage.html) | curl project | HTTP command semantics | Page reviewed; local commands smoke-checked |
| [OpenSSL command reference](https://docs.openssl.org/master/man1/openssl/) | OpenSSL project | Subcommands and cryptographic utilities | Page reviewed |
| [Nmap reference](https://nmap.org/book/man.html) | Nmap project | Purpose and manual | Page reviewed; no scan performed |
| [Wireshark main window](https://www.wireshark.org/docs/wsug_html_chunked/ChUseMainWindowSection.html) | Wireshark Foundation | Interface panes and screenshot | Page and image reviewed |
| [TShark manual](https://www.wireshark.org/docs/man-pages/tshark.html) | Wireshark Foundation | CLI analysis and filters | Page reviewed |
| [tcpdump](https://www.kali.org/tools/tcpdump/) | Kali package documentation | Capture/analyzer purpose | Page reviewed |
| [Burp Proxy](https://portswigger.net/burp/documentation/desktop/tools/proxy) | PortSwigger | Proxy purpose | Page reviewed |
| [Burp getting started](https://portswigger.net/burp/documentation/desktop/getting-started/intercepting-http-traffic) | PortSwigger | Intercept/history states and two screenshots | Page and images reviewed; GUI not executed |
| [ZAP passive scan](https://www.zaproxy.org/docs/desktop/start/features/pscan/) | ZAP project | Passive versus active analysis | Page reviewed |
| [journalctl](https://www.man7.org/linux/man-pages/man1/journalctl.1.html) | systemd manual rendered by man7 | Journal querying | Indexed primary manual reviewed; direct systemd site blocked |
| [Get-WinEvent](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent) | Microsoft | Windows event query | Page reviewed; Windows example not executed |
| [Sysmon](https://learn.microsoft.com/en-us/sysinternals/downloads/sysmon) | Microsoft Sysinternals | Endpoint telemetry | Page reviewed |
| [YARA documentation](https://yara.readthedocs.io/en/stable/) | YARA project | Rule matching | Documentation introduction reviewed |
| [Sigma rules](https://sigmahq.io/docs/basics/rules.html) | SigmaHQ | Detection format | Page reviewed |
| [Zeek monitoring](https://docs.zeek.org/en/master/about/monitoring.html) | Zeek project | Structured network evidence | Indexed primary page reviewed; direct retrieval unavailable |
| [Suricata introduction](https://docs.suricata.io/en/latest/what-is-suricata.html) | OISF / Suricata | Monitoring and deployment roles | Page reviewed; latest URL points to development docs |
| [Lynis guide](https://cisofy.com/documentation/lynis/) | CISOfy | Local audit purpose | Page reviewed |
| [Ghidra project](https://github.com/NationalSecurityAgency/ghidra) | NSA | Software-analysis purpose | Project introduction reviewed |
| [Autopsy overview](https://www.autopsy.com/about/) | Autopsy publisher | Forensics purpose | Publisher overview reviewed |
| [Metasploit](https://www.kali.org/tools/metasploit-framework/), [sqlmap](https://www.kali.org/tools/sqlmap/), [Hydra](https://www.kali.org/tools/hydra/), [Hashcat](https://www.kali.org/tools/hashcat/), [John](https://www.kali.org/tools/john/) | Kali package documentation | High-level recognition guide | Purpose descriptions reviewed; no operational examples reproduced |
| [man](https://man7.org/linux/man-pages/man1/man.1.html) | man-db manual rendered by man7 | Sections and synopsis conventions | Page reviewed |
| [Bash pipelines](https://www.gnu.org/software/bash/manual/html_node/Pipelines.html) | GNU Bash | Shell and program distinction | Indexed primary manual reviewed |
| [SHA-2 utilities](https://www.gnu.org/s/coreutils/manual/html_node/sha2-utilities.html) | GNU Coreutils | Digest calculation | Indexed primary manual reviewed |

For image URL, byte count and hash receipts, see [SCREENSHOTS.md](SCREENSHOTS.md). For the separately requested Church of Malware public listing, see [CHURCH-FORGE.md](../intelligence/CHURCH-FORGE.md) and its [catalog source records](../data/intelligence/forge_catalog.json).

An inspection date records the research activity, not the source's original publication date. Linked upstream documents may change. No proprietary manual was copied wholesale and no hosted offensive tool was acquired.
