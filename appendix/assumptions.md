# Assumptions

The brief invites these and says it's fine if they're off. Flagged by **how much of my argument
falls over if the assumption is wrong** — that seems more useful than a flat list.

---

## Load-bearing — the priorities change if these are wrong

**1 · CS influences or carries a renewal and expansion number.**
The entire value-realization priority assumes CS is measured on commercial outcomes rather than
satisfaction or adoption. If CS is a pure adoption function and renewals sit entirely with
Sales, priority 2 drops to third and the first 90 days go to enablement and coverage instead.
*Confidence: high — the brief says targets are "increasingly tied to demonstrable, AI-driven
business outcomes."*

**2 · Professional Services has the capacity to take the technical load these plays put on it.**
The ownership boundary — CSMs never have to be the smartest technical person in the room — is the
load-bearing beam of the whole operating model. *That the function exists isn't an assumption:* the
role names Professional Services among its cross-functional partners. **Its capacity is.** Four of
eight plays route technical delivery to it, and if it's oversubscribed then the depth gap is a
hiring and training problem rather than a staffing one, and the 90 days look completely different.
*Confidence: medium on capacity. This is the assumption I'd most want checked on day one.*

**3 · Two partner capabilities exist in some form — and I've named them by what they produce,
not by a team I'm claiming exists.**
Beyond the partners the role explicitly names (Renewals, Support, Professional Services, Product,
Sales), two plays depend on capabilities I couldn't verify the shape of, so I've described them
functionally rather than guessing at an org chart:

- **Security & Risk** — whoever can produce customer-facing AI risk and controls artifacts. P5
  assumes I'm *orchestrating* that artifact rather than authoring one from nothing. If that
  capability doesn't exist in customer-facing form, Meridian is a two-quarter project rather than
  a two-month one, and I'd have to tell that sponsor early rather than discover it at week six.
- **Value Validation** — whoever can stand behind a quantitative value claim before it reaches a
  customer's CFO. P4 assumes someone other than the CSM is accountable for the number's integrity.
  If nobody is, then either CS owns quantitative validation itself — which is a capability and
  headcount question, not a process one — or every value narrative carries more risk than the
  status gate implies.

Wherever these actually sit, that's who the plays mean. **Mapping both to real owners is a day-one
question**, and it's the first thing I'd ask about the operating model.
*Confidence: medium-low, and lowest for AI-specific governance content specifically. These are the
two places I'm most likely to be wrong about how the company is arranged.*

**4 · These six accounts are representative of the wider book of ~15 CSMs' worth of accounts.**
I'm generalizing structural patterns from six. The brief says "your job is the book, not any
one account," which implies they're a fair sample, but six is six. If Value evidence is genuinely
a 1 across the full book, priority 2 (the value engine) is right. If these six were selected as the
interesting ones, the real book may skew toward Harbor Lane — quiet, healthy, unrealized — and
the priority shifts toward demand creation.
*Confidence: medium.*

---

## Structural — shape the design, wouldn't reverse the priorities

**5 · A CSM can get a 45-minute structured working session with a customer.**
The diagnostic is designed to be run *with* the customer, screen-shared. If these relationships
can't support that, it degrades into a CRM field scored from a desk and loses most of its
value. Meridian's order-taking drift suggests at least one relationship where this would be
awkward to introduce.

**6 · Renewal dates and ARR live in a CRM that can sync.**
Static in the prototype. Called out in the build's "not built" list. If there's no clean sync,
the base goes stale by month two and that's a real failure mode, not a nitpick.

**7 · Airtable's AI fields can take long custom prompts with multiple field references and
return structured multi-line text.**
The three AI fields depend on this. My understanding is yes, but I'd verify prompt length
limits and output stability before building the demo on it. **I'd want to be corrected here in
the session if I've got it wrong** — I'd rather find out in the room than have it break live.

**8 · The 15 CSMs skew relationship-led over technically deep, roughly half and half.**
Drawn from the brief's description, and the input to the skills matrix. If it's more like 12:3,
partner and pairing capacity becomes the binding constraint before methodology does — I'd pull
the team operating system (priority 3) forward and lean harder on partners than on pairing, since you
can't pair your way out of having only three technical CSMs.

**9 · "AI transformation" here means workflow automation, AI fields and agents inside Airtable
as the system of record — not that we're consulting on the customer's whole enterprise AI
strategy.**
The scope of what a CSM is credibly selling changes completely between those two readings.
I've taken the narrower one.

---

## Cosmetic — mentioned for completeness

**10 · Roughly one HTCSM per 4–6 high-touch accounts**, from 15 CSMs against a book of this
shape. Only affects the CSM seed data.

**11 · Support owns break/fix**, so Floor & Board's automation break isn't CSM work. If CSMs
are the escalation path, that's real capacity I haven't accounted for.

**12 · "Quarters to renewal" is knowable and reasonably accurate.** Stored as a static number
since the snapshot gives relative timing only.

**13 · Today is late July 2026.** All seed dates are relative to this.

---

## Invented content, stated plainly

Everything factual about the six accounts comes from the snapshot. **What I made up:** all
diagnostic scores on the four dimensions (my judgment, reasoning in
[`../docs/02-book-diagnosis.md`](../docs/02-book-diagnosis.md)), the CSM skills-matrix ratings
and pairings, all stakeholder and CSM names, all signal records, and — most importantly — **the
numbers in the Corvus value narrative** (14 min → 3 min triage, ~2,100 cases/month). The snapshot
contains no metrics at all. I invented those so the AI value-narrative field has something to
work with in a demo; the record is flagged as illustrative in its `Source of Truth` field and
deliberately left in `Draft` status. See
[`../airtable-build/data/README.md`](../airtable-build/data/README.md).

**The thing I'd want believed:** every other value narrative is empty of numbers on purpose. That's
what the book actually looks like, and it's what makes the AI field's refusal behaviour
demonstrable on real data rather than staged.
