# The Research You Shouldn't Run Alone — UXTRA talk deck

A self-contained HTML slide deck for the talk on how agents became the research team.

## ▶︎ Live presentation

**https://hanigirl.github.io/torq-deck/torq2/**

(its own standalone link — good to send to people or run live at the conference)

**Short version:** https://hanigirl.github.io/torq-deck/torq-short/ — 6 slides (evolution, agent traits, all tips on one slide, tomorrow morning, Design to Code workshop CTA), on phones it becomes one long page you scroll down (each slide's steps play as it comes into view). Safari gets HEVC-with-alpha copies of the transparent videos (`*-hevc.mov`), since it can't draw WebM transparency. Lives in [`torq-short/index.html`](torq-short/index.html).

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
