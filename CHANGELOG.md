# CHANGELOG

## draft/campaign-max-truth-training – 28 July 2026 (Campaign — not yet merged)

### Slice A — Campaign scaffold
- Branch `draft/campaign-max-truth-training` opened and pushed.
- Inventories + nine RP-* package stubs; status-drift cleanup (Ch13 52→65 rows; process queues).

### Slice B — Public harvest + truth campaign start
- `RP-PHYS/PUBLIC_HARVEST.md`: pinned imperial 0.052 to **D. Wright, StoneAge, 2013 WJTA-IMCA** public PDF (Eq. 1 = reaction force formula).
- Metric constant independently re-derived: **0.232711 → operational 0.233** (T1 Pass); no live operational `0.745`.
- `RP-STD/PUBLIC_HARVEST.md`: WJTA FT/FV (19HBFT/19HBFV); WJA Black Code + training/medical algorithm URLs.
- `RP-INJ/PUBLIC_HARVEST.md`: StatPearls NBK542210 + training caution (field emergency still mandatory for water injections).
- `RP-INC` + `RP-IMCA` PUBLIC_HARVEST: IMCA SF stable URL table (18/20, 09/17, 03/15, 15/18, 05/11, 07/11, 33/20).
- `TRUTH_CAMPAIGN_v9.md` moved from stub to **in progress**.
- Master source inventory updated with public URLs.
- **No new MCR rows. No training pack files. No formula changes.** Freeze still requires T3 + Claude + human.

## v8.6.5 – 16 July 2026 (Residual Status Drift + AUDIT-004 Closed)

### Critical
- **AUDIT-004**: Section 23.6 still contained the old wrong metric reaction force constant (0.745). This is the fourth independent restatement of the same unit-conversion defect. Corrected to 0.233 with full historical note. Standing rule expanded: restatement search now explicitly covers all narrative sections, not only the three previously known locations.

### Status Sync
- Section 23 MCR mapping table + Verification Log: MCR-053–060 updated from Drafting → Visible.
- Section 27 MCR mapping table + Verification Log: MCR-061–065 updated from Drafting → Visible.
- docs/00_Encyclopedia_Structure.md already current at v8.6.4 (confirmed); Section 21 path confirmed real under references/standards/.

### Previous
- v8.6.4: Full numeric truth audit formally closed; docs/00 aligned; manufacturer summaries scanned.
- v8.6.3 / v8.6.2 / v8.6.1: Three earlier instances of the 0.745 bug fixed + housekeeping.

**This changelog prioritises truth over presentation.**
