---
title: Analyze ML models with Arm ML Inference Advisor

description: Learn how to use Arm ML Inference Advisor from the command line to check model compatibility, estimate performance, and identify target-aware model improvement opportunities using Ethos-U as the example target.

minutes_to_complete: 45

who_is_this_for: This Learning Path is for ML developers who want to use the Arm ML Inference Advisor (MLIA) to evaluate whether a model is suitable for a target before moving into deployment, graph inspection, or runtime profiling.

learning_objectives:
  - Use the MLIA CLI to discover target profiles and backends.
  - Run compatibility and performance analysis on LiteRT, Tensor Operator Set Architecture (TOSA), and ExecuTorch artifacts.
  - Interpret MLIA JSON output, advice, Vela estimates, and Corstone whole-model NPU performance counters.
  - (Optional) Call the MLIA Python API from automation or other tools.

prerequisites:
  - Ubuntu 22.04 LTS or another compatible Linux environment
  - Python 3.10 or later
  - Git and Git Large File Storage (LFS) to download the model artifacts
  - Basic familiarity with machine learning model deployment concepts
  - Basic familiarity with command-line tools

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-25T16:09:23Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: fd6174ed455ac37b777456bd6894b86f078555fbaeeb49fda696618ecb9c6489
  summary_generated_at: '2026-09-25T16:09:23Z'
  summary_source_hash: fd6174ed455ac37b777456bd6894b86f078555fbaeeb49fda696618ecb9c6489
  faq_generated_at: '2026-09-25T16:09:23Z'
  faq_source_hash: fd6174ed455ac37b777456bd6894b86f078555fbaeeb49fda696618ecb9c6489
  summary: >-
    You'll use MLIA to assess model suitability for Ethos-U targets before
    deployment. First, you'll install MLIA, discover target profiles and backends, and compare LiteRT and TOSA
    artifacts with Vela. Then, you'll analyze packaged ExecuTorch `.pte` artifacts with Corstone. You'll
    learn that Vela provides compiler estimates and operator breakdowns, while Corstone reports
    whole-model NPU counters. Optionally, you'll automate compatibility checks with the Python API.
  faqs:
  - question: How do I confirm that Git LFS is set up before downloading the model artifacts?
    answer: >-
      Run `git lfs version`. If the command fails on Ubuntu, run `sudo apt update`, then install
      Git LFS and the Python development package with `sudo apt install -y git-lfs python3.10-dev`.
      Run `git lfs install` before you clone the repository and pull the model artifacts.
  - question: How do I verify that MLIA is installed and discover available backends and target profiles?
    answer: >-
      Activate your virtual environment with `source mlia_env/bin/activate`, then run `mlia --help`
      to confirm that the CLI works. To list target profiles, run `mlia target list`. To see available
      and installed backends, run `mlia backend list`.
  - question: Why is the FP32 LiteRT model incompatible while the INT8 model is compatible?
    answer: >-
      Ethos-U acceleration needs supported quantized integer workloads. The FP32 model lacks the
      needed quantization parameters, so MLIA reports `accelerator_operator_percentage` as `0`.
      For the supplied INT8 model, Vela reports `status` as `ok` and
      `accelerator_operator_percentage` as `100.0` for the `ethos-u85-256` profile.
  - question: What does Vela performance analysis tell me about LiteRT and TOSA artifacts?
    answer: >-
      You get target-aware compiler estimates, including cycles, utilization, memory use, and
      operator-level breakdowns when available. Treat these values as estimates for NPU work, not
      final latency measurements from hardware. Use the advice to identify operators that dominate
      estimated cycles or have low MAC utilization.
  - question: When should I use Corstone analysis or the MLIA Python API?
    answer: >-
      Use Corstone to run a packaged ExecuTorch `.pte` artifact on an Fixed Virtual Platform (FVP) and collect whole-model NPU
      performance counters. It doesn't provide per-layer estimates or operator breakdowns. Use
      `run_advisor()` from the Python API when you want to integrate MLIA compatibility checks into
      a product, dashboard, workflow runner, or CI system.
# END generated_summary_faq

author:
  - Matt Cossins

generate_summary_faq: false
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
