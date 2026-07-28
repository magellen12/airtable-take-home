# Interface 1 · CSM Cockpit — build guide

Click-by-click for Airtable Interface Designer. Implements
[`interfaces.md` §1](interfaces.md). **Airtable exposes no interface API** — every step here is
manual in the UI. Roughly 45–60 minutes.

Base **`appFGgbrUOs62IndE`** → https://airtable.com/appFGgbrUOs62IndE

---

## 0 · Prerequisites

Done via API on 2026-07-28 and verified live — no action needed:

| Change | Why |
|---|---|
| `Accounts.Stage Label` → renamed **`Stage`** | Interface configs bind by field name; `schema.md` says `Stage` |
| `Diagnostics.Diagnostic Age` (formula) added | Block 1 corner; `DATETIME_DIFF(TODAY(), {Diagnostic Date}, 'days')` |
| `Accounts.Diagnostic Age` (lookup) added | Same value on the account record, via `Current Diagnostic` |
| `Plays.Applies at Stage` → **multi-select `0`–`4`** | Was `singleLineText` holding ranges (`1-2`, `0-4`); expanded per record |
| `Diagnostics.Constraint Override Reason` added + populated | Records *why* Harbor Lane's constraint was overridden — see §9 |

**Manual steps first — the API cannot delete fields or change a field's type:**

1. **`Account Plays` → change `Name` (the primary field) from Single line text to Formula:**
   ```
   {Account Name} & " — " & {Play Code}
   ```
   It is currently **blank on all 9 records**. `Account Name` and `Play Code` were added via API on
   2026-07-28 and are populated — only the type conversion is left. **Do this before building
   Block 2:** the Accept button (beat 4) and automation A2 (beat 7) both *create* `Account Plays`
   records, and with a blank primary every newly created record renders as unnamed in the exact two
   moments you are demoing creation. Renders as `Floor & Board Furniture — P2`.
2. `Plays` → delete **`zz Applies at Stage (retired text — delete in UI)`**
3. `CSMs` → hide **`From field: Paired With`** (auto-generated reciprocal; hide, don't delete)
4. `Accounts` → hide **`Diagnostic (from Current Diagnostic)`** (stray lookup, unused)

**Field names are case-sensitive.** It is `ARR at Risk` (lowercase *at*), not `ARR At Risk`.

---

## 1 · Create the interface

1. **Interfaces** → **Create interface** → start from **Blank**
2. Layout: **Record review**
3. Name it **CSM Cockpit**
4. Source table: **Accounts**

Record review gives you the left list + main detail panel the spec calls for. Don't use Dashboard
here — it can't do per-record detail.

---

## 2 · Left rail — my book

**Sort:** `ARR at Risk` **descending**. This is deliberate and worth saying out loud in the demo:
sorting by ARR at risk rather than renewal date puts the largest preventable loss at the top of the
screen every morning.

**Filter (demo):** none — show all six.
**Filter (real deployment):** `CSM` **is** *current user*. Build it, then switch it off for the
demo so the whole book is visible. Access control is deliberately deferred (see
[`README.md`](README.md)).

**Fields to show, in order:**

| Field | Note |
|---|---|
| `Account` | |
| `ARR` | currency |
| `Quarters to Renewal` | |
| `Stage` | the lookup — renders `2 Contained` |
| `Constraint` | label this column **Binding constraint** (see §8) |
| `Renewal Readiness` | |

### ⚠ The spec table in `interfaces.md` is missing a row

`interfaces.md:14–20` lists **five** accounts. The book has **six** — **Meridian Health Systems
($1.1M, Stage 3, Value evidence, ⚠️ No current value)** is absent. It sorts last on `ARR at Risk`
($0, renews in 4 quarters), which is almost certainly how it got dropped when that table was typed
by hand. **Build six rows.** Live values, verified 2026-07-28:

| Account | ARR | Renewal | Stage | Binding constraint | Readiness |
|---|---|---|---|---|---|
| Floor & Board Furniture | $1,700,000 | 2Q | 2 Contained | Sponsorship | ⚠️ No current value |
| Corvus Financial Group | $890,000 | 3Q | 2 Contained | Value Evidence | ⚠️ No current value |
| Voltaic Software | $520,000 | 2Q | 2 Contained | Governance | ⚠️ No current value |
| TrailLine Logistics | $540,000 | 7Q | 1 Sponsored | Adoption | Not yet in cycle |
| Harbor Lane Retail | $310,000 | 5Q | 0 Unaware | Value Evidence | Not yet in cycle |
| Meridian Health Systems | $1,100,000 | 4Q | 3 Governed | Value Evidence | ⚠️ No current value |

Rows 1–3 carry the $3,110,000. Rows 4–6 carry $0 at risk.

---

## 3 · Block 1 — Where this account is

Header text element: **Where this account is**

| Element | Config |
|---|---|
| Field | `Stage` — add a **Text** element beside it reading `AI read` |
| Field ×4 | `Adoption`, `Sponsorship`, `Governance`, `Value Evidence` from `Current Diagnostic` |
| Field | `Diagnostic Age`, top-right corner |
| Field | the `Stage` rationale — see below |

**The four dimension bars.** The spec says "bars"; the source fields are `rating` type, which
Interface Designer renders as filled dots, not bars. Accept the dots — they read the same at a
glance and cost nothing. Do not convert the rating fields to number to chase the visual; the rating
type is what makes the 1–5 anchors enforceable in Interface 3.

**The rationale.** `Diagnostics.Stage` holds both lines (`STAGE:` and `RATIONALE:`). Add a
**Text** element labelled **Why this stage** with an `AI read` chip, bound to `Stage`. It will show
the `STAGE:` prefix too — acceptable, and it reinforces that the whole block is one model output.

**`Diagnostic Age`** — conditional formatting, grey when `> 90`.
**This will not fire.** All six diagnostics are dated 2026-07-20 (age 8 days) because the book was
swept at once. Build the rule anyway and leave it dormant; the line in the room is *"every
diagnostic here is eight days old because we just ran the sweep — at 90 days this greys out and
drops into the Director's inspection queue."* Do **not** backdate a record to light it up.

---

## 4 · Block 2 — Your next play

Header: **Your next play**

1. **Text** element, top of block:
   `Binding constraint (computed): ` + field `Constraint`
   Subtitle, smaller: *Lowest score selects the play.*
2. **Field** → `Recommended Play` from `Current Diagnostic`. Renders the full AI-2 output:
   `PLAY:` / `WHY:` / `FIRST THREE MOVES:` / `PARTNER TO PULL IN:` / `ALSO SEQUENCE:`
3. **Button** → **Accept** → action **Run automation** → creates the `Account Plays` record
4. **Button** → **Override** → action **Open record** → `Diagnostics`, focused on `Override Reason`

**Getting the constraint red.** Interface Designer can't conditionally colour a *lookup* field.
Two options — pick the first:

- **Recommended:** place four pre-styled Text elements (`Sponsorship` / `Governance` / `Adoption` /
  `Value Evidence`), each red, each with **conditional visibility** on `Constraint`. Exactly one
  shows. Five minutes, no schema change.
- Convert `Diagnostics.Constraint` to a single-select written by automation. More faithful colouring,
  but it makes the constraint mutable state instead of a derived value — **don't**, it breaks the
  "the formula picks the play" story.

---

## 5 · Block 3 — The value position

| Element | Config |
|---|---|
| Field | `Latest Value Story Status` (rollup on `Accounts`) |
| Grid | `Value Stories` filtered to this account — show `Value Story`, `Business Metric`, `Status`, `Narrative` |
| Button | **Draft value narrative** → Run automation → creates a `Value Stories` record and triggers AI-3 |

All six accounts read **`Draft`** — value coverage is **0 / 6**, and that is the point of the whole
brief. Floor & Board has **two** value stories; the rollup uses `ARRAYUNIQUE` so it still reads
`Draft` rather than `Draft, Draft`.

---

## 6 · Block 4 — Who we know

| Element | Config |
|---|---|
| Grid | `Stakeholders`, filtered to this account |
| Fields | `Name`, `Title`, `Role`, `Sentiment`, `Status`, `Last Touch` |
| Text | `Sponsor Roles` rollup + thread count against target of **3** |

**Departed contacts struck through** — Interface Designer has no strikethrough. Use `Status` as a
visible coloured column instead, and sort `Status` ascending so departed/unengaged sort to the top.
Floor & Board's departed champion is then the first row a CSM sees, which is the whole point of the
block.

---

## 7 · Block 5 — Signals

Grid → `Signals`, filtered to this account, sorted `Date` **descending**, **limit 8**.
Colour by `Direction`. Show `Signal`, `Type`, `Direction`, `Date`, `Detail`.

---

## 8 · The labelling decision — constraint vs. rationale

`Constraint` (formula) and AI-1's stage rationale answer **different questions** and disagree on
**four of six accounts**. Both are correct. The screen must not read as a contradiction.

| Account | `Constraint` → picks the play | AI-1 → explains the stage | |
|---|---|---|---|
| Floor & Board | Sponsorship | governance | ✗ |
| Corvus | Value Evidence | governance | ✗ |
| TrailLine | Adoption | sponsorship structure | ✗ |
| Harbor Lane | Value Evidence *(override)* | sponsorship | ✗ |
| Voltaic | Governance | governance | ✓ |
| Meridian | Value Evidence | value evidence | ✓ |

**The resolution — layer two kinds of label:**

- **Block headers are function-first** — *Where this account is* / *Your next play*. This is what a
  CSM navigates by, and the premise of the Cockpit is that no pattern recognition is required.
- **Provenance chips appear only at the point of collision** — `AI read` on the rationale,
  `(computed)` on the binding constraint. A CSM who never notices the chips still reads the screen
  correctly; one who hits the Floor & Board disagreement has the answer four words away.

**Say in the room, don't put on screen:** *the constraint picks the play, the rationale explains the
stage* — or the `AGENTS.md` form, *stage describes, the binding constraint prescribes.* Right
sentence spoken, too abstract in a UI.

---

## 9 · Harbor Lane and Floor & Board — the identical-scores question

Both score **sponsorship 1 / governance 1 / value evidence 1**, adoption higher. They resolve to
**different** constraints. Expect to be asked; both rows are on the same screen.

- **Floor & Board** → `Sponsorship`. The formula's tie-break precedence
  (Sponsorship → Adoption → Value Evidence → Governance) picks it.
- **Harbor Lane** → `Value Evidence`, via `Constraint Override`. Grounded in the assessment's own
  account snapshot: the team *"would need a clear value demonstration tied to an existing use case
  to engage."* Sponsorship is absent, but it isn't what's blocking movement — there is no proof
  point to sponsor.

The reasoning now lives in **`Diagnostics.Constraint Override Reason`**, in the base, not just in
the deck. **Surface that field in Block 1**, directly under the constraint chip, visible only when
`Constraint Override` is set.

This is the strongest human-in-the-loop beat in the build: the formula said Sponsorship, AI-1
independently said sponsorship, a human overrode **both** and wrote down why — and the screen shows
all three. Don't hide it; open it.

---

## 10 · Verification gates

Before calling this done, check on screen:

- [ ] Left rail shows **six** accounts, Floor & Board first, Meridian present
- [ ] Left-rail ARR sums to **$5,060,000**; rows 1–3 carry **$3,110,000** (61%)
- [ ] Voltaic reads **Stage 2 Contained** despite adoption 5 — *the trap*
- [ ] Floor & Board shows constraint **Sponsorship** and rationale saying **governance**, and the
      chips make that legible rather than confusing
- [ ] Harbor Lane shows the override reason
- [ ] `Recommended Play` renders P2 / P4 / P6 / P3 / P5 / P1 across the six
- [ ] `ALSO SEQUENCE: P8` appears on Floor & Board and Voltaic **only**
- [ ] Value position reads `Draft` on all six — value coverage **0 / 6**
- [ ] Accept and Draft-value-narrative buttons both fire

Anything that fails here is a build error, not a data error — all ten were verified against the API
on 2026-07-28.
