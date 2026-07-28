# Internal Gap Register

**Purpose:** Honest list of material that requires human / member / non-public sources.  
**Rule:** Do not invent clause numbers or incident details to fill these. Tag content `[INTERNAL GAP – human source required]`.  
**Last updated:** 28 July 2026  

---

## Open gaps

| Gap ID | Description | Blocks | Needed source | Owner | Status | Target package / section |
|--------|-------------|--------|---------------|-------|--------|--------------------------|
| GAP-001 | Full IMCA D049 clause-by-clause extraction (diver-held limits, equipment tables) | Sec 23 depth only | IMCA member PDF Rev 1.2 | Human | Open | RP-IMCA / Sec23 |
| GAP-002 | Aramco SAES / CSMS / contractor HPWJ requirements | Sec 21 client depth | Company-controlled Aramco docs | Human | Open | RP-OPS / Sec21 |
| GAP-003 | Real anonymised Anabeeb HPWJ incidents / near-misses | Sec 27 volume & MCR-062–063 exercise | QHSSE incident files (anonymised) | Human | Open | RP-INC / Sec27 |
| GAP-004 | OPS-P-019 full controlled original (if summary incomplete vs current controlled copy) | Any MCR change on Anabeeb absolutes | Controlled PDF / document control | Human | Open | RP-OPS / MCR-046–052 |
| GAP-005 | Existing ATC course decks, exam banks, checklists (if any) | Phase 4 efficiency | ATC training archive | Human | Open | RP-TRN / training/ |
| GAP-006 | Practical station equipment list & site photos for ATC delivery | Phase 4 equipment list realism | Operations / ATC | Human | Open | training/ ATC-HPWJ-OP-001 |
| GAP-007 | Manufacturer seawater / wet-service material recommendations (marine) | Sec 23 material notes | OEM data sheets | OEM / Human | Open | RP-MFG / Sec23 |
| GAP-008 | SABIC OMS 8.2 full attachment PDF (beyond existing extract) | Cross-check extract fidelity | Client-controlled PDF | Human | Open | RP-OPS |
| GAP-009 | YANSAB / PETRO RABIGH site-specific HPWJ addenda | Client matrix rows | Site HSE packs | Human | Open | Sec21 |
| GAP-010 | TVTC learning-outcome mapping for accreditation | Accreditation only (not ops truth) | TVTC framework docs | Human / ATC | Open | Ch13 later |
| GAP-STD-WJTA | Full WJTA Orange Book 2026 clause text | Clause-level US practice extract | Purchase 3rd ed. | Human | Open | RP-STD / WJTA_Summary |
| GAP-STD-WJA | Full WJA Black Code text | Clause-level UK practice | WJA App / membership | Human | Open | RP-STD / WJA_Summary |
| GAP-STD-ASNZ | Full AS/NZS 4233.1/.2 text | Legal AU clause extract | Standards licence | Human | Open | ASNZS summary |
| GAP-STD-SIR | Full SIR industrial cleaning manuals | NL industrial depth | SIR / training bodies | Human | Open | RP-STD |

---

## Explicitly not gaps (closed or deprioritised)

| ID | Item | Disposition |
|----|------|-------------|
| N/A | Arithmetic of MCR-017 metric constant | Closed in TRUTH_AUDIT + AUDIT-004 |
| N/A | Section 29 Future Technology | Deliberately deprioritised |
| N/A | Appendix B full OEM expansion | P2 — collect sources in RP-MFG; expand later |
| N/A | Fabricating incidents to “complete” Sec 25/27 | Forbidden — keep composites labelled |

---

## Does an open gap block training freeze?

| Gap | Blocks OP-001 freeze? |
|-----|------------------------|
| GAP-001 IMCA D049 | **No** — land operator course |
| GAP-002 Aramco SAES | **No** — if MCR already reflects Anabeeb + SABIC baseline used in Ch13 |
| GAP-003 Real incidents | **No** — use Sec 25 public/composite cases labelled correctly |
| GAP-004 OPS full PDF | **Soft** — freeze only if human confirms summary matches controlled copy for MCR-046–052 |
| GAP-005 Existing ATC packs | No — build from Ch13 standard |
| GAP-006 Equipment photos | No — list can start as generic minimum |
| GAP-007–010 | No for OP-001 |

**Recommendation:** Human should confirm GAP-004 (OPS-P-019 extract fidelity) before Phase 3 freeze. All other gaps stay open without blocking land OP-001.

---

## Intake process

1. Human drops source into agreed location (or attaches in chat).  
2. Grok adds SRC-* row to MASTER_SOURCE_INVENTORY.md.  
3. Grok extracts claims into relevant RP-* package with tags.  
4. New controls → MCR **Drafting** only → Claude → human promote.  
5. Close or reduce Gap ID when extraction verified.
