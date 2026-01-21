from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, Optional

from .util import ensure_path, run_subprocess


def convert_etdump_to_csv(etdump: Path, out_dir: Path, python: Path) -> Optional[Path]:
    ensure_path(out_dir)
    cmd = [
        str(python),
        "model_profiling/tools/etdump_to_csv.py",
        "--etdump",
        str(etdump),
        "--out-dir",
        str(out_dir),
        "--all-runs",
    ]
    run_subprocess(cmd, cwd=Path.cwd())
    # Naming convention has evolved; support both:
    # - <stem>_exec_all_runs_timeline.csv  (current)
    # - <stem>_all_runs_timeline.csv       (legacy)
    candidates = [
        out_dir / f"{etdump.stem}_exec_all_runs_timeline.csv",
        out_dir / f"{etdump.stem}_all_runs_timeline.csv",
    ]
    for timeline in candidates:
        if timeline.exists():
            return timeline
    return None


def run_robust_latency_analysis(
    timeline_csv: Path, out_dir: Path, name: str, python: Path
) -> Optional[Dict[str, Any]]:
    cmd = [
        str(python),
        "model_profiling/tools/robust_latency_analysis.py",
        "--timeline-csv",
        str(timeline_csv),
        "--output-dir",
        str(out_dir),
        "--name",
        name,
    ]
    run_subprocess(cmd, cwd=Path.cwd())
    robust_path = out_dir / f"{timeline_csv.stem}_robust_stats.json"
    if robust_path.exists():
        return json.loads(robust_path.read_text())
    return None


def run_operator_analysis(timeline_csv: Path, out_dir: Path, python: Path) -> None:
    if not timeline_csv.exists():
        return
    cmd = [
        str(python),
        "model_profiling/tools/analyze_etdump_csv.py",
        "--timeline-csv",
        str(timeline_csv),
        "--output-dir",
        str(out_dir),
    ]
    run_subprocess(cmd, cwd=Path.cwd())


def extract_kernels_from_xnntrace(
    xnntrace_log: Path, out_dir: Path, model_id: str, python: Path
) -> Optional[Path]:
    """Extract kernels from xnntrace log using xnntrace_to_kernels.py."""
    if not xnntrace_log.exists():
        return None
    ensure_path(out_dir)
    kernel_csv = out_dir / f"{model_id}_kernels.csv"
    cmd = [
        str(python),
        "model_profiling/tools/xnntrace_to_kernels.py",
        "--xnntrace",
        str(xnntrace_log),
        "--out",
        str(kernel_csv),
        "--model-id",
        model_id,
    ]
    run_subprocess(cmd, cwd=Path.cwd())
    return kernel_csv if kernel_csv.exists() else None


def generate_kernel_view(
    sme2_on_csv: Path,
    sme2_off_csv: Path,
    out_path: Path,
    title: str,
    filter_op: str = "gemm",
    python: Path = None,
) -> Optional[Path]:
    """Generate kernel view table comparing SME2-On vs SME2-Off."""
    if not sme2_on_csv.exists() or not sme2_off_csv.exists():
        return None
    if python is None:
        python = Path(sys.executable)
    ensure_path(out_path.parent)
    cmd = [
        str(python),
        "model_profiling/tools/generate_kernel_view.py",
        "--sme2-on",
        str(sme2_on_csv),
        "--sme2-off",
        str(sme2_off_csv),
        "--out",
        str(out_path),
        "--filter-op",
        filter_op,
        "--title",
        title,
    ]
    run_subprocess(cmd, cwd=Path.cwd())
    return out_path if out_path.exists() else None
