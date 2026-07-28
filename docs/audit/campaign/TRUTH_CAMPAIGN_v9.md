# Truth Campaign v9 — Broader than Arithmetic Audit

**Status:** **IN PROGRESS** (Phase 3 started 28 July 2026)  
**Branch:** `draft/campaign-max-truth-training`  
**Opened:** 28 July 2026  
**Predecessor:** `docs/audit/TRUTH_AUDIT_v8.6.1.md` (arithmetic **closed**; AUDIT-001–004 closed)

---

## Scope

| Track | Focus | Method | Status |
|-------|-------|--------|--------|
| **T1 Arithmetic** | Derived formulas/tables | Independent re-derivation + restatement search | **Partial — RF constant class Pass** |
| **T2 Citation fidelity** | High-priority MCR + Never Rules + OPS numbers | Source exists? Matches? | **Partial — RF formula primary cite pinned** |
| **T3 Consistency** | Same rule, different wording | Diff vs MCR; use `MCR_RESTATEMENT_MAP.md` | Pending deep wording pass |

---

## T1 results (28 July 2026)

### MCR-017 metric constant

| Step | Result |
|------|--------|
| Re-derive from imperial 0.052 with exact unit factors | **k = 0.232711** → operational **0.233** |
| Match Sec16 shown derivation | Pass |
| Repo grep live operational `0.745` (excluding historical notes) | **Zero live uses** — only CHANGELOG/audit/history |
| Live `0.233` present at canonical + App C + template + Sec16 + Sec23 | Pass |

**Primary public citation for imperial 0.052:**  
D. Wright (StoneAge), *Impact Force of High Pressure Waterjets*, 2013 WJTA-IMCA Conference, Equation 1 — public PDF  
https://www.wjta.org/images/wjta/Proceedings/Papers/2013/C1%20-%20DW%20Impact.pdf  
See `docs/research/packages/RP-PHYS/PUBLIC_HARVEST.md`.

### Jet velocity table (ideal √(2P/ρ), ρ=1000 kg/m³, Cd=1)

| psi | Claimed (Sec16) | Re-derived | Delta |
|-----|-----------------|------------|-------|
| 10 000 | 371 m/s | 371.3 | 0.3 |
| 15 000 | 455 m/s | 454.8 | 0.2 |
| 20 000 | 525 m/s | 525.2 | 0.2 |
| 40 000 | 743 m/s | 742.7 | 0.3 |

**T1 Pass** (rounding only).

### RF worked example consistency

6 GPM @ 15 000 psi → Fr ≈ 38.2 lbf ≈ 170 N (imperial path).  
Metric path 0.233 × Q_L/min × √P_bar → ≈ 170.2 N. **Pass** (paths agree within 0.2 N).

### Still open on T1

- [ ] Appendix C every table cell full re-spot-check
- [ ] Sec17 plunger-change examples
- [ ] Sec20 all RPN multiplications
- [ ] Sec23 seawater density / underwater RF narrative numbers

---

## T2 results (28 July 2026)

| Claim family | Primary source now | Status |
|--------------|-------------------|--------|
| Imperial RF 0.052 | Wright 2013 public PDF | **Pinned** |
| Metric 0.233 | Derived from imperial | Pass |
| MCR-046–052 Anabeeb absolutes | OPS-P-019 summary in repo | Pending human GAP-004 fidelity check |
| IMCA SF 18/20 lessons | Public IMCA page | URL verified; maps MCR-057 |
| Injection injury clinical | StatPearls NBK542210 | URL verified — training caution logged |
| WJTA FT/FV structure | WJTA public pages | Verified for training design only |

---

## T3 results (sample — freeze candidates)

| Control | Sample files checked | Result |
|---------|---------------------|--------|
| MCR-050 (10k / 1.6 mm / 250 N) | MCR, OPS summary, Ch12, Ch13 | **Consistent** |
| MCR-047 (team of 3) | MCR, OPS summary, Ch13 | **Consistent** |
| MCR-051 (10 m unauthorised) | MCR, App D, App G, Ch13, Ch5 bands | **Consistent** (bands vs absolute rule correctly distinguished) |
| MCR-017 constant | Canonical + App C + template + Sec16 + Sec23 | **0.233 live; 0.745 historical only** |

Full prose wording-diff across all chapters still open; freeze-candidate set looks clean on samples.

Restatement map: `docs/research/inventory/MCR_RESTATEMENT_MAP.md`.

---

## Defect table (new findings start at AUDIT-005)

| ID | Location | Description | Severity | Status |
|----|----------|-------------|----------|--------|
| — | — | No new arithmetic defects found in RF class re-check | — | — |

Legacy closed: AUDIT-001–004 (metric RF 0.745 class).

---

## Safe-to-freeze statement (training)

> Numeric + control freeze for ATC-HPWJ-OP-001 is **not** authorized until:
> 1. T1–T3 complete for freeze-candidate MCR set (016, 017, 046–052, high-priority RPN set, hose life MCR-001–004 as used in OP-001)
> 2. Claude Verification Report on this branch
> 3. Explicit human sign-off in `CAMPAIGN_LOG.md`
> 4. Recommended: human confirms GAP-004 (OPS-P-019 extract = controlled copy for 046–052)

**Human freeze:** _Pending_

---

## Work log

| Date | Action |
|------|--------|
| 28 Jul 2026 | Stub created; restatement map populated for high-risk IDs |
| 28 Jul 2026 | Public harvest: Wright 2013, WJTA FT/FV, WJA Black Code, IMCA SF URLs, StatPearls |
| 28 Jul 2026 | T1 RF metric re-derive Pass; 0.745 live-use Pass |
| 28 Jul 2026 | T1 jet velocity table Pass; RF imperial/metric worked example Pass |
| 28 Jul 2026 | T3 sample pass on MCR-047/050/051/017 freeze candidates |
