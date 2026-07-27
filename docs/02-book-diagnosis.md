# Book Diagnosis — the working behind the brief

This is the analysis the [strategic brief](01-strategic-brief.md) compresses. It scores all six
accounts on the four dimensions of the readiness model, identifies each account's binding
constraint, and assigns the play that clears it.

---

## The four dimensions

Each scored 1–5 by the CSM, with written evidence required for any score of 4 or 5. The labels
track the vocabulary the function is measured on — adoption, sponsorship, governance, value.

| Dimension | The question it answers | 1 | 5 |
|---|---|---|---|
| **Adoption depth** | How deeply is AI actually in production — breadth across teams and depth of real use? | No AI adoption; unaware of the capability | AI in production across teams; customer builds independently |
| **Sponsorship & multi-threading** | Does a named executive own the AI outcome, and is it threaded beyond one person? | No exec owns it, or it sits with one person | Named exec sponsor, ≥3 threads, publicly committed to an outcome |
| **Governance maturity** | Is there a structure that decides what gets built, approves it, and scales it? | Nothing — or ungoverned shadow building | CoE + working review path + published standards |
| **Value evidence** | Is there a quantified outcome in the language of the person who signs? | Nothing stated | Customer-validated, dated, repeated back by the economic buyer |

**Why these four.** They're the four things that have to be true for AI transformation to
survive contact with a real organization, and each one fails independently — which is what makes
the model diagnostic rather than descriptive. An account can be a 5 on Adoption and a 1 on Value
evidence (Voltaic, Corvus) or a 5 on Sponsorship and stuck on Value evidence behind a governance
gate (Meridian). An average would hide all of it.

---

## The scores

| Account | ARR | Renewal | Adoption | Sponsor | Govern | Value ev. | Avg | Stage | Constraint |
|---|---|---|---|---|---|---|---|---|---|
| Floor & Board | $1.7M | ~2Q | 3 | 1 | 1 | 1 | 1.50 | 2 → regressing | **Sponsorship (+ CoE)** |
| Meridian Health | $1.1M | 4Q | 4 | 5 | 3 | 2 | 3.50 | 3 Governed | **Value evidence** |
| TrailLine | $540K | yr 1 | 1 | 3 | 1 | 1 | 1.50 | 1 Sponsored | **Adoption** |
| Corvus Financial | $890K | 3Q | 4 | 2 | 2 | 1 | 2.25 | 2 Contained | **Value evidence** |
| Harbor Lane | $310K | 5Q | 2 | 1 | 1 | 1 | 1.25 | 0 Unaware | **Value evidence** |
| Voltaic | $520K | 2Q | 5 | 2 | 1 | 2 | 2.50 | 2 *(presents as 4)* | **Governance** |
| **Average** | | | **3.2** | **2.3** | **1.5** | **1.3** | | | |

**Commercial exposure:** $5.06M book. $3.11M (61%) renews within 3 quarters. $4.21M (83%)
within 4. Every account renewing within 3 quarters scores 1 on Value evidence.

---

## Account by account

### Floor & Board Furniture — $1.7M · ~1500 seats · renewal conversation in ~2 quarters
**The largest account in the book and the one closest to a preventable loss.**

| | Score | Evidence |
|---|---|---|
| Adoption depth | **3** | Core calendar and base in strong daily use across all 4 teams. Consumer Insights designed and is piloting its own AI workflow — real latent depth, but only 1 of 4 teams has moved on AI. |
| Sponsorship | **1** | Champion (Sr. Director, Marketing Ops) left 3 months ago. Deputy keeps the base running but has no mandate for the AI roadmap. No replacement identified. |
| Governance | **1** | No governance body or CoE. "The vision lived in one person's head." |
| Value evidence | **1** | No value-realization conversation since kickoff. A large idea backlog with one item moved. |

**Read:** This account is not failing on product — daily use across four teams is genuine
health. It's failing because the transformation had exactly one owner and no institutional home.
The kickoff workshop generated a backlog, which felt like progress and was actually debt: a list
of ideas with no governing body to sequence them. Sales is flagging renewal risk correctly, but
the risk isn't usage — it's that in two quarters we walk into a renewal where nobody senior has a
reason to care.

**Constraint: Sponsorship** → **Play P2 · Re-Sponsor** (near-term) **+ a CoE** (structural).
This is the account that shows why re-sponsoring *alone* is a trap: install one new champion and
you've rebuilt the exact single-point-of-failure that just cost us three months. So the near-term
play stops the bleeding — find a new executive owner within 6 weeks and restart the value
conversation, using the Consumer Insights pilot as the proof asset — and the structural play makes
it durable: stand up a lightweight CoE so the vision survives the *next* departure. The one moved
idea is the only capital we have; spend it on recruiting a sponsor and seeding a governing body,
not on shipping idea #2.

**Not a methodology input:** the cross-team automation break escalation. That's Support's, and
the CSM shouldn't be spending renewal-cycle hours on it.

---

### Meridian Health Systems — $1.1M · ~900 seats · renewal in 4 quarters
**The most mature account in the book, and completely stuck — the account that proves the
constraint rule.**

| | Score | Evidence |
|---|---|---|
| Adoption depth | **4** | Mature deployment, established CoE, team ships independently. |
| Sponsorship | **5** | Strong exec sponsor who wants to move aggressively on AI agents. |
| Governance | **3** | Functioning CoE — but every proposed AI use case has sat in the customer's own security and data-governance review for over a quarter. The governance *structure* is mature; it's jammed. |
| Value evidence | **2** | Expansion appetite is real but blocked. No quantified risk-or-value case built for the audience that's actually blocking. |

**Read:** Meridian has the highest average in the book (3.50) and is producing nothing —
Sponsorship at 5 and Adoption at 4 are irrelevant while the review board is the gate. But note
*which* dimension is lowest: **Value evidence (2), not Governance.** Meridian is not
governance-*immature* — it has a CoE and a functioning review board, which is more governance
structure than anyone else in the book. What it lacks is the **evidence artifact that clears the
board**: a risk-and-controls case addressing data residency, model governance, and audit trail.
The review board is the customer we're not serving — nobody has treated it as a stakeholder with
its own success criteria and built for it.

**Constraint: Value evidence** → **Play P5 · Governance Case**. This is the nuance that makes the
model honest: value evidence isn't always a dollar figure. For a commercial buyer it's a
cost-or-cycle-time number (that's P4); for a governance board it's a risk-and-controls case (P5).
Same constraint, different audience, different artifact. Security & Risk and Product co-build the
case; the CSM owns the relationship with the review board and the sequencing. This is also the
first of the three **governance through-line** plays (see below).

**Separate item — the CSM, not the account.** "Drifted into order-taking, relaying questions
between the review board and Airtable." That's a role-definition failure and it's coachable:
relaying is what you do when you don't know you're allowed to lead. It goes in the base as a
coaching flag, not an account risk — a strong relationship CSM who needs permission and a partner,
not a performance conversation.

---

### TrailLine Logistics — $540K · ~400 seats · first year · **kickoff in 3 weeks**
**The only account where the clock is measured in weeks.**

| | Score | Evidence |
|---|---|---|
| Adoption depth | **1** | No AI adoption yet. Kickoff hasn't happened. |
| Sponsorship | **3** | COO is enthusiastic and bought the transformation vision — but it's single-threaded and top-only. |
| Governance | **1** | Nothing exists. |
| Value evidence | **1** | Nothing delivered. |

**Read:** The deal was sold *at* the COO and will be lived *by* an ops team that has been burned
twice by tools that "created work instead of removing it." That's not skepticism to overcome with
enthusiasm — it's a correct prediction based on evidence, and if the kickoff is a vision workshop
it becomes their third data point. The failure mode here is completely foreseeable and we have
three weeks.

**Constraint: Adoption** (tie at 1 with Governance and Value evidence, resolved by ladder order)
→ **Play P3 · Kickoff Re-Contract**. Restructure the kickoff around one workflow that visibly
removes work from the skeptical team, with success criteria written by *their* lead, not by us. Do
not present the COO's vision to that room in week one.

**Staffing (pairing, not reassignment):** the assigned HTCSM is one of the team's strongest
builders and newer to executive engagement — the right person here, because the hard part is the
ops floor, not the COO. Per the skills matrix, they own the ops-floor re-contract (their strength)
and are *paired* with an exec-engagement partner for the COO thread through the first two cycles,
rather than reassigned off an account that's mostly a builder's problem.

---

### Corvus Financial Group — $890K · ~600 seats · renewal in 3 quarters
**The cleanest test of the whole thesis.**

| | Score | Evidence |
|---|---|---|
| Adoption depth | **4** | Automations *plus field agents in production*. Genuinely strong — but contained to one BU. |
| Sponsorship | **2** | Strong champion inside one BU. Procurement and the CFO's office will decide the multi-year expansion — and neither is sponsored. |
| Governance | **2** | Adoption contained to one BU; no structure to spread it. |
| Value evidence | **1** | "No value narrative exists that translates the BU's results into business outcomes they care about." Expansion is significant but unsubstantiated. |

**Read:** Everything needed for a large expansion already exists except the sentence that makes it
purchasable. The customer has done the hard part. We have production AI adoption and an
enterprise-wide appetite, and it will die in procurement because the results live in a BU's
operational language and the decision gets made in the CFO's. **This is the account that proves
the problem is evidence, not adoption** — the highest adoption depth in the book that renews soon,
and the weakest value evidence.

**Constraint: Value evidence** → **Play P4 · Quantify & Translate**, then **P7 · Spread From the
Pocket**. Baseline vs. current on the BU's production workflows, converted into the CFO's metrics,
validated by the champion before it's ever shown to finance.

**Staffing:** the CSM has excellent relationships and instincts, lighter technical depth, and has
never quantified an AI adoption story. This is precisely the person the value-narrative generator
in the build is aimed at — the base drafts the numbers, Professional Services validates them, and
the CSM does the part they're genuinely best at: getting the CFO's office to believe it.

---

### Harbor Lane Retail — $310K · ~200 seats · renewal in 5 quarters
**The account that should get the least of my attention and the most of the template.**

| | Score | Evidence |
|---|---|---|
| Adoption depth | **2** | Healthy, stable usage of the core product inside its comfort zone. Zero AI adoption; largely unaware of the capability. |
| Sponsorship | **1** | No executive push for AI. |
| Governance | **1** | None. |
| Value evidence | **1** | Zero. Significant unrealized platform value, no expansion motion. |

**Read:** "Pleasant and shallow" is an accurate and dangerous description. Nothing is wrong, which
is why nothing will change without a deliberate intervention. The account text is explicit about
what it would take: a clear value demonstration tied to an existing use case.

**This is where the model needed a second rule.** The constraint logic wanted me to fix
Sponsorship first — recruit an executive. But you cannot sponsor an abstraction. At Stage 0,
nobody there has seen the thing they'd be sponsoring. So: **below Stage 1, Value evidence leads;
at Stage 1 and above, Sponsorship leads.** Prove one narrow thing, then you have something a
sponsor can attach to.

**Constraint: Value evidence** → **Play P1 · Prove One Thing**. One adjacent AI use case on a
merchandising workflow they already run. Small, fast, and measured.

**Prioritization call:** lowest ARR, furthest renewal, most standard play. This is the account I
hand to a mid-tenure CSM to run unsupervised from the playbook — and it's the best test of whether
the system actually works without me in the room.

---

### Voltaic Software — $520K · ~350 seats · renewal in **2 quarters**
**The trap.**

| | Score | Evidence |
|---|---|---|
| Adoption depth | **5** | The most AI-adopted customer in the book by a distance — RevOps builds and ships agents independently. |
| Sponsorship | **2** | No exec sponsor in evidence. Internal builders dominate. QBR attendance declining two quarters running — sponsor disengagement, not calendar friction. |
| Governance | **1** | Building own agents and AI workflows, "some of them poorly governed," self-serving expansion. |
| Value evidence | **2** | Seats growing — but without CS influence, so we can't attribute or defend any of it. |

**Read:** Voltaic presents as the most advanced account in the book. It isn't. It's a Stage 2
account moving at Stage 4 speed with no governance and no CS seat, renewing in two quarters into a
pricing negotiation we won't be in the room for. **Seat growth without CS influence isn't health —
it's a customer that has priced us as a tool.** When the renewal comes, the builders will argue we
added nothing beyond check-ins, and on the current evidence they'll be right.

The opening is in their own weakness: they said the governance quiet part out loud. A technically
confident team shipping ungoverned agents has a problem it cannot solve by building harder — agent
sprawl, cost drift, no standards, no audit path. That is the one thing CS can offer that they
can't self-serve.

**Constraint: Governance** → **Play P6 · Governance Partner Insert**. Agent inventory, a
governance standard, a sprawl-and-cost view. Stop selling them roadmap previews they don't want;
sell them the thing they can't build. Second of the three governance through-line plays.

---

## The governance through-line

Read as separate account tactics, governance work looks like three problems. It's one motion, and
it's a **required play, not an aspiration** — which is why the play library treats it as a named
motion rather than a footnote:

| Account | Governance artifact | What it unlocks |
|---|---|---|
| **Meridian** | A risk-and-controls case for the review board | Clears the gate that's been stuck a quarter; releases the blocked expansion |
| **Voltaic** | An agent inventory + a governance standard | The wedge back to relevance before the pricing negotiation |
| **Floor & Board** | A lightweight CoE | Makes the transformation survive the next champion's departure |

Three different artifacts, one insight: **the durable fix for person-dependence is a structure,
not a better person.** That's the throughline the Director owns across the book.

---

## What the pattern actually says

Read the columns, not the rows.

- **Adoption 3.2** — the platform works. Three of six are in real production; one is world-class.
- **Value evidence 1.3** — no account in the book can prove its value. Not one.
- **Governance 1.5** — five of six have no functioning structure for deciding what gets built.
- **Sponsorship 2.3** — carried almost entirely by Meridian's 5.

If the diagnosis were "drive more usage," Corvus and Voltaic would be the healthy accounts.
They're two of the three most at-risk dollars in the book. **Adoption is not the leading
indicator. Governance and value evidence are.**

That's the whole argument: build the function around producing governance and value evidence
repeatably, and the adoption metric takes care of itself — because in this book it already has.
