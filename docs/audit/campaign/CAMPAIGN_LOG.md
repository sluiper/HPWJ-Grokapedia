# Campaign Log — Max Data → Organize → Max Truth → Training

**Branch:** `draft/campaign-max-truth-training`  
**Opened:** 28 July 2026  
**Owner:** Grok (draft) + Human (gate) + Claude (verify when packages ready)  
**Governing process:** AGENTS.md / WORKFLOW.md / PROCESS.md  

---

## Campaign sequence (locked)

| Phase | Name | Status | Notes |
|-------|------|--------|-------|
| 0 | Setup / scaffold | **Done (branch)** | Log + inventory dirs + research package stubs |
| 1 | Max data collection | **Strong progress** | Inventories + 9 RP stubs + PUBLIC_HARVEST for PHYS/STD/INJ/INC/IMCA |
| 2 | Organize data | **Partial** | Restatement map + drift cleanup; inventories updated with public URLs |
| 3 | Max truth | **Near freeze** | T1 high-risk PASS; T3 freeze-set PASS; need Claude + human freeze |
| 4 | Training material | **In progress** | ATC-HPWJ-OP-001 pack under `training/` (provisional freeze) |

---

## Mac gold-mine harvest (28 July 2026) — multi-AI parallel with Rigging + Scaffolding

**Human ask:** Search Mac for ref docs; summarise into each wiki; document what was done; review Aramco CSM as example.

| Result | Detail |
|--------|--------|
| HPWJ binaries mapped | OPS-P-019 (3 paths), SABIC OMS 8.2, WJTA FV4.2 + 8 checklists, ATC decks, Course Overview 9-day, Safetech UHP catalogue |
| Aramco CSM/CSMS primary | **Not found on Mac** — GAP-002 remains; status card written |
| Deliverables | `references/source_materials/*` (README + 4 markdown harvest files) |
| MCR | No promotions from harvest |

---

## Decisions

| Date | Decision | Authority |
|------|----------|-----------|
| 28 July 2026 | Follow user order: collect → organize → truth → training last | Human direction via plan approval |
| 28 July 2026 | Public collection proceeds without waiting on INTERNAL GAPs | Default (plan) |
| 28 July 2026 | First training pack = ATC-HPWJ-OP-001 only | Default (plan) |
| 28 July 2026 | No hard-coded training constants until human freeze after Phase 3 | Process + plan |
| 28 July 2026 | User directed **“go”** after T1 near-freeze report → proceed Phase 4 OP-001 pack on draft branch; freeze treated as **provisional for pilot pack build** (Claude formal report still welcome) | Human direction in session |

---

## Human-gated intake (does not block Phase 1A / 2)

| Item | Status | Blocks |
|------|--------|--------|
| Full IMCA D049 member PDF | Waiting | Sec 23 full clause extraction only |
| Aramco SAES / CSMS HPWJ clauses | Waiting (Mac crawl 28 Jul: **not on disk**) | Sec 21 client depth |
| OPS-P-019 full controlled original (if summary incomplete) | Waiting | Any MCR wording change on 046–052 |
| Real anonymised Anabeeb incidents | Waiting | Sec 27 volume |
| Existing ATC course materials / exam banks | Waiting | Phase 4 efficiency |
| Practical-station equipment list / site photos | Waiting | Phase 4 realism |

---

## Phase exit checklist

### Phase 0
- [x] Draft branch created
- [x] `docs/research/inventory/` + `docs/research/packages/RP-*/` + `docs/audit/campaign/`
- [x] CAMPAIGN_LOG.md opened
- [ ] Self-check after first push

### Phase 1
- [x] MASTER_SOURCE_INVENTORY.md populated from existing repo + public harvest plan
- [x] INTERNAL_GAP_REGISTER.md
- [x] ≥8 research package stubs with SOURCE_INVENTORY (9 packages)
- [x] No unauthorized Visible MCR promotions
- [ ] Deeper public web harvest into RP-PHYS / RP-STD / RP-INJ (next slice)

### Phase 2
- [x] MCR_RESTATEMENT_MAP stub (numeric / absolute rules)
- [x] Status drift fixes (Ch13 “52 rows”, process queue, campaign pointers)
- [x] Appendix E letter reserved or explained
- [ ] Section health sheet (optional, later)

### Phase 3
- [x] TRUTH_CAMPAIGN_v9.md (in progress / near freeze)
- [x] T1 high-risk arithmetic (App C, Sec16/17/20/23 RF class) — see T1_T3_RUN_2026-07-28.md
- [x] T3 freeze-candidate restatement samples
- [x] Claude Verification Report — `CLAUDE_VERIFICATION_REPORT_2026-07-28.md` (no P0; P1s F-01–F-03)
- [x] Grok applied F-01–F-08 on `draft/claude-p1-fixes` — see `GROK_RESPONSE_CLAUDE_F_FINDINGS.md`
- [x] Standing T1 unit-pair sweep adopted
- [ ] Human freeze recorded here (GAP-004 still open for independent OPS bar wording)

### Phase 4
- [x] `training/ATC-HPWJ-OP-001/` full pack (0.1-draft)
- [x] Cite-MCR-only design (RF via MCR-017; thresholds by MCR-ID)
- [x] Pack drift check — `PACK_DRIFT_CHECK_2026-07-28.md` (clean)
- [ ] Human pilot approval

---

## Defect / finding log (campaign)

| ID | Found | Severity | Status | Notes |
|----|-------|----------|--------|-------|
| (seed) AUDIT-001–004 | Pre-campaign | Closed | Closed | Metric RF constant 0.745 class; fixed |
| AUDIT-005 / F-01 | Claude 28 Jul | P1 | Fixed (conversion) | MCR-050 680→≈690 bar derived; GAP-004 if OPS independent |
| AUDIT-006 / F-02 | Claude 28 Jul | P1 | Fixed | Sec20 list ≥180 + Cavitation 192 |
| AUDIT-007 / F-03 | Claude 28 Jul | P1 | Fixed | Sec16.6 Cd-consistent work |
| F-04–F-08 | Claude 28 Jul | P2 | Fixed | Tables, 2758 bar, Ch8, caveats, labels |

---

## Session notes

### 28 July 2026 — Slice A start
- Plan approved; branch `draft/campaign-max-truth-training` cut from main.
- Scaffold + inventories + package stubs created from **existing on-disk sources** first (max collection baseline), then expand public harvest.
- Training directory intentionally **not** populated with pack content until Phase 3 freeze.

### 28 July 2026 — Push + public harvest + T1
- Pushed branch to `origin/draft/campaign-max-truth-training`.
- Public harvest: Wright 2013 RF Eq.1 PDF; WJTA FT/FV; WJA Black Code + medical algorithm URL; StatPearls NBK542210; IMCA SF URL table expanded.
- T1: metric k re-derived **0.232711 → 0.233**; no live operational `0.745`.
- No MCR changes; freeze still pending human.

### 28 July 2026 — Full T1 high-risk + T3 freeze-set
- App C: **78/78** table cells PASS; worked examples PASS.
- Sec20: **17/17** RPN multiplications PASS.
- Sec17 Ex2 intermediate-rounding clarified; App A aligned.
- Sec23 seawater +2.5% PASS under stated assumption.
- Freeze-candidate MCR restatements (046–052, 016/017) consistent.
- **Ready for Claude review + human freeze** before OP-001 training pack.

### 28 July 2026 — Phase 4 OP-001 pack (user “go”)
- Provisional freeze for pilot pack build.
- Created full `training/ATC-HPWJ-OP-001/` pack: README, course spec, trainer guide, workbook, practical checklist, exam bank, assessment/cert, equipment list.
- Hard rules: no free-floating RF constants; cite MCR-017 / MCR rows.
- Pilot approval + optional Claude pack review still open before main merge.

### 28 July 2026 — AWARE + VOC + OP-001 polish + PR
- User directed “1-3 go”: AWARE pack, VOC pack, OP-001 Forms A/B + AR headings, open PR.
- OP-001 → 0.2-draft; training/README index.
- PR: https://github.com/sluiper/HPWJ-Grokapedia/pull/1

### 28 July 2026 — SUP pack (user “go”)
- Built `training/ATC-HPWJ-SUP/` Level 4 two-day pack (Ch12 four gates).
- PR #1 updated via push; still do not merge until human pilot/freeze approval.

### 28 July 2026 — MERGED TO MAIN
- Human directed **“merge”**.
- PR #1 merged: https://github.com/sluiper/HPWJ-Grokapedia/pull/1  
- Merge commit on main: `afdcbc3`  
- Training freeze treated as **authorized for pilot use on main** by human merge decision.

### 28 July 2026 — Full stack audit + keep building
- PR #3 (UHP/Sec21) + PR #4 (Claude F-fixes) merged to main.
- Full-stack audit written; unit-pair sweep tool; section health sheet.
- AUTO/LTC training scaffold; residual LP bar pair fixed.
- Top human gap remains **GAP-004** (controlled OPS-P-019).

### 28 July 2026 — Multi-AI docs + gap hunt + IBC/OBC
- PR #5 merged. Multi-AI working protocol + session board.
- gap_hunter.py; Verification Logs on 8 chapters; IBC/OBC + T3 scaffold.
- gap_hunter clean: 0 orphan MCR, 0 missing VL on docs/*, 0 unit-pair issues.
