#!/usr/bin/env python3
"""Render the strategic brief to print-ready HTML.

Deliberately narrow: it supports exactly the markdown constructs that
docs/01-strategic-brief.md uses, and raises on anything it does not
recognise rather than silently dropping it.
"""
import html
import re
import sys

CODE = "\x00CODE%d\x00"


def inline(text):
    """Inline markdown -> HTML. Order matters: code spans are protected
    first so emphasis inside them is left alone, and bold runs before
    italic so ** is never mistaken for two * delimiters."""
    spans = []

    def stash(m):
        spans.append(html.escape(m.group(1)))
        return CODE % (len(spans) - 1)

    text = re.sub(r"`([^`]+)`", stash, text)
    text = html.escape(text)
    # Relative links to sibling docs cannot resolve in a standalone PDF,
    # so keep the link text and drop the target.
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text, flags=re.S)
    text = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", text, flags=re.S)
    for i, span in enumerate(spans):
        text = text.replace(CODE % i, f"<code>{span}</code>")
    return text


def convert(md):
    lines = md.split("\n")
    out = []
    i = 0
    seen_h1 = False

    while i < len(lines):
        line = lines[i]

        if not line.strip():
            i += 1
            continue

        if line.startswith("# "):
            out.append(f"<h1>{inline(line[2:].strip())}</h1>")
            seen_h1 = True
            i += 1
            continue

        if line.startswith("## "):
            out.append(f"<h2>{inline(line[3:].strip())}</h2>")
            i += 1
            continue

        if re.fullmatch(r"-{3,}", line.strip()):
            out.append("<hr>")
            i += 1
            continue

        if line.startswith(">"):
            block, i = [], i
            while i < len(lines) and lines[i].startswith(">"):
                block.append(lines[i].lstrip(">").strip())
                i += 1
            paras, cur = [], []
            for b in block:
                if b:
                    cur.append(b)
                elif cur:
                    paras.append(" ".join(cur))
                    cur = []
            if cur:
                paras.append(" ".join(cur))
            body = "".join(f"<p>{inline(p)}</p>" for p in paras)
            out.append(f"<blockquote>{body}</blockquote>")
            continue

        if re.match(r"\d+\. ", line):
            items = []
            while i < len(lines) and re.match(r"\d+\. ", lines[i]):
                cur = [re.sub(r"^\d+\. ", "", lines[i])]
                i += 1
                # continuation lines are indented under the marker
                while i < len(lines) and lines[i].startswith("   ") and lines[i].strip():
                    cur.append(lines[i].strip())
                    i += 1
                items.append(" ".join(cur))
                while i < len(lines) and not lines[i].strip():
                    if i + 1 < len(lines) and re.match(r"\d+\. ", lines[i + 1]):
                        i += 1
                    else:
                        break
            body = "".join(f"<li>{inline(it)}</li>" for it in items)
            out.append(f"<ol>{body}</ol>")
            continue

        # paragraph: join wrapped lines so bold/italic spanning a line
        # break is parsed as one run
        cur = []
        while i < len(lines) and lines[i].strip() and not re.match(
            r"(#{1,6} |>|-{3,}$|\d+\. )", lines[i]
        ):
            cur.append(lines[i].strip())
            i += 1
        para = " ".join(cur)
        cls = ""
        if seen_h1 and not any(o.startswith(("<p", "<blockquote", "<h2")) for o in out):
            cls = ' class="subtitle"'
        out.append(f"<p{cls}>{inline(para)}</p>")

    return "\n".join(out)


if __name__ == "__main__":
    src, dst, css = sys.argv[1], sys.argv[2], sys.argv[3]
    with open(src, encoding="utf-8") as f:
        body = convert(f.read())
    with open(css, encoding="utf-8") as f:
        style = f.read()
    page = (
        "<!doctype html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
        "<title>Strategic Brief — High Touch Customer Success</title>\n"
        f"<style>\n{style}\n</style>\n</head>\n<body>\n{body}\n</body>\n</html>\n"
    )
    with open(dst, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"wrote {dst} ({len(page)} bytes)")
