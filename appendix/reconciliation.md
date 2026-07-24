# Reconciliation — two strategy drafts, merged

The assessment says: *"we'd love to hear how you used AI — what you kept, changed, and verified."*
The most substantive version of that story isn't about tooling — it's this: two independent
strategy drafts of the same book, and the discipline of merging them.

I wrote one version. A second, independent articulation of the same six-account book was then put
in front of me. This documents how I reconciled them — what I **kept**, **combined**, and
**deleted**, and why — grounded against the
[Director JD](https://job-boards.greenhouse.io/airtable/jobs/8602201002) rather than personal
preference. The result is [v2.0](../CHANGELOG.md) (`98b4b78`).

**The headline finding is the convergence itself.** Two drafts, written independently, landed on
the same three structural patterns, the same three priorities, and the same read of the two
trap accounts (Voltaic, Corvus). That agreement is a stronger signal than either draft alone —
it means the diagnosis is reproducible, not a single analyst's take. So this was a
sharpen-and-merge, not a rewrite.

---

## What each draft was stronger at

| | My draft | The alternate |
|---|---|---|
| **Backbone** | Quantified — a scored table, four headline numbers, a "binding constraint" engine | Prose point-of-view, no scores |
| **Pattern 2** | Customer-side person-dependence + a weak, separate "4th pattern" about the team | Person-dependence framed as **both sides of the table** — customer *and* CSM |
| **Priorities** | Diagnostic / Value / Plays | Methodology / Value / **Team OS** (team as a headline) |
| **Governance** | Scattered across constraint-specific plays | A **required through-line** answering three accounts at once |
| **Team depth** | Ownership table + "I take the COO thread myself" | **Skills matrix + pairing-of-complements** (systematic, not heroic) |
| **Engine** | Lowest-dimension constraint rule | "stage → plays" |
| **Vocabulary** | Capability / Proof | Adoption / Value evidence (tracks the JD) |

The JD settled every close call: it rewards *"data-driven… operational rigor… systems thinking,"*
leads its responsibilities with *"Lead and Scale a High-Performing Team,"* names *"Centers of
Excellence"* and *"value realization"* explicitly, and lists *adoption* and *customer maturity
progression* among the owned metrics.

---

## KEEP — my differentiators the alternate lacked

- **The quantified scored table + four numbers** ($5.06M book, $3.11M/61% at risk, value evidence
  1.3 vs adoption 3.2). The receipts prose doesn't have. *JD: "data-driven, operational rigor."*
- **The binding-constraint engine** (lowest dimension picks the play, not the average) —
  reconciled with the alternate's "stage → plays" as **stage describes, constraint prescribes.**
- **The Stage-0 exception + "the model was wrong once on Harbor Lane" story** — a coachability
  signal the rubric explicitly scores.
- **The AI `INSUFFICIENT EVIDENCE` refusal** — the strongest single demo beat.

## COMBINE — the alternate's sharper framing, folded in

- **Pattern 2 → two-sided.** Person-dependence on *both* sides of the table; absorbed my weak
  standalone "4th pattern." The single biggest upgrade.
- **Pattern 1 → "evidence problem, not adoption problem."** I had the substance; took the phrasing.
- **Priorities → Methodology / Value engine / Team OS**, matching the JD's own structure (which
  leads with team leadership).
- **Governance → a required through-line** answering Meridian (risk-and-controls case), Voltaic
  (governance wedge), and Floor & Board (a CoE so the vision survives the next departure).

## ADD — mechanisms the alternate had that mine didn't

- **Skills matrix (builder depth × exec presence × domain) + deliberate pairing**, replacing my
  hero-mode "I take the COO thread myself." *JD: "teams who act as strategic advisors and
  technically capable partners."*
- **Metrics in JD vocabulary:** stage progression QoQ, value narratives ready ≥1 quarter before
  renewal. And a reframed stance on customer health — the four-dimension diagnostic *is* the
  health read, kept multidimensional so it never averages away the score that predicts a loss.

## DELETE / FIX

- **Deleted** the orphan "4th pattern" (absorbed into pattern 2) and the hero-mode framing.
- **Renamed** the four dimensions to JD-aligned labels — Adoption depth / Sponsorship &
  multi-threading / Governance maturity / Value evidence (was Capability / … / Proof). Scores
  were unchanged; the rename rippled through schema, prompts, seed CSVs, and the script.
- **Fixed a real bug the re-read surfaced:** Meridian was scored with Value evidence as its
  lowest dimension but labeled "Governance" as its binding constraint — a violation of my own
  lowest-score rule. Corrected so the formula and the prose agree. It's also a *better*
  diagnosis: Meridian isn't governance-immature (it has a CoE and a review board); it lacks the
  evidence *artifact* the board needs, which routes it to a risk-and-controls case (P5).

---

## VERIFY — how I checked the merge didn't break anything

Not by eye — the numbers were recomputed:

- `python3 scripts/seed_airtable.py --dry-run` → all 8 CSVs parse, all 83 linked references
  resolve.
- Constraints recomputed from the seed scores for all six accounts: Floor & Board → Sponsorship,
  Meridian → **Value Evidence** (the fix), TrailLine → Adoption, Corvus → Value Evidence, Harbor
  Lane → Value Evidence (Stage-0 exception), Voltaic → Governance.
- `ARR at Risk` recomputed to **$3,110,000**; book total **$5,060,000**; ARR-by-constraint has
  Value evidence largest at $2.3M — which the brief and the Director dashboard both cite.
- Full-repo sweep for stale vocabulary (old dimension names, old play names, old partner labels)
  until clean.

---

## What this says about how I'd run the team

The reconciliation is a small model of the operating rhythm in
[`../docs/04-operating-model.md`](../docs/04-operating-model.md): two independent takes, a
structured merge that keeps the best of each, a bias toward the sharper framing, and verification
that isn't "looks right." When two people — or a person and a model — disagree on an account, the
answer isn't to pick a winner; it's to find what each saw that the other missed, and to check the
result against the data. That's the same discipline the diagnostic and the play retro are built
to produce across fifteen CSMs.
