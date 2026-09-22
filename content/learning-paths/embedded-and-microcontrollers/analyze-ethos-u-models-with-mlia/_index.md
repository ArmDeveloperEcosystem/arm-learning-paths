---
title: Analyze ML models with Arm ML Inference Advisor (MLIA)

description: Learn how to use Arm ML Inference Advisor from the command line to check model compatibility, estimate performance, and identify target-aware model improvement opportunities using Ethos-U as the example target.

minutes_to_complete: 45

who_is_this_for: This Learning Path is for ML developers who want to use Arm's ML Inference Advisor (MLIA) to evaluate whether a model is suitable for a target before moving into deployment, graph inspection, or runtime profiling.

learning_objectives:
  - Use the MLIA CLI to discover target profiles and backends
  - Run compatibility and performance analysis on LiteRT, TOSA, and ExecuTorch artifacts
  - Interpret MLIA JSON output, advice, Vela estimates, and Corstone whole-model NPU performance counters
  - (Optional) Call the MLIA Python API from automation or other tools

prerequisites:
  - Ubuntu 22.04 LTS or another compatible Linux environment
  - Python 3.10 or later
  - Git and Git LFS to download the model artifacts
  - Basic familiarity with machine learning model deployment concepts
  - Basic familiarity with command-line tools

author:
  - Matt Cossins

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
  - Cortex-M
  - Ethos-U

operatingsystems:
  - Linux

tools_software_languages:
  - MLIA
  - Vela
  - ExecuTorch
  - Python
  - TOSA
  - LiteRT

further_reading:
  - resource:
      title: Arm MLIA
      link: https://github.com/arm/mlia
      type: repository
  - resource:
      title: MLIA Ethos-U Plugin
      link: https://github.com/arm/mlia-ethos-u
      type: repository
  - resource:
      title: Arm ML model artifacts
      link: https://github.com/arm-education/ml-model-artifacts
      type: repository
  - resource:
      title: Ethos-U Vela compiler
      link: https://gitlab.arm.com/artificial-intelligence/ethos-u/ethos-u-vela
      type: repository

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
