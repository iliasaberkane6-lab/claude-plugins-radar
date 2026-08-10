"""Registry data model and YAML loading for awesome lists."""

from __future__ import annotations

import re
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional

import yaml

ENTRY_REQUIRED = ("name", "repo")
CATEGORY_ID_RE = re.compile(r"^[a-z0-9-]+$")


@dataclass
class Entry:
    name: str
    repo: str
    category: str
    description: str = ""
    install: str = ""
    tags: List[str] = field(default_factory=list)
    official: bool = False
    stars: Optional[int] = None
    forks: Optional[int] = None
    language: str = ""
    license: str = ""
    last_push: str = ""
    archived: bool = False
    missing: bool = False

    @property
    def url(self) -> str:
        return f"https://github.com/{self.repo}"

    @property
    def display_description(self) -> str:
        return self.description or "*(no description available)*"


@dataclass
class Category:
    id: str
    title: str
    subtitle: str = ""
    entries: List[Entry] = field(default_factory=list)


@dataclass
class Registry:
    title: str = ""
    description: str = ""
    categories: List[Category] = field(default_factory=list)

    def all_entries(self) -> List[Entry]:
        return [e for c in self.categories for e in c.entries]


def load_registry(path: Path) -> Registry:
    raw = yaml.safe_load(Path(path).read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError("registry must be a YAML mapping")

    list_meta = raw.get("list", {}) or {}
    reg = Registry(
        title=str(list_meta.get("title", "")),
        description=str(list_meta.get("description", "")),
    )

    categories = raw.get("categories", []) or []
    if not categories:
        raise ValueError("registry has no categories")

    for cat in categories:
        cid = str(cat.get("id", ""))
        if not CATEGORY_ID_RE.fullmatch(cid):
            raise ValueError(f"invalid category id: {cid!r} (use lowercase letters, digits, dashes)")
        cat_obj = Category(id=cid, title=str(cat.get("title", cid)), subtitle=str(cat.get("subtitle", "")))
        for e in cat.get("entries", []) or []:
            if not isinstance(e, dict):
                raise ValueError(f"entry in '{cid}' must be a mapping")
            missing = [f for f in ENTRY_REQUIRED if not e.get(f)]
            if missing:
                raise ValueError(f"entry in '{cid}' missing required fields: {', '.join(missing)}")
            cat_obj.entries.append(
                Entry(
                    name=str(e["name"]).strip(),
                    repo=str(e["repo"]).strip().lower(),
                    category=cid,
                    description=str(e.get("description") or "").strip(),
                    install=str(e.get("install") or "").strip(),
                    tags=[str(t) for t in (e.get("tags") or [])],
                    official=bool(e.get("official", False)),
                )
            )
        if cat_obj.entries:
            reg.categories.append(cat_obj)

    if not reg.categories:
        raise ValueError("registry has no entries")
    return reg


def dump_registry(reg: Registry, path: Path) -> None:
    """Serialize a registry back to YAML (used by future tooling)."""
    payload: Dict[str, Any] = {
        "list": {"title": reg.title, "description": reg.description},
        "categories": [
            {
                "id": c.id,
                "title": c.title,
                "subtitle": c.subtitle,
                "entries": [
                    {
                        "name": e.name,
                        "repo": e.repo,
                        "description": e.description,
                        "install": e.install,
                        "tags": e.tags,
                        "official": e.official,
                    }
                    for e in c.entries
                ],
            }
            for c in reg.categories
        ],
    }
    Path(path).write_text(
        yaml.safe_dump(payload, sort_keys=False, allow_unicode=True, width=120),
        encoding="utf-8",
    )
