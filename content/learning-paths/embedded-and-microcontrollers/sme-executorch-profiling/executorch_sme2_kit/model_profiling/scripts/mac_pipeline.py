#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


ROOT = Path(__file__).resolve().parents[2]  # executorch_sme2_kit/model_profiling/scripts/ -> executorch_sme2_kit/
EXECUTORCH_DIR = ROOT / "executorch"


LAT_RE = re.compile(r"Model executed successfully.*?in\s+([0-9.]+)\s+ms", re.IGNORECASE)


def run_cmd(cmd: List[str], *, cwd: Optional[Path] = None) -> str:
    print("+", " ".join(cmd))
    p = subprocess.run(cmd, cwd=str(cwd) if cwd else None, capture_output=True, text=True)
    out = (p.stdout or "") + "\n" + (p.stderr or "")
    if p.returncode != 0:
        raise RuntimeError(f"Command failed ({p.returncode}): {' '.join(cmd)}\n{out}")
    return out


def parse_latency_ms(output: str) -> Optional[float]:
    m = LAT_RE.search(output)
    if not m:
        return None
    return float(m.group(1))


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def executorch_git_info() -> Dict[str, Any]:
    if not EXECUTORCH_DIR.exists():
        return {"present": False}
    try:
        sha = (
            subprocess.check_output(["git", "-C", str(EXECUTORCH_DIR), "rev-parse", "HEAD"])
            .decode("utf-8")
            .strip()
        )
        # Treat the checkout as "dirty" only if tracked files are modified.
        # Build outputs commonly create untracked files (cmake-out/), which should not mark runs as dirty.
        dirty = False
        try:
            subprocess.check_call(["git", "-C", str(EXECUTORCH_DIR), "diff", "--quiet"])
            subprocess.check_call(["git", "-C", str(EXECUTORCH_DIR), "diff", "--cached", "--quiet"])
        except subprocess.CalledProcessError:
            dirty = True
        return {"present": True, "sha": sha, "dirty": dirty}
    except Exception:
        return {"present": True, "sha": None, "dirty": None}


def run_experiment(
    *,
    name: str,
    runner: Path,
    model: Path,
    out_dir: Path,
    threads: int,
    runs: int,
) -> Dict[str, Any]:
    out_dir.mkdir(parents=True, exist_ok=True)
    etdump = out_dir / f"{name}_t{threads}.etdump"
    logfile = out_dir / f"{name}_t{threads}.log"

    latencies: List[float] = []
    for i in range(runs):
        # Write ETDump each time (overwrite) — enough to keep a representative trace.
        cmd = [
            str(runner),
            f"-model_path={model}",
            f"-etdump_path={etdump}",
            "-num_executions=1",
            f"-cpu_threads={threads}",
        ]
        t0 = time.perf_counter()
        output = run_cmd(cmd)
        t1 = time.perf_counter()
        latencies.append((t1 - t0) * 1000.0)
        logfile.write_text(output, encoding="utf-8")

    metrics = {
        "runs": runs,
        "threads": threads,
        "latency_ms": latencies,
        "median_ms": (sorted(latencies)[len(latencies) // 2] if latencies else None),
        "min_ms": (min(latencies) if latencies else None),
        "max_ms": (max(latencies) if latencies else None),
        # Keep absolute paths for debugging, but also write run-root-relative paths for portability.
        "etdump": str(etdump),
        "log": str(logfile),
    }
    return metrics


def main() -> None:
    ap = argparse.ArgumentParser(description="Run the macOS profiling pipeline (ExecuTorch executor_runner).")
    ap.add_argument("--config", type=Path, required=True)
    args = ap.parse_args()

    cfg = load_json(args.config)
    model = Path(cfg["model"]).resolve()
    out_root = Path(cfg["output_root"]).resolve()
    experiments = cfg.get("experiments", [])

    run_root = out_root
    run_root.mkdir(parents=True, exist_ok=True)

    manifest: Dict[str, Any] = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "config": str(args.config.resolve()),
        "model": str(model),
        "executorch": executorch_git_info(),
        "run_root": str(run_root),
        "results": [],
    }

    for exp in experiments:
        name = exp["name"]
        runner = Path(exp["runner_path"]).resolve()
        runs = int(exp.get("runs", 10))
        threads_list = [int(t) for t in exp.get("threads", [1])]

        exp_dir = run_root / name
        for threads in threads_list:
            metrics = run_experiment(
                name=name,
                runner=runner,
                model=model,
                out_dir=exp_dir,
                threads=threads,
                runs=runs,
            )
            # Add relative paths to make the output stable across machines and usable in fixtures.
            try:
                metrics["etdump_rel"] = str(Path(metrics["etdump"]).resolve().relative_to(run_root))
            except Exception:
                metrics["etdump_rel"] = None
            try:
                metrics["log_rel"] = str(Path(metrics["log"]).resolve().relative_to(run_root))
            except Exception:
                metrics["log_rel"] = None
            manifest["results"].append({"experiment": name, "metrics": metrics})

    write_json(run_root / "manifest.json", manifest)
    write_json(run_root / "metrics.json", {"results": manifest["results"]})
    print(f"Wrote: {run_root / 'manifest.json'}")
    print(f"Wrote: {run_root / 'metrics.json'}")
    print("Next: python model_profiling/scripts/analyze_results.py --run-dir", str(run_root))


if __name__ == "__main__":
    main()


