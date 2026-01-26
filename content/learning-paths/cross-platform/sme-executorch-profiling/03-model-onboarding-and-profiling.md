---
title: "Export PyTorch models and analyze performance"
weight: 4
layout: "learningpathall"
---

## Onboard a model and analyze its performance

This section walks you through the end-to-end workflow you repeat for each model: onboarding and export to .pte, running the two-run performance analysis (timing-only and trace-enabled), and analyzing operator-level results. Model-specific work usually appears during onboarding and export; after you produce a .pte file, the pipeline is model-agnostic.

## Prepare your model for onboarding

For a concrete example of model onboarding, see [EfficientSAM](https://github.com/pytorch/executorch/tree/main/examples/models/efficient_sam) in `executorch/examples/models/`, which demonstrates the full onboarding process including input/output handling, quantization, and backend delegation.

Model onboarding prepares the model for export and accurate profiling. Typical steps include defining or wrapping a PyTorch model so it is exportable (implements `EagerModelBase` interface), defining representative example inputs (shapes/dtypes that match your use case), refactoring model code to avoid unsupported operations or dynamic control flow (if needed), and choosing export dtype and quantization.

{{% notice Note %}}
`executor_runner` can use default all-one input tensors if no input is provided, but for accurate performance analysis you should define representative inputs that match your actual use case. The export step uses these example inputs to capture the model graph with correct shapes and dtypes.
{{% /notice %}}

**Export dtype and quantization options:**
  - Floating-point: FP16/FP32 (no quantization)
  - Quantization: INT8 with various quantization schemes:
    - Static quantization: Requires calibration data; weights and activations are quantized at export time
    - Dynamic quantization: Activations quantized at runtime; weights quantized at export time
    - Channel-wise quantization: Per-channel quantization for weights (often more accurate than per-tensor)
    - Per-tensor quantization: Single scale/zero-point per tensor (simpler but less accurate)
  - Backend partitioning: XNNPACK vs portable (which operators are delegated to XNNPACK)

Real onboarding work often requires small wrapper layers (normalization/scaling), operator substitutions, and shape stabilization. 

## Register models in the profiling pipeline

To add a new model to the performance analysis workflow:

1. Create [`model_profiling/models/<model_name>/`](https://github.com/ArmDeveloperEcosystem/sme-executorch-profiling/tree/main/model_profiling/models) directory
2. Implement `EagerModelBase` interface in `model.py`:
   - `get_eager_model()`: Returns the PyTorch model
   - `get_example_inputs()`: Returns tuple of example tensors
3. Register in [`model_profiling/models/__init__.py`](https://github.com/ArmDeveloperEcosystem/sme-executorch-profiling/blob/main/model_profiling/models/__init__.py):
   ```python
   from . import your_model
   register_model("your_model", YourModelClass)
   ```

The key insight: This registration system lets you add models without touching ExecuTorch source code. The exporter patches the registry at runtime, so your models appear alongside ExecuTorch's built-in models.

Advanced onboarding example: The EdgeTAM image encoder (see agent skill [`08_onboard_edgetam.md`](https://github.com/ArmDeveloperEcosystem/sme-executorch-profiling/blob/main/agent_skill_ml_profiling/08_onboard_edgetam.md) for complete onboarding workflow) demonstrates:
- Wrapper classes for input/output normalization
- Operator replacement strategies
- Shape constraint handling
- Export-friendly refactoring patterns

## Export models to PTE format

Exporting a model to `.pte` format is model-specific work. This code repository used for this learning path includes a reference exporter at [`model_profiling/export/export_model.py`](https://github.com/ArmDeveloperEcosystem/sme-executorch-profiling/blob/main/model_profiling/export/export_model.py) that demonstrates the export process.

The exporter uses a registry patching system that allows local models (in `model_profiling/models/`) to be exported without editing ExecuTorch source code. This keeps the pipeline stable while you add new models.

Supported models:
- `toy_cnn` (no extra deps; good for smoke tests)
- `mobilenet_v3_small` (requires `torchvision`; otherwise it falls back to `toy_cnn`)

Example export command:

```bash
python model_profiling/export/export_model.py \
  --model toy_cnn \
  --dtype fp16 \
  --outdir model_profiling/out_toy_cnn/artifacts/
```

Expected outputs:

- `model_profiling/out_toy_cnn/artifacts/toy_cnn_xnnpack_fp16.pte`
- `model_profiling/out_toy_cnn/artifacts/toy_cnn_xnnpack_fp16.pte.etrecord` (optional; operator metadata)

Keep exported artifacts under out_<model>/artifacts/ to separate model binaries from source and enable clean versioning.

## Configure timing and trace profiling runs

For complete analysis you must run two experiment types:
  * Timing-only runs — no kernel trace logging; use these for accurate latency comparisons (SME2 on vs SME2 off).
  * Trace-enabled runs — enable XNNPACK kernel trace logging; use these to collect kernel-selection evidence and traces for kernel-level analysis. Trace logging affects timing and should never be used to compare end-to-end latency.

Run timing-only for latency measurement, and run trace-enabled only when you need kernel-level details.

## Configure profiling experiments with JSON

Experiments are defined with JSON configs. Minimal required fields:

- `model`: path to `.pte`
- `output_root`: where to write run artifacts
- `experiments[]`: a list of runs (SME2 on/off, threads, runs, runner_path)

Use template configs in `model_profiling/configs/templates/` and examples in `model_profiling/configs/examples/` as starting points.
To inspect a template or example config:

```bash
cat model_profiling/configs/templates/mac_template.json
```

Or use the provided example:

```bash
cat model_profiling/configs/examples/mac_mobilenet_fp16.json
```

Important fields to set:
- `experiments[].runner_path`: Points to the runner binary in `executorch/cmake-out/<preset>/executor_runner` (timing-only or trace-enabled)
- `experiments[].num_runs`: Number of iterations (default 10 for statistical significance)
- `experiments[].num_threads`: Thread count (usually 1 for single-threaded performance analysis)

JSON configs are version-controlled and reproducible, and they let you run batches of experiments with consistent parameters.

## Run profiling on Android and macOS

The pipeline supports both Android (representative device testing) and macOS (developer accessibility). The same pipeline scripts are used; only runner binaries and environment differ.

### 6.1 Run on Android (for real-world edge ML performance on mobile devices)

For testing on real Arm edge mobile devices, Android runs are essential. This is the only way to validate performance on actual hardware with real thermal constraints, memory bandwidth, and device-specific optimizations.

**Critical: Device power management settings** - Power management settings significantly impact inference latency measurements. Configure your device for consistent performance mode and keep settings consistent across runs. Inconsistent power settings can cause measurement variance that obscures actual performance differences.

**Configure device settings before running**:

**Option 1: Unconstrained boost mode** (for stress testing hardware - removes all CPU frequency caps and scaling policies):
```bash
adb shell settings put global low_power 0

adb shell settings put global stay_on_while_plugged_in 15
adb shell svc power stayon true

adb shell settings put global window_animation_scale 0
adb shell settings put global transition_animation_scale 0
adb shell settings put global animator_duration_scale 0
```
These settings disable low power mode and UI animations, and force the device to stay on while plugged.

**Option 2: App developer mode** (for perceived app performance - real user daily experience):
```bash
adb shell settings put global stay_on_while_plugged_in 1

adb shell settings put global window_animation_scale 1
adb shell settings put global transition_animation_scale 1
adb shell settings put global animator_duration_scale 1

adb shell settings put global low_power 0
```
These settings disable low power mode, keep UI animations enabled, and use normal device settings.

**Verify settings**:
```bash
adb shell settings get global stay_on_while_plugged_in
adb shell settings get global low_power
adb shell dumpsys power | grep -i "stay.*awake\|thermal"
```

{{% notice  Note%}}
Unconstrained boost mode (value 15) removes all CPU frequency caps and scaling policies for stress testing hardware. App developer mode (value 1) reflects normal device usage and perceived app performance for real user daily experience. Choose based on your measurement goals and keep settings consistent across all runs.
{{% /notice %}}

Run the Android pipeline (example):

```bash
python model_profiling/scripts/android_pipeline.py --config model_profiling/configs/examples/android_mobilenet_fp16.json
python model_profiling/scripts/analyze_results.py --run-dir model_profiling/out_toy_cnn/runs/android
```
The pipeline uses adb to push and execute runners on-device, pulls ETDump traces back to the host, and runs automatic analysis.

The generated output should be similar to:

```output
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

Timing-only run example:

```bash
python model_profiling/scripts/mac_pipeline.py --config model_profiling/configs/examples/mac_mobilenet_fp16.json
```

Trace-enabled (kernel analysis) run example — use a config that points to trace-enabled runners:

```bash
python model_profiling/scripts/mac_pipeline.py --config model_profiling/configs/examples/mac_mobilenet_fp16.json
```
Validate run artifacts (optional):

```bash
python model_profiling/scripts/validate_results.py --results model_profiling/out_toy_cnn/runs/mac
```
Validation checks for JSON files, but they're not required for analysis. The analysis script works directly with ETDump files.

After a run, the following files are generated:

```output
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

The `.etdump` files are the primary data source. End-to-end latency numbers and operator-level breakdowns are derived from them. The JSON files (`manifest.json`, `metrics.json`) are optional metadata/logs for reproducibility and convenience, but analysis scripts work directly with ETDump.


## Analyze operator-level performance with ETDump

The pipeline runs `analyze_results.py` automatically after measurement. To rerun analysis manually:

```bash
python model_profiling/scripts/analyze_results.py \
  --run-dir model_profiling/out_toy_cnn/runs/mac
```

The analysis generates `model_profiling/out_toy_cnn/runs/mac/analysis_summary.json` (operator-category breakdown) and CSV files in the same directory as ETDump files (if not already generated by pipeline).

**Operator categories:**

- Convolution: Time spent in Conv2d operations (should decrease with SME2)
- GEMM: Time spent in Linear/MatMul operations (should decrease with SME2)
- Data Movement: Time spent in transpose, permute, copy operations (often increases as % after SME2)
- Elementwise: Time spent in add, mul, relu, etc. (usually small)
- Other: Everything else (check for unexpected operations)

After SME2 accelerates CONV/GEMM, you'll see data movement become a larger percentage of total time. This is expected, as SME2 reveals the next bottleneck. The visualization makes it obvious where to optimize next.

## Optimize models based on profiling results

Before SME2: CONV/GEMM dominate timing (e.g., 60-80% of total time)

Typical outcome after SME2: 
  - CONV/GEMM shrink (e.g., 20-30% of total time)
  - Data Movement grows (e.g., 40-60% of total time)
  - Overall latency decreases (the speedup)

If data movement dominates after SME2, focus optimizations on transpose elimination to reduce layout changes, layout optimization to choose layouts that minimize copies, and memory access patterns to reduce cache misses.

Use trace-enabled runs to confirm which kernel variants were selected (e.g., SME2-enabled kernels vs NEON). Remember trace-enabled runs are evidence-gathering only and should not be used for direct latency comparisons.

