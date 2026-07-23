# Build checklist

Ordered steps to stand the base up. Roughly **2–3 hours** in the product. Order matters —
linked-record fields resolve by name, so referenced tables must exist first.

---

## Phase 1 · Tables and data (~45 min)

- [ ] Create base **HTCS Transformation OS** in the workspace shared with the recruiter.
- [ ] Import in **this order** — each depends on the one before:
  1. [ ] `data/csms.csv` → **CSMs**
  2. [ ] `data/plays.csv` → **Plays**
  3. [ ] `data/accounts.csv` → **Accounts**
  4. [ ] `data/diagnostics.csv` → **Diagnostics**
  5. [ ] `data/stakeholders.csv` → **Stakeholders**
  6. [ ] `data/signals.csv` → **Signals**
  7. [ ] `data/value-stories.csv` → **Value Stories**
  8. [ ] `data/account-plays.csv` → **Account Plays**
- [ ] Convert text columns to their real types per [`schema.md`](schema.md) — importing creates
      everything as text. Specifically: link fields (`Account`, `CSM`, `Play`, `Owner`),
      ratings (the four score fields), currency (`ARR`), dates, single/multi selects.
- [ ] Set `Accounts.Current Diagnostic` → the July 2026 diagnostic for each account.

## Phase 2 · Formulas (~30 min)

- [ ] `Diagnostics.Lowest Score`, `.Average`, `.Constraint`
- [ ] `Accounts.Diagnostic Age`, `.ARR at Risk`, `.Renewal Readiness`, `.Exec Sponsor Named`
- [ ] `Value Stories.Age (days)`, `.Freshness`
- [ ] `Account Plays.Cycle Time`, `.Over Cycle Time`
- [ ] Lookups/rollups: `Accounts.Stage`, `.Constraint`, `.Proof Score`, `.Threads Mapped`,
      `.Latest Value Story Status`; `CSMs.Book ARR`, `.Diagnostics Run`

**Checkpoint —** `Accounts.Renewal Readiness` should read **⚠️ No current proof** on Floor &
Board, Corvus and Voltaic, and `ARR at Risk` should total **$3,110,000**. If it doesn't, the
lookups aren't wired to the right diagnostic.

## Phase 3 · AI (~45 min)

Prompts are in [`ai-components.md`](ai-components.md) — copy verbatim, then use the `+` picker
to insert each `{Field Name}` as a real field reference.

- [ ] **AI-3 Value narrative** on `Value Stories.Narrative` — **build this first.** It's the
      demo, and it's the one that proves the refusal behaviour.
- [ ] Run it on the Corvus record → should produce a CFO-language paragraph.
- [ ] Run it on the Floor & Board record → **should return `INSUFFICIENT EVIDENCE`.** If it
      invents a number instead, rule 3 isn't landing — tighten it before going further.
- [ ] **AI-1 Stage classifier** on `Diagnostics.Stage` + `.Stage Rationale`
- [ ] Run on Voltaic → **must return Stage 2, not Stage 4.** This is the single most important
      output in the base. If it says 4, the critical rule needs strengthening.
- [ ] **AI-2 Play recommender** on `Diagnostics.Recommended Play`
- [ ] Spot-check all six against the assignments in
      [`../docs/03-transformation-methodology.md`](../docs/03-transformation-methodology.md#4--the-play-library).
      Harbor Lane is the one to watch — it must return **P1**, not a sponsorship play.
- [ ] **AG-1 Discovery agent** — optional if time is short, but it's the best live-demo moment.

## Phase 4 · Automations (~20 min)

- [ ] **A1** Current-diagnostic maintenance
- [ ] **A2** Renewal proof alert — daily 07:00. *Test it: it should fire on Floor & Board and
      Voltaic immediately.*
- [ ] **A3** Evidence enforcement on scores ≥ 4

## Phase 5 · Interfaces (~40 min)

Per [`interfaces.md`](interfaces.md).

- [ ] **CSM Cockpit** — record review, filtered to the current user. Build Dana Whitfield's
      view first; she has Floor & Board and Corvus, which is the strongest demo book.
- [ ] **Director Book Review** — dashboard. Four number widgets, stage distribution, ARR at
      risk by constraint, renewal timeline, CSM grid.
- [ ] **Diagnostic Session** — form with the 1–5 anchors visible, evidence required.

## Phase 6 · Before the session

- [ ] Grant **editor** access to the recruiter; note the workspace ID.
- [ ] Walk the demo path end to end once, timed — see
      [`../session/talk-track.md`](../session/talk-track.md).
- [ ] Have one **live AI generation** ready to run in the room. Pre-generated output looks
      like a screenshot; running it live is the part that can't be faked.
- [ ] Deliberately leave the Floor & Board `INSUFFICIENT EVIDENCE` output un-fixed. Showing the
      system refuse is stronger than showing it succeed six times.

---

## If you only have 90 minutes

Cut to the spine that still demos:

1. `Accounts` + `Diagnostics` + `Plays` only (skip Stakeholders, Signals, Account Plays)
2. `Constraint` formula + `Renewal Readiness` formula
3. **AI-3** value narrative — Corvus and Floor & Board records only
4. One interface: the CSM Cockpit

That still shows the diagnosis, the constraint mechanic, the AI drafting, and the refusal.
Everything else is depth on an argument already made.
