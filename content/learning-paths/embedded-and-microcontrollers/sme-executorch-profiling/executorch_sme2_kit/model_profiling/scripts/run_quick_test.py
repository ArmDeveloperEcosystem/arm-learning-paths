#!/usr/bin/env python3
from __future__ import annotations

import argparse
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]  # executorch_sme2_kit/model_profiling/scripts/ -> executorch_sme2_kit/


def run(cmd: list[str]) -> None:
    print("+", " ".join(cmd))
    subprocess.check_call(cmd)


def main() -> None:
    ap = argparse.ArgumentParser(description="Quick smoke test for the SME2 profiling kit.")
    ap.add_argument("--platform", choices=["mac"], default="mac")
    args = ap.parse_args()

    # 1) Validate setup
    run(["python", "model_profiling/scripts/validate_setup.py"])

    # 2) Build runners (shell orchestration)
    run(["bash", "model_profiling/scripts/build_runners.sh"])

    # 3) Export a tiny model
    model_name = "toy_cnn"
    artifacts_dir = ROOT / f"out_{model_name}" / "artifacts"
    artifacts_dir.mkdir(parents=True, exist_ok=True)
    run(["python", "model_profiling/export/export_model.py", "--model", model_name, "--dtype", "fp16", "--outdir", str(artifacts_dir)])
    # Export script creates: toy_cnn_xnnpack_fp16.pte
    model = artifacts_dir / "toy_cnn_xnnpack_fp16.pte"

    # 4) Write a minimal config by copying the template and patching paths
    cfg = ROOT / "model_profiling" / "configs" / "quick_mac.json"
    cfg.parent.mkdir(parents=True, exist_ok=True)
    template = ROOT / "model_profiling" / "configs" / "templates" / "mac_template.json"
    text = template.read_text(encoding="utf-8")
    text = text.replace("REPLACE_WITH_PATH_TO_MODEL_PTE", str(model))
    text = text.replace("out_<model>", f"out_{model_name}")
    cfg.write_text(text, encoding="utf-8")

    # 5) Run pipeline
    run(["python", "model_profiling/scripts/mac_pipeline.py", "--config", str(cfg)])

    # 6) Validate results
    run(["python", "model_profiling/scripts/validate_results.py", "--results", str(ROOT / f"out_{model_name}" / "runs" / args.platform)])

    print("\n✅ Quick test completed.")


if __name__ == "__main__":
    main()


