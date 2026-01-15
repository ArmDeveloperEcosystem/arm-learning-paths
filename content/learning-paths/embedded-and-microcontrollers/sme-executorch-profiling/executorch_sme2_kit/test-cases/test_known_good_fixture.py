#!/usr/bin/env python3
from __future__ import annotations

import json
import shutil
import subprocess
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "test-cases" / "fixtures" / "known_good_mac"


def run(cmd: list[str], *, cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, cwd=str(cwd), text=True, capture_output=True)


def test_known_good_fixture_validates() -> None:
    assert FIXTURE.exists()

    with tempfile.TemporaryDirectory() as td:
        work = Path(td) / "kit"
        shutil.copytree(FIXTURE, work)

        # validate_results expects a run dir that contains manifest.json + metrics.json + at least one .etdump under it
        # The fixture mimics the output layout under work/runs/mac/...
        p = run(
            ["python", "scripts/validate_results.py", "--results", str(work / "runs" / "mac")],
            cwd=ROOT,
        )
        assert p.returncode == 0, p.stdout + "\n" + p.stderr

        manifest = json.loads((work / "runs" / "mac" / "manifest.json").read_text(encoding="utf-8"))
        assert "executorch" in manifest

        summary = json.loads((work / "runs" / "mac" / "analysis_summary.json").read_text(encoding="utf-8"))
        assert "category_totals_ms" in summary
        assert "per_etdump" in summary

        # Compare against itself (schema-level). This is the critical “agent test case”:
        # the agent should be able to produce a run dir that matches this structure.
        p2 = run(
            [
                "python",
                "scripts/compare_run_to_known_good.py",
                "--run-dir",
                str(work / "runs" / "mac"),
                "--fixture-dir",
                str(work / "runs" / "mac"),
            ],
            cwd=ROOT,
        )
        assert p2.returncode == 0, p2.stdout + "\n" + p2.stderr


if __name__ == "__main__":
    test_known_good_fixture_validates()
    print("OK")


