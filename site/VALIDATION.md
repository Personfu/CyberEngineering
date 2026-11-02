# NIGHTSHIFT · Executed validation

## Research and workbench expansion · 2026-11-02

Executed in the managed environment using Python 3.12.14, Node 24.19.0, Playwright 1.62.1 and the installed Chromium. The generated site has **11 pages**, **510 reader documents**, **69 individually researched reviews**, **65 retrieved primary references**, **24 exercises** and **nine long-form walkthroughs**. The prior imported video directory has been removed.

- **49 unit tests passed.** New checks cover source/feature binding, model distinctions, HTML escaping, document completeness, artifact changes, board/chip/type mismatch, example-only flash refusal, loopback and redirect boundaries, real local HTTP 200/404, malformed BLE/UF2, pin conflicts, missing timestamps, nonfinite numeric inputs and power assumptions.
- Atlas, research, assessment, deterministic experiments, research visuals, foundations HTTP smoke, community receipts and site integrity checks passed. The build and its consistency check pass with sorted document JSON keys.
- The Playwright suite passed at 1440 × 1080 and 390 × 844 with no page errors. It exercised feature search, combined filters/empty states, sort/shuffle, comparison limits/clearing, cited product manuals, lab search/equipment filters, lesson rendering, ten mobile navigation routes, mobile comparison containment and existing notes/bookmarks/reader/theme behavior.
- The CLI inventory, hash verification, message analysis, BLE decode, pin-map and power examples were run. The authored C example compiled with warnings treated as errors and printed `observed=3`. OpenSSL SHA-256 matched the Python/fixture-manifest digest.
- Local gallery images decoded. External publisher images must either decode or show the existing explicit source-link fallback; their continued remote availability is not claimed.

Physical flashes, RF trials, battery/runtime measurements, instrument calibration and hardware recovery were **not executed**. The Flipper example requires its matching SDK/device workflow. YARA and TShark are optional tools and were not installed or claimed as executed. Documentation/specifications and proposed physical exercises are not represented as measured product results.

Browser screenshots for this run were saved under `/tmp/nightshift-screenshots`; they are local verification artifacts rather than replacements for the historical committed captures below. Website deployment is separate from these local checks.

## Previous validation · 2026-10-03

Reviewed and executed on **2026-10-03**. These are checks of this static learning site and its fixture content, not proof of hardware behavior, vulnerability exploitation or field effectiveness.

## Actual browser checks

The agent-browser CLI could not start its daemon in this execution environment. The browser skill's requested opening was attempted. Verification continued with **Playwright 1.62.1** and **Chrome Headless Shell 154.0.8037.92**, using a temporary HTTP server bound to `127.0.0.1` in the verification process. No approval escalation was used. [`scripts/verify_site.cjs`](../scripts/verify_site.cjs) implements this check and closes both browser and server when finished.

| Check | Executed result |
|---|---|
| Desktop profile, 1440 × 1080 | Correct title, primary content and eight room-navigation links |
| Mission search | All 180 cards loaded; “firmware” returns a subset; nonexistent term gives zero-result message |
| Conference filter and bookmarks | All 32 cards loaded; six workshops; bookmark survives reload; removing bookmark updates the saved-only view |
| Tool search | Twenty entries loaded; “curl” returns one core tool |
| Community credits | Fifteen distinct attribution cards |
| Hardware room | Seven device/model entries |
| Field note | Saved fictional note survives reload, then clears |
| Document reader | Tool guide with twenty headings and mission 001 render; missing document reports a useful message |
| Local figures | All local gallery diagrams/figures loaded with nonzero natural width |
| Mobile, 390 × 844 | Eight navigation routes checked; no document-width overflow |
| Theme | Light mode survives reload |
| JavaScript page errors | None observed in the checked flows |

Three CC BY-SA image files (two hardware photographs and one Proxmark help-screen capture) were inspected and added with creator, license and digest receipts. The Flipper and Proxmark hardware file SHA-1 values matched the publisher file metadata. Independent browser navigation through the public-content proxy returned HTTP 200 and decoded nonzero-size images for Wireshark, Burp history, Chameleon and Pager URLs. Layout captures used recorded, genuine publisher-image bytes through an optional verification-only fixture map, to avoid inconsistent proxy subresource behavior. These bytes were previously downloaded and inspected; no replacement or synthetic images were used. The navigation test accepted the proxy certificate, while the layout run used local image fixtures. Neither setting becomes site configuration. External assets may become unavailable later. The screenshot images belong to their publishers and are referenced with documentation links in the gallery. No accessibility certification, screen-reader audit, cross-browser matrix or hardware trial is claimed.

## Real screenshots of this implementation

- [Desktop profile](screenshots/profile-desktop.png)
- [Mobile profile](screenshots/profile-mobile.png)
- [Hardware bench](screenshots/hardware-desktop.png)
- [Rendered tool guide](screenshots/tool-guide.png)

These are browser captures of the implemented pages, not generated interface mockups. The desktop/profile and document images capture a viewport; hardware and mobile images capture the full page.

## Reproducible content checks

`python scripts/build_site.py --check` verifies the committed pages, diagram bytes, catalogs and synthetic hardware fixture match the builder. `python scripts/check_site.py` verifies nine HTML pages, 401 repository-document copies, all 180 mission links, all 150 assessment module documents, conference-source binding and absent media receipts, sixty labeled synthetic rows, relative HTML references and local visual assets. The existing atlas, research, assessment, fixture and source checks also passed; all **26 unit tests** passed.

To rerun browser verification with Playwright installed:

```bash
node scripts/verify_site.cjs
```

Optional environment variables: `CYBER_BROWSER_PATH` selects an installed Chromium-compatible executable; `CYBER_SCREENSHOT_DIR` selects where captures are saved. Without a custom executable, Playwright uses its installed Chromium. `CYBER_IMAGE_FIXTURES` optionally points to a JSON object mapping publisher image URLs to downloaded original files for layout verification. `CYBER_VERIFY_PROXY` optionally selects a verification-only public-content proxy; it never becomes site configuration. There is no fixed public port or persistent server.
