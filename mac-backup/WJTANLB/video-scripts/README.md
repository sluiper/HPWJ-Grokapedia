# WJTA Universal Deck — video scripts

Scripts for the **16 videos embedded in** the 1.39 GiB file:

`WJTANLB/WJTA_FV4.2_UniversalDeck_Updated_04-26-24_FGR.pptx`

That file is not on GitHub (100 MB limit). These markdown files are the reviewable scripts.

**Do not merge `mac-backup` into `main`.**

## How these were made

- Videos extracted from `ppt/media/` in the PPTX (12 mp4 + 4 mov).
- Mapped to **presentation order** slide numbers via slide relationships.
- **Spoken videos** (4): transcribed with whisper.cpp `medium.en` on this Mac. Raw `.txt` / `.srt` in `raw/`.
- **Silent / music / field-noise videos** (12): no usable speech. Script = on-screen text + shot-by-shot description + instructor notes from the deck.
- Hallucinated Whisper lines on silent clips (`For more information, visit www.wjta.com`) were discarded.

## Index

| # | Slide | File | Duration | Kind | Title |
| --- | --- | --- | --- | --- | --- |
| 01 | 2 | [01-slide-002-good-vs-bad.md](01-slide-002-good-vs-bad.md) | 4:50 | visual+music | Good vs bad field footage (Frank G montage) |
| 02 | 27 | [02-slide-027-pump-animation.md](02-slide-027-pump-animation.md) | 1:21 | silent-animation | Uraca triplex plunger-pump animation |
| 03 | 29 | [03-slide-029-pump-inspection.md](03-slide-029-pump-inspection.md) | 4:48 | spoken | Pre-operation pump inspection (2024 generic) |
| 04 | 37 | [04-slide-037-hose-and-tool-inspection.md](04-slide-037-hose-and-tool-inspection.md) | 10:11 | spoken | Hose and tool inspection (2024 generic) |
| 05 | 54 | [05-slide-054-failed-steel-whip-check.md](05-slide-054-failed-steel-whip-check.md) | 0:04 | silent-demo | Failed steel whip-check (20 mm test) |
| 06 | 54 | [06-slide-054-nylon-whip-check.md](06-slide-054-nylon-whip-check.md) | 0:07 | silent-demo | Yellow nylon whip-check restraining hose motion |
| 07 | 64 | [07-slide-064-shotgun-vs-ppe.md](07-slide-064-shotgun-vs-ppe.md) | 0:17 | silent-demo | Shotgun vs PPE — cutting power of water |
| 08 | 67 | [08-slide-067-tst-ce-garment-test.md](08-slide-067-tst-ce-garment-test.md) | 2:10 | visual+music | TST CE certification verification test 2022 |
| 09 | 72 | [09-slide-072-manual-shotgun-training.md](09-slide-072-manual-shotgun-training.md) | 7:41 | spoken | Manual shotgun / surface-prep training (2024 generic) |
| 10 | 76 | [10-slide-076-nlb-shroud-burst.md](10-slide-076-nlb-shroud-burst.md) | 0:15 | silent-demo | NLB shroud burst test |
| 11 | 112 | [11-slide-112-whats-wrong-tube-cleaning.md](11-slide-112-whats-wrong-tube-cleaning.md) | 0:26 | field-clip | Tube cleaning — “what’s wrong here?” (air preheater, 5 hose, no AWD) |
| 12 | 127 | [12-slide-127-bjv-centralizer.md](12-slide-127-bjv-centralizer.md) | 0:11 | silent-animation | BJV / StoneAge centralizer in pipe (line mole) |
| 13 | 135 | [13-slide-135-reversal-no-stinger.md](13-slide-135-reversal-no-stinger.md) | 0:05 | silent-animation | Anti-reversal FAIL — no stinger (tool turns around in the pipe) |
| 14 | 135 | [14-slide-135-reversal-with-stinger.md](14-slide-135-reversal-with-stinger.md) | 0:04 | silent-animation | Anti-reversal PASS — stinger / ARD keeps the tool from turning around |
| 15 | 136 | [15-slide-136-smash-plate.md](15-slide-136-smash-plate.md) | 0:13 | silent-demo | Smash plate / anti-withdrawal on pipe end (trash-can AWD) |
| 16 | 163 | [16-slide-163-automated-tube-cleaning.md](16-slide-163-automated-tube-cleaning.md) | 7:36 | spoken | Automated exchanger tube-cleaning setup (2024 AE generic) |

## The four talking videos (use these as procedures)

These are the only clips with a real spoken script:

1. [03 — Pump inspection](03-slide-029-pump-inspection.md) — 4:48
2. [04 — Hose and tool inspection](04-slide-037-hose-and-tool-inspection.md) — 10:11
3. [09 — Manual shotgun](09-slide-072-manual-shotgun-training.md) — 7:41
4. [16 — Automated tube cleaning](16-slide-163-automated-tube-cleaning.md) — 7:36

Together ~30 minutes of WJTA 2024 “generic” narration.

## Deck bugs worth knowing while you review

- Slide **72** and slide **163** speaker notes are a copy-paste of the **adapters/fittings** notes (NPT / MP). They do not match the videos.
- Slide 27 (animation) and slide 29 (inspection) share the same pump-function notes.

## Raw transcripts

Spoken-video Whisper output:

- [raw/media3.txt](raw/media3.txt) / [raw/media3.srt](raw/media3.srt)
- [raw/media4.txt](raw/media4.txt) / [raw/media4.srt](raw/media4.srt)
- [raw/media9.txt](raw/media9.txt) / [raw/media9.srt](raw/media9.srt)
- [raw/media16.txt](raw/media16.txt) / [raw/media16.srt](raw/media16.srt)
