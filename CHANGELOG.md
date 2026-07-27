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

## [v2.7] — 2026-07-27 — Make the brief readable to someone who hasn't seen the assessment
*7 files*

- **Added an orienting header to the brief.** It opened with *"the working is in `02`, `03`, `04`"* —
  insider shorthand that tells a reader nothing. It now says plainly what the document is (the 1–2
  page brief the assessment asks for), what it deliberately isn't (a comprehensive plan), and where
  each piece of supporting detail lives, including the play library.
- **Anchored two passages to what was actually asked** — *"the job is the book, not any one
  account"* ahead of the three patterns, and the **leverage test** framed as the assessment's own
  question (*does this make all fifteen CSMs better, not just me?*) rather than a phrase of mine.
- **Renamed the brief's priorities `P1/P2/P3` → `Priority 1/2/3`.** They collided with the play
  codes `P1`–`P8`: `assumptions.md` said "P2 drops to third" (a priority) two documents away from
  "Play P2 · Re-Sponsor". Updated across the brief, assumptions, Q&A, talk track, and the build's
  README and interfaces.
- **Replaced arrow shorthand with English** — *"Baseline → instrument → quantify → narrate"* became
  *baseline the workflow, measure it, convert it into the buyer's terms, tell it back to them*;
  *"diagnostic → stage → plays"* became *diagnose, stage, then run a play*. Spelled out
  Center of Excellence on first use.
- **Fixed a third instance of the templated-play error:** `airtable-build/README.md` still claimed
  three of eight plays have artifact templates and named the wrong three. It's five — P1, P2, P4,
  P6, P8 — per `plays.csv`. The same wrong claim was corrected in the Q&A in v2.5; this was the
  copy that got missed.
- **Then cut the fluff back out.** The additions took the brief to ~1,140 words; a trim pass —
  hedges, parenthetical lists, redundant qualifiers, never concepts — brought the body back to
  **~1,025 words**, the original target, with the ~60-word orienting header on top. Every
  load-bearing number, both required threads (people-manager lens, global consistency / local
  customization) and all five internal links verified intact afterward. `AGENTS.md` records the
  measurement and the priority-vs-play naming rule so neither drifts back.

## [v2.6] — 2026-07-27 — Add `AGENTS.md`; record the audit in how-I-used-AI
*4 files*

- **Added** [`AGENTS.md`](AGENTS.md) — the conventions this repo is edited under, written so the
  v2.5 audit can't quietly regress: the complete list of Airtable-side functions that may be named,
  the capability descriptions that replace the invented ones, the rule that definitions of done are
  signals rather than predictions, the standard-vs-latitude split, the verified load-bearing
  numbers, and the PR-and-changelog workflow. Most of its rules exist because something went wrong
  once, and each says which.
- **Added** §6 to [`appendix/how-i-used-ai.md`](appendix/how-i-used-ai.md) — *the failure mode I
  didn't expect.* The earlier AI errors were wrong **numbers**, and numbers get checked. This one
  was a wrong **premise** applied consistently across nine files, which is harder to see because
  internal consistency reads as correctness. The control isn't more careful reading; it's asking
  "what's the source for this?" of things that have stopped looking like claims.
- **Fixed a number that had been wrong since v1.0:** the seed record count was stated as 83 in
  three places (`how-i-used-ai.md`, `scripts/README.md`, and the v2.0 entry below). The dry-run
  reports **84** across 8 CSVs, and recounting at the v2.0 commit confirms it was 84 then too — so
  that entry's "verified" claim was itself unverified. All three corrected. A stale number in a
  deliverable arguing for value evidence is a bad look, and this one had been recited three times
  without being recomputed once.
- **Corrected:** the tooling note said Opus 4.8; later revisions ran on Opus 5.
- **Verified:** seed dry-run passes, all link references resolve.

## [v2.5] — 2026-07-27 · `66a6c12` — Name partner *capabilities*, not teams I can't verify exist
*13 files*

A self-audit of invented content, prompted by asking where each partner name actually came from.

- **Verified against the sources first.** The assessment names no Airtable-side partner functions
  at all; the JD names exactly five — *"partner closely with Renewals, Support, Professional
  Services, Product, and Sales."* Anything outside that list was mine.
- **The problem:** `Value Eng`, `Trust & Security`, `Deal Desk` and `Solutions` were org-chart
  names I'd invented and then used as if they were given. `Value Eng` wasn't even flagged in the
  assumptions.
- **Renamed repo-wide** to describe what has to be produced and who stands behind it —
  `Value Eng` → **Value Validation** (stands behind a quantitative claim before it reaches a
  customer's CFO), `Trust & Security` → **Security & Risk** (produces customer-facing risk and
  controls artifacts), `Deal Desk` → *whoever owns contracting*, and `Professional Services /
  Solutions` → **Professional Services**, which the JD does name. Touches the base schema's select
  options, the seed script, both play CSVs, `docs/02–05`, the AI component prompts, interfaces, the
  Omni brief, the talk track and the Q&A.
- **Kept, because they're grounded:** every customer-side name — Marketing Ops, RevOps, the IT
  Security & Data Governance Review Board, the CFO's office, procurement — is verbatim from the
  account snapshot, and the audit confirmed each one rather than assuming it.
- **Stated the rule rather than just applying it:** `docs/05` gains *"A note on partner names"* and
  `docs/04` makes the split explicit — named functions keep their names, unverifiable ones are
  described by capability, and **mapping them to real owners is a day-one question.**
  `appendix/assumptions.md` §3 now covers both capabilities and what breaks if either is missing.
- **Removed two unsupported claims about customer behavior.** P5's "most of what we are guessing at
  is written down somewhere" became *ask whether the criteria exist in writing — if they don't,
  that itself tells you how the board decides.* P6's "they already know they have agents nobody
  owns" became *run it where the customer has already raised the concern.* Voltaic's version stays,
  because they volunteered it in the snapshot — the generalization to all accounts was the part
  without support.
- **Fixed two internal inconsistencies:** the Q&A claimed only three plays were templated and named
  P2 as the next gap, but the base marks five templated (P1, P2, P4, P6, P8) — the real gap is P5
  then P7. And `docs/04`'s Corvus example had Professional Services validating value numbers while
  every other document said otherwise.
- **Verified:** seed dry-run passes, all link references resolve, and a full-repo sweep confirms
  every Airtable-side function named is one of the JD's five or an explicitly-labeled capability.

## [v2.4] — 2026-07-27 · `bcd7616` — Add the full play library
*3 files · +440*

- **Added** [`docs/05-play-library.md`](docs/05-play-library.md): all eight plays written out in
  full, where previously they existed only as a one-row-per-play table in `docs/03` and a CSV.
- **The organizing principle is the brief's** *global consistency, local customization*: each play
  splits into **the standard** — constraint, trigger, partner, artifact, signal, changed in the
  monthly retro rather than in the field — and **the latitude**, which is sequencing, framing, who
  to approach and what to say. Sequences are explicitly labeled *a default, not a mandate*.
- **Changed how "done" is written.** Definitions of done are now phrased as **signals we look for
  on the customer's side**, not as predictions of customer behavior or commitments made on their
  behalf, with a short section up front stating the distinction. A play can be run well and still
  not reach its signal — that's information for the retro, not a failed CSM.
- **Also added:** what's deliberately *not* a play (the QBR, the exec dinner, the training webinar,
  "increase adoption", the health-score save); how the library is added to and retired, including
  the override-rate check on the mechanism itself; and the honest gaps — 5 of 8 plays have a built
  artifact template, and the bars are demanding enough that I'd expect to revise one within two
  quarters.
- Account specifics were kept light and consolidated into a single summary table, so the plays read
  as reusable rather than bespoke to these six accounts.

## [v2.3] — 2026-07-24 · `e810f33` — Human review pass on the brief (PR [#1](https://github.com/magellen12/airtable-take-home/pull/1))
*1 file · +74 / −79 — three review commits, merged with history preserved.*

Run as a pull request on purpose: the agent-drafted vs. human-edited diff is itself an artifact of
how I work with AI.

- **`beea6a1`** — agent-proposed revision applying a people-manager lens to priority 3, flagged as
  proposed rather than adopted.
- **`1e6ee98`** — my round-2 additions: the team-engagement lens; the observation that **the team
  has the book's own pathology** (fifteen tenured CSMs "connected on the org chart, not in
  practice"); and the **global consistency, local customization** principle — *consistency is the
  floor, not the ceiling.*
- **`fd117b4`** — trimmed 1,315 → 1,030 words to hold the ~1.75-page target. Cut hedges and
  redundant examples, kept every concept.

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
- **Verified:** seed dry-run passes (84 records, all links resolve); ARR-at-risk recomputed to
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
