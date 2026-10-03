# MERCURY · What Kali Linux actually gives you

Kali is a Debian-based Linux distribution assembled for penetration testing, auditing and related security work. It supplies packaged tools and a specialized environment; it does not automatically choose the right question or interpret an output. The Kali project's own introduction assumes familiarity with Linux. Start with [IT fundamentals](IT.md) if the shell is new. Source: [What is Kali Linux?](https://www.kali.org/docs/introduction/what-is-kali-linux/).

## A practical learning setup

1. Follow the project's [official image and verification guide](https://www.kali.org/docs/introduction/download-official-kali-linux-images/). Verify the image and signed checksum process against the current official instructions.
2. Import an appropriate official VM or use the [official VirtualBox guest guide](https://www.kali.org/docs/virtualization/install-virtualbox-guest-vm/). Choose resources your host can support; this repository sets no universal RAM or disk requirement.
3. For these tutorials, keep the work inside the guest and use loopback or offline fixtures. Disable shared folders, clipboard and drag-and-drop while learning boundaries. This is this guide's isolation choice, not a claim about upstream defaults.
4. Understand the VM network setting: NAT provides outbound connectivity, bridged networking joins a physical network, and host-only networking connects the host and guest. None is a complete security boundary by itself.
5. Record a clean checkpoint and a tool inventory before a lab. Restore only your dedicated learning VM when needed.

No Kali VM was installed or booted for this documentation release. The executable lab checks use the development environment's available Python and curl; the GUI screenshots come from official publishers.

## Find out what is installed

```bash
cat /etc/os-release
command -v nmap
nmap --version
curl --version
python3 --version
```

`command -v` asks your shell which executable it would invoke. A missing tool is an installation-state observation, not a reason to run unrelated commands as root. Compare a package with [Kali's tool directory](https://www.kali.org/tools/) and its upstream manual. Do not assume every Kali image contains every tool.

## Know the kind of tool

| Kind | Examples | Measurement |
|---|---|---|
| Local state | `ip`, `ss`, `journalctl` | What the OS reports at the observation time |
| Protocol inspection | Wireshark, TShark, tcpdump | Captured packets and decoded fields |
| HTTP observation | curl, Burp Proxy, ZAP passive analysis | Requests, responses and their properties |
| Content and evidence | YARA, Autopsy, Ghidra | File patterns, artifacts or reconstructed program structure |
| Defensive monitoring | Sysmon, Zeek, Suricata, Sigma | Events, network evidence, alerts or detection definitions |
| Advanced assessment | Metasploit, sqlmap, password-auditing tools | Specialized security testing with additional prerequisites |

Names in the last row are explained in the [recognition section](TOOLS.md#advanced-kali-tools-recognition-guide). Beginner exercises use ordinary service requests and harmless fixtures.

## Learn one command carefully

Read its purpose, input, privileges, options, output format and exit status. Predict the outcome before running a local example. Save the version and the command with your note. Consult [manual-page navigation](MANUALS.md), then complete [Lab 1](LABS.md#lab-1--read-a-command-before-running-it).
