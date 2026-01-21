from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import List, Optional

SUPPORTED_EXPERIMENT_MODES = ("timing", "xnntrace")


@dataclass
class ExperimentConfig:
    name: str
    runner_path: Optional[Path]
    mode: str = "timing"  # timing | xnntrace
    runs: int = 100
    warmup: int = 10
    threads: List[int] = field(default_factory=lambda: [1])
    extra_args: List[str] = field(default_factory=list)
    cpu_affinity: Optional[str] = None  # CPU affinity mask (e.g., "0x80" for cpu7) for Android


@dataclass
class ComparisonConfig:
    baseline_experiment: str
    baseline_threads: int
    candidate_experiment: str
    candidate_threads: int
    label: str = ""


@dataclass
class PipelineConfig:
    model: Path
    output_root: Optional[Path]
    experiments: List[ExperimentConfig]
    comparisons: List[ComparisonConfig] = field(default_factory=list)
