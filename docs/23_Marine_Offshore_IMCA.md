# Section 23: Marine / Offshore / IMCA-specific HPWJ

**Status:** Live on main (production draft after clean dual-model verification)  
**Version:** 8.6.5  
**Date:** 16 July 2026  
**MCR Controls Referenced:** MCR-016, MCR-039, MCR-043, MCR-046, MCR-047, MCR-051 + MCR-053 to MCR-060 (all now Visible)

## MCR Mapping for This Section

| ID | Topic | Status |
|----|-------|--------|
| MCR-016 | Reaction Force (Three Additive) | Visible (extended underwater) |
| MCR-039 | Hierarchy of Methods | Visible (elevated underwater) |
| MCR-043 | Medical Alert Card | Visible (extended) |
| MCR-046 | Maximum System Pressure | Visible |
| MCR-047 | Anabeeb Minimum Team Size | Visible (higher manning wet) |
| MCR-051 | Unauthorised Person Exclusion | Visible (stricter wet) |
| MCR-053 | Diver HPWJ Authorisation | Visible |
| MCR-054 | Underwater Reaction Force Control | Visible |
| MCR-055 | Hose Tethering & Securing (Wet) | Visible |
| MCR-056 | Dump / Dead-Man System (Underwater) | Visible |
| MCR-057 | Exclusion of Non-Essential Personnel | Visible |
| MCR-058 | Medical Alert + DMAC | Visible |
| MCR-059 | Maximum Pressure for Diver-Held | Visible |
| MCR-060 | Cavitation Blaster / Special Tools | Visible |

---

## 23.1 Purpose & Scope

This section provides the additional controls, differences, and best practices required when High Pressure Water Jetting (HPWJ / hydroblasting) is performed in a marine, offshore, diving, dry-dock, moon-pool, or ROV-assisted environment. It is written for Anabeeb operations that interface with or support diving/marine work and aligns with the publicly available principles of IMCA D049 while remaining fully subordinate to Anabeeb OPS-P-019 and the Master Control Register. [SYNTHESIS + CITATION: IMCA D049 Scope]

It does **not** replace the land-based operational core (Chapters 1–15) or the physics baseline (Section 16). All land controls remain in force; this section only adds or elevates requirements where the wet/offshore environment increases risk.

---

## 23.2 Key Differences: Land (Anabeeb/SABIC) vs Wet/Offshore/IMCA

| Aspect | Land (Anabeeb / SABIC baseline) | Wet / Offshore / IMCA | Implication for Anabeeb |
|--------|----------------------------------|-----------------------|-------------------------|
| Minimum team | 3 competent persons (MCR-047) | Surface tender + standby diver + diving supervisor + HPWJ supervisor | Higher manning required |
| Exclusion | 10 m unauthorised (MCR-051) | Line-of-fire + physical barriers + no non-essential personnel in immediate area; dock bottom / moon-pool treated as high-risk | Stricter enforcement of MCR-057 |
| Hose management | Whip checks both ends + life limits (MCR-001–006) | + multi-point tethering / securing to prevent whip and entanglement of diver | MCR-055 |
| Reaction force | Three additive controls ≤250 N / ≤1/3 body weight / geometry (MCR-016) | Same physics + buoyancy reduces effective body weight → tighter practical application of the 1/3 rule | MCR-054 |
| Dump system | Operator dead-man + surface (MCR-010) | Dual: diver (if equipped) + surface tender, continuous communication, pre-agreed emergency dump signal | MCR-056 |
| Method hierarchy | Prefer automated / mechanized (MCR-039) | Strongly prefer ROV / remote / automated over diver-held | Elevated under MCR-059 |
| Medical | Medical Alert Card (MCR-043) | + DMAC awareness + surface medical team trained on jet injury mechanism | MCR-058 |
| Max pressure | 40 000 psi absolute (MCR-046) | Same ceiling, but method selection hierarchy is stricter; diver-held work typically kept to lower pressure classes unless specially engineered | MCR-059 |
| Competency | Anabeeb Training Dept + method-specific (MCR-042) | + IMCA D049 (or equivalent) diver jetting competence | MCR-053 |

---

## 23.3 Regulatory & Standards Framework

Primary public reference: **IMCA D049 – Recommended practice for the use of high pressure jetting equipment by divers** (Rev 1.2, November 2023; content largely stable since Rev 1 July 2013). [CITATION]

Supporting public sources used:
- IMCA Safety Flash 18/20 (12 June 2020) – Serious injury caused by high-pressure washer (250 bar kick-back, line-of-fire).
- IMCA Safety Flash 09/17 – LTI leg injury during HP water jetting (hose securing).
- IMCA Safety Flash 03/15 – Diver sustains water jetting injury.
- IMCA Safety Flash 06/07 – Diver injury using cavitation blaster (extracted in D049).
- IMCA Safety Flash 15/18 – LTI diver injured during water jetting.
- DMAC recommendations on high-pressure water jet accidents (Appendix 1 of D049).

Relationship to Anabeeb:
- Anabeeb OPS-P-019 and the Master Control Register remain the governing documents for Anabeeb personnel and equipment.
- Where IMCA D049 or diving regulations impose stricter controls, those become mandatory for the marine portion of the work.
- Full clause-by-clause mapping of D049 is [INTERNAL GAP – requires IMCA membership or licensed copy].

---

## 23.4 Personnel Competency & Authorisation (MCR-053)

Only divers who have been trained and assessed as competent for underwater HP/UHP jetting in accordance with IMCA D049 (or an equivalent company standard accepted by the diving contractor) may operate the jetting equipment while diving. Surface support personnel (tender, supervisor) must hold concurrent competence in the HPWJ system in use. [CITATION: IMCA D049 principles; MCR-042 extension]

Anabeeb personnel supervising or supporting such work must verify the diving contractor’s competency records before the permit is issued. Method-specific certification (MCR-042) still applies; automatic land qualification does not authorise underwater work.

---

## 23.5 Equipment & Hose Management Underwater (MCR-055, MCR-056)

**Hose tethering (MCR-055)**  
All high-pressure hoses must be securely tied off / restrained at multiple convenient points so that a free hose cannot whip or entangle the diver. Free-floating high-pressure hose is prohibited. This is a direct operational requirement drawn from IMCA D049 guidance and reinforced by IMCA SF 09/17. [CITATION]

**Dump / dead-man system (MCR-056)**  
A fail-safe dump system must be operable by both the diver (where the tool design permits) and the surface tender. Continuous two-way communication is mandatory. A pre-agreed emergency dump signal must be briefed and tested before the dive. [CITATION: IMCA D049 principles + general diving safety practice]

All other land-based equipment rules (whip checks both sides, life limits, rupture disc ≤1.2× lowest MAWP, pre-use inspection, etc.) remain fully in force.

Seawater corrosion, biofouling, and elastomer compatibility with seawater are additional equipment integrity issues. Specific material recommendations are manufacturer-dependent and marked [INTERNAL GAP – manufacturer data required].

---

## 23.6 Reaction Force & Control Underwater (MCR-016 + MCR-054)

### Physics (unchanged magnitude)

The reaction force at the nozzle is determined by the rate of change of momentum of the jet:

$$ F_r = \dot{m} \, v = \rho \, Q \, v $$

With the theoretical exit velocity from Bernoulli:

$$ v = \sqrt{\frac{2 \Delta P}{\rho}} $$

After unit conversion and typical discharge-coefficient factors this yields the industry formula already verified in Section 16 and corrected in MCR-017:

$$ F_r\ (\text{lbf}) \approx 0.052 \times Q\ (\text{GPM}) \times \sqrt{P\ (\text{psi})} $$

$$ F_r\ (\text{N}) \approx 0.233 \times Q\ (\text{L/min}) \times \sqrt{P\ (\text{bar})} $$

**Historical note (AUDIT-004):** The previous constant 0.745 was a unit-conversion error (correct only for MPa). Corrected 16 July 2026. This is the fourth independent restatement of the same bug that the standing restatement-search rule was designed to catch.

The formula itself does not change when the work is performed underwater. Ambient water pressure at dive depth is negligible compared with system pressures of hundreds of bar. [DERIVED from Section 16 + MCR-017]

### Buoyancy effect on the “≤ 1/3 body weight” control

Buoyancy reduces the diver’s effective weight in water. Therefore the second of the three additive controls in MCR-016 (“≤ 1/3 body weight”) becomes tighter in practice. The absolute 250 N limit and the geometry requirement remain unchanged. Many operators therefore adopt a lower absolute force limit for free-swimming or surface-supplied diver-held work. [DERIVED]

### Worked example (public 250 bar incident class – IMCA SF 18/20)

Incident pressure: 250 bar ≈ 3626 psi.  
Assumed typical hand-lance flow for this class of work: 5 GPM (≈ 19 L/min).

$$ F_r \approx 0.052 \times 5 \times \sqrt{3626} $$

$$ \sqrt{3626} \approx 60.22 $$

$$ 0.052 \times 5 \times 60.22 \approx 15.66\ \text{lbf} \approx 70\ \text{N} $$

Even this modest force produced a kick-back injury when the operator was unprepared and a supervisor stood in the line of fire. At higher pressures the force scales with √P and rapidly exceeds safe handheld limits for a diver without mechanical restraint. [DERIVED + CITATION: IMCA SF 18/20]

### Seawater as jetting fluid (rare)

Most systems use fresh or treated water. If seawater (ρ ≈ 1025 kg/m³) is used as the jetting fluid:

**Assumption (stated):** Positive-displacement plunger pumps hold volumetric flow rate Q essentially constant. Reaction force therefore scales directly with density:

$$ \frac{F_{\text{seawater}}}{F_{\text{fresh}}} = \frac{\rho_{\text{seawater}}}{\rho_{\text{fresh}}} \approx \frac{1025}{1000} = 1.025 $$

i.e. a **2.5 % increase** in reaction force. [DERIVED under stated constant-Q assumption]

If the pump were pressure-regulated instead of positive-displacement, the effect would be different (velocity falls as √(1/ρ) while mass flow rises as √ρ, net force still rises but by a smaller factor). Because the pumps used in this encyclopedia are positive-displacement, the 2.5 % figure applies. The effect is small and is treated as a qualitative awareness item rather than a hard control change. [DERIVED]

---

## 23.7 Operational Procedures & Communication

- Pre-dive briefing must include jetting-specific hazards, emergency dump signal, hose routing, and exclusion zones.
- Continuous communication between diver and surface tender is mandatory.
- Barriers and positive control of the work area (including dock bottom) are required. Non-essential personnel, including supervisors, must not enter the line of fire (MCR-057; direct lesson from IMCA SF 18/20). [CITATION]
- SIMOPS with other diving or vessel operations must be coordinated through the diving supervisor.
- All land-based pre-use inspection, LOTO, and permit requirements remain in force.

---

## 23.8 Medical Management (MCR-058)

All divers engaged in HPWJ tasks shall carry an immediately accessible waterproof Medical Alert Card (extension of MCR-043). Surface medical support must be briefed on the injury mechanism of high-pressure water jets (deep tissue damage, infection risk, delayed presentation) as set out in the DMAC recommendations referenced in IMCA D049 Appendix 1. [CITATION]

Any jetting injury, however minor it appears, is a medical emergency until proven otherwise (see Chapter 10).

---

## 23.9 Hierarchy of Methods (Elevated) (MCR-039 + MCR-059)

The existing hierarchy of methods (MCR-039) is elevated underwater:

1. Automated / ROV-deployed / remote tooling with operators outside the jetting area is the preferred method wherever reasonably practicable.
2. Diver-held manual jetting requires elevated approval, specific IMCA D049 competence (MCR-053), and the full set of underwater controls (MCR-054 to MCR-058).
3. Flexible lance without AWD / catcher remains Not Permitted (MCR-020).

Anabeeb’s absolute 40 000 psi ceiling (MCR-046) continues to apply, but diver-held work is typically kept well below this limit unless the tool and procedure are specially engineered and risk-assessed. [SYNTHESIS]

---

## 23.10 Specific Failure Modes & Lessons from IMCA Safety Flashes

| Failure Mode | Source | Key Lesson |
|--------------|--------|------------|
| Kick-back / loss of control + personnel in line of fire | IMCA SF 18/20 (250 bar) | Barriers + no non-essential personnel in immediate area (MCR-057) |
| Hose whip / entanglement | IMCA SF 09/17 + D049 | Multi-point tethering mandatory (MCR-055) |
| Diver jetting injury | IMCA SF 03/15, 15/18 | Competence + dump system + medical awareness |
| Cavitation blaster injury | IMCA SF 06/07 (in D049) | Special risk assessment and training (MCR-060) |

These lessons reinforce, rather than replace, the land-based FMEA in Section 20.

---

## 23.11 Worked Examples Summary

- Reaction force at 250 bar / 5 GPM ≈ 70 N (full derivation in 23.6).
- Seawater density effect under constant-Q assumption = +2.5 % (full derivation in 23.6).
- Buoyancy tightens the “≤ 1/3 body weight” control; absolute 250 N and geometry controls remain.

No other hard numeric thresholds are asserted beyond those already in the Master Control Register.

---

## 23.12 Checklist Additions for Marine / Diving Work

In addition to the standard Pre-Use Inspection Checklist and ATT-6 style forms, the following must be verified before any wet/offshore HPWJ task:

- [ ] Diver and surface support hold IMCA D049 (or equivalent) competence records (MCR-053)
- [ ] Hoses multi-point tethered / secured (MCR-055)
- [ ] Dual dump capability tested and emergency signal briefed (MCR-056)
- [ ] Barriers in place; non-essential personnel excluded (MCR-057)
- [ ] Medical Alert Cards carried; surface medical team briefed on DMAC jet-injury guidance (MCR-058)
- [ ] Method hierarchy justification recorded if diver-held work is selected (MCR-059)
- [ ] Standby diver and diving supervisor present and briefed

---

## Verification Log (Section 23)

| Claim / Formula | Method | Source / Cross-check | Status |
|-----------------|--------|----------------------|--------|
| Reaction force formula unchanged underwater | First-principles momentum + Bernoulli (Section 16) | Existing verified Section 16 | **Verified** |
| Metric constant 0.233 | First-principles unit conversion from verified imperial (MCR-017) | Corrected in v8.5.1 / v8.6.5 (AUDIT-004) | **Corrected & Verified** |
| 250 bar / 5 GPM worked example ≈ 70 N | Full arithmetic re-derivation | IMCA SF 18/20 pressure + industry formula | **Verified** |
| Seawater +2.5 % force under constant-Q | Density ratio 1025/1000 with stated positive-displacement assumption | Standard fluid density + pump type used throughout encyclopedia | **Verified under stated assumption** |
| Buoyancy tightens 1/3 body-weight control | Qualitative physical reasoning | Standard diving physics | **Verified as qualitative** |
| Hose tethering requirement | Direct from public IMCA sources | IMCA D049 principles + SF 09/17 | **Verified (public portion)** |
| No non-essential personnel in line of fire | Direct lesson | IMCA SF 18/20 | **Verified** |
| All other numeric thresholds | Existing MCR | MCR-016, 039, 043, 046, 047, 051 | **Unchanged** |
| Full D049 numerical limits for diver-held tools | Not publicly available | Member document | **[INTERNAL GAP]** |

**No remaining unverified numeric claims that are asserted as hard numbers.**  
All MCR-053–060 are now Visible (promoted by human gate after dual-model review).

---

**End of Section 23**

This section is deliberately conservative. It adds only those controls that can be grounded in public IMCA material or rigorous derivation from already-verified physics. Full member-only D049 details and any Anabeeb-specific marine procedure remain human-gated gaps.
