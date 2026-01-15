#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import subprocess
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional


ROOT = Path(__file__).resolve().parents[2]  # executorch_sme2_kit/model_profiling/scripts/ -> executorch_sme2_kit/
EXECUTORCH_DIR = ROOT / "executorch"

LAT_RE = re.compile(r"Average execution time:\s*([0-9.]+)\s*ms", re.IGNORECASE)


def run_cmd(cmd: List[str], *, cwd: Optional[Path] = None) -> str:
    print("+", " ".join(cmd))
    p = subprocess.run(cmd, cwd=str(cwd) if cwd else None, capture_output=True, text=True)
    out = (p.stdout or "") + "\n" + (p.stderr or "")
    if p.returncode != 0:
        raise RuntimeError(f"Command failed ({p.returncode}): {' '.join(cmd)}\n{out}")
    return out


def adb_base(serial: Optional[str]) -> List[str]:
    return ["adb", "-s", serial] if serial else ["adb"]


def executorch_git_info() -> Dict[str, Any]:
    if not EXECUTORCH_DIR.exists():
        return {"present": False}
    try:
        sha = (
            subprocess.check_output(["git", "-C", str(EXECUTORCH_DIR), "rev-parse", "HEAD"])
            .decode("utf-8")
            .strip()
        )
        dirty = bool(
            subprocess.check_output(["git", "-C", str(EXECUTORCH_DIR), "status", "--porcelain"])
            .decode("utf-8")
            .strip()
        )
        return {"present": True, "sha": sha, "dirty": dirty}
    except Exception:
        return {"present": True, "sha": None, "dirty": None}


def load_json(path: Path) -> Dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def parse_avg_latency_ms(output: str) -> Optional[float]:
    m = LAT_RE.search(output)
    if not m:
        return None
    return float(m.group(1))


def push_dir_shared_libs(adb: List[str], runner_dir: Path, device_dir: str) -> None:
    for so in sorted(runner_dir.glob("*.so")):
        run_cmd([*adb, "push", str(so), f"{device_dir}/{so.name}"])


def main() -> None:
    ap = argparse.ArgumentParser(description="Run profiling on an Android device and pull ETDump traces back to host.")
    ap.add_argument("--config", type=Path, required=True)
    ap.add_argument("--serial", default=None, help="Optional: adb device serial")
    ap.add_argument("--device-dir", default="/data/local/tmp/sme2_profiling")
    args = ap.parse_args()

    cfg = load_json(args.config)
    model = Path(cfg["model"]).resolve()
    out_root = Path(cfg["output_root"]).resolve()
    experiments = cfg.get("experiments", [])

    adb = adb_base(args.serial)
    run_cmd([*adb, "shell", "mkdir", "-p", args.device_dir])

    # Device facts for the manifest (best-effort)
    abi = run_cmd([*adb, "shell", "getprop", "ro.product.cpu.abi"]).strip()
    model_name = run_cmd([*adb, "shell", "getprop", "ro.product.model"]).strip()
    soc = run_cmd([*adb, "shell", "getprop", "ro.soc.model"]).strip()

    # Push model (pte) only; etrecord stays on host for analysis correlation.
    run_cmd([*adb, "push", str(model), f"{args.device_dir}/model.pte"])

    out_root.mkdir(parents=True, exist_ok=True)

    manifest: Dict[str, Any] = {
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "config": str(args.config.resolve()),
        "model": str(model),
        "executorch": executorch_git_info(),
        "run_root": str(out_root),
        "device": {"serial": args.serial, "model": model_name, "abi": abi, "soc": soc},
        "results": [],
    }

    for exp in experiments:
        name = exp["name"]
        runner = Path(exp["runner_path"]).resolve()
        threads_list = [int(t) for t in exp.get("threads", [1])]
        runs = int(exp.get("runs", 10))

        exp_dir = out_root / name
        exp_dir.mkdir(parents=True, exist_ok=True)

        # Push runner + shared libs from its directory if present
        runner_dir = runner.parent
        device_runner = f"{args.device_dir}/executor_runner"
        run_cmd([*adb, "push", str(runner), device_runner])
        push_dir_shared_libs(adb, runner_dir, args.device_dir)
        run_cmd([*adb, "shell", "chmod", "755", device_runner])

        for threads in threads_list:
            etdump_remote = f"{args.device_dir}/{name}_t{threads}.etdump"
            etdump_local = exp_dir / f"{name}_t{threads}.etdump"
            logfile = exp_dir / f"{name}_t{threads}.log"

            latencies: List[float] = []
            for _ in range(runs):
                cmd = (
                    f"cd {args.device_dir} && "
                    f"export LD_LIBRARY_PATH={args.device_dir}:$LD_LIBRARY_PATH && "
                    f"./executor_runner "
                    f"-model_path=model.pte "
                    f"-num_executions=1 "
                    f"-cpu_threads={threads} "
                    f"-etdump_path={etdump_remote}"
                )
                out = run_cmd([*adb, "shell", cmd])
                logfile.write_text(out, encoding="utf-8")
                lat = parse_avg_latency_ms(out)
                if lat is not None:
                    latencies.append(lat)

            # Pull ETDump once (last run’s trace is representative enough)
            run_cmd([*adb, "pull", etdump_remote, str(etdump_local)])

            manifest["results"].append(
                {
                    "experiment": name,
                    "metrics": {
                        "runs": runs,
                        "threads": threads,
                        "avg_latency_ms": latencies,
                        "etdump": str(etdump_local),
                        "log": str(logfile),
                        # Also keep portable, run-root-relative paths.
                        "etdump_rel": str(etdump_local.relative_to(out_root)),
                        "log_rel": str(logfile.relative_to(out_root)),
                    },
                }
            )

    write_json(out_root / "manifest.json", manifest)
    write_json(out_root / "metrics.json", {"results": manifest["results"]})
    print(f"Wrote: {out_root / 'manifest.json'}")
    print(f"Wrote: {out_root / 'metrics.json'}")
    print(f"Next: python model_profiling/scripts/analyze_results.py --run-dir {out_root}")


if __name__ == "__main__":
    main()


