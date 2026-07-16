# Appendix C: Reaction Force Quick Calculator & Reference

**Status:** Draft on `draft/appendices`  
**Version:** 8.5.1 (updated after MCR-017 critical correction)  
**Purpose:** Printable field tool for supervisors and operators to quickly check whether a proposed nozzle/flow/pressure combination stays inside the three additive controls.

---

## C.1 The Three Additive Controls (MCR-016 + MCR-054)

All three must be true:

1. Absolute force ≤ **250 N** (≈ 56 lbf)
2. Force ≤ **1/3 of operator body weight**
3. Barrel / lance geometry prevents the jet from crossing the operator’s own feet or legs

Underwater (MCR-054): buoyancy reduces effective body weight → the 1/3 rule becomes tighter in practice. Absolute 250 N and geometry rules remain unchanged.

---

## C.2 Formulas (Corrected 16 July 2026)

**Imperial (verified)**  
$$ F_r \ (\text{lbf}) \approx 0.052 \times Q\ (\text{GPM}) \times \sqrt{P\ (\text{psi})} $$

**Metric (CORRECTED)**  
$$ F_r \ (\text{N}) \approx 0.233 \times Q\ (\text{L/min}) \times \sqrt{P\ (\text{bar})} $$

### Derivation of the Metric Constant (Full Work Shown)
Starting from the verified imperial formula:
- 1 GPM = 3.785411784 L/min
- 1 psi = 0.0689475729 bar → √(psi) = √(bar) / √0.0689475729 ≈ √(bar) / 0.26258
- 1 lbf = 4.448221615 N

$$ F_r(N) = 0.052 \times \left(\frac{Q_{L/min}}{3.785411784}\right) \times \left(\frac{\sqrt{P_{bar}}}{0.26258}\right) \times 4.448221615 \approx 0.2327 \times Q_{L/min} \times \sqrt{P_{bar}} $$

**Operational constant used:** **0.233**

**Historical note:** The previous constant 0.745 was correct only when pressure is expressed in **MPa**. It was incorrectly paired with bar. This is the same class of √10-scale unit conversion error previously fixed in Section 16 jet velocity. Appendix C tables were already correct because they were computed via the imperial path.

---

## C.3 Quick Lookup Tables (Pre-calculated with Corrected Formula)

### Imperial – Force in lbf (and N)

| Q (GPM) | 5 000 psi | 10 000 psi | 15 000 psi | 20 000 psi | 30 000 psi | 40 000 psi |
|---------|-----------|------------|------------|------------|------------|------------|
| 2       | 7.4 lbf (33 N) | 10.4 lbf (46 N) | 12.7 lbf (57 N) | 14.7 lbf (65 N) | 18.0 lbf (80 N) | 20.8 lbf (93 N) |
| 3       | 11.0 lbf (49 N) | 15.6 lbf (69 N) | 19.1 lbf (85 N) | 22.0 lbf (98 N) | 27.0 lbf (120 N) | 31.2 lbf (139 N) |
| 4       | 14.7 lbf (65 N) | 20.8 lbf (93 N) | 25.5 lbf (113 N) | 29.4 lbf (131 N) | 36.0 lbf (160 N) | 41.6 lbf (185 N) |
| 5       | 18.4 lbf (82 N) | 26.0 lbf (116 N) | 31.8 lbf (142 N) | 36.7 lbf (163 N) | 45.0 lbf (200 N) | 52.0 lbf (231 N) |
| 6       | 22.1 lbf (98 N) | 31.2 lbf (139 N) | 38.2 lbf (170 N) | 44.1 lbf (196 N) | 54.0 lbf (240 N) | 62.4 lbf (278 N) |
| 8       | 29.4 lbf (131 N) | 41.6 lbf (185 N) | 50.9 lbf (227 N) | 58.8 lbf (262 N) | 72.0 lbf (320 N) | 83.2 lbf (370 N) |
| 10      | 36.8 lbf (164 N) | 52.0 lbf (231 N) | 63.7 lbf (283 N) | 73.5 lbf (327 N) | 90.0 lbf (400 N) | 104.0 lbf (463 N) |

**Red zone** = > 250 N (≈ 56 lbf) — not permitted for handheld without special engineering controls and elevated approval.

### Metric – Force in N (Corrected Formula)

| Q (L/min) | 350 bar | 700 bar | 1000 bar | 1400 bar | 2000 bar | 2750 bar |
|-----------|---------|---------|----------|----------|----------|----------|
| 8         | 35 N    | 49 N    | 59 N     | 70 N     | 83 N     | 98 N     |
| 12        | 52 N    | 74 N    | 88 N     | 105 N    | 125 N    | 147 N    |
| 15        | 65 N    | 92 N    | 110 N    | 131 N    | 156 N    | 183 N    |
| 19        | 83 N    | 117 N   | 140 N    | 166 N    | 198 N    | 232 N    |
| 23        | 100 N   | 141 N   | 169 N    | 201 N    | 239 N    | 281 N    |
| 30        | 131 N   | 184 N   | 220 N    | 262 N    | 312 N    | 366 N    |

---

## C.4 How to Use in the Field

1. Know your actual orifice size and measured or rated flow (do not guess).
2. Look up (or calculate) the force using the **corrected** formulas above.
3. Check against all three additive controls.
4. If any one fails → change nozzle, reduce pressure, or switch to mechanised / automated method (MCR-039 / MCR-059).
5. Record the check on the pre-use inspection form.

---

## C.5 Worked Example (Already Verified)

0.040-inch orifice at 15 000 psi ≈ 5–6 GPM → **≈ 38 lbf / 170 N** (inside 250 N but still requires geometry and body-weight check).

250 bar (≈ 3626 psi) at 5 GPM → **≈ 15.7 lbf / 70 N** (the IMCA SF 18/20 incident class).

---

## Verification Log

| Claim | Source | Status |
|-------|--------|--------|
| Imperial formula | Section 16 + MCR-016/017 | Verified |
| Metric constant 0.233 | First-principles conversion from verified imperial (shown above) | **Corrected & verified 16 July 2026** |
| Tables | Direct calculation from corrected formulas | Derived |
| ±1 N shifts vs earlier draft table | Rounding refinement using the precise 0.2327 constant rather than a coarser intermediate value | **Not a second correction** – pure precision update |
| Three additive controls | MCR-016 + MCR-054 | Verified |
| Red zone definition | MCR-016 absolute 250 N | Verified |

**No new hard claims.** Pure synthesis + critical correction of upstream formula.
