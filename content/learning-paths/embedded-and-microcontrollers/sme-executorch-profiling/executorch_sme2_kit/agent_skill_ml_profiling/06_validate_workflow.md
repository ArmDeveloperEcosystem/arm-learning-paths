---
name: validate_workflow
description: End-to-end smoke test to validate the complete profiling workflow. Runs setup, build, export, profiling, and analysis in a single command. Use for first-time validation, CI/CD pipelines, troubleshooting, or quick sanity checks after environment changes.
---

# Skill: Validate Workflow

**Purpose**: End-to-end smoke test to validate the complete profiling workflow

**When to use**: 
- After initial setup (first-time validation)
- In CI/CD pipelines (automated validation)
- When troubleshooting workflow issues
- Quick sanity check after environment changes
- Before committing changes to profiling pipeline

## Overview

This skill runs a **complete end-to-end validation** of the profiling workflow using a minimal toy model. It orchestrates all previous skills in sequence:

1. Validates setup (or runs setup if needed)
2. Builds runners (if not already built)
3. Exports toy CNN model
4. Runs Mac pipeline (SME2 on/off)
5. Validates results structure
6. Runs analysis

**Key benefit**: Single command validates the entire workflow. If this passes, you know the environment is correctly configured.

**Prerequisites**:
- Workspace set up (or will be set up by this skill)
- Network access for cloning ExecuTorch (if setup needed)

## Steps

### Run End-to-End Smoke Test

```bash
python model_profiling/scripts/run_quick_test.py
```

This single command:
- Validates setup (or runs setup if needed)
- Builds runners (if not already built)
- Exports toy CNN model (`toy_cnn_xnnpack_fp16.pte`)
- Runs Mac pipeline (SME2 on/off) - **automatically runs analysis and generates CSV files**
- Validates results structure

**Verification**:

```bash
# Check all expected artifacts exist
test -f model_profiling/out_toy_cnn/artifacts/toy_cnn_xnnpack_fp16.pte && echo "✓ Model exported"
test -f executorch/cmake-out/mac-arm64/executor_runner && echo "✓ Runners built"
test -f model_profiling/out_toy_cnn/runs/mac/*/*.etdump && echo "✓ Profiling completed"
test -f model_profiling/out_toy_cnn/runs/mac/*/*_all_runs_timeline.csv && echo "✓ CSV files generated"
test -f model_profiling/out_toy_cnn/runs/mac/*_pipeline_summary.json && echo "✓ Pipeline summary generated"

# Run comprehensive validation
python model_profiling/scripts/validate_setup.py
python model_profiling/scripts/validate_results.py --results model_profiling/out_toy_cnn/runs/mac
```

**Expected outputs**:
- All artifacts from `01_setup_workspace`, `02_build_runners`, `03_export_model`, `04_run_profiling`, and `05_analyze_results`
- Exit code 0 from all validation scripts
- Complete workflow validated end-to-end

## Failure Handling

| Issue | Symptom | Fix |
|-------|---------|-----|
| **Setup failures** | ExecuTorch clone/install errors | Check prerequisites, network connectivity, see `01_setup_workspace.md` |
| **Build failures** | Runner build errors | Review build logs, check CMake/Ninja versions, see `02_build_runners.md` |
| **Export failures** | Model export errors | Verify model registration, check export logs, see `03_export_model.md` |
| **Pipeline failures** | Profiling errors | Check runner paths, model paths, config validity, see `04_run_profiling.md` |
| **Analysis failures** | Analysis errors | Verify ETDump files exist and are valid, see `05_analyze_results.md` |

## Use Cases

### 1. First-Time Setup Validation

```bash
# Fresh workspace - validates everything
python model_profiling/scripts/run_quick_test.py
```

### 2. CI/CD Pipeline

```bash
# In CI: fail fast if workflow broken
python model_profiling/scripts/run_quick_test.py || exit 1
```

### 3. Troubleshooting

```bash
# After environment changes - quick sanity check
python model_profiling/scripts/run_quick_test.py
```

### 4. Pre-Commit Validation

```bash
# Before committing changes - ensure workflow still works
python model_profiling/scripts/run_quick_test.py
```

## Success Criteria

- [ ] All validation checks pass
- [ ] All expected artifacts present
- [ ] No error messages in logs
- [ ] Exit code 0 from smoke test script
- [ ] ETDump files are non-empty
- [ ] Analysis summary has timing data

## What Gets Validated

| Component | Validation |
|-----------|-----------|
| **Setup** | ExecuTorch importable, submodules initialized |
| **Runners** | Binaries exist, executable, respond to `--help` |
| **Export** | `.pte` file exists and is non-empty |
| **Profiling** | ETDump files exist and are non-empty |
| **Analysis** | Summary JSON exists with timing data |

## Best Practices

- **Run after environment changes** - Quick way to verify everything still works
- **Use in CI/CD** - Automated validation prevents broken workflows
- **Check logs on failure** - Script outputs detailed error messages
- **Don't skip steps** - This validates the complete workflow, not individual components

## Implementation Checklist

- [ ] Smoke test script executed
- [ ] All artifacts present (model, runners, ETDump, analysis)
- [ ] Validation scripts pass
- [ ] No errors in output
- [ ] Exit code 0

**References**:
- Smoke test script: `model_profiling/scripts/run_quick_test.py`
- Validation scripts: `model_profiling/scripts/validate_setup.py`, `model_profiling/scripts/validate_results.py`
- Learning path: `01-overview.md` (quickstart section)
- Use case doc: `test-cases/use-cases/01-smoke-test-mac.md`

**Assets**:
- `model_profiling/scripts/run_quick_test.py` - End-to-end smoke test
- `test-cases/use-cases/01-smoke-test-mac.md` - Detailed smoke test documentation
