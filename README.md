<div align="center">

<img src="docs/banner.png" alt="Claude Plugins Radar" width="100%"/>

# 📡 Claude Plugins Radar

### The live, hand-curated, machine-readable directory of Claude Code plugins, skills & agents.

Every entry is manually verified. Every star count and last-commit date is **refreshed daily** by
[`awesome-guard`](https://pypi.org/project/awesome-guard/) — the open-source engine that runs this repo.

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/Python-3.9%2B-3776AB.svg)](pyproject.toml)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Updated daily](https://img.shields.io/badge/updated-daily-2ea44f.svg)](.github/workflows/refresh.yml)
[![PyPI](https://img.shields.io/pypi/v/awesome-guard.svg)](https://pypi.org/project/awesome-guard)

</div>

---

## Why this list is different

| | |
|---|---|
| 🟢 **Live, not stale** | Every star count and last-commit date is refreshed **every day** by a GitHub Action. Most "awesome" lists rot within weeks — this one cannot. |
| 🤖 **Agent-readable** | The whole catalog ships as [`awesome.json`](awesome.json). Claude Code and other agents can query it directly instead of scraping markdown. |
| ✍️ **Human-curated** | Every entry is manually checked for quality and relevance before it lands. No auto-scraped junk, no dead links. If it's here, it's real. |

## For agents

Claude Code can read this catalog like a database:

```bash
curl -s https://raw.githubusercontent.com/iliasaberkane6-lab/claude-plugins-radar/main/awesome.json
```

Example prompt inside Claude Code:

> Read `https://raw.githubusercontent.com/iliasaberkane6-lab/claude-plugins-radar/main/awesome.json`
> and recommend a memory plugin for Claude Code with more than 10k stars. Explain in two sentences why.

The JSON includes `stars`, `last_push`, `license`, `language`, `tags`, `install` hints and `verified: true`
for every entry — updated daily, schema versioned (`awesome-guard/v1`).

## Quickstart

Install a plugin from the official marketplace (auto-registered):

```bash
/plugin install code-review@claude-plugins-official
```

Install a community plugin (add the marketplace first):

```bash
/plugin marketplace add obra/superpowers-marketplace
/plugin install superpowers@superpowers-marketplace
```

> **Install column conventions:** `plugin:` → add that marketplace first, then install by name.
> `npm:` / `clone:` / bare repo → install via the repo's README. `ccpi` → the
> [ccpi](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) package manager.

## The catalog

Stats are live. Entries sorted by stars within each category. ⚠️ Star counts are a popularity signal,
not a quality rating — read the description before installing.

<!-- AG-META:START -->

> **Last refreshed:** `2026-08-10 19:15 UTC` · **67 repos** tracked · **7** categories · source: `data/entries.yml`

<!-- AG-META:END -->

### Frameworks & Methodology

Change how Claude Code thinks, plans and works — not just what it can access.

<!-- AG-START:frameworks -->

| Project | What it does | Stars | Updated | Install |
| --- | --- | ---: | --- | --- |
| [Superpowers](https://github.com/obra/superpowers) | TDD-first skills framework: planning, brainstorming, structured debugging, skill authoring. | 270.2k | 2026-08-08 | `plugin: obra/superpowers-marketplace` |
| [gstack](https://github.com/garrytan/gstack) | Garry Tan's virtual engineering team: 23 slash-command skills for plan, review, design, QA, securit… | 127.4k | 2026-08-08 | `gstacks.org/install.sh` |
| [ponytail](https://github.com/dietrichgebert/ponytail) | Makes your agent think like the laziest senior dev in the room: short, decisive output. | 100.1k | 2026-08-07 | `DietricGebert/ponytail` |
| [claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | From vibe coding to agentic engineering: battle-tested practices that make Claude better. | 64.3k | 2026-08-10 | `shanraisshan/claude-code-best-practice` |
| [planning-with-files](https://github.com/othmanadi/planning-with-files) | Persistent file-based planning for long-running agent tasks that survives crashes and context reset… | 26.1k | 2026-08-09 | `clone: OthmanAdi/planning-with-files` |
| [Compound Engineering](https://github.com/everyinc/compound-engineering-plugin) | Spawns 50+ sub-agents so Claude gets smarter about your codebase over time. | 24.2k | 2026-08-08 | `plugin: EveryInc/compound-engineering-plugin` |
| [harness](https://github.com/revfactory/harness) | Meta-skill that designs domain-specific agent teams and generates the skills they use. | 8.7k | 2026-07-24 | `revfactory/harness` |
| [pro-workflow](https://github.com/rohitg00/pro-workflow) | Self-correcting memory workflow: Claude learns from your corrections, compounding over time. | 2.8k | 2026-08-03 | `rohitg00/pro-workflow` |
| [autoharness](https://github.com/tigerless-labs/autoharness) | Self-learning skill layer for Claude Code that distills skills from your own sessions. | 904 | 2026-07-28 | `tigerless-labs/autoharness` |

<!-- AG-END:frameworks -->

### Plugins & Marketplaces

Ready-made plugin packs and marketplaces you can install in one command.

<!-- AG-START:plugins -->

| Project | What it does | Stars | Updated | Install |
| --- | --- | ---: | --- | --- |
| [ui-ux-pro-max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Design-intelligence plugin that layers opinionated UI/UX guidance on top of Claude's output. | 115.3k | 2026-08-06 | `plugin: nextlevelbuilder/ui-ux-pro-max-skill` |
| [agents](https://github.com/wshobson/agents) | Multi-harness agentic plugin marketplace for Claude Code, Codex CLI, Cursor and more. | 38.7k | 2026-08-05 | `plugin: wshobson/agents` |
| [pm-skills](https://github.com/phuryn/pm-skills) | PM skills marketplace: 100+ agentic skills, commands and plugins for the whole product lifecycle. | 25.1k | 2026-07-03 | `plugin: phuryn/pm-skills` |
| [claude-skills](https://github.com/alirezarezvani/claude-skills) | 345 Claude Code skills, agents and plugins: 30+ agents, 70+ custom commands. | 24.2k | 2026-08-09 | `plugin: alirezarezvani/claude-skills` |
| [claude-code-plugins-plus-skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) | 471 plugins, 3,069 skills and 347 agents. Open-source marketplace with the ccpi CLI package manager. | 2.6k | 2026-08-10 | `ccpi` |
| [claude-code-settings](https://github.com/feiskyer/claude-code-settings) | Curated skills, sub-agents and config templates that supercharge Claude Code. | 1.6k | 2026-07-27 | `feiskyer/claude-code-settings` |
| [claude-codex-settings](https://github.com/fcakyon/claude-codex-settings) | Battle-tested Claude Code, Codex and Cursor configs, plugins, hooks and agents. | 1.0k | 2026-08-10 | `fcakyon/claude-codex-settings` |
| [claude-night-market](https://github.com/athola/claude-night-market) | 23 Claude Code plugins: TDD enforcement hooks, git/PR workflows, spec-driven development. | 327 | 2026-08-08 | `plugin: athola/claude-night-market` |
| [ultraship](https://github.com/houseofmvps/ultraship) | 39 skills, 33 tools and 11 agents for ship-ready workflows. | 115 | 2026-07-08 | `plugin: Houseofmvps/ultraship` |
| [claude-plugins](https://github.com/2389-research/claude-plugins) | 28 plugins and MCP servers: TDD, multi-agent orchestration and iteration workflows. | 90 | 2026-08-05 | `plugin: 2389-research/claude-plugins` |

<!-- AG-END:plugins -->

### Memory & Context

Give Claude Code memory across sessions and keep context windows lean.

<!-- AG-START:memory -->

| Project | What it does | Stars | Updated | Install |
| --- | --- | ---: | --- | --- |
| [claude-mem](https://github.com/thedotmack/claude-mem) | Persistent context across sessions for every agent: captures everything your agent learns. | 90.3k | 2026-08-10 | `npm: claude-mem` |
| [context-mode](https://github.com/mksglu/context-mode) | Context-window optimization: sandboxes tool output (98% reduction), persists session memory. | 19.8k | 2026-08-10 | `mksglu/context-mode` |
| [Continuous-Claude-v3](https://github.com/parcadei/continuous-claude-v3) | Context management via hooks: state kept in ledgers with clean handoffs between sessions. | 3.9k | 2026-01-26 | `parcadei/Continuous-Claude-v3` |
| [arscontexta](https://github.com/agenticnotetaking/arscontexta) | Claude Code plugin that generates individualized knowledge systems from your conversations. | 3.5k | 2026-02-24 | `plugin: agenticnotetaking/arscontexta` |
| [memsearch](https://github.com/zilliztech/memsearch) | Persistent, unified memory layer for all your AI agents — Claude Code, Codex and more. | 2.5k | 2026-07-31 | `zilliztech/memsearch` |
| [mex](https://github.com/mex-memory/mex) | Persistent project memory for AI coding agents: structured scaffold plus drift detection. | 1.4k | 2026-08-08 | `mex-memory/mex` |
| [Citadel](https://github.com/sethgammon/citadel) | Operating layer for Claude Code and Codex: persistent project memory and state. | 853 | 2026-08-10 | `SethGammon/Citadel` |
| [sidstack](https://github.com/junixlabs/sidstack) | Persistent project memory exposed through 32 MCP tools for knowledge and impact. | 1 | 2026-03-12 | `junixlabs/sidstack` |

<!-- AG-END:memory -->

### Skills & Libraries

Curated skill libraries for engineering, research, design, security and business work.

<!-- AG-START:skills -->

| Project | What it does | Stars | Updated | Install |
| --- | --- | ---: | --- | --- |
| [skills](https://github.com/mattpocock/skills) | Production engineering skills: debugging, testing, architecture and code review workflows. | 212.4k | 2026-08-07 | `mattpocock/skills` |
| [agentic-awesome-skills](https://github.com/sickn33/agentic-awesome-skills) | AAS Core: the local, agent-first control plane for complete catalog discovery. | 44.7k | 2026-08-10 | `sickn33/agentic-awesome-skills` |
| [awesome-agent-skills](https://github.com/voltagent/awesome-agent-skills) | 1,000+ agent skills from official dev teams and the community, for any agent. | 29.9k | 2026-08-10 | `VoltAgent/awesome-agent-skills` |
| [i-have-adhd](https://github.com/ayghri/i-have-adhd) | A skill that stops your coding agent from burying the answer: ADHD-friendly output. | 19.1k | 2026-08-10 | `ayghri/i-have-adhd` |
| [skills](https://github.com/browser-act/skills) | Browser automation CLI built for AI agents: breaks through anti-bot walls. | 5.3k | 2026-08-05 | `browser-act/skills` |
| [video-shotcraft](https://github.com/vincentwei1021/video-shotcraft) | AI video skill for Claude Code and Codex: cinematic product videos with Remotion. | 4.5k | 2026-08-09 | `Vincentwei1021/video-shotcraft` |
| [Generative-Media-Skills](https://github.com/samuraigpt/generative-media-skills) | Multi-modal generative media skills for Claude Code, Cursor and Gemini CLI. | 4.0k | 2026-08-08 | `SamurAIGPT/Generative-Media-Skills` |
| [ctf-skills](https://github.com/ljagiello/ctf-skills) | Agent skills for solving CTF challenges: web exploitation, binary pwn and crypto. | 3.0k | 2026-07-31 | `ljagiello/ctf-skills` |
| [vibe-coding-prompt-template](https://github.com/khazp/vibe-coding-prompt-template) | Templates and workflow for generating PRDs, tech designs and MVPs. | 2.8k | 2026-07-18 | `KhazP/vibe-coding-prompt-template` |
| [Claude-Code-Everything-You-Need-to-Know](https://github.com/wesammustafa/claude-code-everything-you-need-to-know) | A practical Claude Code guide with clear mental models and copy-paste examples. | 2.6k | 2026-07-28 | `wesammustafa/Claude-Code-Everything-You-Need-to-Know` |
| [Deep-Research-skills](https://github.com/weizhena/deep-research-skills) | Structured deep-research skill for Claude Code, Codex and others with human-in-the-loop checkpoints. | 1.9k | 2026-05-07 | `Weizhena/Deep-Research-skills` |
| [skills](https://github.com/wondelai/skills) | Wondel.ai agent skills: business, marketing, UX and coding frameworks. | 1.9k | 2026-08-10 | `wondelai/skills` |
| [engram](https://github.com/nagisanzenin/engram) | Evidence-based learning engine: first-principles curricula with frequent review. | 1.3k | 2026-08-04 | `nagisanzenin/engram` |
| [gpt-image2-ppt-skills](https://github.com/juneyaooo/gpt-image2-ppt-skills) | Clone any .pptx into your own deck: gpt-image-2 mimics the layout, you keep the story. | 1.2k | 2026-08-02 | `JuneYaooo/gpt-image2-ppt-skills` |
| [auteur](https://github.com/agiwhitelist/auteur) | The Claude Code skill that directs a website like a film: commit-sheet, scenes, cut. | 1.1k | 2026-08-06 | `agiwhitelist/auteur` |
| [claude-smart](https://github.com/reflexioai/claude-smart) | Turns your corrections into preferences, project-specific skills and shared skills. | 765 | 2026-08-08 | `ReflexioAI/claude-smart` |

<!-- AG-END:skills -->

### Agents & Orchestration

The agents themselves, multi-agent orchestration and agent team management.

<!-- AG-START:agents -->

| Project | What it does | Stars | Updated | Install |
| --- | --- | ---: | --- | --- |
| [claude-code](https://github.com/anthropics/claude-code) <sub>✅ official</sub> | Anthropic's official terminal-based coding agent. The platform everything else plugs into. | 140.9k | 2026-08-08 | `npm: @anthropic-ai/claude-code` |
| [OpenMythos](https://github.com/kyegomez/openmythos) | Theoretical reconstruction of the Claude Mythos architecture, built from first principles. | 14.8k | 2026-05-23 | `kyegomez/OpenMythos` |
| [claude-octopus](https://github.com/nyldn/claude-octopus) | Surface AI blindspots: up to 8 AI models on every research and code task before you ship. | 4.0k | 2026-08-10 | `nyldn/claude-octopus` |
| [NotFair](https://github.com/nowork-studio/notfair) | Goal-driven, loop-powered marketing agents that pursue your business goals 24/7. | 3.3k | 2026-08-09 | `nowork-studio/NotFair` |
| [babysitter](https://github.com/a5c-ai/babysitter) | Enforces obedience on agentic workforces and helps them manage execution. | 1.7k | 2026-08-10 | `a5c-ai/babysitter` |
| [hivemind](https://github.com/activeloopai/hivemind) | Turns your traces into reusable skills across agents. | 1.5k | 2026-07-30 | `activeloopai/hivemind` |
| [ai-maestro](https://github.com/23blocks-os/ai-maestro) | AI agent orchestrator with skills system: manage Claude, Codex or any agent from one dashboard. | 745 | 2026-08-07 | `23blocks-OS/ai-maestro` |
| [claude-code-agent-teams-exercises](https://github.com/panaversity/claude-code-agent-teams-exercises) | 30 practical exercises for agent teams: creation, coordination, quality hooks, parallel review. | 32 | 2026-02-11 | `panaversity/claude-code-agent-teams-exercises` |

<!-- AG-END:agents -->

### Safety, Quality & Review

Guardrails, code review and verification layers for agentic engineering.

<!-- AG-START:quality -->

| Project | What it does | Stars | Updated | Install |
| --- | --- | ---: | --- | --- |
| [agent-rules-books](https://github.com/ciembor/agent-rules-books) | AGENTS.md rules and skills for AI coding agents — Codex, Cursor and Claude Code. | 2.5k | 2026-05-22 | `ciembor/agent-rules-books` |
| [pg-aiguide](https://github.com/timescale/pg-aiguide) | MCP server and Claude plugin for Postgres skills and documentation: better SQL from AI. | 1.8k | 2026-06-26 | `timescale/pg-aiguide` |
| [cc-safety-net](https://github.com/kenryu42/cc-safety-net) | AI coding agent guardrail: a CLI hook that blocks destructive git and filesystem actions. | 1.5k | 2026-08-10 | `kenryu42/cc-safety-net` |
| [getspecstory](https://github.com/specstoryai/getspecstory) | Local-first extensions for AI IDEs and terminal agents: specs, history and insights. | 1.3k | 2026-08-10 | `specstoryai/getspecstory` |
| [brooks-lint](https://github.com/hyhmrright/brooks-lint) | AI code reviews grounded in 12 classic engineering books, with decay-risk diagnostics. | 1.3k | 2026-08-04 | `hyhmrright/brooks-lint` |
| [claude-video-vision](https://github.com/jordanrendric/claude-video-vision) | Give Claude the ability to watch and understand videos: Claude Code plugin with vision tools. | 1.2k | 2026-08-07 | `jordanrendric/claude-video-vision` |

<!-- AG-END:quality -->

### Directories & Catalogs

Where the rest of the ecosystem lives: marketplaces, mega-lists and searchable catalogs.

<!-- AG-START:catalogs -->

| Project | What it does | Stars | Updated | Install |
| --- | --- | ---: | --- | --- |
| [skills](https://github.com/anthropics/skills) <sub>✅ official</sub> | Anthropic's official skills library, showing how skills are designed and used internally. | 167.4k | 2026-08-07 | `anthropics/skills` |
| [awesome-mcp-servers](https://github.com/punkpeye/awesome-mcp-servers) | The de-facto catalog of MCP servers, for Claude Code, Cursor and any MCP client. | 92.0k | 2026-08-03 | `punkpeye/awesome-mcp-servers` |
| [servers](https://github.com/modelcontextprotocol/servers) <sub>✅ official</sub> | Official reference MCP servers from the Model Context Protocol team. | 89.4k | 2026-08-10 | `modelcontextprotocol/servers` |
| [awesome-claude-skills](https://github.com/composiohq/awesome-claude-skills) | 1,000+ skills and SaaS integrations in one install. | 72.2k | 2026-07-24 | `ComposioHQ/awesome-claude-skills` |
| [awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | The big curated collection of Claude Code patterns, hooks and commands. | 52.1k | 2026-08-10 | `hesreallyhim/awesome-claude-code` |
| [claude-plugins-official](https://github.com/anthropics/claude-plugins-official) <sub>✅ official</sub> | Anthropic's official marketplace: 200+ curated first-party and partner plugins. | 33.4k | 2026-08-10 | `auto-registered` |
| [claude-code-templates](https://github.com/davila7/claude-code-templates) | Open-source catalog and CLI behind aitmpl.com: thousands of agents, commands, skills and MCP server… | 30.2k | 2026-08-10 | `aitmpl.com` |
| [awesome-claude-plugins](https://github.com/composio-community/awesome-claude-plugins) | Curated list of production-ready plugins that extend Claude Code. | 1.9k | 2026-07-26 | `composio-community/awesome-claude-plugins` |
| [awesome-claude-plugins-metrics](https://github.com/quemsah/awesome-claude-plugins) | Automated collection of Claude Code plugin adoption metrics across GitHub repositories. | 1.2k | 2026-08-08 | `quemsah/awesome-claude-plugins` |
| [claude-plugins-community](https://github.com/anthropics/claude-plugins-community) <sub>✅ official</sub> | Anthropic's reviewed community marketplace, installed with the @claude-community suffix. | 341 | 2026-08-10 | `@claude-community` |

<!-- AG-END:catalogs -->

## Contribute

This list lives from PRs. Three ways to help:

1. **Add a tool** — open a PR following [`.github/PULL_REQUEST_TEMPLATE/add-tool.md`](.github/PULL_REQUEST_TEMPLATE/add-tool.md). A bot validates the entry and refreshes its stats automatically.
2. **Report a dead entry** — open an issue and we'll verify within days.
3. **Improve the engine** — [`awesome-guard`](src/awesome_guard) is a small, dependency-light Python package. PRs welcome.

See [CONTRIBUTING.md](CONTRIBUTING.md) for the full workflow.

## The engine

This repository is a dogfood of its own tooling. [`awesome-guard`](https://pypi.org/project/awesome-guard/)
is a pip-installable engine that:

- reads a YAML registry ([`data/entries.yml`](data/entries.yml)),
- fetches live metadata from the GitHub API (stars, license, last push, archive status),
- regenerates the README tables **and** `awesome.json` between marker blocks,
- runs daily on GitHub Actions, and can check any PR that touches the registry.

Run it locally:

```bash
pip install awesome-guard
awesome-guard check                # validate the registry schema
awesome-guard refresh              # fetch live data and regenerate README + awesome.json
```

Use it to keep *your own* awesome list fresh forever.

## Support

If this list saves you an afternoon, a star is plenty. If it saves you a week,
[GitHub Sponsors](https://github.com/sponsors/iliasaberkane6-lab) is open.

Also building automations for small businesses — spreadsheets, forms, CRMs, workflows —
[this list is one of the things they feed on](https://github.com/iliasaberkane6-lab). Questions are welcome.

## License

MIT — see [LICENSE](LICENSE). The catalog data is CC0. The engine is yours to reuse.
