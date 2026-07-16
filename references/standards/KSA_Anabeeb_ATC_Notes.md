# KSA / Anabeeb / Client-Specific Requirements – v8.1 (SABIC Gold Source Integrated)

**Last updated:** 16 July 2026  
**Status:** Primary differentiator file. SABIC OMS Attachment 8.2 (mandatory for KSA/MEA) now fully extracted and mapped. Aramco internal SAES/CSMS still require company documents.

This file is the highest-priority differentiator for Anabeeb. It is now the deepest standards document in the repository for SABIC work.

---

## 1. Anabeeb Operating Context
- Company: Arabian Pipeline & Services Co. Ltd. (Anabeeb)
- Primary base: Al Jubail Industrial City / Eastern Province
- Key clients: PETRO RABIGH, SABIC affiliates (incl. YANSAB), Aramco-related work, other industrial turnarounds
- Training: Anabeeb Training Center (ATC), Majd Square – TVTC approval process, ECITB relationship (MJI-10 etc.)
- QHSSE: Direct reporting line to CEO; owns CASE actions, ISO, training licence, HSE/Iqama recruitment

---

## 2. SABIC OMS Attachment 8.2 – High Pressure Water Jetting (Mandatory for KSA)

**Source document:** SABIC OPERATIONS MANAGEMENT SYSTEM – Attachment 8.2 High Pressure Water Jetting (HPWJ). Mandatory for KSA sites; optional/recommended for other regions. Cross-referenced to SHEM 08.07, SHEM 08.10, SHEM 08.08, SHEM 08.09, SHEM 08.11, SHEM 05.00, OMS-232, OMS-234.

### 2.1 Hierarchy of Methods (Table 4.1) – Core Selection Control

| Method | Permission Status | Key Notes |
|--------|-------------------|-----------|
| Fully automated mechanized, controls outside | Yes | Preferred |
| Mechanized, controls outside (>6 m or shielding) | Yes | Preferred |
| Mechanized, controls inside | Yes with team JSA | Full PPE |
| Manual with strain relief (no reaction force) | Yes with team JSA | Full PPE |
| Manual without strain relief (reaction force) | Discouraged – Area Sr. Manager + RA | Highest risk |
| Flexible lance with hose catcher / AWD | Only rare cases – Director + RA | Level 3 only |
| Flexible lance without catcher / open-ended | **Not permitted** | Absolute ban |

**MCR-039** implements this hierarchy.

### 2.2 Planning & Authorising Person (SABIC 2.2)
- End-User Manager appoints trained **HPWJ Authorising Person**.
- Service only from SABIC GPS approved contractor list, specialised in the rated pressure and method.
- **Technical Specification form (ATT-1)** mandatory: materials, condition, tags, method, max pressure, flow, location (in-situ vs designated area), residual process hazards (SDS), environmental controls, access/tenting/barriers.
- Maximum permitted pressures (ATT-2) – exceed only with Process + Asset Engineering Manager approval.
- Lone working prohibited.
- **MCR-041**.

### 2.3 Competency & Medical (SABIC 2.3)
- TQCP (or equivalent) for the **specific method/technique and pressure class** + min 1 year similar experience + 2-year refresh. Stamped in third-party qualification passport.
- Automatic-machine qualification does **not** authorise manual HPWJ.
- Medical fitness required.
- **Medical Alert Card** (waterproof, immediately accessible) mandatory for all operators (ATT-4 sample). Injuries appear insignificant but destroy deep tissue.
- Kick-off meeting (SHEM 05.00); EHSS orientation; HPWJ Hazard Awareness (ATT-3).
- Annual third-party inspection of HPWJ machine, high-pressure components and safety features.
- **MCR-042, MCR-043**.

### 2.4 Site Preparation Highlights (SABIC 2.4)
- Designated “special cleaning areas” preferred (quiet, rarely-visited, fully enclosed, No Entry signs).
- No jetting on pebbled areas.
- Confined space: avoid if practicable; if required, full CSE permit + increased ricochet/mist/slip controls.
- Electrical: remove flammables; bonding/grounding if static risk (SHEM 08.05); hazardous-area classification for diesel/electric units.
- Safe platform: escape routes clear; reaction force ≤250 N longitudinal; **no ladders**; scaffolding designed/secured; steel guarding preferred for lance operator (especially downward jetting on tube bundles).
- Water source: potable quality, free of suspended solids; fire hydrant only per SHEM 11.04; adequate drainage; chemical waste via Environmental team.
- **MCR-016 (250 N), MCR-027 / MCR-031 (barricading)**.

### 2.5 PPE (SABIC 2.4.6 + TST / TurtleSkin)
- Last resort. Pressure-class matched:
  - Body/Hand: **10/28** up to 14 500 psi; **20/30** up to 30 000 psi or TurtleSkin WaterArmor.
  - Foot: waterproof boots + metatarsal guards; 3000 boots or WaterArmor for high pressure.
  - Shin guards for gun operators.
  - Head: hard hat + face shield + safety glasses (goggles if aerosol); full-face visor BS EN 166 Impact Grade B min + chin protection; head protection 20/30.
  - Hearing as required.
  - Gloves correct size (must not jam trigger); specialist jet-penetration resistant recommended.
  - Full body suit for the HPWJ pressure when inside jetting area (ATT-8 example).
  - RPE if process residues produce hazardous mist (MSDS).

### 2.6 Equipment & Area Setup (SABIC 2.6)
- Failsafe dump (dead-man) control valves mandatory.
- Pressure control: calibrated knob/gauge; annual calibration.
- Hoses: no kinks/cuts/chipping; pressure rating engraved; annual pressure test; visual every use; no splicing (only proper fittings).
- Lances: **minimum 1.2 m** (48 in) from trigger to tip. Shorter only with double trigger + extra hand protection. Flexible hoses require ≥300 mm stainless rigid leader at nozzle end.
- Safety shroud **≥6 ft** at gun/lance connection.
- Hose anti-whip / restraining devices at all connections, correct rating.
- No quick-connect fittings on high-pressure hoses.
- Barricade: rope/tape minimum **6 m** from work piece. Robust screens (≥2 m high) may allow closer (not <3 m) if agreed and documented. “NO UNAUTHORISED ENTRY – HIGH PRESSURE WATER JETTING IN PROGRESS” notices at all approaches.
- ATT-6 Pre-Job Checklist is **pre-requisite** for HPWJ Work Permit (ATT-7 / SHEM 08.10).
- **MCR-044, MCR-045, MCR-023, MCR-027**.

### 2.7 Operational Arrangements (SABIC 2.7)
- Minimum two-person team. Pump operator watches lance operator for fatigue/difficulty and monitors area.
- Additional members for remote dump, sheeted enclosures, complex SIMOPS, UHP.
- Continuous communication without blind spots; hand signals agreed pre-job.
- Only team members inside barrier while jetting. Any entry = suspend jetting + Supervisor escort.
- HPWJ Supervisor primary liaison with Permit Issuer; Authorising Person does periodic visits.
- Rotate duties to minimise fatigue.
- Full Do’s and Don’ts (ATT-5) enforced as Never Rules (MCR-038).

### 2.8 Reaction Force Formula (Confirmed)
```
Back Thrust (lbf) = 0.052 × Flow (GPM) × √Pressure (psi)
1 lbf = 4.448 N
Maximum ≤ 250 N longitudinal
```
Matches MCR-016 / MCR-017 and YANSAB JSA.

### 2.9 Work Process Flow (SABIC 2.5)
Exact step/responsibility table is reproduced in Chapter 8.11. Key gate: ATT-6 complete → HPWJ Work Permit issued → work proceeds under continuous control.

### 2.10 Supporting Attachments (Internal SABIC ECM Links)
- ATT-1: Technical Specification form
- ATT-2: Maximum Permitted Pressures
- ATT-3: HPWJ Awareness PPT
- ATT-4: Medical Alert Card sample
- ATT-5: Do’s and Don’ts
- ATT-6: Pre-Job HPWJ Safety Checklist
- ATT-7: HPWJ Work Permit (use SHEM 08.10 / OMS 316.10 H Appendix)
- ATT-8: PPE Suit example
- ATT-9: Equipment details

---

## 3. YANSAB Field Evidence (C-1201 Quench Water Tower Hydrojetting JSA + Checklist)

Real YANSAB JSA (Nov 2021 / Jan 2022) for internals cleaning by hydrojetting confirms:
- Same 250 N reaction force formula and limit.
- Same PPE ratings (10/28, 20/30, TurtleSkin, metatarsal boots, shin guards).
- Buddy system + signal communication mandatory.
- ATT-6 style checklist items (barricade 6 m, dead-man, third-party certificates, no quick-connects, safety shroud 6 ft, anti-withdrawal, Medical Alert Card, etc.).
- Environmental controls: residue to drain system, continuous level checks, mesh/strainer, drip tray for machine oil.
- Confined-space interfaces fully controlled (gas testing, SCBA for first entry, LOTO, N2 isolation, rescue plan).
- Heat load from PPE explicitly controlled by work regiment + rotation + rest area.

This is living proof that the SABIC controls are actively enforced on SABIC affiliate sites.

---

## 4. Saudi Aramco Interface (Still Partially Open)

### Publicly Documented
- CSMS pre-qualification mandatory; historical performance (≈3-year window); Red Cards can permanently exclude.
- Hydrojetting is a procured Corporate Maintenance service (vessels, exchangers, piping by certified personnel).
- Strict PTW, isolation, competency records, barricading, SIMOPS, stop-work, heat stress, environmental controls expected.

### Still [UNVERIFIED – internal documents required]
- Full SAES clauses specific to high-pressure water jetting.
- Exact CSMS questionnaire scoring elements for HPWJ contractors.
- Any Aramco-specific maximum permitted pressures or PPE tables beyond general industry practice.

**Action:** Extract from Anabeeb-held Aramco CSMS packs, SAES library, and any client hydrojetting procedures. Map line-by-line to MCR.

---

## 5. PETRO RABIGH / Ma’aden / Other

Same practical pattern as SABIC: company PTW, LOTO, competency demonstration, SIMOPS, medical emergency protocols. Exact clause extraction still required from Anabeeb-held manuals.

---

## 6. Saudi Civil Defense & Local
- Civil Defense primarily fire equipment / facility compliance. No public mobile HPWJ-specific standard located.
- GOSI / Ministry of Labor general occupational rules apply (training, PPE, incident reporting, heat stress). Exact numeric thresholds for jetting remain **[UNVERIFIED – local HSE/legal review]**.

---

## 7. TVTC & ATC Implications
- ATC courses must produce audit-ready evidence: competency register, Medical Alert Card issuance log, practical assessment records, method-specific TQCP-aligned modules.
- Specialty modules (UHP tube bundle, automated systems, SABIC Authorising Person awareness) are high-value once core is solid.
- Chapter 8 + Chapter 13 + ATT-6 style checklists form the natural ATC training package for SABIC work.

---

## 8. Compliance Matrix Snapshot (SABIC → MCR → Chapter)

| SABIC Control | MCR | Primary Chapter / Template |
|---------------|-----|----------------------------|
| Hierarchy of methods / Table 4.1 | MCR-039 | Ch8, Ch3 |
| Min 2 persons / no lone work | MCR-040 | Ch8 |
| Authorising Person appointment | MCR-041 | Ch8, Ch12 |
| TQCP + 1 yr + 2-yr refresh | MCR-042 | Ch8, Ch13 |
| Medical Alert Card | MCR-043 | Ch8, Ch10, templates |
| Lance ≥1.2 m / 48 in | MCR-044 | Ch7, Ch8 |
| Safety shroud ≥6 ft | MCR-045 | Ch7, Ch8, Checklist |
| Reaction force ≤250 N | MCR-016 | Ch7, Ch8, Sec16 |
| Barricade min 6 m | MCR-027 / 031 | Ch5, Ch8 |
| ATT-6 pre-use gate | MCR-023 | Ch7, templates, Ch8 |
| Dump / dead-man | MCR-010 | Ch7 |
| No flexible lance without AWD | MCR-020 | Ch7, Ch8, Ch9 |
| Heat/work-rest/rotation | MCR-033 | Ch5, Ch8, Sec26 |
| Full Do’s & Don’ts | MCR-038 | Ch9, Ch8 |

---

## 9. Verification Log

| Claim | Source | Status |
|-------|--------|--------|
| Full hierarchy Table 4.1 + permission levels | SABIC OMS 8.2 §2.1 | Verified |
| Authorising Person, TQCP, 1 yr, 2-yr, Medical Card | SABIC 2.2–2.3 | Verified |
| 250 N + formula | SABIC 2.4.5.2; YANSAB JSA | Verified |
| 6 m barricade / 1.2 m lance / 6 ft shroud / no QC on HP hoses | SABIC 2.6 + Checklist | Verified |
| ATT-6 pre-requisite for permit | SABIC 2.6.8 / 3.7 | Verified |
| PPE 10/28 & 20/30 ratings | SABIC 2.4.6; TST catalogue | Verified |
| YANSAB JSA confirms same controls in field | YANSAB C-1201 JSA + Checklist | Verified |
| Aramco full SAES / CSMS questionnaire | — | **[UNVERIFIED – internal docs needed]** |

---

## 10. Immediate Next Actions (Updated)
1. ~~Extract SABIC OMS 8.2~~ → **Done** (this file + Ch8 + MCR-039–045).
2. Obtain and extract Aramco CSMS questionnaire + any SAES / GI hydrojetting clauses held by Anabeeb.
3. Same for PETRO RABIGH contractor HSE manuals.
4. Build printable one-page “SABIC HPWJ Gate Checklist” (ATT-6 + MCR cross-ref) for ATC and field use.
5. Update Medical Alert Card template if any wording differences vs SABIC ATT-4 sample.
6. Feed any new Aramco thresholds into MCR and this file.

**Owner:** Anabeeb QHSSE / ATC Lead  
**Target achieved for SABIC:** This is now the deepest client-specific standards file in the repository. Aramco remains the open differentiator gap.
