# Full Stack Audit & Gap Map — HPWJ-Grokapedia

**Date:** 28 July 2026  
**Main head:** post PR #1–#4 merge (`2672b46` lineage)  
**Purpose:** Single view of what is live, what audits closed, what gaps remain, what to build next.

---

## 1. Stack layers (current)

| Layer | Location | Status |
|-------|----------|--------|
| **SSOT controls** | `MASTER_CONTROL_REGISTER.md` (65 Visible) | Live; AUDIT-005/007 unit fixes on main |
| **Ops core** | `docs/01`–`15` | Live |
| **Technical** | `docs/16`–`20`, `22`–`28` | Live; Sec16/20 post-Claude fixes |
| **Regulatory matrix** | `references/standards/21_…` | Expanded Class A/B + global rows |
| **Standards harvest** | `references/standards/*`, GLOBAL_STACK | Public stack dense; paid manuals open |
| **OEM harvest** | `references/manufacturers/*` + RP-MFG | Summaries + public safety harvest |
| **Field toolkit** | appendices C–J, templates | Live; App C tables regenerated |
| **Truth audits** | TRUTH_AUDIT v8.6.1, T1_T3_RUN, Claude report, Grok F-response | Arithmetic closed; Claude P1/P2 applied |
| **Training** | `training/` OP-001, SUP, UHP, AWARE, VOC | Live on main; pack drift clean |
| **Process** | AGENTS / WORKFLOW / PROCESS | Unit-pair T1 sweep adopted |

---

## 2. Audit chain (closed defects)

| ID | Class | Status |
|----|-------|--------|
| AUDIT-001–004 | Metric RF 0.745 restatements | **Closed** |
| AUDIT-005 / F-01 | MCR-050 680 vs 690 bar | **Fixed** (derived ≈690; GAP-004 if OPS independent) |
| AUDIT-006 / F-02 | Sec20 priority list vs RPN scores | **Fixed** (≥180 + Cavitation 192) |
| AUDIT-007 / F-03 | Sec16.6 orifice/Cd work | **Fixed** (4.97 GPM → 141 N) |
| F-04–F-08 | Rounding, 2758 bar, Ch8 PPE, caveats, labels | **Fixed** |

**Claude overall:** No P0. Freeze-ready: MCR-016/017, 047–049, 051–052, RPN arithmetic. Soft hold: independent OPS bar wording (GAP-004).

---

## 3. Gap register (prioritised)

### A. Human-gated (cannot invent)

| Priority | Gap | Impact | Action |
|----------|-----|--------|--------|
| **P0 soft** | **GAP-004** OPS-P-019 controlled PDF | Absolute Anabeeb numbers fidelity | Human drop PDF → re-extract MCR-046–052 |
| P1 | GAP-001 IMCA D049 full | Marine Sec23 depth | Membership / PDF |
| P1 | GAP-002 Aramco SAES/CSMS | Sec21 client depth | Internal docs |
| P1 | GAP-008 SABIC OMS 8.2 full PDF | Extract fidelity | Client PDF |
| P2 | GAP-003 Real Anabeeb incidents | Sec27 volume | QHSSE anonymised pack |
| P2 | GAP-005/006 ATC decks & equipment photos | Training polish | ATC / Ops |
| P2 | GAP-STD-* Orange Book / Black Code / ASNZS / SIR full text | Clause-level global | Purchase/license |
| P3 | GAP-007/009/010 OEM wet materials, site addenda, TVTC | Niche | As available |

### B. Buildable now (public / editorial)

| ID | Gap | Build action |
|----|-----|--------------|
| B-01 | Method endorsement packs (LTC/IBC/OBC/Bundle) | Scaffold AUTO + one LTC day |
| B-02 | T3 train-the-trainer pack | Later (after SUP pilot) |
| B-03 | Section health sheet | Create inventory of Verification Logs / MCR maps |
| B-04 | Unit-pair automation | `tools/audit/unit_pair_sweep.py` |
| B-05 | Residual unit pair LP 3000 psi (200 bar) | Fix to ≈207 bar |
| B-06 | Appendix B OEM matrix expansion | Optional P2 content |
| B-07 | Sec29 Future tech | Deprioritised |
| B-08 | Self-grading language residual sweep | Optional cleanup |
| B-09 | Training freeze formal sentence | Human |

### C. Unit-pair sweep (this audit)

| Pair | Status |
|------|--------|
| 10 000 psi / ≈690 bar | Aligned |
| 40 000 psi / ≈2 758 bar | Aligned |
| **3 000 psi / 200 bar** | **Mismatch** (true ≈206.8 bar) — fix in this branch |
| Other major pairs | Pass within 1.5% / 2 bar |

---

## 4. Training portfolio completeness

| Code | On main? | Notes |
|------|----------|-------|
| OP-001 | Yes | Core; Forms A/B |
| SUP | Yes | Level 4 |
| UHP | Yes | Level 3 |
| AWARE | Yes | Site |
| VOC | Yes | Refresh |
| AUTO / method days | **No** | Build next |
| T3 | No | Later |

---

## 5. Recommended build order (next)

1. Fix residual unit pair (LP 3000 psi).  
2. Ship `tools/audit/unit_pair_sweep.py`.  
3. Section health sheet.  
4. ATC-HPWJ-AUTO overview + LTC 1-day endorsement scaffold.  
5. Full-stack audit this file on main via PR.  
6. Human: GAP-004 + freeze sentence.

---

## 6. Freeze recommendation (current)

| Freeze set | Recommendation |
|------------|----------------|
| MCR-016, 017 | Freeze |
| MCR-047–049, 051, 052 | Freeze |
| Sec20 RPN products + ranked list | Freeze (post F-02) |
| MCR-046, 050 **psi** limits | Freeze as psi-primary; bar parentheticals derived |
| MCR-046/050 **if OPS states independent bar** | Hold until GAP-004 |
| Training packs | Pilot-ready (drift clean) |
