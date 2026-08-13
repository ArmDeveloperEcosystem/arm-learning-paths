---
title: Visualize Ethos-U NPU performance with ExecuTorch on Arm FVPs

description: Learn how to identify Arm-based targets for TinyML, install Fixed Virtual Platforms, deploy ExecuTorch models on Corstone-320 FVP, and visualize model execution using the FVP graphical interface.

minutes_to_complete: 120

who_is_this_for: This is an introductory topic for developers and data scientists who are new to TinyML and want to visualize ExecuTorch model performance on virtual Arm hardware.

learning_objectives:
  - Identify Arm-based targets suitable for TinyML workloads
  - Install and configure Fixed Virtual Platforms (FVPs)
  - Deploy a TinyML model using ExecuTorch on a Corstone-320 FVP
  - Visualize model execution using the FVP graphical interface

prerequisites:
    - Familiarity with basic machine learning concepts
    - A Linux or macOS computer with Python 3 installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-13T18:59:18Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ef164a14279db720143e61bd5eac1273d0e03fd771db55926af8be257cc45fb6
  summary_generated_at: '2026-08-13T18:59:18Z'
  summary_source_hash: ef164a14279db720143e61bd5eac1273d0e03fd771db55926af8be257cc45fb6
  faq_generated_at: '2026-08-13T18:59:18Z'
  faq_source_hash: ef164a14279db720143e61bd5eac1273d0e03fd771db55926af8be257cc45fb6
  summary: >-
    You'll use ExecuTorch and the Corstone-320 FVP to explore TinyML execution with
    Ethos-U. First, you'll set up ExecuTorch, install the FVP, and export a model with the ahead-of-time
    workflow. Then, you'll run MobileNet V2 and use the FVP graphical interface to visualize CPU and
    NPU activity without physical hardware.
  faqs:
  - question: What additional setup do I need before running the FV on macOS?
    answer: >-
      Follow the guidance in the [FVPs-on-Mac GitHub repository](https://github.com/Arm-Examples/FVPs-on-Mac/) before launching the Corstone-320 FVP.
  - question: Where is the MobileNet V2 example located in the ExecuTorch repository?
    answer: >-
      The Python code for MobileNet V2 is in `executorch/examples/models/mobilenet_v2/model.py`.
      Use this example when deploying the model to the Corstone-320 FVP.
  - question: How do I run the MobileNet V2 example on the Corstone-320 FVP?
    answer: >-
      Use the provided `run.sh` script with the additional parameters shown in the steps after completing
      the environment and FVP setup. Run the script from the `executorch` repository.
  - question: How do I know the Corstone-320 FVP installed and started correctly?
    answer: >-
      The FVP should launch without errors and present its graphical interface.
  - question: How do I verify that execution uses the simulated Ethos-U NPU?
    answer: >-
      Use the FVP graphical interface to visualize model execution and look for activity corresponding
      to CPU and NPU components.
# END generated_summary_faq

author: Waheed Brown

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
    - macOS

tools_software_languages:
    - Arm Virtual Hardware
    - FVP
    - Python
    - PyTorch
    - ExecuTorch
    - Arm Compute Library
    - GCC
    - Docker

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
