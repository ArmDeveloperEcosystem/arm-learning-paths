import test from 'node:test';
import assert from 'node:assert/strict';
import { createEngine, tokenize } from '../../assets/search-lab/engine.mjs';
const records = [
  { id: '/gcc/', title: 'GNU Compiler', authors: ['Jason Andrews'], description: 'Install GCC on Linux', type: 'install-guide', category: '' },
  { id: '/llama/', title: 'Deploy llama.cpp', authors: ['Pareena Verma', 'Jason Andrews'], description: 'Deploy a chatbot on AWS Graviton', type: 'learning-path', category: 'servers-and-cloud-computing' },
  { id: '/other/', title: 'Python chatbot', summary: 'Example mentions llama.cpp', type: 'learning-path', category: 'cross-platform' }
];
const search = createEngine(records);
test('technical punctuation survives tokenization', () => {
  assert.deepEqual(tokenize('llama.cpp SVE2 C++'), ['llama.cpp', 'sve2', 'c++']);
});
test('prerequisites and FAQ questions and answers can independently find content', () => {
  const expandedSearch = createEngine([
    { id: '/path/', title: 'Application tutorial', type: 'learning-path', prerequisites: 'SSH access with PMU counters', faq: 'Which binary path should I use? Use performix-analysis/dot_scalar.' },
    { id: '/guide/', title: 'Setup guide', type: 'install-guide', prerequisites: 'Arduino IDE' },
    { id: '/empty/', title: 'Another tutorial', type: 'learning-path' }
  ]);
  for (const query of ['PMU', 'binary path', 'dot_scalar']) {
    assert.equal(expandedSearch({ query }).results[0].id, '/path/');
  }
  assert.equal(expandedSearch({ query: 'Arduino' }).results[0].id, '/guide/');
  assert.equal(expandedSearch({ query: 'Arduino', type: 'learning-path' }).total, 0);
});
test('exact title and query coverage win', () => {
  assert.equal(search({ query: 'How do I deploy llama.cpp on Graviton?' }).results[0].id, '/llama/');
});
test('filters apply before limiting and total is independent of limit', () => {
  assert.equal(search({ query: 'chatbot', limit: 1 }).total, 2);
  assert.equal(search({ query: 'chatbot', category: 'cross-platform' }).results[0].id, '/other/');
  assert.equal(search({ query: 'GCC', type: 'learning-path' }).total, 0);
});
test('reject invalid tool arguments', () => {
  for (const input of [null, [], {}, { query: 'gcc', offset: -1 }, { query: 'gcc', offset: 1.5 }, { query: 'gcc', limit: 101 }, { query: 'gcc', limit: 1.5 }, { query: 'gcc', category: 'fake' }, { query: 'gcc', type: 'fake' }]) assert.throws(() => search(input));
});
test('stop-word-only or irrelevant queries produce no matches', () => {
  assert.equal(search({ query: 'the and' }).total, 0);
  assert.equal(search({ query: 'unfindable' }).total, 0);
});

test('author names are searchable alongside topic terms and returned in results', () => {
  assert.equal(search({ query: 'Jason Andrews' }).total, 2);
  assert.equal(search({ query: 'pArEeNa VeRmA' }).results[0].id, '/llama/');
  assert.equal(search({ query: 'Jason GCC' }).results[0].id, '/gcc/');
  assert.deepEqual(search({ query: 'Pareena' }).results[0].authors, ['Pareena Verma', 'Jason Andrews']);
});

test('newest sorting applies to all matches before limiting, with relevance as an alternative', () => {
  const datedSearch = createEngine([
    { id: '/old/', title: 'Docker Docker Docker', lastUpdated: '2025-01-01', type: 'install-guide' },
    { id: '/new/', title: 'Containers', description: 'Docker', lastUpdated: '2026-10-29', type: 'install-guide' },
    { id: '/missing/', title: 'Docker', type: 'learning-path' }
  ]);
  assert.deepEqual(datedSearch({ query: 'docker', sort: 'updated' }).results.map(r => r.id), ['/new/', '/old/', '/missing/']);
  assert.equal(datedSearch({ query: 'docker', sort: 'updated', limit: 1 }).results[0].id, '/new/');
  assert.equal(datedSearch({ query: 'docker', limit: 1 }).results[0].id, '/old/');
  assert.equal(datedSearch({ query: 'docker', sort: 'relevance' }).results[0].id, '/old/');
  assert.throws(() => datedSearch({ query: 'docker', sort: 'invalid' }));
});

test('relevance ranks all content by score, with content type available as a filter', () => {
  const prioritize = createEngine([
    { id: '/path/', title: 'Docker', type: 'learning-path', lastUpdated: '2026-10-29' },
    { id: '/weak-guide/', title: 'Containers', summary: 'Docker', type: 'install-guide', lastUpdated: '2025-01-01' },
    { id: '/strong-guide/', title: 'Docker', type: 'install-guide', lastUpdated: '2025-01-01' },
    { id: '/weak-path/', title: 'Containers', summary: 'Docker', type: 'learning-path', lastUpdated: '2026-10-28' },
    { id: '/unmatched/', title: 'GCC', type: 'install-guide' }
  ]);
  assert.deepEqual(prioritize({ query: 'docker', sort: 'relevance' }).results.map(r => r.id),
    ['/path/', '/strong-guide/', '/weak-guide/', '/weak-path/']);
  assert.equal(prioritize({ query: 'docker', sort: 'relevance', limit: 1 }).results[0].id, '/path/');
  assert.equal(prioritize({ query: 'docker', sort: 'updated' }).results[0].id, '/path/');
  assert.deepEqual(prioritize({ query: 'docker', sort: 'relevance', type: 'learning-path' }).results.map(r => r.id), ['/path/', '/weak-path/']);
  assert.deepEqual(prioritize({ query: 'docker', sort: 'relevance', type: 'install-guide' }).results.map(r => r.id), ['/strong-guide/', '/weak-guide/']);
});

test('a title and author match outranks install guides matching only the topic', () => {
  const search = createEngine([
    { id: '/llvm/', title: 'LLVM toolchain', summary: 'BOLT', type: 'install-guide' },
    { id: '/bolt/', title: 'Optimize applications with BOLT', authors: ['Gayathri'], type: 'learning-path' }
  ]);
  assert.equal(search({ query: 'bolt Gayathri', sort: 'relevance', limit: 1 }).results[0].id, '/bolt/');
});

test('all significant words rank before stronger partial matches, across fields', () => {
  const search = createEngine([
    { id: '/partial/', title: 'BOLT BOLT BOLT', description: 'BOLT', lastUpdated: '2026-10-01' },
    { id: '/complete/', title: 'Other topic', faq: 'BOLT', authors: ['Gayathri'], lastUpdated: '2025-01-01' }
  ]);
  const input = { query: 'BOLT and Gayathri' };
  assert.equal(search(input).results[0].id, '/complete/');
  assert.equal(search({ ...input, limit: 1 }).results[0].id, '/complete/');
  assert.equal(search({ ...input, sort: 'updated' }).results[0].id, '/partial/');
});

test('prefix completions rank below exact matches and cover every query word', () => {
  const search = createEngine([
    { id: '/prefix/', title: 'Graviton Docker' },
    { id: '/exact/', summary: 'grav dock' },
    { id: '/partial/', title: 'Graviton' }
  ]);
  assert.deepEqual(search({ query: 'grav dock' }).results.map(r => r.id), ['/exact/', '/prefix/', '/partial/']);
  assert.equal(search({ query: 'viton' }).total, 0, 'No arbitrary substring matches');
  assert.equal(search({ query: 'gr' }).total, 0, 'Prefixes need at least three letters');
});

test('typo fallback supports one edit including adjacent transposition', () => {
  const search = createEngine([{ id: '/docker/', title: 'Docker', authors: ['Gayathri'] }]);
  for (const query of ['dokcer', 'doker', 'dockerr', 'dockar', 'dokcer Gayathri']) {
    assert.equal(search({ query }).results[0]?.id, '/docker/', query);
  }
  assert.equal(search({ query: 'dakkar' }).total, 0, 'Two edits do not match');
  assert.equal(search({ query: 'dockar', type: 'install-guide' }).total, 0, 'Filters still apply');
});

test('typos do not expand valid tokens, short words, or technical identifiers', () => {
  const search = createEngine([
    { id: '/valid/', title: 'dockar' },
    { id: '/other/', title: 'Docker GCC SVE2 llama.cpp' }
  ]);
  assert.deepEqual(search({ query: 'dockar' }).results.map(r => r.id), ['/valid/']);
  for (const query of ['gdc', 'SVE3', 'llama.cop']) assert.equal(search({ query }).total, 0, query);
});


test('language aliases match in both queries and indexed fields without changing identifiers', () => {
  const search = createEngine([
    { id: '/cpp-tag/', title: 'Qt application', metadata: ['CPP'] },
    { id: '/cpp-title/', title: 'C++ application' },
    { id: '/sharp-tag/', title: 'Application', metadata: ['csharp'] },
    { id: '/sharp-title/', title: 'C# application' },
    { id: '/identifier/', title: 'llama.cpp' },
    { id: '/c/', title: 'C application' }
  ]);
  for (const [alias, language] of [['CPP', 'C++'], ['csharp', 'C#']]) {
    assert.deepEqual(search({ query: alias }), search({ query: language }));
    assert.equal(search({ query: language }).total, 2);
  }
  assert.deepEqual(tokenize('C C# C++ cpp csharp llama.cpp'), ['c', 'c#', 'c++', 'c++', 'c#', 'llama.cpp']);
  assert.equal(search({ query: 'llama.cpp' }).total, 1);
});

test('install guides ignore Learning Path categories while other searches keep them', () => {
  assert.deepEqual(search({ query: 'GCC', type: 'install-guide', category: 'cross-platform' }),
    search({ query: 'GCC', type: 'install-guide' }));
  assert.equal(search({ query: 'GCC', category: 'cross-platform' }).total, 0);
});

test('blank browsing filters before pagination and sorts newest first with missing dates last', () => {
  const records = [
    { id: '/old/', title: 'Old', type: 'learning-path', category: 'cross-platform', lastUpdated: '2025-01-01' },
    { id: '/new/', title: 'New', type: 'install-guide', category: '', lastUpdated: '2026-01-01' },
    { id: '/missing/', title: 'Missing date', type: 'learning-path', category: 'cross-platform' }
  ];
  const search = createEngine(records);
  for (const query of ['', '   ']) {
    assert.deepEqual(search({ query }).results.map(r => r.id), ['/new/', '/old/', '/missing/']);
    assert.equal(search({ query, offset: 1, limit: 1 }).results[0].id, '/old/');
    assert.equal(search({ query, offset: 10 }).total, 3);
    assert.equal(search({ query, offset: 10 }).results.length, 0);
    assert.equal(search({ query, type: 'install-guide', category: 'cross-platform' }).total, 1);
    assert.equal(search({ query, type: 'learning-path' }).total, 2);
    assert.equal(search({ query, category: 'cross-platform', offset: 1, limit: 1 }).results[0].id, '/missing/');
  }
});

test('offset pagination preserves keyword rankings', () => {
  const all = search({ query: 'chatbot' });
  assert.deepEqual(search({ query: 'chatbot', offset: 1, limit: 1 }).results, all.results.slice(1, 2));
});
