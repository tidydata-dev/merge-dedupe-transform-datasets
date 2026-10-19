"""Daily job: merge today's scraper run into a CSV of ONLY the items not seen before. pip install apify-client"""
import os, sys
from apify_client import ApifyClient

client = ApifyClient(os.environ["APIFY_TOKEN"])
todays_dataset = sys.argv[1]  # e.g. the defaultDatasetId of your scraper's last run
run = client.actor("tidydata/merge-dedupe-datasets").call(run_input={
    "datasetIds": [todays_dataset],
    "dedupeFields": ["url"],
    "normalizeKeys": True,
    "onlyNew": True,
    "onlyNewMemoryName": "my-daily-listings",   # one memory per project
    "exportFormats": ["csv"],
})
items = client.dataset(run["defaultDatasetId"]).list_items().items
print(f"{len(items)} new items today")
