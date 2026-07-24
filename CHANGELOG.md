# Changelog

A running log of how this take-home evolved, so the evolution is trackable rather than a single
finished drop. The assessment asks to hear *"how you used AI — what you kept, changed, and
verified"*; this is part of that answer. Newest first.

The deeper story behind the biggest revision (v2) is in
[`appendix/reconciliation.md`](appendix/reconciliation.md); the tooling side is in
[`appendix/how-i-used-ai.md`](appendix/how-i-used-ai.md).

> View any change directly, e.g. `git diff 67bd569 98b4b78`, or a single revision with
> `git show <sha>`.

---

## [v2.2] — 2026-07-24 · `9bedf3b` — Tighten the brief to 1–2 pages
*2 files · +85 / −193*

- **Changed:** cut `docs/01-strategic-brief.md` from ~2,200 words (~4 pages) to ~1,020 (~1.8
  pages), because the assessment asks for 1–2 pages and "a point of view, not a comprehensive
  plan." Kept the reframe, the three patterns, the Voltaic trap, the three priorities, the
  constraint mechanic, and the leverage test.
- **Why it didn't lose anything:** the depth it shed already lived in `docs/02–04`, which the
  brief now points to as its working.

## [v2.1] — 2026-07-24 · `05ab8e9` — Add the Omni build brief
*3 files · +385 / −1*

- **Added** [`airtable-build/omni-build-brief.md`](airtable-build/omni-build-brief.md): the whole
  Airtable build as six sequenced copy-paste prompts for Airtable Omni (the AI app builder), each
  with a verify-and-fix gate for the things Omni approximates — formula syntax, verbatim AI-field
  prompts, exact select options.
- **Verified:** carries the same correctness gates as the human checklist ($3.11M at risk,
  Meridian → Value Evidence, Voltaic → Stage 2, Floor & Board → INSUFFICIENT EVIDENCE).

## [v2.0] — 2026-07-24 · `98b4b78` — Reconcile with an alternate draft + align to the JD
*21 files · +767 / −567 — the biggest revision. Full detail:
[`appendix/reconciliation.md`](appendix/reconciliation.md).*

A second strategy articulation was written independently; the two converged hard, so this is a
sharpen-and-merge, not a rewrite. Grounded against the [Director JD](https://job-boards.greenhouse.io/airtable/jobs/8602201002).

- **Kept** (my differentiators): the quantified scored table + four headline numbers, the
  binding-constraint engine, the Stage-0 "the model was wrong once" story, the AI
  `INSUFFICIENT EVIDENCE` refusal.
- **Combined** (adopted the alternate's sharper framing): pattern 2 made two-sided
  (person-dependence on both sides of the table); pattern 1 recut to "evidence problem, not
  adoption problem"; priorities regrouped to **Methodology / Value engine / Team OS**; governance
  elevated to a required through-line.
- **Added:** the skills matrix + pairing-of-complements (replacing hero-mode "I take the COO
  thread myself"); metrics in JD vocabulary (stage progression QoQ, value coverage).
- **Renamed** the four dimensions to JD-aligned labels — Adoption depth / Sponsorship &
  multi-threading / Governance maturity / Value evidence (was Capability / … / Proof). Same
  scores; rippled through schema, prompts, seed CSVs, and the script.
- **Fixed:** Meridian's binding constraint was labeled Governance but its lowest score is Value
  evidence — corrected so the formula and the prose agree (a sharper diagnosis, not just a
  cleanup).
- **Verified:** seed dry-run passes (83 records, all links resolve); ARR-at-risk recomputed to
  $3,110,000; all six constraints derive correctly.

## [v1.0] — 2026-07-23 · `67bd569` — Initial artifact set
*26 files · +2,745*

- Strategic brief + backing analysis (book diagnosis, methodology, operating model); the Airtable
  build spec (schema, AI components, interfaces, checklist) with seed data for all six accounts;
  an API seeding script; the live-session run-of-show and Q&A; assumptions and how-I-used-AI.
- **Verified:** seed CSVs validate via `scripts/seed_airtable.py --dry-run`.

## `dccd2d3` — 2026-07-23 — Repo created
- Empty README.

---

*Dates are the working dates of the exercise. Shas link each entry to the exact change.*
