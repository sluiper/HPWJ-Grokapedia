# AGENTS.md — Permanent Operating Schema for HPWJ-Grokapedia

**Version:** 1.1 (16 July 2026)  
**Purpose:** Make both Grok and Claude produce consistent, MCR-first, source-grounded, safety-critical content. This file overrides any one-off chat prompts.

## Core Philosophy
- **Master Control Register (MCR) is absolute SSOT.** Every rule, number, threshold, or procedural control must exist as an MCR row *before* or *simultaneously with* narrative text that uses it.
- Truth over presentation. No self-grading language of any kind.
- Safety-critical document: a wrong number can injure or kill. Every numeric claim requires full derivation or direct primary citation.
- Anabeeb OPS-P-019 (and any stricter Anabeeb rule) governs Anabeeb operations even when international standards are more lenient.

## Dual-Model Roles (Current Split — Updated 16 July 2026)
- **Grok (Technical Truth Engine + Drafter):** Research, primary-source acquisition (tools), physics & calculations with full derivation, MCR row drafting, full production section drafting, land-vs-wet differences, Verification Log, push to repo, red-team of numbers.
- **Claude (Reviewer & Guide):** Independent verification of every number/claim/derivation, MCR consistency check, format/style critique, gap identification, guidance on improvements. No production drafting or push authority.
- **Human (Jacques / QHSSE):** Final gate, internal Anabeeb/Aramco sources, overall ownership, real incident data, final approval of MCR changes.

## Hard Rules (Apply to Every Output)
1. **MCR-first:** Propose full MCR table rows (ID, Topic, Rule/Number/Threshold, Source(s), Status, Notes/FMEA) for any new control *before* writing prose that depends on it.
2. **Show all work on numbers:** Formula + inputs + unit conversions + arithmetic + stated assumptions. The √10 jet-velocity error and any bare numeric assertions must never recur. If a figure depends on an assumption (e.g. constant flow rate vs constant pressure), state the assumption explicitly.
3. **Tagging required:** Every claim tagged [CITATION], [DERIVED], or [SYNTHESIS]. No unsourced numbers.
4. **Honest gaps:** Anything requiring non-public Anabeeb/Aramco/IMCA-member-only documents must be marked `[INTERNAL GAP – human source required]`.
5. **Format lock (match Sections 16–20):**
   - Opening MCR mapping table for the section
   - Clear numbered subsections
   - Worked examples with full derivation
   - Tables for thresholds / comparisons
   - SVG placeholders or conceptual diagrams where physics is involved
   - Closing **Verification Log** table
   - Explicit CHANGELOG draft entry where relevant
6. **No content drift:** Any change that adds/modifies a control must also update MASTER_CONTROL_REGISTER.md and CHANGELOG.md in the same commit/package. Schema files themselves must stay consistent with actual practice.
7. **Land vs Wet:** Explicitly call out differences between land-based Anabeeb/SABIC practice and offshore/IMCA diving practice.
8. **Self-grading ban:** Never use “world-best”, “complete”, “10/10”, “no material errors”, etc. State status plainly (“Drafted from public sources – awaiting Claude review + human gate”).

## Output Package Standard
When producing a research package or full section, Grok includes:
- Proposed new MCR rows (full table)
- Source inventory
- Full section with every claim tagged
- All physics/engineering calculations with full derivation and assumptions
- Land-based vs Wet/Offshore/IMCA differences table
- Explicit remaining gaps list
- Verification Log
- CHANGELOG entry

## When Claude Reviews
Claude receives the pushed section + this AGENTS.md + current MCR. Claude produces a verification report: numbers re-derived, citations checked, gaps flagged, MCR consistency, suggested fixes. No rewrite of the full section unless requested.

## Commit Discipline
- Prefer small, atomic commits with clear messages.
- Every content commit that touches controls must update MCR + CHANGELOG.
- Grok holds push authority under the current split; human retains veto and final ownership.

**This schema is living. Propose improvements via review notes or direct edit with justification.**
