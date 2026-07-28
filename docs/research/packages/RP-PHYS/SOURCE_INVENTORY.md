# RP-PHYS — Physics & Hydraulics Research Package

**Status:** Phase 1 baseline (repo-backed) + expansion queue  
**Opened:** 28 July 2026  
**Canonical narrative:** `docs/16_Physics_and_Hydraulics.md`  
**Canonical controls:** MCR-016, MCR-017 (+ MCR-012 NPSH, MCR-029 water hammer)  
**Tagging:** [CITATION] / [DERIVED] / [SYNTHESIS] per AGENTS.md  

---

## A. Claims already locked in encyclopedia (do not change without dual re-derive)

| Claim | Tag | Location | Notes |
|-------|-----|----------|-------|
| Fr(lbf) ≈ 0.052 × Q(GPM) × √P(psi) | [CITATION]+[DERIVED lineage] | Sec16, MCR-017 | Industry formula; conference lineage cited in Sec16 |
| Fr(N) ≈ 0.233 × Q(L/min) × √P(bar) | [DERIVED] | Sec16, MCR-017 | From imperial; 0.2327 → 0.233 |
| Jet velocity from √(2P/ρ) tables | [DERIVED] | Sec16 | Audit re-derived 371/455/525/743 m/s class |
| Re worked example ~66 800 | [DERIVED] | Sec16 | Inputs stated |
| Compressibility @ 40 kpsi | [DERIVED] | Sec16 | Audit scope |
| Hydraulic power formula | [DERIVED] | Sec16 | Audit scope |
| Three additive RF controls | [CITATION]/[SYNTHESIS] | MCR-016 | Procedural industry + client |

---

## B. Source inventory (physics)

| Source ID | Source | Access | Use | Status |
|-----------|--------|--------|-----|--------|
| SRC-PHYS-RF | Imperial RF industry formula lineage (WJTA-IMCA conference paper as cited Sec16) | Secondary | Anchor imperial constant | In repo as citation note — strengthen with full biblio in expansion |
| SRC-PHYS-RF-M | First-principles unit conversion | Derived | Metric 0.233 | Locked by dual audit |
| SRC-PHYS-V | Bernoulli / orifice jet velocity | Textbook first principles | Velocity tables | Locked arithmetic |
| SRC-PHYS-RE | Reynolds definition ρvD/μ | Textbook | Turbulence regime | Locked example |
| SRC-AUDIT-861 | TRUTH_AUDIT_v8.6.1 | Process | Evidence of re-derivation | Closed |

---

## C. Public harvest queue (max collection)

1. Capture full bibliographic reference for the RF formula paper/lineage used in Sec16 (title, authors, year, venue).  
2. Collect 2–3 independent public industry sources that restate 0.052 imperial form (WJTA materials, manufacturer training, regulator guidance) — **for citation density only**, not to invent new constants.  
3. Document water density assumptions (fresh 1000 kg/m³ vs seawater ~1025) already used in Sec23 — keep consistent.  
4. List any competing RF formulas found publicly; if different, open Phase 3 defect rather than silent change.  
5. NPSH margin 0.5–1.0 bar (MCR-012): capture pump handbook / OEM typical practice citations.

---

## D. Proposed new MCR rows

None at this time. Physics package supports existing MCR-016/017. Any new derived threshold requires Drafting row + human gate.

---

## E. Honest gaps

| Gap | Note |
|-----|------|
| Full text of conference paper for RF formula | May be paywalled — use public restatements + existing derivation |
| Client-specific RF limits stricter than 250 N | Only if appear in OPS/SABIC extracts |

---

## F. Verification Log (package)

| Check | Result |
|-------|--------|
| Live operational constant is 0.233 not 0.745 | Pass (grep baseline 28 Jul 2026) |
| Derivation chain present in Sec16 | Pass |
| Restatement map lists known RF sites | Pass (MCR_RESTATEMENT_MAP) |
| New constants introduced in this package | None |

---

## G. Next actions

- [ ] Add bibliography block when public harvest completes  
- [ ] Phase 3 T1: re-derive metric constant once more as campaign entry exercise  
- [ ] Phase 3 T3: wording pass on all 0.052 / 250 N restatements  
