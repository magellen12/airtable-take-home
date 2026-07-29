# Operating Model — running this across 15 CSMs

The methodology is the *what*. This is the *how it holds up* when fifteen people of varied
tenure and technical depth run it, with no manager layer between them and me.

---

## 1 · The starting condition

- **15 HTCSMs**, varied tenure and technical depth.
- **No manager layer.** Fifteen direct reports, or something close to it.
- Some CSMs can credibly lead AI conversations with executives; others are strong relationship
  managers who can't — *yet, and in some cases ever, and that has to be fine.*
- No shared methodology, so no shared language, so **no inspection surface**.

That last one is the binding constraint on me, the same way governance is the binding
constraint on Meridian. I can't coach, prioritize, staff, or defend the book against what I
can't see. Which is why the first 30 days are spent building a surface rather than fixing
accounts.

---

## 2 · The ownership boundary, the skills matrix, and pairing

> **A CSM must always own being the person who knows what their account needs.**
> **A CSM must never have to be the smartest technical person in the room.**

| CSM always owns | Partner leads, CSM orchestrates | Never the CSM |
|---|---|---|
| The diagnostic and its evidence | AI solution architecture, agent design — **Professional Services** | Break/fix and technical escalation — **Support** |
| The stakeholder and sponsor map | Governance, risk, security artifacts — **Security & Risk** + **Product** | Contract paper and legal — *whoever owns contracting* |
| The value narrative and executive story | Commercial construct, renewal & procurement path — **Sales + Renewals** | |
| The customer's operating rhythm | Quantitative validation of value claims — **Value Validation** | |
| The transformation plan and its sequencing | | |

**Bold names are the five partners the role explicitly names** — *"partner closely with Renewals,
Support, Professional Services, Product, and Sales"* — so "pull in a partner" points at a function
I can actually point to, never a favour.

**Everything in italics is a capability, not an org-chart claim.** I don't know how this company is
arranged beyond those five, so rather than invent teams I've named **what has to be produced and
who has to stand behind it**:

| Capability | What it means here |
|---|---|
| *Security & Risk* | Whoever produces customer-facing AI risk and controls artifacts — the P5 dependency |
| *Value Validation* | Whoever can stand behind a quantitative claim before it reaches a customer's CFO — the P4 dependency |
| *Contracting* | Whoever owns contract paper and legal review |

Each may be a dedicated function, a corner of an existing one, or nobody yet. **Mapping them to
real owners is a day-one question**, and the first two are live assumptions rather than details:
if the security-and-risk capability doesn't exist in customer-facing form, P5 is a materially
longer play than it looks (see [`../appendix/assumptions.md`](../appendix/assumptions.md)).

I'd rather name a capability I can defend than a team I'd be guessing at — and the same discipline
applies to the plays, which is why [`05-play-library.md`](05-play-library.md) carries the same note.

### The skills matrix — the artifact that makes pairing systematic

Person-dependence isn't only a customer problem (pattern 2); it's ours too — account outcomes
currently track individual CSM strengths rather than a common motion. The fix is a matrix across
the whole book, scored on three axes, that turns "who's good at what" from tribal knowledge into
a staffing input:

| Axis | 1 | 5 |
|---|---|---|
| **Builder depth** | Can't configure a base | Ships production agents, reverse-mentors others |
| **Executive presence** | Comfortable with the day-to-day user | Credible across the table from a CFO |
| **Domain** | Generalist | Deep in the customer's vertical |

**This converts varied depth from a performance problem into a staffing question** — and the move
is **pairing of complements, not reassignment.** You don't take an account away from a strong
builder because it has hard executive dynamics; you pair them with executive presence for the
threads that need it, and they keep the account and grow. Two worked examples from the book:

- **TrailLine.** The CSM is one of the team's strongest builders (builder depth 5, executive
  presence 2), newer to executive engagement. They *keep* the account and own the ops-floor
  re-contract — the genuinely hard part and exactly their strength. They're paired with an
  exec-presence partner for the COO thread through the first two cycles. I sit in early, but the
  system is the pairing, not me being the hero.
- **Corvus.** The CSM has excellent instincts and relationships and lighter technical depth
  (executive presence 4, builder depth 2). The base drafts the numbers, the value-validation
  partner checks them, and the CSM does what they're best at — getting the CFO's office to believe it.
  Not asked to become a solutions architect.

Neither person is being fixed. Both are being deployed — and the pairing is visible in the base,
so it's a decision I can inspect, not a favour I remember to do.

---

## 3 · Operating rhythm

| Cadence | Session | Length | What actually happens |
|---|---|---|---|
| **Weekly**, Mon | **Book review** | 60 min | Run live in the base, never in slides. Constraint distribution, ARR at risk, plays past their cycle time, stale value narratives. Three accounts deep, rotating — everyone presents roughly monthly. |
| **Biweekly** | **1:1** | 45 min | Walk *one* account against its diagnostic. Not a status update — a coaching conversation about a specific judgment they made. |
| **Monthly** | **Play retro** | 60 min | Which plays hit their definition of done, which didn't, what we retire and what we add. **CSMs author plays; I approve them.** |
| **Quarterly** | **Book re-baseline** | half day | Every diagnostic refreshed. Stage movement reviewed. This is the anti-decay mechanism. |
| **Quarterly**, per account | **Customer value review** | 60 min | Customer-facing. The forcing function that keeps Value evidence from sliding back to 1. |
| **Day 45 / Day 90** | **Leadership readout** | — | Out of the same base I inspect the team in. No parallel deck economy. |

**The rule that makes the weekly work:** if it isn't in the base, it didn't happen, and I won't
discuss it. Not bureaucracy — it's the only way a team of fifteen with no managers gets a
single version of the truth.

---

## 4 · What I measure

### Leading — I own these, reviewed weekly, all from the base

| Metric | Today | 90-day target | Why it's the leading indicator |
|---|---|---|---|
| **% of book staged** — accounts scored on the diagnostic | 0% | 100% | No diagnosis, no coaching, no prioritization |
| **Stage progression QoQ** — accounts that advanced a stage | — | Baseline, then positive | The maturity-progression metric; the whole point is movement, not a static score |
| **Sponsor coverage** — % with a named exec sponsor and ≥3 mapped threads | **33%** (2 of 6 — Meridian and TrailLine) | 70% | Single-threading is how Floor & Board happened |
| **Value coverage** — % with a customer-validated narrative ready ≥1 quarter before renewal | **0%** | 100% of accounts renewing within 3Q by day 60 | This is the renewal predictor |
| **Governance body in place** — % of Stage 2+ accounts with a CoE or review path | low | rising | Structure is the durable fix for person-dependence |
| **Play cycle time** — days from play start to DoD | — | Baseline by day 60, then compress | Tells me where the team is stuck vs. slow |
| **Partner pull-through** — % of plays with the right partner engaged | — | >80% | Are CSMs asking for help, or drowning quietly? |

> **A note on sponsor coverage, because building the base changed the number.** An earlier draft
> said 1 of 6. Run against the live data, this definition returns **2 of 6** — Meridian and
> TrailLine. TrailLine qualifies on the letter of it: a named exec sponsor plus three mapped
> threads. But its three threads are skeptical ops users, not sponsor threads, which is arguably
> not what this metric is trying to measure. I've left the number honest rather than tightening
> the definition until it returned the answer I'd already written down. It's a good example of why
> the definition matters as much as the target.

### Lagging — what I'm accountable for

GRR · NRR · adoption · expansion influence · **value realization** · **renewal surprises, target
zero**.

That last one is the one I'd want to be judged on. **A surprise at renewal is a diagnostic
failure six months earlier.** If the system works, nothing at a renewal is new information.

**On customer health specifically:** the four-dimension diagnostic *is* our customer-health
instrument — I'm not against measuring health, I'm against a single composite health score that
averages the binding constraint away. Voltaic is exactly why: a one-number health score built on
seats and usage would render it green while it's two quarters from being repriced. A
*multidimensional* health read keeps the score that predicts the loss (Value evidence 2,
Governance 1) visible instead of drowning it in the two that look fine.

### Team health

Plays run per CSM · DoD hit rate · play authorship (who is contributing to the library) ·
diagnostic quality — **I personally grade three diagnostics a week**, which is roughly the
whole book monthly and is my highest-leverage hour.

**What I refuse to measure:** activity counts. Calls logged, QBRs held, emails sent. Voltaic
has had QBRs the whole time and is two quarters from being repriced by people who think we're
a tool. Activity metrics would have shown that account green.

---

## 5 · Enablement — carried by the plays, not a curriculum

No classroom in the first 90 days. The methodology is learned by running it:

1. **Week 1–2:** I run two live diagnostics with the team watching. Real accounts, real
   customers, including one I'll get wrong.
2. **Week 3–4:** Every CSM runs their own, and I sit in on the first one for each of the
   fifteen. That's fifteen hours and it's the best-spent time in the quarter — it's a full
   skills assessment of the team disguised as account work, and it's what populates the skills
   matrix I pair from.
3. **Ongoing:** every play carries its own artifact template and DoD, so running the play *is*
   the training. Nobody starts from a blank page.
4. **Peer-led:** the CSM who runs a play well presents it at the monthly retro and their
   version becomes the template. The library is authored by the team, which is the only way it
   gets used.

**A stated position on the depth gap:** I don't intend to turn fifteen relationship managers
into fifteen solutions architects, and I don't think the assessment's premise requires it. I
need every CSM to *diagnose* at a high level and to know which conversation they should not be
having alone. Depth is bought with partners; judgment can't be.

---

## 6 · Leading a team that just lost its manager layer

**The first thing I say to them:** the manager layer disappearing is not their failure, and I'm
not arriving with a verdict. The first 30 days are me learning the book *through* them.

**The diagnostic is the coaching instrument.** I never grade a person — I grade an account,
with them, using the same four dimensions. How someone scores their own account, what evidence
they bring, and how they respond when I push on a 4 tells me more than any competency
framework. It also means every developmental conversation is anchored in a real customer
rather than in an abstraction about their skills.

**On the manager layer:** I'm not hiring it in the first 90 days. Leads should surface through
play authorship and diagnostic quality, not tenure or volume — and I want the evidence before
I make a decision that reshapes fifteen people's reporting lines twice in one year. I'd expect
two or three to be visible by day 60, and I'd make the call at day 90 with the base as
evidence.

**Fifteen direct reports is not sustainable and I'd say so out loud** rather than pretend the
system solves it. What the system buys me is that inspection is asynchronous — I read the base
before the 1:1 instead of spending the 1:1 finding out what's happening. That's the difference
between fifteen reports being temporarily survivable and immediately broken.

**On trust:** the fastest way to lose this team is to arrive with a methodology and no
demonstration that I can run it. So I run the two hardest accounts' first plays myself, in
front of them — Meridian's governance case and Voltaic's re-entry — and I let them watch me
get one wrong.

---

## 7 · The 90-day sequence

| Days | Focus | Done means |
|---|---|---|
| **1–14** | Meet the team. Two live diagnostics run by me. Base stood up with the six accounts seeded. Skills matrix started. | Team has seen the instrument work |
| **15–30** | Every CSM stages their own book. I sit in on fifteen first sessions (this populates the skills matrix). Pairings set. **TrailLine kickoff re-contract ships — it's in 3 weeks and won't wait.** | % of book staged = 100%; I have a real read on team depth |
| **31–45** | Value narratives started on every account renewing within 3Q — Floor & Board, Voltaic, Corvus. Play library v1 published. Weekly book review begins. | Day 45 leadership readout, from the base |
| **46–60** | Value narratives customer-validated on the three near-term renewals. Floor & Board re-sponsor play in flight (CoE seeded behind it). Voltaic governance insert in flight. | Value coverage 100% on near-term renewals |
| **61–90** | Meridian governance case with Security & Risk / Product. Corvus expansion narrative to the CFO's office. First monthly play retro with CSM-authored plays. Manager-layer recommendation. | Day 90 readout; a book that runs without me in every room |

**The forcing dates that drive this ordering**, not my preference: TrailLine's kickoff is in
three weeks. Voltaic renews in two quarters. Floor & Board's renewal conversation starts in
two. Those three dates set the sequence — everything else is fitted around them.
