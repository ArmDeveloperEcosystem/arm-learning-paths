#!/usr/bin/env python3
"""Compare FP32 and INT4 SmolVLA ONNX outputs and CPU latency."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import platform
import time

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import onnxruntime as ort

INPUT_INTERFACE = (
    ("camera1", "tensor(float)", (1, 3, 512, 512)),
    ("camera2", "tensor(float)", (1, 3, 512, 512)),
    ("lang_tokens", "tensor(int64)", (1, 48)),
    ("lang_attention_mask", "tensor(int64)", (1, 48)),
    ("state", "tensor(float)", (1, 8)),
    ("noise", "tensor(float)", (1, 50, 32)),
)
DTYPES = {"tensor(float)": np.dtype("float32"), "tensor(int64)": np.dtype("int64")}
ACTION_SHAPE = (1, 50, 7)
COLORS = {"FP32": "#2563EB", "INT4": "#F97316"}

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--fp32-model", type=Path, required=True)
    parser.add_argument("--int4-model", type=Path, required=True)
    parser.add_argument("--reference-dir", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True, help="Output PNG path")
    parser.add_argument("--threads", type=int, default=8)
    parser.add_argument("--warmups", type=int, default=1)
    parser.add_argument("--runs", type=int, default=5)
    args = parser.parse_args()
    if args.threads < 1 or args.runs < 1 or args.warmups < 0:
        parser.error("--threads and --runs must be positive; --warmups cannot be negative")
    if args.output.suffix.lower() != ".png":
        parser.error("--output must end in .png")
    return args

def make_session(path: Path, threads: int) -> ort.InferenceSession:
    options = ort.SessionOptions()
    options.intra_op_num_threads = threads
    options.inter_op_num_threads = 1
    options.execution_mode = ort.ExecutionMode.ORT_SEQUENTIAL
    options.graph_optimization_level = ort.GraphOptimizationLevel.ORT_ENABLE_ALL
    options.log_severity_level = 3
    return ort.InferenceSession(
        str(path.resolve(strict=True)), options, providers=["CPUExecutionProvider"]
    )

def interface(session: ort.InferenceSession) -> tuple[tuple[tuple[object, ...], ...], ...]:
    describe = lambda values: tuple(
        (value.name, value.type, tuple(value.shape)) for value in values
    )
    return describe(session.get_inputs()), describe(session.get_outputs())

def validate_models(fp32: ort.InferenceSession, int4: ort.InferenceSession) -> None:
    description = interface(fp32)
    if description != interface(int4):
        raise ValueError("FP32 and INT4 model interfaces differ")
    inputs, outputs = description
    if inputs != INPUT_INTERFACE:
        raise ValueError(f"Unexpected model inputs: {inputs}")
    if outputs != (("actions", "tensor(float)", ACTION_SHAPE),):
        raise ValueError(f"Expected one float actions output with shape {ACTION_SHAPE}")

def load_reference(
    directory: Path, session: ort.InferenceSession
) -> dict[str, np.ndarray]:
    directory = directory.resolve(strict=True)
    if not directory.is_dir():
        raise NotADirectoryError(directory)
    feeds = {}
    for model_input in session.get_inputs():
        path = directory / f"{model_input.name}.npy"
        value = np.load(path, allow_pickle=False)
        expected_dtype = DTYPES.get(model_input.type)
        if expected_dtype is None or value.dtype != expected_dtype:
            raise TypeError(f"{path.name} has dtype {value.dtype}; expected {expected_dtype}")
        if value.shape != tuple(model_input.shape):
            raise ValueError(
                f"{path.name} has shape {value.shape}; expected {tuple(model_input.shape)}"
            )
        if np.issubdtype(value.dtype, np.floating) and not np.isfinite(value).all():
            raise ValueError(f"{path.name} contains non-finite values")
        feeds[model_input.name] = np.ascontiguousarray(value)
    return feeds

def infer(session: ort.InferenceSession, feeds: dict[str, np.ndarray]) -> tuple[np.ndarray, float]:
    start = time.perf_counter_ns()
    result = session.run(None, feeds)
    elapsed_ms = (time.perf_counter_ns() - start) / 1_000_000
    if len(result) != 1:
        raise ValueError(f"Expected one model output, found {len(result)}")
    actions = np.asarray(result[0])
    if actions.shape != ACTION_SHAPE or actions.dtype != np.float32:
        raise ValueError(f"Expected float32 actions with shape {ACTION_SHAPE}")
    if not np.isfinite(actions).all():
        raise ValueError("A model produced non-finite actions")
    return actions, elapsed_ms

def run_pairs(
    sessions: dict[str, ort.InferenceSession],
    feeds: dict[str, np.ndarray],
    iterations: int,
    timed: bool,
) -> tuple[dict[str, np.ndarray], dict[str, list[float]]]:
    outputs: dict[str, np.ndarray] = {}
    timings = {"FP32": [], "INT4": []}
    for index in range(iterations):
        order = ("FP32", "INT4") if index % 2 == 0 else ("INT4", "FP32")
        for name in order:
            outputs[name], elapsed = infer(sessions[name], feeds)
            if timed:
                timings[name].append(elapsed)
    return outputs, timings

def render(output: Path, actions: dict[str, np.ndarray], medians: dict[str, float], speedup: float, mae: float) -> None:
    background, ink, muted, grid = "#F4F7FB", "#142033", "#617086", "#DCE4EE"
    plt.rcParams.update({"font.family": "DejaVu Sans", "text.color": ink})
    figure = plt.figure(figsize=(12.8, 7.2), dpi=100, facecolor=background)
    outer = figure.add_gridspec(
        1, 2, left=0.055, right=0.965, bottom=0.08, top=0.82,
        width_ratios=(4.4, 1.25), wspace=0.18
    )
    plots = outer[0, 0].subgridspec(4, 2, hspace=0.5, wspace=0.24)
    figure.text(0.055, 0.945, "SmolVLA Action Comparison", fontsize=22, weight="bold")
    figure.text(
        0.055, 0.9,
        "FP32 vs INT4 · identical reference inputs · 50 predicted steps · normalized model outputs",
        fontsize=10.5, color=muted,
    )
    figure.text(0.055, 0.85, "SEVEN ACTION CHANNELS", fontsize=8.5, weight="bold", color=muted)
    figure.text(0.055, 0.025, "Each channel uses its own vertical scale.", fontsize=7.5, color=muted)

    steps = np.arange(ACTION_SHAPE[1])
    fp32, int4 = actions["FP32"][0], actions["INT4"][0]
    axes = [figure.add_subplot(plots[index // 2, index % 2]) for index in range(7)]
    for channel, axis in enumerate(axes):
        axis.plot(steps, fp32[:, channel], color=COLORS["FP32"], linewidth=1.7)
        axis.plot(steps, int4[:, channel], color=COLORS["INT4"], linewidth=1.5, linestyle="--")
        axis.set_title(f"Action {channel}", loc="left", fontsize=9, weight="bold", pad=3)
        axis.text(
            1, 1.03, f"MAE {np.mean(np.abs(int4[:, channel] - fp32[:, channel])):.3g}",
            transform=axis.transAxes, ha="right", va="bottom", fontsize=7, color=muted,
        )
        axis.set_xlim(0, 49)
        axis.set_xticks((0, 25, 49))
        axis.tick_params(labelsize=7, colors=muted, length=2)
        axis.grid(axis="y", color=grid, linewidth=0.7)
        axis.spines[["top", "right"]].set_visible(False)
        axis.spines[["left", "bottom"]].set_color("#C9D5E3")
    for axis in (axes[5], axes[6]):
        axis.set_xlabel("Predicted step", fontsize=7.5, color=muted)

    legend = figure.add_subplot(plots[3, 1])
    legend.set_axis_off()
    legend.plot([], [], color=COLORS["FP32"], linewidth=2, label="FP32")
    legend.plot([], [], color=COLORS["INT4"], linewidth=2, linestyle="--", label="INT4")
    legend.legend(loc="upper left", frameon=False, fontsize=9, ncol=2)

    latency = figure.add_subplot(outer[0, 1], facecolor="white")
    names = ("FP32", "INT4")
    values = [medians[name] for name in names]
    bars = latency.barh(names, values, color=[COLORS[name] for name in names], height=0.48)
    latency.invert_yaxis()
    latency.bar_label(bars, labels=[f"{value:,.1f} ms" for value in values], padding=4, fontsize=9)
    latency.set_xlim(0, max(values) * 1.28)
    latency.set_title("CPU latency", loc="left", fontsize=10, weight="bold", pad=14)
    latency.tick_params(axis="y", labelsize=9, length=0)
    latency.tick_params(axis="x", bottom=False, labelbottom=False)
    latency.spines[:].set_visible(False)
    latency.text(0, -0.55, "Median session.run · lower is better", fontsize=8, color=muted)
    latency.set_ylim(2.8, -0.75)
    latency.text(0, 2.05, f"{speedup:.2f}×", fontsize=25, weight="bold")
    latency.text(0, 2.35, "FP32 latency ÷ INT4 latency", fontsize=8, color=muted)
    latency.text(0, 2.62, f"Normalized MAE  {mae:.4g}", fontsize=9, weight="bold")

    output.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output, dpi=100, facecolor=background)
    plt.close(figure)

def main() -> None:
    args = parse_args()
    sessions = {
        "FP32": make_session(args.fp32_model, args.threads),
        "INT4": make_session(args.int4_model, args.threads),
    }
    validate_models(sessions["FP32"], sessions["INT4"])
    feeds = load_reference(args.reference_dir, sessions["FP32"])
    if args.warmups:
        run_pairs(sessions, feeds, args.warmups, timed=False)
    actions, timings = run_pairs(sessions, feeds, args.runs, timed=True)
    medians = {name: float(np.median(values)) for name, values in timings.items()}
    speedup = medians["FP32"] / medians["INT4"]
    difference = actions["INT4"].astype(np.float64) - actions["FP32"]
    mae = float(np.mean(np.abs(difference)))
    report = {
        "timing_scope": "ONNX Runtime session.run on CPUExecutionProvider",
        "platform_machine": platform.machine(), "onnxruntime_version": ort.__version__,
        "threads": args.threads, "warmups": args.warmups, "runs": args.runs,
        "model_interface": {
            "inputs": [
                {"name": name, "type": dtype, "shape": shape}
                for name, dtype, shape in INPUT_INTERFACE
            ],
            "output": {"name": "actions", "type": "tensor(float)", "shape": ACTION_SHAPE},
        },
        "median_latency_ms": medians, "speedup": speedup,
        "normalized_output_error": {
            "mae": mae,
            "rmse": float(np.sqrt(np.mean(np.square(difference)))),
            "max_abs": float(np.max(np.abs(difference))),
        },
    }
    output = args.output.resolve()
    sidecar = output.with_suffix(".json")
    render(output, actions, medians, speedup, mae)
    sidecar.write_text(
        json.dumps(report, indent=2, allow_nan=False) + "\n", encoding="utf-8"
    )
    print(f"FP32 median: {medians['FP32']:.3f} ms")
    print(f"INT4 median: {medians['INT4']:.3f} ms")
    print(f"Speedup: {speedup:.3f}x")
    print(f"Saved {args.output} and {args.output.with_suffix('.json')}")

if __name__ == "__main__":
    main()
