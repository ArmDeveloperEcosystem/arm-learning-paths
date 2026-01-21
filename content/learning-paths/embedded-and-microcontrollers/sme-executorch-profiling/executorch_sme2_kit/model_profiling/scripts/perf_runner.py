#!/usr/bin/env python3
"""
Perf Runner: simple one-thread performance driver for ExecuTorch .pte models

Goals
- One run = one CPU thread value (no ranges or lists to parse).
- Do timing, and optionally XNNPACK verbose trace and xctrace, for that thread.
- Mirror run_pte_ab_v2.sh naming with t{threads} in filenames.

Examples
  # Timing + traces for t=4
  python model_profiling/scripts/perf_runner.py \
    --model model_profiling/out_edgetam/export_memory_attention_real/edgetam_memory_attention_xnnpack_fp32.pte \
    --quiet-runner ./cmake-out/release-base/executor_runner \
    --verbose-runner ./cmake-out/release-base-xnnlogging/executor_runner \
    --threads 4 --exp base --warmup 10 --timing-runs 100

  # Timing only for t=1 (skip traces)
  python model_profiling/scripts/perf_runner.py \
    --model .../model.pte --quiet-runner ./executor_runner --threads 1 --no-xnntrace --no-xtrace
"""

from __future__ import annotations

import argparse
import os
import re
import subprocess
import sys
import time
from pathlib import Path
from typing import List, Optional, Tuple


def _time_to_seconds(val: float, unit: str) -> float:
    unit = unit.lower()
    if unit in ('s', 'sec', 'secs', 'second', 'seconds'):
        return float(val)
    if unit in ('ms', 'msec', 'msecs', 'millisecond', 'milliseconds'):
        return float(val) / 1000.0
    if unit in ('us', 'usec', 'usecs', 'microsecond', 'microseconds'):
        return float(val) / 1_000_000.0
    return float(val)


def parse_runner_times(log_path: Path) -> Tuple[Optional[float], Optional[float]]:
    """Best-effort parse of runner-reported total/average times from a log.

    Returns (runner_total_sec, runner_avg_sec) or (None, None) if not found.
    """
    try:
        if not log_path.exists():
            return None, None
        text = log_path.read_text(errors='ignore')
    except Exception:
        return None, None
    total_sec: Optional[float] = None
    avg_sec: Optional[float] = None
    lines = text.splitlines()
    # First, try to match the executor_runner summary line
    for line in reversed(lines):
        m0 = re.search(r"model executed successfully\s+(\d+)\s+time\(s\)\s+in\s+([0-9]+(?:\.[0-9]+)?)\s*ms", line, flags=re.IGNORECASE)
        if m0:
            runs = int(m0.group(1))
            ms_total = float(m0.group(2))
            total_sec = ms_total / 1000.0
            avg_sec = total_sec / max(1, runs)
            return total_sec, avg_sec
    # Fallback: scan for generic total/avg tokens
    for line in reversed(lines):
        low = line.lower()
        m = re.search(r'([0-9]+(?:\.[0-9]+)?)\s*(ms|us|s)\b', low)
        if not m:
            continue
        sec = _time_to_seconds(float(m.group(1)), m.group(2))
        if total_sec is None and ('total' in low or 'sum' in low):
            total_sec = sec
        if avg_sec is None and ('avg' in low or 'average' in low):
            avg_sec = sec
        if total_sec is not None and avg_sec is not None:
            break
    return total_sec, avg_sec


def timing_run(cmd: List[str], env: Optional[dict], log_path: Path, cwd: Optional[Path] = None) -> Tuple[int, float, float]:
    """Run a command, capturing wall time. Returns (rc, total_sec, avg_sec_per_exec)."""
    start = time.time()
    rc = 0
    with log_path.open('w') as f:
        try:
            result = subprocess.run(cmd, stdout=f, stderr=subprocess.STDOUT, env=env, check=True, cwd=cwd)
            rc = result.returncode
        except subprocess.CalledProcessError as e:
            rc = e.returncode
            # Write error info to log
            f.write(f"\nCommand failed with exit code {rc}\n")
            f.write(f"Command: {' '.join(cmd)}\n")
            if cwd:
                f.write(f"Working directory: {cwd}\n")
        except Exception as e:
            rc = -1
            f.write(f"\nUnexpected error: {e}\n")
            f.write(f"Command: {' '.join(cmd)}\n")
    end = time.time()
    # Extract num_executions from cmd
    try:
        idx = cmd.index('--num_executions')
        num_exec = int(cmd[idx + 1])
    except Exception:
        num_exec = 1
    total = end - start
    avg = total / max(1, num_exec)
    return rc, total, avg


def run_warmup(quiet_runner: Path, model: Path, threads: int, warmup: int, xnn_log_level: int, cwd: Optional[Path] = None) -> int:
    if warmup <= 0:
        return 0
    env = os.environ.copy()
    env['XNN_LOG_LEVEL'] = str(xnn_log_level)
    cmd = [str(quiet_runner), '--model_path', str(model), '--num_executions', str(warmup), '--cpu_threads', str(threads)]
    try:
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, env=env, check=True, cwd=cwd)
        return 0
    except subprocess.CalledProcessError as e:
        return e.returncode


def main() -> int:
    p = argparse.ArgumentParser(description='Simple one-thread performance runner for ExecuTorch .pte models')
    p.add_argument('--model', required=True, help='Path to .pte model')
    p.add_argument('--quiet-runner', required=True, help='Path to base executor_runner')
    p.add_argument('--verbose-runner', default=None, help='Path to verbose executor_runner for XNNPACK logging')
    p.add_argument('--exp', default='base', help='Experiment tag used in filenames')
    p.add_argument('--outdir', default=None, help='Optional override for outputs directory (default: alongside model)')
    p.add_argument('--mode', choices=['timing', 'xnntrace', 'xtrace'], default='timing', help='Which scenario to run')
    p.add_argument('--threads', type=int, default=1, help='CPU threads for this run')
    p.add_argument('--warmup', type=int, default=10, help='Warmup iterations (always runs)')
    p.add_argument('--timing-runs', type=int, default=100, help='Execution iterations for timing')
    p.add_argument('--output', dest='output', action='store_true', help='Write outputs (logs/trace/etdump) with auto naming')
    p.add_argument('--no-output', dest='output', action='store_false', help='Do not write outputs (print summary only)')
    p.set_defaults(output=True)
    # xtrace controls
    p.add_argument('--xtrace-template', default='Time Profiler', help='xctrace template')
    p.add_argument('--xtrace-target-sec', type=float, default=10.0, help='Target seconds for xctrace auto scaling')
    p.add_argument('--xtrace-min-exec', type=int, default=10)
    p.add_argument('--xtrace-max-exec', type=int, default=400)
    p.add_argument('--xtrace-execs', type=int, default=0, help='If > 0, override auto scaling and use this many executions')
    args = p.parse_args()

    model = Path(args.model).resolve()
    quiet_runner = Path(args.quiet_runner).resolve()
    verbose_runner = Path(args.verbose_runner).resolve() if args.verbose_runner else None
    if not model.exists():
        print(f"❌ Model not found: {model}", file=sys.stderr)
        return 1
    if not quiet_runner.exists():
        print(f"❌ Quiet runner not found: {quiet_runner}", file=sys.stderr)
        return 1
    if args.mode == 'xnntrace' and (verbose_runner is None or not verbose_runner.exists()):
        print("❌ Verbose runner not found; provide --verbose-runner for xnntrace mode.", file=sys.stderr)
        return 1

    outdir = Path(args.outdir).resolve() if args.outdir else model.parent.parent / "results"
    outdir.mkdir(parents=True, exist_ok=True)
    stem = model.stem

    t = int(args.threads)
    # Determine working directory - use executorch directory if runner is in executorch
    cwd = None
    if 'executorch' in str(quiet_runner):
        # Runner is in executorch, so run from executorch directory
        # Find executorch directory by walking up the path
        current = quiet_runner.parent
        while current != current.parent:  # Stop at root
            if current.name == 'executorch':
                cwd = current
                break
            current = current.parent
    # warmup
    rc = run_warmup(quiet_runner, model, t, args.warmup, xnn_log_level=0, cwd=cwd)
    if rc != 0:
        print(f"[WARN] Warmup failed for t={t} (rc={rc})")

    # Compute paths (or temp files when no-output)
    if args.mode == 'timing':
        lat_log = outdir / f"{stem}_{args.exp}_t{t}_latency.log" if args.output else outdir / f"{stem}_{args.exp}_t{t}_latency.tmp.log"
    else:
        lat_log = Path('/dev/null')
    xnntrace_log = outdir / f"{stem}_{args.exp}_t{t}_xnntrace.log" if args.output and args.mode == 'xnntrace' else Path('/dev/null')
    xtrace_path = outdir / f"{stem}_{args.exp}_t{t}_xctrace.trace" if args.output and args.mode == 'xtrace' else outdir / f"{stem}_{args.exp}_t{t}_xctrace.tmp.trace"
    etdump_exec = outdir / f"{stem}_{args.exp}_t{t}.etdump" if args.output and args.mode == 'timing' else None
    etdump_xtrace = outdir / f"{stem}_{args.exp}_t{t}_xtrace.etdump" if args.output and args.mode == 'xtrace' else None

    avg = 0.0
    if args.mode == 'timing':
        env = os.environ.copy(); env['XNN_LOG_LEVEL'] = '0'
        cmd = [str(quiet_runner), '--model_path', str(model), '--num_executions', str(args.timing_runs), '--cpu_threads', str(t)]
        if etdump_exec:
            cmd.extend(['--etdump_path', str(etdump_exec)])
        rc, total, avg = timing_run(cmd, env, lat_log, cwd=cwd)
        if rc != 0:
            print(f"❌ Timing failed for t={t}; see {lat_log}")
            return rc
        # Parse runner totals/averages if present
        run_total, run_avg = parse_runner_times(lat_log)
        rt = f" runner_total={run_total:.6f}s" if run_total is not None else ""
        ra = f" runner_avg={run_avg:.6f}s" if run_avg is not None else ""
        print(f"[Timing] t={t} runs={args.timing_runs} wall_total={total:.3f}s wall_avg={avg:.6f}s{rt}{ra}  → {lat_log if args.output else '(no-output)'}")
        
        # Add summary to latency log
        if args.output and lat_log.exists():
            with lat_log.open('a') as f:
                f.write("\n")
                f.write("=========================================\n")
                f.write("PERFORMANCE SUMMARY\n")
                f.write("=========================================\n")
                f.write(f"Experiment:              {args.exp}\n")
                f.write(f"Model:                   {model.name}\n")
                f.write(f"Warmup Iterations:       {args.warmup}\n")
                f.write(f"Execution Iterations:    {args.timing_runs}\n")
                f.write(f"Execution Total Wall:    {total:.6f}s\n")
                f.write(f"Execution Total Runner:  {run_total:.6f}s\n" if run_total is not None else "Execution Total Runner:  N/A\n")
                f.write(f"Avg Wall/Run:            {avg:.6f}s\n")
                f.write(f"Avg Runner/Run:          {run_avg:.6f}s\n" if run_avg is not None else "Avg Runner/Run:          N/A\n")
                f.write(f"CPU Threads:             {t}\n")
                f.write(f"Quiet Runner:            {quiet_runner.name}\n")
                f.write(f"Model Size:              {model.stat().st_size / 1024 / 1024:.1f} MB\n")
                f.write(f"Execution ETDump Path:   {etdump_exec}\n" if etdump_exec else "Execution ETDump Path:   N/A\n")
                f.write("=========================================\n")
                f.write("Guidance: Wall timing includes process overhead. Runner timing is more accurate for model execution time.\n")
        
        # Clean temp log if no-output
        if not args.output and lat_log.exists():
            try:
                lat_log.unlink()
            except Exception:
                pass

    elif args.mode == 'xnntrace':
        env = os.environ.copy(); env['XNN_LOG_LEVEL'] = '5'
        cmd = [str(verbose_runner), '--model_path', str(model), '--num_executions', '1', '--cpu_threads', str(t)]
        rc, _, _ = timing_run(cmd, env, xnntrace_log, cwd=cwd)
        if rc != 0:
            print(f"❌ XNNPACK trace failed for t={t}; see {xnntrace_log if args.output else '(no log)'}")
            return rc
        print(f"[XNNTRACE] t={t} → {xnntrace_log if args.output else '(no-output)'}")

    else:  # xtrace
        # If we don't have avg from timing, probe a single run
        env = os.environ.copy(); env['XNN_LOG_LEVEL'] = '0'
        if avg <= 0:
            probe_cmd = [str(quiet_runner), '--model_path', str(model), '--num_executions', '1', '--cpu_threads', str(t)]
            probe_log = outdir / f"{stem}_{args.exp}_t{t}_probe.log"
            _, total_probe, _ = timing_run(probe_cmd, env, probe_log, cwd=cwd)
            avg = max(1e-3, total_probe)
            if not args.output and probe_log.exists():
                try: probe_log.unlink()
                except Exception: pass
        n_exec = args.xtrace_execs if args.xtrace_execs > 0 else max(args.xtrace_min_exec, min(args.xtrace_max_exec, int(args.xtrace_target_sec / avg + 0.999)))
        cmd = [
            'xctrace', 'record', '--template', args.xtrace_template,
            '--output', str(xtrace_path), '--launch', '--',
            str(quiet_runner), '--model_path', str(model), '--num_executions', str(n_exec), '--cpu_threads', str(t)
        ]
        if etdump_xtrace:
            cmd.extend(['--etdump_path', str(etdump_xtrace)])
        print(f"[XTRACE] t={t} execs={n_exec} target~{args.xtrace_target_sec:.1f}s → {xtrace_path if args.output else '(temp)'}")
        try:
            subprocess.run(cmd, env=env, check=True)
        except subprocess.CalledProcessError as e:
            print(f"❌ xctrace failed for t={t} (rc={e.returncode})")
            return e.returncode
        if not args.output:
            try:
                if xtrace_path.exists(): xtrace_path.unlink()
                if etdump_xtrace and Path(etdump_xtrace).exists(): Path(etdump_xtrace).unlink()
            except Exception:
                pass

    print("Done.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
