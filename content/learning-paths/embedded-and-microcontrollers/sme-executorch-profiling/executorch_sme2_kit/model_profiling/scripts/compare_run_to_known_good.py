#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Dict, List, Tuple


def load_json(p: Path) -> Dict[str, Any]:
    return json.loads(p.read_text(encoding="utf-8"))


def require(path: Path, errors: List[str], what: str) -> None:
    if not path.exists():
        errors.append(f"missing {what}: {path}")


def _pick_etdump_path(metrics: Dict[str, Any]) -> str | None:
    return metrics.get("etdump_rel") or metrics.get("etdump")


def _required_manifest_fields(m: Dict[str, Any]) -> List[Tuple[str, str]]:
    return [
        ("model", "manifest.model"),
        ("executorch", "manifest.executorch"),
        ("results", "manifest.results"),
    ]


def compare(run_dir: Path, fixture_dir: Path) -> List[str]:
    errors: List[str] = []

    require(run_dir / "manifest.json", errors, "run manifest.json")
    require(run_dir / "metrics.json", errors, "run metrics.json")
    require(run_dir / "analysis_summary.json", errors, "run analysis_summary.json (run analyze_results.py first)")
    if errors:
        return errors

    run_manifest = load_json(run_dir / "manifest.json")
    fix_manifest = load_json(fixture_dir / "manifest.json")

    for key, label in _required_manifest_fields(run_manifest):
        if key not in run_manifest:
            errors.append(f"missing field: {label}")

    # Schema-level checks: results list exists and has at least one experiment with an etdump path.
    run_results = run_manifest.get("results", [])
    if not isinstance(run_results, list) or not run_results:
        errors.append("manifest.results must be a non-empty list")
        return errors

    # Compare experiment names (ignore ordering).
    # The fixture is allowed to be a *minimal* subset ("known-good sanity run"),
    # while the user's run may include additional experiments (e.g., SME2 on/off).
    run_names = sorted({r.get("experiment") for r in run_results if isinstance(r, dict)})
    fix_names = sorted({r.get("experiment") for r in fix_manifest.get("results", []) if isinstance(r, dict)})
    if fix_names and not set(fix_names).issubset(set(run_names)):
        errors.append(f"experiment set mismatch (fixture must be subset of run): run={run_names} fixture={fix_names}")

    # Ensure each experiment has an ETDump file on disk (prefer rel path).
    for r in run_results:
        if not isinstance(r, dict):
            continue
        m = r.get("metrics", {}) if isinstance(r.get("metrics"), dict) else {}
        etdump_path = _pick_etdump_path(m)
        if not etdump_path:
            errors.append(f"missing etdump path in metrics for experiment {r.get('experiment')}")
            continue
        # If rel, resolve under run_dir; if abs, use as-is.
        p = Path(etdump_path)
        if not p.is_absolute():
            p = run_dir / p
        if not p.exists():
            errors.append(f"missing etdump file for experiment {r.get('experiment')}: {p}")

    # Compare analysis_summary schema keys and category names (ignore absolute timings).
    run_summary = load_json(run_dir / "analysis_summary.json")
    fix_summary = load_json(fixture_dir / "analysis_summary.json")

    for k in ["category_totals_ms", "per_etdump", "kernel_hints"]:
        if k not in run_summary:
            errors.append(f"analysis_summary missing key: {k}")

    run_cats = set((run_summary.get("category_totals_ms") or {}).keys())
    fix_cats = set((fix_summary.get("category_totals_ms") or {}).keys())
    if fix_cats and not fix_cats.issubset(run_cats):
        errors.append(f"category set mismatch (fixture must be subset of run): run={sorted(run_cats)} fixture={sorted(fix_cats)}")

    return errors


def main() -> None:
    ap = argparse.ArgumentParser(description="Compare a run directory against the known-good fixture (schema-level).")
    ap.add_argument("--run-dir", type=Path, required=True, help="Your run dir (e.g., runs/mac)")
    ap.add_argument(
        "--fixture-dir",
        type=Path,
        default=Path("test-cases/fixtures/known_good_mac/runs/mac"),
        help="Known-good fixture run dir",
    )
    args = ap.parse_args()

    run_dir = args.run_dir.resolve()
    fixture_dir = (Path(__file__).resolve().parents[1] / args.fixture_dir).resolve()

    errs = compare(run_dir, fixture_dir)
    if errs:
        print("❌ Run does not match known-good fixture (schema-level):")
        for e in errs:
            print(" -", e)
        raise SystemExit(2)

    print("✅ Run matches known-good fixture schema.")


if __name__ == "__main__":
    main()


