---
title: Quantize and export DeiT-Tiny to VGF
description: Calibrate DeiT-Tiny, measure quantized host accuracy, and export a VGF-backed ExecuTorch program.
weight: 5
layout: "learningpathall"
---

## Export the quantized model

Convert your fine-tuned checkpoint into a quantized ExecuTorch `.pte` program with VGF delegate data. Calibration uses 300 training images to determine quantization parameters. A separate host accuracy check evaluates breed predictions on 100 test images:

```bash
python examples/arm/image_classification_example_vgf/model_export/export_deit.py \
  --model-path arm_test/deit_vgf/deit-tiny-oxford-pet/final_model \
  --output-path arm_test/deit_vgf/deit_quantized_vgf.pte \
  --num-calibration-samples 300 \
  --num-test-samples 100 \
  2>&1 | tee arm_test/deit_vgf/export.log
```

The script does the following:

- Exports the floating-point graph
- Calibrates symmetric INT8 post-training quantization
- Evaluates the quantized model in PyTorch
- Delegates supported operations through the Arm VGF backend
- Writes the `.pte` file

## Check the export result

Find the accuracy result and the export confirmation in the log, then check that the program exists:

```bash
grep -E 'Top-1 accuracy|Exported model saved' arm_test/deit_vgf/export.log
test -s arm_test/deit_vgf/deit_quantized_vgf.pte
```

The output is similar to:

```output
Top-1 accuracy on 100 test samples: 0.8900
Exported model saved to arm_test/deit_vgf/deit_quantized_vgf.pte
```

The example accuracy of `0.8900` means the highest-scoring breed matches the dataset label for 89 of the 100 test images. Your result can differ. A successful export also reports the output path, and `test -s` exits successfully when that file is nonempty.

The reported accuracy measures the quantized PyTorch model before VGF execution. The training log evaluates a different number of test images, so those two values alone don't measure the accuracy change caused by quantization. Use the same evaluation images when investigating that change.

The `.pte` includes its VGF delegate data. You don't need to supply a separate `.vgf` file to the ExecuTorch runner.

## What you've accomplished and what's next

You've produced a quantized VGF-backed program and recorded its host accuracy.

Next, you'll classify a pet image with the runner that you built during setup.
