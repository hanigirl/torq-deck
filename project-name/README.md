# Mobbin Researcher

An autonomous **design-inspiration researcher**. It reads your project's knowledge base,
finds the strongest real-world references on **Mobbin**, and lays them out as an inspiration
board in **FigJam** — each with a short "why it's good / what to apply" analysis.

## What's inside

```
project-name/
├── README.md                          ← this file (for humans)
├── CLAUDE.md                          ← context for Claude Code (loaded automatically)
├── agents/
│   └── mobbin-researcher.md           ← the agent prompt template — fill in the [brackets]
└── skills/
    ├── benchmark/SKILL.md             ← structured competitive-benchmarking flow
    └── competitive-analysis/SKILL.md  ← dependency the benchmark skill calls
```

## Quick start

1. **Fill in the template.** Open `agents/mobbin-researcher.md` and replace every
   `[bracketed]` placeholder:
   - `[X]` — path to your knowledge-base folder (brief, research, persona, requirements)
   - `[X]`, `[Y]`, `[Z]` — what you're looking for (the patterns/flows/screens)
   - `[FigJam board URL]` — the board where inspirations get posted
   - *(optional)* routine + trigger
2. **Connect the MCP servers** (see below).
3. **Run the agent** with that prompt. It reads the knowledge base, runs the `benchmark`
   skill, searches Mobbin, posts results into your FigJam board, and replies with a summary
   plus the board link.

## Requirements / Setup

Two MCP servers must be connected and authenticated before running. Run these in your terminal:

**Mobbin** (reference search — needs a paid Mobbin plan):
```bash
claude mcp add mobbin --scope user --transport http https://api.mobbin.com/mcp
```
Then start a new Claude Code session → pick `mobbin` → **Authenticate** → sign in via the browser.

**Figma** (writes the FigJam board) — local desktop server:
1. In the Figma desktop app: **Dev Mode** (`Shift+D`) → *MCP server* → **Enable desktop MCP server**.
2. ```bash
   claude mcp add --transport http figma-desktop http://127.0.0.1:3845/mcp
   ```
   (or remote: `claude mcp add --transport http figma https://mcp.figma.com/mcp`)

Check both with `claude mcp list`.

| MCP | Used for | Tools |
|-----|----------|-------|
| **Mobbin** | searching references | `search_screens`, `search_flows` |
| **Figma** | writing the FigJam board | `get_figjam`, `use_figma` |

## Output

- A populated **FigJam inspiration board**, grouped by theme (`[X]` / `[Y]` / `[Z]`).
- A written summary: top picks per theme, one top recommendation, and the board link.

## Credits

Benchmark skills sourced from
[Owl-Listener/designer-skills](https://github.com/Owl-Listener/designer-skills).
