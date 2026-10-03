# MERCURY · Six beginner labs

Run commands from the repository root on your own learning machine. Python 3 is needed for the web lab and fixture reading; curl is needed for the HTTP commands. The fixtures are authored classroom data. No external service, live account or malware sample is needed.

## Lab 1 · Read a command before running it

**Goal:** explain options rather than memorize a command.

```bash
curl --version
curl --help all
man 1 curl
```

Find the manual entries for `--include`, `--noproxy` and `--fail`. Write what each changes and which output would distinguish a transport failure from an HTTP error. Record your installed version. If the manual is absent, use the [official curl reference](https://curl.se/docs/manpage.html).

**Deliver:** a five-line command explanation with an input, output and limitation. **Red question:** does the predicted result match the actual result? **Blue question:** what evidence would a help-desk ticket need?

## Lab 2 · Map your local configuration

**Goal:** distinguish identity, address, route and socket state.

Use the read-only Linux or Windows examples in [IT.md](IT.md). Draw a four-column table: command, observation time, relevant field, interpretation. Choose one local listener if one exists; if there is none, record that result rather than inventing it.

**Deliver:** a local configuration note with private values omitted from a public export. **Red question:** which assumption about reachability is unsupported? **Blue question:** which normal service owner can explain a listener? **Expected learning:** a local socket alone cannot prove external reachability.

## Lab 3 · Observe your own HTTP service

**Goal:** see a normal request, a normal response and an ordinary error.

In terminal A, start the training server with its document root limited to the three small classroom web files:

```bash
python3 -m http.server 8765 --bind 127.0.0.1 --directory foundations/fixtures/web
```

In terminal B on the **same machine**, request the health document:

```bash
curl --noproxy '*' --include http://127.0.0.1:8765/health.json
```

Read the status, content type and body separately. The fixture body contains `"status": "ok"`; it is a static teaching value, not a measurement of a real service's health.

Request a nonexistent classroom path and observe curl's exit status immediately:

```bash
curl --noproxy '*' --fail http://127.0.0.1:8765/not-present.txt
echo $?
```

For this server, expect HTTP 404 and curl exit code 22 with `--fail`. Without that option, successful receipt of a 404 response can still be a successful transfer. Stop terminal A with Ctrl+C when finished. If port 8765 is already occupied, stop this lab and choose a free local port consistently in both terminals.

**Optional GUI observation:** on the same learning machine, use Burp's configured browser with interception off to visit this localhost page and inspect Proxy → HTTP history. Request paths and status codes should match your browser actions; actual counts may include extra browser requests. Do not run a scan. A proxy can observe HTTPS content only when its TLS mediation is configured and trusted; this exercise deliberately uses plain local HTTP.

**Deliver:** one request/response note, with tool/version and the server's matching log entry. **Red question:** which expected property did you challenge? **Blue question:** can you explain an ordinary 404 without declaring an intrusion? [curl manual](https://curl.se/docs/manpage.html) · [Burp Proxy](https://portswigger.net/burp/documentation/desktop/tools/proxy).

## Lab 4 · Triage synthetic sign-in evidence

**Goal:** separate a repeated denial pattern from a conclusion about intent.

```bash
python3 -m json.tool foundations/fixtures/events.json
```

The file contains eight fictional records, including three denied sign-ins, one allowed sign-in and one explicit sensor-gap record. Count events by event type and result. Keep `unknown` separate from a successful or unsuccessful event. Write two competing explanations for the denied sign-ins and one additional observation that would distinguish them.

**Deliver:** a short evidence timeline. **Red question:** can an ordinary mistake resemble the pattern being studied? **Blue question:** what corroboration would justify escalation? **Expected learning:** a pattern is observable while its cause can remain unknown. This is not a dataset for estimating a real incident rate.

## Lab 5 · Verify file integrity

**Goal:** understand a fingerprint without confusing it with trusted authorship.

```bash
sha256sum foundations/fixtures/note.txt
python3 -m json.tool foundations/fixtures/integrity.json
```

Compare the digest with the fixture manifest. A matching digest establishes agreement with this reference, subject to trust in the reference itself. It does not establish that a file is benign or who created it. Optionally compare `openssl dgst -sha256 foundations/fixtures/note.txt` against the same value. [GNU SHA-2 utilities](https://www.gnu.org/s/coreutils/manual/html_node/sha2-utilities.html) · [OpenSSL](https://docs.openssl.org/master/man1/openssl/).

**Deliver:** file path, byte count, digest, reference and conclusion. **Red question:** could an untrusted reference validate an untrusted file? **Blue question:** how would signed provenance improve the decision?

## Lab 6 · Write a red-blue handoff

**Goal:** make the result useful to a teammate.

Fill in [finding-template.md](fixtures/finding-template.md) using one of the previous labs. The red cell writes the question and expected evidence. The blue cell records observations and alternative explanations. The white cell checks that the conclusion follows from the fixture. The service owner defines the retest.

**Deliver:** a completed note with an owner and an achievable next observation. **Expected learning:** “unknown; collect the missing context” can be a better result than an unsupported incident claim. Continue with [RT024](../assessment/modules/RT024.md) and [RT036](../assessment/modules/RT036.md).

## What was verified for this release

See [local validation](VALIDATION.md) for the checks actually executed. The automated HTTP smoke uses an ephemeral loopback port, avoiding fixed-port conflicts. GUI installation, live packet capture and Windows commands were not executed as part of those checks.
