---
title: "Model onboarding + performance analysis: export, run, analyze"
weight: 4
layout: "learningpathall"
---

## Goal: Onboard a model and analyze its performance

This page covers the workflow you follow for each model: onboarding, export, running the performance analysis pipeline, and analyzing results.

Once you have runners built (from 02 – Setup + pipeline), you can analyze a model's performance by onboarding it, exporting it to `.pte`, running the performance analysis pipeline, and analyzing the results. It is important to know that model onboarding can require model-specific code edits (wrappers, operator replacements, shape constraints), but once you have a `.pte` file, the performance analysis pipeline is model-agnostic—the same commands and scripts work across different models.

## 1. Model onboarding: what you need to do per model

For a concrete example of model onboarding, see [EfficientSAM](https://github.com/pytorch/executorch/tree/main/examples/models/efficient_sam) in `executorch/examples/models/`, which demonstrates the full onboarding process including input/output handling, quantization, and backend delegation.

What you need to do:

- Define or wrap a PyTorch model so it is exportable (implements `EagerModelBase` interface)
- Define representative example inputs (shapes/dtypes that match your use case). Note: `executor_runner` can use default all-one input tensors if no input is provided, but for accurate performance analysis you should define representative inputs that match your actual use case. The export step uses these example inputs to capture the model graph with correct shapes and dtypes.
- Refactor model code to avoid unsupported ops or dynamic control flow (if needed)
- Choose export dtype and quantization:
  - Floating-point: FP16/FP32 (no quantization)
  - Quantization: INT8 with various quantization schemes:
    - Static quantization: Requires calibration data; weights and activations are quantized at export time
    - Dynamic quantization: Activations quantized at runtime; weights quantized at export time
    - Channel-wise quantization: Per-channel quantization for weights (often more accurate than per-tensor)
    - Per-tensor quantization: Single scale/zero-point per tensor (simpler but less accurate)
  - Backend partitioning: XNNPACK vs portable (which operators are delegated to XNNPACK)

Real-world example: The EdgeTAM image encoder (see agent skill `08_onboard_edgetam.md` for onboarding steps) required:
- Input/output normalization wrappers
- Operator replacements (unsupported ops → supported equivalents)
- Shape constraint fixes (dynamic shapes → static shapes)
- Export-friendly refactoring (control flow → data flow)

## 2. Registering new models

To add a new model to the performance analysis workflow:

1. Create [`model_profiling/models/<model_name>/`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/tree/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/model_profiling/models) directory
2. Implement `EagerModelBase` interface in `model.py`:
   - `get_eager_model()`: Returns the PyTorch model
   - `get_example_inputs()`: Returns tuple of example tensors
3. Register in [`model_profiling/models/__init__.py`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/model_profiling/models/__init__.py):
   ```python
   from . import your_model
   register_model("your_model", YourModelClass)
   ```

The key insight: This registration system lets you add models without touching ExecuTorch source code. The exporter patches the registry at runtime, so your models appear alongside ExecuTorch's built-in models.

Advanced onboarding example: The EdgeTAM image encoder (see agent skill `08_onboard_edgetam.md` for complete onboarding workflow) demonstrates:
- Wrapper classes for input/output normalization
- Operator replacement strategies
- Shape constraint handling
- Export-friendly refactoring patterns

## 3. Export a model

Exporting a model to `.pte` format is model-specific work. This learning path ships a reference exporter at [`model_profiling/export/export_model.py`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/model_profiling/export/export_model.py) that demonstrates the export process.

How it works: The exporter uses a registry patching system that allows local models (in `model_profiling/models/`) to be exported without editing ExecuTorch source code. This keeps the pipeline stable while you add new models.

Supported models:
- `toy_cnn` (no extra deps; good for smoke tests)
- `mobilenet_v3_small` (requires `torchvision`; otherwise it falls back to `toy_cnn`)

### 3.1 Export command (example)

```bash
python model_profiling/export/export_model.py \
  --model toy_cnn \
  --dtype fp16 \
  --outdir model_profiling/out_toy_cnn/artifacts/
```

Expected outputs:

- `model_profiling/out_toy_cnn/artifacts/toy_cnn_xnnpack_fp16.pte`
- `model_profiling/out_toy_cnn/artifacts/toy_cnn_xnnpack_fp16.pte.etrecord` (optional; operator metadata)

Why `out_<model>/artifacts/`: This keeps the `models/` directory clean (source code only). Exported artifacts live in a separate tree, making it easy to version control models without committing large `.pte` files.

## 4. The two-run workflow: Why you need both

This page covers a critical insight: you need two types of runs for complete performance analysis.

1. Timing-only runs: Accurate latency measurements (no trace logging overhead)
2. Trace-enabled runs: Kernel-level insights (trace logging impacts timing, so these are only for kernel analysis)

Why this matters: If you only run with trace logging enabled, your latency numbers are inflated by logging overhead. If you only run without trace logging, you can't see which kernels were selected. The solution: run both, use timing-only for latency comparisons, use trace-enabled for kernel analysis.

## 5. Configure a run (JSON)

The pipeline is config-driven. The required keys are:

- `model`: path to `.pte`
- `output_root`: where to write run artifacts
- `experiments[]`: a list of runs (SME2 on/off, threads, runs, runner_path)

Why JSON configs: They're version-controllable, reproducible, and easy to generate programmatically. You can keep configs for different models, platforms, or experiment variations.

Start from the template:

```bash
cat model_profiling/configs/templates/mac_template.json
```

Or use the provided example:

```bash
cat model_profiling/configs/examples/mac_mobilenet_fp16.json
```

Config files: [`mac_template.json`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/model_profiling/configs/templates/mac_template.json), [`mac_mobilenet_fp16.json`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/model_profiling/configs/examples/mac_mobilenet_fp16.json)

Key fields:
- `experiments[].runner_path`: Points to the runner binary in `executorch/cmake-out/<preset>/executor_runner` (timing-only or trace-enabled)
- `experiments[].num_runs`: Number of iterations (default 10 for statistical significance)
- `experiments[].num_threads`: Thread count (usually 1 for single-threaded performance analysis)

## 6. Run the performance analysis pipeline

The pipeline supports both **Android** (for real-world edge ML performance on mobile devices) and **macOS** (included for developer accessibility). The workflow is identical—only the runner binaries and execution environment differ.

**Platform context**: This learning path demonstrates analyzing ExecuTorch model performance on SME2-enabled devices using Android as the mobile device example. Android runs provide realistic edge ML performance with actual device constraints (memory bandwidth, thermal throttling, device-specific optimizations). macOS is included because most developers have Mac access, making it convenient for learning the workflow and initial testing. For production validation and accurate performance measurements, Android runs on real SME2-enabled devices provide the most representative results.

### 6.1 Run on Android (for real-world edge ML performance on mobile devices)

For testing on real Arm edge mobile devices, Android runs are essential. This is the only way to validate performance on actual hardware with real thermal constraints, memory bandwidth, and device-specific optimizations.

**Critical: Device power management settings** - Power management settings significantly impact inference latency measurements. Configure your device for consistent performance mode and keep settings consistent across runs. Inconsistent power settings can cause measurement variance that obscures actual performance differences.

**Configure device settings before running**:

**Option 1: Unconstrained boost mode** (for stress testing hardware - removes all CPU frequency caps and scaling policies):
```bash
# Disable low power mode
adb shell settings put global low_power 0

# Force "stay on while plugged" (removes CPU frequency caps)
adb shell settings put global stay_on_while_plugged_in 15
adb shell svc power stayon true

# Disable UI animations
adb shell settings put global window_animation_scale 0
adb shell settings put global transition_animation_scale 0
adb shell settings put global animator_duration_scale 0
```

**Option 2: App developer mode** (for perceived app performance - real user daily experience):
```bash
# Stay on only when USB connected (normal device usage setting)
adb shell settings put global stay_on_while_plugged_in 1

# Keep UI animations enabled (real user experience)
adb shell settings put global window_animation_scale 1
adb shell settings put global transition_animation_scale 1
adb shell settings put global animator_duration_scale 1

# Disable low power mode (consistent performance)
adb shell settings put global low_power 0
```

**Verify settings**:
```bash
adb shell settings get global stay_on_while_plugged_in
adb shell settings get global low_power
adb shell dumpsys power | grep -i "stay.*awake\|thermal"
```

**Note**: Unconstrained boost mode (value 15) removes all CPU frequency caps and scaling policies for stress testing hardware. App developer mode (value 1) reflects normal device usage and perceived app performance for real user daily experience. Choose based on your measurement goals and keep settings consistent across all runs.

After building Android runners and connecting a device:

```bash
python model_profiling/scripts/android_pipeline.py --config model_profiling/configs/examples/android_mobilenet_fp16.json
python model_profiling/scripts/analyze_results.py --run-dir model_profiling/out_toy_cnn/runs/android
```

See [`android_pipeline.py`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/model_profiling/scripts/android_pipeline.py) for the implementation.

This uses the Android runners (`executorch/cmake-out/android-arm64-v9a/executor_runner`, `executorch/cmake-out/android-arm64-v9a-sme2-off/executor_runner`) which have no trace logging overhead.

Outputs (example):

```text
out_<model>/runs/android/
  android_sme2_on/
    <model>_android_sme2_on_t1.etdump      # Primary: operator-level trace data
    <model>_android_sme2_on_t1.log         # Runner stdout/stderr
  android_sme2_off/
    <model>_android_sme2_off_t1.etdump     # Primary: operator-level trace data
    <model>_android_sme2_off_t1.log        # Runner stdout/stderr
  manifest.json                # Optional: run metadata (ExecuTorch SHA, config path, model path)
  metrics.json                 # Optional: summary latencies (duplicate of manifest results)
```

The workflow: Same pipeline, different platform. The config points to Android runners, and the script uses `adb` to push binaries and run on device. ETDump traces are pulled back to the host for analysis.

Expected outcome: You'll see similar operator-category breakdowns, but with real device timing. Often, data movement bottlenecks are more pronounced on real hardware due to memory bandwidth constraints.

For kernel-level insights on Android, run again with trace-enabled runners (separate config pointing to trace-enabled runner builds). Note: Trace logging impacts timing, so these runs are only for kernel analysis, not latency measurement.

```bash
# Use a separate config that points to trace-enabled Android runners
# Note: Create a trace config by copying an existing config and updating runner_path to point to trace-enabled runners
python model_profiling/scripts/android_pipeline.py --config model_profiling/configs/examples/android_mobilenet_fp16.json
```

### 6.2 Run on macOS (developer accessibility)

For development and initial testing, run on macOS. This is fast and convenient, but not representative of real device performance.

#### 6.2.1 Timing-only runs (for latency measurement)

Run with timing-only runners (default) to get accurate latency measurements:

```bash
python model_profiling/scripts/mac_pipeline.py --config model_profiling/configs/examples/mac_mobilenet_fp16.json
```

See [`mac_pipeline.py`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/model_profiling/scripts/mac_pipeline.py) for the implementation.

This uses the standard runners (`executorch/cmake-out/mac-arm64/executor_runner`, `executorch/cmake-out/mac-arm64-sme2-off/executor_runner`) which have no trace logging overhead.

Outputs (example):

```text
out_<model>/runs/mac/
  mac_sme2_on/
    <model>_mac_sme2_on_t1.etdump      # Primary: operator-level trace data
    <model>_mac_sme2_on_t1.log         # Runner stdout/stderr
  mac_sme2_off/
    <model>_mac_sme2_off_t1.etdump     # Primary: operator-level trace data
    <model>_mac_sme2_off_t1.log        # Runner stdout/stderr
  manifest.json                # Optional: run metadata (ExecuTorch SHA, config path, model path)
  metrics.json                 # Optional: summary latencies (duplicate of manifest results)
```

Critical insight: The `.etdump` files are the primary data source. End-to-end latency numbers and operator-level breakdowns are derived from them. The JSON files (`manifest.json`, `metrics.json`) are optional metadata/logs for reproducibility and convenience, but analysis scripts work directly with ETDump.

#### 6.2.2 Trace-enabled runs (for kernel-level analysis)

For kernel-level insights, run again with trace-enabled runners (separate config pointing to trace-enabled runner builds). Note: Trace logging impacts timing, so these runs are only for kernel analysis, not latency measurement.

```bash
# Use a separate config that points to trace-enabled runners
# Note: Create a trace config by copying an existing config and updating runner_path to point to trace-enabled runners
python model_profiling/scripts/mac_pipeline.py --config model_profiling/configs/examples/mac_mobilenet_fp16.json
```

See [`mac_pipeline.py`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/model_profiling/scripts/mac_pipeline.py) for the implementation.

When to use: When you need to verify which kernels were selected (e.g., `__neonsme2` vs `neon`). This is evidence-gathering, not performance measurement.

Validate (optional):

```bash
# Validates that expected files exist (including optional manifest.json/metrics.json)
python model_profiling/scripts/validate_results.py --results model_profiling/out_toy_cnn/runs/mac
```

See [`validate_results.py`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/model_profiling/scripts/validate_results.py) for the implementation.

> **Note**: Validation checks for JSON files, but they're not required for analysis. The analysis script works directly with ETDump files.

## 7. Analyze ETDump (operator categories + kernel hints)

**Note**: The pipeline automatically runs analysis after performance measurement, generating CSV files from ETDump and creating `analysis_summary.json`. You only need to run this manually if you want to re-analyze existing ETDump files or if analysis failed during pipeline execution.

To manually run analysis:

```bash
python model_profiling/scripts/analyze_results.py \
  --run-dir model_profiling/out_toy_cnn/runs/mac
```

See [`analyze_results.py`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/model_profiling/scripts/analyze_results.py) for the implementation.

It writes:

- `model_profiling/out_toy_cnn/runs/mac/analysis_summary.json` (operator-category breakdown)
- CSV files in the same directory as ETDump files (if not already generated by pipeline)

And prints a category summary like:

- Convolution: Time spent in Conv2d operations (should decrease with SME2)
- GEMM: Time spent in Linear/MatMul operations (should decrease with SME2)
- Data Movement: Time spent in transpose, permute, copy operations (often increases as % after SME2)
- Elementwise: Time spent in add, mul, relu, etc. (usually small)
- Other: Everything else (check for unexpected operations)

**The key insight**: After SME2 accelerates CONV/GEMM, you'll see data movement become a larger percentage of total time. This is expected, as SME2 reveals the next bottleneck. The visualization makes it obvious where to optimize next.

### 7.1 Interpreting the breakdown (Android vs macOS)

Before SME2: CONV/GEMM dominate timing (e.g., 60-80% of total time)

After SME2: 
- CONV/GEMM shrink (e.g., 20-30% of total time)
- Data Movement grows (e.g., 40-60% of total time)
- Overall latency decreases (the speedup)

**Platform differences**: Android runs on real devices often show more pronounced data movement bottlenecks due to memory bandwidth constraints, thermal throttling, and device-specific optimizations. macOS runs are useful for learning the workflow and initial testing, but Android runs provide the realistic performance measurements needed for production validation.

What this tells you: If data movement dominates after SME2, focus on:
- Transpose elimination (reduce layout changes)
- Layout optimization (choose layouts that minimize copies)
- Memory access patterns (reduce cache misses)

### 7.2 About kernel-level insight (xnntrace / kernel hints)

This applies to both Android and macOS runs.

Kernel-level analysis requires separate trace-enabled runs because XNNPACK kernel trace logging impacts timing. The workflow is:

1. Use timing-only runs for latency measurements (SME2 on vs off comparison)
2. Use trace-enabled runs (separate execution) for kernel selection evidence

In this learning path, [`model_profiling/scripts/analyze_results.py`](https://github.com/ArmDeveloperEcosystem/arm-learning-paths/blob/main/content/learning-paths/embedded-and-microcontrollers/sme-executorch-profiling/executorch_sme2_kit/model_profiling/scripts/analyze_results.py) extracts best-effort kernel hints from Inspector TSV fields when present (e.g. matching `__neonsme2`, `sme2`, `neon`).

- If your ExecuTorch build emits delegate debug/kernel identifiers into ETDump/Inspector metadata, you'll see non-empty `kernel_hints` from trace-enabled runs.
- If not, you still get robust operator/category timing from timing-only runs, but kernel selection evidence may be sparse.

> **Important**: Always use timing-only runs for latency comparisons. Trace-enabled runs are only for kernel analysis and should not be used for performance measurements.
