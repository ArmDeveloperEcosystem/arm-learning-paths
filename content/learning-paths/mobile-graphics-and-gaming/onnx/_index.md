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
