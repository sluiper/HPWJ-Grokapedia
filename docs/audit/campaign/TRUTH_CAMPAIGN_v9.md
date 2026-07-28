# Truth Campaign v9 — Broader than Arithmetic Audit

**Status:** **IN PROGRESS** — T1 substantially complete; freeze **not** authorized  
**Branch:** `draft/campaign-max-truth-training`  
**Opened:** 28 July 2026  
**Detail run log:** `T1_T3_RUN_2026-07-28.md`  
**Predecessor:** `docs/audit/TRUTH_AUDIT_v8.6.1.md` (arithmetic closed; AUDIT-001–004 closed)

---

## Track status

| Track | Focus | Status |
|-------|-------|--------|
| **T1 Arithmetic** | Derived formulas/tables | **Substantially complete — all high-risk checks PASS** |
| **T2 Citation fidelity** | Primary sources for freeze numbers | **RF formula pinned; OPS/SABIC extract fidelity = human GAP-004** |
| **T3 Consistency** | Restatement vs MCR | **Freeze-candidate set PASS on samples; full map optional** |

---

## T1 summary (28 July 2026)

| Item | Result |
|------|--------|
| MCR-017 metric k = 0.232711 → 0.233 | PASS |
| Live operational 0.745 | **None** (historical notes only) |
| Sec16 jet velocity 371/455/525/743 | PASS (≤0.3 m/s) |
| Appendix C imperial 42 cells | PASS |
| Appendix C metric 36 cells | PASS |
| Appendix C worked examples | PASS |
| Sec17 Ex1 plunger | PASS exact |
| Sec17 Ex2 plunger | Intermediate-rounding clarified (not a formula defect) |
| App A Ex2 aligned to Sec17 | Done |
| Sec20 all 17 S×L×D → RPN | PASS 17/17 |
| Sec23 seawater +2.5% @ ρ=1025 | PASS under stated assumption |
| Wright 2013 public PDF for 0.052 | Pinned in Sec16 + RP-PHYS |

---

## T2 summary

| Claim family | Primary source | Status |
|--------------|----------------|--------|
| Imperial RF 0.052 | Wright 2013 WJTA-IMCA public PDF | Pinned |
| Metric 0.233 | Derived from imperial | Pass |
| MCR-046–052 | OPS-P-019 summary in repo | **Pending human GAP-004** |
| IMCA SF 18/20 etc. | Public IMCA URLs | Verified |
| Injection clinical | StatPearls NBK542210 | Verified |

---

## T3 summary (freeze candidates)

MCR-016/017, 046, 047, 048, 050, 051, 052 — restatement samples across MCR, OPS summary, Ch11–13, App C/D/G/J, templates: **consistent**. No soft conflicts found that change operational meaning.

---

## Defect table

| ID | Location | Description | Severity | Status |
|----|----------|-------------|----------|--------|
| — | — | No new arithmetic defects this campaign | — | — |

Legacy closed: AUDIT-001–004.

---

## Safe-to-freeze checklist (ATC-HPWJ-OP-001)

| # | Criterion | Status |
|---|-----------|--------|
| 1 | T1 high-risk arithmetic PASS | **Done** |
| 2 | T3 freeze-candidate restatements clean | **Done (sample + greps)** |
| 3 | Claude Verification Report on branch | **Pending** |
| 4 | Human confirms GAP-004 (OPS extract fidelity) | **Pending human** |
| 5 | Human freeze sentence in CAMPAIGN_LOG | **Pending human** |

**Human freeze:** _Pending_

Suggested freeze sentence (when ready):

> “Numeric + control freeze for ATC-HPWJ-OP-001 is authorized against MCR-016, 017, 046–052 and the high-priority RPN set as of commit _____ on draft/campaign-max-truth-training.”

---

## Work log

| Date | Action |
|------|--------|
| 28 Jul 2026 | Campaign open; inventories; public harvest |
| 28 Jul 2026 | Wright 2013 cite; RF metric re-derive; velocity Pass |
| 28 Jul 2026 | App C 78 cells Pass; Sec20 17 RPNs Pass; Sec17 Ex2 clarified; App A aligned |
| 28 Jul 2026 | T1_T3_RUN log written |
