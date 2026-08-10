"""Command-line interface for awesome-guard."""

from __future__ import annotations

import argparse
import sys
from datetime import datetime, timezone
from pathlib import Path

from . import __version__, github, model, render


def _load(registry: str) -> model.Registry:
    return model.load_registry(Path(registry))


def cmd_check(args: argparse.Namespace) -> int:
    reg = _load(args.registry)
    errors: list[str] = []
    seen: set[str] = set()
    total = 0
    for cat in reg.categories:
        for entry in cat.entries:
            total += 1
            if entry.repo in seen:
                errors.append(f"{entry.repo}: duplicate repository")
            seen.add(entry.repo)
            if entry.repo.count("/") != 1 or " " in entry.repo:
                errors.append(f"{entry.repo}: repo must look like 'owner/name'")
            if entry.official and not entry.install:
                errors.append(f"{entry.repo}: official entries should include an install hint")
    if errors:
        for err in errors:
            print(f"error: {err}", file=sys.stderr)
        return 1
    print(f"OK: {total} entries across {len(reg.categories)} categories (schema valid)")
    return 0


def cmd_refresh(args: argparse.Namespace) -> int:
    reg = _load(args.registry)
    token = args.token or github.get_token()
    readme_path = Path(args.readme)
    json_path = Path(args.json)
    readme = readme_path.read_text(encoding="utf-8")

    entries = reg.all_entries()
    if args.offline:
        live = {e.repo: {"exists": True} for e in entries}
    else:
        print(f"Fetching live GitHub data for {len(entries)} repos ...")
        live = github.fetch_all(entries, token=token, max_workers=args.workers)

    missing: list[str] = []
    rate_limited = False
    for entry in entries:
        info = live.get(entry.repo, {})
        if info.get("rate_limited"):
            rate_limited = True
            continue
        if not info.get("exists"):
            entry.missing = True
            missing.append(entry.repo)
            continue
        entry.stars = info.get("stars")
        entry.forks = info.get("forks")
        entry.language = info.get("language") or ""
        entry.license = info.get("license") or ""
        entry.last_push = info.get("last_push") or ""
        entry.archived = bool(info.get("archived"))
        if not entry.description and info.get("description"):
            entry.description = info["description"]

    for cat in reg.categories:
        cat.entries = [e for e in cat.entries if not e.missing]

    now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")
    readme = render.apply_blocks(readme, {c.id: render.render_category(c) for c in reg.categories})
    readme = render.apply_blocks(
        readme,
        {"__meta__": render.render_meta(reg, now, missing, rate_limited)},
        render.META_START,
        render.META_END,
    )
    readme_path.write_text(readme, encoding="utf-8")
    render.dump_json(render.build_json(reg, now, missing), str(json_path))

    print(f"Updated {len(reg.all_entries())} entries -> {readme_path.name} and {json_path.name}")
    if missing:
        print(f"warning: unverified entries (removed): {', '.join(missing)}", file=sys.stderr)
    if rate_limited:
        print("warning: GitHub API rate limit reached; rerun later for complete data", file=sys.stderr)
    if missing and not args.allow_missing:
        return 1
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="awesome-guard",
        description="Keep an awesome list live: fetch GitHub stats, render README tables, emit JSON.",
    )
    parser.add_argument("--version", action="version", version=f"%(prog)s {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    p_check = sub.add_parser("check", help="validate the registry schema (no network)")
    p_check.add_argument("--registry", default="data/entries.yml")
    p_check.set_defaults(func=cmd_check)

    p_refresh = sub.add_parser("refresh", help="fetch live stats and regenerate README + JSON")
    p_refresh.add_argument("--registry", default="data/entries.yml")
    p_refresh.add_argument("--readme", default="README.md")
    p_refresh.add_argument("--json", default="awesome.json")
    p_refresh.add_argument("--token", default=None, help="GitHub token (or GH_TOKEN / GITHUB_TOKEN env)")
    p_refresh.add_argument("--offline", action="store_true", help="skip network; use registry values only")
    p_refresh.add_argument("--allow-missing", action="store_true", help="exit 0 even if repos are unverified")
    p_refresh.add_argument("--workers", type=int, default=6, help="concurrent GitHub requests")
    p_refresh.set_defaults(func=cmd_refresh)

    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except (ValueError, OSError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
