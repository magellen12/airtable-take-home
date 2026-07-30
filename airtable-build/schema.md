# Schema — HTCS Transformation OS

8 tables. Every field listed with its type; formulas given verbatim.

```
   CSMs ──┐
          ├──< Accounts >──┬──< Diagnostics >──< (Plays)
Segments  │                ├──< Stakeholders
(single   │                ├──< Signals
 select)  │                ├──< Value Stories
          │                └──< Account Plays >──> Plays
```

---

## 1 · `Accounts`
The spine. One record per account.

| Field | Type | Notes |
|---|---|---|
| `Account` | Single line text | Primary field. e.g. "Floor & Board Furniture" |
| `Function` | Single line text | "Marketing Ops", "PMO & Clinical Ops" |
| `ARR` | Currency (USD, 0 dp) | |
| `Seats` | Number | |
| `Contract Stage` | Single select | `First year` · `Mid-term` · `Renewal cycle` |
| `Quarters to Renewal` | Number | Static in the prototype; CRM-sourced in production |
| `CSM` | Link → `CSMs` | |
| `Current Diagnostic` | Link → `Diagnostics` | The latest one. **Set by hand in the prototype** — automation A1 is specified, not built |
| `Stage` | Lookup → `Current Diagnostic.Stage` | |
| `Constraint` | Lookup → `Current Diagnostic.Constraint` | |
| `Value Evidence Score` | Lookup → `Current Diagnostic.Value Evidence` | Surfaced on Accounts because it's the renewal predictor |
| `Diagnostic Age (days)` | Formula | `DATETIME_DIFF(TODAY(), {Diagnostic Date}, 'days')` |
| `Threads Mapped` | Count → `Stakeholders` | Multi-threading metric |
| `Exec Sponsor Named` | Formula | See below |
| `Active Plays` | Link → `Account Plays` | |
| `Value Stories` | Link → `Value Stories` | |
| `Latest Value Story Status` | Rollup → `Value Stories.Status` (MAX by date) | |
| `ARR at Risk` | Formula | See below |
| `Renewal Readiness` | Formula | **The flag the whole base exists to produce.** See below |
| `Notes` | Long text | |

**`Exec Sponsor Named`**
```
IF(COUNTA({Sponsor Roles}) = 0, "No", IF(FIND("Exec Sponsor", ARRAYJOIN({Sponsor Roles})) > 0, "Yes", "No"))
```

**`ARR at Risk`** — ARR that renews inside three quarters without value evidence behind it.
```
IF(AND({Quarters to Renewal} <= 3, {Value Evidence Score} <= 2), {ARR}, 0)
```
Deliberately binary rather than a weighted score. A probability-weighted number invites
debate about the weighting; a hard "this dollar renews soon and we can't defend it" does not.
On seed data it totals **$3,110,000** — Floor & Board, Corvus, Voltaic.

**`Renewal Readiness`**
```
IF({Quarters to Renewal} > 4, "Not yet in cycle",
IF(AND({Latest Value Story Status} = "Customer-validated", {Exec Sponsor Named} = "Yes"), "Ready",
IF({Latest Value Story Status} = "Customer-validated", "Value only — no sponsor",
IF(OR({Latest Value Story Status} = BLANK(), {Latest Value Story Status} = "Stale"), "⚠️ No current value", "In progress"))))
```

> Floor & Board, Voltaic and Corvus all evaluate to **⚠️ No current value** on seed data. That
> is the demo's opening screen — 61% of book ARR, flagged by a formula, two quarters early.

---

## 2 · `Diagnostics`
One record per account per assessment cycle. **The instrument.** Quarterly re-baseline creates
a new record rather than overwriting, so stage movement is visible over time.

| Field | Type | Notes |
|---|---|---|
| `Diagnostic ID` | Formula | `{Account Name} & " · " & DATETIME_FORMAT({Diagnostic Date}, "YYYY-MM")` |
| `Account` | Link → `Accounts` | |
| `Diagnostic Date` | Date | |
| `Run By` | Link → `CSMs` | |
| `Sponsorship` | Rating (1–5) | Sponsorship & multi-threading |
| `Sponsorship Evidence` | Long text | **Required for a score of 4–5.** Validated by automation A3 |
| `Governance` | Rating (1–5) | Governance maturity |
| `Governance Evidence` | Long text | |
| `Adoption` | Rating (1–5) | Adoption depth |
| `Adoption Evidence` | Long text | |
| `Value Evidence` | Rating (1–5) | Quantified outcome in the buyer's language |
| `Value Evidence Notes` | Long text | |
| `Average` | Formula | `ROUND(({Sponsorship}+{Governance}+{Adoption}+{Value Evidence})/4, 2)` — displayed *only* to demonstrate that it's the wrong number to manage by |
| `Lowest Score` | Formula | `MIN({Sponsorship}, {Governance}, {Adoption}, {Value Evidence})` |
| `Constraint` | Formula | The constraint rule. See below |
| `Stage` | AI field | → [`ai-components.md`](ai-components.md#ai-1) |
| `Stage Rationale` | AI field | Same call as Stage |
| `Recommended Play` | AI field | → [`ai-components.md`](ai-components.md#ai-2) |
| `Play Accepted` | Single select | `Accepted` · `Overridden` · `Pending` — **the model-quality metric** |
| `Override Reason` | Long text | Every override is training data for the next version of the prompt |
| `Session Notes` | Long text | Raw notes from the customer session; input to the agent |

**`Constraint`** — ladder order `Sponsorship → Adoption → Value Evidence → Governance`, with the
Stage 0 exception applied by the AI field when it classifies stage.
```
IF({Sponsorship} = {Lowest Score}, "Sponsorship",
IF({Adoption} = {Lowest Score}, "Adoption",
IF({Value Evidence} = {Lowest Score}, "Value Evidence", "Governance")))
```
On seed data this yields: Floor & Board → Sponsorship, Meridian → **Value Evidence** (its lowest,
at 2 — the review-board case is a value-evidence artifact for a governance audience), TrailLine →
Adoption, Corvus → Value Evidence, Harbor Lane → Value Evidence (via the Stage 0 exception),
Voltaic → Governance.

---

## 3 · `Plays`
The library. 8 records, seeded from [`data/plays.csv`](data/plays.csv).

| Field | Type | Notes |
|---|---|---|
| `Play` | Single line text | Primary. "P4 · Quantify & Translate" |
| `Code` | Single line text | `P4` |
| `Clears Constraint` | Single select | `Sponsorship` · `Governance` · `Adoption` · `Value Evidence` |
| `Applies at Stage` | Multiple select | `0`–`4` |
| `CSM Owns` | Long text | |
| `Partner Leads` | Multiple select | `Professional Services` · `Security & Risk` · `Product` · `Sales` · `Renewals` · `Value Validation` · `Support` |
| `Artifact Produced` | Long text | |
| `Definition of Done` | Long text | **Always customer behaviour, never our activity** |
| `Typical Duration (wks)` | Number | Baseline for cycle-time measurement |
| `First Three Moves` | Long text | What the CSM does Monday morning — fed to AI field 2 |
| `Template Status` | Single select | `Templated` · `Specified` — 3 of 8 templated on purpose |

---

## 4 · `Account Plays`
Execution records. Where cycle time is measured.

| Field | Type | Notes |
|---|---|---|
| `Play ID` | Formula | `{Account Name} & " — " & {Play Code}` — **primary.** Renders `Floor & Board Furniture — P2`. Named to match `Diagnostics.Diagnostic ID`, the base's other derived primary; the `ID` suffix signals a value that's computed rather than typed. Needs the two lookups below to exist first — both were missing until 2026-07-28, which is why this field was blank on every record |
| `Account Name` | Lookup → `Accounts.Account` | via `Account`. Added 2026-07-28 |
| `Play Code` | Lookup → `Plays.Code` | via `Play`. Added 2026-07-28 |
| `Account` | Link → `Accounts` | |
| `Play` | Link → `Plays` | |
| `Owner` | Link → `CSMs` | |
| `Partner Engaged` | Multiple select | Same options as `Plays.Partner Leads` — measures partner pull-through |
| `Status` | Single select | `Not started` · `In flight` · `Blocked` · `Done — DoD met` · `Abandoned` |
| `Start Date` / `Target Date` / `Completed Date` | Date | |
| `Cycle Time (days)` | Formula | `IF({Completed Date}, DATETIME_DIFF({Completed Date}, {Start Date}, 'days'))` |
| `Over Cycle Time` | Formula | `IF(AND(NOT({Completed Date}), DATETIME_DIFF(TODAY(), {Start Date}, 'days') > {Typical Duration} * 7), "⚠️ Over", "OK")` |
| `Outcome` | Long text | |
| `Evidence` | Attachment / URL | |

---

## 5 · `Value Stories`
The renewal spine. One per quantified outcome.

| Field | Type | Notes |
|---|---|---|
| `Value Story` | Single line text | Primary |
| `Account` | Link → `Accounts` | |
| `Use Case` | Single line text | e.g. "Field agent triage — Enterprise Ops BU" |
| `Business Metric` | Single select | `Cost` · `Cycle time` · `Revenue` · `Risk/Compliance` · `Capacity` |
| `Baseline` / `Current` | Single line text | |
| `Quantified Impact` | Single line text | e.g. "$1.4M annualized" |
| `Source of Truth` | Long text | Where the number came from — **required before status can leave Draft** |
| `Audience` | Single select | `CFO` · `COO` · `CIO` · `Procurement` · `BU Leader` · `Ops Lead` |
| `Narrative` | **AI field** | → [`ai-components.md`](ai-components.md#ai-3). The buyer-language paragraph |
| `Status` | Single select | `Draft` · `Reviewed` · `Customer-validated` · `Stale` |
| `Validated By` | Single line text | The customer name who said it back |
| `Date Validated` | Date | |
| `Age (days)` | Formula | `DATETIME_DIFF(TODAY(), {Date Validated}, 'days')` |
| `Freshness` | Formula | `IF({Age (days)} > 90, "Stale", "Current")` — drives automation A2 |

---

## 6 · `Stakeholders`
Flat by design. Exists to measure multi-threading, which is the metric Floor & Board failed on.

| Field | Type | Notes |
|---|---|---|
| `Name` | Single line text | |
| `Account` | Link → `Accounts` | |
| `Title` | Single line text | |
| `Role` | Single select | `Exec Sponsor` · `Economic Buyer` · `Champion` · `Builder` · `Blocker` · `User Lead` |
| `Sentiment` | Single select | `Advocate` · `Supportive` · `Neutral` · `Skeptical` · `Opposed` |
| `Last Touch` | Date | |
| `Status` | Single select | `Active` · `Departed` · `Unengaged` |
| `Notes` | Long text | |

---

## 7 · `Signals`
Adoption, support and commercial events. Input to the AI risk summary.

| Field | Type | Notes |
|---|---|---|
| `Signal` | Single line text | Primary |
| `Account` | Link → `Accounts` | |
| `Type` | Single select | `Adoption` · `Support` · `Commercial` · `Engagement` · `Governance` |
| `Direction` | Single select | `Positive` · `Neutral` · `Negative` |
| `Date` | Date | |
| `Detail` | Long text | |
| `Weight` | Number (1–3) | Crude materiality flag |

---

## 8 · `CSMs`
The team. Fifteen in production; six seeded here.

| Field | Type | Notes |
|---|---|---|
| `Name` | Single line text | |
| `Tenure (months)` | Number | |
| `Strength Profile` | Multiple select | `Relationship` · `Technical/Builder` · `Executive` · `Commercial` · `Governance` |
| `Builder Depth` | Rating (1–5) | **Skills-matrix axis** — can they build? |
| `Executive Presence` | Rating (1–5) | **Skills-matrix axis** — credible across from a CFO? |
| `Domain` | Rating (1–5) | **Skills-matrix axis** — depth in the customer's vertical |
| `Paired With` | Link → `CSMs` (self-link) | The complement pairing — who covers this CSM's low axis on which account |
| `Development Focus` | Single line text | What I'm coaching them on |
| `Accounts` | Link → `Accounts` | |
| `Book ARR` | Rollup → `Accounts.ARR` (SUM) | |
| `Diagnostics Run` | Count → `Diagnostics` | |
| `Plays Authored` | Number | **How leads surface** |
| `DoD Hit Rate` | Formula / manual | % of plays closed at Definition of Done |

The three rating axes are the **skills matrix**. A CSM low on `Executive Presence` on an account
with hard executive dynamics is *paired*, not reassigned — the pairing is visible here so it's an
inspectable decision, not a favour. Drives the pairing logic in
[`../docs/04-operating-model.md`](../docs/04-operating-model.md#2--the-ownership-boundary-the-skills-matrix-and-pairing).

---

## Design notes

**Why `Diagnostics` is a separate table and not fields on `Accounts`.** Stage movement over
time *is* the coaching artifact. Overwriting a score destroys the only evidence I'd have that
a CSM's judgment is improving — and the quarterly re-baseline is the anti-decay mechanism for
the whole methodology.

**Why `Average` is shown at all.** It's the number a new director would instinctively manage
by, and Meridian (3.50 average, completely stuck) is standing right next to it in the same
view. The field earns its place by being visibly wrong.

**Why `Play Accepted` exists.** It's how I know whether the AI recommendation is any good.
A high override rate isn't a failure of the CSMs — it's a failing prompt, and the override
reasons are the training data for the next version of it.

**Why `Source of Truth` gates `Status`.** An AI-drafted number with no traceable source is the
single most dangerous artifact this system could produce. The field is required before a value
story can leave `Draft`.

---

## Live base — what building it actually changed

Base `appFGgbrUOs62IndE`. This section is the diff between the spec above and the base as built.
Kept honest deliberately: the corrections are part of the answer to *"what did you keep, change and
verify."*

### Fields added that this spec didn't have

| Table | Field | Why it was needed |
|---|---|---|
| `Diagnostics` | `Constraint Override` (single select) + `Constraint Override Reason` (long text) | Lets a human overrule the computed constraint **in writing**. Used on Harbor Lane |
| `Diagnostics` | `Diagnostic Age` (formula) | `DATETIME_DIFF(TODAY(), {Diagnostic Date}, 'days')`. The 90-day staleness rule needs it |
| `Diagnostics` | `Stage Label` (formula) | Extracts just the `STAGE:` line out of AI-1's two-line output |
| `Accounts` | `Adoption`, `Sponsorship`, `Governance`, `Stage Rationale`, `Recommended Play`, `Constraint Override Reason` (lookups) | **Interfaces cannot read across a link.** A field element binds only to the page's source table, so anything on `Diagnostics` had to be exposed on `Accounts` before the Cockpit could show it |
| `Accounts` | `Diagnostic Age`, `Stage` (lookups) | Same reason |
| `Account Plays` | `Account Name`, `Play Code` (lookups) | The primary-field formula references both; neither existed |
| `CSMs` | `Book ARR` (rollup) | `SUM` over linked `Accounts.ARR`. Row 3 of the Director view. Totals $5,060,000 |

### Where the live base differs from the spec above

**`Renewal Readiness`'s final branch.** The published formula flags only blank or `Stale`, but all
six seeded value stories are `Draft`, so the documented outcome never fired. The live formula ends
`IF({Latest Value Story Status} = "Reviewed", "In progress", "⚠️ No current value")`. It also needs
`ARRAYUNIQUE`, because Floor & Board has two value stories.

**`Exec Sponsor Named` counts only active sponsors.** As published it counted departed and
unengaged ones — Floor & Board's is literally named "Unknown," and Voltaic's had disengaged. The
live rollup carries a `Status is Active` condition. This is what moves sponsor coverage to 2 of 6.

**`Plays.Applies at Stage` is a multi-select `0`–`4`.** It loaded as single-line text holding ranges
(`1-2`, `0-4`); the ranges are now expanded per record.

**`Constraint` has an override branch in front of it:**
`IF({Constraint Override}, {Constraint Override}, <the nested IFs>)`. Tie-break precedence among
equal-lowest scores is **Sponsorship → Adoption → Value Evidence → Governance**.

### Fields specified here and deliberately not built

No interface reads them, and building unread fields is how a schema rots: `Threads Mapped`,
`Cycle Time (days)`, `Over Cycle Time`, `Age (days)`, `Diagnostics Run`, `DoD Hit Rate`, `Evidence`
(attachment). `DoD Hit Rate` and the cycle-time pair are additionally undefined on seed data —
**zero plays are completed**, so there is nothing to compute from.
