# Appendix C: Reaction Force Quick Calculator & Reference

**Status:** Draft on `draft/appendices` – synthesis of verified Section 16 + MCR-016/017/054  
**Purpose:** Printable field tool for supervisors and operators to quickly check whether a proposed nozzle/flow/pressure combination stays inside the three additive controls.

---

## C.1 The Three Additive Controls (MCR-016 + MCR-054)

All three must be true:

1. Absolute force ≤ **250 N** (≈ 56 lbf)
2. Force ≤ **1/3 of operator body weight**
3. Barrel / lance geometry prevents the jet from crossing the operator’s own feet or legs

Underwater (MCR-054): buoyancy reduces effective body weight → the 1/3 rule becomes tighter in practice. Absolute 250 N and geometry rules remain unchanged.

---

## C.2 Formulas (Already Verified in Section 16)

**Imperial**  
$$ F_r \ (\text{lbf}) \approx 0.052 \times Q\ (\text{GPM}) \times \sqrt{P\ (\text{psi})} $$

**Metric**  
$$ F_r \ (\text{N}) \approx 0.745 \times Q\ (\text{L/min}) \times \sqrt{P\ (\text{bar})} $$

---

## C.3 Quick Lookup Tables (Pre-calculated)

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

### Metric – Force in N

| Q (L/min) | 350 bar | 700 bar | 1000 bar | 1400 bar | 2000 bar | 2750 bar |
|-----------|---------|---------|----------|----------|----------|----------|
| 8         | 35 N    | 50 N    | 59 N     | 70 N     | 84 N     | 98 N     |
| 12        | 53 N    | 75 N    | 89 N     | 105 N    | 126 N    | 147 N    |
| 15        | 66 N    | 93 N    | 111 N    | 131 N    | 157 N    | 184 N    |
| 19        | 83 N    | 118 N   | 141 N    | 166 N    | 199 N    | 233 N    |
| 23        | 101 N   | 143 N   | 171 N    | 202 N    | 241 N    | 282 N    |
| 30        | 132 N   | 186 N   | 222 N    | 263 N    | 314 N    | 368 N    |

---

## C.4 How to Use in the Field

1. Know your actual orifice size and measured or rated flow (do not guess).
2. Look up (or calculate) the force.
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
| Formulas | Section 16 (verified) + MCR-016/017 | Verified |
| Tables | Direct calculation from verified formulas | Derived |
| Three additive controls | MCR-016 + MCR-054 | Verified |
| Red zone definition | MCR-016 absolute 250 N | Verified |

**No new hard claims.** Pure synthesis for field use.
