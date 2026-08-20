---
title: Convert SmolVLA to ONNX for Arm CPUs
description: Export SmolVLA from PyTorch to ONNX, create a packed INT4 weight-only model with TorchAO quantization, and run both models with ONNX Runtime on an Arm CPU.
minutes_to_complete: 180
who_is_this_for: Machine learning developers who want to deploy a vision-language-action policy with ONNX Runtime on an Arm CPU.
learning_objectives:
  - Export SmolVLA from PyTorch as an ONNX model.
  - Run and validate the FP32 ONNX model with ONNX Runtime on an Arm CPU.
  - Quantize eligible linear weights to INT4 and store them in a packed ONNX model.
  - Run the FP32 and INT4 models with identical inputs and compare their action outputs and ONNX Runtime latency.
prerequisites:
  - An aarch64 Linux system, such as the Radxa Orion O6.
  - Enough free storage for the model data, checkpoint weights, Python environment, and generated ONNX files.
  - Git and Python 3.12.
  - Familiarity with Python, PyTorch, and Linux command-line tools.
author: ""
generate_summary_faq: true
rerun_summary: false
rerun_faqs: false
skilllevels: Advanced
subjects: ML
armips:
  - Cortex-A
operatingsystems:
  - Linux
tools_software_languages:
  - Python
  - PyTorch
  - TorchAO
  - ONNX
  - ONNX Runtime
  - LeRobot
further_reading:
  - resource:
      title: PyTorch ONNX exporter documentation
      link: https://docs.pytorch.org/docs/stable/onnx.html
      type: documentation
  - resource:
      title: TorchAO documentation
      link: https://docs.pytorch.org/ao/stable/
      type: documentation
  - resource:
      title: ONNX Runtime 4-bit quantization
      link: https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html#quantize-to-int4uint4
      type: documentation
  - resource:
      title: ONNX Runtime Execution Providers
      link: https://onnxruntime.ai/docs/execution-providers/
      type: documentation
  - resource:
      title: KleidiAI optimized micro-kernels for Arm CPUs
      link: https://github.com/ARM-software/kleidiai
      type: GitHub Repository

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
