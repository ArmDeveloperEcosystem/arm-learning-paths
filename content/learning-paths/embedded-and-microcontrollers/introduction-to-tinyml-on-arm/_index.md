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


generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:23:20Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: aa49e4a1651367965e79d36c5f6af16e9b341c392d48cf051f24cbb21070e972
  summary_generated_at: '2026-06-01T21:40:55Z'
  summary_source_hash: aa49e4a1651367965e79d36c5f6af16e9b341c392d48cf051f24cbb21070e972
  faq_generated_at: '2026-06-02T22:23:20Z'
  faq_source_hash: aa49e4a1651367965e79d36c5f6af16e9b341c392d48cf051f24cbb21070e972
  summary: >-
    This introductory path explains what differentiates TinyML from other AI domains and why Arm-based
    edge devices are a good fit. You set up a Linux-hosted TinyML environment using PyTorch, ExecuTorch,
    and the Corstone-320 Fixed Virtual Platform (FVP), a pre-silicon virtual platform that models
    Cortex-M processors and Arm Ethos-U NPUs. The steps include installing and configuring ExecuTorch,
    running scripts to provision the Corstone-320 FVP, and defining a small PyTorch feedforward
    network that you export with ExecuTorch tooling to validate the setup. By the end, you can
    describe TinyML trade-offs, identify suitable Arm devices, and work with a basic TinyML sandbox
    on Linux. Prerequisites: basic ML knowledge and a Linux computer.
  faqs:
  - question: What do I need before running the setup?
    answer: >-
      You need basic knowledge of Machine Learning concepts and a Linux computer. No other explicit
      prerequisites are listed.
  - question: Do I need physical Arm hardware to complete this path?
    answer: >-
      No. The Corstone-320 Fixed Virtual Platform provides a virtual representation of Arm-based
      microcontrollers so you can develop and test before boards are available.
  - question: What does the Corstone-320 FVP provide for this workflow?
    answer: >-
      It is a pre-silicon software development environment designed for AI and ML workloads, with
      support for Arm Ethos-U NPUs and Cortex-M processors. It enables early software validation
      and development for embedded AI applications.
  - question: How do I validate that ExecuTorch and the environment are installed correctly?
    answer: >-
      Follow the steps to run the setup scripts for the Corstone-320 reference package and then
      execute the provided example. Being able to run the example without errors indicates the
      environment is ready.
  - question: What code artifact will I create in the modeling step?
    answer: >-
      You will create a Python file (simple_nn.py) that defines a small feedforward neural network
      for a classification task. The example uses PyTorch export utilities and ExecuTorch conversion
      APIs to target edge execution.
# END generated_summary_faq

author: Dominica Abena O. Amanfo

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

