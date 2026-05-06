---
title: Quantize neural upscaling models with ExecuTorch
description: Learn how to apply post-training quantization to PyTorch models using TorchAO and export INT8 models to .vgf format with the ExecuTorch Arm backend.
    
minutes_to_complete: 60

who_is_this_for: This is an advanced topic for ML developers who want to reduce latency and memory bandwidth by exporting INT8 models to the `.vgf` file format using the ExecuTorch Arm backend.

learning_objectives:
    - Explain when to use post-training quantization (PTQ) vs quantization-aware training (QAT)
    - Prepare and quantize a PyTorch model using TorchAO PT2E quantization APIs
    - Export the quantized model to TOSA and generate a model artifact with the ExecuTorch Arm backend
    - Validate the exported graph by visualizing it using Google's Model Explorer

prerequisites:
    - Basic PyTorch model training and evaluation experience
    - A development machine with Python 3.10+ and PyTorch installed that runs ExecuTorch

generate_summary_faq: true

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:56Z'
  generator: template
  source_hash: 56d9d0fe9606e42281a2d2be52992c7a4b6846b208376c92e7fe3094647d1c70
  summary: >-
    Learn how to apply post-training quantization to PyTorch models using TorchAO and export INT8
    models to .vgf format with the ExecuTorch Arm backend. It is designed for ML developers who
    want to reduce latency and memory bandwidth by exporting INT8 models to the `.vgf` file format
    using the ExecuTorch Arm backend. By the end, you will be able to explain when to use post-training
    quantization (PTQ) vs quantization-aware training (QAT), prepare and quantize a PyTorch model
    using TorchAO PT2E quantization APIs, and export the quantized model to TOSA and generate
    a model artifact with the ExecuTorch Arm backend. It focuses on tools and technologies such
    as ExecuTorch, TorchAO, Vulkan, TOSA, and NX, Linux, macOS, and Windows environments, and
    Arm platforms including Mali. The main steps cover Explore PTQ and QAT for ExecuTorch INT8
    deployment, Set up your environment for ExecuTorch quantization, Apply PTQ and export a quantized
    VGF model, Apply QAT and export a quantized VGF model, and Inspect the graph with Model Explorer.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will explain when to use post-training quantization (PTQ) vs quantization-aware training
      (QAT), prepare and quantize a PyTorch model using TorchAO PT2E quantization APIs, and export
      the quantized model to TOSA and generate a model artifact with the ExecuTorch Arm backend.
      Learn how to apply post-training quantization to PyTorch models using TorchAO and export
      INT8 models to .vgf format with the ExecuTorch Arm backend.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for ML developers who want to reduce latency and memory bandwidth
      by exporting INT8 models to the `.vgf` file format using the ExecuTorch Arm backend.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Basic PyTorch model training and evaluation
      experience; A development machine with Python 3.10+ and PyTorch installed that runs ExecuTorch.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including ExecuTorch, TorchAO, Vulkan, TOSA, and NX, Linux,
      macOS, and Windows environments, and Arm platforms such as Mali.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Explore PTQ and QAT for ExecuTorch INT8 deployment,
      Set up your environment for ExecuTorch quantization, Apply PTQ and export a quantized VGF
      model, Apply QAT and export a quantized VGF model, and Inspect the graph with Model Explorer.
# END generated_summary_faq

author:
- Richard Burton
- Annie Tallund

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Mali
tools_software_languages:
    - ExecuTorch
    - TorchAO
    - Vulkan
    - TOSA
    - NX
operatingsystems:
    - Linux
    - macOS
    - Windows

further_reading:
    - resource:
        title: Get started with neural graphics using ML Extensions for Vulkan
        link: /learning-paths/mobile-graphics-and-gaming/vulkan-ml-sample/
        type: learningpath
    - resource:
        title: Fine-tuning neural graphics models with Model Gym
        link: /learning-paths/mobile-graphics-and-gaming/model-training-gym/
        type: learningpath
    - resource:
        title: Neural Graphics Development Kit
        link: https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics
        type: website
    - resource:
        title: Arm neural technology in ExecuTorch 1.0
        link: https://developer.arm.com/community/arm-community-blogs/b/ai-blog/posts/arm-neural-technology-in-executorch-1-0
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

