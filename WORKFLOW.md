# WORKFLOW.md — Dual-Model Operating Rhythm for HPWJ-Grokapedia

**Live as of 16 July 2026 (v1.1 role split)**

## Current Role Split
- **Grok** researches, derives, drafts full production sections, updates MCR/CHANGELOG, and pushes.
- **Claude** independently verifies numbers, citations, derivations, format, and MCR consistency; provides guidance; does **not** draft or push production content.
- **Human** provides internal sources, final gate, and ownership.

## Standard Loop for Any New Section or Major Expansion

1. **Human** states the goal + any internal sources (Anabeeb procedure excerpts, real incidents, Aramco notes).
2. **Grok** produces research (if needed) then full production section matching AGENTS.md format, proposes MCR rows, shows all work, updates supporting files, and pushes.
3. **Claude** reviews the live section: re-derives every number, checks citations against sources, verifies MCR consistency, flags any remaining unshown work or gaps, and returns a clear verification report with required fixes.
4. **Grok** applies agreed fixes and re-pushes if needed.
5. **Human** gives final approval (especially for Anabeeb operational rules).

## Immediate Priority Queue (as of v8.3)
- [x] Fix README MCR row-count drift
- [x] Lock dual-model schema (AGENTS.md + WORKFLOW.md) with correct role split
- [x] Section 23 Research Package + full production draft + push
- [ ] Claude verification of Section 23 + any fixes
- [ ] Section 27 Lessons Learned (seed with public + any anonymised Anabeeb cases)
- [ ] Section 29 Future Technology
- [ ] Appendices expansion
- [ ] Aramco deep extraction (human-gated)

## How to Start a New Task
Simply say:
“Grok: Draft and push Section XX / Topic”  
or  
“Claude: Review the live Section 23 and report findings”

Both models must re-read AGENTS.md and the current MASTER_CONTROL_REGISTER.md before every major output.

## Safety Gate
No new MCR row or numeric claim goes live without:
- Full derivation or primary citation + stated assumptions
- Dual-model review (Grok draft + Claude verification)
- Human final awareness (especially for Anabeeb operational rules)

This workflow exists so the encyclopedia stays true even as it grows deeper.
