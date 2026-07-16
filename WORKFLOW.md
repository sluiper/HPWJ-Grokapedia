# WORKFLOW.md — Dual-Model Operating Rhythm for HPWJ-Grokapedia

**Live as of 16 July 2026**

## Standard Loop for Any New Section or Major Expansion

1. **Human** states the goal + any internal sources (Anabeeb procedure excerpts, real incidents, Aramco notes).
2. **Grok** produces full Research Package (see AGENTS.md) using tools, primary sources, full calculations, MCR draft rows. Output is a markdown file under `docs/research/` or root.
3. **Claude** receives the Research Package and drafts the production section (`docs/23_....md`) matching existing style, adding full narrative, cross-links, and performing MCR consistency check.
4. **Grok** re-verifies every number, formula, and citation in Claude’s draft against primary sources and physics. Produces a short Verification Delta report.
5. **Claude** (or Grok) applies any final fixes.
6. **Human** reviews (focus on Anabeeb-specific truth and operational reality) and either:
   - Approves → Grok or Claude pushes the commit, **or**
   - Requests changes.

## Immediate Priority Queue (as of v8.3-prep)
- [x] Fix README MCR row-count drift (done)
- [x] Lock dual-model schema (AGENTS.md + WORKFLOW.md) (done)
- [ ] Section 23 Research Package → Claude draft → number re-verification → merge
- [ ] Section 27 Lessons Learned (seed with public + any anonymised Anabeeb cases)
- [ ] Section 29 Future Technology
- [ ] Appendices expansion
- [ ] Aramco deep extraction (human-gated)

## How to Start a New Task
Simply say:
“Grok: Research Package for [Section XX / Topic]”  
or  
“Claude: Draft Section 23 from the Research Package now available”

Both models must re-read AGENTS.md and the current MASTER_CONTROL_REGISTER.md before every major output.

## Safety Gate
No new MCR row or numeric claim goes live without:
- Full derivation or primary citation
- Dual-model review
- Human final awareness (especially for Anabeeb operational rules)

This workflow exists so the encyclopedia stays true even as it grows deeper.
