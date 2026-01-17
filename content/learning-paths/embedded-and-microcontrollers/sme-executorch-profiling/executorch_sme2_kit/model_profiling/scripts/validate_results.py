#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path


def check(cond: bool, ok: str, fail: str) -> bool:
    if cond:
        print(f"✅ {ok}")
        return True
    print(f"❌ {fail}")
    return False


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate outputs of a profiling run directory.")
    ap.add_argument("--results", type=Path, required=True, help="Run directory (e.g., out_<model>/runs/mac)")
    args = ap.parse_args()

    run_dir = args.results.resolve()
    ok = True

    ok &= check(run_dir.exists(), f"run dir exists: {run_dir}", f"missing run dir: {run_dir}")

    manifest = run_dir / "manifest.json"
    metrics = run_dir / "metrics.json"
    ok &= check(manifest.exists(), "manifest.json exists", "manifest.json missing")
    ok &= check(metrics.exists(), "metrics.json exists", "metrics.json missing")

    # Check at least one ETDump exists.
    etdumps = list(run_dir.glob("**/*.etdump"))
    ok &= check(bool(etdumps), f"found {len(etdumps)} .etdump file(s)", "no .etdump found")

    # Basic schema sanity.
    if manifest.exists():
        try:
            data = json.loads(manifest.read_text(encoding="utf-8"))
            ok &= check("model" in data, "manifest contains model", "manifest missing model field")
            ok &= check("results" in data and isinstance(data["results"], list), "manifest contains results[]", "manifest missing results[]")
        except Exception as exc:
            ok &= check(False, "manifest JSON parses", f"manifest JSON parse error: {exc}")

    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())


