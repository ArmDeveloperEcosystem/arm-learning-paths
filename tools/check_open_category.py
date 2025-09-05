#!/usr/bin/env python3
"""
Simple checker for tools_software_languages.

Usage:
  python tools/check_tools_software_languages.py /abs/or/rel/path/to/content/<section>/<category>/<lp_name>/_index.md

Behavior:
  - Fails LOUDLY if OPENAI_API_KEY is not set or OpenAI call cannot be made.
  - Prints each step and the key variables/paths.
  - Exits 0 if nothing to change; exits 1 if suggestions/replacements are recommended; exits 2 for usage/path errors; exits 3 for OpenAI errors.

Requires:
  pip install pyyaml openai
  export OPENAI_API_KEY=sk-...
"""

from __future__ import annotations
import os
import re
import sys
import json
import difflib
from pathlib import Path
from typing import Dict, List, Tuple

import yaml
from openai import OpenAI


# ----------------------------
# 1) File helpers (front matter)
# ----------------------------

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n?", re.DOTALL)

def read_front_matter(md_path: Path) -> Tuple[Dict, str]:
    text = md_path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.search(text)
    if not m:
        print(f"[ERROR] No YAML front matter found in {md_path}")
        sys.exit(2)
    front = yaml.safe_load(m.group(1)) or {}
    body = text[m.end():]
    return front, body


# ----------------------------
# 2) Path resolution
# ----------------------------

def resolve_category_index(lp_index_path: Path) -> Path:
    """
    Works for:
      .../content/<section>/<category>/<lp>/_index.md
    or
      .../content/<category>/<lp>/_index.md

    The category file is the _index.md one level above the LP folder.
    """
    category_index = lp_index_path.parent.parent / "_index.md"
    print(f"[step] Resolved category index -> {category_index}")
    if not category_index.exists():
        print(f"[ERROR] Category _index.md not found at {category_index}")
        sys.exit(2)
    return category_index


# ----------------------------
# 3) Canonical list loading
# ----------------------------

def load_canonical_map(category_index_path: Path) -> Dict[str, int]:
    """
    Expects in category front matter:
      tools_software_languages_filter:
        - Label A: 3
        - Label B: 1
        ...
    Returns dict {label: count}
    """
    front, _ = read_front_matter(category_index_path)
    raw = front.get("tools_software_languages_filter")
    if raw is None:
        print("[WARN] 'tools_software_languages_filter' not found in category front matter. Using empty list.")
        return {}

    canonical: Dict[str, int] = {}
    if isinstance(raw, list):
        for item in raw:
            if isinstance(item, dict):
                for k, v in item.items():
                    canonical[str(k)] = int(v)
            elif isinstance(item, str):
                if ":" in item:
                    k, v = item.split(":", 1)
                    canonical[k.strip()] = int(v.strip())
                else:
                    canonical[item.strip()] = 0
    elif isinstance(raw, dict):
        canonical = {str(k): int(v) for k, v in raw.items()}
    else:
        print("[WARN] Unexpected format for tools_software_languages_filter; treating as empty.")
    print(f"[step] Loaded {len(canonical)} canonical labels from category.")
    return canonical


# ----------------------------
# 4) Normalization & similarity
# ----------------------------

def normalize_label(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"\s*&\s*|\s*and\s*", "/", s)  # use slash for combined items
    s = re.sub(r"[–—-]", "-", s)             # normalize dashes
    s = re.sub(r"\s*[\/|]\s*", "/", s)       # normalize separators
    s = re.sub(r"\s+", " ", s)
    return s

def shortlist_similar(entry: str, canon_labels: List[str], n: int = 5) -> List[str]:
    return difflib.get_close_matches(entry, canon_labels, n=n, cutoff=0.6)

def title_like(label: str) -> str:
    out = []
    for tok in re.split(r"(\s+)", label):
        if not tok.strip():
            out.append(tok)
            continue
        if re.search(r"[^A-Za-z]", tok) or tok.isupper():
            out.append(tok)
        else:
            out.append(tok.capitalize())
    return "".join(out).strip()


# ----------------------------
# 5) OpenAI call (FAILS if key missing or call fails)
# ----------------------------

def require_openai_client(model: str = "gpt-4o-2024-08-06") -> OpenAI:
    key = os.environ.get("OPENAI_API_KEY")
    if not key:
        print("ERROR: OPENAI_API_KEY is not set. This checker requires AI. Exiting.")
        sys.exit(3)
    try:
        client = OpenAI(api_key=key)
        # quick no-op to surface auth issues early (optional)
        # (we rely on the first call below; keeping it simple)
        print(f"[step] OpenAI client ready. Model = {model}")
        return client
    except Exception as e:
        print(f"ERROR: Failed to init OpenAI client: {e}")
        sys.exit(3)

def ai_decide_label(client: OpenAI, entry: str, candidates: List[str], examples: List[str],
                    model: str = "gpt-4o-2024-08-06") -> Dict:
    """
    Structured decision:
      action: use_existing | improve_new | ok
      suggested_label: string
      confidence: 0..1
      reason: string
    """
    schema = {
        "name": "ToolsLabelDecision",
        "schema": {
            "type": "object",
            "properties": {
                "action": {"type": "string", "enum": ["use_existing", "improve_new", "ok"]},
                "suggested_label": {"type": "string"},
                "confidence": {"type": "number", "minimum": 0.0, "maximum": 1.0},
                "reason": {"type": "string"}
            },
            "required": ["action", "suggested_label", "confidence", "reason"],
            "additionalProperties": False,
        },
        "strict": True,
    }

    system = (
        "You standardize taxonomy labels for 'tools_software_languages' on a public site. "
        "Prefer an existing canonical label if the user's entry is a near-duplicate. "
        "Otherwise, minimally rewrite to match brand-correctness (NGINX not ngnix; AWS Lambda not Lambda; Apache Tomcat not Tomcat; Visual Studio Code not VS Code)."
    )

    payload = {
        "entry": entry,
        "candidate_existing_labels": candidates,
        "canonical_examples": examples[:40]
    }

    print(f"[ai] entry={entry!r}, candidates={candidates}")

    try:
        resp = client.responses.create(
            model=model,
            instructions=system,
            input=[{"role": "user", "content": [{"type": "input_text", "text": json.dumps(payload, ensure_ascii=False)}]}],
            response_format={"type": "json_schema", **schema},
            temperature=0.0,
        )
        out = json.loads(resp.output_text)
        print(f"[ai] decision={out}")
        return out
    except Exception as e:
        print(f"ERROR: OpenAI call failed: {e}")
        sys.exit(3)


# ----------------------------
# 6) Core check logic
# ----------------------------

def check_entries(lp_index_path: Path, model: str = "gpt-4o-2024-08-06") -> int:
    """
    Returns number of issues (suggestions or replacements).
    """
    print(f"[step] LP index path -> {lp_index_path}")
    front, _ = read_front_matter(lp_index_path)

    # Read LP entries
    entries = front.get("tools_software_languages")
    if entries is None:
        print("[WARN] No 'tools_software_languages' field found in LP. Treating as empty.")
        entries = []
    if not isinstance(entries, list):
        print("[ERROR] 'tools_software_languages' must be a list.")
        sys.exit(2)
    print(f"[step] Found {len(entries)} LP entries.")

    # Resolve category and load canonicals
    category_index = resolve_category_index(lp_index_path)
    canonical_map = load_canonical_map(category_index)
    canonical_labels = sorted(canonical_map.keys())
    canonical_norm = {normalize_label(k): k for k in canonical_labels}
    print(f"[step] Canonical labels (print up to 10): {canonical_labels[:10]}")

    # Require OpenAI (fail loudly if missing)
    client = require_openai_client(model=model)

    # Analyze entries
    issues = []
    for raw in entries:
        if not isinstance(raw, str):
            issues.append({"entry": raw, "status": "error", "message": "Non-string value."})
            print(f"[entry] {raw!r} -> ERROR non-string")
            continue

        entry = raw.strip()
        if not entry:
            issues.append({"entry": raw, "status": "error", "message": "Empty string."})
            print(f"[entry] {raw!r} -> ERROR empty")
            continue

        print(f"[entry] Checking: {entry!r}")

        # Exact match
        if entry in canonical_labels:
            print("  - exact canonical: OK")
            continue

        # Normalized match
        norm = normalize_label(entry)
        if norm in canonical_norm:
            suggested = canonical_norm[norm]
            print(f"  - normalized match -> suggest canonical '{suggested}'")
            issues.append({"entry": entry, "status": "replace", "suggested": suggested, "why": "Normalization match."})
            continue

        # Similar candidates + AI decision
        sims = shortlist_similar(entry, canonical_labels, n=7)
        decision = ai_decide_label(client, entry, sims, canonical_labels, model=model)

        action = decision.get("action")
        suggested = decision.get("suggested_label", entry)
        conf = decision.get("confidence", 0.0)
        reason = decision.get("reason", "")

        if action == "use_existing":
            print(f"  - AI: use existing -> '{suggested}' (conf={conf:.2f})")
            issues.append({"entry": entry, "status": "replace", "suggested": suggested,
                           "why": f"Near-duplicate per AI (conf {conf:.2f})", "reason": reason})
        elif action == "improve_new":
            # If the rewrite equals a canonical, treat as replace; else rewrite
            if suggested in canonical_labels:
                print(f"  - AI: rewrite equals canonical -> replace with '{suggested}' (conf={conf:.2f})")
                issues.append({"entry": entry, "status": "replace", "suggested": suggested,
                               "why": f"AI rewrite aligns with canonical (conf {conf:.2f})", "reason": reason})
            else:
                print(f"  - AI: suggest rewrite -> '{suggested}' (conf={conf:.2f})")
                issues.append({"entry": entry, "status": "rewrite", "suggested": suggested,
                               "why": f"Style-aligned rewrite (conf {conf:.2f})", "reason": reason})
        else:
            # ok; minor style nits?
            improved = title_like(entry).replace(" & ", "/").replace("&", "/")
            improved = re.sub(r"\s*/\s*", "/", improved)
            if improved != entry:
                print(f"  - OK but style tweak -> '{improved}'")
                issues.append({"entry": entry, "status": "rewrite", "suggested": improved,
                               "why": "Minor style tweak."})
            else:
                print("  - OK as-is.")

    # Report
    print("\n[report]")
    if not issues:
        print("✓ tools_software_languages: all entries look good.")
        return 0

    for i, it in enumerate(issues, 1):
        print(f"{i}. Entry: {it['entry']!r}")
        print(f"   Status: {it['status']}")
        if "suggested" in it:
            print(f"   Suggested: {it['suggested']}")
        if "why" in it:
            print(f"   Why: {it['why']}")
        if "reason" in it and it["reason"]:
            print(f"   Model: {it['reason']}")
        print()

    print("[json]")
    print(json.dumps({"file": str(lp_index_path), "issues": issues}, ensure_ascii=False, indent=2))
    return len(issues)


# ----------------------------
# 7) main()
# ----------------------------

def main():
    if len(sys.argv) != 2:
        print("Usage: python tools/check_tools_software_languages.py /path/to/content/<section>/<category>/<lp>/_index.md")
        sys.exit(2)

    lp_index_path = Path(sys.argv[1]).resolve()
    if not lp_index_path.exists():
        print(f"[ERROR] File not found: {lp_index_path}")
        sys.exit(2)

    # Single sequential flow so you can follow the variables:
    problems = check_entries(lp_index_path, model="gpt-4o-2024-08-06")

    # Exit codes: 0 ok, 1 issues found
    sys.exit(1 if problems > 0 else 0)


if __name__ == "__main__":
    main()
