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

## [v3.4] — 2026-08-04 — Session prep: what the base actually looks like on demo day
*2 files*

Rehearsal pass over [`session/`](session/) two days before the live session, checking the demo
against the base rather than against the plan. Three things were wrong about the *run*, not about
the argument.

### Changed

- **The live AI generation moved from Corvus to Floor & Board.** The pre-flight said *"one AI
  generation held back to run live, not pre-generated."* That isn't true: **all six narratives are
  already generated**, so beat 5 was a regeneration, not a generation. Direction matters, because
  Corvus's current output is the strongest artifact in the build — it produces the CFO-ready numbers
  and then reports `CONFIDENCE: Low`, disclosing that the figures are "an illustrative seed value
  not yet reconciled against platform run logs." Re-rolling that in the room is a coin flip on
  whether the disclosure survives. Floor & Board has genuinely no evidence, so it refuses every
  time and only the wording varies. **Show Corvus, generate Floor & Board.**
- **The three structural patterns now name which account proves each one.** The beat said "give one
  account as evidence for each" without saying which, which is a decision you don't want to be
  making live. Now Corvus for value realization, Floor & Board for person-dependence (*"the roadmap
  left with her"*, verbatim from the stakeholder record), TrailLine for no readiness model.
- **Added the empty-fields answer to [`qa-prep.md`](session/qa-prep.md).** `Play Accepted` is unset
  on all six diagnostics, value coverage is 0 of 6, `Plays Authored` is 0 of 6, and five of six
  narratives carry a stale flag. Each is a baseline rather than a gap, and each has a one-line
  answer now. **Do not populate them to look finished** — a dashboard with invented coverage is
  what this argument exists against.

### Verified

- **Two fields hidden in the base, neither deleted, deliberately.** `CSMs.From field: Paired With`
  is the reciprocal half of a link whose other half is a live column on the Director Review skills
  matrix, and its data is fully duplicated, so there was nothing to reclaim.
  `Diagnostics.Diagnostic` turned out to have a **live interface dependency** on the *Inbox:
  Accounts Detail* record page; Airtable warns that field deletion is undoable but dependency
  changes are not. Hiding a field does **not** remove it from an interface that displays it, so
  the field stays blank-but-present on that page. Cost of leaving it: nothing, on a page unlikely
  to be opened.
- **Already done, and no longer on any list:** the `zz Applies at Stage` field is gone from `Plays`,
  and `Accounts.Diagnostic (from Current Diagnostic)` does not exist.

---

## [v3.3] — 2026-07-29 · `ed46d6e` — The build corrected the documents
*8 files · +tools/pdf*

Interface 1, Interface 2 and the diagnostic session form all got built this round, and building
them falsified things the documents asserted. This entry is mostly a list of those. The most
important one is in the brief's first paragraph.

### Changed

- **The value-evidence claim in the brief was wrong.** [`docs/01`](docs/01-strategic-brief.md) said
  all three at-risk accounts *"sit at 1 of 5 on value evidence."* Read live from the base:
  **Floor & Board 1, Corvus 1, Voltaic 2.** The **$3.11M / 61%** figure is unaffected, because
  `Accounts.ARR at Risk` fires at `Value Evidence Score <= 2` rather than at 1 — so the headline
  survived a claim that didn't. Now stated as *"none of that ARR scores above 2 of 5, and $2.59M of
  it sits at 1."* Same force, one more real number, and it matches a base the reader can open. Fixed
  in the brief, the PDF source, [`README.md`](README.md), [`AGENTS.md`](AGENTS.md) and the talk
  track, and the PDF was regenerated.
- **The talk track claimed an automation fired.** Beat 7 said A2 *"fired on Floor & Board and
  Voltaic the morning I stood this up."* **No automations are built in this base.** The two
  `Account Plays` rows whose `Outcome` reads "Auto-created by automation A2" are seed data. Beat 7
  is now the diagnostic session form, which answers the *"where do the scores come from"* question
  the demo previously left open, and A1, A2 and AG-1 are all labelled **specified, not built**.
- **Two smaller unsourced claims in the talk track.** Floor & Board's *"one thread mapped"* was
  two; what it actually has none of is an exec thread, which is the P2 target on the stakeholder
  record. And Corvus's *"seven-figure expansion"* was a number that appears nowhere in the base —
  now *"enterprise-wide rollout off a single contained business unit,"* which the account notes
  support.
- **[`schema.md`](airtable-build/schema.md)** described `Current Diagnostic` as *"set by automation
  A1"* in the present tense. A1 is specified, not built.
- **The interface guides were wrong in four places**, all found by building against them:
  Number elements can't sum a money field or render a fraction, so ARR at Risk needs a grid with
  the column total switched on; a Timeline was impossible because `Accounts` has **no date field at
  all**; the empty Stage 4 bar can't render, because a chart's categories are the distinct values
  present in a formula-derived lookup; and interfaces can't read across a link, so anything on
  `Diagnostics` has to be exposed as a lookup on `Accounts` first.

### Kept

- **Requiring all ten form fields**, but for a corrected reason — see Verified. The line to say out
  loud is unchanged: making the four evidence fields required is what stops a score being an
  opinion.
- **Grouping charts by a lookup field.** Flagged as a risk, tested, works. No flattening formula
  fields were added to the base and none are needed.
- **`session/` stays in the deliverable.** [`README.md`](README.md) advertises it and a written run
  of show is evidence of how this role would be run. Two lines that described managing the room
  rather than making the argument were softened instead.

### Verified

- **The blank-rating claim was wrong in both directions, and is now measured.** An early draft
  required only the four evidence fields. The correction to it claimed a blank rating reads as `0`
  and yields a confidently wrong constraint and play. Tested by submitting throwaway diagnostics
  and reading back what computed: **`MIN` skips blanks**, so `Lowest Score` and `Constraint` stay
  correct. The real damage is `Average`, which divides by a fixed `4` and so silently deflates
  (2.25 reported where the mean of the scores given was 3.00), and **both AI fields, which stop on
  `emptyDependency`** and leave `#ERROR!` where the Cockpit expects a stage. Require all four
  ratings because a blank yields a *dead* record, not a wrong one.
- **`Diagnostics` has two links to `Accounts`, and the plural one corrupts the account.** `Account`
  is the history link and belongs on the form. `Accounts` is the reciprocal of
  `Current Diagnostic`, and setting it from the diagnostic side **appends rather than replaces**: a
  test record left TrailLine with two current diagnostics, `Constraint` reading `Adoption, Adoption`
  and **`ARR at Risk` at `#ERROR!`**. So promoting a diagnostic is not one link field, which is the
  honest reason A1 is an automation rather than a form field.
- **No drift in the numbers.** After every test record was deleted: 6 accounts, 6 diagnostics,
  ARR **$5,060,000**, ARR at Risk **$3,110,000 (61.5%)**, sponsor coverage 2 of 6, value coverage
  0 of 6, every account on exactly one current diagnostic, no error cells.
- **What could not be verified, stated as such.** Airtable exposes no API for interfaces or
  automations, so all three interfaces and the absence of automations rest on the builder's word,
  not on a check. `Diagnostic Date` "defaults to today" could not be confirmed either.

### Also audited: `session/qa-prep.md`

Never checked against the live base before. 212 lines, four errors, all in claims about what the
build does rather than in the judgment calls.

- **The sequencing examples didn't match the base.** *"Floor & Board is Sponsorship then a CoE,
  Corvus is Value evidence then Adoption."* Live: Floor & Board sequences **P8 Renewal Value
  Review**, not a CoE, and Corvus returns **`ALSO SEQUENCE: None`**. Both examples were offered as
  proof that the system sequences, in an answer conceding the lowest-score rule is crude — so both
  would have failed if checked. Now stated as the base has it, plus the real gap volunteered:
  Floor & Board has governance at 1 and no CoE and the model doesn't sequence a governance play
  there. The same wrong CoE claim was in **talk track beat 4** and is fixed there too.
- **The four-dimensions answer used the wrong account for adoption.** It cited *"Harbor Lane on
  adoption and awareness"*; Harbor Lane's adoption is **2** and its binding constraint is **value
  evidence**. It also left governance unexemplified while citing value evidence twice. Now:
  Floor & Board on sponsorship, **TrailLine** on adoption (1, and its constraint), **Voltaic** on
  governance (1, and its constraint), Meridian and Corvus on value evidence for different audiences.
  Four dimensions, four accounts, each one the binding constraint.
- **"Evidence is required for any 4 or 5"** understated the build. The form requires evidence for
  **every** score; Airtable's required toggle isn't conditional. Corrected upward.

### Verified in `qa-prep.md`, and left alone

Checked and correct: Voltaic's 5 adoption / 1 governance / **2** value evidence; Meridian's 3.5
average, $1.1M, four quarters, sponsorship 5, value-evidence constraint; TrailLine's sponsorship 3;
Floor & Board's $1.7M, two quarters, no exec sponsor, and champion departed three months;
**P3, P5 and P7 are the three plays without a built template**, exactly as claimed; `Source of
Truth`, `Validated By` and the `Draft → Reviewed → Customer-validated` status ladder all exist as
described; only Corvus carries a quantified impact and all six value stories are `Draft`, so *"the
value narratives are mostly empty and only Corvus has numbers"* is accurate; value coverage 0 of 6;
Marcus (builder 5, exec 2) and Ben (exec 5, builder 2) are paired both directions, which is the
TrailLine pairing answer; and Voltaic's *"agents nobody owns and worried about cost"* is near-verbatim
from a `Signals` record rather than an embellishment.

*Not changed, flagged only:* `qa-prep` still says GRR, NRR and stage progression *QoQ*, which
[v3.2](#v32--2026-07-29--de586b9--answer-the-assessments-own-bullets) deliberately removed from the
brief as unexplained. Defensible as spoken vocabulary in a live Q&A where the brief has to stand
alone, so it stays a known inconsistency rather than a silent one.

### Swept the same four errors out of the files that weren't in the first pass

Fixing a claim in one file and leaving it in three others is how the invented org chart survived
nine files last time, so after merging the above I grepped for each corrected phrase across the
whole repo. Four more hits:

- **[`docs/03:65`](docs/03-transformation-methodology.md)** carried the same unsourced
  *"seven-figure expansion"* for Corvus. This one mattered more than the talk track's, because
  `docs/` is a deliverable.
- **[`schema.md:168`](airtable-build/schema.md)** said `Freshness` *"drives automation A2"*, present
  tense. Now "the trigger A2 would read. A2 is specified, not built."
- **[`interfaces.md:54`](airtable-build/interfaces.md)** carried the *"one thread mapped"* error, and
  also had the CSM **clicking an Accept button that doesn't exist** — buttons were dropped from the
  Cockpit in favour of opening the record, which is the more defensible design anyway, since
  `Constraint Override` challenges the formula and `Play Accepted` challenges the AI and both need
  the record. The walkthrough now says so, and notes that lookups are read-only so neither is
  editable from the Accounts page.

Confirmed clean afterwards: no file still claims all three at-risk accounts sit at 1 of 5, that A1
or A2 runs, that Corvus's expansion has a figure attached, or that Floor & Board has one thread.

### Also

- **[`AGENTS.md`](AGENTS.md) §4 was itself a stale number**, which is the failure §5 of the same file
  exists to prevent. It claimed a ~1,025-word body plus a ~60-word header, ~1,090 total, ~1.75 pages.
  Recounted: **~1,140-word body, ~60-word header, 1,213 words rendered, filling 2 pages.** The
  assessment allows 1–2, so there is no room left, and §4 now says to recount rather than quote it.
- **Removed the stale second PDF from the repo root.** `Mauger-Strategic-Brief-*.pdf` was the older
  pre-v3.2 text, still carrying the unexplained NRR/QoQ and lacking the owns-vs-partner line and the
  expansion mechanism. It was never the file submitted, and having two similarly-named briefs sitting
  together was a send-the-wrong-one risk. Both were gitignored, so this doesn't appear in the diff.
- **`tools/pdf/` is now tracked.** It was untracked, which meant the brief's presentation variant
  (`brief-plain.md`, the PDF's source, em dashes removed) lived outside the repo — so a content
  correction could silently land in only one of the two files. That is exactly what this entry
  corrects, so the toolchain belongs under version control. Regenerated PDF: 2 pages, 1,213 words,
  zero em or en dashes.

---

## [v3.2] — 2026-07-29 · `de586b9` — Answer the assessment's own bullets
*1 file · +14 / −12*

Audited [`docs/01`](docs/01-strategic-brief.md) against the three things the assessment says the
brief **must make clear**, rather than against my own sense of whether it read well. Two were short.

### Changed

- **"How value realization connects to renewal *and expansion* outcomes."** Renewal had a stated
  mechanism; expansion was asserted twice in passing and never explained. The
  dated-value-narrative paragraph was defining a term rather than doing work, so it now carries
  both: renewals because the date makes staleness visible and the base flags it, expansions
  because procurement only argues about scope once value is settled. Corvus is the grounded case
  ([`docs/03:165`](docs/03-transformation-methodology.md),
  [`docs/02:153`](docs/02-book-diagnosis.md)) — *"everything a large expansion needs except the
  sentence that makes it purchasable."*
- **"What CSMs own versus partner on."** The brief asserted a *"clear CSM-owns-vs-partners line"*
  and never drew it. Now drawn, straight from the table in
  [`docs/04`](docs/04-operating-model.md): the CSM always owns the diagnostic, sponsor map, value
  narrative and plan; partners lead solution architecture, the commercial path, and the
  quantitative backing for any number that reaches a CFO. Named partners are drawn from the five
  the role names; *value validation* stays an italic capability per [`AGENTS.md`](AGENTS.md) §1.
- **Dropped `NRR` and `QoQ`.** Neither appears anywhere in the assessment — which says *"retention
  and expansion"* — and neither was spelled out on first use, which §4 requires. `NRR` does appear
  in [`docs/04:132`](docs/04-operating-model.md) and
  [`session/qa-prep.md:138`](session/qa-prep.md), so it wasn't invented; it was just unexplained in
  the one document a stranger reads first.

### Funded by

- Trimming the skills-matrix illustration in Priority 3. The pairing concept and the matrix
  survive; the TrailLine builder-CSM example does not. Priority 3 still carries the two §4 threads
  — the diagnostic as coaching instrument, and leads surfacing through play authorship.

### Verified

- **1,195 words**, still two pages. Every load-bearing figure unchanged; both required threads
  present; zero bare `P1`/`P2`/`P3`; no invented organizational names. Checked by script.

## [v3.1] — 2026-07-29 · `04dce43` — Define the terms a first-time reader can't infer
*1 file · +26 / −24*

Read as a standalone document — which is how a recruiter receives it — the brief leaned on terms
it never introduced, and committed to a few things I haven't decided.

### Changed — defined on first use

- **The 1–5 scale and the four dimensions**, before any score is quoted. Worth stating plainly:
  the scale is **mine, not the assessment's**. The assessment asks only for *"a scored assessment
  and recommended plays"*; the four dimensions are defined in
  [`docs/03`](docs/03-transformation-methodology.md). The brief was introducing both cold and then
  quoting "1 of 5" as if the reader already had the frame.
- **Staging** — one common read on how far an account has actually got.
- **"Dated value narrative"** — it means *carrying a validation date*, not *outdated*. The
  ambiguity was the whole problem; the date is the point, because it is what makes staleness
  visible against `Draft → Reviewed → Customer-validated → Stale`
  ([`docs/03:159`](docs/03-transformation-methodology.md)).

### Changed — claimed less

- **"With no manager layer I have no shared language"** read as though nobody manages the team.
  Fifteen CSMs report to me directly, with no managers in between —
  [`docs/04:4`](docs/04-operating-model.md) already had it right.
- **"the manager roles I fill at day 90"** → knowing who the candidates are and whether the roles
  are warranted. I may not fill them.
- **"inspect weekly"** → *on a regular cadence*; and the **weekly book review and peer-authored
  play library** are now *a shared place to see each other's accounts and reuse what works*. Both
  named a commitment I haven't made, and the second introduced two artifacts with no context.
- **"I grade the account *with* the CSM, never the person"** never said what that protects: the
  score measures the account's maturity, not the owner's performance, which is what makes honest
  scoring safe.
- **"as the strongest's"** → *the most experienced CSM's account*.

### Changed — cut for room

- **The Voltaic trap paragraph.** This **reverses [v2.2](#v22--2026-07-24--9bedf3b--tighten-the-brief-to-12-pages)**,
  which kept it through a much larger trim. Logged rather than quietly dropped, per
  [`AGENTS.md`](AGENTS.md) §6. What's lost is *"seat growth without CS influence isn't health;
  it's a customer that's priced us as a tool"* — Voltaic still appears three times.
- *"A methodology in a doc dies the way Floor & Board's backlog did."*
- The `(days 1–30 / 15–60 / 30–90)` parentheticals.

### Verified

- **Every load-bearing figure unchanged** — $5.06M, $3.11M/61%, 1 of 5, 3.2, 1.3, 1.5, 2/6, 0/6,
  avg 3.5, avg 2.25 — checked by script, not by eye.
- **Both required threads survive** ([`AGENTS.md`](AGENTS.md) §4): the people-manager lens and
  *consistency is the floor, not the ceiling*. Zero bare `P1`/`P2`/`P3`.
- **No invented organizational facts** ([`AGENTS.md`](AGENTS.md) §1). Specifically **not** written:
  a cause or date for the manager layer's departure. The assessment says only that the team
  *"recently lost its manager layer"*, and [`session/qa-prep.md:210`](session/qa-prep.md) still
  lists *"reorg, attrition, or performance"* as an open question to ask.
- **1,138 words**, still inside the 1–2 page bound of §4.

### Not in this change

- A **PDF rendering** of the brief now exists for recruiter distribution, carrying these same
  eleven clarifications with the em dashes removed. It is a **presentation variant only** and is
  deliberately not committed — `.gitignore` covers `*.pdf`. This document remains the source.

## [v3.0] — 2026-07-29 — Build the base, and let it correct the documents
*11 files*

The first version where the deliverable was executed rather than specified. Everything below was
found by running the spec against real records — none of it was visible on paper.

### Verified

- **All three AI fields pass every gate**, run live on `appFGgbrUOs62IndE`: Voltaic returns Stage 2
  not 4 · Floor & Board returns `INSUFFICIENT EVIDENCE` · Corvus invents no figures · Harbor Lane
  returns P1 · Meridian returns P5 not P4 · **ARR at risk $3,110,000 of a $5,060,000 book**.
- **The `[VERIFY]` banner is gone** from [`appendix/how-i-used-ai.md`](appendix/how-i-used-ai.md),
  replaced with results — including the answer to assumption 7, which was flagged unverified on
  purpose.

### Changed — the base corrected the docs

- **Sponsor coverage is 2 of 6, not 1 of 6.** Meridian *and* TrailLine both clear the published
  definition. The number was wrong in four places. TrailLine qualifies on the letter of it while
  its three threads are skeptical ops users — [`docs/04`](docs/04-operating-model.md) now says so
  rather than tightening the definition until it returned the answer already written down.
- **The Cockpit's left rail was missing an account.** [`interfaces.md`](airtable-build/interfaces.md)
  listed five; the book has six. **Meridian** — $1.1M, the second-largest account — sorts last on a
  $0 column, which is exactly how it went missing. Restored, with the note that it sits one quarter
  outside the at-risk gate: if its value position holds, $3.11M → $4.21M.
- **The Director's inspection queue is empty on seed data, and that's correct.** Nothing is past
  cycle time, every diagnostic is days old, no override is pending, and every score ≥4 already
  carries evidence. Rendered as four empty grids it reads as broken; rendered as one line it reads
  as true. `DoD hit rate` and `plays over cycle time` are cut — zero plays are completed, so both
  are undefined.
- **`Account Plays` had a blank primary field on every record.** Its formula referenced
  `{Account Name}` and `{Play Code}`, neither of which existed. Both added.
- **`Exec Sponsor Named` was counting departed and unengaged sponsors** — Floor & Board's is
  literally named "Unknown." Now conditioned on active status, which is what moves sponsor coverage.
- **`Renewal Readiness`'s published formula never fired**, because it flags blank or `Stale` and all
  six seeded stories are `Draft`. Rewritten, plus `ARRAYUNIQUE` for Floor & Board's two stories.

### Added

- **`Constraint Override` + `Constraint Override Reason`.** Harbor Lane's constraint is Value
  Evidence on the assessment's own words — *"a clear value demonstration tied to an existing use
  case"* — against a three-way score tie the formula resolves to Sponsorship. The reasoning now
  lives in the base rather than in a deck.
- **Six lookups on `Accounts`.** Interfaces cannot read across a link: a field element binds only to
  its page's source table. Everything on `Diagnostics` had to be exposed on `Accounts` before the
  Cockpit could render it. This invalidated a first draft of the build guide.
- **Three new build documents** — [`cockpit-build-guide.md`](airtable-build/cockpit-build-guide.md),
  [`director-review-build-guide.md`](airtable-build/director-review-build-guide.md), and
  [`how-data-gets-in.md`](airtable-build/how-data-gets-in.md), the last answering how context
  accumulates to inform future ratings.
- **A live-base diff section in [`schema.md`](airtable-build/schema.md)** recording every deviation
  between the spec and what was actually built.

### Kept

- **The constraint and AI-1's stage rationale disagree on four of six accounts, and both stay.**
  They answer different questions — the constraint picks the play, the rationale explains the
  stage. Resolved with labelling rather than by forcing agreement.
- **Value coverage stays 0 of 6, and `Plays Authored` stays 0 across all six CSMs.** Both are
  baselines, not gaps. The metrics that matter start at zero.
- **The Cockpit's buttons were dropped in favour of opening the record.** A CSM challenging the
  system is the point; two labelled places to disagree in writing — `Constraint Override` for the
  formula, `Play Accepted` for the AI — beat a button that only navigates anyway.

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
