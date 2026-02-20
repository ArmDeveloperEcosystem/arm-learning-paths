---
title: Explore PTQ and QAT for ExecuTorch INT8 deployment
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Quantization with ExecuTorch and the Arm backend

PTQ and QAT both aim to run your model with quantized operators (typically INT8). The difference is where you pay the cost: PTQ optimizes for speed of iteration, while QAT optimizes for quality and robustness.

In this Learning Path, you use quantization as part of the ExecuTorch Arm backend. The goal is to export a quantized model that can run on Arm hardware with dedicated neural accelerators (NX).

To keep the workflow concrete, you start with a complete, runnable CIFAR-10-based example that exports `.vgf` artifacts end to end. After you have a known-good baseline, you can apply the same steps to your own neural network and training code.

The Arm backend in ExecuTorch provides an open, standardized, minimal operator set for neural network operations to be lowered to, and is used by Arm platforms and accelerators. 

The ExecuTorch Arm backend uses three key components to optimize your model for Arm hardware:

- TOSA (Tensor Operator Set Architecture) provides a standardized operator set for acceleration on Arm platforms.
- ExecuTorch Arm backend lowers your PyTorch model to TOSA using ahead-of-time (AOT) compilation.
- VGF backend produces portable `.vgf` artifacts that work with downstream tools and Vulkan-based pipelines.

### Post-training quantization (PTQ)

PTQ keeps training simple. You train your FP32 model as usual, then run a calibration pass using representative inputs to determine quantization parameters (for example, scales). After calibration, you convert the model and export a quantized graph.

PTQ is a good default when you need a fast iteration loop and you have a calibration set that looks like the actual inference data. For neural networks, PTQ can be good enough for early bring-up, especially when your goal is to validate the export and integration path. Depending on the model and use case, PTQ can provide good quality results equal to the original floating-point graph.

### Quantization-aware training (QAT)

QAT simulates quantization effects during training. You prepare the model for QAT, fine-tune with fake-quantization enabled, then convert and export.

QAT introduces visible drop in model accuracy. For example, this is common for image-to-image tasks because small numeric changes can show up as banding, ringing, or loss of fine detail.

## ExecuTorch quantization workflow for Arm

For Arm-based platforms, the workflow stays consistent across models:

- Train and evaluate the neural network in PyTorch.
- Quantize (PTQ or QAT) to reduce runtime cost.
- Export with ExecuTorch (via TOSA) to generate a `.vgf` artifact.
- Run the `.vgf` model in your Vulkan-based pipeline.

In later sections, you generate the `.vgf` file using the ExecuTorch Arm backend VGF partitioner.

## What you've accomplished and what's next

In this section:
- You covered the difference between PTQ and QAT, and when to use each
- You saw how the ExecuTorch Arm backend uses TOSA as an intermediate representation
- You traced the end-to-end export workflow that produces `.vgf` artifacts

In the next section, you create a Python environment with all the tools needed to run the examples.
