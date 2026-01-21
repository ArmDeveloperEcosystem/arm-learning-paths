#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from model_profiling.pipeline import PipelineOrchestrator, load_pipeline_config
from model_profiling.pipeline.mac_runner import MacRunner


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="ExecuTorch macOS (M-series) performance pipeline.")
    parser.add_argument("--config", required=True, type=Path, help="Path to pipeline JSON config.")
    parser.add_argument("--only", nargs="*", help="Run only specific experiments.")
    parser.add_argument("--analysis-only", action="store_true", help="Skip execution, re-run analysis.")
    parser.add_argument("--verbose", action="store_true")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = load_pipeline_config(args.config)
    runner = MacRunner()
    orchestrator = PipelineOrchestrator(config, runner, verbose=args.verbose)
    orchestrator.execute(only=args.only, analysis_only=args.analysis_only)


if __name__ == "__main__":
    main()
