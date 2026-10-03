"""Validate beginner fixtures and optionally exercise only a local HTTP service."""
import argparse
import functools
import hashlib
import http.server
import json
from pathlib import Path
import re
import shutil
import subprocess
import threading
import urllib.error
import urllib.parse
import urllib.request

ROOT = Path(__file__).resolve().parents[1]


def load(path):
    return json.loads((ROOT / path).read_text())


def heading_ids(text):
    return {
        re.sub(r"[^\w\s-]", "", match.group(1).lower()).strip().replace(" ", "-")
        for match in re.finditer(r"^#{1,6}\s+(.+)$", text, re.MULTILINE)
    }


def check_links():
    pages = list((ROOT / "foundations").rglob("*.md"))
    pages.append(ROOT / "intelligence/CHURCH-FORGE.md")
    pages.extend((ROOT / "community").glob("*.md"))
    pages.append(ROOT / "DELIVERY_STATUS.md")
    for page in pages:
        for match in re.finditer(r"\[[^\]]*\]\(([^)]+)\)", page.read_text()):
            target = urllib.parse.urlsplit(match.group(1))
            if target.scheme or target.netloc:
                continue
            path = (page.parent / urllib.parse.unquote(target.path)).resolve() if target.path else page
            if not path.is_file():
                raise ValueError(f"Missing link in {page.relative_to(ROOT)}: {match.group(1)}")
            if target.fragment and path.suffix == ".md" and target.fragment not in heading_ids(path.read_text()):
                raise ValueError(f"Missing heading in {path.relative_to(ROOT)}: {target.fragment}")


def validate():
    tools = (ROOT / "foundations/TOOLS.md").read_text()
    ids = re.findall(r"^### (\d{2}) · ", tools, re.MULTILINE)
    if ids != [f"{i:02d}" for i in range(1, 21)]:
        raise ValueError("Core tool entries must remain 01–20")
    fixture = load("foundations/fixtures/events.json")
    events = fixture["events"]
    if fixture["evidence_class"] != "synthetic" or len(events) != 8:
        raise ValueError("Unexpected classroom fixture")
    if [e["sequence"] for e in events] != list(range(1, 9)):
        raise ValueError("Fixture sequence")
    denied = [e for e in events if e["event"] == "sign_in" and e["result"] == "denied"]
    allowed = [e for e in events if e["event"] == "sign_in" and e["result"] == "allowed"]
    unknown = [e for e in events if e["result"] == "unknown"]
    if (len(denied), len(allowed), len(unknown)) != (3, 1, 1):
        raise ValueError("Lab's stated counts no longer match its input")
    integrity = load("foundations/fixtures/integrity.json")
    content = (ROOT / "foundations/fixtures/note.txt").read_bytes()
    if integrity["bytes"] != len(content) or integrity["sha256"] != hashlib.sha256(content).hexdigest():
        raise ValueError("Integrity reference differs from fixture bytes")
    catalog = load("data/intelligence/forge_catalog.json")
    rows = catalog["repositories"]
    sources = {s["id"]: s for s in catalog["sources"]}
    if catalog["count"] != len(rows) or len({x["repository_path"] for x in rows}) != len(rows):
        raise ValueError("Forge catalog coverage")
    if sources[catalog["primary_source_id"]]["url"] != "https://git.churchofmalware.org/explore/repos":
        raise ValueError("Wrong user-selected primary source")
    for source_id, source in sources.items():
        expected = source["visible_records_reviewed"]
        if sum(source_id in row["source_ids"] for row in rows) != expected:
            raise ValueError("Listing/source coverage does not reconcile")
    for row in rows:
        if not set(row["source_ids"]).issubset(sources) or row["integration_status"] != "REFERENCE ONLY":
            raise ValueError("Unbound source or unsupported integration claim")
    check_links()
    print("Validated 20 core tool entries, eight synthetic events, integrity bytes, source-bound forge metadata records and local links.")


def smoke():
    class Handler(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *args):
            pass

    handler = functools.partial(Handler, directory=str(ROOT / "foundations/fixtures/web"))
    server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    base = f"http://127.0.0.1:{server.server_port}"
    opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
    try:
        with opener.open(base + "/health.json", timeout=5) as response:
            body = json.loads(response.read())
            if response.status != 200 or body.get("evidence_class") != "synthetic" or body.get("status") != "ok":
                raise ValueError("Loopback health response differs from documented fixture")
        try:
            opener.open(base + "/not-present.txt", timeout=5)
        except urllib.error.HTTPError as error:
            if error.code != 404:
                raise
        else:
            raise ValueError("Missing path did not return 404")
        curl = shutil.which("curl")
        if curl is None:
            raise RuntimeError("curl is required for the documented HTTP smoke")
        success = subprocess.run([curl, "--noproxy", "*", "--silent", "--show-error", "--include", base + "/health.json"], capture_output=True, text=True, timeout=5)
        failure = subprocess.run([curl, "--noproxy", "*", "--silent", "--show-error", "--fail", base + "/not-present.txt"], capture_output=True, text=True, timeout=5)
        if success.returncode != 0 or '"status": "ok"' not in success.stdout or failure.returncode != 22:
            raise ValueError("curl result does not match tutorial's success/error explanation")
        print("Loopback-only smoke passed: HTTP 200/404, curl success and --fail exit 22; temporary server closed.")
    finally:
        server.shutdown()
        server.server_close()
        thread.join(timeout=5)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--smoke", action="store_true", help="Run the bounded local HTTP/curl check")
    args = parser.parse_args()
    validate()
    if args.smoke:
        smoke()
