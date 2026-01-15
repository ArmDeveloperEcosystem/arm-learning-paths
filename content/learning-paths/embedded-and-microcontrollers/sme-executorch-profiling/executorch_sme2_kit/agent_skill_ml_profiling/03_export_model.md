---
name: export_model
description: Export a PyTorch model to ExecuTorch .pte format for profiling. Supports built-in models (toy_cnn) and custom registered models. Use when preparing models for profiling, converting PyTorch to ExecuTorch format, or generating .pte artifacts for pipeline runs.
---

# Skill: Export Model

**Purpose**: Export a PyTorch model to ExecuTorch `.pte` format for profiling

**When to use**: 
- After `setup_workspace` completes
- Before `run_profiling` (model must be exported first)
- When onboarding a new model to the profiling workflow
- When regenerating `.pte` files after model changes

## Overview

This skill exports PyTorch models to ExecuTorch's portable format (`.pte`). The exporter uses a **registry patching system** that allows local models (in `model_profiling/models/`) to be exported without editing ExecuTorch source code.

**Key principle**: Models are exported to `out_<model_name>/artifacts/` to keep the `models/` directory clean (source code only). This follows the best practice from the working repository.

**Prerequisites**:
- `.venv/` activated
- ExecuTorch installed (from setup_workspace)
- Model registered in `model_profiling/models/` (or use built-in `toy_cnn`)

## Model Selection

| Model | Use Case | Dependencies | Notes |
|-------|----------|-------------|-------|
| `toy_cnn` | Smoke tests, quick validation | None | Built-in, no extra deps |
| `mobilenet_v3_small` | Real-world CV model | `torchvision` | Requires torchvision package |
| Custom models | Your own models | Model-specific | Must implement `EagerModelBase` |

## Steps

### 1. Activate Virtual Environment

```bash
source .venv/bin/activate
```

### 2. Export Model

```bash
python model_profiling/export/export_model.py \
  --model <model_name> \
  --dtype fp16 \
  --outdir model_profiling/out_<model_name>/artifacts/
```

**Example with built-in toy model**:
```bash
python model_profiling/export/export_model.py \
  --model toy_cnn \
  --dtype fp16 \
  --outdir model_profiling/out_toy_cnn/artifacts/
```

**Example with MobileNet** (if torchvision available):
```bash
python model_profiling/export/export_model.py \
  --model mobilenet_v3_small \
  --dtype fp16 \
  --outdir model_profiling/out_mobilenet/artifacts/
```

### 3. Verify Export

```bash
ls -lh model_profiling/out_<model_name>/artifacts/*.pte
```

**Verification**:

```bash
# Check .pte file exists and is non-empty
PTE_FILE="model_profiling/out_<model_name>/artifacts/<model>_xnnpack_fp16.pte"
test -f "$PTE_FILE" && echo "✓ .pte file exists"
test -s "$PTE_FILE" && echo "✓ .pte file is non-empty"

# Optional: check .etrecord exists (if available)
ETRECORD="${PTE_FILE}.etrecord"
if [ -f "$ETRECORD" ]; then
  echo "✓ .etrecord file exists (optional, for operator attribution)"
else
  echo "ℹ️  .etrecord not generated (analysis still works, but operator names may be generic)"
fi

# Validate with setup script
python model_profiling/scripts/validate_setup.py --model "$PTE_FILE"
```

**Expected outputs**:
- `model_profiling/out_<model_name>/artifacts/<model>_xnnpack_fp16.pte` (or `_fp32.pte`)
- Optionally: `model_profiling/out_<model_name>/artifacts/<model>_xnnpack_fp16.pte.etrecord` (operator metadata)

## Export Options

| Option | Values | Default | Description |
|--------|--------|---------|-------------|
| `--model` | Model name | Required | Model to export (must be registered) |
| `--dtype` | `fp16`, `fp32` | `fp16` | Data type for export |
| `--backend` | `xnnpack`, `portable` | `xnnpack` | Backend partitioner |
| `--outdir` | Directory path | Required | Output directory (creates `out_<model>/artifacts/`) |
| `--quantize` | Flag | `False` | Produce INT8 quantized model |
| `--save-graph` | Flag | `False` | Emit `graph.json` alongside `.pte` |
| `--verbose` | Flag | `False` | Verbose logging |

## Failure Handling

| Issue | Symptom | Fix |
|-------|---------|-----|
| **Model not found** | `Unknown model '<name>'` | Check model is registered in `model_profiling/models/__init__.py` |
| **Export errors** | Unsupported ops, dynamic control flow | Review model code, refactor to avoid unsupported operations |
| **Out of memory** | OOM during export | Reduce model size or use smaller input shapes |
| **Missing dependencies** | Import errors | Ensure ExecuTorch is properly installed: `python -c "import executorch"` |
| **Backend errors** | XNNPACK partitioner failures | Check submodules initialized, verify ExecuTorch build |

## Model Onboarding (Advanced)

To add a new model:

1. Create `model_profiling/models/<model_name>/` directory
2. Implement `EagerModelBase` interface in `model.py`
3. Register in `model_profiling/models/__init__.py`
4. Export using the same command

See `references/model-onboarding.md` for detailed guide.

## Best Practices

- **Use `out_<model>/artifacts/` pattern** - Keeps `models/` directory clean (source code only)
- **Record export parameters** - Note dtype, backend, quantization settings for reproducibility
- **Validate .pte immediately** - Check file exists and is non-empty before proceeding
- **Keep .etrecord if available** - Helps with operator name attribution in analysis (optional)

## Implementation Checklist

- [ ] Virtual environment activated
- [ ] Model name verified (registered in model registry)
- [ ] Export command executed successfully
- [ ] `.pte` file exists and is non-empty
- [ ] (Optional) `.etrecord` file exists
- [ ] Validation script passes

**References**:
- Export script: `model_profiling/export/export_model.py`
- Model registry: `model_profiling/models/__init__.py`
- Model base interface: `model_profiling/models/model_base.py`
- Learning path: `02-setup-and-model-onboarding.md` (model onboarding guide)

**Assets**:
- `model_profiling/export/export_model.py` - Model export script with registry patching
- `model_profiling/models/` - Model registry and onboarding scaffolding
- `model_profiling/models/toy_cnn/` - Example model implementation

**Next skill**: `04_run_profiling.md`
