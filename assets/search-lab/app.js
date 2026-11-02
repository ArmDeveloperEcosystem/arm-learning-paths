const $ = id => document.getElementById(id);
const main = document.querySelector('main[data-index]');
let worker, workerFailure;
let nextId = 0, generation = 0, limit = 10;
const pending = new Map();
function failWorker() {
  workerFailure = Error('Search is unavailable. Reload the page to retry.');
  worker?.terminate();
  ++generation;
  for (const request of pending.values()) request.reject(workerFailure);
  pending.clear();
  $('more').hidden = true;
  $('search-diagnostics').hidden = true;
  $('status').textContent = workerFailure.message;
}
try {
  worker = new Worker(main.dataset.worker, { type: 'module' });
  worker.onmessage = ({ data }) => {
    const request = pending.get(data.id);
    if (!request) return;
    pending.delete(data.id);
    data.error ? request.reject(Error(data.error)) : request.resolve(data.result);
  };
  worker.onerror = failWorker;
  worker.onmessageerror = failWorker;
} catch { failWorker(); }
function call(action, input) {
  if (workerFailure) return Promise.reject(workerFailure);
  return new Promise((resolve, reject) => {
    const id = ++nextId;
    pending.set(id, { resolve, reject });
    try { worker.postMessage({ id, action, input, url: main.dataset.index }); }
    catch { failWorker(); }
  });
}
const ready = call('init');
const tool = {
  name: 'search_arm_content',
  description: 'Find Arm Learning Paths and install guides by keyword or author name, with word prefixes and limited typo tolerance. Relevance defaults to complete query matches first. Returns source URLs and metadata excerpts; use these sources to read the full instructions. Scores indicate keyword relevance, not confidence.',
  inputSchema: { type: 'object', properties: {
    query: { type: 'string', minLength: 1, maxLength: 300 },
    type: { type: 'string', enum: ['', 'learning-path', 'install-guide'], default: '' },
    category: { type: 'string', description: 'Learning Path category slug, such as servers-and-cloud-computing.' },
    sort: { type: 'string', enum: ['relevance', 'updated'], default: 'relevance' },
    limit: { type: 'integer', minimum: 1, maximum: 100, default: 10 }
  }, required: ['query'], additionalProperties: false },
  annotations: { readOnlyHint: true },
  async execute(input, { signal } = {}) {
    try {
      signal?.throwIfAborted();
      await ready;
      signal?.throwIfAborted();
      const result = await call('search', input);
      signal?.throwIfAborted();
      return { content: [{ type: 'text', text: JSON.stringify(result) }], structuredContent: result };
    } catch (error) {
      if (signal?.aborted) throw error;
      return { isError: true, content: [{ type: 'text', text: error.message }] };
    }
  }
};
// The tester and the registered tool invoke precisely the same callback.
$('run-tool').onclick = async () => {
  try { $('tool-output').textContent = JSON.stringify(await tool.execute(JSON.parse($('tool-input').value)), null, 2); }
  catch (error) { $('tool-output').textContent = error.message; }
};
async function register() {
  const context = document.modelContext || navigator.modelContext;
  if (!context?.registerTool) {
    $('webmcp').textContent = 'Native WebMCP is unavailable in this browser. Use the tool tester below.';
    return;
  }
  try {
    await context.registerTool(tool);
    $('webmcp').textContent = 'WebMCP registered: search_arm_content';
  } catch (error) { $('webmcp').textContent = `WebMCP registration failed: ${error.message}. The tester still works.`; }
}
register();
async function render() {
  const current = ++generation;
  const query = $('query').value.trim();
  const params = new URLSearchParams();
  if (query) params.set('q', query);
  if ($('type').value) params.set('type', $('type').value);
  if ($('category').value) params.set('category', $('category').value);
  params.set('sort', $('sort').value);
  history.replaceState(null, '', `${location.pathname}${params.size ? '?' + params : ''}${location.hash}`);
  $('results').replaceChildren();
  $('more').hidden = true;
  $('search-diagnostics').hidden = true;
  if (workerFailure) { $('status').textContent = workerFailure.message; return; }
  if (!query) { $('status').textContent = ''; return; }
  $('status').textContent = 'Searching…';
  const start = performance.now();
  try {
    await ready;
    const result = await call('search', { query, type: $('type').value, category: $('category').value, sort: $('sort').value, limit });
    if (current !== generation) return;
    $('status').textContent = `${result.total} result${result.total === 1 ? '' : 's'} for “${query}”`;
    $('performance').textContent = `Last search: ${result.searchMs.toFixed(1)} ms engine · ${(performance.now() - start).toFixed(1)} ms response`;
    $('search-diagnostics').hidden = false;
    if (!result.total) $('status').textContent += '. Try fewer words or remove a filter.';
    if (result.total > 100) $('status').textContent += `. Showing ${result.results.length} of the first 100 results. Narrow your search to find other matches.`;
    for (const record of result.results) {
      const li = document.createElement('li'); li.className = 'search-result-card';
      const a = document.createElement('a'); a.href = record.url; a.textContent = record.title;
      const h = document.createElement('h3'); h.className = 'result-title'; h.append(a);
      const meta = document.createElement('p'); meta.className = 'result-meta';
      const badge = document.createElement('span'); badge.className = 'result-type';
      badge.textContent = record.type === 'learning-path' ? 'Learning Path' : 'Install guide'; meta.append(badge);
      if (record.category) { const category = document.createElement('span'); category.textContent = categoryLabel(record.category); meta.append(category); }
      const p = document.createElement('p'); p.className = 'result-description'; p.textContent = record.description || record.summary;
      const footer = document.createElement('div'); footer.className = 'result-footer';
      if (record.authors?.length) { const authors = document.createElement('p'); authors.textContent = 'By ' + record.authors.join(', '); footer.append(authors); }
      const updated = document.createElement('p');
      if (record.lastUpdated) {
        const time = document.createElement('time'); time.dateTime = record.lastUpdated;
        time.textContent = new Date(record.lastUpdated + 'T00:00:00Z').toLocaleDateString('en-GB', { day: 'numeric', month: 'short', year: 'numeric', timeZone: 'UTC' });
        updated.append('Last updated: ', time);
      } else { updated.textContent = 'Last updated: unavailable'; }
      footer.append(updated); li.append(meta, h, p, footer); $('results').append(li);
    }
    $('more').hidden = result.total <= limit || limit >= 100;
  } catch (error) { if (current === generation) $('status').textContent = error.message; }
}
function categoryLabel(slug) {
  return slug.split('-').map((word, index) => index && ['and'].includes(word) ? word : word[0].toUpperCase() + word.slice(1)).join(' ');
}
for (const button of main.querySelectorAll('[data-query]')) button.onclick = () => {
  $('query').value = button.dataset.query; $('type').value = ''; $('category').value = ''; limit = 10; render();
};
let timer;
$('query').oninput = () => { clearTimeout(timer); timer = setTimeout(() => { limit = 10; render(); }, 120); };
$('search-form').onsubmit = event => { event.preventDefault(); clearTimeout(timer); limit = 10; render(); };
for (const id of ['type', 'category', 'sort']) $(id).onchange = () => { limit = 10; render(); };
$('more').onclick = () => { limit = Math.min(100, limit + 10); render(); };
const params = new URLSearchParams(location.search);
$('query').value = (params.get('q') || '').slice(0, 300);
if (['updated', 'relevance'].includes(params.get('sort'))) $('sort').value = params.get('sort');
if (['learning-path', 'install-guide'].includes(params.get('type'))) $('type').value = params.get('type');
try {
  const info = await ready;
  for (const category of info.categories) { const option = document.createElement('option'); option.value = category; option.textContent = categoryLabel(category); $('category').append(option); }
  if (info.categories.includes(params.get('category'))) $('category').value = params.get('category');
  $('metrics').textContent = `${info.count} documents · ${(info.bytes / 1024).toFixed(0)} KB index (uncompressed) · ${info.loadMs.toFixed(0)} ms to download and prepare`;
  render();
} catch (error) { $('status').textContent = `Unable to load search: ${error.message} Reload to retry.`; }
