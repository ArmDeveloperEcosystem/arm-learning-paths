# Search lab

`/search/` searches a static JSON index in a browser worker. Queries are stored in the page URL but are not sent to a search service. The page requests `noindex,nofollow` and is excluded from the sitemap; it remains publicly accessible.

## Shared layout changes

The `page-head` block in the theme's `baseof.html` lets the search layout load its scoped stylesheet. The `browser_search` front-matter flag tells `footer/script-includes.html` to skip legacy list-filter scripts on this page. Existing search entry points are unchanged.

## Index and ranking

`layouts/search-lab/list.html` generates the index and fingerprinted assets on each build. It includes Learning Path landing pages and install-guide entry points, with multi-part guides represented by their entry point. Draft, future, and expired content is excluded, including content with hidden ancestors, even with `--buildDrafts`.

`assets/search-lab/engine.mjs` uses weighted BM25 keyword scoring: title > description/authors > taxonomy/objectives/extra search terms/prerequisites > summary/FAQ text. Full tutorial steps and guide body text are not indexed. FAQ text comes from `generated_summary_faq.faqs`. Identifiers such as `llama.cpp` retain punctuation.

Relevance is the default for the page and agent tool. Results matching every significant query word exactly come first, followed by complete matches using word expansion, then partial matches. Common words such as “and” are ignored. Within each group, results sort by score regardless of content type. Scores express ranking, not confidence.

Alphabetic prefixes of at least three letters match token beginnings (`grav` matches `Graviton`). If a word has no exact token or prefix completion, words of at least five letters allow one insertion, deletion, substitution, or adjacent letter swap (`dokcer` matches `Docker`). Typo matching applies only to alphabetic tokens of at least five letters; identifiers with punctuation or digits are not corrected. Expanded matches receive lower weights. There is no arbitrary substring matching, stemming, synonym expansion, or embedding search.

Newest-first remains available and sorts by date instead of match completeness: the latest page date across a Learning Path, or the entry-page date for an install guide. Missing dates sort last; ties use score. Sorting and content filters apply before pagination. Existing URLs with `sort=updated` retain newest-first sorting.

`assets/search-lab/worker.js` loads and prepares the index once per page load. The WebMCP adapter and tester in `assets/search-lab/app.js` invoke the same callback without changing the human's current search. The tester works without native WebMCP support; it does not prove an agent connection. See the [CLI WebMCP demo](WEBMCP_DEMO.md) for native tool invocation.

## Verify

Run from the repository root:

```sh
node --test tools/search-lab/engine.test.mjs tools/search-lab/app.test.mjs
hugo --destination /private/tmp/arm-search-lab-build
node tools/search-lab/check-index.mjs /private/tmp/arm-search-lab-build
```

The index checker expects unminified HTML. To check draft exclusion, also build with `--buildDrafts` into a separate directory and compare index record IDs. Before rollout, check mobile widths, light/dark themes, keyboard navigation, slow loading, and browsers with and without native WebMCP support.
