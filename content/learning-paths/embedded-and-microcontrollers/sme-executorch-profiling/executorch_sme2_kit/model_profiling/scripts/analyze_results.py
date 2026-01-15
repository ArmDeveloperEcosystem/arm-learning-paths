#!/usr/bin/env python3
from __future__ import annotations

import argparse
import csv
import json
import os
import re
import warnings
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Dict, Iterable, List, Tuple


KERNEL_HINT_RE = re.compile(r"__neonsme2|sme2|neon", re.IGNORECASE)


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def _find_etdump_files(run_dir: Path) -> List[Path]:
    return sorted(run_dir.glob("**/*.etdump"))


def _infer_etrecord_for_model(model_pte: Path) -> Path:
    # Default: <pte>.etrecord (this is how export_model.py writes by default).
    return Path(str(model_pte) + ".etrecord")


def _inspector_rows(etrecord: Path, etdump: Path) -> List[Dict[str, Any]]:
    """
    Return Inspector tabular rows as dictionaries.
    """
    from executorch.devtools.inspector import Inspector

    ins = Inspector(etrecord=str(etrecord), etdump_path=str(etdump))
    # Save TSV to memory (Inspector API supports file-like). We'll use a temp string buffer.
    import io

    buf = io.StringIO()
    ins.save_data_to_tsv(buf)
    buf.seek(0)
    reader = csv.DictReader(buf, delimiter="\t")
    return list(reader)


def _categorize_op(op_name: str) -> str:
    s = (op_name or "").lower()
    if "conv" in s:
        return "Convolution"
    if "matmul" in s or "linear" in s or "gemm" in s:
        return "GEMM"
    if "transpose" in s or "reshape" in s or "copy" in s or "convert" in s or "pad" in s:
        return "Data Movement"
    if any(
        k in s
        for k in [
            # activations / pointwise
            "relu",
            "gelu",
            "sigmoid",
            "tanh",
            "hardtanh",
            "hardswish",
            "hard_swish",
            "clamp",
            # arithmetic
            "add",
            "mul",
            "sub",
            "div",
        ]
    ):
        return "Elementwise"
    return "Other"


def _extract_kernel_hints(rows: Iterable[Dict[str, Any]]) -> Counter:
    """
    Best-effort: the Inspector output may contain delegate debug info fields depending on ExecuTorch version.
    We look across all columns and extract strings that hint about kernel selection.
    """
    c = Counter()
    for r in rows:
        joined = " | ".join(str(v) for v in r.values() if v)
        for m in KERNEL_HINT_RE.finditer(joined):
            c[m.group(0).lower()] += 1
    return c


def summarize(run_dir: Path, model_pte: Path) -> Dict[str, Any]:
    etrecord = _infer_etrecord_for_model(model_pte)
    if not etrecord.exists():
        raise SystemExit(f"Missing etrecord: {etrecord} (re-export model with model_profiling/export/export_model.py)")

    etdumps = _find_etdump_files(run_dir)
    if not etdumps:
        raise SystemExit(f"No .etdump files found under: {run_dir}")

    summaries: List[Dict[str, Any]] = []
    category_totals: Dict[str, float] = defaultdict(float)
    kernel_hints_total = Counter()

    for etdump in etdumps:
        rows = _inspector_rows(etrecord, etdump)
        kernel_hints_total.update(_extract_kernel_hints(rows))

        # Heuristic: use avg/ms columns if present; otherwise skip numeric attribution.
        # Many Inspector TSVs include 'avg (ms)'.
        per_cat = defaultdict(float)
        for r in rows:
            op_types = r.get("op_types") or ""
            cat = _categorize_op(op_types)
            avg_ms = r.get("avg (ms)") or r.get("avg_ms") or ""
            try:
                v = float(avg_ms)
            except Exception:
                v = 0.0
            per_cat[cat] += v

        for k, v in per_cat.items():
            category_totals[k] += v

        summaries.append(
            {
                "etdump": str(etdump),
                "categories_ms": dict(per_cat),
                "rows": len(rows),
            }
        )

    return {
        "run_dir": str(run_dir),
        "model": str(model_pte),
        "etrecord": str(etrecord),
        "etdump_count": len(etdumps),
        "category_totals_ms": dict(category_totals),
        "kernel_hints": dict(kernel_hints_total),
        "per_etdump": summaries,
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="Analyze ETDump with ExecuTorch Inspector and summarize operator categories.")
    ap.add_argument("--run-dir", type=Path, required=True, help="Run output directory (e.g., runs/mac)")
    ap.add_argument("--model", type=Path, default=None, help="Path to .pte (default: read from manifest.json if present)")
    ap.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress noisy warnings from ExecuTorch Inspector/debug format parsing.",
    )
    args = ap.parse_args()

    if args.quiet:
        # Reduce common native logging noise during torch/executorch import.
        # (Best-effort: some builds still emit messages.)
        os.environ.setdefault("GLOG_minloglevel", "2")  # 0=INFO,1=WARNING,2=ERROR,3=FATAL
        os.environ.setdefault("TF_CPP_MIN_LOG_LEVEL", "2")

    run_dir = args.run_dir.resolve()
    manifest = run_dir / "manifest.json"
    model = args.model
    if model is None and manifest.exists():
        model = Path(load_json(manifest).get("model", ""))
    if model is None or not model.exists():
        raise SystemExit("Model .pte not found. Provide --model <path-to.pte> or ensure manifest.json exists.")

    if args.quiet:
        # These warnings are common across ExecuTorch versions and are usually not actionable
        # for end users running the learning path.
        warnings.filterwarnings("ignore", message="Output Buffer not found.*")
        warnings.filterwarnings("ignore", message="Unsupported kwarg encountered:*")

    report = summarize(run_dir, model.resolve())
    out = run_dir / "analysis_summary.json"
    write_json(out, report)
    print(f"Wrote: {out}")

    # Human-friendly console highlight:
    print("\nTop categories (ms, summed across traces):")
    for k, v in sorted(report["category_totals_ms"].items(), key=lambda kv: kv[1], reverse=True):
        print(f"  - {k}: {v:.3f}")
    if report["kernel_hints"]:
        print("\nKernel hints (best-effort, depends on ExecuTorch debug data):")
        for k, v in sorted(report["kernel_hints"].items(), key=lambda kv: kv[1], reverse=True):
            print(f"  - {k}: {v}")


if __name__ == "__main__":
    main()


