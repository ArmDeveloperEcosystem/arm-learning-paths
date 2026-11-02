import test from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import vm from 'node:vm';

const source = fs.readFileSync(new URL('../../assets/search-lab/app.js', import.meta.url), 'utf8');
const flush = () => new Promise(resolve => setImmediate(resolve));

// Run the actual app with a small DOM and controllable worker to exercise failure paths.
async function startApp({ startupFailure = false, initFailure = false, total = 472, query = '' } = {}) {
  const elements = new Map();
  const element = id => {
    if (!elements.has(id)) elements.set(id, {
      value: '', textContent: '', hidden: false, children: [],
      append(...children) { this.children.push(...children); },
      replaceChildren(...children) { this.children = children; }
    });
    return elements.get(id);
  };
  let worker, tool;
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
        if (this.throwOnPost) throw Error('Cannot post message');
        if (this.pause) return;
        queueMicrotask(() => {
          if (message.action === 'init' && initFailure) return this.onerror();
          const result = message.action === 'init'
            ? { categories: [], count: total, bytes: 1, loadMs: 1 }
            : { total, searchMs: 1, results: Array.from({ length: Math.min(total, message.input.limit || 10) }, (_, i) => ({
              title: `Result ${i}`, url: `/result/${i}/`, type: 'learning-path'
            })) };
          this.onmessage({ data: { id: message.id, result } });
        });
      }
    },
    URLSearchParams, history: { replaceState() {} },
    location: { search: query ? `?q=${encodeURIComponent(query)}` : '', pathname: '/search/', hash: '' },
    performance, setTimeout, clearTimeout, queueMicrotask
  });
  await vm.runInContext(`(async () => {\n${source}\n})()`, context);
  await flush();
  return { element, worker, tool };
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

test('searches above the cap explain the limit before and after Show more', async () => {
  const { element } = await startApp({ query: 'Linux' });
  assert.match(element('status').textContent, /472 results.*Showing 10 of the first 100 results.*Narrow/);
  assert.equal(element('more').hidden, false);
  for (let i = 0; i < 9; i++) {
    element('more').onclick();
    await flush();
  }
  assert.equal(element('results').children.length, 100);
  assert.match(element('status').textContent, /Showing 100 of the first 100 results/);
  assert.equal(element('more').hidden, true);
});

test('searches at or below the cap have no truncation warning', async () => {
  for (const total of [0, 10, 100]) {
    const { element } = await startApp({ query: 'Linux', total });
    assert.doesNotMatch(element('status').textContent, /first 100|Narrow your search/);
    assert.equal(element('more').hidden, total <= 10);
  }
});
