# Merge, deduplicate & transform datasets — examples

Recipes for the hosted **[Merge, Deduplicate & Transform Datasets](https://apify.com/tidydata/merge-dedupe-datasets?fpr=wtg6qt)** Actor on Apify: combine the results of your scrapers (or CSV, Excel, JSON files and Google Sheets), **remove or merge duplicates**, **filter**, **sort**, add **computed columns**, keep **only new rows since the last run**, and export **CSV / Excel / JSON**. **$0.25 per 1,000 output rows**; duplicates and filtered rows are free.

## Recipes

| You want to… | Input |
|---|---|
| Combine daily Google Maps runs without duplicates | `datasetIds: [...]`, `dedupeFields: ["placeId"]` |
| Get only **new** items each day | `onlyNew: true`, `dedupeFields: ["url"]`, run it on a schedule |
| Same page written differently (utm, www, https) | `dedupeFields: ["url"]`, `normalizeKeys: true` |
| One complete row per lead from two sources | `dedupeFields: ["website"]`, `keep: "merge"`, `normalizeKeys: true` |
| JSON → CSV / Excel | `fileUrls: [{"url": "…/data.json"}]`, `exportFormats: ["csv", "xlsx"]` |
| Excel / Google Sheet → JSON | `fileUrls: [{"url": "https://docs.google.com/spreadsheets/d/…"}]`, `exportFormats: ["json"]` |
| Domain column + numeric price + sort | `computedFields: ["domain = {website\|domain}", "price = {price\|number}"]`, `sortBy: ["price desc"]` |
| One row per email | `unwindField: "emails"` |
| Filter | `filters: ["country in ES, FR", "rating >= 4.5", "url regex /product/"]`, `filterMode: "all"` |

## Python

```python
import os
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
run = client.actor("tidydata/merge-dedupe-datasets").call(run_input={
    "datasetIds": ["<RUN_1_DATASET_ID>", "<RUN_2_DATASET_ID>"],
    "fileUrls": [{"url": "https://example.com/extra-leads.csv"}],
    "dedupeFields": ["website"],
    "normalizeKeys": True,
    "keep": "merge",
    "filters": ["email exists"],
    "exportFormats": ["csv", "xlsx"],
})
store = client.key_value_store(run["defaultKeyValueStoreId"])
csv_data = store.get_record("merged.csv")["value"]
open("merged.csv", "wb").write(csv_data if isinstance(csv_data, bytes) else csv_data.encode("utf-8"))
print("rows:", client.dataset(run["defaultDatasetId"]).get()["itemCount"])
```

More: [`examples/only_new_items.py`](examples/only_new_items.py) · [`examples/node.mjs`](examples/node.mjs) · [`examples/integration.md`](examples/integration.md) (run it automatically after any scraper)

## Related

- [Phone Number Validator](https://apify.com/tidydata/phone-number-validator?fpr=wtg6qt) and [Email Validator](https://apify.com/tidydata/email-validator?fpr=wtg6qt) — clean contact columns.
- [Google Sheets Export & Import](https://apify.com/tidydata/google-sheets-export-import?fpr=wtg6qt) — append results to a sheet without duplicates.

Examples are MIT-licensed.

---
<sub>Links to apify.com include our affiliate ID: if you start a paid Apify plan through them, Apify pays TidyData a commission at no extra cost to you.</sub>
