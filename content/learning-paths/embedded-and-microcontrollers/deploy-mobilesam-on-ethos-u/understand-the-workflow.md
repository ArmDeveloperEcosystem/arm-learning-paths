---
title: Understand the MobileSAM deployment workflow
description: Learn how the example quantizes MobileSAM, delegates it to Ethos-U85, and validates the segmentation mask on virtual hardware.
weight: 2

layout: "learningpathall"
---

## Understand the MobileSAM deployment workflow

MobileSAM is a compact variant of the Segment Anything Model. It takes an image and point prompts, then predicts a binary mask for the object selected by those points.

You will run the ExecuTorch MobileSAM example on a Corstone-320 Fixed Virtual Platform (FVP). The system combines a Cortex-M85 processor with an Ethos-U85 neural processing unit (NPU). This lets you test the complete bare-metal deployment without a physical board.

## Follow the model from PyTorch to the target

The example performs the following sequence:

1. Downloads the pinned MobileSAM `vit_t` source and checkpoint.
2. Embeds the positive point `(219, 193)` into the exported model.
3. Calibrates post-training quantization with the example dog image.
4. Uses 8-bit activations and weights for most of the graph, with 16-bit activations and 8-bit weights for TinyViT attention.
5. Lowers the quantized graph to an Ethos-U85-256 delegate and writes an ExecuTorch `.pte` program.
6. Builds a bare-metal runtime, runs it on the Corstone-320 FVP, and compares its mask with the host quantized mask.

The default image tensor has shape `[1, 3, 448, 448]`. The model produces one mask-logit tensor with shape `[1, 1, 112, 112]`.

## Understand the fixed-prompt contract

The exported `.pte` accepts an image tensor as its only runtime input. The point prompt is part of the exported graph, so changing the image doesn't require another export. Changing the point coordinates does require another export.

The example uses `multimask_output=False` and keeps mask thresholding outside the model. This arrangement focuses the target graph on the MobileSAM image encoder and mask decoder while keeping target-side post-processing small.

## Know what the validation proves

The workflow performs two comparisons:

- Host validation compares the floating-point mask with the quantized mask before lowering.
- Target validation compares the mask produced by the FVP with the host quantized mask.

Both comparisons enforce a minimum intersection over union (IoU) of `0.9`. Export stops if the host comparison falls below that threshold. The visualization step stops if the target comparison fails or produces a degenerate mask.

## What you've learned

You now know what the example deploys, why the point prompt is fixed, and how the host and target checks cover different stages of the pipeline. Next, you will prepare ExecuTorch and the Arm development tools.
