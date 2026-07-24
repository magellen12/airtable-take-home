# Airtable — Director, AI Transformation & Customer Success
### Take-home assessment · High Touch Customer Success

This repo contains my response to the take-home: a point of view on the High Touch book,
the transformation methodology I'd build around it, and the spec + seed data for the
Airtable operating system the team would run it in.

**Start here → [`docs/01-strategic-brief.md`](docs/01-strategic-brief.md)** (2 pages, ~6 min)

---

## The short version

Six accounts, **$5.06M ARR**. **61% of it ($3.11M) has a renewal conversation inside three
quarters** — and all three of those accounts score **1 out of 5 on Value evidence**: nobody can
state, in the buyer's language, what the customer actually got.

I scored the whole book on four dimensions — **Adoption depth, Sponsorship & multi-threading,
Governance maturity, Value evidence.** Adoption averages **3.2/5**. Value evidence averages
**1.3** and Governance **1.5**. In no account is the blocker "Airtable can't do this."

**The platform is working. The operating model around it isn't** — the job is moving from a
relationship-led motion to a transformation-led one. That premise drives everything else here.

---

## What's in here

| # | Deliverable | File | What it is |
|---|---|---|---|
| 1 | **Strategic brief** | [`docs/01-strategic-brief.md`](docs/01-strategic-brief.md) | Top 3 priorities for the first 90 days and the reasoning. The primary deliverable. |
| — | Book diagnosis | [`docs/02-book-diagnosis.md`](docs/02-book-diagnosis.md) | The scored analysis behind the brief — all six accounts, dimension by dimension, with the play each one gets. |
| — | Methodology | [`docs/03-transformation-methodology.md`](docs/03-transformation-methodology.md) | The repeatable motion: maturity ladder, constraint rule, the governance through-line, and the 8-play library. |
| — | Operating model | [`docs/04-operating-model.md`](docs/04-operating-model.md) | How this runs across 15 CSMs — ownership boundaries, the skills matrix + pairing, rhythm, metrics, inspection, and how I'd develop the team. |
| 2 | **Airtable build** | [`airtable-build/`](airtable-build/) | Schema, AI component specs, interface specs, build checklist, and seed data for all six accounts. |
| — | Seed data | [`airtable-build/data/`](airtable-build/data/) | Import-ready CSVs — the six accounts pre-scored, 8 plays, stakeholders, signals, value narratives, CSM skills matrix. |
| — | Build guides | [`airtable-build/build-checklist.md`](airtable-build/build-checklist.md) · [`omni-build-brief.md`](airtable-build/omni-build-brief.md) | Two ways to build it: human-in-UI steps, or copy-paste prompts for Airtable Omni. |
| — | Build script | [`scripts/`](scripts/) | Optional: creates the base and loads the data via the Airtable API. |
| 3 | **Live session** | [`session/`](session/) | 60-minute run of show and prepared answers to the pushback I expect. |
| — | Appendix | [`appendix/`](appendix/) | Assumptions I'm making, and how I used AI to build this. |

---

## The Airtable build in one paragraph

**HTCS Transformation OS** — a portfolio operating base covering priorities 1 and 2 from the
brief. A CSM runs a four-dimension diagnostic with the customer; the base identifies the
account's **binding constraint** and recommends the play that clears it; adoption and
commercial signals feed an AI-drafted **value narrative** in the buyer's own language, which is
what the CSM carries into renewal. Two interfaces: a **CSM Cockpit** (my book, my constraint,
my next move) and a **Director Book Review** (the inspection surface — and the skills matrix — a
team that just lost its manager layer doesn't have).

The leverage test: the weakest CSM on the team gets the same quality of diagnosis, the same
play, and a first draft of the executive narrative. The strongest gets time back and authors
new plays. I get one place to inspect instead of fifteen opinions.

Build details → [`airtable-build/README.md`](airtable-build/README.md)

---

## Assumptions

I've listed everything I assumed about Airtable's business and the HTCS function in
[`appendix/assumptions.md`](appendix/assumptions.md), flagged by how much the argument
depends on each one. Several are probably wrong; the brief notes which ones would change my
priorities if they are.
