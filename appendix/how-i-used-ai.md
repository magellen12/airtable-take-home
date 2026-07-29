# How I used AI

The brief says: *"we'd love to hear how you used them — what you kept, changed, and verified."*

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

## Verified in the live base — every gate passed

Run against `appFGgbrUOs62IndE` with real records, 2026-07-28.

- [x] **AI-1 on Voltaic → Stage 2, not Stage 4.** The trap holds. Elite adoption plus governance at
      1 reads as a risk signal rather than maturity, which is the whole point of the account.
- [x] **AI-3 on Corvus → no invented figures.** It quantifies from what's in the fields and returns
      `CONFIDENCE: Low`, where the spec had predicted Medium. It was righter than the spec.
- [x] **AI-3 on Floor & Board → `INSUFFICIENT EVIDENCE`.** Both of its value stories refuse
      independently; three of the six refuse overall. Not a lucky roll — the baseline data isn't
      there and the field says so.
- [x] **AI-2 on Harbor Lane → P1**, not a sponsorship play. The Stage 0 exception works.
- [x] **AI-2 on Meridian → P5**, not P4. Same value-evidence constraint as Corvus, but a governance
      audience routes it to the risk-and-controls case. The audience rule works.
- [x] **ARR at risk = $3,110,000 of a $5,060,000 book.**

### What the product did differently from what the prompts assumed

**Assumption 7 in [`assumptions.md`](assumptions.md) flagged this as unverified. Here's the answer.**

**One AI field can hold two outputs, and it should.** AI-1 was going to be two fields — stage, and
rationale. Built that way, separate generations disagree with each other. It's one field emitting
both lines, split afterward by a formula.

**AI fields reference other fields by name, and the wrong name is silent.** AI-2 read `{Stage}` when
it needed `{Stage Label}`, so it started picking plays off AI-1's *rationale* prose instead of the
computed constraint. Nothing errored. It took three rounds to find.

**Prose instructions produce prose omissions.** AI-2 kept dropping the follow-on play. The fix
wasn't a better sentence, it was making it a required output slot:
`ALSO SEQUENCE: <line, or exactly "None">`. Structure the output and the model stops improvising
about what to leave out.

**Every correction was about output discipline, never about the decision.** Every play, stage and
refusal was right the first time. What needed three rounds was internal reasoning, rule citations
and visible deliberation leaking into fields a CSM or a customer reads. Same shape as the invented
org chart: the substance was fine, the framing was wrong, and it was only visible against real
records.

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
