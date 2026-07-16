# CHANGELOG

## v8.3 – 16 July 2026 (Section 23 Live + Schema Role Split Fixed)

### Structural / Process
- Updated AGENTS.md and WORKFLOW.md to the actual current role split: **Grok drafts full production sections and pushes; Claude reviews/guides only** (no longer “Claude drafts”).
- Fixed the seawater density claim: full derivation under the explicit constant-flow-rate (positive-displacement pump) assumption now present; +2.5 % is no longer a bare assertion.
- All format rules (MCR mapping table, full derivations, Verification Log, land-vs-wet table, honest gaps) enforced in the live section.

### Content
- **Section 23 – Marine / Offshore / IMCA** is now live as a full production draft (`docs/23_Marine_Offshore_IMCA.md`).
- 8 new MCR rows proposed (MCR-053 to MCR-060) covering diver authorisation, underwater reaction/hose/dump/medical controls, elevated method hierarchy, and cavitation tools. Status = Drafting until Claude review + human gate.
- Public sources only: IMCA D049 principles (TOC + public extracts), Safety Flashes 18/20, 09/17, 03/15, 06/07, 15/18, DMAC, and verified Section 16 physics.
- Research package retained under `docs/research/` as audit trail and updated to point to the live section.

### Status
Section 23 is ready for Claude’s independent verification pass. No MCR rows have been promoted from Drafting to Visible yet.

### Previous (v8.2 – 16 July 2026)
- Anabeeb OPS-P-019 fully integrated + Safetech PPE.
- MCR to 52 rows (MCR-046 to MCR-052).
- Where Anabeeb is stricter, Anabeeb governs.

### Remaining Honest Gaps
- Full IMCA D049 clause extraction (member document).
- Exact numerical pressure/orifice limits for diver-held tools inside current D049.
- Anabeeb-specific marine/diving procedure (if any).
- Section 27 Lessons Learned.
- Section 29 Future Technology.
- Full appendices.
- Deep Aramco SAES/CSMS (internal docs only).

**This changelog prioritises truth over presentation.**
