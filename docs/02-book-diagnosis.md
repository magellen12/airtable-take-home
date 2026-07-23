# Book Diagnosis — the working behind the brief

This is the analysis the [strategic brief](01-strategic-brief.md) compresses. It scores all six
accounts on the four dimensions of the maturity model, identifies each account's binding
constraint, and assigns the play that clears it.

---

## The four dimensions

Each scored 1–5 by the CSM, with written evidence required for any score of 4 or 5.

| Dimension | The question it answers | 1 | 5 |
|---|---|---|---|
| **Sponsorship** | Does a named executive own the AI outcome, and is it multi-threaded? | No exec owns it, or it sits with one person | Named exec sponsor, ≥3 threads, publicly committed to an outcome |
| **Governance** | Is there a structure that decides what gets built, approves it, and scales it? | Nothing — or ungoverned shadow building | CoE + working review path + published standards |
| **Capability** | Can the customer's own people design and run AI workflows? | Nobody can build; unaware of capability | Self-sufficient builders shipping production agents |
| **Proof** | Is there a quantified outcome in the language of the person who signs? | Nothing stated | Customer-validated, dated, repeated back by the economic buyer |

**Why these four.** They're the four things that have to be true for AI transformation to
survive contact with a real organization, and each one fails independently — which is what
makes the model diagnostic rather than descriptive. An account can be a 5 on Capability and a
1 on Proof (Voltaic) or a 5 on Sponsorship and stuck at Governance (Meridian). An average
would hide both.

---

## The scores

| Account | ARR | Renewal | Sponsor | Govern | Cap. | Proof | Avg | Stage | Constraint |
|---|---|---|---|---|---|---|---|---|---|
| Floor & Board | $1.7M | ~2Q | 1 | 1 | 3 | 1 | 1.50 | 2 → regressing | **Sponsorship** |
| Meridian Health | $1.1M | 4Q | 5 | 3 | 4 | 2 | 3.50 | 3 Governed | **Governance** |
| TrailLine | $540K | yr 1 | 3 | 1 | 1 | 1 | 1.50 | 1 Sponsored | **Capability** |
| Corvus Financial | $890K | 3Q | 2 | 2 | 4 | 1 | 2.25 | 2 Contained | **Proof** |
| Harbor Lane | $310K | 5Q | 1 | 1 | 2 | 1 | 1.25 | 0 Unaware | **Proof** |
| Voltaic | $520K | 2Q | 2 | 1 | 5 | 2 | 2.50 | 2 *(presents as 4)* | **Governance** |
| **Average** | | | **2.3** | **1.5** | **3.2** | **1.3** | | | |

**Commercial exposure:** $5.06M book. $3.11M (61%) renews within 3 quarters. $4.21M (83%)
within 4. Every account renewing within 3 quarters scores 1 on Proof.

---

## Account by account

### Floor & Board Furniture — $1.7M · ~1500 seats · renewal conversation in ~2 quarters
**The largest account in the book and the one closest to a preventable loss.**

| | Score | Evidence |
|---|---|---|
| Sponsorship | **1** | Champion (Sr. Director, Marketing Ops) left 3 months ago. Deputy keeps the base running but has no mandate for the AI roadmap. No replacement identified. |
| Governance | **1** | No governance body or CoE. "The vision lived in one person's head." |
| Capability | **3** | Core calendar and base in strong daily use across all 4 teams. Consumer Insights designed and is piloting its own workflow — real latent build capability. |
| Proof | **1** | No value-realization conversation since kickoff. A large idea backlog with one item moved. |

**Read:** This account is not failing on product — daily use across four teams is genuine
health. It's failing because the transformation had exactly one owner and no institutional
home. The kickoff workshop generated a backlog, which felt like progress and was actually
debt: a list of ideas with no governing body to sequence them. Sales is flagging renewal risk
correctly, but the risk isn't usage, it's that in two quarters we will walk into a renewal
where nobody senior has a reason to care.

**Constraint: Sponsorship** → **Play P2 · Re-Sponsor**, then **P4 · Quantify & Translate**.
Find and install a new executive owner within 6 weeks, using the Consumer Insights pilot as
the proof asset that makes sponsorship attractive rather than abstract. The one moved idea is
the only capital we have — spend it on recruiting a sponsor, not on shipping idea #2.

**Not a methodology input:** the cross-team automation break escalation. That's Support's,
and the CSM shouldn't be spending renewal-cycle hours on it.

---

### Meridian Health Systems — $1.1M · ~900 seats · renewal in 4 quarters
**The most mature account in the book, and completely stuck.**

| | Score | Evidence |
|---|---|---|
| Sponsorship | **5** | Strong exec sponsor who wants to move aggressively on AI agents. |
| Governance | **3** | Functioning CoE — but every proposed AI use case has sat in the customer's own security and data-governance review for over a quarter, and nobody has built the case that would clear it. |
| Capability | **4** | Mature deployment, established CoE. |
| Proof | **2** | Expansion appetite is real but blocked; no quantified outcome built for the audience that's actually blocking. |

**Read:** This is the account that proves the constraint rule matters. Meridian has the
highest average score in the book (3.50) and is producing nothing. Sponsorship at 5 and
Capability at 4 are irrelevant while a review board is the gate. **The review board is the
customer we're not serving.** Nobody has treated it as a stakeholder with its own success
criteria — risk posture, data residency, model governance, audit trail — and built for it.

**Constraint: Governance** → **Play P5 · Governance Unblock**. Trust/Security and Product
lead the artifact; the CSM owns the relationship with the review board and the sequencing.

**Separate item — the CSM, not the account.** "Drifted into order-taking, relaying questions
between the review board and Airtable." That's a role-definition failure and it's coachable:
relaying is what you do when you don't know you're allowed to lead. It goes in the base as a
coaching flag, not as an account risk. This is a strong relationship CSM who needs permission
and a partner, not a performance conversation.

---

### TrailLine Logistics — $540K · ~400 seats · first year · **kickoff in 3 weeks**
**The only account where the clock is measured in weeks.**

| | Score | Evidence |
|---|---|---|
| Sponsorship | **3** | COO is enthusiastic and bought the transformation vision — but it's single-threaded and top-only. |
| Governance | **1** | Nothing exists. Kickoff hasn't happened. |
| Capability | **1** | No AI adoption yet. |
| Proof | **1** | Nothing delivered. |

**Read:** The deal was sold *at* the COO and will be lived *by* an ops team that has been
burned twice by tools that "created work instead of removing it." That's not skepticism to
overcome with enthusiasm — it's a correct prediction based on evidence, and if the kickoff is
a vision workshop it will be their third data point. The failure mode here is completely
foreseeable and we have three weeks.

**Constraint: Capability** (tie at 1 with Governance and Proof, resolved by ladder order) →
**Play P3 · Kickoff Re-Contract**. Restructure the kickoff around one workflow that visibly
removes work from the skeptical team, with success criteria written by their lead, not by us.
Do not present the COO's vision to that room in week one.

**Staffing:** the assigned HTCSM is one of the team's strongest builders and newer to
executive engagement. That's the right person for this account — the hard part here is the
ops floor, not the COO. I take the COO thread with them for the first two cycles.

---

### Corvus Financial Group — $890K · ~600 seats · renewal in 3 quarters
**The cleanest test of the whole thesis.**

| | Score | Evidence |
|---|---|---|
| Sponsorship | **2** | Strong champion inside one BU. Procurement and the CFO's office will decide the multi-year expansion — and neither is sponsored. |
| Governance | **2** | Adoption contained to one BU; no structure to spread it. |
| Capability | **4** | Automations *plus field agents in production*. Genuinely strong. |
| Proof | **1** | "No value narrative exists that translates the BU's results into business outcomes they care about." Expansion is significant but unsubstantiated. |

**Read:** Everything needed for a large expansion already exists except the sentence that
makes it purchasable. The customer has done the hard part. We have production AI adoption and
an enterprise-wide appetite, and it will die in procurement because the results live in a BU's
operational language and the decision gets made in the CFO's. This is the account that proves
the problem is translation, not adoption.

**Constraint: Proof** → **Play P4 · Quantify & Translate**, then **P7 · Spread From the
Pocket**. Baseline vs. current on the BU's production workflows, converted into the CFO's
metrics, validated by the champion before it's ever shown to finance.

**Staffing:** the CSM has excellent relationships and instincts, lighter technical depth, and
has never quantified an AI adoption story. This is precisely the person the value-story
generator in the build is aimed at — the base drafts the numbers, Solutions validates them,
and the CSM does the part they're genuinely best at: getting the CFO's office to believe it.

---

### Harbor Lane Retail — $310K · ~200 seats · renewal in 5 quarters
**The account that should get the least of my attention and the most of the template.**

| | Score | Evidence |
|---|---|---|
| Sponsorship | **1** | No executive push for AI. |
| Governance | **1** | None. |
| Capability | **2** | Healthy, stable usage of the core product — inside its comfort zone. Largely unaware of AI capability. |
| Proof | **1** | Zero. Significant unrealized platform value, no expansion motion. |

**Read:** "Pleasant and shallow" is an accurate and dangerous description. Nothing is wrong,
which is why nothing will change without a deliberate intervention. The account text is
explicit about what it would take: a clear value demonstration tied to an existing use case.

**This is where the model needed a second rule.** The constraint logic wanted me to fix
Sponsorship first — recruit an executive. But you cannot sponsor an abstraction. At Stage 0,
nobody there has seen the thing they'd be sponsoring. So: **below Stage 1, Proof leads; at
Stage 1 and above, Sponsorship leads.** Prove one narrow thing, then you have something a
sponsor can attach to.

**Constraint: Proof** → **Play P1 · Prove One Thing**. One adjacent AI use case on a
merchandising workflow they already run. Small, fast, and measured.

**Prioritization call:** lowest ARR, furthest renewal, most standard play. This is the account
I hand to a mid-tenure CSM to run unsupervised from the playbook — and it's the best test of
whether the system actually works without me in the room.

---

### Voltaic Software — $520K · ~350 seats · renewal in **2 quarters**
**The trap.**

| | Score | Evidence |
|---|---|---|
| Sponsorship | **2** | No exec sponsor in evidence. Internal builders dominate. QBR attendance declining two quarters running — that's sponsor disengagement, not calendar friction. |
| Governance | **1** | Building own agents and AI workflows, "some of them poorly governed," self-serving expansion. |
| Capability | **5** | The most capable customer in the book by a distance. |
| Proof | **2** | Seats growing — but without CS influence, so we can't attribute or defend any of it. |

**Read:** Voltaic presents as the most advanced account in the book. It isn't. It's a Stage 2
account moving at Stage 4 speed with no governance and no CS seat, renewing in two quarters
into a pricing negotiation we won't be in the room for. **Seat growth without CS influence
isn't health — it's a customer that has priced us as a tool.** When the renewal comes, the
builders will argue we added nothing beyond check-ins, and on the current evidence they'll be
right.

The opening is in their own weakness: they said the governance quiet part out loud. A
technically confident team that is shipping ungoverned agents has a problem it cannot solve by
building harder — agent sprawl, cost drift, no standards, no audit path. That is the one thing
CS can offer that they can't self-serve.

**Constraint: Governance** → **Play P6 · Governance Partner Insert**. Agent inventory, a
governance standard, a sprawl-and-cost view. Stop selling them roadmap previews they don't
want; sell them the thing they can't build.

---

## What the pattern actually says

Read the columns, not the rows.

- **Capability 3.2** — the platform works. Three of six can build; one is world-class at it.
- **Proof 1.3** — no account in the book can prove its value. Not one.
- **Governance 1.5** — five of six have no functioning structure for deciding what gets built.
- **Sponsorship 2.3** — carried almost entirely by Meridian's 5.

If the diagnosis were "drive more usage," Corvus and Voltaic would be the healthy accounts.
They're two of the three most at-risk dollars in the book. **Usage is not the leading
indicator. Governance and proof are.**

That's the whole argument: build the function around producing governance and proof
repeatably, and the adoption metric takes care of itself — because in this book it already has.
