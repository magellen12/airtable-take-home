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
| `Current Diagnostic` | Link → `Diagnostics` | The latest one; set by automation A1 |
| `Stage` | Lookup → `Current Diagnostic.Stage` | |
| `Constraint` | Lookup → `Current Diagnostic.Constraint` | |
| `Proof Score` | Lookup → `Current Diagnostic.Proof` | Surfaced on Accounts because it's the renewal predictor |
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

**`ARR at Risk`** — ARR that renews inside three quarters without proof behind it.
```
IF(AND({Quarters to Renewal} <= 3, {Proof Score} <= 2), {ARR}, 0)
```
Deliberately binary rather than a weighted score. A probability-weighted number invites
debate about the weighting; a hard "this dollar renews soon and we can't defend it" does not.
On seed data it totals **$3,110,000** — Floor & Board, Corvus, Voltaic.

**`Renewal Readiness`**
```
IF({Quarters to Renewal} > 4, "Not yet in cycle",
IF(AND({Latest Value Story Status} = "Customer-validated", {Exec Sponsor Named} = "Yes"), "Ready",
IF({Latest Value Story Status} = "Customer-validated", "Proof only — no sponsor",
IF(OR({Latest Value Story Status} = BLANK(), {Latest Value Story Status} = "Stale"), "⚠️ No current proof", "In progress"))))
```

> Floor & Board, Voltaic and Corvus all evaluate to **⚠️ No current proof** on seed data. That
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
| `Sponsorship` | Rating (1–5) | |
| `Sponsorship Evidence` | Long text | **Required for a score of 4–5.** Validated by automation A3 |
| `Governance` | Rating (1–5) | |
| `Governance Evidence` | Long text | |
| `Capability` | Rating (1–5) | |
| `Capability Evidence` | Long text | |
| `Proof` | Rating (1–5) | |
| `Proof Evidence` | Long text | |
| `Average` | Formula | `ROUND(({Sponsorship}+{Governance}+{Capability}+{Proof})/4, 2)` — displayed *only* to demonstrate that it's the wrong number to manage by |
| `Lowest Score` | Formula | `MIN({Sponsorship}, {Governance}, {Capability}, {Proof})` |
| `Constraint` | Formula | The constraint rule. See below |
| `Stage` | AI field | → [`ai-components.md`](ai-components.md#ai-1) |
| `Stage Rationale` | AI field | Same call as Stage |
| `Recommended Play` | AI field | → [`ai-components.md`](ai-components.md#ai-2) |
| `Play Accepted` | Single select | `Accepted` · `Overridden` · `Pending` — **the model-quality metric** |
| `Override Reason` | Long text | Every override is training data for the next version of the prompt |
| `Session Notes` | Long text | Raw notes from the customer session; input to the agent |

**`Constraint`** — ladder order `Sponsorship → Capability → Proof → Governance`, with the
Stage 0 exception applied by the AI field when it classifies stage.
```
IF({Sponsorship} = {Lowest Score}, "Sponsorship",
IF({Capability} = {Lowest Score}, "Capability",
IF({Proof} = {Lowest Score}, "Proof", "Governance")))
```

---

## 3 · `Plays`
The library. 8 records, seeded from [`data/plays.csv`](data/plays.csv).

| Field | Type | Notes |
|---|---|---|
| `Play` | Single line text | Primary. "P4 · Quantify & Translate" |
| `Code` | Single line text | `P4` |
| `Clears Constraint` | Single select | `Sponsorship` · `Governance` · `Capability` · `Proof` |
| `Applies at Stage` | Multiple select | `0`–`4` |
| `CSM Owns` | Long text | |
| `Partner Leads` | Multiple select | `Solutions/SE` · `Trust & Security` · `Product` · `AE` · `Value Eng` · `Support` |
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
| `Name` | Formula | `{Account Name} & " — " & {Play Code}` |
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
| `Development Focus` | Single line text | What I'm coaching them on |
| `Accounts` | Link → `Accounts` | |
| `Book ARR` | Rollup → `Accounts.ARR` (SUM) | |
| `Diagnostics Run` | Count → `Diagnostics` | |
| `Plays Authored` | Number | **How leads surface** |
| `DoD Hit Rate` | Formula / manual | % of plays closed at Definition of Done |

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
