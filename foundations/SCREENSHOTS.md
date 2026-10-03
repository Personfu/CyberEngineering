# MERCURY · Actual tool screenshots

These are three **actual upstream interface screenshots**, inspected visually on 2026-10-03. They are referenced from publisher-hosted image URLs with credits; they are not generated illustrations or screenshots of tools run in this release. Historical sample values belong to the upstream examples. The UI version is not independently established, and the publisher may change an image at the same URL.

## Wireshark · Read the three panes

![Actual Wireshark screenshot from its official user guide: packet list, protocol details and byte view](https://www.wireshark.org/docs/wsug_html_chunked/images/ws-main.png)

**Credit:** Wireshark Foundation, [Main Window documentation](https://www.wireshark.org/docs/wsug_html_chunked/ChUseMainWindowSection.html). [Direct image](https://www.wireshark.org/docs/wsug_html_chunked/images/ws-main.png).

Look at the selected DNS response. The packet list summarizes it; the middle pane explains decoded fields; the bottom pane shows bytes. The selection binds all three views to the same packet. Read the filter bar and status bar before interpreting which packets are visible. A displayed packet is evidence of this example capture, not evidence about your network.

**Exercise:** locate the protocol label, the selected DNS transaction field and its bytes. Write which fact comes from the packet and which context comes from the capture.

## Burp Suite · Read HTTP history

![Actual Burp Suite Proxy HTTP history screenshot from PortSwigger documentation, showing request rows and paired request/response panes](https://portswigger.net/burp/documentation/desktop/images/getting-started/quick-start-pro-proxy-history.png)

**Credit:** PortSwigger Ltd., [Intercepting HTTP traffic, HTTP history section](https://portswigger.net/burp/documentation/desktop/getting-started/intercepting-http-traffic). [Direct image](https://portswigger.net/burp/documentation/desktop/images/getting-started/quick-start-pro-proxy-history.png). The example response displays a historical July 2024 date; the documentation was inspected in October 2026.

The selected row binds the request on the left to the response on the right. Find method, path and response status. A browser visit can make several requests, so one page view does not imply one row. When preparing your own evidence exports, remove session identifiers and unnecessary personal fields.

**Exercise:** distinguish the request's protocol line from the response's status line. Explain why an ordinary resource request can return 200 without saying anything about application authorization.

## Burp Suite · Recognize a paused request

![Actual Burp Proxy Intercept screenshot from PortSwigger showing a request held for review and the Forward and Drop controls](https://portswigger.net/burp/documentation/desktop/images/getting-started/quick-start-pro-intercepted-request.png)

**Credit:** PortSwigger Ltd., [same getting-started documentation](https://portswigger.net/burp/documentation/desktop/getting-started/intercepting-http-traffic). [Direct image](https://portswigger.net/burp/documentation/desktop/images/getting-started/quick-start-pro-intercepted-request.png).

This screenshot shows interception enabled and a held request. It explains why a browser can appear to wait when the proxy has intentionally paused traffic. In the localhost observation lab, use interception off so ordinary browsing can proceed while history remains available.

**Exercise:** name the UI control state responsible for the pause. Explain why waiting at this point is not, by itself, evidence that the server failed.

## Image provenance

| Image | Retrieved bytes | SHA-256 of inspected bytes |
|---|---:|---|
| Wireshark main window | 54,925 | `250e5a220b8ff2b0c01d4cd61d7bd8f1db9e924aa54697cce21e6d7ea9a88f99` |
| Burp HTTP history | 170,409 | `9c7a0c588b36ef43a88e38eeb7aead0e6e5e284b66fe63013890f962c278b08e` |
| Burp intercepted request | 51,485 | `5f00351131827b6e2d543375037692ef190a0ca8fb400a0be5e9aac653dd5b63` |

The hashes identify the bytes inspected locally, not a guarantee of future remote rendering. Images remain externally hosted; this repository does not relicense them. The [source ledger](SOURCES.md) supplies the documentation context. The flow diagrams in [the introduction](README.md) and [team guide](TEAMS.md) are authored conceptual visuals, not tool screenshots.
