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


generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:50:53Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: dcdbc4cecc376ed4c0df9377d13cb4fe792ad7c68acfe0610d75cf41898804ff
  summary_generated_at: '2026-06-01T21:59:12Z'
  summary_source_hash: dcdbc4cecc376ed4c0df9377d13cb4fe792ad7c68acfe0610d75cf41898804ff
  faq_generated_at: '2026-06-02T22:50:53Z'
  faq_source_hash: dcdbc4cecc376ed4c0df9377d13cb4fe792ad7c68acfe0610d75cf41898804ff
  summary: >-
    This introductory Learning Path shows how to evaluate TinyML workloads on Arm virtual hardware
    before physical boards are available. You will set up an ExecuTorch development environment
    on Linux or macOS, install and configure the Corstone-320 Fixed Virtual Platform (FVP), and
    deploy a MobileNet V2 model to exercise the Ethos-U NPU in a virtual system. The steps explain
    how ExecuTorch uses ahead-of-time compilation and hybrid CPU/NPU execution, then guide you
    to run the example and visualize execution with the FVP graphical interface. Prerequisites
    are basic machine learning familiarity and a Linux or macOS host with Python 3. The path is
    designed to be completed in about 120 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need familiarity with basic machine learning concepts and a Linux or macOS computer
      with Python 3 installed. The path is introductory and assumes no prior TinyML experience.
  - question: I’m using macOS—are there extra steps to run the FVP?
    answer: >-
      Yes. The path notes additional setup is required on macOS for FVP execution and points to
      the FVPs-on-Mac GitHub repository for the necessary steps.
  - question: Where is the example model and how do I run it?
    answer: >-
      The MobileNet V2 Python code is located in executorch/examples/models/mobilenet_v2/model.py
      within your local ExecuTorch repository. You deploy it using the run.sh script with extra
      parameters as shown in the steps.
  - question: How do I know the FVP and ExecuTorch setup worked?
    answer: >-
      After setup, you should be able to start the Corstone-320 FVP and run an ExecuTorch-compiled
      model. You can then visualize model execution in the FVP graphical interface.
  - question: Do I need physical hardware to test Ethos-U NPU performance?
    answer: >-
      No. The Corstone-320 FVP simulates an Arm-based embedded system so you can deploy and test
      TinyML models, including visualization, without any hardware.
# END generated_summary_faq

author: Waheed Brown

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

