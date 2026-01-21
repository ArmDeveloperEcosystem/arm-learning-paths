#!/usr/bin/env python3
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from model_profiling.pipeline import PipelineOrchestrator, load_pipeline_config
from model_profiling.pipeline.android_runner import AndroidRunner, AndroidRunnerSettings


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="ExecuTorch Android performance pipeline.")
    parser.add_argument("--config", required=True, type=Path, help="Path to pipeline JSON config.")
    parser.add_argument("--only", nargs="*", help="Run only the specified experiments.")
    parser.add_argument("--analysis-only", action="store_true", help="Skip execution, re-run analysis.")
    parser.add_argument("--verbose", action="store_true", help="Verbose logging.")
    parser.add_argument("--remote-device", type=str, help="Remote device address (e.g., '10.1.16.56:5555') for ADB connection.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    config = load_pipeline_config(args.config)
    
    # Create AndroidRunner with optional remote device connection
    settings = AndroidRunnerSettings(remote_device=args.remote_device) if args.remote_device else None
    runner = AndroidRunner(settings=settings)
    
    orchestrator = PipelineOrchestrator(config, runner, verbose=args.verbose)
    orchestrator.execute(only=args.only, analysis_only=args.analysis_only)


if __name__ == "__main__":
    main()
