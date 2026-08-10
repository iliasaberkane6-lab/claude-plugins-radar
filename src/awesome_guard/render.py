"""Rendering: README tables, machine-readable JSON, marker block handling."""

from __future__ import annotations

import json
import re
from typing import Dict, List, Optional

from .model import Category, Entry, Registry

BLOCK_START = "<!-- AG-START:{id} -->"
BLOCK_END = "<!-- AG-END:{id} -->"
META_START = "<!-- AG-META:START -->"
META_END = "<!-- AG-META:END -->"

STAR_COLORS = {5_000: "#2da44e", 1_000: "#1f6feb"}  # thresholds checked in descending order


def fmt_count(n: Optional[int]) -> str:
    if n is None:
        return "—"
    if n >= 1000:
        return f"{n / 1000:.1f}k"
    return str(n)


def _esc(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def render_category(cat: Category) -> str:
    lines = [
        "| Project | What it does | Stars | Updated | Install |",
        "| --- | --- | ---: | --- | --- |",
    ]
    for e in sorted(cat.entries, key=lambda x: (x.stars if x.stars is not None else -1), reverse=True):
        badges = ""
        if e.official:
            badges += " <sub>✅ official</sub>"
        if e.archived:
            badges += " <sub>🔴 archived</sub>"
        name = f"[{e.name}]({e.url}){badges}"
        desc = e.display_description.strip("`")
        if len(desc) > 100:
            desc = desc[:99].rstrip() + "…"
        updated = e.last_push or "—"
        install = _esc(e.install or "—")
        lines.append(f"| {name} | {_esc(desc)} | {fmt_count(e.stars)} | {updated} | `{install}` |")
    return "\n".join(lines)


def render_meta(reg: Registry, updated_at: str, missing: List[str], rate_limited: bool) -> str:
    total = len(reg.all_entries())
    head = (
        f"> **Last refreshed:** `{updated_at}` · **{total} repos** tracked · "
        f"**{len(reg.categories)}** categories · source: `data/entries.yml`"
    )
    if rate_limited:
        head += "\n> ⚠️ GitHub API rate limit hit — some stats may be stale until the next run."
    if missing:
        head += "\n> ⚠️ Unverified entries (hidden from tables): " + ", ".join(f"`{r}`" for r in missing)
    return head


def apply_blocks(
    text: str,
    blocks: Dict[str, str],
    start_tpl: str = BLOCK_START,
    end_tpl: str = BLOCK_END,
) -> str:
    for marker_id, content in blocks.items():
        pattern = re.compile(
            re.escape(start_tpl.format(id=marker_id))
            + r".*?"
            + re.escape(end_tpl.format(id=marker_id)),
            re.DOTALL,
        )
        if not pattern.search(text):
            raise ValueError(f"marker block not found in target file: {marker_id}")
        replacement = (
            start_tpl.format(id=marker_id)
            + "\n\n"
            + content.strip()
            + "\n\n"
            + end_tpl.format(id=marker_id)
        )
        text = pattern.sub(lambda _m: replacement, text, count=1)
    return text


def build_json(reg: Registry, updated_at: str, missing: List[str]) -> dict:
    categories = []
    for cat in reg.categories:
        entries = [
            {
                "name": e.name,
                "repo": e.repo,
                "url": e.url,
                "description": e.display_description,
                "tags": e.tags,
                "official": e.official,
                "install": e.install,
                "stars": e.stars,
                "forks": e.forks,
                "language": e.language,
                "license": e.license,
                "last_push": e.last_push,
                "archived": e.archived,
                "verified": True,
            }
            for e in sorted(cat.entries, key=lambda x: (x.stars if x.stars is not None else -1), reverse=True)
        ]
        categories.append(
            {"id": cat.id, "title": cat.title, "subtitle": cat.subtitle, "entries": entries}
        )
    return {
        "schema": "awesome-guard/v1",
        "title": reg.title,
        "description": reg.description,
        "updated_at": updated_at,
        "repo_count": len(reg.all_entries()),
        "category_count": len(reg.categories),
        "unverified": missing,
        "categories": categories,
    }


def dump_json(payload: dict, path: str) -> None:
    with open(path, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, indent=2, ensure_ascii=False)
        fh.write("\n")
