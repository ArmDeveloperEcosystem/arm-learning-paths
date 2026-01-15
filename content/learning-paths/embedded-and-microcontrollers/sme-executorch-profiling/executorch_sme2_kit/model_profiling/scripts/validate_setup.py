#!/usr/bin/env python3
from __future__ import annotations

import argparse
import platform
import shutil
import sys
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]  # executorch_sme2_kit/model_profiling/scripts/ -> executorch_sme2_kit/


def check(condition: bool, ok: str, fail: str) -> bool:
    if condition:
        print(f"✅ {ok}")
        return True
    print(f"❌ {fail}")
    return False


def main() -> int:
    ap = argparse.ArgumentParser(description="Validate SME2 profiling kit setup.")
    ap.add_argument("--model", type=Path, default=None, help="Optional: validate a .pte model path exists")
    args = ap.parse_args()

    all_ok = True

    all_ok &= check(sys.version_info >= (3, 9), "Python >= 3.9", f"Python too old: {sys.version.split()[0]}")

    all_ok &= check(shutil.which("git") is not None, "git available", "git not found")
    all_ok &= check(shutil.which("cmake") is not None, "cmake available", "cmake not found (install CMake 3.29+)")

    is_arm64 = platform.machine() in ("arm64", "aarch64")
    all_ok &= check(is_arm64, f"host arch: {platform.machine()}", "expected arm64 host for best experience")

    venv_ok = (ROOT / ".venv").exists()
    all_ok &= check(venv_ok, ".venv exists", "missing .venv (run model_profiling/scripts/setup_repo.sh)")

    executorch_dir = ROOT / "executorch"
    all_ok &= check(executorch_dir.exists(), "executorch checkout exists", "missing executorch/ (run model_profiling/scripts/setup_repo.sh)")

    if executorch_dir.exists():
        try:
            sha = (
                subprocess.check_output(["git", "-C", str(executorch_dir), "rev-parse", "HEAD"])
                .decode("utf-8")
                .strip()
            )
            # Only consider tracked changes as "dirty". Untracked build artifacts are expected.
            dirty = False
            try:
                subprocess.check_call(["git", "-C", str(executorch_dir), "diff", "--quiet"])
                subprocess.check_call(["git", "-C", str(executorch_dir), "diff", "--cached", "--quiet"])
            except subprocess.CalledProcessError:
                dirty = True
            print(f"ℹ️  ExecuTorch SHA: {sha}{' (dirty)' if dirty else ''}")
        except Exception:
            print("⚠️  Could not read ExecuTorch git SHA (is executorch/ a git checkout?)")

    try:
        import executorch  # noqa: F401

        all_ok &= check(True, "ExecuTorch import ok", "ExecuTorch import failed")
    except Exception as exc:
        all_ok &= check(False, "ExecuTorch import ok", f"ExecuTorch import failed: {exc}")

    if args.model is not None:
        all_ok &= check(args.model.exists(), f"model exists: {args.model}", f"model not found: {args.model}")

        etrecord = Path(str(args.model) + ".etrecord")
        all_ok &= check(etrecord.exists(), f"etrecord exists: {etrecord}", f"etrecord not found: {etrecord}")

    # Check for runners in executorch/cmake-out/ (runners stay with their ExecuTorch version)
    executorch_dir = ROOT / "executorch"
    runners_ok = (executorch_dir / "cmake-out" / "mac-arm64" / "executor_runner").exists() or \
                 (executorch_dir / "cmake-out" / "mac-arm64-sme2-off" / "executor_runner").exists()
    all_ok &= check(runners_ok, "runners built in executorch/cmake-out/", "runners missing (run model_profiling/scripts/build_runners.sh)")

    build_script = ROOT / "model_profiling" / "scripts" / "build_runners.sh"
    all_ok &= check(build_script.exists(), "model_profiling/scripts/build_runners.sh exists", "missing model_profiling/scripts/build_runners.sh")

    return 0 if all_ok else 1


if __name__ == "__main__":
    raise SystemExit(main())


