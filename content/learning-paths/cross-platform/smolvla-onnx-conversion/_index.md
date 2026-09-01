---
title: Export and quantize SmolVLA for ONNX Runtime on Arm

description: Export SmolVLA from PyTorch to ONNX, quantize linear weights to INT4 with TorchAO, and compare action accuracy and ONNX Runtime latency on an Arm CPU.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for machine learning developers who want to export and quantize a vision-language-action model for ONNX Runtime on Arm.

learning_objectives:
  - Export SmolVLA from PyTorch as an ONNX model
  - Run and validate the FP32 ONNX model with ONNX Runtime on an Arm CPU
  - Quantize eligible linear weights to INT4 and store them in a packed ONNX model
  - Run the FP32 and INT4 models with identical inputs and compare their action outputs and ONNX Runtime latency

prerequisites:
  - An Arm Linux system, such as an Arm cloud instance or Radxa Orion O6, with Python 3.12 installed and at least 50 GB of free storage
  - Familiarity with Python, PyTorch, and Linux command-line tools

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-26T22:01:23Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 928438780614fcd9081745b0f052058751923431630919351e91acf15e4a76ab
  summary_generated_at: '2026-08-26T22:01:23Z'
  summary_source_hash: 928438780614fcd9081745b0f052058751923431630919351e91acf15e4a76ab
  faq_generated_at: '2026-08-26T22:01:23Z'
  faq_source_hash: 928438780614fcd9081745b0f052058751923431630919351e91acf15e4a76ab
  summary: >-
    You'll export SmolVLA from PyTorch to FP32 ONNX and validate it with ONNX Runtime on an Arm Linux CPU.
    First, you'll set up the pinned model, source, and Python environment. Then, you'll export the
    model and compare its output with PyTorch. Finally, you'll quantize eligible linear weights to
    packed INT4 with TorchAO and compare FP32 and INT4 action outputs and latency using identical inputs.
  faqs:
  - question: What do I need to check on my Arm machine before I run the setup scripts?
    answer: >-
      Confirm you are on an Arm Linux CPU with Python 3.12 and at least 50 GB of free storage.
  - question: Where do the scripts place the exported and quantized models?
    answer: >-
      The FP32 export is saved at `work/onnx/fp32/model.onnx`. The TorchAO converter writes the
      packed INT4 model to `work/onnx/int4/smolvla-int4.onnx`.
  - question: What output confirms that the ONNX export matches PyTorch?
    answer: >-
      The exporter ends with `PASS: ONNX Runtime matches PyTorch within atol=0.001 and rtol=0.001`.
      You can also inspect `work/onnx/fp32/validation.json` to confirm the provider, output shape,
      and validation result.
  - question: What exactly gets quantized, and how can I verify it?
    answer: >-
      TorchAO applies weight-only INT4 quantization to eligible constant linear weights and replaces
      supported `MatMul` and `Gemm` operations with packed `com.microsoft::MatMulNBits` operations.
      The converter reports how many eligible linear operations it converted.
  - question: How should I compare FP32 and INT4 runs on Arm?
    answer: >-
      Run both models with the deterministic reference batch created during export. The comparison
      writes an action-output figure and JSON report with the latency and overall output error.
# END generated_summary_faq

author: Tirui Wu

generate_summary_faq: false
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
