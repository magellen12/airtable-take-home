# Strategic Brief — High Touch Customer Success
**Director, AI Transformation & Customer Success · First 90 days**

---

## What I see in the book

Six accounts, $5.06M ARR. **$3.11M of it — 61% — has a renewal conversation inside three
quarters**: Floor & Board, Voltaic, Corvus. All three score **1 out of 5 on the one dimension
that decides a renewal**: whether anyone can state, in the buyer's language, what the customer
got for the money.

I scored every account on four dimensions — **Sponsorship, Governance, Capability, Proof**
(full working in [`02-book-diagnosis.md`](02-book-diagnosis.md)):

| Account | ARR | Renewal | Sponsor | Govern | Capability | **Proof** | Stage | Binding constraint |
|---|---|---|---|---|---|---|---|---|
| Floor & Board | $1.7M | ~2Q | 1 | 1 | 3 | **1** | 2 → regressing | Sponsorship |
| Meridian Health | $1.1M | 4Q | 5 | 3 | 4 | **2** | 3 Governed | Governance |
| TrailLine | $540K | first yr | 3 | 1 | 1 | **1** | 1 Sponsored | Capability |
| Corvus Financial | $890K | 3Q | 2 | 2 | 4 | **1** | 2 Contained | Proof |
| Harbor Lane | $310K | 5Q | 1 | 1 | 2 | **1** | 0 Unaware | Proof |
| Voltaic | $520K | 2Q | 2 | 1 | 5 | **2** | 2 *(presents as 4)* | Governance |
| **Book average** | | | **2.3** | **1.5** | **3.2** | **1.3** | | |

Capability is roughly **double** Proof and Governance. In no account is the blocker "Airtable
can't do this." Every blocker is organizational: nobody owns the outcome, nobody governs the
build, nobody can prove the value.

**So the premise I'm running on: this function's job is organizational change management with
a platform attached, not feature adoption.** Everything below follows from that.

### Three structural patterns — and what's just account noise

**1. Value is never made legible. (6 of 6.)** Not one account has a current, quantified
outcome stated in the language of the person who signs the renewal. Corvus has AI agents in
production and *still* can't substantiate an expansion. Floor & Board hasn't had a
value-realization conversation since kickoff. This is not an adoption problem — Corvus and
Voltaic are adopting fine. It's a translation problem, and it's structural because no artifact,
ritual, or role currently produces the translation.

**2. Transformation is single-threaded on individuals. (4 of 6.)** Floor & Board's vision
"lived in one person's head" and left with them. Corvus is contained to one BU with one
champion. TrailLine is one enthusiastic COO with a hostile user layer beneath. Voltaic is a
builder team with no exec. When transformation depends on a person rather than a structure —
sponsor, CoE, governance path — it dies with the person or never leaves the pocket.

**3. There is no readiness standard, so the motion is unsequenced.** Harbor Lane gets nothing
because it isn't asking. Voltaic gets check-ins it outgrew two quarters ago. TrailLine is
three weeks from a kickoff that will land exactly like the two "transformation" tools that
burned that ops team before. Each CSM is applying the play they personally know rather than
the play the account's stage calls for.

**What's genuinely account-specific** — and which I'd handle as work, not as an input to
methodology: Floor & Board's cross-team automation break (Support owns it, not the CSM),
Meridian's particular review board, TrailLine's kickoff date.

**And the fourth pattern is internal.** The team lost its manager layer, so there is no
inspection surface. Fifteen CSMs are producing fifteen different qualities of work and I
currently have no way to see it except by asking. That constrains how fast anything else can
move.

### The trap in the book

**Voltaic looks like the most advanced account and is the most dangerous.** Self-building
agents, growing seats, technically confident — it presents as Stage 4. But the build is
ungoverned by the customer's own admission, CS has no seat, QBR attendance has fallen two
quarters running, and it renews in **two quarters** into a pricing negotiation we won't be in
the room for. Seat growth without CS influence isn't health; it's a customer that has priced
us as a tool. I'd read any book for this shape.

---

## My top three priorities

**P1 · Days 1–30 — One diagnostic, run across the entire book.**
Every account gets scored on the same four dimensions, by its CSM, in a structured 45-minute
working session, in the Airtable base described in deliverable #2. I'm starting here because
with no manager layer I have neither a shared language nor an inspection surface, and I cannot
coach what I can't see. It does double duty: **how a CSM scores and defends their account tells
me more about their depth in 45 minutes than a month of skip-levels.** I get a book baseline
and a team assessment from the same exercise.

**P2 · Days 15–60 — Build the value-realization spine, ahead of the near-term renewals.**
Proof = 1 across 61% of book ARR that renews inside three quarters. Every account renewing
within three quarters gets a **validated value story** — a quantified outcome, sourced from
adoption evidence, written in the buyer's language, confirmed by the customer — by day 60.
This is the direct commercial linkage: renewal isn't decided by usage, it's decided by whether
the economic buyer can repeat our number back to us. Corvus is the clean test case: strong
production adoption, zero substantiation, CFO and procurement deciding a multi-year expansion.

**P3 · Days 30–90 — Replace personalities with plays and partners.**
An eight-play library keyed to the *binding constraint*, not to account tactics; explicit
boundaries on what a CSM owns versus partners on; and a weekly operating rhythm run out of the
base. This is the answer to fifteen CSMs of varied depth. I don't need every CSM to be
credible with a CFO on AI risk — I need every CSM to correctly diagnose that the account needs
that conversation and to pull the right partner into it.

**What I'm deliberately not doing in the first 90 days**, and why:
- **Not hiring the manager layer.** I want to see the team run the system first. Leads should
  surface through play authorship and diagnostic quality, not tenure. I'd make that call at
  day 90 with evidence.
- **Not re-cutting segmentation or coverage.** It's the intuitive move with a book this
  uneven, and it's a six-month distraction from three renewals I have to survive first.
- **Not building a formal enablement curriculum.** Enablement rides on the plays — CSMs learn
  the methodology by running it on live accounts with me in the room, not in a classroom.

---

## The methodology, and how it connects to money

**Diagnose → find the constraint → run the play that clears it → convert the result into
proof → carry the proof into the renewal.**

Full detail in [`03-transformation-methodology.md`](03-transformation-methodology.md). Two
mechanics make it work when a mid-tenure CSM runs it:

**The constraint picks the play, not the average.** An account's next move is determined by
its *lowest* dimension, not its overall maturity. Meridian averages 3.5 and is completely
stuck — because Governance is the gate and Capability being a 4 doesn't help. Corvus averages
2.25 and is one artifact away from an expansion. This is why the same diagnostic can produce
sound recommendations for a CSM who doesn't yet have the pattern library to reason it out
themselves.

**Below Stage 1, Proof leads; at Stage 1 and above, Sponsorship leads.** I needed this second
rule after the model gave a wrong answer on Harbor Lane — it wanted me to recruit an executive
sponsor for something nobody there has seen yet. You can't sponsor an abstraction. At Stage 0
you prove one narrow thing first, and *then* you have something to sponsor.

**The commercial linkage is the value story, and it's a dated artifact, not a conversation.**
Adoption signals → quantified outcome → narrative in the buyer's language → validated by the
customer → carried into renewal and expansion. Renewals are lost in the gap between "they use
it a lot" and "here's what it was worth." Expansion is won by closing that gap early enough
that procurement is arguing about scope rather than value. The base enforces the dating: a
value story older than one quarter on an account renewing within two is flagged as a risk in
the same view as a churn signal, because it is one.

---

## Operationalizing it across 15 CSMs

**The ownership rule:** a CSM must always own being the person who knows what their account
needs. **A CSM must never have to be the smartest technical person in the room.**

| CSM always owns | Partner leads, CSM orchestrates |
|---|---|
| The diagnostic and its evidence | AI solution architecture (Solutions/SE) |
| The stakeholder and sponsor map | Governance, risk and security artifacts (Trust + Product) |
| The value story and the executive narrative | Commercial construct and procurement path (AE) |
| The customer's operating rhythm and the transformation plan | Break/fix and technical escalation (Support) |

This is what makes varied depth a staffing question instead of a performance problem. The
TrailLine CSM is one of the strongest builders on the team and newer to executive engagement —
so they own the ops-team re-contract, which is exactly their strength, and I take the COO
conversation with them for the first two cycles. The Corvus CSM has excellent instincts and
lighter technical depth — so the base drafts the quantified narrative and Solutions validates
the numbers, and the CSM does what they're genuinely best at: getting the CFO's office to
believe it. Neither is asked to become someone else.

**Inspection, run weekly out of the base — not out of slides:**

*Leading (I own these):* diagnostic currency (% of book scored within 90 days); sponsor
coverage (% with a named exec sponsor and ≥3 mapped threads — today that's 1 of 6); **proof
coverage** (% with a customer-validated value story dated within a quarter — today 0 of 6);
play cycle time; partner pull-through rate.
*Lagging:* GRR, NRR, CS-sourced expansion pipeline, and **renewal surprises, target zero** —
a surprise at renewal is a diagnostic failure 6 months earlier, and it's the metric I'd be
judged on.

*Rhythm:* Monday 60-minute book review in the base, three accounts deep and rotating.
Biweekly 1:1s that walk one account against its diagnostic rather than reporting status.
Monthly play retro where CSMs — not I — retire and author plays. Quarterly re-baseline plus a
customer-facing value review, which is the forcing function that keeps Proof from decaying
back to 1.

I'd report to leadership at day 45 and day 90 out of the same base I inspect the team in.
No parallel deck economy.

---

## How the build carries this

The Airtable prototype ([`airtable-build/`](../airtable-build/)) implements P1 and P2. A CSM
opens their Cockpit and sees their accounts ranked by ARR-at-risk against constraint, the
recommended play with its first three moves, and what's due this week. They run the diagnostic
inside a customer session; an AI field classifies the stage and drafts the rationale; a second
AI field recommends the play from the library; a third turns adoption evidence into a first
draft of the value story in the buyer's language. An automation flags any account inside two
quarters of renewal whose value story is stale or missing. The Director view is the whole book
on one screen: stage distribution, proof coverage, ARR at risk by constraint, plays overdue.

That's the leverage test. The system carries the pattern recognition so a CSM doesn't have to
have fifteen years of it, and it makes fifteen people's judgment visible in one place — which
is the specific thing this team lost when it lost its managers.

**The honest caveat:** the AI drafts, the human validates. A value story is not real until the
customer says the number back to us, and the base tracks `Draft → Reviewed → Customer-validated`
precisely so we never walk an AI-generated number into a CFO conversation unchecked.

---

*Assumptions this brief depends on — including which ones would change my priorities if wrong —
are in [`appendix/assumptions.md`](../appendix/assumptions.md).*
