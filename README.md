# Airtable — Director, AI Transformation & Customer Success
### Take-home assessment · High Touch Customer Success

This repo contains my response to the take-home: a point of view on the High Touch book,
the transformation methodology I'd build around it, and the spec + seed data for the
Airtable operating system the team would run it in.

**Start here → [`docs/01-strategic-brief.md`](docs/01-strategic-brief.md)** (2 pages, ~6 min)

---

## The short version

Six accounts, **$5.06M ARR**. **61% of it ($3.11M) has a renewal conversation inside three
quarters**: Floor & Board, Voltaic, and Corvus. 

I score each account 1 to 5 on four dimensions: adoption depth, executive sponsorship, governance maturity, and **value evidence**, meaning a quantified business outcome stated in the language of the person who signs. None of that ARR scores above **2 of 5 on value evidence**, and **$2.59M of it sits at 1**, the bottom of the scale. Nobody can say what the customer got for the money. Book-wide, adoption averages 3.2, value evidence 1.3, governance 1.5. Nothing is blocked because "Airtable can't do this"; every blocker is organizational. 

**The platform works; the operating model around it doesn't** — the mandate is that shift, from relationship-led to a transformation-led.

---

## What's in here

| # | Deliverable | File | What it is |
|---|---|---|---|
| 1 | **Strategic brief** | [`docs/01-strategic-brief.md`](docs/01-strategic-brief.md) | Top 3 priorities for the first 90 days and the reasoning. The primary deliverable. |
| — | Book diagnosis | [`docs/02-book-diagnosis.md`](docs/02-book-diagnosis.md) | The scored analysis behind the brief — all six accounts, dimension by dimension, with the play each one gets. |
| — | Methodology | [`docs/03-transformation-methodology.md`](docs/03-transformation-methodology.md) | The repeatable motion: maturity ladder, constraint rule, the governance through-line, and the 8-play library. |
| — | Operating model | [`docs/04-operating-model.md`](docs/04-operating-model.md) | How this runs across 15 CSMs — ownership boundaries, the skills matrix + pairing, rhythm, metrics, inspection, and how I'd develop the team. |
| — | Play library | [`docs/05-play-library.md`](docs/05-play-library.md) | The eight plays in full — each split into **the standard** (global consistency) and **the latitude** (local customization), plus what's deliberately *not* a play. |
| 2 | **Airtable build** | [`airtable-build/`](airtable-build/) | Schema, AI component specs, interface specs, build checklist, and seed data for all six accounts. |
| — | Seed data | [`airtable-build/data/`](airtable-build/data/) | Import-ready CSVs — the six accounts pre-scored, 8 plays, stakeholders, signals, value narratives, CSM skills matrix. |
| — | Build guides | [`airtable-build/build-checklist.md`](airtable-build/build-checklist.md) · [`omni-build-brief.md`](airtable-build/omni-build-brief.md) | Two ways to build it: human-in-UI steps, or copy-paste prompts for Airtable Omni. |
| — | Build script | [`scripts/`](scripts/) | Optional: creates the base and loads the data via the Airtable API. |
| 3 | **Live session** | [`session/`](session/) | 60-minute run of show and prepared answers to the pushback I expect. |
| — | Appendix | [`appendix/`](appendix/) | Assumptions, how I used AI, and the [reconciliation](appendix/reconciliation.md) of two independent strategy drafts. |
| — | Changelog | [`CHANGELOG.md`](CHANGELOG.md) | How this evolved, revision by revision — what I kept, changed, and verified. |
| — | Working conventions | [`AGENTS.md`](AGENTS.md) | The rules this repo is edited under — what may be named, what must be verified, why changes go through PRs. |

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

## Assumptions, and what I invented

I've listed everything I assumed about Airtable's business and the HTCS function in
[`appendix/assumptions.md`](appendix/assumptions.md), flagged by how much the argument
depends on each one. Several are probably wrong; the brief notes which ones would change my
priorities if they are.

**One discipline worth calling out, because it changed the deliverable.** Late in the build I
audited every organizational name in this repo against the source material. The assessment names
no Airtable-side partner function; the role names exactly five — *Renewals, Support, Professional
Services, Product, Sales.* Several others I'd been using were invented and then applied so
consistently that nothing ever contradicted them. They're now described by **capability** —
*whoever can stand behind a quantitative claim before it reaches a customer's CFO* — rather than by
a team name I'd be guessing at. Customer-side specifics all trace to the account snapshot. The
story is in [`appendix/how-i-used-ai.md`](appendix/how-i-used-ai.md) §6, and the working
conventions are in [`AGENTS.md`](AGENTS.md).
