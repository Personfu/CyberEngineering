# Local network lab: response, transport and interpretation

**Outcome:** a repeatable HTTP observation and a clear distinction between server behavior and connection failure.

## 1. Start your own harmless fixture

From the repository root:

```bash
python -m http.server 8765 --bind 127.0.0.1 --directory labs/fixtures
```

Use a second terminal for requests. Keep the first terminal visible so the request can be paired with its server log.

## 2. Compare success and a real HTTP error

```bash
python -m labtools.benchkit http http://127.0.0.1:8765/health.json
python -m labtools.benchkit http http://127.0.0.1:8765/not-present.txt
curl --noproxy '*' --include http://127.0.0.1:8765/health.json
curl --noproxy '*' --fail http://127.0.0.1:8765/not-present.txt
```

The helper records status, content type, byte count and body digest without dumping arbitrary headers. Expect HTTP 200 for the fixture and HTTP 404 for the missing file. The latter still proves that an HTTP server answered; curl’s `--fail` makes it return exit 22. The helper reports `http_success: false` for 404 while successfully recording the observation.

## 3. Compare a transport failure

Stop only the server you started, then repeat the first request. A connection error is different from a 404 response. Record the underlying exit status rather than hiding it behind a successful pipe or a shell message.

## 4. Add browser/proxy observation

Use browser developer tools or configure Burp/ZAP for a disposable browser profile and this local fixture. Observe one request and response with active scanning/interception disabled. Explain method, path, status and content type. A passive scan alert is a rule finding, not proof of exploitation. Do not mix unrelated browsing or personal session data into the record.

## 5. Packet evidence is a separate layer

If Wireshark/TShark is installed, use a harmless saved capture from a classroom fixture. A display filter changes the view of existing packets; it does not recover absent traffic. Identify packet bytes that support a decoded field and distinguish them from capture metadata. Do not make collecting live third-party traffic a prerequisite for this lab.

The custom helper is deliberately loopback-only and also rejects redirects to external destinations. Tests exercise that boundary as well as HTTP 200/404 behavior.

**References:** [curl manual](https://curl.se/docs/manpage.html), [TShark manual](https://www.wireshark.org/docs/man-pages/tshark.html), [ZAP passive scanning](https://www.zaproxy.org/docs/desktop/start/features/pscan/), and [the core tool guide](../../foundations/TOOLS.md).
