---
title: Train and benchmark AI workloads with DeepSpeed on Google Cloud C4A Axion VMs

description: Set up PyTorch and DeepSpeed on Google Cloud C4A Axion Arm VMs running SUSE Linux to train neural network models, benchmark AI workloads, and validate scalable CPU-based AI execution on Arm64 processors.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for DevOps engineers, ML engineers, and software developers who want to run AI training and benchmarking workloads using PyTorch and DeepSpeed on SUSE Linux Enterprise Server (SLES) Arm64, validate CPU-based neural network execution, and benchmark AI performance on Arm processors.

learning_objectives:
    - Install and configure PyTorch and DeepSpeed on Arm-based Google Cloud C4A Axion virtual machines (VMs). 
    - Create and execute neural network training workloads using PyTorch.
    - Benchmark CPU-based AI workloads on Arm64 processors.
    - Validate scalable AI execution and workload performance on Google Axion Arm VMs.

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with Python and machine learning concepts

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-27T18:49:11Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ee3e7ea8337b8506e30d93aaf2dbe144e5838a6740c8eff8447617f8c75629c7
  summary_generated_at: '2026-07-27T18:49:11Z'
  summary_source_hash: ee3e7ea8337b8506e30d93aaf2dbe144e5838a6740c8eff8447617f8c75629c7
  faq_generated_at: '2026-07-27T18:49:11Z'
  faq_source_hash: ee3e7ea8337b8506e30d93aaf2dbe144e5838a6740c8eff8447617f8c75629c7
  summary: >-
    You'll provision a Google Cloud C4A Arm VM running SUSE Linux, set up Python
    3.11, and install PyTorch and DeepSpeed for CPU training and benchmarking. You'll verify the
    `aarch64` architecture and Neoverse-V2 cores with `uname` and `lscpu`, create a dedicated virtual
    environment, and run a baseline model followed by a larger benchmark. From the training logs and benchmark output, you'll confirm correct
    execution.
  faqs:
  - question: How do I know the VM is Arm64 and running on Axion cores?
    answer: >-
      Run `uname -m` and confirm that the output is `aarch64`. Then run `lscpu` and check that the
      model name reports `Neoverse-V2`.
  - question: Which Google Cloud VM configuration should I use for the steps?
    answer: >-
      Use the `c4a-standard-4` machine type with 4 vCPUs and 16 GB of memory. This configuration
      hosts the PyTorch and DeepSpeed workloads.
  - question: Which Python version do I need and what is the virtual environment called?
    answer: >-
      Install Python 3.11 and create a virtual environment for the project. The path uses an environment
      named `deepspeed-env`.
  - question: I opened a new SSH session. What should I do before running workloads?
    answer: >-
      Re-activate the `deepspeed-env` virtual environment and navigate to the `~/deepspeed-demo`
      directory. This ensures the correct dependencies and paths are active.
  - question: What result should I expect from the baseline and benchmark runs?
    answer: >-
      The baseline model should run without errors and print training logs, confirming that PyTorch
      and DeepSpeed are correctly installed. The larger benchmark runs longer and lets you observe
      CPU scaling behavior by reviewing its logs and runtime characteristics.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: ML
cloud_service_providers:
  - Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - DeepSpeed
  - PyTorch
  - Python

operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================

further_reading:
  - resource:
      title: DeepSpeed official documentation
      link: https://www.deepspeed.ai/
      type: documentation

  - resource:
      title: DeepSpeed GitHub repository
      link: https://github.com/microsoft/DeepSpeed
      type: documentation

  - resource:
      title: PyTorch documentation
      link: https://pytorch.org/docs/stable/index.html
      type: documentation

  - resource:
      title: Introducing Google Axion Processors
      link: https://cloud.google.com/blog/products/compute/introducing-googles-new-arm-based-cpu
      type: blog

  - resource:
      title: Arm Neoverse V2 platform
      link: https://www.arm.com/products/silicon-ip-cpu/neoverse/neoverse-v2
      type: website

weight: 1
layout: "learningpathall"
learning_path_main_page: yes
---
