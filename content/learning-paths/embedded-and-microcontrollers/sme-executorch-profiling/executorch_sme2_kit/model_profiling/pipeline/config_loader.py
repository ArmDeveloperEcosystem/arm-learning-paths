from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, List

from .config import ComparisonConfig, ExperimentConfig, PipelineConfig, SUPPORTED_EXPERIMENT_MODES


def load_pipeline_config(path: Path) -> PipelineConfig:
    raw = json.loads(path.read_text())
    model = Path(raw["model"])
    output_root = Path(raw["output_root"]).resolve() if raw.get("output_root") else None
    experiments = [_parse_experiment(item) for item in raw.get("experiments", [])]
    comparisons = _parse_comparisons(raw.get("analysis", {}).get("compare_pairs", []))
    return PipelineConfig(
        model=model,
        output_root=output_root,
        experiments=experiments,
        comparisons=comparisons,
    )


def _parse_experiment(item: Dict[str, Any]) -> ExperimentConfig:
    runner_path_value = item.get("runner_path") or item.get("quiet_runner")
    runner_path = Path(runner_path_value) if runner_path_value else None
    mode = item.get("mode", "timing")
    if mode not in SUPPORTED_EXPERIMENT_MODES:
        modes = ", ".join(SUPPORTED_EXPERIMENT_MODES)
        raise ValueError(f"Unsupported experiment mode '{mode}'. Supported modes: {modes}.")
    return ExperimentConfig(
        name=item["name"],
        runner_path=runner_path,
        mode=mode,
        runs=int(item.get("runs", 100)),
        warmup=int(item.get("warmup", 10)),
        threads=[int(t) for t in item.get("threads", [1])],
        extra_args=item.get("extra_args", []),
        cpu_affinity=item.get("cpu_affinity"),
    )


def _parse_comparisons(raw_pairs: List[Dict[str, Any]]) -> List[ComparisonConfig]:
    comparisons: List[ComparisonConfig] = []
    for entry in raw_pairs:
        baseline = entry.get("baseline", {})
        candidate = entry.get("candidate", {})
        comparisons.append(
            ComparisonConfig(
                baseline_experiment=baseline["experiment"],
                baseline_threads=int(baseline["threads"]),
                candidate_experiment=candidate["experiment"],
                candidate_threads=int(candidate["threads"]),
                label=entry.get("label", ""),
            )
        )
    return comparisons
