#!/usr/bin/env python3
"""Analyze ETDump files and generate CSV files in the same directory as ETDump files."""

import argparse
import json
import os
import subprocess
import sys
import warnings
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, List, Optional


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def _find_etdump_files(run_dir: Path) -> List[Path]:
    return sorted(run_dir.glob("**/*.etdump"))


def _find_etrecord(model_path: Optional[Path]) -> Optional[Path]:
    """Find etrecord file from model path."""
    if not model_path:
        return None
    etrecord = Path(str(model_path) + ".etrecord")
    return etrecord if etrecord.exists() else None


def _convert_etdump_to_csv(etdump: Path, etrecord: Optional[Path]) -> Dict[str, Optional[Path]]:
    """Convert ETDump to CSV files in the same directory as ETDump.
    
    Generates:
    - *_all_runs_timeline.csv: All runs with run_index column
    - *_run0_timeline.csv: Single run (run 0) for convenience
    - *_ops_stats.csv: Aggregated operator statistics
    """
    tools_dir = Path(__file__).parent.parent / "tools"
    etdump_to_csv_script = tools_dir / "etdump_to_csv.py"
    
    if not etdump_to_csv_script.exists():
        return {"timeline": None, "stats": None, "all_runs_timeline": None}
    
    csv_out_dir = etdump.parent  # Same directory as ETDump
    
    try:
        # Generate all_runs CSV (includes run0 as well)
        cmd = [
            sys.executable,
            str(etdump_to_csv_script),
            "--etdump", str(etdump),
            "--out-dir", str(csv_out_dir),
            "--model-id", etdump.stem,
            "--all-runs",  # Generate all_runs_timeline.csv and run0_timeline.csv
        ]
        if etrecord:
            cmd.extend(["--etrecord", str(etrecord)])
        
        subprocess.run(cmd, check=True, capture_output=True, text=True)
        
        csv_prefix = etdump.stem
        all_runs_timeline_csv = csv_out_dir / f"{csv_prefix}_exec_all_runs_timeline.csv"
        run0_timeline_csv = csv_out_dir / f"{csv_prefix}_exec_run0_timeline.csv"
        stats_csv = csv_out_dir / f"{csv_prefix}_exec_ops_stats.csv"
        
        return {
            "timeline": run0_timeline_csv if run0_timeline_csv.exists() else None,  # For backward compatibility
            "all_runs_timeline": all_runs_timeline_csv if all_runs_timeline_csv.exists() else None,
            "stats": stats_csv if stats_csv.exists() else None,
        }
    except Exception:
        return {"timeline": None, "stats": None, "all_runs_timeline": None}


def _categorize_op(op_name: str) -> str:
    s = (op_name or "").lower()
    if "conv" in s:
        return "Convolution"
    if "matmul" in s or "linear" in s or "gemm" in s:
        return "GEMM"
    if "transpose" in s or "reshape" in s or "copy" in s or "convert" in s or "pad" in s:
        return "Data Movement"
    if any(k in s for k in ["relu", "gelu", "sigmoid", "tanh", "hardtanh", "hardswish", "hard_swish", "clamp", "add", "mul", "sub", "div"]):
        return "Elementwise"
    return "Other"


def _analyze_etdump(etdump: Path, etrecord: Optional[Path]) -> Dict[str, Any]:
    """Analyze single ETDump file."""
    from executorch.devtools.inspector import Inspector
    import csv
    import io
    
    try:
        if etrecord:
            inspector = Inspector(etrecord=str(etrecord), etdump_path=str(etdump))
        else:
            inspector = Inspector(etdump_path=str(etdump))
    except Exception:
        if etrecord:
            inspector = Inspector(etdump_path=str(etdump))
        else:
            raise
    
    buf = io.StringIO()
    inspector.save_data_to_tsv(buf)
    buf.seek(0)
    rows = list(csv.DictReader(buf, delimiter="\t"))
    
    per_cat = defaultdict(float)
    for r in rows:
        op_types = r.get("op_types") or ""
        cat = _categorize_op(op_types)
        avg_ms = r.get("avg (ms)") or r.get("avg_ms") or ""
        try:
            per_cat[cat] += float(avg_ms)
        except Exception:
            pass
    
    return {"categories_ms": dict(per_cat), "rows": len(rows)}


def summarize(run_dir: Path, etrecord: Optional[Path] = None) -> Dict[str, Any]:
    etdumps = _find_etdump_files(run_dir)
    if not etdumps:
        raise SystemExit(f"No .etdump files found under: {run_dir}")
    
    summaries = []
    category_totals = defaultdict(float)
    csv_files = []
    
    for etdump in etdumps:
        # Generate CSV files in same directory as ETDump
        csv_info = _convert_etdump_to_csv(etdump, etrecord)
        if csv_info.get("all_runs_timeline"):
            csv_files.append(str(csv_info["all_runs_timeline"]))
        elif csv_info.get("timeline"):
            csv_files.append(str(csv_info["timeline"]))
        if csv_info.get("stats"):
            csv_files.append(str(csv_info["stats"]))
        
        # Analyze ETDump
        analysis = _analyze_etdump(etdump, etrecord)
        for cat, ms in analysis["categories_ms"].items():
            category_totals[cat] += ms
        
        summaries.append({
            "etdump": str(etdump),
            "categories_ms": analysis["categories_ms"],
            "rows": analysis["rows"],
            "csv_timeline": str(csv_info["timeline"]) if csv_info.get("timeline") else None,
            "csv_stats": str(csv_info["stats"]) if csv_info.get("stats") else None,
        })
    
    return {
        "run_dir": str(run_dir),
        "etrecord": str(etrecord) if etrecord else None,
        "etdump_count": len(etdumps),
        "category_totals_ms": dict(category_totals),
        "per_etdump": summaries,
        "csv_files": csv_files,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Analyze ETDump files and generate CSV files.")
    ap.add_argument("--run-dir", type=Path, required=True, help="Run output directory")
    ap.add_argument("--quiet", action="store_true", help="Suppress warnings")
    args = ap.parse_args()
    
    if args.quiet:
        os.environ.setdefault("GLOG_minloglevel", "2")
        os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")
        warnings.filterwarnings("ignore", message="Output Buffer not found.*")
        warnings.filterwarnings("ignore", message="Unsupported kwarg encountered:*")
    
    run_dir = args.run_dir.resolve()
    manifest = run_dir / "manifest.json"
    
    # Find etrecord from manifest if available
    etrecord = None
    if manifest.exists():
        manifest_data = load_json(manifest)
        model_path = manifest_data.get("model")
        if model_path:
            etrecord = _find_etrecord(Path(model_path))
    
    report = summarize(run_dir, etrecord)
    out = run_dir / "analysis_summary.json"
    write_json(out, report)
    print(f"Wrote: {out}")
    
    if report.get("csv_files"):
        print(f"Generated {len(report['csv_files'])} CSV file(s)")
    
    print("\nTop categories (ms, summed across traces):")
    for k, v in sorted(report["category_totals_ms"].items(), key=lambda kv: kv[1], reverse=True):
        print(f"  - {k}: {v:.3f}")


if __name__ == "__main__":
    main()
