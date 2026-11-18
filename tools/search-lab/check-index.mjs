import fs from 'node:fs';
import path from 'node:path';
import assert from 'node:assert/strict';
import { gzipSync } from 'node:zlib';
import { createEngine } from '../../assets/search-lab/engine.mjs';
const root = process.argv[2];
if (!root) throw Error('Pass the Hugo output directory.');
const html = fs.readFileSync(path.join(root, 'search/index.html'), 'utf8');
const assetPath = url => path.join(root, decodeURI(new URL(url, 'https://preview.invalid').pathname));
const indexURL = html.match(/data-index="([^"]+)"/)[1];
const workerURL = html.match(/data-worker="([^"]+)"/)[1];
const bytes = fs.readFileSync(assetPath(indexURL));
const { records } = JSON.parse(bytes);
assert(records.length > 0);
assert.equal(new Set(records.map(r => r.id)).size, records.length, 'Duplicate entries');
for (const record of records) {
  assert(record.title && record.description !== undefined);
  assert.equal(typeof record.prerequisites, 'string');
  assert.equal(typeof record.faq, 'string');
  assert(record.id.startsWith('/learning-paths/') || record.id.startsWith('/install-guides/'));
  assert(fs.existsSync(path.join(root, decodeURI(record.id), 'index.html')), `Missing page: ${record.id}`);
}
for (const url of [indexURL, workerURL, ...[...html.matchAll(/(?:src|href)="([^"]*\/search-lab\/[^"]+\.(?:js|css))"/g)].map(match => match[1])]) {
  assert(fs.existsSync(assetPath(url)), `Missing asset: ${url}`);
  assert(/\.[a-f0-9]{64}\./.test(url), `Asset lacks content fingerprint: ${url}`);
}
const worker = fs.readFileSync(assetPath(workerURL), 'utf8');
const engineURL = worker.match(/import .* from '([^']+)'/)[1];
assert(/\.[a-f0-9]{64}\.mjs$/.test(engineURL));
assert(fs.existsSync(assetPath(engineURL)), 'Missing fingerprinted worker dependency');
const search = createEngine(records);
const performix = records.find(r => r.id === '/learning-paths/servers-and-cloud-computing/performix-get-started/');
assert(performix?.prerequisites.includes('Performance Monitor Unit (PMU)'), 'Missing Learning Path prerequisites');
assert(performix?.faq.includes('Which path should I use for my binary'), 'Missing FAQ question');
assert(performix?.faq.includes('performix-analysis/dot_scalar'), 'Missing FAQ answer');
assert(records.find(r => r.id === '/install-guides/arduino-pico/')?.prerequisites.includes('Arduino IDE'), 'Missing install guide prerequisites');
console.log(JSON.stringify({ documents: records.length, withPrerequisites: records.filter(r => r.prerequisites).length, withFaq: records.filter(r => r.faq).length, bytes: bytes.length, gzipBytes: gzipSync(bytes).length }));
for (const query of ['gcc', 'docker', 'llama.cpp Graviton', 'SVE2', 'Kubernetes', 'Jason Andrews']) {
  const start = performance.now();
  const result = search({ query, limit: 3 });
  assert(result.total > 0, `No results: ${query}`);
  console.log(JSON.stringify({ query, ms: +(performance.now() - start).toFixed(2), top: result.results.map(r => r.title) }));
}
