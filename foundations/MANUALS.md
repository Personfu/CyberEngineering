# MERCURY · Read the manual before the command

The installed manual is usually the closest description of the version on your machine. Online documentation adds context, but may describe a different release. Record both the local version and the date of the online reference.

## Navigate man

```bash
man man
man 1 curl
man 8 ip
man 8 ss
man -k checksum
```

The number selects a manual section. Common sections include **1** for user commands, **5** for file formats and **8** for administration commands. `man -k` searches short descriptions; its database may be missing or stale. In the usual `less` pager, `/word` searches forward, `n` repeats the search, `N` reverses it and `q` exits. Pager behavior can differ. [man manual](https://man7.org/linux/man-pages/man1/man.1.html).

Read **NAME** for purpose, **SYNOPSIS** for syntax, **DESCRIPTION** for behavior, **OPTIONS** for switches, **EXIT STATUS** for machine-readable outcomes and **SEE ALSO** for related references. Brackets usually denote optional elements in a synopsis; do not type the brackets. Uppercase names such as FILE denote values you supply. Follow the page's own notation.

## Help is tool-specific

| Tool | First documentation step | What to look for next |
|---|---|---|
| Nmap | `nmap --help`, `man nmap` | Version, scope, state definitions and output formats |
| curl | `curl --help all`, `man curl` | URL handling, headers, errors and exit codes |
| Wireshark/TShark | GUI Help; `tshark --help`, `man tshark` | Capture versus display filters |
| tcpdump | `tcpdump -h`, `man tcpdump` | Reading files, capture filters and name resolution |
| ip / ss | `ip help`, `ss --help` | Objects, state selections and local observation |
| OpenSSL | `openssl help`, `man openssl` | The separate manual for the selected subcommand |
| journalctl | `journalctl --help`, `man journalctl` | Time, unit, boot and retention semantics |
| PowerShell | `Get-Help Get-WinEvent -Full` | Parameters, examples and returned object fields |
| Sysmon | Microsoft's Sysinternals documentation | Configuration and event meanings |
| YARA | `yara --help` and project rule docs | Inputs, strings, conditions and match meaning |
| Sigma | Official rule specification | Log-source mapping and backend translation |
| Burp / ZAP | Their official desktop documentation | Proxy state, passive analysis and history |
| Zeek / Suricata | Their official documentation | Observation source, output schema and deployment mode |
| Lynis / Autopsy / Ghidra | Publisher documentation and application Help | Applicable checks or evidence-analysis workflow |

These help commands do not install the tools. A missing manual can mean the documentation package is absent. A missing executable can mean a different image or package set. Do not assume a universal `--help` flag or use an undocumented flag just because another program supports it.

## Explain a command out loud

For `curl --noproxy '*' --include http://127.0.0.1:8765/health.json`:

- `curl` is the client program.
- `--noproxy '*'` makes this request avoid configured proxy settings; the quotes prevent shell wildcard expansion.
- `--include` prints response headers with the body.
- The URL identifies the loopback training service, path and port.

The shell passes arguments; curl interprets its own options. A pipe passes stdout to another program. `>` redirects stdout and can replace a destination file; `>>` appends. Stderr is a separate stream. Check what will be written before using redirection. [Bash pipelines](https://www.gnu.org/software/bash/manual/html_node/Pipelines.html) · [curl manual](https://curl.se/docs/manpage.html).

After a Bash command, `echo $?` reads that command's exit status only if no intervening command changed it. Zero usually means command success, not that your security hypothesis is true. A curl transfer can succeed while receiving HTTP 404 unless options change its treatment of HTTP errors.

[Practice with localhost](LABS.md) · [Tool explanations](TOOLS.md)
