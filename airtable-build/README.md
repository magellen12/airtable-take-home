# HTCS Transformation OS — Airtable build

The system the team runs the book in. Implements **P1 (one diagnostic across the book)** and
**P2 (the value-realization spine)** from the [strategic brief](../docs/01-strategic-brief.md).

Scoped deliberately: two priorities, well architected, demoable live — not the whole system.

---

## What it does

```
   SIGNALS                DIAGNOSTIC              CONSTRAINT              PLAY               VALUE NARRATIVE
   adoption, support,  →  4 dimensions      →     lowest score,     →    from the 8-play  →   AI-drafted in the
   commercial, QBR        (adoption, sponsor,     auto-derived           library, with        buyer's language,
   attendance             governance, value)                             partner named        human-validated
                                ↓                                                                    ↓
                          AI: stage +                                                          renewal / expansion
                          rationale                                                            conversation
```

A CSM opens their Cockpit and sees: **my accounts, ranked by ARR at risk · the binding
constraint on each · the recommended play and its first three moves · what's due this week.**

A Director opens the Book Review and sees: **stage distribution · value coverage · ARR at risk
by constraint · the skills matrix · plays past cycle time · fifteen CSMs' judgment in one place.**

---

## The leverage test

> *How does this make all 15 CSMs better — not just you?*

| | Before | With the OS |
|---|---|---|
| **Newest CSM** | Applies the one play they know. Diagnosis quality depends on who trained them. | Same diagnostic, same constraint logic, same play, with the right partner named for them. Gets a first draft of an executive narrative they couldn't yet write. |
| **Strong relationship CSM** *(Corvus)* | Never quantified an AI story; expansion stays unsubstantiated. | Base drafts the numbers, Professional Services validates, they do the persuasion. Deployed, not fixed. |
| **Strong builder CSM** *(TrailLine)* | Great in the workflow, thin above it. | Skills matrix pairs them with an exec-presence partner for the COO thread — they keep the account, not lose it. |
| **Best CSM on the team** | Carries pattern recognition in their head; it benefits one book. | Time back on diagnosis and drafting. Authors plays that all 15 then run. Their judgment becomes shared infrastructure. |
| **Director** | 15 opinions, no inspection surface, discovers problems at renewal. | One base. Grades 3 diagnostics/week. Sees a stale value narrative 2 quarters before it becomes a churn signal. |

**The single sentence:** the system carries the pattern recognition, so a CSM doesn't have to
have fifteen years of it — and it makes fifteen people's judgment visible in one place, which
is the exact thing this team lost when it lost its managers.

---

## Contents

| File | What it is |
|---|---|
| [`schema.md`](schema.md) | 8 tables, every field, types, formulas, relationships |
| [`ai-components.md`](ai-components.md) | The 3 AI fields, 1 agent, and 3 automations — with copy-pasteable prompts |
| [`interfaces.md`](interfaces.md) | CSM Cockpit, Director Book Review, and the live diagnostic session view |
| [`build-checklist.md`](build-checklist.md) | Ordered build steps — roughly 2–3 hours in the product |
| [`data/`](data/) | Import-ready CSVs: 6 accounts pre-scored, 8 plays, 19 stakeholders, 24 signals, 6 value stories, 6 CSMs w/ skills matrix |

---

## Build it

**Fastest path (manual, ~2–3 hrs):** follow [`build-checklist.md`](build-checklist.md) and
import the CSVs in the order listed. Order matters — linked-record fields resolve by name, so
`Plays` and `CSMs` must exist before `Accounts`.

**Scripted path:** [`../scripts/`](../scripts/) creates the base and loads all data via the
Airtable Web API. AI fields and interfaces still have to be added in the UI — the API doesn't
create those.

---

## What is deliberately *not* built

Naming the cut lines matters as much as the build.

- **No *single-number* health score.** The four-dimension diagnostic is the health read, kept
  multidimensional on purpose — a composite that averages the dimensions is exactly the kind of
  number that hides Voltaic. The binding constraint is the signal, not an average.
- **No CRM sync.** Real deployment reads renewal dates and ARR from Salesforce; here they're
  static fields. Assumed, not solved.
- **No full stakeholder relationship graph.** Stakeholders are flat, tagged by role. Enough to
  measure multi-threading, which is the metric that matters.
- **Only three of the eight plays have full artifact templates** (P1, P4, P6). The rest are
  specified but not templated — the team authors those at the monthly retro, and that's the
  point.
- **Access control is deferred.** Real deployment restricts CSMs to their own book; the demo
  shows everything so the whole model is visible.
