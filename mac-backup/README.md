# Mac backup — Desktop HPWJ source folder

Snapshot of the local Mac folder:

`/Users/ab71000372/Desktop/nebosh/hpwj`

Copied onto branch `mac-backup` so other Groks can review the original source files without touching `main`.

- **Copied:** 2026-08-30
- **Source host:** this Mac (user `ab71000372`)
- **Branch:** `mac-backup`
- **Folder in repo:** `mac-backup/`
- **Do not merge this branch into `main`.** It is a binary dump for review, not Grokapedia content.

## What is in here

| Path | What it is |
| --- | --- |
| `*.pptx` / `*.docx` at root | Course slides, trainer scripts, Copilot/Grok/Anabeeb decks |
| `claude/` | Claude-generated 3-day pack: scripts, exam, checklists, gap analysis |
| `sabic/` | SABIC HPWJ awareness deck, MEA region doc, JSA spreadsheet |
| `WJTANLB/` | WJTA-NLB deck, WJTA1 PDF, AUTO/MAN checklists (print + fillable) |
| `WJTANLB/sabic/` | Duplicate of `sabic/` (same files, same sizes) |
| `OPS-P-019-*.doc` | High Pressure Water Jetting procedure |
| `New Catalogue (EN) Safetech UHP 04-2022 (1).pdf` | Safetech UHP catalogue |
| `scan.pdf` | Scanned document |

`claude/HPWJ3day.pptx` is a byte-for-byte duplicate of root `HPWJ3day.pptx`.

## Not copied (GitHub limits / junk)

| File | Size | Reason |
| --- | --- | --- |
| `WJTANLB/WJTA_FV4.2_UniversalDeck_Updated_04-26-24_FGR.pptx` | 1.39 GiB | GitHub rejects files over 100 MB. A 69 MB related copy is in `WJTANLB/1WJTA_FV4.2_UniversalDeck_Updated_04-26-24_FGR.pptx`. Original remains on the Mac. |
| `.DS_Store` | — | Finder metadata |
| `~$*` Office lock files | — | Word/PowerPoint temp locks |

**Video scripts** for the 16 WJTA clips inside that 1.39 GiB deck are in [`WJTANLB/video-scripts/`](WJTANLB/video-scripts/README.md). Four have spoken narration (pump inspection, hose/tool, shotgun, automated tube cleaning); the rest are visual/music demos with shot-by-shot scripts. Step-by-step **pressure-up and shutdown** (engine start → working pressure → dump → pump off) is [`WJTANLB/video-scripts/PRESSURE-UP-AND-SHUTDOWN.md`](WJTANLB/video-scripts/PRESSURE-UP-AND-SHUTDOWN.md).

If a Grok needs the 1.4 GiB Universal Deck, it is still on the Mac at the source path above. Prefer the 69 MB `1WJTA_...pptx` copy first.

## Review notes for Groks

- This is **source material**, not the Grokapedia markdown on `main`.
- Many files are binary (pptx/docx/pdf). Extract text before citing.
- Repo is **public**. Treat SABIC / Anabeeb / procedure files as client-sensitive when quoting.
- Duplicates exist on purpose — this folder mirrors the Mac tree, not a cleaned library.
