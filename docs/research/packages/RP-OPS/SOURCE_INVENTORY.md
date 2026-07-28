# RP-OPS — Anabeeb / Client Operational Controls

**Status:** Phase 1 baseline  
**Opened:** 28 July 2026  
**Canonical:** OPS-P-019 summary + KSA/SABIC notes + MCR-046–052  

---

## On-disk sources

| Source ID | Path | Access |
|-----------|------|--------|
| SRC-OPS-001 | `references/standards/Anabeeb_OPS-P-019_HPWJ_Procedure_Summary.md` | Internal summary |
| SRC-SAB-001 | `references/standards/KSA_Anabeeb_ATC_Notes.md` (SABIC 8.2 extract) | Client extract |
| SRC-REG-021 | `references/standards/21_Regulatory_and_Client_Matrix.md` | Synthesis |
| SRC-MCR | `MASTER_CONTROL_REGISTER.md` | SSOT |

---

## Anabeeb absolute controls (freeze candidates)

| MCR | Rule (short) | Primary source file |
|-----|--------------|---------------------|
| MCR-046 | Max 40 000 psi | OPS summary §3.8 |
| MCR-047 | Team of 3 + e-stop when LOS lost | OPS §6.4 |
| MCR-048 | RD ≤1.2× lowest MAWP | OPS §6.2 |
| MCR-049 | Manual ops ≥2 years + mgmt approval | OPS §9 |
| MCR-050 | Shotgun ≤10k psi / ≤1.6 mm / ≤250 N | OPS §9 |
| MCR-051 | 10 m unauthorised exclusion | OPS §9 |
| MCR-052 | Tip mark ≥600 mm | OPS §9 |

---

## Human-gated (see INTERNAL_GAP_REGISTER)

- GAP-002 Aramco SAES/CSMS  
- GAP-004 OPS full controlled PDF fidelity check  
- GAP-008 SABIC full attachment PDF  
- GAP-009 Site addenda (YANSAB / PETRO RABIGH)

---

## Harvest queue

1. Human confirms OPS summary matches controlled OPS-P-019 for MCR-046–052.  
2. Map every OPS Do/Don’t line → MCR-038 / Ch9.  
3. No new Visible MCR without Drafting + human gate.  

## Verification Log

| Check | Result |
|-------|--------|
| Seven Anabeeb rows present Visible in MCR | Pass (MCR-046–052) |
| Full Aramco extraction | Open GAP-002 |
