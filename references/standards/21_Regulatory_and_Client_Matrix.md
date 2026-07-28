# Section 21 / Regulatory & Client Matrix

**Version:** 8.0 (28 July 2026 — AU Class A/B + global public stack rows)  
**Purpose:** Planning, client interface, ATC curriculum design.  
**SSOT for Anabeeb operations:** `MASTER_CONTROL_REGISTER.md` + OPS-P-019 (where stricter, Anabeeb governs).  
**Public stack map:** `docs/research/inventory/GLOBAL_STACK_PUBLIC_SOURCES.md`

---

## 1. Competency & training systems

| Requirement Area | Anabeeb (this encyclopedia) | WJTA (USA) | WJA (UK) | AS/NZS 4233 + AU practice | Typical Aramco / SABIC / PETRO RABIGH | Notes |
|------------------|----------------------------|------------|----------|---------------------------|--------------------------------------|-------|
| Entry theory | OP-001 Day 1 + MCR workshop | Foundational Training (FT / 19HBFT) | Safety Awareness | Competent person; Class B via **RTO** | Company-approved training | Hybrid design |
| Practical assessment | Field Verification 15 critical items (OP-001) | Field Verification (FV / 19HBFV) | Practical modules + workplace evidence | Units of competency (MSMWJ pathway) | Demonstration often required | Checklist maps to MCR |
| VOC / refresh | **24 months** + triggers (Ch13) | FT often 3 years (public materials) | SA often ~3 years (provider notes) | **≥ every 2 years** (WorkSafe VIC public) | Client-driven | Anabeeb keeps 24-month |
| Trainer standard | Level 5 path + annual audit (Ch13) | Verified Trainer / Training Site | Approved instructors | Class B trainers: RTO + **≥5 years** experience (WorkSafe VIC) | Client approval | |
| Medical Alert | **Mandatory** MCR-043 | Recommended for all team (public) | Strong medical culture + algorithm PDF | Common / promoted | Client medical protocols | Aligns all major systems |
| Supervisor path | ATC-HPWJ-SUP Level 4 (Ch12 four gates) | Practice + owner programs | Leadership modules vary | Competent supervisors | Site Authorising Person (SABIC MCR-041) | |

---

## 2. Pressure / energy classification (comparison — do not swap SSOT)

| System | How energy/pressure is classified | Anabeeb mapping |
|--------|-----------------------------------|-----------------|
| **Anabeeb OPS-P-019** | LP / HP / UHP pressure bands; **absolute ceiling MCR-046** (40 000 psi / 2 759 bar) | **Operational SSOT** |
| **AS/NZS / AU public** | **Class A:** 800–5 600 **bar·L/min**; **Class B:** **> 5 600 bar·L/min** (WorkSafe VIC) | Comparison only until human maps bar·L/min table |
| **WJTA Orange Book** | Practice by pressure class + method (full text paid) | Public edition: 3rd ed. 2026 |
| **WJA Black Code** | Unified CoP across wash → UHP (full text gated) | Public structure only |

### Worked comparison note [DERIVED illustration — not a new control]

Energy product for illustration:  
`P(bar) × Q(L/min) = bar·L/min`

| Example | P | Q | Product | AU class (public definition) |
|---------|---|---|---------|------------------------------|
| 700 bar × 20 L/min | 700 | 20 | 14 000 | Class B (>5600) |
| 350 bar × 12 L/min | 350 | 12 | 4 200 | Class A (800–5600) |
| 2750 bar × 8 L/min (UHP-class flow) | 2750 | 8 | 22 000 | Class B |

Most Anabeeb industrial HP/UHP jobs sit in **AU Class B** territory on energy product. Training intensity should match Class B expectations (RTO-grade discipline), while **legal/ops labels** remain Anabeeb pressure + MCR.

---

## 3. Operational controls matrix

| Requirement Area | Anabeeb (MCR) | WJTA (public practice themes) | WJA (public) | AS/NZS + AU public | Client (SABIC / typical) | Notes |
|------------------|---------------|-------------------------------|--------------|--------------------|--------------------------|-------|
| Pre-use inspection | MCR-023 + 024 | Required (Orange Book topics) | Required | Required | Required | Templates live |
| Hose life / reject | MCR-001–004 | Strong (hose whitepaper linked) | Strong | Strong; Class B hose test themes | Usually required | |
| Whip checks | MCR-006 | Practice | Practice | Practice | Expected | |
| Quick-connect caution | MCR-007 | WJTA 2022 coupling alert | Practice | Practice | Expected | |
| Reaction force | MCR-016 / 017 three additive | Industry 0.052 formula lineage | Practice | “Known and allowable” language (QLD RSHQ public) | Expected | Constants only via MCR-017 |
| AWD flex lance | MCR-019/020 mandatory | Strongly recommended / practice | Practice | Required in practice | Expected | Non-negotiable |
| Exclusion | MCR-027/031/051 (Anabeeb 10 m unauthorised) | Mandatory zones | Mandatory | Mandatory | Strict | |
| Team size | MCR-047 **three** (Anabeeb) | Team themes | Team themes | Competent crew | SABIC baseline two (MCR-040) | Stricter Anabeeb |
| Dump / dead-man | MCR-010 | Practice | Practice | Practice | Expected | |
| Rupture disc factor | MCR-048 ≤1.2× lowest MAWP | Practice | Practice | Practice | Expected | |
| Hierarchy of methods | MCR-039 | Automated equipment section (Orange Book topics) | Practice | Practice | Prefer mechanised | |
| UHP / creeping hose | MCR-034 Level 3 + expanded | Guidance | Guidance | Class B rigor | High scrutiny | ATC-HPWJ-UHP pack |
| SIMOPS | MCR-028 | Expected | Expected | Expected | Strictly enforced | |
| Records / audit | Ch15 + MCR trail | Required | Required | Required | Heavy | |

---

## 4. Medical / emergency

| Area | Anabeeb | Global public alignment |
|------|---------|-------------------------|
| Medical Alert Card | MCR-043 mandatory | WJTA public recommendation; WJA algorithm; Hammelmann first-aid card PDFs; AU promotion |
| Injury framing | Ch10 — emergency, do not dismiss small wound | WJTA public: parallel gunshot evaluation language |
| Clinical depth | Ch24 | StatPearls + journals in RP-INJ |

---

## 5. Marine / offshore

| Area | Anabeeb | Global |
|------|---------|--------|
| Diver HPWJ | MCR-053–060; Sec23 | IMCA D049 (member full text = GAP-001); public SFs |

---

## 6. Living update rules

1. Update this matrix when public edition numbers change (e.g. WJTA edition).  
2. Never import foreign numeric thresholds into MCR without dual-model derivation + human gate.  
3. Client columns with Aramco SAES detail remain **[INTERNAL GAP]** until human supplies documents.

**References:** GLOBAL_STACK_PUBLIC_SOURCES.md; WJTA_Summary.md; WJA_Summary.md; ASNZS + Safe_Work_Australia notes; MASTER_CONTROL_REGISTER.md; OPS-P-019 summary; KSA notes.
