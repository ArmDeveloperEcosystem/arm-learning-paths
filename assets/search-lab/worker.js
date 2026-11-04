import { createEngine } from './engine.mjs';
let search;
self.onmessage = async ({ data }) => {
  const { id, action, input, url } = data;
  try {
    if (action === 'init') {
      const start = performance.now();
      const response = await fetch(url);
      if (!response.ok) throw Error(`Index request failed (${response.status}).`);
      const text = await response.text();
      const index = JSON.parse(text);
      search = createEngine(index.records);
      self.postMessage({ id, result: { count: index.records.length, bytes: new TextEncoder().encode(text).length, loadMs: performance.now() - start, categories: [...new Set(index.records.map(r => r.category).filter(Boolean))].sort() } });
    } else {
      if (!search) throw Error('Search index is not ready.');
      const start = performance.now();
      self.postMessage({ id, result: { ...search(input), searchMs: performance.now() - start } });
    }
  } catch (error) { self.postMessage({ id, error: error.message }); }
};
