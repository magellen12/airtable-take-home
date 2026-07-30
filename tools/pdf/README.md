# PDF rendering of the strategic brief

Produces `Strategic-Brief-High-Touch-Customer-Success.pdf` at the repo root, the recruiter-facing
copy of `docs/01-strategic-brief.md`.

## Why these files exist

There is **no pandoc, no wkhtmltopdf, no node and no python `markdown` module** on this machine, so
there is no off-the-shelf markdown→PDF path. **Google Chrome is installed** and does the whole job
headlessly, with full fidelity — emoji, em dashes, box-drawing and wide tables all render as
ordinary CSS.

| File | What it is |
|---|---|
| `brief-plain.md` | **The PDF's source text.** Same content as `docs/01-strategic-brief.md`, with em dashes, en dashes and `×` removed — a presentation variant, not a second draft. |
| `md2html.py` | Narrow markdown→HTML converter. Supports exactly the constructs the brief uses. |
| `brief.css` | Print stylesheet. `@page` sets Letter and margins. |

## Regenerate

```sh
cd tools/pdf
python3 md2html.py brief-plain.md brief.html brief.css
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" \
  --headless --disable-gpu --no-pdf-header-footer \
  --print-to-pdf=../../Strategic-Brief-High-Touch-Customer-Success.pdf \
  "file://$PWD/brief.html"
```

## Verify before calling it done

Do not trust the render. Poppler is installed:

```sh
pdfinfo ../../Strategic-Brief-*.pdf | grep Pages        # must be 2 — the assessment says 1-2
pdftoppm -png -r 110 ../../Strategic-Brief-*.pdf page   # then actually look at the images
pdftotext ../../Strategic-Brief-*.pdf - | grep -c '—'   # must be 0
```

## Two rules

1. **`brief-plain.md` and `docs/01-strategic-brief.md` must stay content-identical.** They differ
   only in punctuation. Any edit to one has to be made in the other — the user chose this split
   deliberately, keeping em dashes in the repo and out of the PDF.
2. **The page count is a hard constraint.** The assessment asks for 1-2 pages and the brief's own
   header claims it. If content growth pushes it to 3, tighten `brief.css` (body size, leading)
   before cutting anything the user asked for.
