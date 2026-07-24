# Seed data

Import-ready CSVs for the six snapshot accounts. **Import in the order below** — linked-record
fields resolve by name, so referenced tables have to exist first.

| Order | File | Records | Table |
|---|---|---|---|
| 1 | `csms.csv` | 6 | CSMs |
| 2 | `plays.csv` | 8 | Plays |
| 3 | `accounts.csv` | 6 | Accounts |
| 4 | `diagnostics.csv` | 6 | Diagnostics |
| 5 | `stakeholders.csv` | 19 | Stakeholders |
| 6 | `signals.csv` | 24 | Signals |
| 7 | `value-stories.csv` | 6 | Value Stories |
| 8 | `account-plays.csv` | 9 | Account Plays |

---

## What's from the brief and what I made up

**Taken directly from the assessment snapshot:** all six account names, functions, ARR, seats,
contract stage, renewal timing, and every fact in the AI-transformation-state, organizational-
dynamics and CS-signals columns. The `Notes` field on `accounts.csv` is close to verbatim.

**Constructed by me, and clearly invented:**

- **Diagnostic scores** — my judgment applied to the snapshot facts, on the four dimensions
  (Adoption depth, Sponsorship & multi-threading, Governance maturity, Value evidence). The
  reasoning for every score is in [`../../docs/02-book-diagnosis.md`](../../docs/02-book-diagnosis.md).
- **CSM skills-matrix ratings** (builder depth × executive presence × domain) and the pairings
  in `csms.csv` — invented, but mapped to the snapshot's descriptions of each account's CSM.
- **Stakeholder names.** The *roles* are drawn from the snapshot (the departed Sr. Director of
  Marketing Ops, the deputy, the COO, the review board chair, the BU champion); the names are
  invented. Records marked `GAP` in the notes are people the snapshot implies exist but who
  have never been engaged — those gaps are the finding, not the fiction.
- **CSM names.** Strength profiles map to the snapshot's descriptions where it gave them:
  Marcus Oyelaran is TrailLine's "strongest builder, newer to executive engagement," Dana
  Whitfield is Corvus's "excellent relationships, lighter technical depth," Priya Raghavan is
  Meridian's CSM who "drifted into order-taking."
- **Signals** — plausible events consistent with the snapshot. Dates are placed relative to a
  July 2026 "today."

**One number needs flagging explicitly.** The Corvus value story contains illustrative figures
(14 min → 3 min triage, ~2,100 cases/month, ~385 hours recovered). **The snapshot gives no
numbers at all.** I invented them so the AI value-narrative field has something to work with in
a demo. The `Source of Truth` field on that record says so, and the story is left in `Draft`
status rather than `Customer-validated` — because inside the methodology, an unvalidated number
is exactly what it looks like here.

Every other value story is deliberately left empty of numbers. That's not laziness: it's what
the book actually looks like, and it's what makes the AI field's `INSUFFICIENT EVIDENCE`
refusal demonstrable on real seed data.

---

## Date convention

All dates assume **"today" is late July 2026**. `Quarters to Renewal` is stored as a static
number rather than derived from a date, since the snapshot gives relative timing only. In a
real deployment both come from the CRM — see the "not built" list in
[`../README.md`](../README.md).
