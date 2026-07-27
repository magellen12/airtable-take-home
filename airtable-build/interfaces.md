# Interfaces

Three. Two are for the team, one is for the customer session. Each answers a specific question
for a specific person — no general-purpose dashboards.

---

## 1 · CSM Cockpit
**Who:** every HTCSM · **Question:** *What do I do this week, and on which account?*
**Type:** Record-review layout, filtered to `CSM = current user`

### Left rail — my book, sorted by `ARR at Risk` descending

| Account | ARR | Renewal | Stage | Constraint | Readiness |
|---|---|---|---|---|---|
| Floor & Board | $1.7M | 2Q | 2 ↓ | **Sponsorship** | ⚠️ No current value |
| Corvus | $890K | 3Q | 2 | **Value evidence** | ⚠️ No current value |
| Voltaic | $520K | 2Q | 2 *(presents 4)* | **Governance** | ⚠️ No current value |
| TrailLine | $540K | yr 1 | 1 | **Adoption** | Not yet in cycle |
| Harbor Lane | $310K | 5Q | 0 | **Value evidence** | Not yet in cycle |

Sorting by ARR at risk rather than by renewal date is deliberate: it puts the largest
preventable loss at the top of the screen every morning.

### Main panel — the selected account

**Block 1 · Where this account actually is**
Four dimension bars, the constraint called out in red, stage with the AI rationale in plain
language. `Diagnostic Age` in the corner — greys out past 90 days.

**Block 2 · Your next play**
The AI recommendation rendered as a card: play name, why, **first three moves**, partner to
pull in. Two buttons: **Accept → creates the `Account Plays` record** · **Override → asks why.**

**Block 3 · The value position**
Current value narrative with its status chip and age. If missing or stale: a **"Draft value
narrative"** button that creates the record and runs AI-3.

**Block 4 · Who we know**
Stakeholder grid by role. Thread count against target of 3. Departed contacts struck through —
Floor & Board's departed champion is visible here on day one, which is the whole point.

**Block 5 · Signals** — last 8, most recent first, coloured by direction.

### What a CSM actually does here
> Monday, 9am. Opens the Cockpit. Floor & Board is top of the list. Sees: constraint =
> Sponsorship, champion departed 3 months ago, one thread mapped against a target of three,
> no value narrative, renewal conversation in two quarters. The recommended play is **P2
> Re-Sponsor** with three moves and Sales named as partner. They click Accept and the week has
> a shape.
>
> No pattern recognition required. That's a CSM in month four running the same first move as
> the best CSM on the team.

---

## 2 · Director Book Review
**Who:** me · **Question:** *Where is the book, where is the team, and what am I inspecting
on Monday?* · **Type:** Dashboard

### Row 1 — four numbers

| | | |
|---|---|---|
| **ARR at Risk** `$3.11M` — 61% of book | **Value Coverage** `0 / 6` — 0% | **Sponsor Coverage** `1 / 6` — 17% |
| **% of Book Staged** `6 / 6` — 100% | **Stage Progression QoQ** `baseline` | |

Value Coverage sits in position two on purpose. It's the leading indicator I'd be judged on
in six months, and it starts at zero.

### Row 2 — the book on one screen
- **Stage distribution** (bar) — 1 at Stage 0, 1 at Stage 1, 3 at Stage 2, 1 at Stage 3, none
  at 4. *No account in this book is compounding.*
- **Book ARR by constraint** (bar) — Value evidence $2.3M · Sponsorship $1.7M · Adoption $540K ·
  Governance $520K. This is my resourcing argument in one chart: **$2.3M of the book — 45% — is
  blocked on value evidence**, which is the entire case for P2 (the value engine) and for
  Value Validation + Security & Risk partner capacity ahead of more headcount.
- **Renewal timeline** (timeline by `Quarters to Renewal`), each account coloured by
  `Renewal Readiness`.

### Row 3 — the team (the skills matrix)
Grid of CSMs: book ARR · the three matrix axes (**builder depth · executive presence · domain**)
· who they're **paired with** · plays in flight · plays over cycle time · DoD hit rate · plays
authored · development focus.

This is the skills matrix and the staffing view in one place. The matrix axes are what drive
pairing — Marcus (builder 5 / exec 2) is visibly paired with Ben (exec 5) on TrailLine, so the
pairing is an inspectable decision rather than a favour I remember to do.

**`Plays Authored` is the column I watch for the manager-layer decision.** Not tenure, not book
size — who is contributing judgment back to the rest of the team.

### Row 4 — the inspection queue
- Plays over cycle time
- Diagnostics older than 90 days
- **Play overrides awaiting my review** — the model-quality feed
- Accounts with a score ≥4 and no evidence (A3 flags)

### What I actually do here
> Monday, 60 minutes, screen shared. Not a status round-robin — I open the ARR-at-risk-by-
> constraint chart and we work the top three. Three accounts deep, rotating, so each CSM
> presents about monthly. Then I read three diagnostics before the 1:1s and grade the
> *reasoning*, not the score.

---

## 3 · Diagnostic Session
**Who:** CSM, live in front of a customer · **Question:** *Where are you, honestly?*
**Type:** Form → record layout

Designed to be screen-shared with the customer. That constraint drives everything about it:
plain language, no internal jargon, no scores visible until all four are entered.

**Flow**
1. **Four blocks, one per dimension.** Each shows the 1–5 anchors in customer-readable
   language and requires the evidence note before advancing. The customer sees the anchors —
   that's what makes the conversation honest rather than flattering.
2. **Notes field** at the end. Optionally run **AG-1** first to pre-draft scores from raw notes,
   then correct them live.
3. **Reveal.** All four scores, the stage, the constraint. Shown *to the customer.*
4. **The play**, in customer language: here's what we do next and here's who from our side.

**Why the customer sees their own score.** A diagnostic the customer doesn't see is a CRM
field. A diagnostic they help produce is a shared agenda — and it's what converts a
relationship conversation into a transformation conversation, which is precisely the shift
this function is being asked to make. It also fixes Meridian's order-taking problem
structurally: you cannot run this session as an order-taker.

---

## Interfaces deliberately not built

- **Executive/CRO rollup.** Would be next. Not what's being assessed.
- **Customer-facing portal.** Real leverage, wrong scope for 4–6 hours.
- **Mobile.** No.
