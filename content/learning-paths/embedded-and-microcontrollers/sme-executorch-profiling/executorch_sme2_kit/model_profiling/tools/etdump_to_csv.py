#!/usr/bin/env python3
import argparse
import csv
import json
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional, Tuple
import sys

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "src"))
sys.path.insert(0, str(REPO_ROOT))

from executorch.devtools import Inspector  # type: ignore
from executorch.devtools.inspector import TimeScale  # type: ignore


def base_op_type(name: str) -> str:
    if not isinstance(name, str):
        return ""
    n = name.strip().strip('"')
    if " #" in n:
        n = n.rsplit(" #", 1)[0]
    return n


def choose_backend(row: Dict[str, Any]) -> str:
    is_delegated = bool(row.get("is_delegated_op"))
    if is_delegated:
        b = row.get("delegate_backend_name")
        if b is None or b == "":
            return "delegated"
        return str(b)
    return "portable"


def extract_run_events(df, run_index: int) -> List[Dict[str, Any]]:
    """Extract events for a single run."""
    rows: List[Dict[str, Any]] = []
    node_id = 0
    for _, r in df.iterrows():
        starts = r.get("start_time")
        raws = r.get("raw")
        if not (isinstance(starts, list) and isinstance(raws, list)):
            # skip rows without per-run timing
            continue
        if not (0 <= run_index < len(starts) and len(starts) == len(raws)):
            continue
        start_ns = starts[run_index]
        dur_ms = raws[run_index]
        try:
            start_us = float(start_ns) / 1000.0
            dur_ms_f = float(dur_ms)
        except Exception:
            continue
        end_us = start_us + dur_ms_f * 1000.0
        name = r.get("event_name")
        rec = {
            "node_id": node_id,
            "run_index": run_index,
            "block": r.get("event_block_name"),
            "name": name,
            "type": base_op_type(str(name) if name is not None else ""),
            "delegate_backend": choose_backend(r),
            "start_us": start_us,
            "end_us": end_us,
            "duration_ms": dur_ms_f,
        }
        rows.append(rec)
        node_id += 1
    # pct_total computed by caller
    return rows


def extract_all_runs_events(df) -> List[Dict[str, Any]]:
    """Extract events for all runs, with run_index column indicating which run each event belongs to."""
    rows: List[Dict[str, Any]] = []
    node_id = 0
    for _, r in df.iterrows():
        starts = r.get("start_time")
        raws = r.get("raw")
        if not (isinstance(starts, list) and isinstance(raws, list)):
            # skip rows without per-run timing
            continue
        if len(starts) != len(raws):
            continue
        
        name = r.get("event_name")
        base_type = base_op_type(str(name) if name is not None else "")
        backend = choose_backend(r)
        block = r.get("event_block_name")
        
        # Extract all runs for this event
        for run_index in range(len(starts)):
            start_ns = starts[run_index]
            dur_ms = raws[run_index]
            try:
                start_us = float(start_ns) / 1000.0
                dur_ms_f = float(dur_ms)
            except Exception:
                continue
            end_us = start_us + dur_ms_f * 1000.0
            
            rec = {
                "node_id": node_id,
                "run_index": run_index,
                "block": block,
                "name": name,
                "type": base_type,
                "delegate_backend": backend,
                "start_us": start_us,
                "end_us": end_us,
                "duration_ms": dur_ms_f,
            }
            rows.append(rec)
        node_id += 1
    
    # Compute pct_total per run (each run's events should sum to 100%)
    run_totals: Dict[int, float] = {}
    for row in rows:
        run_idx = row["run_index"]
        run_totals[run_idx] = run_totals.get(run_idx, 0.0) + row["duration_ms"]
    
    for row in rows:
        run_idx = row["run_index"]
        total_ms = run_totals.get(run_idx, 0.0)
        row["pct_total"] = (row["duration_ms"] / total_ms * 100.0) if total_ms > 0 else 0.0
    
    return rows


def write_csv(path: Path, rows: List[Dict[str, Any]], fieldnames: List[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=fieldnames)
        w.writeheader()
        for r in rows:
            w.writerow({k: r.get(k) for k in fieldnames})


def aggregate_stats(df) -> List[Dict[str, Any]]:
    # Prefer avg (ms) if present (already aggregated across runs)
    time_col = "avg (ms)" if "avg (ms)" in df.columns else ("avg" if "avg" in df.columns else None)
    if time_col is None:
        return []
    df = df.copy()
    df["op_type"] = df["event_name"].map(lambda x: base_op_type(x) if isinstance(x, str) else x)
    df["backend"] = df.apply(lambda r: choose_backend(r), axis=1)
    total_ms = float(df[time_col].sum()) if time_col in df.columns else 0.0
    g = df.groupby(["op_type", "backend"], dropna=False)[time_col]
    agg = g.agg(["count", "sum", "mean"]).reset_index()
    agg = agg.sort_values("sum", ascending=False)
    rows: List[Dict[str, Any]] = []
    for _, r in agg.iterrows():
        sum_ms = float(r["sum"]) if r["sum"] is not None else 0.0
        pct_total = (sum_ms / total_ms * 100.0) if total_ms > 0 else 0.0
        rows.append(
            {
                "name": r["op_type"],
                "type": r["op_type"],
                "delegate_backend": r["backend"],
                "count": int(r["count"]) if r["count"] is not None else 0,
                "total_ms": sum_ms,
                "avg_ms": float(r["mean"]) if r["mean"] is not None else 0.0,
                "pct_total": pct_total,
            }
        )
    return rows


def run(
    etdump: str,
    etrecord: Optional[str],
    out_dir: str,
    run_index: Optional[int],
    json_out: bool,
    strict_etrecord: bool = False,
    model_id: Optional[str] = None,
    all_runs: bool = False,
) -> None:
    # Attempt to use ETRecord if provided; fall back quietly if deserialization fails unless strict requested.
    try:
        insp = Inspector(
            etdump_path=etdump,
            etrecord=etrecord,
            source_time_scale=TimeScale.NS,
            target_time_scale=TimeScale.MS,
        )
    except Exception as e:
        if etrecord and not strict_etrecord:
            msg = f"[warn] Failed to load etrecord '{etrecord}' ({type(e).__name__}: {e}); continuing without it."
            # Add guidance for common FX/NodeSource version skew
            emsg = str(e)
            if isinstance(e, AttributeError) and ("NodeSource" in emsg or "_from_dict" in emsg or "from_node" in emsg):
                msg += (
                    "\n       Hint: ETRecord/Inspector version skew detected (FX NodeSource). "
                    "Regenerate the .etrecord in the same environment as analysis, "
                    "or rerun without --etrecord. Use --strict-etrecord to fail hard."
                )
            print(msg)
            insp = Inspector(
                etdump_path=etdump,
                etrecord=None,
                source_time_scale=TimeScale.NS,
                target_time_scale=TimeScale.MS,
            )
        else:
            raise
    df = insp.to_dataframe()
    mod_id = model_id or Path(etdump).stem

    out_path = Path(out_dir)
    # Derive prefix (model + experiment) and variant from etdump filename
    etdump_name = Path(etdump).name
    if etdump_name.endswith('.etdump'):
        etdump_stem = etdump_name[:-7]
    else:
        etdump_stem = etdump_name
    variant = 'exec'
    if etdump_stem.endswith('_xtrace'):
        variant = 'xtrace'
        prefix = etdump_stem[:-7]  # remove _xtrace
    else:
        prefix = etdump_stem
    file_prefix = f"{prefix}_{variant}"

    # Stats across runs (aggregated by op_type, backend)
    stats = aggregate_stats(df)
    for r in stats:
        r["model_id"] = mod_id
    stats_path = out_path / f"{file_prefix}_ops_stats.csv"

    # Timeline extraction: single run or all runs
    primary_timeline: List[Dict[str, Any]]
    primary_path: Path

    if all_runs:
        # Extract all runs in one CSV
        timeline_all = extract_all_runs_events(df)
        for r in timeline_all:
            r["model_id"] = mod_id
        timeline_all_path = out_path / f"{file_prefix}_all_runs_timeline.csv"

        write_csv(
            timeline_all_path,
            timeline_all,
            [
                "model_id",
                "name",
                "type",
                "delegate_backend",
                "start_us",
                "end_us",
                "duration_ms",
                "pct_total",
                "node_id",
                "run_index",
                "block",
            ],
        )

        # Additionally emit a run0 timeline for operator analysis convenience
        run0_events = extract_run_events(df, 0)
        if run0_events:
            total_ms = sum((r["duration_ms"] for r in run0_events), 0.0)
            for r in run0_events:
                r["pct_total"] = (r["duration_ms"] / total_ms * 100.0) if total_ms > 0 else 0.0
                r["model_id"] = mod_id
            run0_path = out_path / f"{file_prefix}_run0_timeline.csv"
            write_csv(
                run0_path,
                run0_events,
                [
                    "model_id",
                    "name",
                    "type",
                    "delegate_backend",
                    "start_us",
                    "end_us",
                    "duration_ms",
                    "pct_total",
                    "node_id",
                    "run_index",
                    "block",
                ],
            )
        primary_timeline = timeline_all
        primary_path = timeline_all_path
    else:
        if run_index is None:
            run_index = 0
        timeline = extract_run_events(df, run_index)
        total_ms = sum((r["duration_ms"] for r in timeline), 0.0)
        for r in timeline:
            r["pct_total"] = (r["duration_ms"] / total_ms * 100.0) if total_ms > 0 else 0.0
            r["model_id"] = mod_id
        timeline_path = out_path / f"{file_prefix}_run{run_index}_timeline.csv"
        write_csv(
            timeline_path,
            timeline,
            [
                "model_id",
                "name",
                "type",
                "delegate_backend",
                "start_us",
                "end_us",
                "duration_ms",
                "pct_total",
                "node_id",
                "run_index",
                "block",
            ],
        )
        primary_timeline = timeline
        primary_path = timeline_path
    write_csv(
        stats_path,
        stats,
        [
            "model_id",
            "name",
            "type",
            "delegate_backend",
            "count",
            "total_ms",
            "avg_ms",
            "pct_total",
        ],
    )

    if json_out:
        if all_runs:
            json_path = out_path / f"{file_prefix}_all_runs_timeline.json"
        else:
            json_path = out_path / f"{file_prefix}_run{run_index}_timeline.json"
        json_path.write_text(
            json.dumps(primary_timeline, indent=2), encoding="utf-8"
        )
        (out_path / f"{file_prefix}_ops_stats.json").write_text(
            json.dumps(stats, indent=2), encoding="utf-8"
        )

    print(f"Wrote timeline: {primary_path}")
    print(f"Wrote stats:    {stats_path}")


def main():
    ap = argparse.ArgumentParser(
        description=(
            "Convert ExecuTorch ETDump to readable CSV/JSON: per-run timeline and aggregated op stats."
        )
    )
    ap.add_argument("--etdump", required=True, help="Path to .etdump")
    ap.add_argument("--etrecord", help="Optional path to .etrecord for enriched metadata")
    ap.add_argument("--out-dir", required=True, help="Output directory for CSV/JSON")
    ap.add_argument(
        "--run-index",
        type=int,
        default=0,
        help="Run index for timeline extraction (default: 0). Ignored if --all-runs is used.",
    )
    ap.add_argument(
        "--all-runs",
        action="store_true",
        help="Export all runs in a single CSV file with run_index column. Overrides --run-index.",
    )
    ap.add_argument("--json", action="store_true", help="Also output JSON alongside CSV")
    ap.add_argument(
        "--strict-etrecord",
        action="store_true",
        help="Fail instead of falling back if provided --etrecord cannot be read",
    )
    ap.add_argument("--model-id", help="Optional model identifier to embed; defaults to etdump filename stem")
    args = ap.parse_args()

    run(
        args.etdump,
        args.etrecord,
        args.out_dir,
        args.run_index if not args.all_runs else None,
        args.json,
        strict_etrecord=args.strict_etrecord,
        model_id=args.model_id,
        all_runs=args.all_runs,
    )


if __name__ == "__main__":
    main()
