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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:01:17Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: aba1cea365c0c61e84fb545ada15a64ed52c099f1252dc6312f88ee82385d2d0
  summary_generated_at: '2026-06-02T02:54:49Z'
  summary_source_hash: aba1cea365c0c61e84fb545ada15a64ed52c099f1252dc6312f88ee82385d2d0
  faq_generated_at: '2026-06-03T00:01:17Z'
  faq_source_hash: aba1cea365c0c61e84fb545ada15a64ed52c099f1252dc6312f88ee82385d2d0
  summary: >-
    This advanced Learning Path shows how to build, optimize, and deploy ONNX models for Arm64
    platforms using ONNX Runtime. You will create a small digit-recognition CNN in Python, export
    it to ONNX, validate numerical parity with ONNX Runtime, and apply model optimization techniques
    such as layer fusion. The steps target Arm64 devices including Raspberry Pi, Arm-based servers,
    Windows on Arm, and Android, with Apple Silicon suitable for development. You will culminate
    in deploying an optimized model inside an Android application, using the CPU execution provider
    on edge devices and NNAPI on Android. Prerequisites include Python 3.10 or 3.11, basic PyTorch
    or TensorFlow familiarity, an Arm64 device, and Android Studio for the final deployment stage.
  faqs:
  - question: Which Python version should I install for this Learning Path?
    answer: >-
      Use Python 3.10 or 3.11. Prebuilt ONNX Runtime packages for Arm platforms don't yet support
      Python 3.12.
  - question: Which Arm64 hardware can I use, and can I develop on macOS or Windows on Arm?
    answer: >-
      You can use Raspberry Pi 4/5 (64-bit OS), Jetson (Arm64 CPU; GPU via CUDA if using NVIDIA
      stack), or Arm-based servers. Apple Silicon (macOS/Arm64) and Windows on Arm are suitable
      for development, with deployment to Arm64 Linux later.
  - question: How do I know ONNX Runtime is using the expected execution provider on my device?
    answer: >-
      In the setup step you verify that ONNX Runtime detects and uses the available execution
      providers. On edge Arm64 devices the CPU execution provider is used; on Android the NNAPI
      execution provider is targeted.
  - question: Do I need to prepare a dataset before training the digit recognizer?
    answer: >-
      No manual collection is required. The path guides you to generate a custom Sudoku digit
      dataset, starting from a Hugging Face parquet dataset.
  - question: What artifacts should I expect after training and evaluation, and when is the model
      ready for Android deployment?
    answer: >-
      You will have a PyTorch checkpoint and an exported ONNX model, with numerical parity verified
      against ONNX Runtime. After reviewing evaluation outputs such as the confusion matrix and
      visual diagnostics, proceed to integrate the optimized model into the Android application.
# END generated_summary_faq

author: Dawid Borycki

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

