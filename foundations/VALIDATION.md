# MERCURY · Validation scope

The beginner track adds documentation, three upstream screenshot references, two conceptual diagrams, harmless fixtures and a bounded loopback HTTP/curl smoke. It does not add an offensive runtime or a deployed application.

Run from the repository root:

```bash
python3 scripts/check_foundations.py --smoke
```

The validator checks twenty ordered core tool entries, the eight-event synthetic fixture and its declared counts, the file-integrity reference, the 50-record public metadata catalog, source/coverage reconciliation and local Markdown links/heading anchors. The smoke starts a temporary server bound to `127.0.0.1` on an ephemeral port, verifies ordinary 200/404 responses, verifies curl's successful transfer and `--fail` exit code 22, and closes the server.

The existing atlas, research, assessment, experiment, figure and unit checks remain separate requirements in [the CI workflow](../.github/workflows/atlas.yml). Workflow results are recorded in [GitHub Actions](https://github.com/Personfu/CyberEngineering/actions/workflows/atlas.yml).

No Kali VM, Burp GUI, Wireshark GUI, packet capture, Windows host command or advanced assessment tool was executed for this release. Screenshots were downloaded from official publishers for visual inspection; the pages reference the original remote URLs. Image hashes identify the inspected bytes, while external availability and future changes remain outside the local integrity check.

Public forge metadata was read through publicly accessible listing pages, not a signed-in account or code checkout. The catalog's categories remain publisher-description summaries. License state, exploit validity, current patch status, actual identities and complete repository histories are not established by that review.
