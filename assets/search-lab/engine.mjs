// Dependency-free BM25 baseline. Exact identifiers stay searchable alongside words.
const stop = new Set('a an and are at be can do for from how i in is it me my of on or the to using what with'.split(' '));
export function tokenize(text) {
  return String(text).toLowerCase().match(/[\p{L}\p{N}]+(?:[.+#-][\p{L}\p{N}+#]+)*/gu) || [];
}
// One insertion, deletion, substitution, or adjacent transposition.
function oneEditAway(a, b) {
  if (Math.abs(a.length - b.length) > 1) return false;
  let i = 0;
  while (i < a.length && a[i] === b[i]) i++;
  if (i === a.length) return b.length === a.length + 1;
  if (a.length === b.length) {
    return a.slice(i + 1) === b.slice(i + 1)
      || (a[i] === b[i + 1] && a[i + 1] === b[i] && a.slice(i + 2) === b.slice(i + 2));
  }
  return a.length > b.length ? a.slice(i + 1) === b.slice(i) : a.slice(i) === b.slice(i + 1);
}
export function createEngine(records) {
  const fields = [['title', 5], ['description', 3], ['authors', 3], ['metadata', 2], ['prerequisites', 2], ['summary', 1], ['faq', 1]];
  const docs = records.map(record => ({ record, fields: fields.map(([key, boost]) => {
    const value = record[key] || '';
    const tokens = tokenize(Array.isArray(value) ? value.join(' ') : value);
    const counts = new Map();
    for (const token of tokens) counts.set(token, (counts.get(token) || 0) + 1);
    return { counts, length: tokens.length, boost };
  }) }));
  const averages = fields.map((_, i) => docs.reduce((n, d) => n + d.fields[i].length, 0) / (docs.length || 1) || 1);
  const df = new Map();
  for (const doc of docs) {
    const terms = new Set(doc.fields.flatMap(f => [...f.counts.keys()]));
    for (const term of terms) df.set(term, (df.get(term) || 0) + 1);
  }
  const vocabulary = [...df.keys()];
  return function search(input = {}) {
    if (!input || typeof input !== 'object' || Array.isArray(input)) throw Error('Arguments must be an object.');
    if (Object.keys(input).some(key => !['query', 'type', 'category', 'limit', 'sort'].includes(key))) throw Error('Unknown search argument.');
    const { query, type = '', category = '', limit = 10, sort = 'relevance' } = input;
    if (typeof query !== 'string' || !query.trim() || query.length > 300) throw Error('Query must contain 1–300 characters.');
    if (!['', 'learning-path', 'install-guide'].includes(type)) throw Error('Unknown content type.');
    if (typeof category !== 'string' || (category && !records.some(r => r.category === category))) throw Error('Unknown category.');
    if (!Number.isInteger(limit) || limit < 1 || limit > 100) throw Error('Limit must be an integer from 1 to 100.');
    if (!['updated', 'relevance'].includes(sort)) throw Error('Unknown sort order.');
    const terms = [...new Set(tokenize(query).filter(t => !stop.has(t)))];
    if (!terms.length) return { total: 0, results: [] };
    const expansions = terms.map(term => {
      const candidates = [{ token: term, weight: 1 }];
      if (/^\p{L}{3,}$/u.test(term)) {
        for (const token of vocabulary) {
          if (token !== term && token.startsWith(term)) candidates.push({ token, weight: 0.65 });
        }
        // Correct a typo only when there is no exact token or prefix completion.
        if (!df.has(term) && candidates.length === 1 && /^\p{L}{5,}$/u.test(term)) {
          for (const token of vocabulary) {
            if (/^\p{L}{5,}$/u.test(token) && oneEditAway(term, token)) candidates.push({ token, weight: 0.4 });
          }
        }
      }
      return candidates.map(candidate => ({ ...candidate,
        idf: Math.log(1 + (docs.length - (df.get(candidate.token) || 0) + 0.5) / ((df.get(candidate.token) || 0) + 0.5))
      }));
    });
    const ranked = [];
    for (const doc of docs) {
      if ((type && doc.record.type !== type) || (category && doc.record.category !== category)) continue;
      let score = 0, matched = 0, exact = 0;
      for (const candidates of expansions) {
        let termScore = 0;
        let exactMatch = false;
        doc.fields.forEach((field, i) => {
          let best = 0;
          for (const { token, weight, idf } of candidates) {
            const tf = field.counts.get(token) || 0;
            if (weight === 1 && tf) exactMatch = true;
            best = Math.max(best, weight * field.boost * idf * tf * 2.2 / (tf + 1.2 * (0.25 + 0.75 * field.length / averages[i])));
          }
          termScore += best;
        });
        if (termScore) matched++;
        if (exactMatch) exact++;
        score += termScore;
      }
      // Reward coverage so long natural-language queries can still find partial matches.
      if (matched) ranked.push({ record: { ...doc.record, score: score * (matched / terms.length) ** 2 },
        tier: exact === terms.length ? 2 : matched === terms.length ? 1 : 0 });
    }
    ranked.sort((a, b) => {
      // ISO date strings sort chronologically; missing dates follow dated results.
      const dateOrder = sort === 'updated' ? (b.record.lastUpdated || '').localeCompare(a.record.lastUpdated || '') : 0;
      const coverageOrder = sort === 'relevance' ? b.tier - a.tier : 0;
      return dateOrder || coverageOrder || b.record.score - a.record.score || a.record.id.localeCompare(b.record.id);
    });
    return { total: ranked.length, results: ranked.slice(0, limit).map(item => item.record) };
  };
}
