# MERCURY · IT before security tools

An IT problem is often a configuration, availability or permission problem. Establish what should work, what changed, and which layer you can actually observe.

## Computer and account vocabulary

| Concept | Plain explanation | Useful distinction |
|---|---|---|
| Operating system | Coordinates hardware, files, processes and access decisions | A distribution is an OS package set; a shell is a command interpreter |
| Process | A running program with an identity and resources | An executable file is not the same as a running instance |
| Service | A program providing a continuing function | It may run without a desktop window |
| User and group | Identities used to make access decisions | Authentication proves identity; authorization decides permission |
| Administrator/root | An identity with broad system authority | Ordinary observation usually does not require elevation |
| Permission | A rule about reading, writing or executing an object | Linux directory execute permission means traversal |
| Patch | A change to software or configuration | Downloaded, installed and effective are different states |
| Backup | A recoverable copy with a stated retention policy | Successful copying does not prove a restore works |
| Virtual machine | A guest OS with virtual hardware | Snapshots are convenient checkpoints, not independent backups |
| Log | A record emitted by a particular component | Missing logging does not establish that nothing happened |

## Follow an ordinary browser request

| Layer | What happens | What can fail |
|---|---|---|
| Name | DNS resolves a hostname to address records | Wrong answer, stale cache, unavailable resolver |
| Route | The OS chooses a destination path | Wrong interface, missing gateway, segmentation |
| Transport | TCP or another transport supports communication | No listener, refused connection, timeout |
| TLS | For HTTPS, peers negotiate protection and validate identities under a trust policy | Name mismatch, trust failure, clock error |
| HTTP | A client sends a method/path and receives status, headers and content | Redirect, unauthorized request, application failure |
| Application | Business logic interprets the request | The HTTP response can succeed while the user's task fails |

An IP address locates an interface in a network context. A port identifies a transport endpoint. A MAC address belongs to the link layer. A hostname is a naming label. None alone identifies a person. `127.0.0.1` is IPv4 loopback: traffic stays on the same machine. Binding to `0.0.0.0` has a much broader meaning and is unnecessary for these labs.

## Read local state

These examples observe your own learning machine. Some commands or fields depend on the OS and installed packages. Their output is not included here as a claimed result.

```bash
pwd
id
ls -l foundations/fixtures
ip address show
ip route show
ss -ltn
```

`pwd` reports the working directory; `id` reports your current identity; `ls -l` describes files and mode bits. `ip` asks the local kernel about interfaces and routing. `ss -ltn` requests listening TCP sockets with numeric addresses. A listener is evidence of a local socket, not proof that an external client can reach it. Sources: [GNU Coreutils](https://www.gnu.org/software/coreutils/manual/coreutils.html), [ip manual](https://man7.org/linux/man-pages/man8/ip.8.html), [ss manual](https://man7.org/linux/man-pages/man8/ss.8.html).

On your own Windows learning machine, use PowerShell for comparable questions:

```powershell
Get-Process | Select-Object -First 5 Name, Id
Get-Service | Select-Object -First 5 Name, Status
Get-WinEvent -LogName Application -MaxEvents 5 |
    Select-Object TimeCreated, Id, LevelDisplayName, ProviderName
```

The last command reads up to five Application events; it does not diagnose them. Fields and access vary by host. See Microsoft's [Get-WinEvent reference](https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.diagnostics/get-winevent).

## A useful help-desk triage sequence

1. Write the symptom in user terms: “The training page will not load.”
2. Record the expected behavior, start time, affected scope and last relevant change.
3. Separate name resolution, transport, TLS and application observations.
4. Compare against a known working local baseline.
5. Change one thing only after identifying its owner, rollback and verification.
6. Document the result and the remaining uncertainty.

For a security handoff, keep an observed fact separate from your hypothesis. “Three denied sign-ins appear in this fixture” is an observation. “An attacker did this” requires additional evidence.

[Try the labs](LABS.md) · [Team roles](TEAMS.md)
