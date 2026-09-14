---
title: Quantize and export DeiT-Tiny to VGF
description: Calibrate DeiT-Tiny, measure quantized host accuracy, and export a VGF-backed ExecuTorch program.
weight: 5
layout: "learningpathall"
---

## Export the quantized model

Use 300 training images for calibration and 100 test images for the host accuracy check:

```bash
python examples/arm/image_classification_example_vgf/model_export/export_deit.py \
  --model-path arm_test/deit_vgf/deit-tiny-oxford-pet/final_model \
  --output-path arm_test/deit_vgf/deit_quantized_vgf.pte \
  --num-calibration-samples 300 \
  --num-test-samples 100 \
  2>&1 | tee arm_test/deit_vgf/export.log
```

The script exports the floating-point graph, calibrates symmetric INT8 post-training quantization, and evaluates the quantized model in PyTorch. It then delegates supported operations through the Arm VGF backend and writes the `.pte` file.

## Check the export result

Find the accuracy result and the export confirmation in the log, then check that the program exists:

```bash
grep -E 'Top-1 accuracy|Exported model saved' arm_test/deit_vgf/export.log
test -s arm_test/deit_vgf/deit_quantized_vgf.pte
```

The script reports `Top-1 accuracy on 100 test samples:` followed by the result from your run. A successful export also reports the output path, and `test -s` exits successfully when that file is nonempty.

The reported accuracy measures the quantized PyTorch model before VGF execution. The training log evaluates a different number of test images, so those two values alone do not measure the accuracy change caused by quantization. Use the same evaluation images when investigating that change.

The `.pte` includes its VGF delegate data. You do not need to supply a separate `.vgf` file to the ExecuTorch runner.

## What you've accomplished

You have produced a quantized VGF-backed program and recorded its host accuracy. Next, you will classify a pet image with the runner you built during setup.
