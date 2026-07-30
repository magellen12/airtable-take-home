# Working conventions for this repo

Rules for anyone — human or AI — editing this take-home. Most exist because something went wrong
once. The reasoning behind each is in [`CHANGELOG.md`](CHANGELOG.md) and
[`appendix/how-i-used-ai.md`](appendix/how-i-used-ai.md).

---

## 1 · Don't invent organizational facts

**This is the rule that matters most here, because breaking it is nearly invisible.** Invented
names get applied consistently, and internal consistency reads as correctness — nothing ever
contradicts anything.

**Airtable-side functions that may be named.** The role names exactly five: *"partner closely with
**Renewals, Support, Professional Services, Product, and Sales**."* Engineering appears once
("partner with Product and Engineering"), and the role reports to the Chief Customer Officer. That
is the complete list of internal teams with a source.

**Everything else is described as a capability, in italics** — by what it produces and who stands
behind it, never as a team name:

| Capability | Means |
|---|---|
| *Value Validation* | Whoever can stand behind a quantitative claim before it reaches a customer's CFO |
| *Security & Risk* | Whoever produces customer-facing AI risk and controls artifacts |
| *Contracting* | Whoever owns contract paper and legal review |

`Value Eng`, `Trust & Security`, `Deal Desk` and a `Solutions` function were all invented and have
been removed. **Do not reintroduce them, and do not invent replacements.** If a play needs a
capability that isn't listed, describe the capability and add it to
[`appendix/assumptions.md`](appendix/assumptions.md).

**Customer-side names are different — they're grounded.** Marketing Ops, RevOps, the IT Security &
Data Governance Review Board, the CFO's office, procurement, the COO all come verbatim from the
account snapshot. Don't genericize those; they're evidence.

## 2 · Don't assert what a customer will do

Definitions of done are written as **signals we look for on the customer's side** — not predictions,
not commitments made on a customer's behalf. "The economic buyer uses our number as their own" is
an observation we're waiting for and may not get.

The same applies to generalizations about what customers know or want. *"They already know they
have agents nobody owns"* was cut for this reason. Voltaic's version stayed, because they
volunteered it in the snapshot — the difference is a source, not a hedge.

## 3 · Separate the standard from the latitude

The organizing principle of the whole deliverable is **global consistency, local customization**.
In [`docs/05-play-library.md`](docs/05-play-library.md) every play splits into *the standard*
(constraint, trigger, partner, artifact, signal — changed in the retro, not the field) and *the
latitude* (sequencing, framing, who to approach, what to say). Sequences are labeled *"a default,
not a mandate."* Keep that split in any new play.

## 4 · Keep the brief at 1–2 pages

[`docs/01-strategic-brief.md`](docs/01-strategic-brief.md) is the submission piece: a **~1,025-word
body plus a ~60-word orienting header**, ~1,090 total, ~1.75 pages. Depth belongs in `docs/02–05`.
When trimming, cut hedges, parentheticals and redundant examples — never concepts. Two threads
must survive any edit: the
**people-manager lens** (develop people rather than direct tasks; the diagnostic as a coaching
instrument; leads surface through play authorship) and **global consistency, local customization**
(*consistency is the floor, not the ceiling*).

**The brief's three priorities are "Priority 1/2/3" — never "P1/P2/P3".** `P1`–`P8` are play codes,
and the two collided badly enough that a reader couldn't tell whether "P2" meant *Re-Sponsor* or
*build the value engine*. Keep them distinct in every document.

**Write for a reader who hasn't seen the source material.** No insider shorthand — "the working is
in `02`" became plain English for this reason — and spell out an abbreviation on first use.

## 5 · Numbers are verified, not remembered

Load-bearing figures: book **$5.06M**, ARR at risk **$3,110,000 (61%)**, adoption avg **3.2**,
value evidence **1.3**, governance **1.5**, sponsor coverage **2 of 6**, value coverage **0 of 6**,
seed data **84 records across 8 CSVs**.

Before changing any of them, recompute. Run `python3 scripts/seed_airtable.py --dry-run` after
touching anything in `airtable-build/data/` — it validates every linked-record reference and must
report *"All link references resolve."* A stale number in a deliverable about value evidence is a
bad look, and the 83→84 record count was already wrong once.

## 6 · Changes go through pull requests

The agent-drafted vs. human-edited diff is a deliberate artifact — recruiters can see the review
happen. Work on a branch, commit with messages that say what changed *and why*, open a PR, and
merge with `--merge` (never squash) so the review commits stay visible.

Every substantive change gets a [`CHANGELOG.md`](CHANGELOG.md) entry, newest first, with its sha
and a **Kept / Changed / Verified** framing — the assessment explicitly asks to hear *"what you
kept, changed, and verified."* Corrections get logged, not quietly fixed; the record of being
wrong is part of the argument.

## 7 · Don't commit the assessment PDF

It's Airtable's document. It stays gitignored at
`~/Desktop/Director_AI_Transformation___Customer_Success_-_Presentation_(July_26').pdf`.

---

## Repo map

| Path | What it is |
|---|---|
| `docs/01-strategic-brief.md` | The primary deliverable. 1–2 pages. |
| `docs/02-book-diagnosis.md` | All six accounts scored, dimension by dimension. |
| `docs/03-transformation-methodology.md` | Maturity ladder, the constraint rule, play index. |
| `docs/04-operating-model.md` | Running it across 15 CSMs — ownership, matrix, rhythm, metrics. |
| `docs/05-play-library.md` | The eight plays in full: standard vs. latitude. |
| `airtable-build/` | Schema, AI components, interfaces, build guides, seed CSVs. |
| `scripts/seed_airtable.py` | Creates and loads the base. `--dry-run` validates without credentials. |
| `session/` | Talk track and Q&A prep for the 60-minute session. |
| `appendix/` | Assumptions, how-I-used-AI, reconciliation of two independent drafts. |

**The one-line thesis, for orientation:** six accounts, $5.06M; 61% renews inside three quarters
and none of it scores above 2/5 on value evidence, with $2.59M of it at 1. The platform works; the
operating model around it doesn't. Stage *describes*, the binding constraint *prescribes*.

**Value-evidence scores, live, so this is not re-derived from memory:** Floor & Board 1 · Corvus 1 ·
Voltaic **2** · TrailLine 1 · Harbor Lane 1 · Meridian 2. `Accounts.ARR at Risk` fires at
`Value Evidence Score <= 2`, which is why the $3.11M figure is right while "all three at 1" was not.
