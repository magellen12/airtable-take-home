# Interface 2 · Director Book Review — build guide

Click-by-click for Airtable Interface Designer. Implements
[`interfaces.md` §2](interfaces.md). **No interface API** — all manual. Roughly 40–50 minutes.

**This is demo beat 1 — the opener.** It is the first thing on screen, so it carries more weight
than the Cockpit. Build it second, but rehearse it first.

Base **`appFGgbrUOs62IndE`** → https://airtable.com/appFGgbrUOs62IndE

---

## 0 · Prerequisites

Applied via API on 2026-07-28 and verified:

| Change | Why |
|---|---|
| `CSMs.Book ARR` rollup added | Row 3 column 1. `SUM(values)` over `Accounts → ARR`. Sums to **$5,060,000** ✓ |
| `CSMs.Paired With` — Marcus ↔ Ben **restored** | **Seed load bug.** The pairing is in `data/csms.csv` but never loaded. Row 3's whole argument depends on it |

**Not built, and the guide works around each — see §5:** `DoD Hit Rate`, `Plays in Flight`,
`Cycle Time` / `Over Cycle Time`.

---

## 1 · Create the interface

**Interfaces** → **Create interface** → **Blank** → layout **Dashboard** → name **Director Book
Review**. Dashboard, not Record review — this one is aggregate, with no per-record detail.

---

## 2 · Row 1 — four numbers

Four **Number** elements across the top.

| Tile | Value | Source |
|---|---|---|
| **ARR at Risk** | **$3,110,000** — 61% of book | `SUM(Accounts.ARR at Risk)` |
| **Value Coverage** | **0 / 6** — 0% | count `Latest Value Story Status` = `Customer-validated` |
| **Sponsor Coverage** | **2 / 6** — 33% | count `Exec Sponsor Named` = `Yes` |
| **% of Book Staged** | **6 / 6** — 100% | count accounts with a `Current Diagnostic` |

**Put Value Coverage in position two**, per `interfaces.md:68`. It's the leading indicator you'd be
judged on in six months and it starts at zero. That placement is an argument, not a layout choice.

### ⚠ Sponsor Coverage is 2 / 6 live, not 1 / 6

The docs say `1 / 6` in three places (`docs/01:86`, `docs/04:116`, `AGENTS.md:76`). The live base
returns **2 of 6** — TrailLine and Meridian both have an active `Exec Sponsor`, and both clear the
`docs/04:116` bar of *"named exec sponsor and ≥3 mapped threads"*:

| Account | Sponsor roles (active only) | Exec sponsor? |
|---|---|---|
| TrailLine | Exec Sponsor, User Lead, User Lead | **Yes** |
| Meridian | Exec Sponsor, Champion, Builder | **Yes** |
| Harbor Lane | Champion, User Lead | No |
| Corvus | Champion, Builder | No |
| Floor & Board | Champion, Builder | No |
| Voltaic | Builder | No |

**Show 2 / 6.** Do not reverse-engineer a definition that returns 1 to match the deck — the
`Exec Sponsor Named` formula already excludes departed and unengaged sponsors, which is the honest
read. This number is not in the pre-flight four; don't build a beat on it. If asked, the true answer
is the good one: *"the deck says one, the base says two — the base is right, and I'd rather show you
the system correcting my slide than the other way round."*

### `Stage Progression QoQ` — omit the tile

There is one diagnostic round, so there is no prior quarter to compare. A tile reading `baseline` is
a tile with no information. Say it instead: *"stage progression is the metric I'd run this on in
ninety days; today it's a baseline."*

---

## 3 · Row 2 — the book on one screen

### Stage distribution (bar)
Source `Accounts`, group by `Stage`, count.

| Stage | Count | Accounts |
|---|---|---|
| 0 Unaware | 1 | Harbor Lane |
| 1 Sponsored | 1 | TrailLine |
| 2 Contained | **3** | Floor & Board, Corvus, Voltaic |
| 3 Governed | 1 | Meridian |
| 4 Compounding | **0** | — |

The line: ***no account in this book is compounding.*** The empty Stage 4 bar is the point — make
sure the chart renders the empty category rather than dropping it.

### Book ARR by constraint (bar) — **the resourcing argument**
Source `Accounts`, group by `Constraint`, sum `ARR`. Sort descending.

| Constraint | Book ARR | Accounts |
|---|---|---|
| **Value evidence** | **$2,300,000** — **45%** | Corvus $890K · Meridian $1.1M · Harbor Lane $310K |
| Sponsorship | $1,700,000 | Floor & Board |
| Adoption | $540,000 | TrailLine |
| Governance | $520,000 | Voltaic |
| | **$5,060,000** | |

This is the chart you open the working session on. $2.3M of the book — 45% — is blocked on value
evidence, which is the entire case for priority 2 and for *Value Validation* + *Security & Risk*
capacity ahead of more headcount.

Note Harbor Lane lands in Value evidence because of its `Constraint Override`, not its raw scores.
If asked, the reason is in `Diagnostics.Constraint Override Reason` — open it. That's a feature.

### Renewal timeline
Timeline by `Quarters to Renewal`, coloured by `Renewal Readiness`.

Q2 Floor & Board + Voltaic · Q3 Corvus · Q4 **Meridian** · Q5 Harbor Lane · Q7 TrailLine

**Meridian is the beat here.** It shows ⚠️ No current value but contributes **$0** to ARR at Risk —
it renews in 4 quarters and the at-risk gate cuts at 3. It sits one quarter outside the window. If
the value position doesn't change, the arithmetic moves it in: **$3,110,000 → $4,210,000, 61% →
83%**. That is the leading-indicator argument made concrete on your second-largest account.

---

## 4 · Row 3 — the skills matrix

Grid on `CSMs`, sorted `Book ARR` descending. Verified live:

| CSM | Book ARR | Builder | Exec | Domain | Paired with | Authored |
|---|---|---|---|---|---|---|
| Dana Whitfield | $2,590,000 | 2 | 4 | 3 | — | 0 |
| Priya Raghavan | $1,100,000 | 3 | 4 | 4 | — | 0 |
| **Marcus Oyelaran** | $1,060,000 | **5** | **2** | 3 | **Ben Achterberg** | 0 |
| Sofia Restrepo | $310,000 | 2 | 3 | 3 | — | 0 |
| **Ben Achterberg** | $0 | 2 | **5** | 3 | **Marcus Oyelaran** | 0 |
| Yuki Tanabe | $0 | 4 | 2 | 2 | — | 0 |

Columns: `Name`, `Book ARR`, `Builder Depth`, `Executive Presence`, `Domain`, `Paired With`,
`Plays Authored`, `Development Focus`.

**Marcus (builder 5 / exec 2) paired with Ben (exec 5) is the row that carries the argument** —
pairing is an inspectable decision rather than a favour you remember to do. This only renders
because the seed bug is fixed; check it on screen before the session.

**Ben and Yuki showing $0 book is correct, not missing data.** Ben is the exec-presence pair on
TrailLine (Marcus owns the account); Yuki is the new ramp — *"the clearest test of whether the
diagnostic works without tenure behind it."* Both are deliberate.

### `Plays Authored` is 0 across the board — leave it

`interfaces.md:90` calls this *"the column I watch for the manager-layer decision."* It reads 0 for
everyone, and `data/csms.csv` seeds it as 0 for everyone — that is the **baseline**, not a gap.
Don't populate it. It's the same shape as Value Coverage 0/6: the metric that matters starts at
zero, which is exactly why it's worth watching. The line: *"nobody has authored a play yet. In six
months this column is how I decide who leads."*

---

## 5 · Row 4 — the inspection queue

**All four queues are empty.** Verified:

| Queue | State | Why |
|---|---|---|
| Plays over cycle time | empty | 9 plays: 5 In flight, 4 Not started, **0 completed**; all target dates future |
| Diagnostics older than 90 days | empty | all six dated 2026-07-20 — age 8 days |
| Play overrides awaiting review | empty | `Play Accepted` unset on all six |
| Score ≥4 with no evidence (A3) | empty | **every** score ≥4 has an evidence note — checked all four dimensions |

**Do not build four empty grids in the opener.** Replace with a single **Text** element:

> **Inspection queue — clear.** No play past cycle time, no diagnostic older than 90 days, no
> override awaiting review, no unevidenced score above 4.

That is a stronger screen than four empty boxes, and it's true. The line: *"this is week one, so
everything is clear. These four queues are what I inspect in a quarter — and the fourth one is the
model-quality feed: every time a CSM overrides the recommended play, I read why."*

**`DoD Hit Rate` and `Plays over cycle time` as Row 3 columns: cut them.** Zero plays are completed,
so a hit rate is undefined, and a column of blanks in the skills matrix reads as broken data. Say
they're the next two columns rather than showing them empty.

**Optional, ~5 min if you want a live number in Row 3:** add `Account Plays.In Flight` formula
(`IF({Status}="In flight",1,0)`) and roll it up onto `CSMs` as `Plays in Flight`. Would render
Dana 2 · Marcus 2 · Priya 1 · Sofia 0 · Ben 0 · Yuki 0. Ask and I'll build it.

---

## 6 · Verification gates

- [ ] ARR at Risk reads **$3,110,000**, 61%
- [ ] Value Coverage reads **0 / 6**, sitting in position two
- [ ] Sponsor Coverage reads **2 / 6** — not 1 / 6
- [ ] Stage distribution shows **3 at Stage 2** and an explicitly **empty Stage 4**
- [ ] Constraint chart: Value evidence **$2,300,000**, bars sum to **$5,060,000**
- [ ] Skills matrix `Book ARR` sums to **$5,060,000**
- [ ] **Marcus and Ben both show the pairing** — the seed-bug fix
- [ ] Renewal timeline shows Meridian at Q4, flagged ⚠️ but $0 at risk
- [ ] Inspection queue is one honest text element, not four empty grids

## 7 · Beat 1, for rehearsal

> "This is my Monday. ARR at risk — three point one one million, sixty-one percent of the book.
> Value coverage, zero out of six. No account in this book is compounding.
>
> This chart is the one I open the working session on: forty-five percent of the book is blocked on
> value evidence, not on sponsorship, not on adoption. That's my resourcing argument.
>
> And the skills matrix is on the same screen — how I staff and pair. Marcus is the strongest
> builder on the team and a two on executive presence, so he's paired with Ben on TrailLine's COO
> thread. That's an inspectable decision, not a favour I remembered to do."

Then switch to the Cockpit for beat 2.
