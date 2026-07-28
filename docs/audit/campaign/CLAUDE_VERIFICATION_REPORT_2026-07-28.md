# Claude Verification Report — Phase 3 Truth Freeze (Campaign v9)

**Branch reviewed:** `draft/campaign-max-truth-training`
**Commit pinned:** `8b0e787edba545e1c8086cc25af988a0cfd45789` ("v9 training: ATC-HPWJ-SUP Level 4 Supervisor pack")
**Date:** 28 July 2026
**Reviewer:** Claude (independent — no drafting, no push)
**Scope:** T1 arithmetic, T2 citation fidelity, T3 MCR restatement consistency, MCR/CHANGELOG consistency, format compliance. Training packs checked only for constant drift; a full pack review is a separate item.

**Method note:** every number below was recomputed from first principles in Python from the source constants, not read from `T1_T3_RUN_2026-07-28.md`. The run log was read only afterwards, to compare conclusions.

**Branch was live during review.** Commits `9154cfc`, `44667b5` and `8b0e787` landed while this review was in progress, and the branch advanced to `b734dbe` before this report was filed. All findings are stated against the pinned commit above, and every quoted line was re-confirmed against the working tree at `b734dbe` — none of the findings was affected.

---

### 1. Numbers re-derived

#### Appendix C — imperial table, `Fr(lbf) = 0.052 × Q × √P`

| Check | Result |
|-------|--------|
| 42 lbf cells reproduce the formula | **Pass** — max deviation 0.067 lbf |
| 42 N cells reproduce `lbf × 4.448221615` | **Pass** — max deviation 0.64 N |
| Cells correctly rounded (round-half-up) | **7 of 84 are not** — see F-04 |

#### Appendix C — metric table, `Fr(N) = 0.233 × Q × √P(bar)`

| Check | Result |
|-------|--------|
| 36 cells reproduce the formula | **Pass** — max deviation 1.04 N |
| Cells correctly rounded | **7 of 36 are not** — see F-04 |

#### Metric constant (MCR-017)

`0.052 ÷ 3.785411784 ÷ √0.0689475729 × 4.448221615 = 0.2327110…` → **0.233**. **Pass.** Independently reproduces the run log's `0.232711`.

#### Section 16

| Claim | Recomputed | Result |
|-------|-----------|--------|
| 10 000 psi → 371 m/s | 371.34 | Pass |
| 15 000 psi → 455 m/s | 454.80 | Pass |
| 20 000 psi → 525 m/s | 525.16 | Pass |
| 40 000 psi → 743 m/s | 742.68 | Pass |
| Cross-check 44.721 × √68.95 | 371.35 | Pass |
| §16.5 Re ≈ 66 800 (1" hose, 80 L/min) | v = 2.6314 m/s, Re = 66 837 | Pass |
| §16.11 ΔV/V ≈ 12.5 % at 40 000 psi | 275.79 MPa ÷ 2 200 MPa = 12.54 % | Pass as a linear approximation — see F-06 |
| §16.6 worked example 0.040" @ 15 000 psi → 6 GPM | **Does not reproduce** | **Fail — F-03** |

#### Section 17 / Appendix A — plunger sizing

| Example | Recomputed | Result |
|---------|-----------|--------|
| Ex1: 80 × (12/15)² | 51.2 L/min exactly | Pass |
| Ex1: 10 000 × (80/51.2) | 15 625 psi exactly | Pass |
| Ex2: 50 × (14/12)² | 68.0556 L/min | Pass |
| Ex2: 15 000 × 50/68.0556 | 11 020.4 psi | Pass |
| Ex2 rounded path: 15 000 × 50/68 | 11 029.4 psi | Pass — both paths shown in Sec 17 and App A, correctly labelled as intermediate rounding |

#### Section 20 — FMEA

All 17 explicit `S × L × D` lines recomputed: **17/17 products equal the stated RPN.** Confirms the run log.

#### Section 23 — marine

| Claim | Recomputed | Result |
|-------|-----------|--------|
| ρ_sw/ρ_fw = 1025/1000 = 1.025 → +2.5 % | Exact | Pass under the stated positive-displacement, constant-Q assumption (assumption is stated in §23.6) |
| 250 bar @ 5 GPM ≈ 70 N | 18.927 L/min × 0.233 × √250 = 69.73 N | Pass |

#### Templates

| Claim | Recomputed | Result |
|-------|-----------|--------|
| RF card: 12 GPM @ 15 000 psi ≈ 76 lbf ≈ 340 N | 76.42 lbf / 340.0 N | Pass |
| App C: 250 N ≈ 56 lbf | 56.20 lbf | Pass |

---

### 2. Citations checked

| Source | Exists? | Matches claim? | Flags |
|--------|---------|----------------|-------|
| D. Wright (StoneAge), *Impact Force of High Pressure Waterjets*, 2013 WJTA-IMCA, Eq. 1 — public PDF at the URL cited in §16.6 | **Yes — retrieved and read in full** | **Yes.** Paper text: "Force (pounds) = .052 x Pressure (psi)^1/2 x Flow (gpm)" and "This is the same equation used to calculate the reaction force produced by a waterjet." | The paper also states measured **impact** force at 50× orifice diameter was **20–35 % greater** than Eq. 1. §16.8 equates impact and reaction force without that caveat — see F-07 |
| Metric 0.233 | Derived, not cited | Derivation reproduces | Pass |
| MCR-046–052 → OPS-P-019 | Repo summary only | Cannot verify against controlled original | **GAP-004 remains open and is now load-bearing** — see F-01, F-02 |
| IMCA SF 18/20, D049; StatPearls NBK542210; NIOSH CA/FACE 16CA001 | URLs/IDs present in repo inventories | Not independently retrieved this run | Out of scope for the numeric freeze; flagged as not-verified rather than verified |

---

### 3. MCR consistency

- Every `MCR-nnn` cited anywhere in the repo exists in `MASTER_CONTROL_REGISTER.md`: **Y** — 65 IDs defined, 65 distinct IDs cited, **zero dangling references, zero orphan rows**.
- Status of rows correct: **Y** — all 65 rows are `Visible`; **zero `Drafting` rows**. This campaign created no new MCR rows and performed no Drafting → Visible promotion, consistent with the Phase 1 exit criterion.
- Legacy `0.745`: **zero live operational uses.** All 21 occurrences are historical notes, audit records, changelog entries or restatement-search tokens. Confirms the run log.
- Freeze-candidate restatement sweep (MCR-047, 048, 051, 052) across MCR, OPS summary, Ch 11–13, App D/G/J, templates and all four training packs: **consistent, no drift.**
- **MCR-046 and MCR-050 are not clean** — see F-01 and F-02.

---

### 4. CHANGELOG consistency

**Y.** Slices A–F are present and each maps to a real commit; every file claimed in Slice D, E and F exists on disk and is tracked (`training/README.md`, Forms A/B, answer keys, AWARE, VOC, SUP). `CAMPAIGN_LOG.md` session notes match the commit history. No claimed-but-absent files found — Grok's self-check under AGENTS rule 10 holds for this branch.

---

### 5. Format compliance

**Y with notes.** Sections 16, 17, 20, 23 and the appendices carry MCR mapping, worked examples with derivation, Verification Logs and honest-gap statements. Land-vs-wet is called out in §23. Self-grading language was not found in the campaign documents.

Notes:

- §20's risk-band **labels** do not follow §20's own legend (see F-05).
- §16.6's worked example carries a Verification Log entry marked "Corrected & Verified" for a derivation that does not reproduce (F-03). A Verification Log entry that asserts a status the work does not support is the failure mode this process exists to catch.

---

### 6. Remaining gaps

- **GAP-004 (OPS-P-019 controlled original)** — now the single highest-value open gap. F-01 and F-02 are both unit-conversion discrepancies inside the MCR-046–052 block, and neither can be closed without the controlled document.
- GAP-001, 002, 003, 005–010 remain open; none blocks a land-based numeric freeze.
- §16.11 UHP compressibility correction factors remain flagged as requiring specialist data — honest and appropriately caveated.
- §16.14 70–85 % efficiency is correctly presented as a typical range, not a constant.

---

### 7. Required fixes

#### P0 (blocks merge)

**None.** No error was found that changes an operational decision, and no rounding or conversion discrepancy moves any value across the 250 N handheld threshold (checked explicitly across all 78 Appendix C cells: zero threshold crossings).

#### P1 (must fix before any Drafting → Visible promotion, and before MCR-046/050 are frozen)

**F-01 — MCR-050 states two pressure limits that disagree (AUDIT-005).**
`MCR-050` and the OPS-P-019 summary both render the shotgunning limit as **"10 000 psi (680 bar)"**. 10 000 psi = **689.5 bar**. The same 10 000 psi threshold is rendered **"≈690 bar"** in `docs/03` and `docs/05`. So the register and two chapters disagree by 9.5 bar (1.4 %) on the same limit.
- Direction: 680 bar is *stricter* than 10 000 psi, so no operator is endangered by following it.
- But an operator working in bar and an operator working in psi are being given different limits by the SSOT.
- Cannot be fixed by arithmetic alone: if the controlled OPS-P-019 genuinely says 680 bar, the MCR should state that explicitly as a source-stated value rather than presenting it as an equivalence. **Human + GAP-004 required.**
- Files: `MASTER_CONTROL_REGISTER.md:81`, `references/standards/Anabeeb_OPS-P-019_HPWJ_Procedure_Summary.md:132`.

**F-02 — Section 20 top-priority lists contradict their own stated criterion (AUDIT-006).**
Both list headers state **"RPN > 180"**, then list five modes at 210, 200, 200, 180, 180 — two of which are not `> 180` — while **omitting Cavitation Damage at RPN 192**, which ranks **4th of 17** by RPN.
- Verified ranking: 210, 200, 200, **192**, 180, 180, 180 (candidate), 175, 168, 160, 160, 135, 128, 126, 120, 108, 90.
- Consequence: the section states these five "represent the greatest potential for serious injury or fatality", which its own scoring does not support. §20.7 repeats the same list. This list is what feeds training emphasis.
- Fix is editorial and needs a decision: either change the criterion to `≥ 180` and add Cavitation, or re-score Cavitation. Not a Claude call.
- Files: `docs/20_Failure_Modes_and_Effects_Analysis.md:37-45`, `:687-693`.

**F-03 — Section 16.6 worked example does not reproduce from its own stated inputs (AUDIT-007).**
§16.6 states: *"Using Cd ≈ 0.85 and correct area gives flow in the range ≈ 5–6 GPM"*, then uses 6 GPM to obtain **38.2 lbf ≈ 170 N**.
Recomputed: d = 1.016 mm → A = 8.1073×10⁻⁷ m²; v = 454.8 m/s at 15 000 psi.

| Cd | Q | Fr |
|----|---|-----|
| 0.80 | 4.68 GPM | 132.5 N |
| 0.85 | **4.97 GPM** | 140.7 N |
| 0.90 | 5.26 GPM | 149.0 N |

- The stated Cd 0.85 gives **4.97 GPM, not 5–6**. The 6 GPM actually used implies **Cd ≈ 1.03**, which is physically impossible for an orifice.
- The Verification Log cites "Cd 0.8–0.9", which yields **4.68–5.26 GPM** — the "5–6 GPM" range is not supported by either figure.
- The resulting 170 N is **conservative** (~20 % high vs the Cd-consistent 142 N), so it is safe to act on. But AGENTS rule 2 requires the shown work to produce the stated number, and here it does not.
- Propagates to `Appendix_C:84`. The 6 GPM / 15 000 psi *table cell* itself is arithmetically correct — only the orifice-to-flow step is unsupported.
- Files: `docs/16_Physics_and_Hydraulics.md:135-138`, `:279`; `docs/appendices/Appendix_C_Reaction_Force_Quick_Calculator.md:84`.

#### P2 (nice to have)

**F-04 — 14 Appendix C cells are not correctly rounded.** All reproduce the formula within the run log's stated ±0.15 lbf / ±1.5 N tolerance, so the run log's PASS is true as stated; but under round-half-up they are wrong in the last digit, all truncated downward (non-conservative direction, max 1.04 N):
- Imperial lbf: Q3@20k (22.0→22.1), Q5@20k (36.7→36.8), Q8@30k (72.0→72.1), Q10@30k (90.0→90.1)
- Imperial N: Q5@20k (163→164), Q8@30k (320→321), Q10@30k (400→401)
- Metric N: Q15@1000 (110→111), Q23@700 (141→142), Q23@2000 (239→240), Q30@700 (184→185), Q30@1000 (220→221), Q30@2000 (312→313), Q30@2750 (366→367)
- **Zero cells change side of the 250 N threshold.** Recommend regenerating both tables programmatically and stating the rounding convention.

**F-05 — MCR-046 bar conversion uses an inconsistent factor.** "40 000 psi (2 759 bar)" implies 1 bar = 14.5 psi. Using the repo's own constant from §16.2 (1 bar = 14.5038 psi), 40 000 psi = **2 757.9 bar → 2 758**. Appears in 5 files (`MASTER_CONTROL_REGISTER.md:77`, OPS summary ×2, `MCR_RESTATEMENT_MAP.md:69`, `Appendix_G:16`). Operationally trivial (16 psi) but it is the absolute ceiling row in the SSOT.

**F-06 — Section 08 PPE band parenthetical is wrong.** "Up to 30 000 psi (≈2000–3000 bar)" — 30 000 psi = **2 068 bar**. The stated range extends to 3 000 bar = 43 500 psi, which is above the MCR-046 absolute ceiling. A reader working in bar could take 20/30 PPE as rated to 3 000 bar. Recommend "≈2 070 bar". File: `docs/08_...:182`.

**F-07 — §16.11 and §16.8 caveats.** (a) 12.5 % compressibility is the linear ΔP/K result; real water stiffens under pressure, so this overstates the true value — the section flags this as "partially verified" but the inline number carries no caveat. (b) §16.8 equates impact force and reaction force; the Wright paper explicitly measured impact at **20–35 % greater** than Eq. 1. Worth one sentence in §16.8.

**F-08 — §20 risk-band labels don't follow §20's legend.** Legend: <100 monitor, 100–150 review, >150 high priority. Actual labels: RPN 108, 120, 128 tagged "(High)"; RPN 126 tagged "(Medium-High)"; RPN 90 tagged "(Medium-High)". Cosmetic, but the FMEA is a training input.

---

### Process observation (not a defect)

T3 verified restatements **against each other** and found them consistent. F-01 and F-05 are cases where a value is consistently restated and consistently wrong — cross-restatement checking cannot detect this by construction. A unit-conversion sweep (recompute every `X unit (Y unit)` pair against the repo's stated conversion constants) catches a different failure class than the restatement search, and is what surfaced both. Recommend adding it as a standing T1 sub-check.

---

### Overall recommendation

**No P0. Partial freeze recommended.**

| Freeze candidate | Recommendation |
|------------------|----------------|
| MCR-016 / MCR-017 (reaction force + formulas) | **Ready to freeze.** Constant independently re-derived; primary source retrieved and matches verbatim; zero live legacy constants; restatements consistent across all sections, templates and four training packs. |
| MCR-047, 048, 051, 052 | **Ready to freeze.** Restatements consistent everywhere; no numeric discrepancy found. |
| MCR-049 | **Ready to freeze** (non-numeric). |
| Section 20 RPN set | **Ready to freeze on the arithmetic** (17/17). **Not ready on the priority list** — F-02. |
| **MCR-046** | **Hold** — F-05, plus GAP-004. |
| **MCR-050** | **Hold** — F-01. Two disagreeing limits in the SSOT should not be frozen into a training pack. |

The OP-001 / AWARE / VOC / SUP packs contain **no free-floating reaction-force constants** and cite MCR IDs throughout — the Phase 4 build rule held. None of them propagates the 680 bar or 2 759 bar values, so F-01 and F-05 do not currently contaminate the training material.

**Suggested action order:** Grok applies F-02, F-03 and the P2 set on this branch → human resolves F-01 and F-05 against the controlled OPS-P-019 (GAP-004) → human records the freeze sentence in `CAMPAIGN_LOG.md` → merge.

This report does not tick the Phase 3 checkbox in `CAMPAIGN_LOG.md` and does not record a freeze. Both are outside Claude's authority under AGENTS.md; the human freeze remains the gate.
