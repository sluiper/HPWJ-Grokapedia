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
| 4 | Training material | **Blocked until Phase 3 freeze** | First pack: ATC-HPWJ-OP-001 |

---

## Decisions

| Date | Decision | Authority |
|------|----------|-----------|
| 28 July 2026 | Follow user order: collect → organize → truth → training last | Human direction via plan approval |
| 28 July 2026 | Public collection proceeds without waiting on INTERNAL GAPs | Default (plan) |
| 28 July 2026 | First training pack = ATC-HPWJ-OP-001 only | Default (plan) |
| 28 July 2026 | No hard-coded training constants until human freeze after Phase 3 | Process + plan |
| — | Numeric + control freeze for OP-001 authorized | **Pending human** |

---

## Human-gated intake (does not block Phase 1A / 2)

| Item | Status | Blocks |
|------|--------|--------|
| Full IMCA D049 member PDF | Waiting | Sec 23 full clause extraction only |
| Aramco SAES / CSMS HPWJ clauses | Waiting | Sec 21 client depth |
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
- [ ] Claude Verification Report
- [x] No open P0 / no AUDIT-005
- [ ] Human freeze recorded here

### Phase 4
- [ ] `training/ATC-HPWJ-OP-001/` full pack
- [ ] Cite-MCR-only verified
- [ ] Human pilot approval

---

## Defect / finding log (campaign)

| ID | Found | Severity | Status | Notes |
|----|-------|----------|--------|-------|
| (seed) AUDIT-001–004 | Pre-campaign | Closed | Closed | Metric RF constant 0.745 class; fixed |
| — | — | — | — | New findings start AUDIT-005 |

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
