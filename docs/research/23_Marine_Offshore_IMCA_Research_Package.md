# Research Package: Section 23 – Marine / Offshore / IMCA-specific HPWJ

**Prepared by:** Grok (Technical Truth Engine)  
**Date:** 16 July 2026  
**Status:** Research Package + production section now live. This package retained for audit trail.  
**MCR baseline:** 52 rows (v8.2). New rows proposed as MCR-053 onward (still Drafting until human gate).  
**Depth target:** Match Sections 16–20 (full physics, worked examples, tables, Verification Log).

---

## A. Proposed New MCR Rows (MCR-first)

| ID | Topic | Rule / Number / Threshold | Source(s) | Status | Notes / FMEA Link |
|----|-------|---------------------------|-----------|--------|-------------------|
| MCR-053 | Diver HPWJ Authorisation | Only divers trained and certified for underwater HP/UHP jetting per IMCA D049 (or equivalent company standard) may operate. Surface support must hold concurrent competence. | IMCA D049 Rev 1.2; Anabeeb OPS-P-019 principle | Drafting | Priority for any marine work |
| MCR-054 | Underwater Reaction Force Control | Reaction force limits remain the three additive controls (≤250 N, ≤1/3 body weight, geometry). In water buoyancy reduces effective weight → tighter practical limit. Dedicated standby diver + surface dump control mandatory. | IMCA D049 principles; MCR-016 extension; industry practice | Drafting | Higher RPN underwater |
| MCR-055 | Hose Tethering & Securing (Wet) | All high-pressure hoses must be securely tied off / restrained at multiple points to prevent hose whip or entanglement of diver. Never free-floating. | IMCA D049; IMCA SF 09/17 extract | Drafting | Direct from D049 guidance |
| MCR-056 | Dump / Dead-Man System (Underwater) | Fail-safe dump system must be operable by both the diver (if equipped) and surface tender. Continuous communication + pre-agreed emergency dump signal. | IMCA D049; general diving safety | Drafting | Non-negotiable |
| MCR-057 | Exclusion of Non-Essential Personnel | No non-essential personnel (including supervisors) inside the immediate work area or line of fire. Barriers + positive communication. Dock-bottom / moon-pool / confined wet areas treated as high-risk. | IMCA SF 18/20; IMCA D049 | Drafting | Direct lesson from SF 18/20 |
| MCR-058 | Medical Alert + DMAC | All divers engaged in HPWJ carry Medical Alert Card + awareness of DMAC recommendations for high-pressure water jet injuries. Immediate surface medical support must know the injury mechanism. | IMCA D049 Appendix 1 (DMAC); MCR-043 extension | Drafting | Critical |
| MCR-059 | Maximum Pressure for Diver-Held | Follow IMCA D049 / company limit. Typical public practice for diver-held is lower than land UHP (often ≤10–15k psi class unless specially engineered). Anabeeb 40k psi ceiling still applies but method selection hierarchy (prefer automated/ROV) is stricter underwater. | IMCA D049; MCR-046; MCR-039 | Drafting | Hierarchy of methods elevated |
| MCR-060 | Cavitation Blaster / Special Tools | Cavitation tools have additional injury modes (see IMCA SF 06/07). Require specific risk assessment and training beyond standard HPWJ. | IMCA D049 Appendix 5; SF 06/07 | Drafting | |

**Total proposed new:** 8 rows (MCR-053 to MCR-060). Final wording subject to Claude review + human gate before Status changes from Drafting to Visible.

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

**Note:** Full text of IMCA D049 is not freely downloadable (member-only). All claims are limited to publicly visible TOC, safety flashes, secondary references, and standard offshore practice. Full clause extraction marked as [INTERNAL GAP] where needed.

---

## C–H. (Superseded by live production section)

The full production draft is now at `docs/23_Marine_Offshore_IMCA.md`.  
This research package is retained as the audit trail of sources, proposed MCR rows, and original derivations.  
See the production section for the corrected seawater density derivation and complete narrative.

---

**End of Research Package (updated after Claude review feedback)**
