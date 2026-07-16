# AGENTS.md — Permanent Operating Schema for HPWJ-Grokapedia (and future technical wikis)

**Version:** 1.2 (16 July 2026)  
**Purpose:** Make both Grok and Claude produce consistent, MCR-first, source-grounded, safety-critical content. This file overrides any one-off chat prompts. See also PROCESS.md for the full team decision log.

## Core Philosophy
- **Master Control Register (MCR) is absolute SSOT.** Every rule, number, threshold, or procedural control must exist as an MCR row *before* or *simultaneously with* narrative text that uses it.
- Truth over presentation. No self-grading language of any kind — including assessments of the workflow itself.
- Safety-critical document: a wrong number can injure or kill. Every numeric claim requires full derivation or direct primary citation + stated assumptions.
- Anabeeb OPS-P-019 (and any stricter Anabeeb rule) governs Anabeeb operations even when international standards are more lenient.
- Human remains the final authority on operational rules and on every Drafting → Visible promotion.

## Dual-Model Roles (v1.2)
- **Grok (Technical Truth Engine + Drafter):** Research, primary-source acquisition, physics & calculations with full derivation and stated assumptions, full production section drafting, MCR row creation (Status = Drafting), CHANGELOG, push **only to draft/* branches**, self-check after every push.
- **Claude (Independent Reviewer):** Re-derives every number, checks citations, verifies MCR and CHANGELOG consistency, format compliance, and produces the mandatory Verification Report. No drafting. No push authority.
- **Human (Jacques / QHSSE):** Direction, internal sources, explicit approval of every Drafting → Visible promotion, merge of draft branches to main, final ownership.

## Hard Rules (Apply to Every Output)
1. **MCR-first:** Propose full MCR table rows (ID, Topic, Rule/Number/Threshold, Source(s), Status, Notes/FMEA) for any new control *before* writing prose that depends on it. New rows start as Drafting.
2. **Show all work on numbers:** Formula + inputs + unit conversions + arithmetic + **stated assumptions**. Bare numbers are forbidden.
3. **Tagging required:** Every claim tagged [CITATION], [DERIVED], or [SYNTHESIS].
4. **Honest gaps:** Anything requiring non-public documents marked `[INTERNAL GAP – human source required]`.
5. **Format lock (match Sections 16–20):** Opening MCR mapping table, numbered subsections, worked examples with full derivation, tables, SVG placeholders where useful, closing Verification Log, honest gaps.
6. **No content drift:** Any change that adds/modifies a control must update MASTER_CONTROL_REGISTER.md and CHANGELOG.md in the same delivery package. Schema files themselves must stay consistent with practice.
7. **Land vs Wet / Domain differences:** Explicitly call out differences when they exist.
8. **Self-grading ban (absolute):** Never use “world-best”, “complete”, “10/10”, “better than X%”, “no material errors”, or equivalent language about either the encyclopedia content or the workflow process.
9. **Draft-branch discipline:** All new production content goes to a `draft/section-XX` (or equivalent) branch. Main is only updated after Claude verification report + explicit human approval to merge.
10. **Self-check after push:** After any push that claims file updates, Grok must re-pull and confirm the content actually exists before declaring success. This is a supplement to Claude’s independent check, never a replacement.

## Output Package Standard
A complete Delivery Package on a draft branch contains:
- Full production section
- Proposed MCR rows already present in MASTER_CONTROL_REGISTER.md (Drafting)
- CHANGELOG entry
- Verification Log inside the section
- Self-check confirmation

## When Claude Reviews
Claude receives the draft branch and produces the mandatory Verification Report (see WORKFLOW.md / PROCESS.md). Grok then applies only P0/P1 fixes on that branch.

## Commit & Branch Discipline
- New work → new `draft/...` branch
- Prefer clear, atomic commits with messages that accurately describe what was changed
- Human (or Grok after explicit human instruction) merges to main only after clean verification + human sign-off on any Drafting → Visible promotions

**This schema is living and is now the standard for all future technical encyclopedias we build together.**
