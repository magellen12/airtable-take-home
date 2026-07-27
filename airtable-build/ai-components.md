# AI components

Three AI fields, one agent, three automations. Prompts are copy-pasteable — `{Field Name}`
tokens are Airtable field references inserted with the `+` picker in the prompt editor.

**Design principle running through all of them:** *AI drafts, humans own.* Every AI output
lands in a field that a person has to accept, edit or override, and every override is captured.
Nothing AI-generated reaches a customer without passing a status gate.

| | Component | Where | Job |
|---|---|---|---|
| AI-1 | Stage classifier + rationale | `Diagnostics` | Turns four scores + evidence into a stage and a defensible rationale |
| AI-2 | Play recommender | `Diagnostics` | Turns the constraint into the next play and its first three moves |
| AI-3 | **Value narrative generator** | `Value Stories` | Turns evidence into a paragraph in the economic buyer's language — *the one to build first* |
| AG-1 | Discovery agent | Base agent | Turns raw session notes into draft scores with evidence |
| A1–A3 | Automations | — | Currency, staleness, evidence enforcement |

---

## AI-1 · Stage classifier {#ai-1}
**Field type:** AI field on `Diagnostics` · **Output:** two fields (`Stage`, `Stage Rationale`)

```
You are a customer transformation analyst for Airtable's High Touch Customer Success team.

Classify this account's AI transformation stage using ONLY the scores and evidence below.

Account: {Account}
Sponsorship: {Sponsorship}/5 — {Sponsorship Evidence}
Governance: {Governance}/5 — {Governance Evidence}
Adoption: {Adoption}/5 — {Adoption Evidence}
Value evidence: {Value Evidence}/5 — {Value Evidence Notes}

STAGE DEFINITIONS
0 Unaware — core product healthy, AI not on the agenda, nobody has asked.
1 Sponsored — an executive has bought a vision, nothing delivered yet.
2 Contained — real AI value exists in one pocket and does not spread.
3 Governed — sponsor + CoE + a working review path exist; scale is a governance question.
4 Compounding — customer builds AND governs independently; expansion is customer-initiated
  and attributable to us.

CRITICAL RULE
Stage 4 requires Governance >= 4. A customer building fast without governance is Stage 2
regardless of how sophisticated they look. High adoption with low governance is a risk
signal, not a maturity signal — say so explicitly in the rationale when you see it.

Return exactly:
STAGE: <0-4> <name>
RATIONALE: <two sentences. Name the single dimension holding this stage back. If the account
presents as more mature than it is, say so directly.>
```

**Why the critical rule is in the prompt.** Without it the model scores Voltaic a 4 — it reads
"building its own agents and AI workflows" as maturity. That's the exact mistake a human makes
too, and it's the one that loses the account. Encoding it means every CSM gets the correction
whether or not they'd have caught it themselves.

**Example output on seed data** *(drafted against this prompt outside the product — re-run and
verify in the AI field once it's live; see [`../appendix/how-i-used-ai.md`](../appendix/how-i-used-ai.md)):*
> `STAGE: 2 Contained` — *"Voltaic has the highest adoption depth in the book but is shipping
> agents its own team describes as poorly governed, with no executive sponsor and declining QBR
> attendance. It presents as Compounding; the absence of governance and of any CS-attributable
> outcome makes it Contained with elevated renewal risk."*

---

## AI-2 · Play recommender {#ai-2}
**Field type:** AI field on `Diagnostics` · **Output:** `Recommended Play`

```
You are recommending the next transformation play for an Airtable High Touch account.
The CSM running this may be new to AI transformation work — be concrete and directive.

Account: {Account} — {ARR} ARR, {Quarters to Renewal} quarters to renewal
Stage: {Stage}
Binding constraint: {Constraint}
Scores — Sponsorship {Sponsorship}, Governance {Governance}, Adoption {Adoption}, Value evidence {Value Evidence}
Context: {Session Notes}

THE PLAY LIBRARY
P1 Prove One Thing — clears Value evidence, stage 0. Partner: Professional Services.
P2 Re-Sponsor — clears Sponsorship, stage 1-2. Partner: Sales.
P3 Kickoff Re-Contract — clears Adoption, stage 1. Partner: Professional Services.
P4 Quantify & Translate — clears Value evidence for a COMMERCIAL audience (CFO/COO), stage 2-3. Partner: Value Validation.
P5 Governance Case — clears Value evidence for a GOVERNANCE audience (a review board), stage 3. Partner: Security & Risk + Product.
P6 Governance Partner Insert — clears Governance, stage 2 fast-moving. Partner: Professional Services + Security & Risk.
P7 Spread From the Pocket — clears Adoption / seeds a CoE, stage 2. Partner: Professional Services.
P8 Renewal Value Review — clears Value evidence, any stage at T-2 quarters. Partner: Renewals.

RULES
1. Recommend the play that clears the BINDING CONSTRAINT, not the account's weakest-sounding
   narrative detail.
2. Stage 0 exception: below Stage 1, Value evidence leads even if Sponsorship scores lower. You
   cannot recruit a sponsor for something nobody has seen.
3. Value-evidence audience rule: if the constraint is Value evidence and a governance/review
   board is the blocker (stage 3), recommend P5 (a risk-and-controls case), not P4. Otherwise
   Value evidence → P4 (a commercial number).
4. If renewal is within 2 quarters and Value evidence <= 2, sequence P8 alongside the primary play.
5. Never recommend a play whose partner requirement the CSM would have to fulfil alone.

Return exactly:
PLAY: <code and name>
WHY: <one sentence tying it to the binding constraint>
FIRST THREE MOVES: <three numbered actions the CSM takes this week — specific enough to do
Monday morning, each naming who is involved>
PARTNER TO PULL IN: <role, and what you are asking them for>
```

**Rule 5 is the leverage test in a single line.** It stops the system recommending a CFO-level
AI risk conversation to a CSM with no partner attached — which is how a relationship-led CSM ends
up failing alone at something they were never equipped for. **Rule 3 is what routes Meridian to
P5 and Corvus to P4** even though both have Value evidence as the binding constraint — same
constraint, different audience, different artifact.

**Example output on Corvus** *(drafted against this prompt outside the product — verify in-field):*
> `PLAY: P4 · Quantify & Translate`
> `WHY:` Value evidence is the binding constraint at 1 — production AI adoption exists in the
> Enterprise Ops BU but no artifact translates it into terms the CFO's office can buy from.
> `FIRST THREE MOVES:` 1. 45-min working session with the BU champion to baseline the field
> agent triage workflow (pre/post volume, handling time, headcount). 2. Pull the value-validation partner in to
> validate the cost conversion before anything is written down. 3. Draft the narrative and
> get the champion to confirm the numbers *before* procurement ever sees them.
> `PARTNER TO PULL IN:` Value Validation — to validate the cost model. Sales/Renewals — to map the
> procurement path.

---

## AI-3 · Value narrative generator {#ai-3}
**Field type:** AI field on `Value Stories` · **Output:** `Narrative`
**⭐ Build this one first — it's the demo.**

```
You are drafting a value realization narrative for an Airtable enterprise customer.
This will be read by a senior executive who did not implement the product and does not care
about product features.

Account: {Account} — {Function}
Use case: {Use Case}
Business metric: {Business Metric}
Baseline: {Baseline}
Current: {Current}
Quantified impact: {Quantified Impact}
Evidence source: {Source of Truth}
Audience: {Audience}

RULES
1. Write for {Audience}. A CFO cares about cost, margin and risk. A COO cares about throughput,
   cycle time and capacity. Do not send a COO a cost paragraph.
2. Lead with the business outcome. Airtable is named once, as the mechanism, never as the subject.
3. Use only the numbers given. Do NOT estimate, extrapolate, annualize or invent a figure. If
   the evidence is too thin to support a claim, write exactly: "INSUFFICIENT EVIDENCE — need:"
   followed by what is missing.
4. No adjectives that cannot be evidenced. Never "transformative", "game-changing", "dramatic".
5. Maximum 120 words. It has to survive being read aloud in a renewal meeting.

Return:
NARRATIVE: <the paragraph>
CONFIDENCE: <High / Medium / Low> — <what would raise it>
```

**Rule 3 is the most important line in this repo.** The failure mode of an AI value-story
generator is a plausible, well-written, invented number walking into a CFO conversation. The
`INSUFFICIENT EVIDENCE` escape hatch means the field refuses rather than confabulates — and on
seed data it *does* refuse, on Floor & Board, because there genuinely is no evidence there yet.
That refusal is the most useful thing it outputs all demo.

**Example output — Corvus, audience CFO** *(drafted against this prompt outside the product):*
> `NARRATIVE:` The Enterprise Operations team reduced field-agent case triage from 14 minutes
> to 3 minutes per case across roughly 2,100 cases a month — recovering about 385 hours of
> analyst capacity monthly, which the BU has redeployed to exception handling rather than
> backfilling two open roles. The work is running in production today on automations and AI
> agents built by the team itself. Extending the same pattern to the remaining four business
> units is the subject of the multi-year proposal.
> `CONFIDENCE: Medium` — case volumes are BU-reported and not yet reconciled against the
> platform's own run logs; validate before this reaches procurement.

**Example output — Floor & Board, audience CIO** *(drafted against this prompt outside the product):*
> `INSUFFICIENT EVIDENCE — need: a baseline for the Consumer Insights pilot workflow, a current
> measurement, and one business metric the customer already tracks. Daily active usage across
> four teams is an adoption signal, not a business outcome.`

That is the correct answer and the system is right to say it.

---

## AG-1 · Discovery agent
**Type:** base agent · **Input:** `Diagnostics.Session Notes` · **Output:** draft scores + evidence

The answer to *"how does a CSM who's never run this get a first draft?"* The CSM pastes raw
notes from a customer conversation; the agent proposes scores with the quote that justifies
each one.

```
You are a transformation diagnostic assistant for Airtable High Touch CS.

The CSM has pasted raw notes from a customer conversation. Produce a DRAFT diagnostic the CSM
will review, correct and own. You are not the decision-maker.

NOTES:
{Session Notes}

For each of Sponsorship, Governance, Adoption and Value evidence, return:
- a score 1-5
- the specific quote or observation from the notes that justifies it
- CONFIDENCE: High / Medium / Low
- if the notes do not support a score, return "NOT EVIDENCED" and the exact question the CSM
  should ask next — do not guess

Then return:
GAPS: the three highest-value questions the CSM did not ask in this conversation.

Scoring anchors:
Sponsorship 1 = nobody owns it or it lives with one person; 5 = named exec, 3+ threads, public
  commitment to an outcome.
Governance 1 = nothing or ungoverned shadow building; 5 = CoE + working review path + published
  standards.
Adoption 1 = no AI adoption, unaware; 5 = AI in production across teams, self-sufficient builders.
Value evidence 1 = nothing stated; 5 = customer-validated, dated, repeated back by the economic buyer.

Bias toward the LOWER score when evidence is ambiguous. An inflated diagnostic produces a
confident wrong play, which is worse than an honest gap.
```

**The `GAPS` output is the coaching mechanism.** It tells a CSM what a stronger CSM would have
asked in that meeting — every time they run it, on their own accounts, without me in the room.
That's the piece that scales me across fifteen people.

---

## Automations

### A1 · Keep the current diagnostic current
**Trigger:** record created in `Diagnostics`
**Actions:** set `Accounts.Current Diagnostic` → this record; mark prior diagnostics for that
account `Superseded`.

### A2 · Renewal value alert — *the commercial one*
**Trigger:** daily, at 07:00
**Condition:** `Quarters to Renewal <= 2` **AND** (`Latest Value Story Status` is not
`Customer-validated` **OR** `Freshness` = `Stale`)
**Actions:** create an `Account Plays` record for **P8 · Renewal Value Review** if none open;
Slack the owning CSM; flag the account on the Director Book Review.

> On seed data this fires on **Floor & Board** and **Voltaic** the morning the base is stood
> up. Both renew inside two quarters with no current value narrative. That's the automation
> earning its place in the first five minutes.

### A3 · Evidence enforcement
**Trigger:** record updated in `Diagnostics`, any score field
**Condition:** a score is `>= 4` and its matching evidence field is empty
**Action:** set `Diagnostic Status` → `Evidence required`; notify the CSM.

> Not bureaucracy. This is the specific control that stops a relationship-led CSM from scoring
> their friendliest account a 5 on Sponsorship — the failure mode that let Floor & Board's
> champion departure go unnoticed for three months.

---

## Where AI is *not* used, on purpose

| Not AI | Why |
|---|---|
| The constraint calculation | A deterministic formula. If a CSM can't reproduce why an account got its play, they won't defend it in front of a customer. |
| Value story `Status` | Only a human can confirm a customer said the number back. |
| Single composite health score | The four dimensions *are* the health read, kept multidimensional on purpose. Rolling them into one number is exactly what would have shown Voltaic green. |
| Customer-facing sends | Everything AI-drafted stops at a human. No automation emails a customer. |
