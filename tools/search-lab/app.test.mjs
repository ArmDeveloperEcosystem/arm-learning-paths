import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';
import { createEngine } from '../../assets/search-lab/engine.mjs';

const source = fs.readFileSync(new URL('../../assets/search-lab/app.js', import.meta.url), 'utf8');
const flush = () => new Promise(resolve => setImmediate(resolve));

// Run the actual app with a small DOM and controllable worker to exercise failure paths.
async function startApp({ startupFailure = false, initFailure = false, total = 472, query = '', filters = '', records } = {}) {
  const elements = new Map();
  const element = id => {
    if (!elements.has(id)) elements.set(id, {
      value: id === 'sort' ? 'relevance' : '', textContent: '', hidden: false, children: [],
      focus() { this.focused = true; },
      append(...children) { this.children.push(...children); },
      replaceChildren(...children) { this.children = children; }
    });
    return elements.get(id);
  };
  const search = records && createEngine(records);
  let worker, tool;
  const requests = [], urls = [];
  const context = vm.createContext({
    document: {
      getElementById: element, createElement: () => element(Symbol()),
      querySelector: () => ({ dataset: { worker: '/worker.js', index: '/index.json' }, querySelectorAll: () => [] }),
      modelContext: { registerTool(value) { tool = value; } }
    },
    navigator: {},
    Worker: class {
      constructor() {
        if (startupFailure) throw Error('Worker blocked');
        worker = this;
      }
      terminate() { this.terminated = true; }
      postMessage(message) {
        requests.push(message);
        if (this.throwOnPost) throw Error('Cannot post message');
        if (this.pause) return;
        queueMicrotask(() => {
          if (message.action === 'init' && initFailure) return this.onerror();
          const result = message.action === 'init'
            ? { categories: ['cross-platform'], count: total, bytes: 1, loadMs: 1 }
            : { total, searchMs: 1, results: Array.from({ length: Math.max(0, Math.min(total - (message.input.offset || 0), message.input.limit || 10)) }, (_, i) => ({
              title: `Result ${i + (message.input.offset || 0)}`, url: `/result/${i + (message.input.offset || 0)}/`, type: 'learning-path'
            })) };
          this.onmessage({ data: { id: message.id, result: search && message.action === 'search' ? { ...search(message.input), searchMs: 1 } : result } });
        });
      }
    },
    URLSearchParams, history: { replaceState(_state, _title, url) { urls.push(url); } },
    location: { search: `?q=${encodeURIComponent(query)}&${filters}`, pathname: '/search/', hash: '' },
    performance, setTimeout, clearTimeout, queueMicrotask
  });
  await vm.runInContext(`(async () => {\n${source}\n})()`, context);
  await flush();
  return { element, worker, tool, requests, urls };
}

test('worker startup failures display an error and tool calls settle', { timeout: 1000 }, async () => {
  for (const options of [{ startupFailure: true }, { initFailure: true }]) {
    const { element, tool } = await startApp(options);
    assert.match(element('status').textContent, /Reload/);
    assert.equal((await tool.execute({ query: 'gcc' })).isError, true);
    element('search-form').onsubmit({ preventDefault() {} });
    await flush();
    assert.match(element('status').textContent, /Reload/);
  }
});

test('worker errors reject outstanding and future searches', { timeout: 1000 }, async () => {
  for (const event of ['onerror', 'onmessageerror']) {
    const { element, worker, tool } = await startApp();
    worker.pause = true;
    const outstanding = tool.execute({ query: 'gcc' });
    await flush();
    worker[event]();
    assert.equal((await outstanding).isError, true);
    assert.equal((await tool.execute({ query: 'docker' })).isError, true);
    assert.equal(worker.terminated, true);
    assert.equal(element('more').hidden, true);
    assert.match(element('status').textContent, /Reload/);
  }
});

test('postMessage failures settle current and future searches', { timeout: 1000 }, async () => {
  const { worker, tool } = await startApp();
  worker.throwOnPost = true;
  assert.equal((await tool.execute({ query: 'gcc' })).isError, true);
  assert.equal((await tool.execute({ query: 'gcc' })).isError, true);
});

test('Show more reaches every result beyond 100 without duplicates and filters reset pagination', async () => {
  const { element } = await startApp({ total: 123 });
  element('search-form').onsubmit({ preventDefault() {} });
  await flush();
  assert.match(element('status').textContent, /123 results.*Showing 10 of 123/);
  for (let i = 0; i < 12; i++) {
    assert.equal(element('more').hidden, false);
    element('more').onclick();
    await flush();
  }
  assert.equal(element('results').children.length, 123);
  const titles = element('results').children.map(li => li.children[1].children[0].textContent);
  assert.equal(new Set(titles).size, 123);
  assert.match(element('status').textContent, /Showing 123 of 123/);
  assert.equal(element('more').hidden, true);
  element('type').value = 'install-guide';
  element('type').onchange();
  await flush();
  assert.equal(element('results').children.length, 10);
});

test('blank searches browse all content and respect type, category, and restored URL filters', async () => {
  const records = [
    { id: '/guide/', title: 'Docker guide', type: 'install-guide', category: '' },
    { id: '/path/', title: 'Docker path', type: 'learning-path', category: 'cross-platform' },
    { id: '/other/', title: 'Other path', type: 'learning-path', category: 'servers-and-cloud-computing' }
  ];
  const { element } = await startApp({ records });
  element('search-form').onsubmit({ preventDefault() {} });
  await flush();
  assert.match(element('status').textContent, /3 results.*newest first/);
  for (const [type, category, total] of [['install-guide', '', 1], ['learning-path', '', 2], ['', 'cross-platform', 1]]) {
    element('type').value = type;
    element('category').value = category;
    element('type').onchange();
    await flush();
    assert.equal(element('results').children.length, total);
  }
  element('query').value = 'unfindable';
  element('search-form').onsubmit({ preventDefault() {} });
  await flush();
  assert.equal(element('results').children.length, 0);
  element('query').value = '   ';
  element('search-form').onsubmit({ preventDefault() {} });
  await flush();
  assert.equal(element('results').children.length, 1);
  const restored = await startApp({ records, filters: 'category=cross-platform' });
  assert.equal(restored.element('results').children.length, 0);
  restored.element('search-form').onsubmit({ preventDefault() {} });
  await flush();
  assert.equal(restored.element('results').children.length, 1);
});

test('install guides clear and disable categories on selection and URL restoration', async () => {
  for (const filters of ['category=cross-platform', 'type=install-guide&category=cross-platform']) {
    const { element, requests, urls } = await startApp({ query: 'Docker', filters });
    element('type').value = 'install-guide';
    element('type').onchange();
    await flush();
    assert.equal(element('category').disabled, true);
    assert.equal(element('category').value, '');
    assert.equal(requests.at(-1).input.category, '');
    assert.equal(new URLSearchParams(urls.at(-1).split('?')[1]).has('category'), false);
    if (filters.startsWith('type=')) assert.equal(requests.find(r => r.action === 'search').input.category, '');
    element('type').value = 'learning-path';
    element('type').onchange();
    await flush();
    assert.equal(element('category').disabled, false);
    element('category').value = 'cross-platform';
    element('category').onchange();
    await flush();
    assert.equal(requests.at(-1).input.category, 'cross-platform');
  }
});

test('initial blank page and filter changes wait for submission; clearing live search waits again', async () => {
  const { element, requests } = await startApp();
  assert.equal(element('results').children.length, 0);
  assert.equal(element('more').hidden, true);
  assert.equal(requests.filter(r => r.action === 'search').length, 0);
  element('type').value = 'install-guide';
  element('type').onchange();
  await flush();
  assert.equal(requests.filter(r => r.action === 'search').length, 0);
  element('search-form').onsubmit({ preventDefault() {} });
  await flush();
  assert.equal(element('results').children.length, 10);
  assert.equal(requests.at(-1).input.query, '');
  assert.equal(requests.at(-1).input.type, 'install-guide');
  element('query').value = 'Docker';
  element('query').oninput();
  await new Promise(resolve => setTimeout(resolve, 150));
  assert.equal(requests.at(-1).input.query, 'Docker');
  const count = requests.length;
  element('query').value = '';
  element('query').oninput();
  await new Promise(resolve => setTimeout(resolve, 150));
  assert.equal(element('results').children.length, 0);
  assert.equal(requests.length, count);
});

test('inline clear is available only for an active empty search and returns to no results', async () => {
  const { element, requests, worker } = await startApp({ filters: 'type=install-guide' });
  assert.equal(element('clear-blank-search').hidden, true);
  element('search-form').onsubmit({ preventDefault() {} });
  await flush();
  assert.equal(element('clear-blank-search').hidden, false);
  assert.equal(element('results').children.length, 10);
  worker.pause = true;
  element('more').onclick();
  await flush();
  const pendingId = requests.at(-1).id;
  element('clear-blank-search').onclick();
  worker.onmessage({ data: { id: pendingId, result: { total: 1, searchMs: 1, results: [{ title: 'Stale result', url: '/stale/' }] } } });
  await flush();
  assert.equal(element('results').children.length, 0);
  assert.equal(element('more').hidden, true);
  assert.equal(element('clear-blank-search').hidden, true);
  assert.equal(element('query').focused, true);
  assert.equal(element('type').value, 'install-guide');
  worker.pause = false;
  element('query').value = 'Docker';
  element('search-form').onsubmit({ preventDefault() {} });
  await flush();
  assert.equal(element('clear-blank-search').hidden, true);
});
