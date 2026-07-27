# The Play Library

**Global consistency, local customization.** The play library *is* the global consistency: a shared
set of moves, keyed to constraints, with a common artifact and a common bar for done. What it
deliberately does not standardize is how any individual CSM runs it with their customer — the
sequencing, the language, who they approach first, the creative spin. **Consistency is the floor,
not the ceiling.**

That split is the whole design. This is the most tenured team in the company and they know their
customers better than I will. Standardizing *what* we do gives us a shared language, an inspection
surface, and a way for the newest CSM to start from something rather than nothing. Standardizing
*how* would waste the thing that's actually scarce here — fifteen people's judgment about their own
accounts.

So every play below is written in two parts:

| | |
|---|---|
| **The standard** *(global — this is the play)* | The constraint it clears, the trigger, the partner, the artifact, and the signal we're looking for. Changing these changes the play, and that happens in the monthly retro, not in the field. |
| **The latitude** *(local — this is the CSM's)* | Sequencing, framing, who to approach and in what order, what to say, and how much of it to run themselves versus with a partner. |

[`03-transformation-methodology.md`](03-transformation-methodology.md) explains *why* a play gets
picked — the diagnostic scores four dimensions, the lowest is the binding constraint, the constraint
selects the play. This file is *what the play is* once it's picked.

---

## A note on how "done" is written

Every definition of done below is phrased as **a signal we look for on the customer's side**, not
as a prediction that the customer will do it, and not as something we can commit to on their
behalf. That distinction matters more than it sounds:

- We control our activity. We don't control whether an executive repeats our number back to us.
- Writing done as *our* activity — "we delivered the readout" — is the failure mode the bar exists
  to prevent, because it lets a play close with nothing having changed.
- Writing it as a customer *signal* keeps the bar honest while being clear about what it is: an
  observation we're waiting for, which may not arrive. **A play that doesn't reach its signal isn't
  a failed CSM — it's information**, and it's what the monthly retro is for.

Where a play below says "the customer does X," read it as *the observable signal that this play
worked*, not as a commitment anyone has made to us.

---

## A note on partner names

Every play names a partner, because **"pull in a partner" has to mean a real function rather than a
favour** — that's the whole point of the ownership boundary. But I don't know how this organization
is actually arranged, so the plays name **the capability the play needs**, not an org chart I'd be
guessing at.

- **Five partners the role names, so I use their names:** *"partner closely with Renewals, Support,
  Professional Services, Product, and Sales."* Those five I can point to.
- Where I don't know who owns something, I describe **what has to be produced and who has to stand
  behind it**. Two plays need this: **value validation** (whoever can stand behind a quantitative
  claim before it reaches a customer's CFO) and **security & risk** (whoever produces
  customer-facing risk and controls artifacts). Wherever those sit here — a dedicated function, a
  corner of Product, an individual — that's who the play means.

**Mapping those two to real owners is a day-one question**, and it's a live assumption rather than
a detail (see [`../appendix/assumptions.md`](../appendix/assumptions.md)). If the security-and-risk
capability doesn't exist in a customer-facing form, P5 is a materially longer play than it looks
here, and I'd want to know that before promising a timeline to a sponsor.

---

## The library at a glance

Eight plays, four constraints, two-to-three plays each. **The library is sized to the failure
modes, not to the account count** — which is why it doesn't grow when the book does. A library of
thirty plays is a library nobody opens, and the tell is always the same: plays named after
customers.

| # | Play | Clears | Stage | Typical | Artifact produced | Signal we're looking for |
|---|---|---|---|---|---|---|
| **P1** | Prove One Thing | Value evidence | 0 | 4–6 wks | Before/after on one existing workflow | The result gets retold inside the customer's org without us in the room |
| **P2** | Re-Sponsor | Sponsorship | 1–2 | 6–8 wks | Named exec owner + written charter + ≥3 threads | An executive attaches their name to an outcome and a date |
| **P3** | Kickoff Re-Contract | Adoption | 1 | 3 wks | Success criteria in the *user* lead's words | The user-side lead carries those criteria to their own exec |
| **P4** | Quantify & Translate | Value evidence *(commercial)* | 2–3 | 3–4 wks | Value narrative in the buyer's language + evidence pack | The economic buyer uses our number as their own |
| **P5** | Governance Case | Value evidence *(governance)* | 3 | 6–10 wks | AI risk-and-controls case + reference architecture | A review body clears at least one use case |
| **P6** | Governance Partner Insert | Governance | 2, fast-moving | 4–6 wks | Agent inventory + adopted standard + sprawl/cost view | A standard gets adopted and we're consulted on new builds |
| **P7** | Spread From the Pocket | Adoption | 2 | 8–12 wks | Reusable pattern + CoE charter + second team live | A second team runs in production under a governing body |
| **P8** | Renewal Value Review | Value evidence | any, at T–2Q | 2 wks | Dated value narrative + written expansion hypothesis | Nothing in the renewal conversation is new information to us |

**P5, P6 and P7 are one motion viewed from three angles** — governance. It's the structural answer
to person-dependence: the durable fix is a structure, not a better individual. I'd own that motion
across the book early, because it's the one no CSM should be sent into alone in month one.

---

## P1 · Prove One Thing

> A healthy account that has never seen AI do anything for *them*. You don't sell a vision — you
> take one workflow they already run, rebuild that exact workflow, and let their own team run it
> while you capture the before-and-after together. One workflow. Nothing adjacent.

**The standard.** Clears **value evidence** at **Stage 0**. Triggered when the product is healthy
and AI simply isn't on the agenda. Partner: **Professional Services** builds it. Artifact: a
before/after measurement on one workflow the customer already runs, plus one number they agree
with. Typical **4–6 weeks**.

**Signal we're looking for:** the result gets retold inside their organization without us present.
That's the first point the outcome exists independently of us — and it's the raw material P2 needs,
because **you can't recruit a sponsor for an abstraction.**

**The latitude.** Which workflow, how the demonstration is staged, whether the CSM builds alongside
Professional Services or hands off entirely, and how hard to push for a number versus letting the
team's own reaction carry it. A CSM who knows their customer's culture may find the "number" lands
better as a time saving, a headcount reallocation, or an error rate — that's their read to make.

**A default sequence, not a mandate.**
1. Find the workflow with the most manual downstream work — by asking the people who do it, rather
   than inferring it from usage data or letting an exec pick on their behalf.
2. Build a narrow version of exactly that workflow with Professional Services.
3. Run a short session where **their** team drives, and capture the before/after in the room.

**How it fails.** Scope creep, nearly every time — the moment it grows a second use case it becomes
a project, and projects at Stage 0 tend to die in someone's roadmap. Second failure mode: we run
the session instead of the customer, and produce a demo rather than a proof.

---

## P2 · Re-Sponsor

> The champion left and the roadmap left with them. You map who inherited that person's *scope*,
> use whatever is already working as the proof asset, and open a level above the vacancy — because
> whoever inherited the title rarely inherited the conviction.

**The standard.** Clears **sponsorship** at **Stages 1–2**. Triggered by a low sponsorship score, or
automatically by a champion departure regardless of scores. Partners: **Sales, Renewals**. Artifact:
a named executive owner, a written charter with one outcome and a date, and at least three mapped
threads. Typical **6–8 weeks**.

**Signal we're looking for:** an executive attaches their name to a specific outcome and a date —
in writing or in front of their peers. Verbal enthusiasm in a 1:1 is what tends to evaporate on the
next departure.

**The latitude.** Who to approach and in what order, whether to lead with the working pilot or with
the risk, how much to involve Sales versus keeping it a CS conversation, and how formal to make the
charter. Some customers will sign a one-page charter; others will treat that as bureaucracy and the
same commitment has to be built in a room. The CSM reads which.

**A default sequence, not a mandate.**
1. Map every remaining relationship and work out who inherited the departed champion's scope —
   often it's split across two or three people, and sometimes none of them know it.
2. Package whatever is already working as the proof asset. Recruiting an executive to something
   real and small is generally easier than recruiting them to a roadmap.
3. Open above the vacancy rather than at it.
4. Land the charter: one outcome, one owner, one date, written down.

**Why three threads.** The minimum exists to stop us re-creating the single-threaded dependency we
just watched break. One warm relationship isn't sponsorship recovered; it's the same exposure with
a new name on it.

**How it fails.** We accept the friendliest available person rather than the one with the budget
line. Or we run it before anything works — sponsorship recruited for a roadmap is a meeting;
sponsorship recruited for a working pilot is a charter. If nothing works yet, P1 comes first.

---

## P3 · Kickoff Re-Contract

> An executive bought a vision and the team who has to live with it was never asked. Before
> kickoff, you sit with the skeptical operational lead alone and ask what the last two tools cost
> them. Then you rebuild the kickoff around one workflow that *removes* work from that team.

**The standard.** Clears **adoption** at **Stage 1**. Triggered when the sale was made above the
user layer and the user layer is cold — the tell is an enthusiastic executive and an operations org
that hasn't asked a single question. Partner: **Professional Services**. Artifact: success criteria
written in the user-side lead's words, not ours. Typical **3 weeks**.

**Signal we're looking for:** the user-side lead carries those criteria to their own executive.
Criteria we drafted and they nodded at is the thing that tends to fail in month four.

**The latitude.** How to open the pre-kickoff conversation, how much of the original agenda to cut,
whether the CSM runs the ops-floor thread themselves or splits it with a partner who has more
executive presence, and how visible to be at the kickoff itself. Cutting a vision session an
executive is expecting is a judgment call about that specific relationship — I'd expect a CSM to
make it, not to ask.

**A default sequence, not a mandate.**
1. Time alone with the skeptical operational lead before kickoff. One question, then listening.
2. Rebuild the kickoff around a single workflow that takes work off that team.
3. Position the user-side lead to present the success criteria — we're in the room, not at the
   front of it.

**How it fails.** We write the success criteria in our language and ask for sign-off. Adoption
stalls in month four and everyone calls it a change-management problem. The other failure is
running it on a team that's already engaged, which costs three weeks and reads as though we doubt
them.

---

## P4 · Quantify & Translate

> Real value exists and nobody who signs the check can describe it. You baseline the workflow with
> the champion, have the number independently validated *before* anything is written down, and get
> the champion to confirm it before procurement or a CFO's office ever sees it.

**The standard.** Clears **value evidence** where the audience is **commercial** — a CFO,
procurement, a P&L owner. **Stages 2–3**. Partner: **whoever owns value validation** — the function
that can stand behind a quantitative claim externally. Artifact: a value narrative in the economic
buyer's language plus a traceable evidence pack. Typical **3–4 weeks**.

**Signal we're looking for:** the economic buyer uses our number as their own. That's also the
definition of *value coverage*, a leading metric I'd own — and the book currently sits at zero.

**The latitude.** Which workflow to baseline, which metric to convert into, how to sequence the
champion and the buyer, and how much of the narrative the CSM writes themselves versus drafts from
the base and edits. A CSM whose strength is executive presence rather than build depth should lean
on the base and the validation partner for the numbers and spend their own effort on the room —
that's deployment, not a gap being covered.

**A default sequence, not a mandate.**
1. A working session with the champion to baseline the workflow — volume, cycle time, headcount
   touched.
2. The validation partner checks the conversion into the buyer's metric *before* it's written
   anywhere. A number that leaves our building unvalidated is a liability.
3. The champion confirms the numbers explicitly, in their own words.
4. Executive readout, delivered *with* the champion rather than about them.

**Don't run it when the audience is a review body.** Same constraint, different artifact: a risk
committee doesn't want a savings figure, it wants a controls case. That's P5, and confusing the two
is the most common misread of the value-evidence constraint.

**How it fails.** An unvalidated estimate walks into a CFO conversation and costs us credibility on
every future number. The `Draft → Reviewed → Customer-validated → Stale` status gate exists to make
that specific mistake structurally difficult rather than merely discouraged.

---

## P5 · Governance Case

> A mature account with a committed sponsor, stuck behind a risk review body, and we've been
> relaying messages through the sponsor for a quarter. You stop relaying: ask for direct access,
> get the actual evaluation criteria in writing, and build the controls case against *those*
> criteria rather than sending a generic security packet.

**The standard.** Clears **value evidence** where the audience is a **governance body**.
**Stage 3**. Partners: **whoever owns security and risk artifacts**, plus **Product**. Artifact: an AI risk-and-controls case, a
reference architecture, and answers to the body's stated objections. Typical **6–10 weeks**.

**Signal we're looking for:** a review body clears at least one use case. Not submission, and not
the sponsor being satisfied with what we submitted.

**The latitude.** How to ask for direct access without stepping over the sponsor, how much of the
case the CSM assembles versus orchestrates, and how to keep the sponsor engaged across two months
of slow movement. That last one is mostly craft, and it's the part I'd expect to vary most by
customer.

**A default sequence, not a mandate.**
1. Ask the sponsor for direct time with the review body. Relaying loses the objection's actual
   wording, which is usually the only part that matters.
2. Ask whether the evaluation criteria exist in writing. If they do, that beats inferring them
   from relayed objections; if they don't, that itself tells you how the board actually decides.
3. The security-and-risk partner and Product build the case and reference architecture against
   those specific criteria.
4. Throughout: keep the sponsor warm. **Sponsor patience is the depreciating asset in this play.**

**The distinguishing signal.** A sponsor pushing hard while nothing moves is almost never a
sponsorship problem. If you read it as one you'll run P2 at an account that already has the thing
P2 produces.

**How it fails.** A generic packet against assumed criteria. Or it runs past the sponsor's
attention span — at which point the constraint has quietly moved back to sponsorship, and the play
should be re-sequenced rather than pushed. I'd set a checkpoint rather than let that happen
silently.

---

## P6 · Governance Partner Insert

> The account that outgrew us. Seats growing, agents everywhere, no CS seat, and the check-ins have
> stopped landing. You don't ask for partnership — you offer an agent inventory, come back with a
> sprawl-and-cost view they can't produce themselves, and propose a lightweight standard they own
> and we review. That standard is the seat.

**The standard.** Clears **governance** at **Stage 2, fast-moving** — high adoption, high build
velocity, no structure. **This is the play for the account that looks best in a QBR deck.**
Partners: **Professional Services**, plus **whoever owns security and risk artifacts**. Artifact: an agent inventory, a governance
standard the customer adopts, and a cost-and-sprawl view. Typical **4–6 weeks**.

**Signal we're looking for:** a standard gets adopted *and* we're consulted on new builds. Adoption
of a document alone isn't it — the test is whether the next thing they build happens with us in the
room.

**The latitude.** How to price and position the inventory, how lightweight the standard should be,
whether to bring the security-and-risk partner in early or after the sprawl view lands, and how to time the
executive re-entry relative to any commercial conversation. Customers vary enormously in how much
governance they'll tolerate from a vendor; that read is local.

**A default sequence, not a mandate.**
1. Offer the agent inventory — narrow, fast, low friction. It's a useful thing with a diagnostic
   inside it.
2. Return with the sprawl and cost view. This tends to be the asset that changes the relationship,
   because it's the one thing they generally can't build for themselves.
3. Propose a standard **they own and we review**. Their ownership is what makes it survive; our
   review right is what makes it a seat.
4. Use that seat to re-enter at executive level, ahead of pricing.

**Wait for them to volunteer the problem.** Unrequested governance from a vendor can read as a land
grab. Where a customer has already raised ownership or cost of their own AI sprawl, that's the
opening and the play is straightforward. Where they haven't, I wouldn't assume the concern exists —
the first move is finding out whether it does, not asserting that it should.

**How it fails.** We mistake the inventory for the play and stop after delivering a nice artifact.
The inventory is the wedge, the standard is the play, the seat is the point. And if a customer
declines the inventory outright, that's real information: the honest move is to change the goal
from expansion to defending the commercial position, rather than trying to relationship our way in.
**Not every account gets to be a transformation account.**

---

## P7 · Spread From the Pocket

> Real value exists in exactly one pocket and it isn't spreading. You ask the champion for one
> introduction to a peer, package what the first team built as a reusable pattern rather than a
> bespoke build, and stand up a standing cross-team forum that the champion chairs.

**The standard.** Clears **adoption** at **Stage 2**, and produces governance structure as its
durable output. Partner: **Professional Services**. Artifact: a reusable pattern, a CoE charter, and
a second team in production under a governing body. Typical **8–12 weeks**.

**Signal we're looking for:** a second business unit running an AI workflow in production, under a
governing body. Both halves matter — a second team without a forum is just a second pocket, and
we've doubled the person-dependence rather than fixing it.

**The latitude.** Which peer to target, how formal the forum is, who chairs it, how much of the
pattern is genuinely reusable versus rebuilt, and how long to let the first pocket mature before
spreading. The forum can be a chartered CoE or a standing monthly call — the structure matters, the
formality is a read on the customer.

**A default sequence, not a mandate.**
1. Ask the champion for one named peer introduction. Internal referral tends to beat our outreach.
2. Package the first build as a reusable pattern with Professional Services.
3. Onboard the second team against that pattern.
4. Stand up the cross-team forum, and let the original champion chair it. Ours to convene, theirs
   to run.

**Requires a proven pocket.** This is a spreading play, not a starting one. Spreading a fragile
workflow produces two fragile workflows and a champion who now looks wrong in front of a peer.

**How it fails.** We treat it as a pipeline motion and pitch the second team ourselves. The
referral is the mechanism; without it this is cold outreach with a logo on it.

---

## P8 · Renewal Value Review

> Two quarters before a renewal — not two weeks — you confirm the value narrative is
> customer-validated rather than merely drafted. If it isn't, that *is* the play. Then a joint
> session with Sales and Renewals, and you ask the sponsor directly what would make them not renew.

**The standard.** Clears **value evidence** at **any stage**, triggered at **T–2 quarters**.
Partner: **Renewals**. Artifact: a dated value narrative plus a written expansion hypothesis.
Typical **2 weeks**.

**Signal we're looking for:** nothing raised in the renewal conversation is new information to us.
**This is the outcome measure I'd volunteer to be judged on — renewal surprises, target zero** —
because a surprise at renewal is usually a diagnostic failure six months earlier, and it's the only
lagging measure that indicts the system rather than the market.

**The latitude.** How to run the session, how much Sales and Renewals lead versus support, how
directly to ask the hard question, and what an expansion hypothesis looks like for that customer.

**A default sequence, not a mandate.**
1. Check the narrative's status first. `Draft` or `Stale` means stop and run P4 — treat this as the
   trigger it is, not a box to clear.
2. Joint session with Sales and Renewals, two quarters out.
3. Ask the sponsor what would make them not renew, and record the answer as given.
4. Land the dated narrative and a written expansion hypothesis.

**This is the one play a CSM doesn't choose.** An automation in the base creates it whenever an
account enters the renewal window without a current value narrative. The plays that get skipped are
the ones that depend on somebody remembering — so this one doesn't.

**How it fails.** It gets run as a formality against a stale narrative, which converts a churn
signal into a checkbox. The status field is the guard: a narrative older than a quarter on a
near-term renewal is flagged in the same view, with the same weight, as a support escalation.

---

## What's deliberately *not* in the library

Naming the absences is how you tell whether a library has a point of view.

| Not a play | Why not |
|---|---|
| **The QBR** | It's a meeting, not a motion. An account can have a full history of QBRs and still be drifting toward being repriced — the cadence proves nothing on its own. |
| **The executive dinner** | Relationship maintenance is real work and it clears no constraint. It's possible to hold the relationship and lose the roadmap. |
| **The training webinar** | Enablement rides on the plays. A workflow that removes work tends to spread; a curriculum tends not to. |
| **"Increase adoption"** | An outcome with no owner, no artifact and no definition of done. P1, P3 and P7 are the three specific ways adoption actually moves. |
| **The health-score save** | It presumes a composite score told you something. The four dimensions fail independently, and the lowest one is the one that predicts. |

---

## Where the plays land in this book

The point of the library is that six accounts produce six different plays from one diagnostic —
**the variation lives in the play library rather than in the CSM's personality.** Current
assignments live in the base (`Account Plays`), with owners, partners, dates and status; this is the
summary view.

| Account | Binding constraint | Primary play | Queued behind it |
|---|---|---|---|
| Floor & Board | Sponsorship | **P2** Re-Sponsor | **P7** — a structure, so the account survives the next departure |
| Meridian | Value evidence *(governance audience)* | **P5** Governance Case | P4 |
| TrailLine | Adoption | **P3** Kickoff Re-Contract | P1 |
| Corvus | Value evidence *(commercial audience)* | **P4** Quantify & Translate | P7 |
| Harbor Lane | Value evidence *(Stage 0)* | **P1** Prove One Thing | P2 |
| Voltaic | Governance | **P6** Governance Partner Insert | P8 |

**Sequencing is how the system handles accounts with two constraints** — which is most of them. The
lowest-score rule is blunt on purpose; a weighted multi-factor model would be more accurate and
less usable, and a methodology fifteen people won't run is worth less than a blunt one they will.

---

## How the library stays alive

A play library decays in two directions: it bloats with plays nobody runs, and it goes stale as the
book changes. Both are handled in the monthly retro (see
[`04-operating-model.md`](04-operating-model.md), §3).

- **CSMs author plays; I approve them.** The CSM who runs a play well presents their version at the
  retro and it becomes the template. A library authored solely by a director is a library nobody
  asks about — and **play authorship is one of the two signals I'd use to identify leads**, the
  other being diagnostic quality.
- **This is where local customization becomes global consistency.** A CSM's creative spin on P4
  isn't a deviation to be corrected; it's a candidate for the standard. The retro is the mechanism
  that promotes it — which is what keeps the floor rising instead of the library ossifying.
- **Retire rule.** A play not run in two quarters, or one that misses its signal more often than it
  reaches it, comes out or gets rewritten. The retro reviews that by play, never by person.
- **Adding a play requires a constraint it clears.** If a proposed play doesn't clear one of the
  four dimensions, either it isn't a play or we've found a fifth dimension. A fifth is plausible —
  change-management capacity is my candidate — but not a seventh. At seven, nobody scores honestly.
- **Override rate is the health check on the mechanism itself.** If CSMs override the recommended
  play often — I'd watch a threshold around 20% — the model is wrong rather than the team, and the
  recorded override reasons are the data for fixing it. That field exists for exactly this.

## The honest gaps

**All eight plays are specified to the depth on this page. Five carry a built artifact template in
the base — P1, P2, P4, P6, P8 — and three don't yet: P3, P5, P7.** A play without a template still
asks the CSM to start from a blank page, which is the tax the library exists to remove. P5 is the
one I'd build first: it's needed soonest and no one has run it before.

**Second, the bars are demanding on purpose and some will prove too demanding.** "The economic
buyer uses our number as their own" is a signal the book currently reaches on none of its accounts.
I'd rather discover a bar is unrealistic by missing it visibly than set one we clear by default —
but I'd expect to revise at least one of these eight within two quarters of running them, and the
retro is where that happens.

**Third, these are signals, not guarantees.** Every play here can be run well and still not reach
its signal, because the customer's side of it isn't ours to commit to. What I'd hold a CSM to is
running the play and reading the result honestly — not producing a customer behavior on demand.
