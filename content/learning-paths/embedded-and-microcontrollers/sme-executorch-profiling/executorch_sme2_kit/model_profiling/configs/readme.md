# Profiling Configurations

This directory contains configuration files for profiling runs. Each config file references a `.pte` model that must be exported first.

## Config Files

### `efficient_sam_run.json`
Profiling configuration for EfficientSAM model.

**Export command** (run before profiling):
```bash
source .venv/bin/activate
python model_profiling/export/export_model.py \
  --model efficient_sam \
  --dtype fp32 \
  --backend xnnpack \
  --outdir model_profiling/out_efficient_sam/artifacts/
```

**Expected model path**: `model_profiling/out_efficient_sam/artifacts/efficient_sam_xnnpack_fp32.pte`

**Notes**:
- EfficientSAM is already registered in ExecuTorch's model registry
- Use `fp32` for better accuracy (model is larger, ~39MB)
- Model expects inputs: `(batched_images, batched_points, batched_point_labels)`

### `toy_cnn_run.json`
Profiling configuration for toy CNN model (smoke test).

**Export command**:
```bash
source .venv/bin/activate
python model_profiling/export/export_model.py \
  --model toy_cnn \
  --dtype fp16 \
  --outdir model_profiling/out_toy_cnn/artifacts/
```

**Expected model path**: `model_profiling/out_toy_cnn/artifacts/toy_cnn_xnnpack_fp16.pte`

### `edgetam_image_encoder_run.json` / `edgetam_image_encoder_android_run.json`
Profiling configuration for EdgeTAM image encoder model.

**Prerequisites**: EdgeTAM must be onboarded first (see agent skill `agent_skill_ml_profiling/08_onboard_edgetam.md`).

**Export command** (run before profiling):
```bash
source .venv/bin/activate
python model_profiling/export/export_model.py \
  --model edgetam_image_encoder \
  --dtype fp32 \
  --outdir model_profiling/out_edgetam_image_encoder/artifacts/
```

**Expected model path**: `model_profiling/out_edgetam_image_encoder/artifacts/edgetam_image_encoder_xnnpack_fp32.pte`

**Notes**:
- EdgeTAM image encoder is a video-focused segmentation model
- Requires onboarding via agent skill 08 before export
- Use `fp32` for better accuracy

## Creating New Configs

1. Copy from template:
   ```bash
   cp model_profiling/configs/templates/mac_template.json \
      model_profiling/configs/my_model_run.json
   ```

2. Update the config:
   - Set `"model"` to the path of your exported `.pte` file
   - Set `"output_root"` to where you want profiling results
   - Adjust experiments (SME2-on/off, threads, runs) as needed

3. Document the export command in this README

## Templates

- `templates/mac_template.json` - macOS profiling template
- `templates/android_template.json` - Android profiling template
