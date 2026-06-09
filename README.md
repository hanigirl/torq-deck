# The Research You Shouldn't Run Alone — UXTRA talk deck

A self-contained HTML slide deck for the talk on how agents became the research team.

## ▶︎ Live presentation

**https://hanigirl.github.io/torq-deck/torq2/**

(its own standalone link — good to send to people or run live at the conference)

## Controls

- **→ / Space / Enter** — next step / slide (or click the right half of the screen)
- **←** — back (or click the left half)
- **f** — fullscreen
- **GO #** — type a number to jump to that slide

## Run locally

```bash
python3 serve.py
# → http://localhost:8000/torq2/
```

The deck lives in [`torq2/index.html`](torq2/index.html); media is in `assets/` (lazy-loaded — only the active slide ±1 ever downloads). A `<base href="../">` lets the deck load those root assets from inside the `torq2/` folder.
