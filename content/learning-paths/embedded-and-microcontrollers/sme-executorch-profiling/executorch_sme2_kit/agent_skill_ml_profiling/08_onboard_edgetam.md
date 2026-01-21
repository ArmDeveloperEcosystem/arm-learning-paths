---
name: onboard_edgetam
description: "Onboard EdgeTAM image encoder module for profiling. Clones EdgeTAM repository, extracts the image encoder module, creates model wrapper, and registers the model. Note: EdgeTAM has multiple modules (image encoder, memory encoder, decoder, etc.); this skill onboards only the image encoder for simplicity. Use when adding EdgeTAM image encoder to the profiling workflow, setting up EdgeTAM image encoder for ExecuTorch export, or onboarding EdgeTAM image encoder as a new model."
---

# Skill: Onboard EdgeTAM Image Encoder

**Purpose**: Onboard EdgeTAM image encoder model for profiling by cloning the repository and setting up the model wrapper. **Note**: EdgeTAM is a full video segmentation model with multiple modules (image encoder, memory encoder, decoder, etc.). This skill onboards only the **image encoder module** for simplicity and to demonstrate advanced model onboarding patterns. Other EdgeTAM modules would require separate extraction and onboarding if needed.

**When to use**: 
- When adding EdgeTAM image encoder to the profiling workflow
- When setting up EdgeTAM image encoder for ExecuTorch export
- When onboarding EdgeTAM image encoder as a new model to the local registry
- When learning advanced model onboarding patterns (module extraction, wrapper creation)

## Overview

This skill onboards the EdgeTAM (On-Device Track Anything Model) **image encoder module** for profiling. EdgeTAM is a full video segmentation model with multiple modules (image encoder, memory encoder, decoder, etc.). This skill focuses on the image encoder module only for simplicity and to demonstrate advanced model onboarding patterns. Other EdgeTAM modules would require separate extraction and onboarding if needed.

The process involves:

1. Cloning the EdgeTAM repository into the correct location
2. Creating a model wrapper that extracts the image encoder
3. Registering the model in the local registry

**EdgeTAM Details**:
- **Model**: EdgeTAM Image Encoder (extracted from full EdgeTAM model)
- **Scope**: This skill onboards only the image encoder module. EdgeTAM has other modules (memory encoder, decoder, etc.) that would require separate extraction and onboarding if needed.
- **Input**: Single image tensor `(1, 3, 1024, 1024)`
- **Repository**: https://github.com/facebookresearch/EdgeTAM
- **Location**: `model_profiling/models/edgetam/edgetam_core/`

**Prerequisites**:
- `.venv/` activated
- ExecuTorch installed (from `01_setup_workspace`)
- Git installed
- Network access to clone repository

## Steps

### 1. Activate Virtual Environment

```bash
source .venv/bin/activate
```

### 2. Create Model Directory

```bash
# Create EdgeTAM model directory structure
mkdir -p model_profiling/models/edgetam
```

### 3. Clone EdgeTAM Repository

```bash
# Clone EdgeTAM repository into the correct location
EDGETAM_DIR="model_profiling/models/edgetam/edgetam_core"

if [ ! -d "$EDGETAM_DIR" ]; then
    echo "Cloning EdgeTAM repository..."
    git clone https://github.com/facebookresearch/EdgeTAM.git "$EDGETAM_DIR"
    echo "✓ EdgeTAM repository cloned"
else
    echo "✓ EdgeTAM repository already exists"
fi

# Verify repository was cloned
test -d "$EDGETAM_DIR" && test -f "$EDGETAM_DIR/setup.py" && echo "✓ Repository verified"
```

### 4. Download Checkpoint (Optional - if not already present)

```bash
# Create checkpoints directory
mkdir -p "$EDGETAM_DIR/checkpoints"

# Download checkpoint if not present
CHECKPOINT_URL="https://github.com/facebookresearch/EdgeTAM/raw/main/checkpoints/edgetam.pt"
CHECKPOINT_PATH="$EDGETAM_DIR/checkpoints/edgetam.pt"

if [ ! -f "$CHECKPOINT_PATH" ]; then
    echo "Downloading EdgeTAM checkpoint..."
    curl -L -o "$CHECKPOINT_PATH" "$CHECKPOINT_URL" || wget -O "$CHECKPOINT_PATH" "$CHECKPOINT_URL"
    echo "✓ Checkpoint downloaded"
else
    echo "✓ Checkpoint already exists"
fi

# Verify checkpoint exists
test -f "$CHECKPOINT_PATH" && test -s "$CHECKPOINT_PATH" && echo "✓ Checkpoint verified"
```

### 5. Generate Model Wrapper

Create the model wrapper that loads EdgeTAM image encoder:

```bash
# Generate model.py
cat > model_profiling/models/edgetam/model.py << 'PYEOF'
"""EdgeTAM Image Encoder model implementation."""

from __future__ import annotations

import logging
import sys
from pathlib import Path
from typing import Tuple

import torch

from ..model_base import EagerModelBase

# Add edgetam_core to path
EDGETAM_DIR = Path(__file__).resolve().parent
EDGETAM_CORE = EDGETAM_DIR / "edgetam_core"
if EDGETAM_CORE.exists():
    sys.path.insert(0, str(EDGETAM_CORE))


class EdgeTAMImageEncoderModel(EagerModelBase):
    """EdgeTAM Image Encoder model wrapper for profiling."""

    def __init__(self):
        super().__init__()
        self._model = None

    def _load_model(self) -> torch.nn.Module:
        """Lazy load the EdgeTAM image encoder."""
        if self._model is not None:
            return self._model

        checkpoint_path = EDGETAM_CORE / "checkpoints" / "edgetam.pt"
        config_path = EDGETAM_CORE / "sam2" / "configs" / "edgetam.yaml"

        if not checkpoint_path.exists():
            raise FileNotFoundError(
                f"EdgeTAM checkpoint not found: {checkpoint_path}. "
                "Download from: https://github.com/facebookresearch/EdgeTAM/tree/main/checkpoints"
            )

        if not config_path.exists():
            raise FileNotFoundError(f"EdgeTAM config not found: {config_path}")

        logging.info("Loading EdgeTAM model...")
        try:
            from hydra import initialize_config_dir, compose
            from hydra.core.global_hydra import GlobalHydra
            from hydra.utils import instantiate
            from omegaconf import OmegaConf

            # Initialize Hydra with the config directory
            config_dir = str(EDGETAM_CORE / "sam2" / "configs")
            
            # Clear any existing Hydra instance
            if GlobalHydra.instance().is_initialized():
                GlobalHydra.instance().clear()
            
            # Initialize with config directory
            with initialize_config_dir(config_dir=config_dir, version_base=None):
                # Compose the config
                cfg = compose(config_name="edgetam.yaml")
                OmegaConf.resolve(cfg)
                
                # Instantiate the model
                full_model = instantiate(cfg.model, _recursive_=True)
                
                # Load checkpoint
                checkpoint = torch.load(str(checkpoint_path), map_location="cpu")
                if "model" in checkpoint:
                    full_model.load_state_dict(checkpoint["model"], strict=False)
                else:
                    full_model.load_state_dict(checkpoint, strict=False)
                
                full_model.eval()
                
                # Extract just the image encoder
                image_encoder = full_model.image_encoder
                image_encoder.eval()
                logging.info("Loaded EdgeTAM image encoder")
                self._model = image_encoder
                return image_encoder
        except ImportError as e:
            raise ImportError(
                f"Missing dependency: {e}. Install with: pip install hydra-core omegaconf"
            ) from e
        except Exception as e:
            raise RuntimeError(f"Failed to load EdgeTAM image encoder: {e}") from e

    def get_eager_model(self) -> torch.nn.Module:
        """Return the EdgeTAM image encoder model."""
        return self._load_model()

    def get_example_inputs(self) -> Tuple[torch.Tensor, ...]:
        """Return example image input for EdgeTAM image encoder.
        
        EdgeTAM uses image_size=1024 as per config.
        Input shape: (batch, channels, height, width) = (1, 3, 1024, 1024)
        """
        return (torch.randn(1, 3, 1024, 1024),)
PYEOF

echo "✓ Model wrapper generated"
```

### 6. Generate Model Registration

Create the `__init__.py` file to register the model:

```bash
# Generate __init__.py
cat > model_profiling/models/edgetam/__init__.py << 'PYEOF'
"""EdgeTAM Image Encoder model for profiling."""

from __future__ import annotations

from .model import EdgeTAMImageEncoderModel
from .. import register_model

register_model("edgetam_image_encoder", EdgeTAMImageEncoderModel)
PYEOF

echo "✓ Model registration generated"
```

### 7. Update Main Model Registry

Add EdgeTAM import to the main model registry:

```bash
# Check if edgetam import exists in __init__.py
if ! grep -q "from . import edgetam" model_profiling/models/__init__.py; then
    # Add import using Python to handle edge cases
    python3 << 'PYEOF'
from pathlib import Path
init_file = Path("model_profiling/models/__init__.py")
content = init_file.read_text()
if "from . import edgetam" not in content:
    # Find the last import line and add after it
    lines = content.split('\n')
    new_lines = []
    added = False
    for i, line in enumerate(lines):
        new_lines.append(line)
        if line.startswith("from . import ") and not added:
            # Check if next line is not an import
            if i + 1 < len(lines) and not lines[i + 1].strip().startswith("from . import"):
                new_lines.append("from . import edgetam  # noqa: E402,F401")
                added = True
    if not added:
        # Add at the end before the last line
        new_lines.insert(-1, "from . import edgetam  # noqa: E402,F401")
    init_file.write_text('\n'.join(new_lines))
    print("✓ Added edgetam import to model registry")
else:
    print("✓ EdgeTAM import already exists")
PYEOF
fi
```

### 8. Verify Model Registration

```bash
# Test that model is registered
python3 << 'PYEOF'
import sys
sys.path.insert(0, "model_profiling")
from models import patch_executorch_model_registry, available_models

# Patch registry
patch_executorch_model_registry()

# Check if edgetam_image_encoder is available
models = list(available_models())
if "edgetam_image_encoder" in models:
    print(f"✓ EdgeTAM model registered: {models}")
else:
    print(f"✗ EdgeTAM model not found. Available: {models}")
    sys.exit(1)
PYEOF
```

### 9. Test Model Loading (Optional)

```bash
# Test that model can be instantiated and loaded
python3 << 'PYEOF'
import sys
sys.path.insert(0, "model_profiling")
from models import patch_executorch_model_registry
from models.edgetam import EdgeTAMImageEncoderModel

patch_executorch_model_registry()

try:
    model_wrapper = EdgeTAMImageEncoderModel()
    print("✓ Model wrapper instantiated")
    
    # Test example inputs
    example_inputs = model_wrapper.get_example_inputs()
    print(f"✓ Example inputs: {[x.shape for x in example_inputs]}")
    
    # Test model loading (this will load checkpoint)
    print("Loading model (this may take a moment)...")
    model = model_wrapper.get_eager_model()
    print(f"✓ Model loaded: {type(model).__name__}")
    
    # Test forward pass
    import torch
    with torch.no_grad():
        output = model(*example_inputs)
    print(f"✓ Forward pass successful: output shape = {output.shape if hasattr(output, 'shape') else type(output)}")
    
except Exception as e:
    print(f"✗ Model loading failed: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
PYEOF
```

**Verification**:

```bash
# Check directory structure
test -d model_profiling/models/edgetam && echo "✓ EdgeTAM directory exists"
test -f model_profiling/models/edgetam/model.py && echo "✓ model.py exists"
test -f model_profiling/models/edgetam/__init__.py && echo "✓ __init__.py exists"
test -d model_profiling/models/edgetam/edgetam_core && echo "✓ EdgeTAM repository cloned"
test -f model_profiling/models/edgetam/edgetam_core/setup.py && echo "✓ Repository verified"

# Check model registration
python3 -c "
import sys
sys.path.insert(0, 'model_profiling')
from models import patch_executorch_model_registry, available_models
patch_executorch_model_registry()
assert 'edgetam_image_encoder' in available_models(), 'Model not registered'
print('✓ Model registered successfully')
"
```

**Expected outputs**:
- `model_profiling/models/edgetam/model.py` - Model wrapper implementation
- `model_profiling/models/edgetam/__init__.py` - Model registration
- `model_profiling/models/edgetam/edgetam_core/` - Cloned EdgeTAM repository
- Model registered in `model_profiling/models/__init__.py`

## Next Steps

After onboarding, you can:

1. **Export the model** (using `03_export_model.md`):
   ```bash
   python model_profiling/export/export_model.py \
     --model edgetam_image_encoder \
     --dtype fp32 \
     --backend xnnpack \
     --outdir model_profiling/out_edgetam_image_encoder/artifacts/
   ```

2. **Run profiling** (using `04_run_profiling.md`):
   ```bash
   python3 model_profiling/scripts/mac_pipeline.py \
     --config model_profiling/configs/edgetam_image_encoder_run.json
   ```

## Failure Handling

| Issue | Symptom | Fix |
|-------|---------|-----|
| **Git clone fails** | `git clone` errors | Check network connectivity, verify repository URL, ensure git is installed |
| **Repository already exists** | `fatal: destination path already exists` | Remove existing directory or skip clone step if repository is already present |
| **Checkpoint download fails** | `curl`/`wget` errors | Manually download from https://github.com/facebookresearch/EdgeTAM/tree/main/checkpoints and place in `model_profiling/models/edgetam/edgetam_core/checkpoints/` |
| **Missing dependencies** | `ImportError: No module named 'hydra'` | Install: `pip install hydra-core>=1.3.2 omegaconf` |
| **Config not found** | `FileNotFoundError: edgetam.yaml` | Ensure EdgeTAM repository was cloned correctly, check that `sam2/configs/edgetam.yaml` exists |
| **Model loading fails** | `RuntimeError: Failed to load EdgeTAM` | Check checkpoint file is valid, config YAML is correct, and all dependencies are installed |
| **Model not registered** | `edgetam_image_encoder` not in available models | Verify `__init__.py` files are correct and model registry was patched |

## Implementation Checklist

- [ ] Virtual environment activated
- [ ] Model directory created (`model_profiling/models/edgetam/`)
- [ ] EdgeTAM repository cloned (`edgetam_core/`)
- [ ] Checkpoint downloaded (optional, if not in repo)
- [ ] Model wrapper generated (`model.py`)
- [ ] Model registration generated (`__init__.py`)
- [ ] Main registry updated (import added)
- [ ] Model registration verified
- [ ] Model loading tested (optional but recommended)

## Notes

- **Repository location**: EdgeTAM is cloned to `model_profiling/models/edgetam/edgetam_core/` (not in the learning path repo itself)
- **Checkpoint size**: ~200MB, download may take time depending on connection
- **Model architecture**: Uses RepViT backbone, image size 1024x1024
- **Dependencies**: Requires `hydra-core` and `omegaconf` for config loading
- **Model extraction**: Wrapper extracts just the image encoder from full EdgeTAM model

## References

- EdgeTAM repository: https://github.com/facebookresearch/EdgeTAM
- Checkpoint download: https://github.com/facebookresearch/EdgeTAM/tree/main/checkpoints
- Next skill: `03_export_model.md` (export EdgeTAM to .pte format)

**Assets**:
- Generated files: `model_profiling/models/edgetam/model.py`, `__init__.py`
- Cloned repository: `model_profiling/models/edgetam/edgetam_core/`
- Checkpoint: `model_profiling/models/edgetam/edgetam_core/checkpoints/edgetam.pt`
