# Scripts

## `seed_airtable.py`

Creates the **HTCS Transformation OS** base and loads all 84 seed records via the Airtable
Web API. Standard library only — no dependencies, no install.

```bash
# validate the CSVs and every linked-record reference — no credentials needed
python3 scripts/seed_airtable.py --dry-run

# create the base and load it
export AIRTABLE_PAT=pat...              # scopes: schema.bases:write, data.records:write
export AIRTABLE_WORKSPACE_ID=wsp...     # from the workspace URL
python3 scripts/seed_airtable.py

# or load into a base that already exists
python3 scripts/seed_airtable.py --base-id appXXXXXXXX
```

**Get a PAT:** airtable.com/create/tokens → scopes `schema.bases:write` and
`data.records:write` → grant access to the workspace.
**Workspace ID:** the `wsp...` segment in the workspace URL.

### What it does

1. Creates the base with 8 tables and correct field types (ratings, currency, selects, dates).
2. Adds linked-record fields in a second pass — the API needs a `linkedTableId`, which doesn't
   exist until the tables do.
3. Loads records in dependency order, keeping a name→record-ID map so links resolve.
4. Batches at 10 records per request and backs off on 429s.

### What it does *not* do

Formula, lookup and rollup fields, AI fields, automations and interfaces **cannot be created
through the API**. Add them in the UI:

| | Where |
|---|---|
| Formulas, lookups, rollups | [`../airtable-build/schema.md`](../airtable-build/schema.md) |
| 3 AI fields + 1 agent | [`../airtable-build/ai-components.md`](../airtable-build/ai-components.md) |
| 3 automations | [`../airtable-build/ai-components.md`](../airtable-build/ai-components.md#automations) |
| 3 interfaces | [`../airtable-build/interfaces.md`](../airtable-build/interfaces.md) |

The script prints this list when it finishes.

### Notes

- `Diagnostics` and `Account Plays` have empty primary fields after loading — both are meant to
  be formulas (see [`schema.md`](../airtable-build/schema.md)). Set those first in the UI.
- Uses `typecast: true`, so select options are created on the fly if a CSV value doesn't match
  a predefined choice. Convenient, but it means a typo becomes a new select option rather than
  an error — worth a glance at the select fields after loading.
- Re-running against the same base **duplicates records**. It has no idempotency check.

### Is the script necessary?

No. Manual CSV import per
[`../airtable-build/build-checklist.md`](../airtable-build/build-checklist.md) takes about 45
minutes and is the reasonable path if you're building this once. The script exists because
`--dry-run` catches data errors before they're in the product, and because rebuilding from
scratch after a schema change takes seconds instead of a re-import.
