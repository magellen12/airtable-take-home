# Omni build brief — HTCS Transformation OS

Instructions written for **Airtable Omni** (the AI app builder) to construct this base. Paste
the numbered prompts into Omni **one at a time, in order**, verifying each before moving on.

This is the Omni-driven alternative to the human [`build-checklist.md`](build-checklist.md) and
the [`../scripts/`](../scripts/) API script. The canonical spec is still
[`schema.md`](schema.md) and [`ai-components.md`](ai-components.md) — if Omni and those files
disagree, **the spec files win.**

---

## How to use this

1. Create a new base → **"Build an app with Omni"** → paste **Prompt 1**.
2. Work through Prompts 2–6 in order. Omni builds iteratively; small focused prompts beat one
   giant one.
3. After each prompt, run the **check** beneath it before continuing.
4. Load the seed data (Step A, below) once the structure from Prompt 1 exists.

### What Omni is good at vs. what you must verify

| Omni does this well | Verify / fix by hand |
|---|---|
| Creating tables, fields, links, select options | **Formula syntax** — paste the exact formulas from Prompt 3; Omni often approximates them |
| Building interface layouts from a description | **AI-field prompts** — paste verbatim from Prompt 4; do not let Omni paraphrase them |
| Drafting automations | **Lookup/rollup wiring** — the dependent formulas (ARR at Risk, Renewal Readiness) only work once their source lookups exist |
| Renaming / reshaping after the fact | **Select-option exactness** — option spelling must match the CSVs or import fails |

> **The single most important correction to watch:** Omni will want to score Voltaic as a mature
> Stage 4 account and to treat Meridian's blocker as "Governance." Both are wrong by design —
> see the checks in Prompt 4 and the verification section. If Omni "helpfully" changes these,
> change them back.

---

## Step A · Load the seed data

Two options — pick one:

**A1 — Structure-first (recommended).** After Prompt 1 creates the tables, import each CSV in
[`data/`](data/) into its matching table (**Import → CSV**, per table), in this order so links
resolve: `csms → plays → accounts → diagnostics → stakeholders → signals → value-stories →
account-plays`. Because Prompt 1 uses the **exact field names** in the CSV headers, columns map
1:1. Fix any column Airtable imported as text but should be a rating/number/date/select.

**A2 — Data-first.** Skip Omni for structure: import the 8 CSVs directly (they auto-create the
tables as text fields), then use Prompts 3–6 to add formulas, AI fields, automations and
interfaces on top. Faster to first data, but you convert every field type by hand.

Either way, the `CSMs.Paired With` self-links (Marcus ↔ Ben) are set manually — 2 records.

---

## Prompt 1 — build the tables and fields

> Paste everything in the box into Omni.

```
Build a Customer Success operating base called "HTCS Transformation OS". It runs an AI
transformation methodology across a book of enterprise accounts. Create these 8 tables with
exactly these fields and field names. Do NOT add extra fields. Where I mark a field as a
formula, lookup, rollup, or AI field, just create a placeholder text field for now — I will
configure those in a later step.

TABLE 1 — "Accounts" (primary field: Account)
- Account: single line text
- Function: single line text
- ARR: currency, USD, 0 decimals
- Seats: number, integer
- Contract Stage: single select — options: First year, Mid-term, Renewal cycle
- Quarters to Renewal: number, integer
- CSM: link to CSMs
- Current Diagnostic: link to Diagnostics
- Notes: long text
(Placeholders — leave as text for now: Stage, Constraint, Value Evidence Score, Diagnostic Age (days),
 Threads Mapped, Exec Sponsor Named, Sponsor Roles, Latest Value Story Status, ARR at Risk, Renewal Readiness)

TABLE 2 — "Diagnostics" (primary field: Diagnostic ID)
- Account: link to Accounts
- Diagnostic Date: date (ISO)
- Run By: link to CSMs
- Sponsorship: rating, max 5
- Sponsorship Evidence: long text
- Governance: rating, max 5
- Governance Evidence: long text
- Adoption: rating, max 5
- Adoption Evidence: long text
- Value Evidence: rating, max 5
- Value Evidence Notes: long text
- Play Accepted: single select — options: Accepted, Overridden, Pending
- Override Reason: long text
- Session Notes: long text
(Placeholders — leave as text for now: Diagnostic ID, Average, Lowest Score, Constraint, Stage,
 Stage Rationale, Recommended Play)

TABLE 3 — "Plays" (primary field: Play)
- Play: single line text
- Code: single line text
- Clears Constraint: single select — options: Sponsorship, Governance, Adoption, Value Evidence
- Applies at Stage: multiple select — options: 0, 1, 2, 3, 4
- CSM Owns: long text
- Partner Leads: multiple select — options: Professional Services, Security & Risk, Product, Sales, Renewals, Value Validation, Support
- Artifact Produced: long text
- Definition of Done: long text
- Typical Duration (wks): number, integer
- First Three Moves: long text
- Template Status: single select — options: Templated, Specified

TABLE 4 — "Account Plays" (primary field: Name)
- Account: link to Accounts
- Play: link to Plays
- Owner: link to CSMs
- Partner Engaged: multiple select — options: Professional Services, Security & Risk, Product, Sales, Renewals, Value Validation, Support
- Status: single select — options: Not started, In flight, Blocked, Done — DoD met, Abandoned
- Start Date: date
- Target Date: date
- Completed Date: date
- Outcome: long text
- Evidence: attachment
(Placeholders — leave as text: Name, Cycle Time (days), Over Cycle Time)

TABLE 5 — "Value Stories" (primary field: Value Story)
- Value Story: single line text
- Account: link to Accounts
- Use Case: single line text
- Business Metric: single select — options: Cost, Cycle time, Revenue, Risk/Compliance, Capacity
- Baseline: single line text
- Current: single line text
- Quantified Impact: single line text
- Source of Truth: long text
- Audience: single select — options: CFO, COO, CIO, Procurement, BU Leader, Ops Lead
- Status: single select — options: Draft, Reviewed, Customer-validated, Stale
- Validated By: single line text
- Date Validated: date
(Placeholders — leave as text: Narrative, Age (days), Freshness)

TABLE 6 — "Stakeholders" (primary field: Name)
- Name: single line text
- Account: link to Accounts
- Title: single line text
- Role: single select — options: Exec Sponsor, Economic Buyer, Champion, Builder, Blocker, User Lead
- Sentiment: single select — options: Advocate, Supportive, Neutral, Skeptical, Opposed
- Last Touch: date
- Status: single select — options: Active, Departed, Unengaged
- Notes: long text

TABLE 7 — "Signals" (primary field: Signal)
- Signal: single line text
- Account: link to Accounts
- Type: single select — options: Adoption, Support, Commercial, Engagement, Governance
- Direction: single select — options: Positive, Neutral, Negative
- Date: date
- Detail: long text
- Weight: number, integer

TABLE 8 — "CSMs" (primary field: Name)
- Name: single line text
- Tenure (months): number, integer
- Strength Profile: multiple select — options: Relationship, Technical/Builder, Executive, Commercial, Governance
- Builder Depth: rating, max 5
- Executive Presence: rating, max 5
- Domain: rating, max 5
- Paired With: link to CSMs (self-link)
- Development Focus: single line text
- Plays Authored: number, integer
(Placeholders — leave as text: Book ARR, Diagnostics Run, DoD Hit Rate)
```

**Check:** 8 tables exist; every link field connects the right two tables; select options match
the spelling above exactly (Airtable is case- and punctuation-sensitive on import). Now do
**Step A** to load the CSVs.

---

## Prompt 2 — helper lookups and rollups

> These must exist *before* the formulas in Prompt 3, because several formulas read them.

```
On the base we just built, create these lookup, rollup and count fields:

On "Accounts":
- Stage: lookup from Current Diagnostic → Stage
- Constraint: lookup from Current Diagnostic → Constraint
- Value Evidence Score: lookup from Current Diagnostic → Value Evidence
- Diag Date: lookup from Current Diagnostic → Diagnostic Date
- Threads Mapped: count of linked Stakeholders
- Sponsor Roles: rollup of Stakeholders → Role, using ARRAYJOIN(values, ",")
- Latest Value Story Status: rollup of Value Stories → Status (use MAX to surface the most advanced), or if that's awkward, the Status of the most recent by Date Validated

On "CSMs":
- Book ARR: rollup of Accounts → ARR, SUM
- Diagnostics Run: count of linked Diagnostics
```

**Check:** on the Floor & Board account row, `Stage`, `Constraint` and `Value Evidence Score`
populate from its July 2026 diagnostic (if blank, set `Accounts.Current Diagnostic` to that
diagnostic record first).

---

## Prompt 3 — the formulas (paste exactly; do not let Omni rewrite them)

> Ask Omni to convert each placeholder to a formula field with **this exact formula**. If Omni's
> syntax differs, open the field and paste the formula text yourself.

```
Convert these placeholder fields to formula fields with exactly these formulas.

Diagnostics.Diagnostic ID =
  {Account} & " · " & DATETIME_FORMAT({Diagnostic Date}, "YYYY-MM")

Diagnostics.Average =
  ROUND(({Sponsorship}+{Governance}+{Adoption}+{Value Evidence})/4, 2)

Diagnostics.Lowest Score =
  MIN({Sponsorship}, {Governance}, {Adoption}, {Value Evidence})

Diagnostics.Constraint =
  IF({Sponsorship} = {Lowest Score}, "Sponsorship",
  IF({Adoption} = {Lowest Score}, "Adoption",
  IF({Value Evidence} = {Lowest Score}, "Value Evidence", "Governance")))

Accounts.Diagnostic Age (days) =
  DATETIME_DIFF(TODAY(), {Diag Date}, 'days')

Accounts.Exec Sponsor Named =
  IF(FIND("Exec Sponsor", {Sponsor Roles} & "") > 0, "Yes", "No")

Accounts.ARR at Risk =
  IF(AND({Quarters to Renewal} <= 3, {Value Evidence Score} <= 2), {ARR}, 0)

Accounts.Renewal Readiness =
  IF({Quarters to Renewal} > 4, "Not yet in cycle",
  IF(AND({Latest Value Story Status} = "Customer-validated", {Exec Sponsor Named} = "Yes"), "Ready",
  IF({Latest Value Story Status} = "Customer-validated", "Value only — no sponsor",
  IF(OR({Latest Value Story Status} = BLANK(), {Latest Value Story Status} = "Stale"), "⚠️ No current value", "In progress"))))

Value Stories.Age (days) =
  DATETIME_DIFF(TODAY(), {Date Validated}, 'days')

Value Stories.Freshness =
  IF({Age (days)} > 90, "Stale", "Current")

Account Plays.Name =
  {Account} & " — " & {Code (from Play)}

Account Plays.Cycle Time (days) =
  IF({Completed Date}, DATETIME_DIFF({Completed Date}, {Start Date}, 'days'))

Account Plays.Over Cycle Time =
  IF(AND(NOT({Completed Date}), DATETIME_DIFF(TODAY(), {Start Date}, 'days') > {Typical Duration (wks) (from Play)} * 7), "⚠️ Over", "OK")
```

**Check (do the arithmetic):** `Diagnostics.Constraint` must read **Value Evidence** for
Meridian (its lowest score is 2), **Sponsorship** for Floor & Board, **Adoption** for TrailLine,
**Governance** for Voltaic. `Accounts.ARR at Risk` must total **$3,110,000** across Floor &
Board, Corvus and Voltaic. If either is off, a lookup is pointing at the wrong field.

---

## Prompt 4 — the AI fields (paste the prompts verbatim)

> The full prompts live in [`ai-components.md`](ai-components.md). Have Omni create three AI
> fields; paste each prompt **exactly**, including the CRITICAL RULE lines — those are what stop
> the model making the two signature mistakes. `{Field}` tokens must be inserted as real field
> references, not typed as literal text.

```
Create three AI-powered fields. For each, I will paste the exact prompt — use it verbatim.

1) On "Diagnostics", field "Stage" (plus a companion "Stage Rationale"): use the AI-1 prompt
   from ai-components.md. It classifies an AI-transformation stage 0–4 from the four scores.
   CRITICAL: it must enforce "Stage 4 requires Governance >= 4" — a fast-building, low-governance
   customer is Stage 2, not Stage 4.

2) On "Diagnostics", field "Recommended Play": use the AI-2 prompt. It maps the binding
   constraint to a play. CRITICAL: it must apply the audience rule — a Value-evidence constraint
   blocked by a review board routes to P5 (a risk-and-controls case), not P4.

3) On "Value Stories", field "Narrative": use the AI-3 prompt. It writes a value narrative in
   the buyer's language. CRITICAL: it must return "INSUFFICIENT EVIDENCE — need: ..." rather
   than invent any number the source fields don't contain.
```

**Check — run these three, they are the demo:**
- **AI-1 on Voltaic → must return Stage 2, not Stage 4.**
- **AI-2 on Meridian → must return P5 (Governance Case); on Harbor Lane → P1 (Prove One Thing).**
- **AI-3 on Corvus → a CFO-language paragraph; on Floor & Board → `INSUFFICIENT EVIDENCE`.**

If any of these come out differently, the prompt was paraphrased — repaste it verbatim from
`ai-components.md`.

---

## Prompt 5 — the automations

```
Create three automations.

A1 "Current diagnostic": when a Diagnostics record is created, set that record's Account →
Current Diagnostic to this new record.

A2 "Renewal value alert": every day at 07:00, find Accounts where Quarters to Renewal <= 2 AND
(Latest Value Story Status is not "Customer-validated" OR Freshness is "Stale"). For each, if it
has no open Account Play for "P8 · Renewal Value Review", create one, and notify the account's
CSM. (On the seed data this should flag Floor & Board and Voltaic.)

A3 "Evidence enforcement": when a Diagnostics record is updated, if any of Sponsorship /
Governance / Adoption / Value Evidence is >= 4 AND its matching evidence field (Sponsorship
Evidence / Governance Evidence / Adoption Evidence / Value Evidence Notes) is empty, notify the
CSM that evidence is required.
```

**Check:** manually trigger A2 (or wait for 07:00) — it should create P8 Account Plays for Floor
& Board and Voltaic and no one else.

---

## Prompt 6 — the interfaces

> Full layout detail in [`interfaces.md`](interfaces.md). Build these two first; the diagnostic
> form is optional for a demo.

```
Build two interfaces.

INTERFACE 1 — "CSM Cockpit" (a record-review layout, filtered to CSM = current user):
- Left: a list of the user's Accounts sorted by ARR at Risk descending, showing ARR, Quarters
  to Renewal, Stage, Constraint, Renewal Readiness.
- Main panel for the selected account, in blocks:
  (1) the four diagnostic ratings as bars with the Constraint highlighted, plus Stage and Stage
      Rationale;
  (2) the Recommended Play with its First Three Moves and Partner;
  (3) the current Value Story with Status and Age, and a button to create one;
  (4) linked Stakeholders by Role with a thread count vs a target of 3, departed contacts shown
      struck through;
  (5) the 8 most recent Signals, coloured by Direction.

INTERFACE 2 — "Director Book Review" (a dashboard):
- Number widgets: total ARR at Risk; Value Coverage (share of accounts with a Customer-validated
  value story); Sponsor Coverage (share with an exec sponsor + 3 threads); % of Book Staged.
- A bar of Stage distribution across the book.
- A bar of Book ARR grouped by Constraint.
- A timeline of Accounts by Quarters to Renewal, coloured by Renewal Readiness.
- A grid of CSMs showing Book ARR, Builder Depth, Executive Presence, Domain, Paired With, plays
  in flight, and Plays Authored.
```

**Check:** the Director dashboard shows **ARR at Risk ≈ $3.11M**, **Value Coverage 0/6**, and a
Book-ARR-by-constraint bar where **Value evidence ($2.3M) is the tallest** — that's the whole
thesis in one chart.

---

## Final verification (the same gates as the human checklist)

| Check | Expected |
|---|---|
| `Accounts.ARR at Risk` total | **$3,110,000** (Floor & Board, Corvus, Voltaic) |
| `Diagnostics.Constraint` for Meridian | **Value Evidence** (not Governance) |
| AI-1 on Voltaic | **Stage 2** (not 4) |
| AI-2 on Harbor Lane / Meridian | **P1** / **P5** |
| AI-3 on Floor & Board | **INSUFFICIENT EVIDENCE** |
| A2 automation fires on | **Floor & Board + Voltaic** only |
| `CSMs.Paired With` | Marcus ↔ Ben set manually |

When these pass, the base matches the spec. Then: grant the recruiter **editor** access, note the
workspace ID, and complete the `[VERIFY]` checklist in
[`../appendix/how-i-used-ai.md`](../appendix/how-i-used-ai.md).

---

*If Omni struggles with any step, that step's ground truth is in [`schema.md`](schema.md)
(structure + formulas), [`ai-components.md`](ai-components.md) (AI + automations) and
[`interfaces.md`](interfaces.md) (layouts). The Python path in [`../scripts/`](../scripts/) builds
tables + data non-interactively if you'd rather not hand-build the structure at all.*
