---
title: Deploy SqueezeNet 1.0 INT8 model with ONNX Runtime on Azure Cobalt 100

   
minutes_to_complete: 60   

who_is_this_for: This Learning Path is for developers deploying ONNX-based applications on Arm-based machines.

learning_objectives:
    - Provision an Azure Arm64 virtual machine using Azure console, with Ubuntu Pro 24.04 LTS as the base image
    - Perform ONNX baseline testing and benchmarking on Arm64 virtual machines

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6)
    - Basic understanding of Python and machine learning concepts
    - Familiarity with [ONNX Runtime](https://onnxruntime.ai/docs/) and Azure cloud services

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:43:11Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 84ba887426f3ca45b698c79028023d80cbf0a06e6bc2fb71fcbe924943078dd8
  summary_generated_at: '2026-06-02T04:41:17Z'
  summary_source_hash: 84ba887426f3ca45b698c79028023d80cbf0a06e6bc2fb71fcbe924943078dd8
  faq_generated_at: '2026-06-03T01:43:11Z'
  faq_source_hash: 84ba887426f3ca45b698c79028023d80cbf0a06e6bc2fb71fcbe924943078dd8
  summary: >-
    Provision an Arm-based Azure Cobalt 100 (Dpsv6) virtual machine using the Azure portal and
    Ubuntu Pro 24.04 LTS, then set up a clean Python environment to run ONNX Runtime with a SqueezeNet
    1.0 INT8 model. You will validate your setup by performing a simple baseline latency test
    in Python and then run onnxruntime_perf_test for more systematic benchmarking on Arm64. This
    introductory path targets developers deploying ONNX-based applications on Arm-based machines
    and takes about 60 minutes. Prerequisites include an Azure account with access to Cobalt 100
    instances, basic Python and machine learning knowledge, and familiarity with ONNX Runtime
    and Azure services.
  faqs:
  - question: What do I need before provisioning the VM?
    answer: >-
      You need a Microsoft Azure account with access to Cobalt 100 based instances (Dpsv6). Basic
      understanding of Python and machine learning, and familiarity with ONNX Runtime and Azure
      cloud services, are also assumed.
  - question: When creating the VM, which size series and OS image should I choose?
    answer: >-
      Use a general-purpose D-series Dpsv6 Arm64 VM and select Ubuntu Pro 24.04 LTS as the base
      image. The Learning Path guides you through creation using the Azure portal.
  - question: Can I use the Azure CLI or IaC to create the VM instead of the portal?
    answer: >-
      There are multiple ways to create a Cobalt 100 VM, but this Learning Path uses the Azure
      portal. Other methods are not covered in the steps.
  - question: How should I prepare the Python environment for ONNX Runtime on the VM?
    answer: >-
      Install Python 3, pip, and venv on Ubuntu Pro 24.04 LTS, then create and activate a virtual
      environment as shown in the steps. This prepares the environment to run ONNX models with
      ONNX Runtime.
  - question: How do I run and validate the SqueezeNet INT8 baseline and benchmark?
    answer: >-
      Use the provided baseline.py to load squeezenet-int8.onnx and time a single inference to
      confirm ONNX Runtime is working. Then run onnxruntime_perf_test for detailed statistics;
      successful runs finish without errors and report latency or benchmark metrics.
# END generated_summary_faq

author: Pareena Verma    

### Tags
skilllevels: Introductory
subjects: ML
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - Python
    - ONNX Runtime

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Azure Virtual Machines documentation
      link: https://learn.microsoft.com/en-us/azure/virtual-machines/
      type: documentation
  - resource:
        title: ONNX Runtime Docs
        link: https://onnxruntime.ai/docs/
        type: documentation
  - resource:
        title: ONNX (Open Neural Network Exchange) documentation
        link: https://onnx.ai/
        type: documentation
  - resource:
        title: onnxruntime_perf_test tool - ONNX Runtime performance benchmarking
        link: https://onnxruntime.ai/docs/performance/tune-performance/profiling-tools.html#in-code-performance-profiling
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

