---
title: Convert SmolVLA to ExecuTorch for Arm CPU

draft: true
cascade:
    draft: true

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for machine learning developers who want to export a vision-language-action model to ExecuTorch for Arm CPU inference.

learning_objectives: 
    - Export SmolVLA from PyTorch to ExecuTorch, and lower the model to run on Arm CPU using the XNNPACK backend.
    - Run the FP32 ExecuTorch model on Arm CPU and validate its output against the PyTorch model.
    - Export a model to ExecuTorch with eligible linear weights quantized to INT8.
    - Compare outputs and latency between the FP32 and INT8 models running on the Arm CPU.

prerequisites:
    - An AArch64 Linux system with at least 20 GB of free storage.
    - Familiarity with Python, PyTorch, and the Linux command-line.

author: William Watson

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: true

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
