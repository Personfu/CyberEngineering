# Infrastructure-map reference · Source review

**User-supplied URL:** [gangstalkermap.com](https://gangstalkermap.com/). **Reviewed:** 2026-10-03. **Evidence:** indexed first-party page text; direct retrieval was unavailable and a normal HTTP request returned 403. Live map behavior, markers and source freshness were not verified.

The publisher presents the site as an infrastructure-awareness map. Its description names OpenStreetMap-derived infrastructure, ALPR sources, public-camera providers, aircraft data and satellite thermal-anomaly data. These are publisher statements about the application, not independently checked feed coverage. See [CP06 in the source ledger](SOURCES.md).

## Read the evidence at the right level

| Observation or claim | Supported interpretation | Further evidence needed |
|---|---|---|
| The publisher names a data provider | That provider is part of the application's stated design | Actual requests, returned schema and observation/retrieval times |
| An infrastructure marker appears in a dataset | The source contains a record at a stated position | Record provenance, positional uncertainty and current validity |
| A query returns no markers | The queried source/view returned none | Coverage, filters, provider availability and mapping completeness |
| A camera category is assigned | The source or application classified a record | Device type, operator, current operation and field-level evidence |
| An application says “real-time” | The publisher claims a freshness property | Per-source event time, retrieval time and measured age |

An infrastructure record cannot establish who is observing it, whether it is currently operating, or whether a person is being targeted. Keep application labels, source records and analyst interpretations as separate claims.

## Useful engineering lessons

For a future source-backed map, define a record with provider, source URL, record ID, category basis, observed time if known, retrieval time, geographic uncertainty, freshness and coverage state. Keep **unknown time** explicit. Record each layer's success or failure independently so a partial response cannot appear to be complete coverage.

OpenStreetMap's official [copyright and license page](https://www.openstreetmap.org/copyright) supplies attribution and ODbL context. Provider data rights and API usage rules require separate review when importing data; no OSM dataset was acquired here. A website source-code license and a data-provider license govern different things.

## Classroom task

Use an invented record labeled **synthetic** with no real person or location. Give it a known retrieval time and an unknown observation time. Write a source-health note that preserves that uncertainty. Have a teammate explain why retrieval time cannot substitute for observation time and why a missing layer changes the completeness claim.

Connect the exercise to [RT008](../assessment/modules/RT008.md), [RT011](../assessment/modules/RT011.md), [RT022](../assessment/modules/RT022.md) and [the RF/map primer](../foundations/RF-AND-MAPS.md). No location query, camera endpoint, aircraft feed or personal tracking data was collected for this review.
