---
title: Deploy optimized ML models with ONNX Runtime on Arm platforms
description: Learn how to build, optimize, and deploy machine learning models using ONNX Runtime on Arm64 platforms, including Raspberry Pi, cloud instances, and Android devices.

minutes_to_complete: 240

who_is_this_for: This is an advanced topic for developers who want to build, optimize, and deploy machine learning models using ONNX on Arm64-based platforms such as Raspberry Pi, Arm-based laptops, cloud instances, or Android smartphones.

learning_objectives:
  - Explain what ONNX is and how it enables model portability across ML frameworks
  - Build and export a neural network model in Python to ONNX format
  - Run inference using ONNX Runtime on Arm64 platforms
  - Apply model optimization techniques to improve performance
  - Deploy an optimized ONNX model in an Android application

prerequisites:
  - A development machine with Python 3.10 or 3.11 installed (Prebuilt ONNX Runtime packages for Arm platforms don't yet support Python 3.12)
  - Basic familiarity with PyTorch or TensorFlow
  - An Arm64 device such as a Raspberry Pi or Android smartphone
  - Android Studio (required only for the final deployment section)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-17T22:11:59Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4f34e1982fb812f3ea7352ce4c628d1fe449ba625da430ec7d25d968efc83601
  summary_generated_at: '2026-08-17T22:11:59Z'
  summary_source_hash: 4f34e1982fb812f3ea7352ce4c628d1fe449ba625da430ec7d25d968efc83601
  faq_generated_at: '2026-08-17T22:11:59Z'
  faq_source_hash: 4f34e1982fb812f3ea7352ce4c628d1fe449ba625da430ec7d25d968efc83601
  summary: >-
    This Learning Path walks through an end-to-end workflow for exporting and deploying a compact
    digit recognizer with ONNX Runtime on Arm64 platforms. You generate a synthetic Sudoku dataset,
    train a small CNN in Python, and export the best checkpoint to ONNX using PyTorch’s Dynamo-based
    exporter. The steps then validate numerical parity between PyTorch and ONNX Runtime, analyze
    results with a confusion matrix, and apply targeted optimizations such as layer fusion. Guidance
    on execution provider choices helps you verify runtime configuration on edge devices and Android
    (for example, NNAPI). The path concludes by preparing the optimized ONNX model for Android
    integration, while keeping the broader Sudoku pipeline deterministic and lightweight around
    the model.
  faqs:
  - question: How do I know ONNX Runtime is using the right execution provider on my device?
    answer: >-
      Verify the provider list reported by ONNX Runtime. You should see a CPU execution provider
      on Arm64 systems and NNAPI on Android when available before proceeding.
  - question: What artifacts should I expect after exporting the trained model to ONNX?
    answer: >-
      You will have an ONNX model file produced by the Dynamo-based exporter and your original
      PyTorch checkpoint. Use both to run inference and compare results across frameworks.
  - question: What should I check if ONNX Runtime predictions do not match PyTorch?
    answer: >-
      Confirm that preprocessing matches training: 28×28 grayscale inputs and consistent label
      mapping (0 = blank, 1–9 = digits). Re-run the validation and compare predictions and the
      confusion matrix to identify where outputs diverge.
  - question: I’m using Python 3.12. Can I follow the steps?
    answer: >-
      Prebuilt ONNX Runtime packages for Arm platforms don’t yet support Python 3.12, so use Python
      3.10 or 3.11.
  - question: How do I decide which execution provider to use for deployment?
    answer: >-
      Use the CPU execution provider for Arm64 development and edge devices, and NNAPI on Android
      when it is available. The setup step includes verifying which providers are detected on
      your target.
# END generated_summary_faq

author: Dawid Borycki

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: ML
armips:
  - Cortex-A
  - Neoverse
operatingsystems:
  - Windows
  - Linux
  - macOS
  - Android
tools_software_languages:
  - Python
  - PyTorch
  - TensorFlow
  - ONNX
  - Android
  - Android Studio
  - Kotlin

further_reading:
  - resource:
      title: ONNX
      link: https://onnx.ai
      type: documentation
  - resource:
      title: ONNX Runtime
      link: https://onnxruntime.ai
      type: documentation
  - resource:
      title: Getting Started with ONNX Runtime on Mobile
      link: https://onnxruntime.ai/docs/tutorials/mobile
      type: tutorial
  - resource:
      title: Optimizing Models with ONNX Runtime
      link: https://onnxruntime.ai/docs/performance/model-optimizations.html
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

