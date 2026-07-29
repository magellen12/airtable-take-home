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

| Field | Note |
|---|---|
| `Account` | link — pick the account |
| `Diagnostic Date` | defaults to today |
| `Run By` | link to CSMs |
| `Adoption` | rating 1–5 |
| `Adoption Evidence` | **make required** |
| `Sponsorship` | rating 1–5 |
| `Sponsorship Evidence` | **make required** |
| `Governance` | rating 1–5 |
| `Governance Evidence` | **make required** |
| `Value Evidence` | rating 1–5 |
| `Value Evidence Notes` | **make required** |
| `Session Notes` | free text — feeds AG-1 |

**Making the four evidence fields required is the entire mechanism.** It's what stops a score being
an opinion. A CSM cannot record "governance is a 4" without writing down what they saw that makes it
a 4. Everything downstream — the constraint, the play, the ARR-at-risk figure — inherits its
credibility from that one setting.

**What happens on submit.** The record is created, and the rest computes itself: `Constraint` picks
the lowest score, AI-1 assigns a stage with its reasoning, AI-2 recommends a play. The CSM opens the
Cockpit and the account has moved.

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
