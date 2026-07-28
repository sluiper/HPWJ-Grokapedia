## draft/multi-ai-build-gaps – 28 July 2026

### Multi-AI documentation + gap hunt + more training
- `docs/audit/campaign/MULTI_AI_WORKING.md` — dual-model + human loop, hand-offs, standing checks.
- `docs/audit/campaign/MULTI_AI_SESSION_BOARD.md` — living queue for Grok / Claude / Human.
- `tools/audit/gap_hunter.py` — orphan MCR cites, missing Verification Logs, pack headers, unit-pair.
- Lightweight Verification Logs added to Ch5–7, 9–10, 13, Sec18, Sec20.
- AUTO endorsements: IBC + OBC; T3 scaffold; FAMILY.md pointer.
- gap_hunter clean: 0 orphan MCR, 0 missing VL, 0 unit-pair issues.


# CHANGELOG

## mac-goldmine-harvest – 28 July 2026 (multi-AI, local)

### Source materials pack (`references/source_materials/`)
- `MAC_HARVEST_2026-07-28.md` — full Mac path inventory (OPS-P-019, SABIC OMS 8.2, WJTA FV+checklists, ATC decks, TVTC pack).
- `SABIC_OMS_Att_8.2_HPWJ_Summary.md` — client mandatory KSA/MEA harvest card.
- `WJTA_Checklists_and_Deck_Inventory.md` — PPE + shotgun sequence extract + copyright note.
- `CROSS_WIKI_ARAMCO_CSM_STATUS.md` — honest result: **full Aramco CSM/CSMS not on Mac**; sibling pointers to Rigger III + scaffold CSM-II quotes.
- No MCR promotions. Binaries left on Desktop/Documents. MASTER_SOURCE_INVENTORY + campaign log updated.

## draft/full-stack-audit-build – 28 July 2026

### Full-stack audit + continued build
- `docs/audit/campaign/FULL_STACK_AUDIT_2026-07-28.md` — layers, closed audits, prioritised gaps, freeze map.
- `docs/research/inventory/SECTION_HEALTH_SHEET.md` — section inventory.
- `tools/audit/unit_pair_sweep.py` — standing T1 unit-pair automation.
- Residual unit pair: LP **3 000 psi (200 bar) → ≈207 bar** in OPS summary.
- `training/ATC-HPWJ-AUTO/` overview + **LTC 1-day endorsement** scaffold.

## draft/claude-p1-fixes – 28 July 2026 (Claude Verification F-01–F-08)

### P1
- **AUDIT-005 / F-01:** MCR-050 **680 bar → ≈ 690 bar** (derived from 10 000 psi); OPS summary aligned; GAP-004 note if OPS states independent 680 bar.
- **AUDIT-006 / F-02:** Sec20 priority list **RPN ≥ 180** + Cavitation (192); MCR front matter + §20.7 updated.
- **AUDIT-007 / F-03:** Sec16.6 Cd-consistent orifice example (≈4.97 GPM → ≈141 N); App C known-flow vs orifice cases separated.

### P2
- App C tables round-half-up (F-04); MCR-046 **≈ 2 758 bar** (F-05); Ch8 PPE ≈2 070 bar (F-06); Wright impact + compressibility caveats (F-07); Sec20 band labels (F-08).
- Standing **unit-pair T1 sweep** in PROCESS.md; pack drift check clean.

## draft/max-stack-continue – 28 July 2026 (merged PR #3)

### Max stack build (items 1–4)
- Merged PR #2 (global public stack) to main.
- Sec21 matrix expanded: AU Class A/B **bar·L/min** comparison + worked energy-product examples; competency/ops/medical rows densified.
- Deeper public harvest: OEM (Hammelmann medical PDFs, Jetstream safety manual RF language), EWJI/SIR/DIRV notes, medical OEM expansion.
- **ATC-HPWJ-UHP** Level 3 training pack (MCR-034 / App J) under `training/ATC-HPWJ-UHP/`.
- No new MCR rows; RF still cite-only via MCR-017.

## draft/max-data-web-stack – 28 July 2026 (merged PR #2)

### Global stack expansion (public web only)
- `docs/research/inventory/GLOBAL_STACK_PUBLIC_SOURCES.md` — world map of WJTA / WJA / AS-NZS / SWA / IMCA / SIR / OSHA public sources.
- Expanded `WJTA_Summary.md` (Orange Book **3rd ed. 2026**, public medical extract, coupling alert, color code, hand signals, hose whitepaper).
- Expanded `ASNZS_4233_Australia_Summary.md` + new `Safe_Work_Australia_HPWJ_Guide_Notes.md` (Class A/B **800–5600 / >5600 bar·L/min**, RTO Class B, 2-year refresh).
- Expanded `WJA_Summary.md` (Black Code + injury algorithm).
- Updated `00_Global_Standards_Overview.md` + master source inventory.
- **No new MCR rows. No formula changes.** Full paid manuals remain INTERNAL GAPs.

## draft/campaign-max-truth-training – 28 July 2026 (merged to main as PR #1)

### Slice A — Campaign scaffold
- Branch `draft/campaign-max-truth-training` opened and pushed.
- Inventories + nine RP-* package stubs; status-drift cleanup (Ch13 52→65 rows; process queues).

### Slice B — Public harvest + truth campaign start
- Pinned imperial 0.052 to **D. Wright, StoneAge, 2013 WJTA-IMCA** public PDF; metric re-derive 0.232711→0.233.
- Public harvest packages: PHYS, STD, INJ, INC, IMCA.

### Slice C — T1 complete for high-risk set + T3 freeze samples
- Appendix C: all **42 imperial + 36 metric** cells re-derived **PASS**.
- Section 20: all **17** explicit S×L×D→RPN lines **PASS**.
- Section 17 Ex2: full arithmetic shown (68.06 L/min / 11 020 psi vs rounded 68 / 11 030); Appendix A aligned.
- Section 23 seawater density factor +2.5% re-checked PASS.
- T3 freeze-candidate restatements (MCR-016/017, 046–052) consistent across MCR, OPS summary, Ch11–13, apps, templates.
- Run log: `docs/audit/campaign/T1_T3_RUN_2026-07-28.md`.
- **No AUDIT-005. No new MCR.**

### Slice D — Phase 4 ATC-HPWJ-OP-001 training pack (0.1-draft)
- Full pack under `training/ATC-HPWJ-OP-001/`: course spec, trainer guide, student workbook, 15-item practical checklist with rubrics, theory exam bank (MCR-mapped, RF via MCR-017 lookup), assessment/certificate templates, equipment & PPE list.
- Build rules enforced: cite MCR; no free-floating formula constants.
- Provisional freeze for pilot build (user directed “go”); main merge still needs human pilot approval.

### Slice E — AWARE + VOC packs; OP-001 polish; PR
- `training/ATC-HPWJ-AWARE/` — ½-day site awareness (EN/AR headings, quiz, attendance).
- `training/ATC-HPWJ-VOC/` — 1-day VOC/refresher (reassessment checklist, short theory, record).
- OP-001 **0.2-draft**: printable Exam Forms A/B + assessor answer keys; bilingual EN/AR headings on key files.
- `training/README.md` index.
- PR #1 opened: https://github.com/sluiper/HPWJ-Grokapedia/pull/1

### Slice F — ATC-HPWJ-SUP (Level 4 Supervisor)
- Full 2-day pack: `training/ATC-HPWJ-SUP/` (four Pre-Job Gates, leadership practical checklist, theory exam, assessment record).
- Based on Chapter 12 + MCR-036/041/047–052; RF still via MCR-017 only.

## v8.6.5 – 16 July 2026 (Residual Status Drift + AUDIT-004 Closed)

### Critical
- **AUDIT-004**: Section 23.6 still contained the old wrong metric reaction force constant (0.745). This is the fourth independent restatement of the same unit-conversion defect. Corrected to 0.233 with full historical note. Standing rule expanded: restatement search now explicitly covers all narrative sections, not only the three previously known locations.

### Status Sync
- Section 23 MCR mapping table + Verification Log: MCR-053–060 updated from Drafting → Visible.
- Section 27 MCR mapping table + Verification Log: MCR-061–065 updated from Drafting → Visible.
- docs/00_Encyclopedia_Structure.md already current at v8.6.4 (confirmed); Section 21 path confirmed real under references/standards/.

### Previous
- v8.6.4: Full numeric truth audit formally closed; docs/00 aligned; manufacturer summaries scanned.
- v8.6.3 / v8.6.2 / v8.6.1: Three earlier instances of the 0.745 bug fixed + housekeeping.

**This changelog prioritises truth over presentation.**
