---
title: Export Swin2SR for Arm VGF
description: Convert the pretrained Swin2SR ×2 model into a floating-point ExecuTorch program with Arm VGF.
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Export the pretrained model

You don't need to train Swin2SR. The exporter downloads the pretrained ×2 checkpoint and converts it into an ExecuTorch `.pte` program. The pinned checkpoint revision keeps the model weights consistent between runs.

Run the exporter from your ExecuTorch directory:

```bash
python examples/arm/super_resolution_example_vgf/model_export/export_super_resolution.py \
  --model-name swin2sr \
  --checkpoint caidas/swin2SR-classical-sr-x2-64 \
  --checkpoint-revision cee1c923c6a37361c6e5650b65dcf4be821e5d52 \
  --input-height 64 \
  --input-width 64 \
  --quantization-mode none \
  --output-path swin2sr-work/swin2sr.pte
```

The first run downloads the model weights. `--quantization-mode none` keeps floating-point calculations, so you don't need calibration images.

The `64` dimensions fix the input size for this export. The model produces a 128 × 128 image because the checkpoint upscales by two.

## Keep the program and metadata together

After export finishes, check the two files the runner needs:

```bash
ls -lh swin2sr-work/swin2sr.pte swin2sr-work/swin2sr.json
```

`swin2sr.pte` contains the executable model, including its VGF graphs. `swin2sr.json` tells the image helper how to read the input and reconstruct the output. Keep both files in the same directory with the same base name.

The exporter also saves `swin2sr_delegation.txt`. It records which operations run through VGF and which remain in ExecuTorch. You don't need to change this report to run the example.

## What you've accomplished and what's next

You have a floating-point Swin2SR program configured for one 64 × 64 RGB image. Next, build the host runner and use it to upscale your image.
