# Pipeline Commands Reference

This document shows the **actual commands** end users run to profile their models. This is the workflow you follow after setting up the environment.

## Workflow Overview

The profiling pipeline is **model-agnostic**. Once you have a `.pte` file, the same commands work for any model.

```
Setup → Build Runners → Export Model → Run Pipeline → Analyze Results
```

## Step-by-Step Commands

### 1. Setup Environment (One-time)

```bash
# From executorch_sme2_kit/ directory
bash model_profiling/scripts/setup_repo.sh
```

This creates:
- `.venv/` - Python virtual environment
- `executorch/` - ExecuTorch checkout

### 2. Build Runners (One-time, or when CMake configs change)

```bash
# From executorch_sme2_kit/ directory
bash model_profiling/scripts/build_runners.sh
```

This builds:
- `executorch/cmake-out/mac-arm64/executor_runner` (SME2 ON)
- `executorch/cmake-out/mac-arm64-sme2-off/executor_runner` (SME2 OFF)
- Android runners (if `ANDROID_NDK` is set)

### 3. Export Your Model (Per-model)

```bash
# From executorch_sme2_kit/ directory
# Activate venv first
source .venv/bin/activate

# Export model
python model_profiling/export/export_model.py \
  --model <model_name> \
  --dtype fp16 \
  --outdir out_<model>/artifacts/

# This creates:
# - out_<model>/artifacts/<model>_xnnpack_fp16.pte
# - out_<model>/artifacts/<model>_xnnpack_fp16.pte.etrecord
```

**Model-specific notes:**
- For models in `model_profiling/models/`, use the registered name
- For custom models, you may need to add model registration code first
- See learning path documentation for model onboarding details

### 4. Create Pipeline Config (Per-experiment)

```bash
# Copy template
cp model_profiling/configs/templates/mac_template.json \
   model_profiling/configs/my_experiment.json

# Edit the config:
# - Set "model" to your .pte path (e.g., "out_<model>/artifacts/<model>_xnnpack_fp16.pte")
# - Adjust "experiments" array (SME2 on/off, threads, runs, etc.)
# - Set "output_root" (e.g., "out_<model>/runs/mac")
```

### 5. Run Profiling Pipeline (Per-experiment)

**macOS:**
```bash
# From executorch_sme2_kit/ directory
source .venv/bin/activate

python model_profiling/scripts/mac_pipeline.py \
  --config model_profiling/configs/my_experiment.json
```

**Android:**
```bash
# Ensure device is connected and ANDROID_NDK is set
python model_profiling/scripts/android_pipeline.py \
  --config model_profiling/configs/android_experiment.json \
  --device-serial <optional-device-id>
```

This creates:
- `out_<model>/runs/<platform>/` - Run output directory
- `out_<model>/runs/<platform>/manifest.json` - Run metadata
- `out_<model>/runs/<platform>/metrics.json` - Timing metrics
- `out_<model>/runs/<platform>/<experiment_name>/` - Per-experiment results
  - `*.etdump` - ETDump trace files
  - `*.log` - Runner logs

### 6. Analyze Results (Per-run)

```bash
# From executorch_sme2_kit/ directory
source .venv/bin/activate

python model_profiling/scripts/analyze_results.py \
  --run-dir out_<model>/runs/mac \
  --quiet
```

This creates:
- `out_<model>/runs/mac/analysis_summary.json` - Operator-level breakdown

### 7. Validate Results (Optional)

```bash
python model_profiling/scripts/validate_results.py \
  --results out_<model>/runs/mac
```

## Quick Test (End-to-End Validation)

After setup and build, validate everything works:

```bash
# From executorch_sme2_kit/ directory
source .venv/bin/activate

python model_profiling/scripts/run_quick_test.py
```

This runs: validate → build → export toy model → pipeline → analyze → validate

## Directory Structure After Running

```
executorch_sme2_kit/
├── .venv/                          # Python environment
├── executorch/                     # ExecuTorch checkout
│   └── cmake-out/
│       ├── mac-arm64/executor_runner
│       └── mac-arm64-sme2-off/executor_runner
├── model_profiling/
│   ├── scripts/                    # Pipeline scripts
│   ├── export/                     # Export script
│   ├── configs/                    # Experiment configs
│   └── models/                     # Model registry
├── out_<model>/                    # Per-model outputs
│   ├── artifacts/                  # Exported .pte files
│   └── runs/                       # Profiling results
│       └── mac/
│           ├── manifest.json
│           ├── metrics.json
│           ├── analysis_summary.json
│           └── <experiment_name>/
│               ├── *.etdump
│               └── *.log
└── models/                         # Legacy location (if used)
```

## Key Principles

1. **Model-agnostic pipeline**: Once you have a `.pte`, the same pipeline commands work
2. **Config-driven experiments**: JSON configs define what to run, scripts execute them
3. **Output organization**: Results go under `out_<model>/runs/<platform>/` for clear organization
4. **Version traceability**: Runners stay in `executorch/cmake-out/` to track ExecuTorch version

## Common Workflows

### Compare SME2 On vs Off

1. Export model once
2. Create config with two experiments (SME2 on, SME2 off)
3. Run pipeline
4. Analyze results to see operator-level differences

### Profile Multiple Thread Counts

1. Export model once
2. Create config with `"threads": [1, 2, 4]` in experiments
3. Run pipeline
4. Compare metrics.json across thread counts

### Trace-Enabled Runs (Kernel Analysis)

1. Build trace-enabled runners (separate CMake preset)
2. Create config pointing to trace-enabled runners
3. Run pipeline (note: trace logging impacts timing)
4. Analyze ETDump for kernel selection insights

## Troubleshooting

- **"executor_runner not found"**: Run `build_runners.sh` first
- **"Model not found"**: Check `.pte` path in config JSON
- **"No .etdump files"**: Check runner logs in experiment directory
- **"Analysis failed"**: Ensure `.etrecord` file exists (re-export if needed)
