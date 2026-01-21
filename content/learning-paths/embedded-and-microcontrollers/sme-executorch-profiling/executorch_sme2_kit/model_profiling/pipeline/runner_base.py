from __future__ import annotations

from pathlib import Path
from typing import Dict, List, Optional

from .config import ExperimentConfig
from .util import find_python_executable, run_subprocess


class BaseRunner:
    default_output_dir_name = "results"
    include_timing_artifacts_for_xnntrace = False

    def __init__(self) -> None:
        self.python = find_python_executable()

    def resolve_output_dir(self, model: Path, output_root: Optional[Path]) -> Path:
        if output_root:
            return output_root
        model_dir = model.parent
        if model_dir.name == "artifacts":
            return model_dir.parent / self.default_output_dir_name
        for parent in model_dir.parents:
            if parent.name.startswith("out_"):
                return parent / self.default_output_dir_name
        return model_dir / self.default_output_dir_name

    def resolve_runner_path(self, runner_path: Path) -> Path:
        if runner_path.is_absolute():
            return runner_path
        repo_root = Path.cwd()
        executorch_runner = repo_root / "executorch" / runner_path
        if executorch_runner.exists():
            return executorch_runner
        return runner_path

    def derive_artifact_paths(
        self,
        *,
        model: Path,
        output_root: Optional[Path],
        experiment: ExperimentConfig,
        threads: int,
    ) -> Dict[str, Path]:
        out_dir = self.resolve_output_dir(model, output_root)
        prefix = f"{model.stem}_{experiment.name}_t{threads}"
        return self._build_artifact_paths(out_dir, prefix, experiment.mode)

    def run_command(self, cmd: List[str]) -> None:
        run_subprocess(cmd, cwd=Path.cwd())

    def _build_artifact_paths(self, out_dir: Path, prefix: str, mode: str) -> Dict[str, Path]:
        paths: Dict[str, Path] = {}
        include_timing = mode == "timing" or self.include_timing_artifacts_for_xnntrace
        if include_timing:
            paths["latency_log"] = out_dir / f"{prefix}_latency.log"
            paths["timeline_all"] = out_dir / f"{prefix}_exec_all_runs_timeline.csv"
            paths["timeline_run0"] = out_dir / f"{prefix}_exec_run0_timeline.csv"
            paths["etdump"] = out_dir / f"{prefix}.etdump"
        if mode == "xnntrace":
            paths["xnntrace_log"] = out_dir / f"{prefix}_xnntrace.log"
        return paths
