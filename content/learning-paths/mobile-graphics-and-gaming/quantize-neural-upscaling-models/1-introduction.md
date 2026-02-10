---
title: Understanding PTQ and QAT
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## PTQ vs QAT: what changes in practice?

PTQ and QAT both aim to run your model with quantized operators (typically INT8). The difference is where you pay the cost: PTQ optimizes for speed of iteration, while QAT optimizes for quality and robustness.

In this Learning Path, you use quantization as part of the ExecuTorch Arm backend. The goal is to export a quantized model that can run on Arm hardware with dedicated neural accelerators (NX).

To keep the workflow concrete, you start with a complete, runnable CIFAR-10-based example that exports `.vgf` artifacts end to end. After you have a known-good baseline, you can apply the same steps to your own upscaler model and training loop.

In a nutshell, the Arm backend in ExecuTorch consists of the following building blocks:

- TOSA (Tensor Operator Set Architecture) provides a standardized operator set for acceleration on Arm platforms.
- The ExecuTorch Arm backend lowers your PyTorch model to TOSA and uses an ahead-of-time (AOT) compilation flow.
- The VGF backend produces a portable artifact you can carry into downstream tools, including `.vgf` files.

### Post-training quantization (PTQ)

PTQ keeps training simple. You train your FP32 model as usual, then run a calibration pass using representative inputs to determine quantization parameters (for example, scales). After calibration, you convert the model and export a quantized graph.

PTQ is a good default when you need a fast iteration loop and you have a calibration set that looks like the actual inference data. For upscalers, PTQ can be good enough for early bring-up, especially when your goal is to validate the export and integration path.

### Quantization-aware training (QAT)

QAT simulates quantization effects during training. You prepare the model for QAT, fine-tune with fake-quantization enabled, then convert and export.

QAT is worth the extra effort when PTQ introduces visible artifacts. This is common for image-to-image tasks because small numeric changes can show up as banding, ringing, or loss of fine detail.

## How this maps to the Arm backend

For Arm-based platforms, the workflow stays consistent across models:

1. Train and evaluate the upscaler in PyTorch.
2. Quantize (PTQ or QAT) to reduce runtime cost.
3. Export through TOSA and generate a `.vgf` artifact.
4. Run the `.vgf` model in your Vulkan-based pipeline.

In later sections, you will generate the `.vgf` file by using the ExecuTorch Arm backend VGF partitioner.

With this background, you will now set up a working Python environment and run a baseline export-ready model.
