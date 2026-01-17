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

```bash
python model_profiling/scripts/mac_pipeline.py --config model_profiling/configs/my_run.json
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
python model_profiling/scripts/validate_results.py --results model_profiling/out_<model>/runs/mac
```

**Expected outputs**:
- `model_profiling/out_<model>/runs/mac/<experiment_name>/<experiment_name>_t1.etdump` (ETDump traces - **primary data**)
- `model_profiling/out_<model>/runs/mac/<experiment_name>/<experiment_name>_t1.log` (runner logs)
- Optionally: `model_profiling/out_<model>/runs/mac/manifest.json` and `model_profiling/out_<model>/runs/mac/metrics.json` (metadata logs, not critical)

## Trace-Enabled Runs (for kernel-level analysis)

**Important**: Trace logging impacts timing. Use these runs **only** for kernel analysis, not latency measurements.

If you need kernel-level insights:

1. Build trace-enabled runners (separate build with XNNPACK kernel logging flags)
2. Create separate config pointing to trace-enabled runners
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

### Workflow 1: Quick Latency Comparison

```bash
# 1. Export model
python model_profiling/export/export_model.py --model toy_cnn --dtype fp16 --outdir model_profiling/out_toy_cnn/artifacts/

# 2. Create config (pointing to timing-only runners)
# Edit config to use: executorch/cmake-out/mac-arm64/executor_runner

# 3. Run pipeline
python model_profiling/scripts/mac_pipeline.py --config model_profiling/configs/my_run.json

# 4. Compare latencies
python model_profiling/scripts/analyze_results.py --run-dir model_profiling/out_toy_cnn/runs/mac
```

### Workflow 2: Full Analysis (Timing + Kernel)

```bash
# 1. Timing-only run (for latency)
python model_profiling/scripts/mac_pipeline.py --config model_profiling/configs/timing_config.json

# 2. Trace-enabled run (for kernel insights)
python model_profiling/scripts/mac_pipeline.py --config model_profiling/configs/trace_config.json

# 3. Analyze both
python model_profiling/scripts/analyze_results.py --run-dir model_profiling/out_toy_cnn/runs/mac
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

**References**:
- Pipeline script: `model_profiling/scripts/mac_pipeline.py`
- Android pipeline: `model_profiling/scripts/android_pipeline.py`
- Config templates: `model_profiling/configs/templates/`
- Validation script: `model_profiling/scripts/validate_results.py`
- Learning path: `03-pipeline-and-analysis.md` (detailed pipeline explanation)

**Assets**:
- `model_profiling/scripts/mac_pipeline.py` - macOS profiling pipeline
- `model_profiling/scripts/android_pipeline.py` - Android profiling pipeline
- `model_profiling/configs/templates/mac_template.json` - Config template
- `model_profiling/configs/templates/android_template.json` - Android config template
- `model_profiling/configs/examples/` - Example configs

**Next skill**: `05_analyze_results.md`
