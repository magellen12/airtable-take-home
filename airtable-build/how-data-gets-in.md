# How data gets into this base

The question a recruiter will ask, and the honest answer to it.

> *"This all works because the scores are already there. Where do the scores come from, and what
> stops this being another CRM field nobody updates?"*

---

## The short answer

Four things feed this base. Only one of them is the interesting one.

| What | Where it comes from | Built here? |
|---|---|---|
| **The diagnostic** — four scores plus evidence | A live session with the customer | **Yes** — see below |
| **Draft scores from raw notes** | AG-1 agent reads the CSM's meeting notes | Specified, buildable in ~20 min |
| **Signals** — adoption, support, commercial, QBR | Product telemetry, support system, CRM | **No** — declared cut |
| **Value stories** — baseline, impact, proof | The customer, validated before it moves | Partially — records exist, evidence is manual |

The thing that makes this different from a CRM field nobody updates is that **the diagnostic is not
a form the CSM fills in afterwards. It's the agenda of a meeting they run with the customer, on
screen, together.** Nobody maintains it as admin because maintaining it *is* the customer
conversation.

---

## 1 · The diagnostic session — the primary input

This is Interface 3 in [`interfaces.md`](interfaces.md) §3, and it's the answer to the question.

A CSM sits with the customer and works through four blocks, one per dimension. Each block shows the
1-to-5 anchors **in customer-readable language**, and each requires an evidence note before moving
on. No scores are shown until all four are entered.

**Why the customer sees their own score.** A diagnostic the customer never sees is a CRM field. A
diagnostic they help produce is a shared agenda. That's the difference between a relationship
conversation and a transformation conversation, which is the exact shift this function is being asked
to make.

It also fixes an order-taking problem structurally rather than through coaching: you cannot run this
session as an order-taker. The anchors are on screen and the customer is reading them with you.

### Building it — a form, about 20 minutes

Interfaces → Create interface → **Form** layout → table **Diagnostics**.

Fields, in this order:

Field names below are exact and case-sensitive, checked against the live base.

| Field | Type | Required? | Note |
|---|---|---|---|
| `Account` | link → Accounts | **required** | structural, see below |
| `Diagnostic Date` | date (`YYYY-MM-DD`) | **required** | structural, see below |
| `Run By` | link → CSMs | optional | |
| `Adoption` | rating, 5 stars | **required** | see the blank-rating trap |
| `Adoption Evidence` | long text | **required** | the mechanism |
| `Sponsorship` | rating, 5 stars | **required** | |
| `Sponsorship Evidence` | long text | **required** | the mechanism |
| `Governance` | rating, 5 stars | **required** | |
| `Governance Evidence` | long text | **required** | the mechanism |
| `Value Evidence` | rating, 5 stars | **required** | |
| `Value Evidence Notes` | long text | **required** | the mechanism |
| `Session Notes` | long text | optional | feeds AG-1 |

**Making the four evidence fields required is the entire mechanism.** It's what stops a score being
an opinion. A CSM cannot record "governance is a 4" without writing down what they saw that makes it
a 4. Everything downstream — the constraint, the play, the ARR-at-risk figure — inherits its
credibility from that one setting. That is still the line to say out loud.

The other six required fields are there for a duller reason: without them the record is broken.

**The blank-rating problem. Require all four ratings.** This was tested against the live base by
submitting throwaway diagnostics through the API and reading back what computed. The throwaways were
deleted and the book totals re-verified afterwards.

Two earlier drafts of this section were wrong, in opposite directions. The first required only the
four evidence fields, which is a bug. The second claimed a blank rating reads as `0` and produces a
confidently wrong constraint and play. **It doesn't.** What actually happens, measured:

- **`Lowest Score` ignores blanks.** Airtable's `MIN` skips empty fields rather than reading them as
  zero. A diagnostic submitted with Adoption blank and Sponsorship 3, Governance 2, Value Evidence 4
  returned `Lowest Score = 2` and `Constraint = Governance`, which is correct. So the constraint and
  the play are **not** silently corrupted.
- **`Average` does treat a blank as zero, and that one is silent.** The formula is
  `ROUND((Sponsorship + Governance + Adoption + Value Evidence) / 4, 2)` with the divisor fixed at 4,
  so a blank contributes nothing to the numerator while still dividing by four. The same test record
  returned `Average = 2.25` when the mean of the three scores actually given is 3.00. Nothing flags
  it.
- **A blank rating stops both AI fields dead.** `Stage` and `Recommended Play` returned
  `emptyDependency` errors and stayed there across six polls over a minute. `Stage Label` then reads
  `#ERROR!`, and because `Accounts.Stage` is a lookup of `Stage Label`, the Cockpit shows an error
  where the stage should be. This happened with `Account` filled in, so it is the blank rating
  causing it, not the missing link.

So the honest version is that the base mostly fails **loudly** on a missing rating rather than
confidently, with the deflated average as the one quiet failure. Requiring all four ratings means
you never meet either. The reason to require them is that a blank rating yields a dead record, not
that it yields a wrong answer.

**Why `Account` and `Diagnostic Date` are required.** The table's primary field, `Diagnostic ID`, is
the formula `{Account Name} & " · " & DATETIME_FORMAT({Diagnostic Date}, "YYYY-MM")`, and
`Account Name` is a lookup through the `Account` link. Drop either input and the primary field comes
out as a fragment like `Corvus Financial Group · ` or ` · 2026-07`. An unlinked diagnostic is also
orphaned: nothing on `Accounts` can ever see it.

On `Diagnostic Date` "defaulting to today": **I can't verify that from the API, so plan without it.**
Set it in the session, it's one tap in the date picker. Don't leave the field off the form on the
assumption it fills itself.

**Deliberately not on the form.** The field picker offers six you should skip:

| Leave off | Why |
|---|---|
| `Accounts` (plural) | **The dangerous one.** See below. |
| `Constraint Override` | How you *challenge* the result afterwards, not a session input |
| `Constraint Override Reason` | Same |
| `Override Reason` | Same, and it duplicates the above |
| `Play Accepted` | Challenges the AI's play after the fact |
| `Diagnostic` | Dead text field, empty on all six records. Leave off and hide |

**Two fields on `Diagnostics` link to `Accounts`, and only one of them belongs on the form.** This is
easy to get wrong because the names differ by one letter:

| Field | Reciprocal of | Use on the form? |
|---|---|---|
| `Account` (singular) | `Accounts.Diagnostics`, the history link | **Yes** |
| `Accounts` (plural) | `Accounts.Current Diagnostic` | **No** |

Nothing computed can go on a form at all, so don't hunt for `Constraint`, `Lowest Score`,
`Stage`, `Recommended Play` or `Diagnostic ID` in the picker. That's the point: the CSM supplies
judgment and evidence, the base derives the rest.

### ⚠ What actually happens on submit. Read this before you demo it

An earlier draft said *"The CSM opens the Cockpit and the account has moved."* **That is not true as
the base is built,** and it's the kind of thing that falls over live.

Verified: every field the Cockpit and the Director Review read off `Accounts` is a lookup through
the **`Current Diagnostic`** link. That covers `Stage`, `Constraint`, `Adoption`, `Sponsorship`,
`Governance`, `Stage Rationale`, `Recommended Play`, `Value Evidence Score`, `Diagnostic Age` and
`Constraint Override Reason`. The form writes `Diagnostics.Account`, which populates the
`Accounts.Diagnostics` history link. **It does not touch `Current Diagnostic`.**

So on submit:

- ✅ The `Diagnostics` record is created, and everything **on that record** computes: `Lowest Score`,
  `Constraint`, `Diagnostic ID`, then AI-1's stage and AI-2's play.
- ❌ The **account** does not move. Its stage, constraint, recommended play and ARR-at-risk figure
  all still point at the old diagnostic until someone repoints `Current Diagnostic` at the new
  record.

#### Do not "fix" this by putting `Accounts` on the form

The obvious shortcut is to add the plural `Accounts` field to the form, since it is the reciprocal
of `Current Diagnostic`. **Tested against the live base, and it corrupts the account.**

Setting that link from the diagnostic side **appends rather than replaces**. A test diagnostic
created with `Accounts` pointing at TrailLine left TrailLine holding **two** current diagnostics.
Every lookup through the link then returned two values: `Constraint` read `Adoption, Adoption`,
`Adoption` read `1, 2`, and `ARR at Risk` went to **`#ERROR!`**, because its formula is
`IF(AND({Quarters to Renewal} <= 3, {Value Evidence Score} <= 2), {ARR}, 0)` and a two-value lookup
can't be compared to a number. That is the headline ARR-at-risk figure breaking on screen. Deleting
the test record restored everything.

**So promoting a diagnostic is not one link field.** A1 has to *clear* the old value and then set the
new one, which is exactly why it's an automation rather than a form field. That's a better answer
than a shortcut would have been.

Two honest options for the session:

1. **Say it.** *"Submitting creates the diagnostic and the whole chain computes on it. Promoting it
   to the account's current diagnostic is automation A1 — specified in `ai-components.md`, not built.
   I scoped automations out of the four hours."* This is the better answer if you're near time.
2. **Build A1.** An automation on `Diagnostics` record-created that clears the linked account's
   `Current Diagnostic` and sets it to the new record, and marks the prior diagnostic superseded.
   Not built today. If you build it, test it, because an untested automation failing on screen costs
   more than not having one.

Either way, **if you demo a live form submission, repoint `Current Diagnostic` by hand right after
submitting, clearing the old value first**, or the Cockpit will show the account unchanged and you'll
be explaining it at the worst possible moment.

---

## 2 · AG-1 — the agent that lowers the floor

Fully specified in [`ai-components.md`](ai-components.md#ag-1), prompt included and ready to paste.

**The problem it solves.** A CSM in month four has never run a transformation diagnostic. They come
out of a customer conversation with a page of messy notes and no idea how to turn that into four
defensible scores.

**What it does.** The CSM pastes raw notes into `Session Notes`. The agent proposes a score for each
dimension **with the specific quote from the notes that justifies it**. Where the notes don't support
a score, it returns `NOT EVIDENCED` and the exact question to go back and ask. It's told to bias
toward the lower score when evidence is ambiguous, because an inflated diagnostic produces a
confident wrong play, which is worse than an honest gap.

Then it returns `GAPS`: the three highest-value questions the CSM didn't ask.

**`GAPS` is the part that matters most.** It tells a CSM what a stronger CSM would have asked in that
meeting — every time they run it, on their own accounts, without a manager in the room. That's the
piece that scales one person's judgment across fifteen.

The CSM reviews, corrects and owns the result. The prompt says so explicitly: *"You are not the
decision-maker."*

### Two ways to build it, pick by how much time you have

**Cheap (~15 min):** add an AI field to `Diagnostics` called `Draft Scores` that reads
`Session Notes` and uses the AG-1 prompt as-is. Same output, same demo value, no agent configuration.
The CSM reads the draft and types the real scores in.

**Faithful (longer):** build it as an actual base agent, which can write the scores into the fields
rather than just proposing them in text.

**If you're out of time, say it rather than build it.** The prompt is written and the field it reads
exists. *"The agent is specified and the notes field is live; I built the fields it writes into and
scoped the agent itself out of the four hours"* is a fine answer. Pretending it's running is not.

---

## 3 · Signals — declared as not built

`Signals` holds adoption changes, support escalations, commercial events, QBR attendance. Twenty-four
of them are seeded and they're what a real diagnostic would be argued from.

**In a real deployment these sync in.** Product telemetry for adoption, the support system for
escalations, CRM for commercial events. None of that is built here — the records are static seed
data.

Say that plainly if asked. It's the same category as no CRM sync for ARR and renewal dates: assumed,
not solved, and named as such in [`README.md`](README.md). Claiming a live integration that doesn't
exist is the one answer that would actually cost you.

---

## 4 · The loop — why this compounds instead of going stale

This is worth drawing, because it's the difference between a system and a spreadsheet.

```
  Signals accumulate on an account
        ↓
  Next diagnostic session — the CSM and customer score four dimensions,
  each with evidence, arguing from those signals
        ↓
  Constraint recomputes (lowest score wins)
        ↓
  A different play is recommended
        ↓
  The play runs, produces an artifact, and generates new signals
        ↓
  back to the top
```

**Cadence is quarterly**, enforced by the 90-day staleness rule. A diagnostic older than 90 days
greys out on the CSM's screen and drops into the Director's inspection queue. Nobody has to remember
to re-run it; the system asks.

**What makes the ratings get better over time** isn't the AI. It's that every score carries its
evidence, every override carries its reason, and a Director reads three of them a week and grades the
*reasoning*, not the number. The model gets corrected by people who had the actual conversation.

---

## The 30-second version, for the room

> "The diagnostic isn't a form someone fills in afterwards — it's the agenda of a session the CSM
> runs with the customer, on screen, together. Four dimensions, and you can't record a score without
> recording the evidence for it. That one constraint is what stops this being another health field
> nobody trusts.
>
> For a CSM who's never run one, the agent takes their raw meeting notes and drafts the scores with
> the quote behind each one — and tells them the three questions they should have asked. They correct
> it and own it.
>
> Signals would sync from product and support in a real deployment. Here they're static, and I'd
> rather say that than claim an integration I didn't build.
>
> Then it loops. Signals accumulate, the next diagnostic re-scores, the constraint moves, a different
> play comes up. Quarterly, and the system chases you for it at ninety days rather than waiting for
> you to remember."
