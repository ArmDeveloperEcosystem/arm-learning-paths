---
title: Convert SmolVLA to ExecuTorch for inference on Arm CPUs
description: Convert the SmolVLA vision-language-action model from PyTorch to ExecuTorch, run FP32 and INT8 variants on an Arm CPU, and compare their outputs and latency.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for machine learning developers who want to export a vision-language-action model to ExecuTorch for inference on an Arm CPU.

learning_objectives:
    - Export SmolVLA from PyTorch to ExecuTorch, and lower the model to run on Arm CPU using the XNNPACK backend.
    - Run the FP32 ExecuTorch model on Arm CPU and validate its output against the PyTorch model.
    - Export a model to ExecuTorch with eligible linear weights quantized to INT8.
    - Compare outputs and latency between the FP32 and INT8 models running on the Arm CPU.

prerequisites:
    - An AArch64 Ubuntu system with at least 20 GB of free storage. This Learning Path was tested on NVIDIA's DGX Spark
    - Familiarity with Python, PyTorch, and the Linux command-line

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-15T18:21:16Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 81462250cc3d5d0876affd8f4bf8b54f95da4f30b276d1ca0a5713fd99b1ed09
  summary_generated_at: '2026-09-15T18:21:16Z'
  summary_source_hash: 81462250cc3d5d0876affd8f4bf8b54f95da4f30b276d1ca0a5713fd99b1ed09
  faq_generated_at: '2026-09-15T18:21:16Z'
  faq_source_hash: 81462250cc3d5d0876affd8f4bf8b54f95da4f30b276d1ca0a5713fd99b1ed09
  summary: >-
    You'll convert the SmolVLA vision-language-action model from PyTorch to ExecuTorch, lower it to XNNPACK
    for Arm CPU inference, and validate the FP32 result against the original model. First, you'll generate
    deterministic inputs, export the FP32 components, and run them through a native orchestrator.
    Then, you'll quantize eligible operations to INT8 with TorchAO and reuse the same inputs to compare
    model outputs, latency, and `.pte` sizes.
  faqs:
  - question: How do I validate the exported FP32 model?
    answer: >-
      Run `python scripts/prepare_inputs.py` and `python scripts/validate_pte.py`. Confirm that the
      output reports `Accuracy gate passed` and points to the FP32 validation report.
  - question: Where are the FP32 artifacts saved, and how can I change the location?
    answer: >-
      The artifacts are saved under `artifacts/fp32` when you use the default configuration. To change the
      location, set `SMOLVLA_ARTIFACTS_DIR` to an absolute path and use the same location for the FP32
      benchmark.
  - question: How do I reuse the same inputs for both FP32 and INT8 comparisons?
    answer: >-
      Generate deterministic inputs with the provided script and note the saved input-suite path. Pass
      that path to the INT8 pipeline with `--input-suite`, or set the `SMOLVLA_INPUT_SUITE` environment
      variable to use it.
  - question: How do I confirm that the INT8 pipeline succeeded?
    answer: >-
      Run the pipeline script and confirm that it ends with `[8/8] Native accuracy gate passed`. The
      script stores the artifacts in `artifacts/int8`. Use `--output-dir` to choose another
      location.
  - question: How do I validate the native runner against the PyTorch model?
    answer: >-
      Run `./scripts/run_runner.sh`, then run `python scripts/validate_runner.py`. Confirm that the
      output says `Native split orchestrator output matches the full PyTorch reference.`
# END generated_summary_faq

author: William Watson

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: false

# Optional one-shot controls: set either field to true to regenerate just that
# generated section the next time the summary/FAQ tool runs. The tool resets
# them to false after a successful write.
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-X
    - Cortex-A
tools_software_languages:
    - Python
    - PyTorch
    - TorchAO
    - ExecuTorch
    - XNNPACK
    - LeRobot
    - SmolVLA
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: SmolVLA research paper
        link: https://arxiv.org/pdf/2506.01844
        type: website
    - resource:
        title: SmolVLA base model
        link: https://huggingface.co/lerobot/smolvla_base
        type: website
    - resource:
        title: Getting started with ExecuTorch
        link: https://docs.pytorch.org/executorch/stable/getting-started.html
        type: documentation
    - resource:
        title: XNNPACK documentation
        link: https://docs.pytorch.org/executorch/stable/backends/xnnpack/xnnpack-overview.html
        type: documentation
    - resource:
        title: KleidiAI optimized microkernels for Arm CPUs
        link: https://github.com/ARM-software/kleidiai
        type: documentation
    - resource:
        title: TorchAO documentation
        link: https://docs.pytorch.org/ao/stable/
        type: documentation
    - resource:
        title: Export and quantize SmolVLA for ONNX Runtime on Arm
        link: https://learn.arm.com/learning-paths/cross-platform/smolvla-onnx-conversion/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
