# RP-PHYS — Public Harvest Log

**Date:** 28 July 2026  
**Tags:** [CITATION] / [DERIVED]  
**Purpose:** Strengthen primary citations for reaction-force lineage; re-confirm metric conversion (Phase 3 T1).

---

## 1. Primary public citation for imperial 0.052 formula

| Field | Value |
|-------|--------|
| Title | Impact Force of High Pressure Waterjets |
| Author | D. Wright (StoneAge, Inc., Durango, Colorado) |
| Venue | 2013 WJTA-IMCA Conference and Expo, Houston, Texas, 9–11 September 2013 |
| Access | **Public PDF** |
| URL | https://www.wjta.org/images/wjta/Proceedings/Papers/2013/C1%20-%20DW%20Impact.pdf |
| Tag | [CITATION] |

### Claim extracted (verbatim sense)

Equation 1 in the paper:

> Force (pounds) = .052 × Pressure (psi)^(1/2) × Flow (gpm)

Paper states this is **the same equation used to calculate the reaction force produced by a waterjet**, and compares measured impact force at ~50 orifice diameters to that calculation (measured impact often 20–35% higher than calculated reaction at that standoff).

### Encyclopedia alignment

| Encyclopedia claim | Alignment |
|--------------------|-----------|
| MCR-017 imperial: 0.052 × Q(GPM) × √P(psi) | **Matches** Wright Eq. 1 (order of factors only) |
| Sec16 “WJTA-IMCA conference paper” lineage | **Now pinned** to Wright 2013 + public URL |

**Note:** Paper is about *impact* force vs standoff; it explicitly equates the industry reaction-force formula to Eq. 1. Operational handheld limits (≤250 N etc.) remain procedural [CITATION]/[SYNTHESIS] from MCR-016 / client practice — not from this paper alone.

---

## 2. Metric constant re-derivation (Phase 3 T1 — Grok, 28 July 2026)

**Inputs (exact conversion factors):**

| Factor | Value |
|--------|-------|
| 1 GPM | 3.785411784 L/min |
| 1 psi | 0.0689475729 bar |
| 1 lbf | 4.448221615 N |

**Derivation:**

\[
k_{\mathrm{metric}} = 0.052 \times \frac{1}{3.785411784} \times \frac{1}{\sqrt{0.0689475729}} \times 4.448221615
\]

**Result:** \( k = 0.232711\ldots \) → **operational 0.233** (MCR-017).

| Check | Result |
|-------|--------|
| Matches Sec16 shown work (~0.2327) | Pass |
| Delta vs 0.233 | 0.000289 (rounding only) |
| Live operational `0.745` (non-historical) | **None** (repo grep 28 Jul 2026) |

**Competing public formulas:** Fire-service nozzle formulas (e.g. R = 0.157 × P × d²) appear in secondary forums; they are **not** the industrial HPWJ Q–√P form. Do not mix without explicit domain call-out. [SYNTHESIS]

---

## 3. Related public technical paper (system config)

| Title | Configuring a Waterblast System (D. Wright) |
| URL | https://www.wjta.org/images/wjta/Proceedings/Papers/2009/D1%20Wright%20-%20Configuring.pdf |
| Use | Hose pressure-loss context; not RF constant | [CITATION candidate] |

---

## 4. Harvest status

| Item | Status |
|------|--------|
| Full biblio for 0.052 | **Done** (Wright 2013) |
| Metric re-derive | **Pass** |
| Independent second industry restatement of 0.052 | Open (optional density) |
| NPSH handbook citations | Open |

---

## 5. Proposed MCR changes

**None.** Confirms existing MCR-017; no Drafting rows.
