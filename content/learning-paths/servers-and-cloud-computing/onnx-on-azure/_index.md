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

author: Pareena Verma    

### Tags
skilllevels: Introductory
subjects: ML
cloud_service_providers: Microsoft Azure

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
