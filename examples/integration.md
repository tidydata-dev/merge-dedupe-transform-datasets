# Run it automatically after any scraper

1. Open your scraper (e.g. a Google Maps, Amazon or job scraper) in Apify Console → **Integrations** → **Connect Actor**.
2. Choose **Merge, Deduplicate & Transform Datasets** (`tidydata/merge-dedupe-datasets`).
3. Input:
   ```json
   {
     "datasetIds": ["{{resource.defaultDatasetId}}"],
     "dedupeFields": ["url"],
     "onlyNew": true,
     "onlyNewMemoryName": "my-project",
     "exportFormats": ["csv"]
   }
   ```
4. Schedule the scraper. After every run you get a CSV with only the new items (in the Merge run's **Output** tab), ready for Google Sheets, a CRM or an email alert.
