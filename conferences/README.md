# SIGNAL · DEF CON 34 onward

This is a **partial source-backed schedule catalog**, reviewed on 2026-10-03. It contains every row in the retrieved DEF CON 34 Recon Village schedule and the distinct desktop creator-stage sessions in the retrieved Adversary Village page. It does not establish that every DEF CON talk, recording or slide deck has been retrieved. Scheduled sessions are not proof that a talk took place.

The machine-readable [catalog](../data/conferences/defcon.json) records title, listed speakers, session type, available time/location fields, source and availability. Unknown video/slide URLs are `null`; no recording or slide files were downloaded. Offensive talk titles are bibliographic metadata; this project does not reproduce their exploitation workflows.

| Source | Coverage or retrieval outcome |
|---|---|
| [Official DEF CON 34 guide](https://info.defcon.org/defcon34/menu/) | HTTP 502; public runtime JSON export also 502 |
| [Recon Village schedule](https://reconvillage.org/reconvillage-2026-defcon-34/talks) | Full published schedule retrieved: 14 talks and six workshops |
| [Adversary Village](https://adversaryvillage.org/adversary-events/DEFCON-34/) | Creator-stage desktop schedule retrieved: 12 distinct talks/panels; mobile duplicates removed; other village activities outside this extract |
| [Official media archive](https://media.defcon.org/DEF%20CON%2034/) | Direct retrieval 502; research service reports robots restriction |
| [Guide source repository](https://github.com/junctor/hackertracker-info) | README and tree inspected; runtime conference export absent from inspected repository |
| [DEF CON calendar](https://forum.defcon.org/calendar) | Indexed publisher listing places DEF CON 35 in August 2027; future at review time |

## Expand without losing provenance

For each newly accessible source, record its URL, retrieval date, content digest and selection rule. Preserve publisher titles and public speaker labels. Match records by publisher session ID where available; otherwise review normalized title, speakers, village and time together. Do not merge similar titles automatically. Treat a repeat performance as a separate event when its event identity differs.

Separate **schedule coverage**, **recording availability**, **slide availability** and **content review**. A downloaded playlist is not proof of full conference coverage. Keep counts denominated by the actual source scope; do not calculate a conference completion percentage without a known denominator. Respect publisher permissions; link to media rather than republishing copyrighted recordings or full abstracts.

## Turn a talk into a research question

Record a one-sentence claim, the evidence presented, a competing explanation, assumptions and a falsifiable test. Design a local or synthetic evaluation around a defensive outcome: detection quality, parser correctness, uncertainty, provenance or recovery. Split by independent environment or event, report baseline and ablation results, and avoid using the same examples for training and evaluation. Tool demonstrations are not comparative scientific validation.

The site provides searchable metadata, source filters and browser-local bookmarks. Bookmarks are personal learning notes on that browser, not attendance or public endorsements.
