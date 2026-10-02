---
title: Deploy SqueezeNet 1.0 INT8 model with ONNX Runtime on Azure Cobalt 100

minutes_to_complete: 60   

who_is_this_for: This Learning Path is for developers deploying ONNX-based applications on Arm-based machines.

learning_objectives:
    - Provision an Azure Arm64 virtual machine (VM) using Azure console, with Ubuntu Pro 24.04 LTS as the base image.
    - Perform ONNX baseline testing and benchmarking on Arm64 VMs.

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100-based instances (Dpsv6)
    - Basic understanding of Python and machine learning concepts
    - Familiarity with [ONNX Runtime](https://onnxruntime.ai/docs/) and Azure cloud services

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-01T19:41:46Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3dfb5d613a9e88a35777de0adc65fbcacd46a906031c4d933c744abf9689e6a0
  summary_generated_at: '2026-10-01T19:41:46Z'
  summary_source_hash: 3dfb5d613a9e88a35777de0adc65fbcacd46a906031c4d933c744abf9689e6a0
  faq_generated_at: '2026-10-01T19:41:46Z'
  faq_source_hash: 3dfb5d613a9e88a35777de0adc65fbcacd46a906031c4d933c744abf9689e6a0
  summary: >-
    You'll run and benchmark SqueezeNet 1.0 INT8 inference with ONNX Runtime on an Arm-based Azure VM powered by Cobalt
    100. First, you'll provision an Ubuntu Pro 24.04 LTS Dpsv6 VM and prepare a Python
    environment. You'll then run a baseline script to validate inference and record latency. Finally,
    you'll use `onnxruntime_perf_test` to collect more detailed performance statistics on the Arm64
    system.
  faqs:
  - question: Which Azure VM size and OS image should I use?
    answer: >-
      Select `D4ps_v6` from the Dpsv6 series powered by Azure Cobalt 100.
      Use the Ubuntu Pro 24.04 LTS image and select **Arm64** as the VM architecture.
  - question: What do I need in place before running the baseline latency test?
    answer: >-
      Activate your Python virtual environment, have the `baseline.py` script ready, and ensure that
      the SqueezeNet INT8 model file is available as `squeezenet-int8.onnx`. Place the model in
      the same working directory as the script or provide its full path.
  - question: How do I know the baseline test worked correctly?
    answer: >-
      The script completes without errors and reports a timing result for a single inference through
      the SqueezeNet INT8 model. Successful execution confirms that ONNX Runtime is functioning
      on the VM.
  - question: When should I use onnxruntime_perf_test, and what output should I expect?
    answer: >-
      Use `onnxruntime_perf_test` after validating the Python baseline to capture more detailed
      performance statistics. Expect a summary of inference metrics that you can use to evaluate
      ONNX Runtime efficiency on the Azure Arm64 instance.
  - question: Does the baseline script use a real image as input?
    answer: >-
      No. You generate random `float32` data with shape `(1, 3, 224, 224)`, representing one input
      with three color channels and dimensions of 224 by 224 pixels. You use this synthetic input
      to measure inference latency.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
platforms:
  - Microsoft Azure Cobalt

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
