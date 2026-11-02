# Independent research and review method

Every published review contains product-specific documented features, original analysis, choose/skip guidance, compatibility limits, alternatives, an evaluation plan and a full documentation page. Research uses manufacturer and project-maintainer manuals/repositories. An imported video listing is not a substitute for product research and is not used as review evidence.

## Trace a claim

Each feature carries a source identifier bound to a retrieved document. The [source ledger](PRIMARY-SOURCES.md) records URL, retrieval time, response size and SHA-256. A hash identifies response bytes; it does not establish that a manufacturer claim is independently measured or that a mutable page will remain unchanged.

## Read specifications in context

Separate board revision, MCU, radio, host client, firmware, partition layout and attached accessories. A shared chip is not a matching carrier; an available peripheral is not an implemented application feature. Distinguish a rated capacity or interface from a measured runtime or throughput result. Keep architecture limits such as half duplex, ADC resolution, power budget and memory visible.

Cross-source conflicts stay explicit. For example, the Cardputer ADV manufacturer specification and a Hydra accessory page use different connector counts; the review records that discrepancy and calls for checking the actual pin map rather than choosing a convenient number. Source pages can also be archived, historical or internally inconsistent; the review names those limits.

## Give an original recommendation

Explain the task a product serves and the work it saves. State when a simpler tool is better. Compare the whole system: power, storage, required modules, client support, recovery and maintenance. Do not rank products using copied creator opinions, feature-count totals or invented stars.

## Test the appropriate layer

The workbench contains executed software fixture tests and separately labeled optional-tool and physical-device exercises. Parser tests do not establish RF performance. Browser checks do not establish a device’s battery life. A successful firmware build is not a completed hardware installation. Physical results need an exact device, artifact digest, fixture, method, repeated observations, negative controls and recorded conditions.

## Maintain the library

Edit `data/reviews/catalog.json`, `data/reviews/sources.json` and `data/labs/catalog.json`. The builder generates full product pages, lesson pages, the README index and the site. Update the [coverage register](RESEARCH-COVERAGE.md) when evidence becomes available. It records remaining targets as gaps, not finished reviews.

```bash
python scripts/build_site.py
python scripts/build_site.py --check
python scripts/check_site.py
python -m unittest discover -s tests -v
```

Sources are credited through citations, while the review prose, walkthroughs, scripts and fixtures are original work for this project. No videos, thumbnails or transcripts are republished as the review library.
