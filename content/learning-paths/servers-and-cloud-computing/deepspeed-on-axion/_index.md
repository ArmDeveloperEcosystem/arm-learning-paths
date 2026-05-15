---
title: Train and Benchmark AI Workloads with DeepSpeed on Google Cloud C4A Axion VM

draft: true
cascade:
    draft: true
    
description: Set up PyTorch and DeepSpeed on Google Cloud C4A Axion Arm VMs running SUSE Linux to train neural network models, benchmark AI workloads, and validate scalable CPU-based AI execution on Arm64 processors.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for DevOps engineers, ML engineers, and software developers who want to run AI training and benchmarking workloads using PyTorch and DeepSpeed on SUSE Linux Enterprise Server (SLES) Arm64, validate CPU-based neural network execution, and benchmark AI performance on Arm processors.

learning_objectives:
    - Install and configure PyTorch and DeepSpeed on Google Cloud C4A Axion processors for Arm64
    - Create and execute neural network training workloads using PyTorch
    - Benchmark CPU-based AI workloads on Arm64 processors
    - Validate scalable AI execution and workload performance on GCP Axion Arm VMs

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with Python and machine learning concepts

author: Pareena Verma

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

weight: 1
layout: "learningpathall"
learning_path_main_page: yes
---
