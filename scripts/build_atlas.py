"""Build and verify the GitHub-native HELIOS research atlas.

Uses only the Python standard library. No attached evidence or network access is read.
"""

from __future__ import annotations

import argparse
import html
import json
import math
import re
import sys
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit


ROOT = Path(__file__).resolve().parents[1]
ATLAS = ROOT / "atlas"
HEAD = re.compile(r"(?m)^## (\d{3}) · (.+?)\s*$")
CHAPTER = re.compile(r"(?m)^# (\d{2}) · (.+?)\s*$")
URL = re.compile(r"https://[^\s)<>]+")
LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
COLORS = (
    "#39e6d2", "#76a9ff", "#ffca76", "#c895ff", "#70d4ff",
    "#f493bd", "#8ce9a1", "#e9ba81", "#a9b8ff", "#ff9a89",
    "#9ce0df", "#d3dc78", "#eca7ef", "#80d8a8", "#8fbbff",
)


def normalized(value: str) -> str:
    value = unicodedata.normalize("NFKC", value).casefold()
    return "".join(ch for ch in value if ch.isalnum())


def plain(value: str) -> str:
    value = re.sub(r"!?\[([^\]]+)\]\([^)]+\)", r"\1", value)
    value = re.sub(r"<[^>]+>", "", value)
    value = re.sub(r"[`*_>#|]", " ", value)
    return " ".join(value.split())


def thesis_from(body: str) -> str:
    match = re.search(r"\*\*(?:Hypothesis|Thesis)\.\*\*\s*(.*?)\s+\*\*", body, re.S)
    if match:
        return plain(match.group(1))
    return plain(body)[:260]


def parse() -> tuple[list[dict], list[dict]]:
    files = sorted(ATLAS.glob("[0-9][0-9]-*.md"))
    if len(files) != 15:
        raise ValueError(f"expected 15 atlas chapters; found {len(files)}")
    chapters: list[dict] = []
    ideas: list[dict] = []
    for index, file in enumerate(files, 1):
        if not file.name.startswith(f"{index:02d}-"):
            raise ValueError(f"missing or duplicate chapter {index:02d}")
        content = file.read_text(encoding="utf-8")
        chapter_match = CHAPTER.search(content)
        if not chapter_match or int(chapter_match.group(1)) != index:
            raise ValueError(f"chapter heading invalid: {file}")
        title = chapter_match.group(2).strip()
        headings = list(HEAD.finditer(content))
        if len(headings) != 10:
            raise ValueError(f"{file.name}: expected 10 ideas, found {len(headings)}")
        chapters.append({"number": index, "title": title, "path": file.relative_to(ROOT).as_posix()})
        for offset, heading in enumerate(headings):
            idea_id = int(heading.group(1))
            expected = (index - 1) * 10 + offset + 1
            if idea_id != expected:
                raise ValueError(f"{file.name}: expected idea {expected:03d}, got {idea_id:03d}")
            anchor = f"m{idea_id:03d}"
            if f'<a id="{anchor}"></a>\n\n' not in content[max(0, heading.start() - 40):heading.start()]:
                raise ValueError(f"idea {idea_id:03d} is missing its stable anchor")
            body = content[heading.end(): headings[offset + 1].start() if offset < 9 else len(content)]
            source_urls = sorted(set(URL.findall(body)))
            if not source_urls:
                raise ValueError(f"idea {idea_id:03d} has no direct source URL")
            for source in source_urls:
                if urlsplit(source).hostname is None:
                    raise ValueError(f"idea {idea_id:03d} has malformed source URL: {source}")
            prose = plain(body)
            word_count = len(prose.split())
            if word_count < 65:
                raise ValueError(f"idea {idea_id:03d} is too thin: {word_count} words")
            paragraphs = [plain(p) for p in re.split(r"\n\s*\n", body) if plain(p)]
            abstract = next((p[:280] for p in paragraphs if len(p) > 45), prose[:280])
            ideas.append({
                "id": f"{idea_id:03d}",
                "title": heading.group(2).strip(),
                "chapter": index,
                "theme": title,
                "path": file.relative_to(ROOT).as_posix(),
                "anchor": anchor,
                "thesis": thesis_from(body),
                "abstract": abstract,
                "word_count": word_count,
                "source_urls": source_urls,
                "status": "research proposal; not implemented or validated",
            })
    if len(ideas) != 150 or [int(item["id"]) for item in ideas] != list(range(1, 151)):
        raise ValueError("catalog must contain IDs 001–150 exactly once")
    names = [normalized(item["title"]) for item in ideas]
    if len(names) != len(set(names)):
        raise ValueError("duplicate normalized idea titles")
    if not (ROOT / "SOURCES.md").exists():
        raise ValueError("SOURCES.md is missing")
    source_ledger = (ROOT / "SOURCES.md").read_text(encoding="utf-8")
    uncataloged = sorted({url for item in ideas for url in item["source_urls"] if url not in source_ledger})
    if uncataloged:
        raise ValueError(f"{len(uncataloged)} cited source URLs are absent from SOURCES.md")
    return chapters, ideas


def check_local_links() -> None:
    for file in ROOT.rglob("*.md"):
        if ".git" in file.parts:
            continue
        for href in LINK.findall(file.read_text(encoding="utf-8")):
            if href.startswith(("https://", "http://", "mailto:", "data:")):
                continue
            path_part, _, fragment = href.partition("#")
            target = (file.parent / unquote(path_part)).resolve() if path_part else file
            if not target.is_relative_to(ROOT) or not target.exists():
                raise ValueError(f"broken local link in {file.relative_to(ROOT)}: {href}")
            if re.fullmatch(r"m\d{3}", fragment) and f'<a id="{fragment}"></a>' not in target.read_text(encoding="utf-8"):
                raise ValueError(f"broken mission anchor in {file.relative_to(ROOT)}: {href}")


def make_index(chapters: list[dict]) -> str:
    rows = ["| Orbit | Domain | Missions |", "| :--- | :--- | :---: |"]
    for chapter in chapters:
        lo = (chapter["number"] - 1) * 10 + 1
        hi = lo + 9
        rows.append(
            f'| {chapter["number"]:02d} | [{chapter["title"]}]({chapter["path"]}) | {lo:03d}–{hi:03d} |'
        )
    return "\n".join(rows)


def mission_index(chapters: list[dict], ideas: list[dict]) -> str:
    lines = [
        "# Mission index · all 150 ideas",
        "",
        "Every mission links to its full model, authorized data plan, falsifiable test, boundary, and sources. These are proposed research programs; no performance has been demonstrated here.",
        "",
        "[Return to the atlas](README.md) · [Research method](editorial/RESEARCH_METHOD.md) · [Primary sources](SOURCES.md)",
        "",
    ]
    for chapter in chapters:
        n = chapter["number"]
        lines += [f'## {n:02d} · {chapter["title"]}', "", "| ID and mission | Testable thesis |", "| --- | --- |"]
        for item in ideas[(n - 1) * 10:n * 10]:
            link = f'{item["path"]}#{item["anchor"]}'
            thesis = item["thesis"].replace("|", "\\|")
            lines.append(f'| [{item["id"]} · {item["title"]}]({link}) | {thesis} |')
        lines.append("")
    return "\n".join(lines)


def cover_svg() -> str:
    stars = []
    for i in range(72):
        x = (i * 293 + 71) % 1600
        y = (i * 197 + 37) % 490
        r = 1.2 if i % 7 else 2.2
        stars.append(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#a9bedb" opacity="{0.25 + (i % 5) * .11:.2f}"/>')
    orbits = []
    for j in range(6):
        r = 78 + j * 40
        orbits.append(f'<circle cx="1290" cy="245" r="{r}" fill="none" stroke="#62dbde" stroke-width="1" opacity="{.35 - j*.035:.2f}"/>')
    nodes = []
    for j in range(15):
        a = -math.pi / 2 + 2 * math.pi * j / 15
        r = 100 + 17 * (j % 5)
        x, y = 1290 + r * math.cos(a), 245 + r * math.sin(a)
        nodes.append(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="6" fill="{COLORS[j]}"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1600" height="490" viewBox="0 0 1600 490" role="img" aria-label="Project HELIOS, Cyber Mission Atlas: 150 research missions across 15 domains">
<defs><linearGradient id="night" x2="1" y2="1"><stop stop-color="#08172b"/><stop offset="1" stop-color="#132c49"/></linearGradient><radialGradient id="sun"><stop stop-color="#fff2bb"/><stop offset=".45" stop-color="#ffcc73"/><stop offset="1" stop-color="#f47f74"/></radialGradient></defs>
<rect width="1600" height="490" rx="22" fill="url(#night)"/>
<g>{''.join(stars)}</g><g>{''.join(orbits)}</g><g>{''.join(nodes)}</g>
<circle cx="1290" cy="245" r="50" fill="url(#sun)"/><circle cx="1290" cy="245" r="65" fill="none" stroke="#ffce89" opacity=".5"/>
<path d="M65 380 H1050" stroke="#66e3e0" stroke-width="2" opacity=".6"/>
<text x="66" y="128" fill="#68e4dc" font-family="Arial, sans-serif" font-size="25" font-weight="700" letter-spacing="7">CYBERENGINEERING / RESEARCH ATLAS</text>
<text x="60" y="260" fill="#f4f8ff" font-family="Arial, sans-serif" font-size="106" font-weight="800" letter-spacing="6">HELIOS</text>
<text x="66" y="336" fill="#c4d5eb" font-family="Arial, sans-serif" font-size="32">150 testable missions · 15 domains · one evidence standard</text>
<text x="66" y="437" fill="#a8c1db" font-family="Arial, sans-serif" font-size="21" letter-spacing="3">SYSTEMS • HARDWARE • SOFTWARE • SPACE • HUMAN DECISION</text>
</svg>'''


def constellation_svg(chapters: list[dict]) -> str:
    rows = []
    for i, ch in enumerate(chapters):
        y = 147 + i * 62
        c = COLORS[i]
        dots = "".join(
            f'<circle cx="{1005 + n*44}" cy="{y-7}" r="9" fill="{c}" opacity="{.5 + n*.045:.2f}"/>'
            for n in range(10)
        )
        rows.append(f'<g><text x="50" y="{y}" fill="{c}" font-size="22" font-weight="700">{i+1:02d}</text><text x="108" y="{y}" fill="#e3edfa" font-size="21">{html.escape(ch["title"])}</text><text x="848" y="{y}" fill="#aebed4" font-size="17">{i*10+1:03d}–{i*10+10:03d}</text><line x1="50" y1="{y+17}" x2="1470" y2="{y+17}" stroke="#40566e" opacity=".5"/>{dots}</g>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="1520" height="1120" viewBox="0 0 1520 1120" role="img" aria-label="Fifteen HELIOS research domains, each containing ten ideas">
<rect width="1520" height="1120" rx="20" fill="#0b192e"/><text x="50" y="60" fill="#f2f7ff" font-family="Arial, sans-serif" font-size="38" font-weight="700">THE 150-MISSION CONSTELLATION</text><text x="50" y="98" fill="#aabdd4" font-family="Arial, sans-serif" font-size="20">Every dot is one proposal · color groups a research domain · numbers preserve reading order</text>
<g font-family="Arial, sans-serif">{''.join(rows)}</g><text x="50" y="1095" fill="#8099b4" font-family="Arial, sans-serif" font-size="16">Concept atlas · no deployment or performance claims</text></svg>'''


def render() -> dict[Path, str]:
    chapters, ideas = parse()
    check_local_links()
    catalog = {
        "project": "Project HELIOS · Cyber Mission Atlas",
        "status": "150 research proposals; no empirical performance is claimed",
        "count": len(ideas),
        "chapters": chapters,
        "ideas": ideas,
    }
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    begin, end = "<!-- ATLAS_INDEX_START -->", "<!-- ATLAS_INDEX_END -->"
    if readme.count(begin) != 1 or readme.count(end) != 1:
        raise ValueError("README index markers missing or repeated")
    start = readme.index(begin) + len(begin)
    stop = readme.index(end)
    readme = readme[:start] + "\n" + make_index(chapters) + "\n" + readme[stop:]
    return {
        ROOT / "README.md": readme,
        ROOT / "INDEX.md": mission_index(chapters, ideas),
        ROOT / "data" / "ideas.json": json.dumps(catalog, indent=2, ensure_ascii=False) + "\n",
        ROOT / "assets" / "cover.svg": cover_svg() + "\n",
        ROOT / "assets" / "constellation.svg": constellation_svg(chapters) + "\n",
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="fail if generated files are stale")
    args = ap.parse_args()
    try:
        outputs = render()
        for path, data in outputs.items():
            if args.check:
                if not path.exists() or path.read_text(encoding="utf-8") != data:
                    raise ValueError(f"generated file is stale: {path.relative_to(ROOT)}")
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(data, encoding="utf-8", newline="\n")
        print("Validated 150 unique, cited ideas in 15 ordered chapters.")
        return 0
    except ValueError as exc:
        print(f"Atlas validation failed: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
