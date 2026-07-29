# Interface 1 · CSM Cockpit — build guide

## What you are building

One screen with two halves.

**The left half** is a list of the six accounts in the book. It's always visible. It's sorted so the
account with the most money at risk sits at the top.

**The right half** shows everything about whichever account you clicked in that list. Click a
different account, the right half changes. That right half is broken into five stacked sections:
where the account stands, what to do next, whether there's any proof of value, who we know there,
and what's happened recently.

Time: about an hour. Every step is done by hand in the Airtable web app. There is no way to script
this — Airtable has an API for building tables and fields, but none for building interfaces.

Your base: https://airtable.com/appFGgbrUOs62IndE

---

## Read this before you start — it explains most of the confusion

### Vocabulary

**Table** — a spreadsheet-like grid of records. You have eight of them: Accounts, Diagnostics,
Plays, CSMs, Stakeholders, Signals, Value Stories, Account Plays.

**Field** — a column on a table. `ARR` is a field on the Accounts table.

**Lookup field** — a special kind of field that pulls a value in from a *different* table. For
example, the four diagnostic scores really live on the Diagnostics table, but Accounts has lookup
fields that copy them across so they show up on an account too.

**Interface** — a built page for people to use, separate from the raw tables.

**Element** — one thing you drag onto an interface page. A field element shows one field. A text
element shows words you type. A button element does something when clicked. A grid element shows a
list of records.

**Label** — the words displayed above an element on screen. This is *not* the same as the field's
name in the table. You can show the field `Value Evidence Score` but label it "Value evidence." The
underlying field keeps its real name.

### The rule that trips everyone up

When you add a field element to an interface page, the picker only offers you **fields that exist on
the table the page was built on.** This page is built on **Accounts**, so it only offers Accounts
fields.

That's a problem, because a lot of what this screen needs to display doesn't live on Accounts. The
four scores, the AI's stage explanation, and the AI's recommended play all live on the
**Diagnostics** table. The interface cannot reach across and grab them.

The fix is to copy them onto Accounts as lookup fields first. **This has already been done for you.**
Six lookup fields were added to Accounts on 2026-07-28:

`Adoption` · `Sponsorship` · `Governance` · `Stage Rationale` · `Recommended Play` ·
`Constraint Override Reason`

So when this guide says "add a field called `Adoption`," it will be in your picker. If it isn't,
the most likely cause is that your page got built on the wrong table. Check that first before
hunting for the field.

### What's trustworthy in this guide, and what isn't

Every **field name, value and number** here was checked against the live base on 2026-07-28. If this
guide says Floor & Board's Sponsorship score is 1, it is 1.

The **click paths and menu names** were written from how Interface Designer is structured, not by
someone sitting and clicking through it. Airtable renames menu items between releases. If a menu on
your screen is worded differently from what's written here, trust your screen. The *what* and the
*why* are reliable; the exact *where* may drift.

---

## Step 1 · Three fixes to make in the base first

Do these in the tables, before you touch Interfaces. None of them can be done through the API, which
is why they're left to you.

### 1a. Give the Account Plays table a working name column

Open the **Account Plays** table. Look at the first column — it's called `Name` and every single row
is blank.

That column is the record's title. It's blank because it was supposed to be built as a formula and
never was.

Click the `Name` field header, choose to edit the field, change its type from **Single line text**
to **Formula**, and paste this in:

```
{Account Name} & " — " & {Play Code}
```

Save it. All nine rows should immediately fill in, reading like `Floor & Board Furniture — P2` and
`Voltaic Software — P6`.

**Do this before anything else.** Two moments in your demo create Account Plays records live — the
Accept button on this screen, and the automation in the last beat. If this column is still blank,
every record created in front of your audience appears with no name on it, at exactly the moment
you're showing off record creation.

### 1b. Delete a leftover field

Go to the **Plays** table. There's a field called `zz Applies at Stage (retired text — delete in
UI)`. Delete it.

It's a stale copy. The real field, `Applies at Stage`, was rebuilt properly as a multi-select and
sits alongside it. The old one couldn't be deleted through the API, which is why it's still there
with an ugly name flagging it for removal.

### 1c. Hide two clutter fields

These two aren't broken, they're just noise that Airtable generated automatically. Hide them, don't
delete them — deleting could break the links underneath.

- In **CSMs**, hide the field `From field: Paired With`
- In **Accounts**, hide the field `Diagnostic (from Current Diagnostic)`

---

## Step 2 · Create the interface

1. In your base, click **Interfaces** in the top navigation.
2. Click **Create interface**.
3. When it offers you templates or a blank start, choose **Blank**.
4. It will ask you to pick a layout. Choose **Record review**.
5. Name it **CSM Cockpit**.
6. It will ask which table the page draws from. Choose **Accounts**.

**Why Record review specifically.** It's the layout that gives you a list on one side and a detail
panel on the other, with the detail panel updating as you click through the list. That's exactly the
shape described above. The other layouts won't do this — Dashboard shows aggregate charts with no
per-record detail, and a blank page gives you no list-plus-detail wiring at all.

Once created, you should see a mostly empty page with a list of accounts down the left side. The
right side is where you'll spend the rest of this guide.

---

## Step 3 · Set up the list on the left

Click on the list to select it, and find its settings panel.

### Sorting

Set the sort to **`ARR at Risk`, descending** (largest first).

This is a deliberate design decision and it's worth saying out loud during the demo. Most CS tools
sort a book by renewal date. Sorting by money-at-risk instead means the largest preventable loss is
physically at the top of the screen every morning, without anyone having to think about it.

### Filtering

Leave the filter **off** for the demo, so that all six accounts are visible and your audience can
see the whole book.

In a real deployment you'd add a filter of `CSM is current user`, so each CSM only sees their own
accounts. It's worth building that filter once so you can show it exists, then switching it off
before you present. Restricting access is deliberately out of scope here — the demo shows everything
so the whole model is visible.

### Columns

Set the list to show these six fields, in this order:

1. `Account`
2. `ARR`
3. `Quarters to Renewal`
4. `Stage`
5. `Constraint` — but change the displayed label to **Binding constraint**
6. `Renewal Readiness`

### Important: you should end up with six rows, not five

The written spec in `interfaces.md` shows a table with only five accounts in it. That table is
incomplete. **Meridian Health Systems is missing from it**, and Meridian is the second-largest
account in the entire book at $1.1M.

It was almost certainly dropped by accident. Meridian shows $0 in the ARR-at-risk column, so when
sorted by that column it falls to the very bottom, where it's easy to overlook.

This is what your list should look like once configured:

| Account | ARR | Renewal | Stage | Binding constraint | Readiness |
|---|---|---|---|---|---|
| Floor & Board Furniture | $1,700,000 | 2 qtrs | 2 Contained | Sponsorship | ⚠️ No current value |
| Corvus Financial Group | $890,000 | 3 qtrs | 2 Contained | Value Evidence | ⚠️ No current value |
| Voltaic Software | $520,000 | 2 qtrs | 2 Contained | Governance | ⚠️ No current value |
| TrailLine Logistics | $540,000 | 7 qtrs | 1 Sponsored | Adoption | Not yet in cycle |
| Harbor Lane Retail | $310,000 | 5 qtrs | 0 Unaware | Value Evidence | Not yet in cycle |
| Meridian Health Systems | $1,100,000 | 4 qtrs | 3 Governed | Value Evidence | ⚠️ No current value |

The top three rows are the accounts carrying real risk, and they add up to $3,110,000. The bottom
three each contribute $0 to that figure.

---

## Step 4 · Block 1 — where this account stands

This is the top section of the right-hand panel. It answers: *how healthy is this account, really?*

Start by adding a **text element** at the top of the panel and typing the heading:
**Where this account is**

Then add a field element for each row in the table below. For each one you'll pick the field from
the picker, then set its display label separately.

| Pick this field | Set the label to | Where to put it |
|---|---|---|
| `Stage` | Stage | Top of the block |
| `Adoption` | Adoption | Grouped together as a set of four |
| `Sponsorship` | Sponsorship | " |
| `Governance` | Governance | " |
| `Value Evidence Score` | **Value evidence** | " |
| `Diagnostic Age` | Diagnostic age | Top-right corner |
| `Stage Rationale` | **Why this stage** | Below the four scores |
| `Constraint Override Reason` | Why this was overridden | Below that — see Step 9 |

### Things about that list that will otherwise confuse you

**`Value Evidence Score` has an inconsistent name, and that's intentional.** The other three scores
are just called `Adoption`, `Sponsorship`, `Governance`. This one has "Score" tacked on because it
was created earlier under that name, and the `ARR at Risk` formula depends on it. Renaming it risks
breaking that formula, and `ARR at Risk` is one of your headline numbers. So leave the field alone
and just set the *label* to "Value evidence." On screen nobody will know the difference.

**`Stage` and `Stage Rationale` are two genuinely different fields and you want both.**
`Stage` is short — it reads `2 Contained`. That's what the left-hand list uses, and what you want at
the top of this block. `Stage Rationale` is the full paragraph the AI wrote explaining *why* the
account is at that stage. Put the short one at the top and the paragraph lower down.

**The rationale will include a `STAGE:` line at the start.** The AI writes its answer as two labelled
lines, `STAGE:` and `RATIONALE:`, and the field holds both. That's fine — leave it. It actually helps,
because it makes clear that the whole block is one piece of AI output rather than something assembled
from parts.

**The four scores will display as filled dots, not bars.** The spec asks for bars. These are rating
fields, and Airtable draws rating fields as dots. Leave it alone. They communicate the same thing at
a glance, and converting them to plain numbers to get bars would break the 1-to-5 scale that the
diagnostic session interface relies on later.

### Diagnostic age

Set conditional formatting on the `Diagnostic Age` element so it greys out when the value is over 90.

**It will never actually grey out, and that's fine.** Every diagnostic in the base is dated
2026-07-20, so they're all a few days old and nowhere near 90. The whole book was assessed in one
sweep. (Check the number on screen before you present — it climbs by one each day.)

Build the rule anyway, and handle it with a sentence in the room: *"every diagnostic here is days
old, because we just ran the sweep across the whole book. At ninety days this greys out and the
account drops into my inspection queue."*

**Do not backdate a record to make the grey state appear.** It would contradict the story you're
telling — that this is a brand new operating model and the book was just assessed. A manufactured
stale record buys you a visual effect and costs you the narrative.

---

## Step 5 · Block 2 — the recommended play

This section answers: *so what do I actually do about it?*

Add a text element as a heading: **Your next play**

Then build these five things in order:

**1. Add a field element for `Constraint`.** Set its label to **Binding constraint (computed)**.

To be completely clear, because this caused confusion already: "Binding constraint" is text you type
into the label box. There is no field called "Binding constraint." The field you pick from the picker
is called `Constraint`.

**2. Add a text element directly underneath it** reading: *Lowest score selects the play.*

This one line does a lot of work. It tells the reader that this isn't a judgement call, it's the
mechanical result of taking whichever of the four scores is lowest.

**3. Add a field element for `Recommended Play`.**

This prints the AI's full recommendation. It comes out as five labelled parts: the play name, why
that play was chosen, the first three moves to make, which partner team to bring in, and whether a
follow-on play should be queued behind it. It's several paragraphs, so give it room.

**4. Add a linked-record element for `Current Diagnostic`.** Label it **Challenge this — open the
diagnostic**.

No buttons. Buttons aren't required, and there's a constraint that makes them awkward anyway:
everything from the Diagnostics table reaches this page as a **lookup field, and lookup fields are
read-only**. Nobody can type into them from here. Getting the CSM onto the actual Diagnostics record
is both simpler to build and better for what you're demonstrating.

Clicking this element opens the Diagnostics record in an expanded, editable view. That record is
where a CSM pushes back on what the system told them.

### Why this is the point, not a workaround

There are **two separate things a CSM can challenge**, and both are already built:

**They can challenge the formula's diagnosis.** The four scores are editable, each with its own
evidence note. If the CSM thinks adoption is really a 2 rather than a 4, they change it and say why
in the evidence field. And if they think the computed binding constraint is wrong even though the
scores are right, they set **`Constraint Override`** — a dropdown with all four dimensions — and
explain themselves in **`Constraint Override Reason`**. That's exactly what happened on Harbor Lane.

**They can challenge the AI's recommendation.** **`Play Accepted`** is a dropdown with three
options: **Accepted**, **Overridden**, **Pending**. If they're not running the recommended play, they
set it to `Overridden` and write why in **`Override Reason`**.

This is the whole argument for the system. The base does not hand a CSM an answer and expect
compliance. It hands them a diagnosis, shows its working, and gives them two labelled places to
disagree with it in writing. Everything starts at `Pending` — nothing has been rubber-stamped.

And the overrides aren't just recorded, they're inspected. The Director's screen has a queue that
collects every override for review. That's the feedback loop: the recommendations improve because
someone reads the objections.

**Optional, if you want the play to be tracked once accepted.** Add an automation that watches
`Play Accepted`, and when it changes to `Accepted`, creates the matching `Account Plays` record. An
automation can write to Diagnostics even though the interface can't. Skip it if you're short on
time — the nine `Account Plays` records already exist, so nothing on screen depends on it.

### Making the constraint appear in red

The spec asks for the binding constraint to be called out in red. Airtable won't let you apply
conditional colour to a lookup field, which is what `Constraint` is.

The workaround takes about five minutes. Create four separate text elements, one for each possible
constraint — "Sponsorship", "Governance", "Adoption", "Value Evidence". Style all four in red. Then
set conditional visibility on each one so it only appears when `Constraint` equals that value.

Only one of the four will ever be visible at a time, so on screen it looks like a single red field
that changes as you click between accounts.

There's a second approach — converting `Constraint` from a formula into a single-select that an
automation writes into. **Don't do that.** It would turn a derived value into stored data that can
drift out of sync, and it breaks the thing you're demonstrating, which is that the constraint is
computed rather than chosen.

---

## Step 6 · Block 3 — the value position

This section answers: *can we prove this account is getting value?*

Add a heading: **The value position**

**1. Add a field element for `Latest Value Story Status`.** This shows whether the most recent value
story has been drafted, reviewed, or validated by the customer.

**2. Add a grid element showing `Value Stories` filtered to this account.** Show these columns:
`Value Story`, `Business Metric`, `Status`, `Narrative`.

**3. No button here either.** Make the grid rows clickable so the CSM opens the value story record
itself, the same pattern as Block 2.

That's where the useful work happens. On the open record they can edit the use case, baseline,
current figure and source of truth, and regenerate the `Narrative` field once there's something for
it to work from. The AI narrative is only as good as the evidence underneath it, and the evidence is
what a CSM actually has to go and get.

**This is also how you run the live AI demo.** Two of your beats regenerate the narrative on Corvus
and on Floor & Board. Both already have value story records — open them from this grid and
regenerate the field there.

### What you'll see in this block, and why it's correct

**Value coverage across the book is 0 out of 6.** Not a single account has a customer-validated value
story. That is not missing data — it's the central finding of the whole strategic brief. The platform
is working and people are using it, but nobody has ever proved the value to the person who signs the
renewal.

Two details that look like bugs and aren't:

- **TrailLine has no value story at all.** Its block will be empty apart from the button. There are
  six value stories spread across five accounts.
- **Floor & Board has two value stories, not one.** The status field handles that and still reads
  `Draft` rather than `Draft, Draft`.

---

## Step 7 · Block 4 — who we know

This section answers: *who are our people at this account, and is that enough?*

Add a heading: **Who we know**

**1. Add a grid element showing `Stakeholders` filtered to this account.** Show these columns:
`Name`, `Title`, `Role`, `Sentiment`, `Status`, `Last Touch`.

**2. Sort that grid by `Status`, ascending.** This pushes departed and unengaged contacts to the top
of the list rather than burying them.

**3. Add a field element for `Sponsor Roles`,** and add a text element next to it noting that the
target is three mapped threads.

**About the strikethrough.** The spec asks for departed contacts to appear with a line through their
name. Interface Designer has no strikethrough formatting, so you can't do that literally.

Sorting by Status gets you the same outcome by a different route. On Floor & Board, the departed
champion becomes the first row in the block. That's the entire point — the demo narrative is that a
CSM opening this screen on day one immediately sees that their main contact left three months ago.
Position achieves that just as well as a line through the text.

---

## Step 8 · Block 5 — signals

This section answers: *what's actually been happening on this account lately?*

Add a heading: **Signals**

Add a grid element showing `Signals` filtered to this account. Configure it to:

- Sort by `Date`, newest first
- Show only the most recent 8
- Colour rows by `Direction`, so positive and negative signals are visually distinct
- Display these columns: `Signal`, `Type`, `Direction`, `Date`, `Detail`

---

## Step 9 · Why two things on this screen disagree with each other

This is the part of the build that needs a decision, so read it before you finalise the labels.

This screen displays two things that look like they're answering the same question, and **on four of
the six accounts they give different answers.** Both are correct. They're answering different
questions.

**`Constraint`** is a formula. It looks at the four scores, finds the lowest, and names it. Its
entire job is to **choose which play to run**.

**`Stage Rationale`** is the AI explaining **why the account sits at the maturity stage it does**.
That's a different question, and it can have a different answer.

Here's exactly where they agree and disagree:

| Account | Constraint says | The AI says | Same? |
|---|---|---|---|
| Floor & Board | Sponsorship | governance | no |
| Corvus | Value Evidence | governance | no |
| TrailLine | Adoption | sponsorship | no |
| Harbor Lane | Value Evidence | sponsorship | no |
| Voltaic | Governance | governance | yes |
| Meridian | Value Evidence | value evidence | yes |

If you put these next to each other with no explanation, a CSM reads a contradiction and loses trust
in both.

### How to label it so it reads clearly

**Keep the block headings plain.** *Where this account is* and *Your next play*. That's how a CSM
navigates the screen, and it's what they care about. Don't clutter the headings with explanation.

**Then add a small tag to only the two elements that clash:**

- Tag the AI paragraph with **AI read**
- Tag the constraint with **(computed)**

The reason for doing it this way: someone who never notices the tags still reads the screen correctly,
because the headings tell them what each section is for. Someone who *does* spot the disagreement
finds the explanation sitting four words away. You get clarity without making the whole screen about
provenance.

**Keep this line for speaking, not for the screen:** *the constraint picks the play, the rationale
explains the stage.* It's the right sentence out loud and too abstract printed in a UI.

### Harbor Lane and Floor & Board have identical scores but different constraints

Expect to be asked about this, because both rows sit on the same screen a few lines apart.

Both accounts score 1 on sponsorship, 1 on governance, and 1 on value evidence. Identical. Yet they
show different binding constraints.

**Floor & Board shows Sponsorship.** When several scores tie for lowest, the formula picks between
them in a fixed order, and Sponsorship comes first in that order.

**Harbor Lane shows Value Evidence,** because a human overrode the formula. The reasoning came from
the assessment document itself, which says the team *"would need a clear value demonstration tied to
an existing use case to engage."* Sponsorship is certainly missing at Harbor Lane too — but it isn't
what's blocking progress, because there's nothing yet worth sponsoring. You need a proof point before
you can go find an executive to back it.

That reasoning is now stored in the base, in a field called `Constraint Override Reason`. **Add that
field to Block 1 with conditional visibility so it only appears when it has content.** Right now
Harbor Lane is the only account with anything in it.

**Treat this as a feature, not an awkward question.** The formula said sponsorship. The AI,
independently, also said sponsorship. A human looked at both, disagreed, overrode them, and wrote down
their reasoning where anyone can inspect it. That's the human-in-the-loop story told with a real
artifact instead of a claim. Open the field and talk about it.

---

## Step 10 · Check your work

Go through these on screen before you call it finished:

- [ ] The left list shows **six** accounts, with Floor & Board first and Meridian present
- [ ] The ARR column across all six adds up to **$5,060,000**
- [ ] The top three rows add up to **$3,110,000**
- [ ] Voltaic shows **Stage 2** even though its adoption score is **5** — this is the account that
      looks far healthier than it is, and it's the sharpest thing in the demo
- [ ] Floor & Board shows constraint **Sponsorship** while its AI paragraph says **governance**, and
      the two tags make that legible rather than confusing
- [ ] Harbor Lane displays its override reason; the other five accounts don't
- [ ] Each account recommends the right play. Check them by name, not by position:

      | Account | Play |
      |---|---|
      | Floor & Board | **P2** Re-Sponsor |
      | Corvus | **P4** Quantify & Translate |
      | Voltaic | **P6** Governance Partner Insert |
      | TrailLine | **P3** Kickoff Re-Contract |
      | Harbor Lane | **P1** Prove One Thing |
      | Meridian | **P5** Governance Case |

- [ ] Only **Floor & Board and Voltaic** mention a follow-on play (P8)
- [ ] Every value story reads **Draft** — and **TrailLine has none at all**, which is expected
- [ ] Clicking the diagnostic in Block 2 opens an **editable** record where you can change a score,
      set `Constraint Override`, and set `Play Accepted` to `Overridden` with a reason
- [ ] Clicking a value story in Block 3 opens an **editable** record where `Narrative` can be
      regenerated

If any of these come out differently, it's a build configuration problem rather than a data problem.
All ten were verified directly against the live base on 2026-07-28.

---

## What to say when you demo this screen

You arrive here from the Director's screen, so open by naming the switch in perspective.

> "This is the same base, now as a CSM sees it. Floor & Board is at the top of Dana's list — sorted
> by money at risk rather than by renewal date, so the largest preventable loss is on her screen
> every single morning.
>
> Sponsorship scores a 1. Her champion left three months ago. One thread mapped against a target of
> three. No value narrative at all. And the renewal conversation is two quarters out.
>
> The recommended play is P2, Re-Sponsor — with three specific moves and Sales named as the partner
> to bring in. She clicks Accept and her week has a shape.
>
> No pattern recognition required. That's a CSM in month four running the same first move as the
> best CSM on the team."
