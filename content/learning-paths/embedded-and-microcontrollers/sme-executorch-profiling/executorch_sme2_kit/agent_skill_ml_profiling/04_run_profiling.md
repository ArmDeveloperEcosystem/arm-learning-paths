---
name: run_profiling
description: Execute profiling runs with SME2-on and SME2-off, collect ETDump traces. Supports timing-only runs (accurate latency) and trace-enabled runs (kernel insights). Use when profiling ExecuTorch models, comparing SME2 performance, collecting operator-level traces, or analyzing kernel selection.
---

# Skill: Run Profiling Pipeline

**Purpose**: Execute profiling runs with SME2-on and SME2-off, collect ETDump traces

**When to use**: After `export_model` and `build_runners` complete

## Overview

This skill orchestrates the profiling pipeline to collect performance data. **Critical distinction**: You need **two types of runs** for complete profiling:

1. **Timing-only runs** (default): Accurate latency measurements without trace overhead
2. **Trace-enabled runs** (separate): Kernel-level insights (trace logging impacts timing, use only for kernel analysis)

The pipeline is **model-agnostic** - once you have a `.pte` file, the same commands work for any model.

**New Pipeline Architecture**: The updated pipeline scripts (`mac_pipeline.py` and `android_pipeline.py`) use a modular architecture that:
- Automatically runs analysis after profiling (generates CSV files from ETDump)
- Supports `--only` to run specific experiments
- Supports `--analysis-only` to re-run analysis without re-executing profiling
- Supports `--verbose` for detailed output
- Supports `--remote-device` for Android (remote ADB connection)

**Prerequisites**:
- `.venv/` activated
- Runners built (`executorch/cmake-out/mac-arm64/executor_runner` exists)
- Model exported (`.pte` file exists)
- Config JSON created (or use template)

## Runner Selection Guide

| Run Type | Runner Variant | Use For | Timing Impact |
|----------|---------------|---------|---------------|
| **Latency measurement** | Timing-only (default) | SME2 on/off comparison, performance benchmarks | Accurate (no overhead) |
| **Kernel analysis** | Trace-enabled | Understanding kernel selection, debugging | Overhead present (not for timing) |

**Decision**: Always use timing-only runners for latency comparisons. Use trace-enabled runners only when you need kernel selection evidence.

## Steps

### 1. Create Config JSON

**Option A (from template, recommended)**:
```bash
# Copy template
cp model_profiling/configs/templates/mac_template.json model_profiling/configs/my_run.json

# Update model path programmatically
python - <<'PY'
import json
from pathlib import Path

config_path = Path("model_profiling/configs/my_run.json")
config = json.loads(config_path.read_text())
config["model"] = "model_profiling/out_toy_cnn/artifacts/toy_cnn_xnnpack_fp16.pte"

# Verify runner paths
for exp in config.get("experiments", []):
    if "runner_path" in exp:
        runner = Path(exp["runner_path"])
        if not runner.exists():
            print(f"⚠️  Warning: Runner not found: {runner}")

config_path.write_text(json.dumps(config, indent=2))
print(f"✓ Created {config_path}")
PY
```

**Option B (use example)**:
```bash
cp model_profiling/configs/examples/mac_mobilenet_fp16.json model_profiling/configs/my_run.json
# Edit model path if needed
```

### 2. Run Timing-Only Pipeline (for latency measurement)

**macOS Example**:
```bash
python3 model_profiling/scripts/mac_pipeline.py \
  --config model_profiling/configs/my_run.json
```

**Android Example**:
```bash
python3 model_profiling/scripts/android_pipeline.py \
  --config model_profiling/configs/android_squeezesam_q8_comprehensive_cpu7.json
```

**Critical: Android device power management** - Power management settings significantly impact inference latency measurements. The `stay_on_while_plugged_in` setting is critical: value 15 removes all CPU frequency caps and scaling policies; value 1 is normal device usage. Configure your device for consistent performance mode and keep settings consistent across runs.

**Configure device settings**:

**Option 1: Unconstrained boost mode** (for stress testing hardware - removes all CPU frequency caps):
```bash
adb shell settings put global low_power 0
adb shell settings put global stay_on_while_plugged_in 15
adb shell svc power stayon true
adb shell settings put global window_animation_scale 0
adb shell settings put global transition_animation_scale 0
adb shell settings put global animator_duration_scale 0
```

**Option 2: App developer mode** (for perceived app performance - real user daily experience):
```bash
adb shell settings put global stay_on_while_plugged_in 1
adb shell settings put global window_animation_scale 1
adb shell settings put global transition_animation_scale 1
adb shell settings put global animator_duration_scale 1
adb shell settings put global low_power 0
```

**Note**: Unconstrained boost mode (value 15) removes all CPU frequency caps and scaling policies for stress testing hardware. App developer mode (value 1) reflects normal device usage and perceived app performance for real user daily experience. Keep settings consistent across all runs.

**With additional options**:
```bash
# Run only specific experiments
python3 model_profiling/scripts/mac_pipeline.py \
  --config model_profiling/configs/my_run.json \
  --only mac_sme2_on mac_sme2_off

# Verbose output
python3 model_profiling/scripts/mac_pipeline.py \
  --config model_profiling/configs/my_run.json \
  --verbose

# Android with remote device
python3 model_profiling/scripts/android_pipeline.py \
  --config model_profiling/configs/android_config.json \
  --remote-device 10.1.16.56:5555
```

This uses standard runners with no trace logging overhead → accurate latency measurements.

### 3. Verify Outputs

```bash
python model_profiling/scripts/validate_results.py --results model_profiling/out_<model>/runs/mac
```

**Verification**:

```bash
# Check ETDump files exist and are non-empty
test -f model_profiling/out_<model>/runs/mac/*/mac_sme2_on_t1.etdump && echo "✓ SME2-on ETDump exists"
test -f model_profiling/out_<model>/runs/mac/*/mac_sme2_off_t1.etdump && echo "✓ SME2-off ETDump exists"

# Verify ETDump files are non-empty (critical)
for etdump in model_profiling/out_<model>/runs/mac/*/*.etdump; do
  test -s "$etdump" && echo "✓ $etdump is non-empty" || echo "✗ $etdump is empty"
done

# Validate results structure
python3 model_profiling/scripts/validate_results.py \
  --results model_profiling/out_<model>/runs/mac
```

**Expected outputs**:
- `model_profiling/out_<model>/runs/mac/<model_stem>_<experiment_name>_t<threads>.etdump` (ETDump traces - **primary data**)
- `model_profiling/out_<model>/runs/mac/<model_stem>_<experiment_name>_t<threads>_latency.log` (runner logs)
- `model_profiling/out_<model>/runs/mac/<model_stem>_pipeline_summary.json` (pipeline summary with robust statistics)
- `model_profiling/out_<model>/runs/mac/<model_stem>_pipeline_summary.md` (pipeline summary markdown)
- **CSV files** (automatically generated from ETDump):
  - `*_exec_all_runs_timeline.csv` - Timeline with all runs (used for latency statistics)
  - `*_exec_run0_timeline.csv` - Timeline for run 0 (operator-level analysis)
  - `*_exec_ops_stats.csv` - Aggregated operator statistics

## Trace-Enabled Runs (for kernel-level analysis)

**Important**: Trace logging impacts timing. Use these runs **only** for kernel analysis, not latency measurements.

If you need kernel-level insights:

1. Build trace-enabled runners (separate build with XNNPACK kernel logging flags)
2. Create separate config with `"mode": "xnntrace"` in experiments
3. Run pipeline again with trace config
4. Analyze kernel hints in results

See `references/kernel-tracing.md` for detailed instructions.

## Failure Handling

| Issue | Symptom | Fix |
|-------|---------|-----|
| **Runner not found** | `FileNotFoundError` or config error | Re-run `02_build_runners.md`, verify paths in config |
| **Model not found** | `Model file not found` | Verify `.pte` path in config matches exported file location |
| **Permission errors** | `Permission denied` | `chmod +x executorch/cmake-out/*/executor_runner` |
| **Empty ETDump** | ETDump file exists but is 0 bytes | Check runner logs, verify ExecuTorch build has event tracer enabled |
| **Build mismatch** | Runner crashes or errors | Ensure runner was built with same ExecuTorch version as export |

## Common Workflows

### Workflow 1: Quick Latency Comparison (macOS)

```bash
# 1. Export model
python3 model_profiling/export/export_model.py \
  --model toy_cnn \
  --dtype fp16 \
  --outdir model_profiling/out_toy_cnn/artifacts/

# 2. Create config (pointing to timing-only runners)
# Edit config to use: executorch/cmake-out/mac-arm64/executor_runner

# 3. Run pipeline (automatically runs analysis and generates CSV files)
python3 model_profiling/scripts/mac_pipeline.py \
  --config model_profiling/configs/my_run.json

# 4. Generate report (optional - uses CSV files generated by pipeline)
python3 model_profiling/scripts/generate_report.py \
  --run-dir model_profiling/out_toy_cnn/runs/mac
```

### Workflow 2: Quick Latency Comparison (Android)

**Critical: Device power management** - Configure Android device power settings before running. The `stay_on_while_plugged_in` setting is critical: value 15 removes all CPU frequency caps (stress testing); value 1 is normal device usage (real user experience). Keep settings consistent across runs.

**Configure device settings**:

**Unconstrained boost mode** (value 15 - for stress testing hardware):
```bash
adb shell settings put global low_power 0
adb shell settings put global stay_on_while_plugged_in 15
adb shell svc power stayon true
adb shell settings put global window_animation_scale 0
adb shell settings put global transition_animation_scale 0
adb shell settings put global animator_duration_scale 0
```

**App developer mode** (value 1 - for perceived app performance):
```bash
adb shell settings put global stay_on_while_plugged_in 1
adb shell settings put global window_animation_scale 1
adb shell settings put global transition_animation_scale 1
adb shell settings put global animator_duration_scale 1
adb shell settings put global low_power 0
```

```bash
# 1. Export model
python3 model_profiling/export/export_model.py \
  --model toy_cnn \
  --dtype fp16 \
  --outdir model_profiling/out_toy_cnn/artifacts/

# 2. Create config (pointing to Android runners)
# Edit config to use: executorch/cmake-out/android-arm64/executor_runner

# 3. Run pipeline (with optional remote device, automatically runs analysis)
python3 model_profiling/scripts/android_pipeline.py \
  --config model_profiling/configs/android_toy_cnn_run.json \
  --remote-device 10.1.16.56:5555  # Optional: for remote ADB connection

# 4. Generate report (optional - uses CSV files generated by pipeline)
python3 model_profiling/scripts/generate_report.py \
  --run-dir model_profiling/out_toy_cnn/runs/android
```

### Workflow 3: Full Analysis (Timing + Kernel)

```bash
# 1. Timing-only run (for latency)
python3 model_profiling/scripts/mac_pipeline.py \
  --config model_profiling/configs/timing_config.json

# 2. Trace-enabled run (for kernel insights, automatically extracts kernel info)
python3 model_profiling/scripts/mac_pipeline.py \
  --config model_profiling/configs/trace_config.json

# 3. Generate report (optional - uses CSV files and kernel view tables from pipeline)
python3 model_profiling/scripts/generate_report.py \
  --run-dir model_profiling/out_toy_cnn/runs/mac
```

### Workflow 4: Re-run Analysis Only (Skip Execution)

```bash
# Re-analyze existing ETDump files without re-running profiling
python3 model_profiling/scripts/mac_pipeline.py \
  --config model_profiling/configs/my_run.json \
  --analysis-only
```

## Best Practices

- **Always use timing-only runners for latency comparisons** - trace logging adds overhead
- **Keep configs version-controlled** - record model paths, runner paths, experiment names
- **Verify ETDump files are non-empty** - empty files indicate runner issues
- **Run multiple iterations** - default is 10 runs; adjust in config for statistical significance
- **Record ExecuTorch SHA** - manifest.json includes it for reproducibility

## Implementation Checklist

- [ ] Config JSON created with correct model path
- [ ] Runner paths verified in config (point to `executorch/cmake-out/mac-arm64*/executor_runner`)
- [ ] Timing-only pipeline executed successfully
- [ ] ETDump files exist and are non-empty
- [ ] Validation script passes
- [ ] (Optional) Trace-enabled runs completed if kernel analysis needed

**Command Examples**:

**macOS Pipeline**:
```bash
# Basic usage
python3 model_profiling/scripts/mac_pipeline.py \
  --config model_profiling/configs/my_run.json

# Run only specific experiments
python3 model_profiling/scripts/mac_pipeline.py \
  --config model_profiling/configs/my_run.json \
  --only mac_sme2_on mac_sme2_off

# Verbose output
python3 model_profiling/scripts/mac_pipeline.py \
  --config model_profiling/configs/my_run.json \
  --verbose

# Re-run analysis only (skip execution)
python3 model_profiling/scripts/mac_pipeline.py \
  --config model_profiling/configs/my_run.json \
  --analysis-only
```

**Android Pipeline**:
```bash
# Basic usage
python3 model_profiling/scripts/android_pipeline.py \
  --config model_profiling/configs/android_squeezesam_q8_comprehensive_cpu7.json

# With remote device connection
python3 model_profiling/scripts/android_pipeline.py \
  --config model_profiling/configs/android_config.json \
  --remote-device 10.1.16.56:5555

# Run only specific experiments with verbose output
python3 model_profiling/scripts/android_pipeline.py \
  --config model_profiling/configs/android_config.json \
  --only android_sme2_on android_sme2_off \
  --verbose
```

**References**:
- Pipeline script: `model_profiling/scripts/mac_pipeline.py`
- Android pipeline: `model_profiling/scripts/android_pipeline.py`
- Config templates: `model_profiling/configs/templates/`
- Validation script: `model_profiling/scripts/validate_results.py`
- Learning path: `03-pipeline-and-analysis.md` (detailed pipeline explanation)

**Assets**:
- `model_profiling/scripts/mac_pipeline.py` - macOS profiling pipeline
- `model_profiling/scripts/android_pipeline.py` - Android profiling pipeline
- `model_profiling/scripts/perf_runner.py` - Performance runner (used by MacRunner)
- `model_profiling/configs/templates/mac_template.json` - Config template
- `model_profiling/configs/templates/android_template.json` - Android config template
- `model_profiling/configs/examples/` - Example configs

**Next skill**: `05_analyze_results.md`
