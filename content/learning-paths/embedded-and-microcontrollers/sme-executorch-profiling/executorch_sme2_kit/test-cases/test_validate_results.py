#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=str(ROOT), text=True, capture_output=True)


def test_validate_results_passes_on_minimal_layout() -> None:
    with tempfile.TemporaryDirectory() as td:
        run_dir = Path(td) / "runs" / "mac"
        run_dir.mkdir(parents=True, exist_ok=True)

        (run_dir / "manifest.json").write_text(
            json.dumps({"model": "models/x.pte", "results": []}, indent=2) + "\n", encoding="utf-8"
        )
        (run_dir / "metrics.json").write_text(json.dumps({"results": []}) + "\n", encoding="utf-8")
        # at least one etdump somewhere under run_dir
        (run_dir / "mac_sme2_on").mkdir(parents=True, exist_ok=True)
        (run_dir / "mac_sme2_on" / "x.etdump").write_text("dummy", encoding="utf-8")

        p = run(["python", "scripts/validate_results.py", "--results", str(run_dir)])
        assert p.returncode == 0, p.stdout + "\n" + p.stderr


if __name__ == "__main__":
    test_validate_results_passes_on_minimal_layout()
    print("OK")


