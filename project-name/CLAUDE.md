# Project — Design Inspiration Research

This project runs an autonomous **design-inspiration researcher**: it reads our knowledge base,
benchmarks references on Mobbin, and assembles an inspiration board in FigJam.

## Structure

```
project-name/
├── CLAUDE.md                          ← you are here (loaded automatically by Claude Code)
├── README.md                          ← human-readable overview
├── agents/
│   └── mobbin-researcher.md           ← the agent prompt template (fill in the [brackets])
└── skills/
    ├── benchmark/SKILL.md             ← structured benchmarking flow
    └── competitive-analysis/SKILL.md  ← dependency used by the benchmark skill
```

## How to run

1. Open `agents/mobbin-researcher.md` and fill in every `[bracketed]` placeholder:
   - the knowledge-base folder `[X]`
   - what we're looking for: `[X]`, `[Y]`, `[Z]`
   - the `[FigJam board URL]` to post inspirations into
   - (optional) the routine / trigger
2. Run the agent with that prompt. It will read the knowledge base, run the `benchmark`
   skill, search Mobbin, and post the results into the FigJam board.

## Required MCP connections

Make sure these MCP servers are connected/authenticated **before** running the agent.

### 1. Mobbin MCP (reference search — requires a paid Mobbin plan)
Run in your terminal:
```bash
claude mcp add mobbin --scope user --transport http https://api.mobbin.com/mcp
```
Then start a new Claude Code session, pick `mobbin` from the MCP list, choose **Authenticate**,
and sign in with your Mobbin account in the browser window that opens.
Tools: `mcp__mobbin__search_screens`, `mcp__mobbin__search_flows`

### 2. Figma MCP (writes the FigJam board)
**Option A — local desktop server (recommended for FigJam writes):**
In the Figma **desktop app**: toggle **Dev Mode** (`Shift+D`) → in the inspect panel's
*MCP server* section click **Enable desktop MCP server**. Then in your terminal:
```bash
claude mcp add --transport http figma-desktop http://127.0.0.1:3845/mcp
```
> The local server only responds while the Figma desktop app is open with the MCP server enabled.

**Option B — remote server:**
```bash
claude mcp add --transport http figma https://mcp.figma.com/mcp
```
Tools: `mcp__claude_ai_Figma__get_figjam`, `mcp__claude_ai_Figma__use_figma`

Verify both are connected with `claude mcp list`.

## Skills

- `skills/benchmark/` — the main flow the agent calls.
- `skills/competitive-analysis/` — referenced by the benchmark skill; keep it alongside.

> Source of the skills: https://github.com/Owl-Listener/designer-skills
