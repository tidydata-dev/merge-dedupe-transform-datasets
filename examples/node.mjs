// npm i apify-client  ·  APIFY_TOKEN=... node examples/node.mjs
import { ApifyClient } from 'apify-client';

const client = new ApifyClient({ token: process.env.APIFY_TOKEN });
const run = await client.actor('tidydata/merge-dedupe-datasets').call({
    fileUrls: [{ url: 'https://docs.google.com/spreadsheets/d/1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms/edit#gid=0' }],
    filters: ['Major in English, Math'],
    sortBy: ['Student Name asc'],
    exportFormats: ['json'],
});
const { items } = await client.dataset(run.defaultDatasetId).listItems();
console.log(items.length, 'rows', items[0]);
