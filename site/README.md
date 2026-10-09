# NIGHTSHIFT · Cyberengineering profile

A static, responsive cyberpunk learning site with a MySpace-inspired profile rail, credit wall, field notebook and nine connected page types. All 180 research dossiers and 150 assessment modules remain available through the document reader.

From the repository root:

```bash
python scripts/build_site.py
python -m http.server 3000 --bind 127.0.0.1 --directory site
```

Open `http://127.0.0.1:3000/`. Stop with Ctrl+C. Use HTTP rather than opening HTML with `file://`, because the document reader and catalogs load local JSON files.

## Pages and behavior

| Page | Function |
|---|---|
| `index.html` | Profile, preserved-project counts, linked rooms, browser-local notebook |
| `learn.html` | IT basics, red/blue/purple concepts, local HTTP tutorial, manual map |
| `tools.html` | Searchable twenty-tool field guide with purpose and mechanism |
| `hardware.html` | Seven device/model entries with official resources and conceptual architecture |
| `missions.html` | Search and domain filters over all 180 research dossiers |
| `talks.html` | Search/type/bookmark filters over retrieved DEF CON metadata; explicit gaps |
| `community.html` | All fifteen unique ProtoPirate README credit labels and source reviews |
| `gallery.html` | Credited hardware photographs, four sourced tool screenshots, seven data figures and eleven conceptual diagrams |
| `reader.html?doc=foundations/README.md` | Local repository-document renderer with rewritten document links |

No analytics, geolocation, public comments, remote tool execution or live hardware connection. Notes, theme preference and bookmarks use `localStorage` on the current browser; they do not synchronize between devices. Browser storage can be disabled. The UI reports storage failures.

The build uses Python's standard library. Generated JSON, pages and figures are committed. The document reader uses the vendored **Marked 17.0.5** browser distribution under its MIT license; see `vendor/LICENSE.marked`. The reader permits a restricted set of document markup and removes executable schemes and event attributes. Markdown Mermaid/math source remains readable source text; the gallery provides rendered original diagrams and data figures. Publisher screenshots remain externally hosted and may disappear or change.

## Hosting and verification

The site is published automatically to [Personfu/CyberEngineering GitHub Pages](https://personfu.github.io/CyberEngineering/) after a successful push to `main`. The workflow validates the atlas, research extension, foundations, community receipts, and static site before deploying `site/` as the Pages artifact. Pull requests run the same validation but do not deploy.

The site can also be hosted manually as static files, including under a repository subpath. All internal navigation and data requests use relative URLs.

Run `python scripts/build_site.py --check` and `python scripts/check_site.py` for deterministic outputs, all document links, catalog coverage and HTML references. See `VALIDATION.md` for actual browser results and screenshots once captured.
