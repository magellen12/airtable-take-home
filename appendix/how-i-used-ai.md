# How I used AI

The brief says: *"we'd love to hear how you used them — what you kept, changed, and verified."*

> **⚠️ Complete this before submitting.** The sections marked **[VERIFY]** describe work that
> happens in Airtable itself and can't be filled in from outside the product. Everything else
> is an accurate record of how this repo was produced. Delete this banner when it's done.

---

## The setup

**Claude Code (Opus 4.8, later Opus 5)** in the terminal, working directly in this repo, for the
analysis and the artifacts. Airtable's own AI fields for the components inside the build.

Deliberately not a chat-and-paste workflow. Working in the repo meant the model could read the
seed CSVs it had written, validate its own link references, and catch its own inconsistencies —
which it did, twice, both times on numbers I'd have shipped wrong. It also meant the review could
be run as pull requests, so the agent-drafted vs. human-edited diff is itself a visible artifact
(PRs [#1](https://github.com/magellen12/airtable-take-home/pull/1) and
[#2](https://github.com/magellen12/airtable-take-home/pull/2)) rather than a claim.

---

## What I used it for, and what happened

### 1 · Reading the source
The take-home PDF wouldn't extract — no PDF tooling on the machine. Rather than retype it, I
had the model write a throwaway zlib stream decompressor to pull the text out, then install
poppler when that turned out to be the cleaner path. Two minutes instead of twenty.

**Kept:** all of it. Mechanical work, no judgment involved.

### 2 · The diagnosis — where AI helped least
This is the part that mattered most and where AI added the least, which is worth saying out
loud.

**Kept:** the structural framing of "score the book on dimensions, find the pattern in the
columns rather than the rows." Good instinct, arrived at fast.

**Changed:** almost every score. The first pass scored **Voltaic a 4 on maturity** — it read
"building its own agents and AI workflows" as sophistication. That's precisely the mistake that
loses the account, and it's the same mistake a human makes. The finding that Voltaic is the
trap in this book is the single most important thing in my brief, and the model had it exactly
backwards until I pushed on it.

That correction is now hard-coded into the production prompt as a rule
(`Stage 4 requires Governance >= 4`), so **every CSM gets the correction whether or not they'd
have caught it themselves.** That's the most useful thing that came out of the whole exercise:
a mistake I caught once, encoded so nobody has to catch it again.

**Verified:** I recomputed the ARR figures by hand. $5.06M book, $3.11M at risk, 61%. Two
inconsistencies surfaced during the build — an `ARR at Risk` formula that would have produced
$3.66M against a stated $3.11M, and a mislabelled chart summing to the wrong total. Both are
fixed; both were the kind of error that gets found in the room, by the panel, not by me.

### 3 · The methodology
**Kept:** the constraint mechanic (lowest score picks the play, not the average). It survived
being tested against all six accounts and produced the right answer on five.

**Changed:** it produced the *wrong* answer on two accounts. On Harbor Lane the rule said "fix
sponsorship" — go recruit an executive for a team that has never seen an AI capability. You
can't sponsor an abstraction. That failure produced the second rule (*below Stage 1, Value
evidence leads*). On Meridian it wanted to route a value-evidence gap to a commercial value play,
when the evidence a *review board* needs is a risk-and-controls case — same constraint, different
audience — which produced the audience rule in the play recommender. I've deliberately left both
failures documented in
[`../docs/03-transformation-methodology.md`](../docs/03-transformation-methodology.md) rather
than presenting the model as if it arrived clean. A methodology that has visibly been wrong
is more trustworthy than one that hasn't been tested.

**Changed:** the first play library had fourteen plays. Cut to eight. A library nobody can
hold in their head is a library nobody uses.

### 4 · The build
**Kept:** the schema — eight tables, the separation of `Diagnostics` from `Accounts` so stage
movement is preserved over time.

**Changed:** the first draft included a composite health score rolling the four dimensions into
one number. Cut it entirely. **A composite score is exactly what would show Voltaic green** —
it would reintroduce the failure the whole model exists to prevent.

**Verified:** the seed CSVs are machine-validated. `scripts/seed_airtable.py --dry-run` parses
all 8 files, resolves every linked-record reference across 84 records, and reports failures by
row. It passes. That's real verification, not a read-through.

### 5 · The AI field prompts
Written with the model, then adversarially tested against the seed data by asking it to break
its own prompts.

**The change that mattered:** the value narrative generator originally produced a confident,
well-written paragraph for Floor & Board — an account with **no measurements of any kind**. It
inferred plausible numbers from "strong daily use across all 4 teams." That is the single most
dangerous thing this system could do: a fabricated figure in a CFO conversation is worse than
walking in with nothing.

Rule 3 (`Do NOT estimate, extrapolate, annualize or invent a figure`) plus the
`INSUFFICIENT EVIDENCE` escape hatch were added in response. The field now refuses on Floor &
Board and tells the CSM what to go collect. **I'm demoing the refusal, not just the success.**

### 6 · The audit pass — the failure mode I didn't expect

Late on, writing the full play library, I asked a question I should have asked much earlier:
**where did the name "Value Engineering" come from?**

Nowhere. I'd invented it. So had I invented `Trust & Security`, `Deal Desk`, and a `Solutions`
function. The model had proposed them early as plausible cross-functional partners, I hadn't
challenged them, and from that point on **they were used perfectly consistently** — in the play
library, the base schema's select options, the seed data, the AI component prompts, the talk
track. That consistency is exactly what made them invisible. Nothing ever contradicted anything.

**Verified against the sources rather than my memory of them.** The assessment names no
Airtable-side partner function at all. The job description names exactly five: *"partner closely
with Renewals, Support, Professional Services, Product, and Sales."* Everything outside that list
was mine.

**Changed:** rather than swap in different team names — which would have been the same mistake
with better cover — the unverifiable ones are now described by **what has to be produced and who
has to stand behind it**: *Value Validation* is whoever can stand behind a quantitative claim
before it reaches a customer's CFO; *Security & Risk* is whoever produces customer-facing risk and
controls artifacts. `docs/04` marks the split visually, bold for named partners and italics for
capabilities, and mapping the capabilities to real owners is on the day-one question list.

**Kept:** every customer-side name — Marketing Ops, RevOps, the IT Security & Data Governance
Review Board, the CFO's office, procurement — because a sweep confirmed each one is verbatim from
the account snapshot. The audit was about separating the two, not about deleting specifics.

The same pass caught two unsupported claims about customer behavior ("*they already know they have
agents nobody owns*") and rewrote every definition of done as **a signal we look for** rather than
a prediction of what a customer will do.

**What I'd take from it:** the earlier errors were wrong *numbers*, and numbers get checked. This
one was a wrong *premise*, applied consistently — which is the harder failure to see, because
internal consistency reads as correctness. The control isn't more careful reading; it's asking
"what's the source for this?" of things that have stopped looking like claims. That's a habit I'd
want on a team shipping AI-drafted customer-facing material, and it's why the value narrative
carries a `Source of Truth` field rather than just a status.

---

## [VERIFY] — to complete in Airtable before the session

- [ ] Run **AI-1** on Voltaic. It must return **Stage 2, not Stage 4.** If it returns 4, the
      critical rule isn't landing and needs strengthening — note what you changed.
- [ ] Run **AI-3** on Corvus. Check it doesn't invent a number beyond what's in the fields.
- [ ] Run **AI-3** on Floor & Board. It must return `INSUFFICIENT EVIDENCE`. **This is the
      demo moment** — if it fabricates instead, tighten rule 3 and record the fix here.
- [ ] Run **AI-2** on Harbor Lane. It must return **P1**, not a sponsorship play — that's the
      Stage 0 exception working.
- [ ] Run **AI-2** on Meridian. It must return **P5 (Governance Case)**, not P4 — same
      Value-evidence constraint, but a governance audience routes it to the risk-and-controls
      case. That's the audience rule working.
- [ ] Note anything Airtable's AI fields do differently from what these prompts assume (prompt
      length limits, output formatting, field-reference behaviour). Assumption 7 in
      [`assumptions.md`](assumptions.md) flags this as unverified on purpose.

---

## What I'd say about it in the room

**AI was fast at structure and wrong about judgment.** It gave me a maturity model in minutes
and then scored the most dangerous account in the book as the healthiest. It drafted a
convincing value narrative for a customer with no measurements at all. It invented an org chart
and then used it flawlessly across nine files. All three were plausible, well-formed, and would
have cost me the things I most needed to get right — and the third is the one I'd warn a team
about, because it never looked like an error.

What it genuinely bought me: I spent my hours on the diagnosis and the judgment calls instead
of on schema design, CSV wrangling and formula syntax. And the two places it was wrong turned
into the two best mechanics in the system — the governance rule in the stage classifier and
the evidence refusal in the value generator. **Both are now controls that protect fifteen CSMs
from making the mistake I nearly made once.**

That's the pattern I'd want this team running: use it to move fast on structure, overrule it on
judgment, and when it's wrong in an interesting way, encode the correction so the whole team
inherits it.
