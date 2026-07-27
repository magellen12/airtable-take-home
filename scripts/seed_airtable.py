#!/usr/bin/env python3
"""
Create the HTCS Transformation OS base and load the seed data via the Airtable Web API.

  export AIRTABLE_PAT=pat...            # needs schema.bases:write, data.records:write
  export AIRTABLE_WORKSPACE_ID=wsp...
  python3 scripts/seed_airtable.py --dry-run     # validate CSVs, create nothing
  python3 scripts/seed_airtable.py

What this does NOT do: AI fields, automations and interfaces are not creatable via the API.
Add those in the UI — prompts are in airtable-build/ai-components.md, steps in
airtable-build/build-checklist.md.

Standard library only. No dependencies.
"""

import argparse
import csv
import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

API = "https://api.airtable.com/v0"
DATA = Path(__file__).resolve().parent.parent / "airtable-build" / "data"

# ---------------------------------------------------------------- schema

SELECT = lambda *opts: {"choices": [{"name": o} for o in opts]}

TABLES = [
    {
        "name": "CSMs",
        "fields": [
            {"name": "Name", "type": "singleLineText"},
            {"name": "Tenure (months)", "type": "number", "options": {"precision": 0}},
            {"name": "Strength Profile", "type": "multipleSelects",
             "options": SELECT("Relationship", "Technical/Builder", "Executive", "Commercial", "Governance")},
            {"name": "Builder Depth", "type": "rating", "options": {"max": 5, "color": "blueBright", "icon": "star"}},
            {"name": "Executive Presence", "type": "rating", "options": {"max": 5, "color": "blueBright", "icon": "star"}},
            {"name": "Domain", "type": "rating", "options": {"max": 5, "color": "blueBright", "icon": "star"}},
            # Self-link — created in the deferred pass. Populated in the UI, not by the loader
            # (self-references can't resolve during a single-pass create); see SKIP below.
            {"name": "Paired With", "type": "multipleRecordLinks", "options": {"linkedTableName": "CSMs"}},
            {"name": "Development Focus", "type": "singleLineText"},
            {"name": "Plays Authored", "type": "number", "options": {"precision": 0}},
        ],
    },
    {
        "name": "Plays",
        "fields": [
            {"name": "Play", "type": "singleLineText"},
            {"name": "Code", "type": "singleLineText"},
            {"name": "Clears Constraint", "type": "singleSelect",
             "options": SELECT("Sponsorship", "Governance", "Adoption", "Value Evidence")},
            {"name": "Applies at Stage", "type": "singleLineText"},
            {"name": "CSM Owns", "type": "multilineText"},
            {"name": "Partner Leads", "type": "multipleSelects",
             "options": SELECT("Professional Services", "Security & Risk", "Product", "Sales", "Renewals", "Value Validation", "Support")},
            {"name": "Artifact Produced", "type": "multilineText"},
            {"name": "Definition of Done", "type": "multilineText"},
            {"name": "Typical Duration (wks)", "type": "number", "options": {"precision": 0}},
            {"name": "First Three Moves", "type": "multilineText"},
            {"name": "Template Status", "type": "singleSelect", "options": SELECT("Templated", "Specified")},
        ],
    },
    {
        "name": "Accounts",
        "fields": [
            {"name": "Account", "type": "singleLineText"},
            {"name": "Function", "type": "singleLineText"},
            {"name": "ARR", "type": "currency", "options": {"precision": 0, "symbol": "$"}},
            {"name": "Seats", "type": "number", "options": {"precision": 0}},
            {"name": "Contract Stage", "type": "singleSelect",
             "options": SELECT("First year", "Mid-term", "Renewal cycle")},
            {"name": "Quarters to Renewal", "type": "number", "options": {"precision": 0}},
            {"name": "CSM", "type": "multipleRecordLinks", "options": {"linkedTableName": "CSMs"}},
            {"name": "Notes", "type": "multilineText"},
        ],
    },
    {
        "name": "Diagnostics",
        "fields": [
            {"name": "Diagnostic", "type": "singleLineText"},
            {"name": "Account", "type": "multipleRecordLinks", "options": {"linkedTableName": "Accounts"}},
            {"name": "Diagnostic Date", "type": "date", "options": {"dateFormat": {"name": "iso"}}},
            {"name": "Run By", "type": "multipleRecordLinks", "options": {"linkedTableName": "CSMs"}},
            {"name": "Sponsorship", "type": "rating", "options": {"max": 5, "color": "redBright", "icon": "star"}},
            {"name": "Sponsorship Evidence", "type": "multilineText"},
            {"name": "Governance", "type": "rating", "options": {"max": 5, "color": "redBright", "icon": "star"}},
            {"name": "Governance Evidence", "type": "multilineText"},
            {"name": "Adoption", "type": "rating", "options": {"max": 5, "color": "redBright", "icon": "star"}},
            {"name": "Adoption Evidence", "type": "multilineText"},
            {"name": "Value Evidence", "type": "rating", "options": {"max": 5, "color": "redBright", "icon": "star"}},
            {"name": "Value Evidence Notes", "type": "multilineText"},
            {"name": "Session Notes", "type": "multilineText"},
            {"name": "Play Accepted", "type": "singleSelect", "options": SELECT("Accepted", "Overridden", "Pending")},
            {"name": "Override Reason", "type": "multilineText"},
        ],
    },
    {
        "name": "Stakeholders",
        "fields": [
            {"name": "Name", "type": "singleLineText"},
            {"name": "Account", "type": "multipleRecordLinks", "options": {"linkedTableName": "Accounts"}},
            {"name": "Title", "type": "singleLineText"},
            {"name": "Role", "type": "singleSelect",
             "options": SELECT("Exec Sponsor", "Economic Buyer", "Champion", "Builder", "Blocker", "User Lead")},
            {"name": "Sentiment", "type": "singleSelect",
             "options": SELECT("Advocate", "Supportive", "Neutral", "Skeptical", "Opposed")},
            {"name": "Last Touch", "type": "date", "options": {"dateFormat": {"name": "iso"}}},
            {"name": "Status", "type": "singleSelect", "options": SELECT("Active", "Departed", "Unengaged")},
            {"name": "Notes", "type": "multilineText"},
        ],
    },
    {
        "name": "Signals",
        "fields": [
            {"name": "Signal", "type": "singleLineText"},
            {"name": "Account", "type": "multipleRecordLinks", "options": {"linkedTableName": "Accounts"}},
            {"name": "Type", "type": "singleSelect",
             "options": SELECT("Adoption", "Support", "Commercial", "Engagement", "Governance")},
            {"name": "Direction", "type": "singleSelect", "options": SELECT("Positive", "Neutral", "Negative")},
            {"name": "Date", "type": "date", "options": {"dateFormat": {"name": "iso"}}},
            {"name": "Detail", "type": "multilineText"},
            {"name": "Weight", "type": "number", "options": {"precision": 0}},
        ],
    },
    {
        "name": "Value Stories",
        "fields": [
            {"name": "Value Story", "type": "singleLineText"},
            {"name": "Account", "type": "multipleRecordLinks", "options": {"linkedTableName": "Accounts"}},
            {"name": "Use Case", "type": "singleLineText"},
            {"name": "Business Metric", "type": "singleSelect",
             "options": SELECT("Cost", "Cycle time", "Revenue", "Risk/Compliance", "Capacity")},
            {"name": "Baseline", "type": "singleLineText"},
            {"name": "Current", "type": "singleLineText"},
            {"name": "Quantified Impact", "type": "singleLineText"},
            {"name": "Source of Truth", "type": "multilineText"},
            {"name": "Audience", "type": "singleSelect",
             "options": SELECT("CFO", "COO", "CIO", "Procurement", "BU Leader", "Ops Lead")},
            {"name": "Status", "type": "singleSelect",
             "options": SELECT("Draft", "Reviewed", "Customer-validated", "Stale")},
            {"name": "Validated By", "type": "singleLineText"},
            {"name": "Date Validated", "type": "date", "options": {"dateFormat": {"name": "iso"}}},
        ],
    },
    {
        "name": "Account Plays",
        "fields": [
            {"name": "Name", "type": "singleLineText"},
            {"name": "Account", "type": "multipleRecordLinks", "options": {"linkedTableName": "Accounts"}},
            {"name": "Play", "type": "multipleRecordLinks", "options": {"linkedTableName": "Plays"}},
            {"name": "Owner", "type": "multipleRecordLinks", "options": {"linkedTableName": "CSMs"}},
            {"name": "Partner Engaged", "type": "multipleSelects",
             "options": SELECT("Professional Services", "Security & Risk", "Product", "Sales", "Renewals", "Value Validation", "Support")},
            {"name": "Status", "type": "singleSelect",
             "options": SELECT("Not started", "In flight", "Blocked", "Done — DoD met", "Abandoned")},
            {"name": "Start Date", "type": "date", "options": {"dateFormat": {"name": "iso"}}},
            {"name": "Target Date", "type": "date", "options": {"dateFormat": {"name": "iso"}}},
            {"name": "Completed Date", "type": "date", "options": {"dateFormat": {"name": "iso"}}},
            {"name": "Outcome", "type": "multilineText"},
        ],
    },
]

# csv file -> (table, primary field, {csv column: (link table, key)}, multi-select columns)
LOADS = [
    ("csms.csv", "CSMs", "Name", {}, {"Strength Profile"}),
    ("plays.csv", "Plays", "Play", {}, {"Partner Leads"}),
    ("accounts.csv", "Accounts", "Account", {"CSM": "CSMs"}, set()),
    ("diagnostics.csv", "Diagnostics", None, {"Account": "Accounts", "Run By": "CSMs"}, set()),
    ("stakeholders.csv", "Stakeholders", "Name", {"Account": "Accounts"}, set()),
    ("signals.csv", "Signals", "Signal", {"Account": "Accounts"}, set()),
    ("value-stories.csv", "Value Stories", "Value Story", {"Account": "Accounts"}, set()),
    ("account-plays.csv", "Account Plays", None, {"Account": "Accounts", "Play": "Plays", "Owner": "CSMs"}, {"Partner Engaged"}),
]

NUMERIC = {"ARR", "Seats", "Quarters to Renewal", "Tenure (months)", "Plays Authored",
           "Weight", "Typical Duration (wks)", "Sponsorship", "Governance", "Adoption",
           "Value Evidence", "Builder Depth", "Executive Presence", "Domain"}

# Columns present in a CSV but not sent to the API. "Paired With" is a self-referential link
# that can't resolve during a single-pass create — set it in the UI (2 rows on seed data).
SKIP = {"Paired With"}


# ---------------------------------------------------------------- http

def call(method, path, token, body=None):
    req = urllib.request.Request(
        f"{API}{path}", method=method,
        data=json.dumps(body).encode() if body is not None else None,
        headers={"Authorization": f"Bearer {token}", "Content-Type": "application/json"},
    )
    for attempt in range(5):
        try:
            with urllib.request.urlopen(req) as r:
                return json.loads(r.read())
        except urllib.error.HTTPError as e:
            detail = e.read().decode()
            if e.code == 429 and attempt < 4:          # rate limited — 5 req/sec per base
                time.sleep(2 ** attempt)
                continue
            sys.exit(f"\n  HTTP {e.code} on {method} {path}\n  {detail}\n")
    return None


def chunks(seq, n):
    for i in range(0, len(seq), n):
        yield seq[i:i + n]


# ---------------------------------------------------------------- load

def read_csv(name):
    with open(DATA / name, newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def build_fields(row, links, multis, index):
    """Turn a CSV row into an Airtable fields payload."""
    out = {}
    for col, raw in row.items():
        if col in SKIP:
            continue
        val = (raw or "").strip()
        if not val:
            continue
        if col in links:
            target = links[col]
            ids = []
            for part in [p.strip() for p in val.split(",") if p.strip()]:
                rid = index.get(target, {}).get(part)
                if not rid:
                    raise KeyError(f"'{part}' not found in {target} (column '{col}')")
                ids.append(rid)
            out[col] = ids
        elif col in multis:
            out[col] = [p.strip() for p in val.split(",") if p.strip()]
        elif col in NUMERIC:
            out[col] = float(val) if "." in val else int(val)
        else:
            out[col] = val
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="validate CSVs and links, create nothing")
    ap.add_argument("--base-id", help="load into an existing base instead of creating one")
    args = ap.parse_args()

    # dry run needs no credentials
    if args.dry_run:
        print("Dry run — validating CSVs\n")
        index, ok = {}, True
        for fname, table, primary, links, multis in LOADS:
            rows = read_csv(fname)
            index[table] = {}
            for i, row in enumerate(rows):
                key = row.get(primary) if primary else None
                if key:
                    index[table][key.strip()] = f"rec_fake_{table}_{i}"
            for i, row in enumerate(rows):
                try:
                    build_fields(row, links, multis, index)
                except KeyError as e:
                    print(f"  ✗ {fname} row {i + 2}: {e}")
                    ok = False
            print(f"  {'✓' if ok else '✗'} {fname:22} {len(rows):>3} rows → {table}")
        print("\nAll link references resolve." if ok else "\nFix the unresolved links above.")
        return 0 if ok else 1

    token = os.environ.get("AIRTABLE_PAT")
    if not token:
        sys.exit("AIRTABLE_PAT is not set. Create a personal access token with "
                 "schema.bases:write and data.records:write.")

    base_id = args.base_id
    if not base_id:
        workspace = os.environ.get("AIRTABLE_WORKSPACE_ID")
        if not workspace:
            sys.exit("AIRTABLE_WORKSPACE_ID is not set (find it in the workspace URL: /wsp.../).")
        print("Creating base 'HTCS Transformation OS'...")
        # linkedTableName is our own convenience key — the API wants linkedTableId, which
        # doesn't exist yet at creation time. Create tables bare, then add links.
        bare = []
        deferred = []
        for t in TABLES:
            plain = [f for f in t["fields"] if f["type"] != "multipleRecordLinks"]
            for f in t["fields"]:
                if f["type"] == "multipleRecordLinks":
                    deferred.append((t["name"], f))
            bare.append({"name": t["name"], "fields": plain})
        res = call("POST", "/meta/bases", token,
                   {"name": "HTCS Transformation OS", "workspaceId": workspace, "tables": bare})
        base_id = res["id"]
        print(f"  base {base_id}")

        table_ids = {t["name"]: t["id"] for t in res["tables"]}
        print("Adding linked-record fields...")
        for table_name, field in deferred:
            payload = {
                "name": field["name"], "type": "multipleRecordLinks",
                "options": {"linkedTableId": table_ids[field["options"]["linkedTableName"]]},
            }
            call("POST", f"/meta/bases/{base_id}/tables/{table_ids[table_name]}/fields", token, payload)
            print(f"  {table_name}.{field['name']}")

    print("\nLoading records...")
    index = {}
    for fname, table, primary, links, multis in LOADS:
        rows = read_csv(fname)
        payload = []
        for i, row in enumerate(rows):
            try:
                payload.append({"fields": build_fields(row, links, multis, index)})
            except KeyError as e:
                sys.exit(f"  {fname} row {i + 2}: {e}")

        created = []
        for batch in chunks(payload, 10):                 # API caps at 10 records per request
            res = call("POST", f"/{base_id}/{urllib.parse.quote(table)}", token,
                       {"records": batch, "typecast": True})
            created.extend(res["records"])
            time.sleep(0.25)                              # stay under 5 req/sec

        index[table] = {}
        if primary:
            for row, rec in zip(rows, created):
                index[table][row[primary].strip()] = rec["id"]
        print(f"  ✓ {table:16} {len(created):>3} records")

    print(f"\nDone — https://airtable.com/{base_id}")
    print("\nStill to do in the UI (not creatable via API):")
    print("  · formulas, lookups and rollups   → airtable-build/schema.md")
    print("  · CSMs 'Paired With' self-links    (2 rows: Marcus ↔ Ben)")
    print("  · 3 AI fields + 1 agent           → airtable-build/ai-components.md")
    print("  · 3 automations                   → airtable-build/ai-components.md")
    print("  · 3 interfaces                    → airtable-build/interfaces.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
