"""Minimal GitHub API client (stdlib only)."""

from __future__ import annotations

import json
import os
from concurrent.futures import ThreadPoolExecutor, as_completed
from typing import Dict, List, Optional
from urllib import request
from urllib.error import HTTPError, URLError

from .model import Entry

API_REPO = "https://api.github.com/repos/{full_name}"

_UA = "awesome-guard/0.1 (+https://github.com/__GH_USER__/claude-plugins-radar)"


def _get(url: str, token: Optional[str]) -> dict:
    headers = {
        "User-Agent": _UA,
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = request.Request(url, headers=headers)
    with request.urlopen(req, timeout=20) as resp:
        return json.loads(resp.read().decode("utf-8"))


def fetch_repo(full_name: str, token: Optional[str]) -> dict:
    try:
        d = _get(API_REPO.format(full_name=full_name), token)
        lic = (d.get("license") or {}).get("spdx_id") or ""
        return {
            "exists": True,
            "stars": d.get("stargazers_count"),
            "forks": d.get("forks_count"),
            "language": d.get("language") or "",
            "license": lic,
            "description": (d.get("description") or "").strip(),
            "last_push": (d.get("pushed_at") or "")[:10],
            "archived": bool(d.get("archived")),
        }
    except HTTPError as exc:
        if exc.code == 404:
            return {"exists": False}
        if exc.code == 403:
            return {"rate_limited": True}
        return {"error": f"HTTP {exc.code}"}
    except URLError as exc:
        return {"error": str(exc.reason)}


def fetch_all(entries: List[Entry], token: Optional[str] = None, max_workers: int = 6) -> Dict[str, dict]:
    results: Dict[str, dict] = {}
    with ThreadPoolExecutor(max_workers=max_workers) as pool:
        futures = {pool.submit(fetch_repo, e.repo, token): e for e in entries}
        for future in as_completed(futures):
            results[futures[future].repo] = future.result()
    return results


def get_token() -> Optional[str]:
    return os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN") or None
