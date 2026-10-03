"""Build a source-bounded community directory without executing upstream projects."""
import argparse
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]


def render():
    data = json.loads((ROOT / "data/community/catalog.json").read_text())
    sources = {s["id"]: s for s in data["sources"]}
    if len(sources) != len(data["sources"]):
        raise ValueError("Duplicate source ID")
    credits = data["credits"]
    if len(credits) != 15 or len({c["label"] for c in credits}) != 15:
        raise ValueError("Pinned README credit coverage")
    for c in credits:
        if c["source_id"] != "CP03" or c["kind"] != "public_credit_label" or not c["roles"]:
            raise ValueError("Unsupported contributor attribution")
    for x in data["resources"]:
        if x["source_id"] not in sources or x["integration_status"] != "REFERENCE ONLY":
            raise ValueError("Resource must retain a source and reference status")
    for x in data["pinned_file_receipts"]:
        if x["source_id"] not in sources or x["full_source_republished"]:
            raise ValueError("Invalid source receipt")
        if not re.fullmatch(r"[a-f0-9]{40}", x["commit_sha"]) or not re.fullmatch(r"[a-f0-9]{40}", x["git_blob_sha"]) or not re.fullmatch(r"[a-f0-9]{64}", x["sha256"]):
            raise ValueError("Invalid commit/file hash")
    index = ["# ORION · Community and Source Directory", "",
        "Public project references for the HELIOS learning track. Review date: **2026-10-03**. The directory records publisher links, pinned source files and named public credits. Its ten resources are **REFERENCE ONLY**.", "",
        "[ProtoPirate public credits](PROTOPIRATE.md) · [RocketGod website review](ROCKETGOD.md) · [Infrastructure-map source review](MAP-SOURCE-REVIEW.md) · [Source receipts](SOURCES.md) · [Beginner guide](../foundations/README.md) · [Delivery status](../DELIVERY_STATUS.md)", "",
        "## Useful public references", "", "| Resource | Engineering relevance | Inspection state |", "|---|---|---|"]
    for x in data["resources"]:
        index.append(f"| [{x['name']}]({x['url']}) | {x['relevance']} | {x['inspection_state']} |")
    index += ["", "## Documented source relationships", "", "```mermaid", "flowchart TD",
        '    R["Pinned RocketGod website source"] -->|"declares site URL"| B["betaskynet.com link hub"]',
        '    B -->|"links project"| P["ProtoPirate GitHub mirror"]',
        '    B -->|"links project"| M["Infrastructure-map reference"]',
        '    P -->|"README designates upstream"| U["ProtoPirate forge: retrieval blocked"]',
        '    P -->|"README names credits"| C["15 public credit labels"]',
        "```", "", "Edges represent documented links or README statements. They do not establish personal friendship, legal identity, organization membership or intrusion attribution. A linked project can have different ownership, licensing and availability from its link hub.", "",
        "## Use the references to learn", "", "Read the [RF and map primer](../foundations/RF-AND-MAPS.md) to distinguish a signal measurement, a decoded interpretation and an infrastructure record. Review local-device authority, source time and coverage before importing any external data. No device connection, location query, radio action, Discord message or upstream project execution was performed for this directory."]
    proto = ["# ProtoPirate · Public project and credit receipts", "",
        f"**Pinned README:** [CP03]({sources['CP03']['url']}). **Reviewed:** 2026-10-03.", "",
        "The publisher describes ProtoPirate as an experimental Flipper Zero protocol-analysis project associated with The Pirates' Plunder. The pinned README identifies a separate forge as upstream and describes other copies as mirrors. Its stated default transmission behavior is a publisher claim; no hardware or application behavior was tested here.", "",
        f"**Publisher-designated upstream:** [CP05]({sources['CP05']['url']}); direct retrieval returned 403. **License receipt:** [CP04]({sources['CP04']['url']}); GitHub metadata identifies GPL-3.0 and the pinned LICENSE text was inspected. No implementation code was adopted.", "",
        "## All distinct labels in the pinned credit section", "", "| Public credit label | Credited role(s) |", "|---|---|"]
    for c in credits:
        proto.append(f"| {c['label']} | {'; '.join(c['roles'])} |")
    proto += ["", "These are fifteen unique README attribution labels, including a driver reference. A label is not necessarily an individual, a verified GitHub account or a current community member. No real names, private contacts or cross-platform alias matches were inferred. The list covers this pinned credit section, not the entire community.", "",
        "## Connected learning", "", "Use [RF terminology](../foundations/RF-AND-MAPS.md) for modulation, decoding, checksums and uncertainty. Use [RT023](../assessment/modules/RT023.md) for source hygiene, [RT016](../assessment/modules/RT016.md) for versioned inputs and [RT026](../assessment/modules/RT026.md) for explicit scope. Hardware or operational evaluation requires its own defined experiment and authority.", "", "[Source directory](README.md) · [File receipts](SOURCES.md)"]
    rocket = ["# RocketGod · Website source review", "",
        f"**User-supplied website:** [betaskynet.com]({sources['CP01']['url']}). **User-supplied repository, pinned:** [CP02]({sources['CP02']['url']}).", "",
        "The website is a first-party project link hub. Its pinned `index.html` declares betaskynet.com in the page metadata and links to the selected public resources in this directory. The inspected website tree has nine files; `index.html` and `script.js` were read without executing the site. Their hashes and commit references appear in the [receipt ledger](SOURCES.md).", "",
        "The script requests repository information at runtime. Loading labels or counters in static page text are not verified live statistics, and this review records no popularity metrics. A pinned source commit does not establish that production currently serves those same bytes.", "",
        "## License and reuse state", "", "No LICENSE file was present in the inspected website tree, and GitHub returned no detected license. Reuse permission is unresolved. This release adds source references and authored explanations; it does not copy the website's implementation, images or styles into HELIOS.", "",
        "## Relevant learning paths", "", "WebSerial/WebUSB link labels suggest useful questions about browser permissions and owned-device selection, but the linked apps were inaccessible to this retrieval environment. The domain and email tools are references for interpretation and report privacy; no domain query or report upload was submitted. The map references are a reason to study field provenance, time and coverage rather than infer personal intent from a marker.", "",
        "[Public resources](README.md) · [Map review](MAP-SOURCE-REVIEW.md) · [Access receipts](SOURCES.md)"]
    ledger = ["# ORION · Sources, access and pinned file receipts", "",
        "Reviewed on **2026-10-03**. Publication dates are unestablished unless provided separately. Access outcomes describe this research session; a retrieval block does not prove a service is down.", "",
        "| ID | Public source | Type | Access/inspection | Claim limit |", "|---|---|---|---|---|"]
    for s in sources.values():
        ledger.append(f"| {s['id']} | [{s['url']}]({s['url']}) | {s['type']} | {s['access']} | {s['claim_limit']} |")
    ledger += ["", "## Pinned files", "", "| Repository / path | Commit | Git blob | Bytes | SHA-256 of inspected bytes |", "|---|---|---|---:|---|"]
    for f in data["pinned_file_receipts"]:
        url = f"https://github.com/{f['repository']}/blob/{f['commit_sha']}/{f['path']}"
        ledger.append(f"| [{f['repository']} / {f['path']}]({url}) | `{f['commit_sha']}` | `{f['git_blob_sha']}` | {f['bytes']} | `{f['sha256']}` |")
    ledger += ["", "Git blob digests were checked against the retrieved file bytes locally. The complete upstream source files are not vendored here. CI validates receipt structure and source binding, not a fresh remote fetch or upstream functionality.", "", "[Machine-readable catalog](../data/community/catalog.json) · [Source directory](README.md)"]
    return {ROOT / "community/README.md": index, ROOT / "community/PROTOPIRATE.md": proto,
            ROOT / "community/ROCKETGOD.md": rocket, ROOT / "community/SOURCES.md": ledger}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true")
    args = parser.parse_args()
    for path, lines in render().items():
        text = "\n".join(lines) + "\n"
        if args.check:
            if not path.exists() or path.read_text() != text:
                raise SystemExit(f"Stale community document: {path.relative_to(ROOT)}")
        else:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text)
    print("Verified ten source-bound resources, fifteen public credit labels and four pinned file receipts.")
