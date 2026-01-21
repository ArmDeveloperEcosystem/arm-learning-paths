from __future__ import annotations

import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional

from .analysis import (
    convert_etdump_to_csv,
    extract_kernels_from_xnntrace,
    generate_kernel_view,
    run_operator_analysis,
    run_robust_latency_analysis,
)
from .config import ComparisonConfig, ExperimentConfig, PipelineConfig
from .util import ensure_path, find_python_executable


class PipelineOrchestrator:
    def __init__(self, config: PipelineConfig, runner, *, verbose: bool = False):
        self.config = config
        self.runner = runner
        self.verbose = verbose
        self.python = find_python_executable()
        self.results: List[Dict] = []

    def execute(self, only: Optional[Iterable[str]] = None, analysis_only: bool = False) -> None:
        ensure_path(self.output_root)
        only_set = set(only or [])
        for exp in self.config.experiments:
            if only_set and exp.name not in only_set:
                continue
            for threads in exp.threads:
                self._run_single(exp, threads, analysis_only=analysis_only)
        self._run_comparisons()
        self._generate_kernel_views()
        self._write_summary()

    @property
    def output_root(self) -> Path:
        return self.runner.resolve_output_dir(self.config.model, self.config.output_root)

    def _run_single(self, exp: ExperimentConfig, threads: int, *, analysis_only: bool) -> None:
        result = {
            "experiment": exp.name,
            "threads": threads,
            "mode": exp.mode,
            "status": "analysis-only" if analysis_only else "pending",
            "paths": {},
            "metrics": {},
            "runs": exp.runs,
            "warmup": exp.warmup,
        }
        if not analysis_only:
            artifact = self.runner.run_experiment(
                model=self.config.model,
                output_root=self.output_root,
                experiment=exp,
                threads=threads,
                python=self.python,
                verbose=self.verbose,
            )
            result["status"] = "ok"
        else:
            artifact = self.runner.derive_artifact_paths(
                model=self.config.model,
                output_root=self.output_root,
                experiment=exp,
                threads=threads,
            )
        result["paths"] = {k: str(v) for k, v in artifact.items()}
        if exp.mode == "timing":
            self._post_process(exp.name, threads, artifact, result)
        elif exp.mode == "xnntrace":
            self._post_process_xnntrace(exp.name, threads, artifact, result)
        self.results.append(result)

    def _post_process(self, exp_name: str, threads: int, artifact: Dict[str, Path], result: Dict) -> None:
        etdump = artifact.get("etdump")
        if not etdump or not etdump.exists():
            return
        out_dir = etdump.parent
        timeline = convert_etdump_to_csv(etdump, out_dir, self.python)
        if timeline:
            result["paths"]["timeline_all"] = str(timeline)
            primary_name = f"{exp_name}_t{threads}"
            stats = run_robust_latency_analysis(timeline, out_dir, primary_name, self.python)
            if stats:
                result["metrics"]["median_ms"] = stats.get("median_ms")
                result["metrics"]["mean_ms"] = stats.get("mean_ms")
                result["metrics"]["cv_percent"] = stats.get("cv_percent")
                result["metrics"]["robust_stats_path"] = str(out_dir / f"{timeline.stem}_robust_stats.json")
            run0 = out_dir / f"{etdump.stem}_run0_timeline.csv"
            if run0.exists():
                result["paths"]["timeline_run0"] = str(run0)
                run_operator_analysis(run0, out_dir, self.python)

    def _post_process_xnntrace(
        self, exp_name: str, threads: int, artifact: Dict[str, Path], result: Dict
    ) -> None:
        """Extract kernels from xnntrace log."""
        xnntrace_log = artifact.get("xnntrace_log")
        if not xnntrace_log or not xnntrace_log.exists():
            return
        out_dir = xnntrace_log.parent
        model_id = f"{self.config.model.stem}_{exp_name}_t{threads}"
        kernel_csv = extract_kernels_from_xnntrace(xnntrace_log, out_dir, model_id, self.python)
        if kernel_csv:
            result["paths"]["kernel_csv"] = str(kernel_csv)

    def _run_comparisons(self) -> None:
        for comp in self.config.comparisons:
            baseline = self._find_result(comp.baseline_experiment, comp.baseline_threads)
            candidate = self._find_result(comp.candidate_experiment, comp.candidate_threads)
            if not baseline or not candidate:
                continue
            base_path = baseline["paths"].get("timeline_all")
            cand_path = candidate["paths"].get("timeline_all")
            if not base_path or not cand_path:
                if self.verbose:
                    print(
                        f"Skipping comparison '{comp.baseline_experiment}' vs "
                        f"'{comp.candidate_experiment}': missing timeline paths."
                    )
                continue
            base_timeline = Path(base_path)
            cand_timeline = Path(cand_path)
            if not base_timeline.exists() or not cand_timeline.exists():
                if self.verbose:
                    print(
                        f"Skipping comparison '{comp.baseline_experiment}' vs "
                        f"'{comp.candidate_experiment}': timeline files not found."
                    )
                continue
            cmd = [
                str(self.python),
                "model_profiling/tools/robust_latency_analysis.py",
                "--timeline-csv",
                str(base_timeline),
                "--compare",
                str(cand_timeline),
                "--name1",
                comp.baseline_experiment,
                "--name2",
                comp.candidate_experiment,
                "--output-dir",
                str(self.output_root),
            ]
            try:
                self.runner.run_command(cmd)
            except Exception:
                continue

    def _find_result(self, experiment: str, threads: int) -> Optional[Dict]:
        for res in self.results:
            if res["experiment"] == experiment and res["threads"] == threads:
                return res
        return None

    def _write_summary(self) -> None:
        summary = {
            "model": str(self.config.model),
            "generated_at": datetime.now(timezone.utc).isoformat(),
            "output_root": str(self.output_root),
            "runs": self.results,
        }
        json_path = self.output_root / f"{self.config.model.stem}_pipeline_summary.json"
        json_path.write_text(json.dumps(summary, indent=2))

        lines = [
            f"# Pipeline Summary – {self.config.model.stem}",
            "",
            f"- Generated: {summary['generated_at']}",
            f"- Output root: `{self.output_root}`",
            "",
        ]
        timing = [r for r in self.results if r["mode"] == "timing"]
        if timing:
            lines.append("## Timing Results")
            lines.append("| Experiment | Threads | Runs | Warmup | Median (ms) | Mean (ms) | CV (%) | Robust Stats |")
            lines.append("|-----------|---------|------|--------|-------------|-----------|--------|---------------|")
            for row in timing:
                metrics = row.get("metrics", {})
                lines.append(
                    "| {exp} | {thr} | {runs} | {warmup} | {median:.2f} | {mean:.2f} | {cv:.2f} | `{stats}` |".format(
                        exp=row["experiment"],
                        thr=row["threads"],
                        runs=row["runs"],
                        warmup=row["warmup"],
                        median=metrics.get("median_ms", float("nan")),
                        mean=metrics.get("mean_ms", float("nan")),
                        cv=metrics.get("cv_percent", float("nan")),
                        stats=metrics.get("robust_stats_path", "n/a"),
                    )
                )
            lines.append("")
        trace = [r for r in self.results if r["mode"] == "xnntrace"]
        if trace:
            lines.append("## XNNTrace Results")
            lines.append("| Experiment | Threads | Log Path |")
            lines.append("|-----------|---------|----------|")
            for row in trace:
                log_path = row["paths"].get("xnntrace_log", "n/a")
                lines.append(f"| {row['experiment']} | {row['threads']} | `{log_path}` |")
            lines.append("")
        md_path = self.output_root / f"{self.config.model.stem}_pipeline_summary.md"
        md_path.write_text("\n".join(lines))

    def _generate_kernel_views(self) -> None:
        """Generate kernel view tables comparing SME2-On vs SME2-Off."""
        # Find SME2-On and SME2-Off xnntrace experiments
        sme2_on_trace = None
        sme2_off_trace = None

        for result in self.results:
            if result["mode"] != "xnntrace":
                continue
            exp_name = result["experiment"]
            kernel_csv = result["paths"].get("kernel_csv")
            if not kernel_csv:
                continue
            if "sme2_off" in exp_name.lower() or "sme2-off" in exp_name.lower():
                sme2_off_trace = Path(kernel_csv)
            elif "sme2" in exp_name.lower() or "f16igemm" in exp_name.lower():
                # Assume this is SME2-On if it's not explicitly SME2-Off
                if sme2_on_trace is None:
                    sme2_on_trace = Path(kernel_csv)

        if sme2_on_trace and sme2_off_trace:
            kernel_view_path = self.output_root / "kernel_view_gemm.md"
            generate_kernel_view(
                sme2_on_trace,
                sme2_off_trace,
                kernel_view_path,
                f"{self.config.model.stem}: GEMM/IGEMM Kernel view (XNNPACK Delegated):",
                filter_op="gemm",
                python=self.python,
            )
