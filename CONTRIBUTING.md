# Contributing

Thanks for helping to keep the Radar accurate. Three contribution paths:

## 1. Add a tool to the catalog

Open a pull request that edits [`data/entries.yml`](data/entries.yml). Use the
[add-tool template](.github/PULL_REQUEST_TEMPLATE/add-tool.md) — it pre-fills the checklist.

Every entry must satisfy the **quality bar**:

- **Real and public** — the repo exists, is public, and is actively maintained (a push within the last ~6 months).
- **Claude Code relevant** — a plugin, skill, agent framework, marketplace, MCP server or catalog for the Claude Code ecosystem. Pure general-purpose libraries are out of scope.
- **Descriptive** — a one-line description in the entry (max ~100 chars). The bot fills gaps from the GitHub description, but a human-written line wins.
- **No spam** — no forks, no templates of this very repo, no renamed clones of a tool already listed.

Checklist for your PR:

```markdown
- [ ] Repo is public and exists (I verified the URL)
- [ ] Repo was pushed to within the last ~6 months
- [ ] Entry is Claude Code relevant (plugin / skill / agent / marketplace / MCP / catalog)
- [ ] Description written by hand, max ~100 chars
- [ ] `repo` is in `owner/name` format
- [ ] I ran `pip install awesome-guard && awesome-guard check` locally
```

The CI workflow validates the schema and refreshes the entry's live stats automatically.
Merge happens after the maintainer (or a bot) verifies the URL.

## 2. Report a dead or outdated entry

Open an issue with the repo name and what's wrong (404, archived, renamed, no longer Claude-Code-related).
The maintainer verifies and removes or updates it within a few days.

## 3. Improve the engine (`awesome-guard`)

Small, stdlib-first codebase in `src/awesome_guard/`. Keep it dependency-light (PyYAML is the only
third-party dependency — deliberate), keep tests runnable with plain `pytest`, and update the
`--help` texts if you touch CLI behavior.

```bash
pip install -e .
awesome-guard check
awesome-guard refresh --offline   # no network, for development
```

## Maintainers

Maintainers commit to:

- reviewing submissions within 7 days,
- running `awesome-guard refresh` (the daily action does this automatically),
- never adding entries they have not verified themselves.
