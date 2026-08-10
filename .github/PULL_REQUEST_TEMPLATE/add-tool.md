---
name: Add a tool to the catalog
about: Add a verified Claude Code plugin, skill, agent or marketplace to data/entries.yml
title: "add: <repo owner>/<repo name>"
labels: ["catalog"]
---

## What are you adding?

- **Name:** <display name>
- **Repo:** <owner/repo>
- **Category:** frameworks | plugins | memory | skills | agents | quality | catalogs

## Quality bar (all must be checked)

- [ ] Repo is public and exists (I verified the URL)
- [ ] Repo was pushed to within the last ~6 months
- [ ] Entry is Claude Code relevant (plugin / skill / agent / marketplace / MCP / catalog)
- [ ] Description written by hand, max ~100 chars
- [ ] `repo` is in `owner/name` format
- [ ] I ran `pip install awesome-guard && awesome-guard check` locally

## Description (one line)

<one sentence: what it does, who it is for>

## Install hint (short)

<`plugin: owner/marketplace`, `npm: package`, clone target or repo path — see README conventions>
