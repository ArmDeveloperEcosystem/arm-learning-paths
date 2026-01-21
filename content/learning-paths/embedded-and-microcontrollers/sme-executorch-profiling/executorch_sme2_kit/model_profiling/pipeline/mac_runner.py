from __future__ import annotations

from pathlib import Path
from typing import Dict, Optional

from .config import ExperimentConfig
from .runner_base import BaseRunner
from .util import ensure_path, run_subprocess


class MacRunner(BaseRunner):
    default_output_dir_name = "results"
    include_timing_artifacts_for_xnntrace = True

    def __init__(self) -> None:
        super().__init__()

    def run_experiment(
        self,
        *,
        model: Path,
        output_root: Path,
        experiment: ExperimentConfig,
        threads: int,
        python: Path,
        verbose: bool = False,
    ) -> Dict[str, Path]:
        _ = python
        out_dir = self.resolve_output_dir(model, output_root)
        ensure_path(out_dir)
        prefix = f"{model.stem}_{experiment.name}_t{threads}"
        if not experiment.runner_path:
            raise ValueError(f"Experiment '{experiment.name}' requires 'runner_path' for mac execution.")
        # Resolve runner path relative to executorch directory
        runner_path = self.resolve_runner_path(experiment.runner_path)
        cmd = [
            str(self.python),
            "model_profiling/scripts/perf_runner.py",
            "--model",
            str(model),
            "--quiet-runner",
            str(runner_path),
            "--threads",
            str(threads),
            "--exp",
            experiment.name,
            "--outdir",
            str(out_dir),
            "--warmup",
            str(experiment.warmup),
        ]
        if experiment.mode == "timing":
            cmd.extend(["--timing-runs", str(experiment.runs)])
        if experiment.mode == "xnntrace" and experiment.runner_path:
            cmd.extend(["--mode", "xnntrace"])
            # Auto-add --verbose-runner if not provided in extra_args
            if not any("--verbose-runner" in arg for arg in experiment.extra_args):
                cmd.extend(["--verbose-runner", str(runner_path)])
        if experiment.extra_args:
            cmd.extend(experiment.extra_args)
        if verbose:
            print(" ".join(cmd))
        run_subprocess(cmd, cwd=Path.cwd())
        return self._build_artifact_paths(out_dir, prefix, experiment.mode)

    def derive_artifact_paths(
        self,
        *,
        model: Path,
        output_root: Path,
        experiment: ExperimentConfig,
        threads: int,
    ) -> Dict[str, Path]:
        out_dir = self.resolve_output_dir(model, output_root)
        prefix = f"{model.stem}_{experiment.name}_t{threads}"
        return self._build_artifact_paths(out_dir, prefix, experiment.mode)
