---
title: Introduction to TinyML on Arm using PyTorch and ExecuTorch

description: Learn what differentiates TinyML from other AI domains, explore Arm-based edge devices for TinyML, and set up a development environment using ExecuTorch and Corstone-320 Fixed Virtual Platform.

minutes_to_complete: 40

who_is_this_for: This is an introductory topic for developers and data scientists new to Tiny Machine Learning (TinyML) who want to explore its potential using PyTorch and ExecuTorch.

learning_objectives:
    - Describe what differentiates TinyML from other AI domains
    - Describe the benefits of deploying AI models on Arm-based edge devices
    - Identify suitable Arm-based devices for TinyML applications
    - Set up and configure a TinyML development environment using ExecuTorch and Corstone-320 Fixed Virtual Platform (FVP)

prerequisites:
    - Basic knowledge of Machine Learning concepts
    - A Linux computer

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-12T20:07:04Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: bf9cd7acd601825e582670b60c243799df8a93d3580834ca1126db15abd5540e
  summary_generated_at: '2026-08-12T20:07:04Z'
  summary_source_hash: bf9cd7acd601825e582670b60c243799df8a93d3580834ca1126db15abd5540e
  faq_generated_at: '2026-08-12T20:07:04Z'
  faq_source_hash: bf9cd7acd601825e582670b60c243799df8a93d3580834ca1126db15abd5540e
  summary: >-
    You'll learn TinyML on Arm with ExecuTorch and the Corstone-320 Fixed Virtual Platform. You'll
    install ExecuTorch, configure the FVP, and compare resource-constrained edge inference with
    cloud machine learning. You'll implement a small PyTorch network and export it through ExecuTorch,
    creating an edge-ready artifact for a virtual target supporting Cortex-M and Arm Ethos-U.
  faqs:
  - question: How do I know the Corstone-320 FVP setup worked?
    answer: >-
      The setup scripts should complete without errors and the reference package should be available
      for use. At that point, the FVP is ready for software development and validation without
      a physical board.
  - question: What does installing ExecuTorch enable in this workflow?
    answer: >-
      ExecuTorch lets you export PyTorch models and prepare them for execution on resource‑constrained
      Arm targets. It provides the APIs used to convert the example network into an edge‑ready
      form.
  - question: What file do I create for the example model, and what does it include?
    answer: >-
      You create `simple_nn.py`, which defines a small feedforward network with two linear layers
      and a ReLU activation for a classification task. The script also uses `torch.export` and ExecuTorch
      conversion to generate an edge representation.
  - question: Do I need a physical development board to complete the example?
    answer: >-
      No. The Corstone-320 Fixed Virtual Platform provides a pre-silicon environment to build
      and test software before hardware is available.
  - question: Which Arm components does the Corstone-320 FVP support in this path?
    answer: >-
      The FVP includes support for Arm Ethos-U NPUs and Cortex-M processors. It is designed for
      AI and machine learning workloads on microcontrollers.
# END generated_summary_faq

author: Dominica Abena O. Amanfo

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
    - Cortex-M
    - Ethos-U

operatingsystems:
    - Linux

tools_software_languages:
    - Arm Virtual Hardware
    - FVP
    - Python
    - PyTorch
    - ExecuTorch
    - Arm Compute Library
    - GCC

further_reading:
    - resource:
        title: TinyML Brings AI to Smallest Arm Devices
        link: https://newsroom.arm.com/blog/tinyml
        type: blog
    - resource:
        title: Arm Machine Learning Resources
        link: https://www.arm.com/developer-hub/embedded-and-microcontrollers/ml-solutions/getting-started
        type: documentation
    - resource:
        title: Arm Developers Guide for Cortex-M Processors and Ethos-U NPU
        link: https://developer.arm.com/documentation/109267/0101
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
