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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:58Z'
  generator: template
  source_hash: 84ba887426f3ca45b698c79028023d80cbf0a06e6bc2fb71fcbe924943078dd8
  summary: >-
    Deploy SqueezeNet 1.0 INT8 model with ONNX Runtime on Azure Cobalt 100 walks you through an
    end-to-end Arm software workflow. It is designed for developers deploying ONNX-based applications
    on Arm-based machines. By the end, you will be able to provision an Azure Arm64 virtual machine
    using Azure console, with Ubuntu Pro 24.04 LTS as the base image and perform ONNX baseline
    testing and benchmarking on Arm64 virtual machines. It focuses on tools and technologies such
    as Python and ONNX Runtime, Linux environments, Arm platforms including Neoverse, and cloud
    platforms such as Microsoft Azure. The main steps cover Overview, Create an Arm-based Azure
    Cobalt 100 virtual machine, ONNX Installation, Baseline Testing, and Benchmark ONNX runtime
    performance with onnxruntime_perf_test.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Azure Arm64 virtual machine using Azure console, with Ubuntu Pro 24.04
      LTS as the base image and perform ONNX baseline testing and benchmarking on Arm64 virtual
      machines.
  - question: Who is this Learning Path for?
    answer: >-
      This Learning Path is for developers deploying ONNX-based applications on Arm-based machines.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Microsoft Azure](https://azure.microsoft.com/)
      account with access to Cobalt 100 based instances (Dpsv6); Basic understanding of Python
      and machine learning concepts; Familiarity with [ONNX Runtime](https://onnxruntime.ai/docs/)
      and Azure cloud services.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Python and ONNX Runtime, Linux environments, Arm
      platforms such as Neoverse, and cloud platforms such as Microsoft Azure.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Overview, Create an Arm-based Azure Cobalt 100 virtual
      machine, ONNX Installation, Baseline Testing, and Benchmark ONNX runtime performance with
      onnxruntime_perf_test.
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

