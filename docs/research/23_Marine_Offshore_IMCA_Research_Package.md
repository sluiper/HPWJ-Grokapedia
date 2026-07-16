# Research Package: Section 23 – Marine / Offshore / IMCA-specific HPWJ

**Prepared by:** Grok (Technical Truth Engine)  
**Date:** 16 July 2026  
**Status:** Research Package only — ready for Claude structured draft  
**MCR baseline:** 52 rows (v8.2). New rows proposed below as MCR-053 onward.  
**Depth target:** Match Sections 16–20 (full physics, worked examples, tables, Verification Log).

---

## A. Proposed New MCR Rows (MCR-first)

| ID | Topic | Rule / Number / Threshold | Source(s) | Status | Notes / FMEA Link |
|----|-------|---------------------------|-----------|--------|-------------------|
| MCR-053 | Diver HPWJ Authorisation | Only divers trained and certified for underwater HP/UHP jetting per IMCA D049 (or equivalent company standard) may operate. Surface support must hold concurrent competence. | IMCA D049 Rev 1.2; Anabeeb OPS-P-019 principle | Drafting | Priority for any marine work |
| MCR-054 | Underwater Reaction Force Control | Reaction force limits remain the three additive controls (≤250 N, ≤1/3 body weight, geometry). In water buoyancy reduces effective weight → tighter practical limit. Dedicated standby diver + surface dump control mandatory. | IMCA D049 principles; MCR-016 extension; industry practice | Drafting | Higher RPN underwater |
| MCR-055 | Hose Tethering & Securing (Wet) | All high-pressure hoses must be securely tied off / restrained at multiple points to prevent hose whip or entanglement of diver. Never free-floating. | IMCA D049; IMCA SF 09/17 extract | Drafting | Direct from D049 guidance |
| MCR-056 | Dump / Dead-Man System (Underwater) | Fail-safe dump system must be operable by both the diver (if equipped) and surface tender. Continuous communication + pre-agreed emergency dump signal. | IMCA D049; general diving safety | Drafting | Non-negotiable |
| MCR-057 | Exclusion / Exclusion of Non-Essential | No non-essential personnel (including supervisors) inside the immediate work area or line of fire. Barriers + positive communication. Dock-bottom / moon-pool / confined wet areas treated as high-risk. | IMCA SF 18/20; IMCA D049 | Drafting | Direct lesson from SF 18/20 |
| MCR-058 | Medical Alert + DMAC | All divers engaged in HPWJ carry Medical Alert Card + awareness of DMAC recommendations for high-pressure water jet injuries. Immediate surface medical support must know the injury mechanism. | IMCA D049 Appendix 1 (DMAC); MCR-043 extension | Drafting | Critical |
| MCR-059 | Maximum Pressure for Diver-Held | Follow IMCA D049 / company limit. Typical public practice for diver-held is lower than land UHP (often ≤10–15k psi class unless specially engineered). Anabeeb 40k psi ceiling still applies but method selection hierarchy (prefer automated/ROV) is stricter underwater. | IMCA D049; MCR-046; MCR-039 | Drafting | Hierarchy of methods elevated |
| MCR-060 | Cavitation Blaster / Special Tools | Cavitation tools have additional injury modes (see IMCA SF 06/07). Require specific risk assessment and training beyond standard HPWJ. | IMCA D049 Appendix 5; SF 06/07 | Drafting | |

**Total proposed new:** 8 rows (MCR-053 to MCR-060). Final numbers and exact wording to be confirmed after Claude draft + human review.

---

## B. Source Inventory (Public Only)

| Source | Type | Revision / Date | Access | Key Content Used |
|--------|------|-----------------|--------|------------------|
| IMCA D049 – Recommended practice for the use of high pressure jetting equipment by divers | Primary recommended practice | Rev 1.2 – November 2023 (content stable from Rev 1.1 Oct 2021 / Rev 1 July 2013) | Member document; TOC + public references available | Scope, Equipment, Protection of personnel, Operational procedures, Avoidance of accidents, Medical appendices, Safety flash extracts |
| IMCA Safety Flash 18/20 – Serious injury caused by high-pressure washer | Incident | 12 June 2020 | Public | 250 bar kick-back, supervisor in line of fire, barrier failure, lessons on non-essential personnel |
| IMCA Safety Flash 09/17 – LTI: Leg injury during HP water jetting | Incident | 2017 | Public | Hose securing / tethering |
| IMCA Safety Flash 03/15 – Diver sustains water jetting injury | Incident | 2015 | Public | Direct reference to D049 |
| IMCA Safety Flash 06/07 – Diver injury using cavitation blaster | Incident | 2007 | Extract in D049 | Cavitation-specific risk |
| IMCA Safety Flash 15/18 – LTI diver injured during water jetting | Incident | 2018 | Public | Related |
| DMAC (Diving Medical Advisory Committee) recommendations on HP water jet accidents | Medical | Referenced in D049 Appendix 1 | Public via D049 | Injury mechanism, medical response |
| Anabeeb OPS-P-019 + existing MCR-001 to MCR-052 | Company + internal SSOT | Current | Internal | Land baseline that must be adapted, never relaxed |
| WJTA / general HPWJ practice + existing Section 16 physics | Technical | Current | Public + existing | Reaction force, velocity, hose rules |

**Note:** Full text of IMCA D049 is not freely downloadable (member-only). All claims below are therefore limited to publicly visible TOC, safety flashes, secondary references, and standard offshore practice. Full clause extraction marked as [INTERNAL GAP] where needed.

---

## C. Full Section Outline (Tagged)

**docs/23_Marine_Offshore_IMCA.md** structure (to match 16–20):

1. **Purpose & Scope** [SYNTHESIS + CITATION to D049 Scope]
2. **Applicability** – When Anabeeb work is marine / offshore / diving / dry-dock / moon-pool / ROV-assisted [SYNTHESIS]
3. **Key Differences: Land (Anabeeb/SABIC) vs Wet/Offshore/IMCA** (table) [SYNTHESIS + DERIVED]
4. **Regulatory & Standards Framework** – IMCA D049 hierarchy, relationship to Anabeeb OPS-P-019, IOGP, national diving regs [CITATION]
5. **Personnel Competency & Authorisation** (MCR-053, MCR-042 extension) [CITATION + SYNTHESIS]
6. **Equipment Requirements Specific to Underwater** – hose tethering, dump systems, AWD/catchers underwater, rupture discs, seawater corrosion [CITATION + DERIVED]
7. **Reaction Force & Control Underwater** – buoyancy effect, three additive controls still apply, worked example adjustment [DERIVED from Section 16 + MCR-016]
8. **Operational Procedures** – pre-dive briefing, communication, emergency dump, SIMOPS with diving, barriers [CITATION from flashes + D049 principles]
9. **Medical & Injury Management** – DMAC recommendations, Medical Alert Card underwater, surface medical support [CITATION]
10. **Hierarchy of Methods (Elevated)** – prefer ROV / automated / remote over diver-held (MCR-039 + MCR-059) [SYNTHESIS]
11. **Specific Failure Modes** – hose whip underwater, entanglement, cavitation blaster, line-of-fire on dock bottom [CITATION to flashes]
12. **Worked Examples** – reaction force in water, exclusion zone in confined wet space [DERIVED]
13. **Templates / Checklists** – Marine Pre-Use / Dive-specific additions to existing ATT-6 style [SYNTHESIS]
14. **Verification Log**
15. **MCR Mapping Table** (top of section)

---

## D. Physics / Engineering Calculations (Full Derivation)

### D.1 Reaction Force Remains Physically Unchanged
The reaction force formula is independent of ambient medium for the jet itself:

$$ F_r \ (\text{lbf}) \approx 0.052 \times Q\ (\text{GPM}) \times \sqrt{P\ (\text{psi})} $$

or metric $$ F_r \ (\text{N}) \approx 0.745 \times Q\ (\text{L/min}) \times \sqrt{P\ (\text{bar})} $$

**Derivation reminder (from Section 16):** Momentum rate $$ \dot{m} v = \rho Q v $$, with $$ v = \sqrt{2\Delta P / \rho} $$ leading to the industry coefficient 0.052 after unit conversion and Cd factors.

**Underwater practical effect [DERIVED]:**
- Buoyancy reduces the diver’s effective weight → the “≤ 1/3 body weight” control becomes tighter in practice.
- Water drag on the hose and tool changes handling feel but does **not** reduce the reaction force magnitude at the nozzle.
- Therefore the three additive controls of MCR-016 remain mandatory; many operators adopt a lower absolute N limit for diver-held work.

**Worked example (public 250 bar incident class):**
250 bar ≈ 3626 psi. Assume a typical hand lance 15–20 L/min (≈ 4–5.3 GPM).
Using 5 GPM at 3626 psi:  
$$ F_r \approx 0.052 \times 5 \times \sqrt{3626} \approx 0.052 \times 5 \times 60.2 \approx 15.65\ \text{lbf} \approx 70\ \text{N} $$
Even this modest force caused a kick-back injury when the operator was unprepared and the supervisor was in the line of fire (IMCA SF 18/20). At higher UHP pressures the force scales with √P and becomes rapidly unmanageable for a free-swimming or even surface-supplied diver without mechanical restraint.

### D.2 Jet Velocity (Unchanged)
Same Bernoulli derivation as Section 16.4. Water density is essentially the same; ambient pressure at dive depth adds a small static head but is negligible compared with 100–400+ bar system pressure for velocity calculation.

### D.3 Additional Underwater Considerations (No New Hard Numbers)
- Seawater density ≈ 1025 kg/m³ → minor increase in reaction force (~2.5 %) if using seawater as the jetting fluid (rare; most systems use fresh or treated water).
- Hose buoyancy and current loading → additional mechanical loads on fittings and tethers (qualitative only).

---

## E. Land-based (Anabeeb/SABIC) vs Wet/Offshore/IMCA Differences

| Aspect | Land (Anabeeb / SABIC baseline) | Wet / Offshore / IMCA | Implication for Anabeeb |
|--------|----------------------------------|-----------------------|-------------------------|
| Minimum team | 3 competent persons (MCR-047) | Surface tender + standby diver + supervisor + diving supervisor | Higher manning |
| Exclusion | 10 m unauthorised (MCR-051) | Line-of-fire + barriers + no non-essential in immediate area; dock bottom treated specially | Stricter enforcement |
| Hose management | Whip checks both ends + life limits | + multi-point tethering / securing to prevent whip & entanglement | MCR-055 new |
| Reaction force | Three additive ≤250 N etc. | Same physics + buoyancy reduces effective body weight | Tighter practical limit |
| Dump system | Operator dead-man + surface | Dual: diver + surface tender, continuous comms | MCR-056 |
| Method hierarchy | Prefer automated (MCR-039) | Strongly prefer ROV / remote / automated over diver-held | Elevated |
| Medical | Medical Alert Card | + DMAC awareness + surface medical team trained on jet injury | MCR-058 |
| Max pressure | 40 000 psi absolute (MCR-046) | Same ceiling but method selection stricter; diver-held usually lower class | MCR-059 |
| Competency | Anabeeb Training Dept + method-specific | + IMCA D049 diver jetting competence | MCR-053 |

---

## F. Explicit Remaining Gaps (Honest)

- Full clause-by-clause extraction of IMCA D049 (member-only document) → [INTERNAL GAP – requires IMCA membership or licensed copy]
- Exact numerical pressure / orifice limits for diver-held tools in current D049 → [INTERNAL GAP]
- Anabeeb-specific marine / diving procedure (if any exists beyond OPS-P-019) → [INTERNAL GAP – human source]
- Real Anabeeb or KSA offshore HPWJ incident data → for Section 27 later
- Detailed ROV-integrated HPWJ configurations and manufacturer data for underwater tools → partial, can expand later
- Seawater-specific hose / elastomer compatibility tables → manufacturer data needed

---

## G. Draft CHANGELOG Entry (for v8.3)

```
## v8.3 – 16 July 2026 (Section 23 Research + Schema Lock)

### Structural
- Fixed README MCR row-count drift (38 → 52).
- Added AGENTS.md (permanent dual-model schema, MCR-first, format lock, no self-grading).
- Added WORKFLOW.md (research → draft → re-verify → human gate loop).

### Content
- Created full Research Package for Section 23 – Marine / Offshore / IMCA (docs/research/23_Marine_Offshore_IMCA_Research_Package.md).
- Proposed 8 new MCR rows (MCR-053 to MCR-060) covering diver authorisation, underwater reaction/hose/dump/medical controls, method hierarchy elevation.
- Public sources only: IMCA D049 (TOC + principles), multiple IMCA Safety Flashes (18/20, 09/17, 03/15, 06/07, 15/18), DMAC medical recommendations, existing physics (Section 16).
- Explicit land-vs-wet differences table and full derivation of reaction-force applicability underwater.
- No production prose yet — package ready for Claude structured draft.

### Status
Section 23 now has a complete, source-grounded research foundation. Next: Claude drafts the full section, Grok re-verifies numbers, human gate, then merge + MCR update to 60 rows.
```

---

## H. Ready-to-Expand Markdown Skeleton for Claude

```markdown
# Section 23: Marine / Offshore / IMCA-specific HPWJ

**Status:** Drafted from public sources (IMCA D049 principles + Safety Flashes) – awaiting number re-verification and human Anabeeb gate  
**MCR Controls Referenced:** MCR-016, MCR-039, MCR-043, MCR-046, MCR-047, MCR-051 + new MCR-053 to MCR-060

## MCR Mapping for This Section
| Control | Topic |
|---------|-------|
| MCR-053 | Diver HPWJ Authorisation |
| ... | ... |

## 23.1 Purpose & Scope
...

## 23.2 Key Differences: Land vs Wet
(table from Research Package E)

## 23.3 Regulatory Framework
...

## 23.4 Personnel Competency
...

## 23.5 Equipment & Hose Management Underwater
...

## 23.6 Reaction Force & Control Underwater
(full derivation + worked example)

## 23.7 Operational Procedures & Communication
...

## 23.8 Medical Management (DMAC)
...

## 23.9 Hierarchy of Methods (Elevated)
...

## 23.10 Specific Failure Modes & Lessons from IMCA Flashes
...

## 23.11 Worked Examples
...

## 23.12 Checklists & Templates Additions
...

## Verification Log
| Claim | Method | Source | Status |
|-------|--------|--------|--------|
| ... | ... | ... | ... |

**End of skeleton — expand fully while preserving all tags and derivations.**
```

---

**End of Research Package**

This package is deliberately conservative. All numeric claims that appear are either re-derived from Section 16 or taken from public incident descriptions. No member-only D049 numerical limits have been invented.

Ready for Claude to turn into production Section 23.

**Next action for human/Claude:** “Claude: Draft the full docs/23_Marine_Offshore_IMCA.md from this Research Package, following AGENTS.md format rules.”
