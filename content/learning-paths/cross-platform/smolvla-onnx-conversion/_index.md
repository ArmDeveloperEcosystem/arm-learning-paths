---
title: Export and Quantize SmolVLA for ONNX Runtime on Arm

draft: true
cascade:
    draft: true
  
description: Export SmolVLA from PyTorch to ONNX, quantize linear weights to INT4 with TorchAO, and compare action accuracy and ONNX Runtime latency on an Arm CPU.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for machine learning developers who want to export and quantize a vision-language-action model for ONNX Runtime on Arm.
learning_objectives:
  - Export SmolVLA from PyTorch as an ONNX model
  - Run and validate the FP32 ONNX model with ONNX Runtime on an Arm CPU
  - Quantize eligible linear weights to INT4 and store them in a packed ONNX model
  - Run the FP32 and INT4 models with identical inputs and compare their action outputs and ONNX Runtime latency

prerequisites:
  - An Arm Linux system, such as an Arm cloud instance or Radxa Orion O6
  - Familiarity with Python, PyTorch, and Linux command-line tools

author: Tirui Wu
generate_summary_faq: true
rerun_summary: false
rerun_faqs: false
skilllevels: Advanced
subjects: ML
armips:
  - Cortex-A
  - Neoverse
operatingsystems:
  - Linux
tools_software_languages:
  - Python
  - PyTorch
  - TorchAO
  - ONNX
  - ONNX Runtime
  - LeRobot
### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - embedded-and-microcontrollers

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
