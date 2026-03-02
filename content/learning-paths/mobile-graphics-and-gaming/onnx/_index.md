---
title: "ONNX in Action: Building, Optimizing, and Deploying ML Models on Arm64 and Mobile Devices"

draft: true
cascade:
    draft: true
    
minutes_to_complete: 240

who_is_this_for: This learning path is intended for developers who want to build, optimize, and deploy machine learning models using ONNX. It is particularly relevant for those targeting Arm64-based platforms such as Raspberry Pi, Arm-based laptops, cloud instances, or Android smartphones, where performance-per-watt and efficient edge inference are critical.

learning_objectives:
  - Explain what ONNX is and how it enables model portability across ML frameworks.
  - Build and export a simple neural network model in Python to ONNX format.
  - Run inference (and optionally training workflows) using ONNX Runtime on Arm64 platforms.
  - Apply model optimization techniques to improve performance.
  - Integrate and deploy an optimized ONNX model inside an Android application.

prerequisites:
  - A development machine with Python 3.10 or 3.11 installed (Prebuilt ONNX Runtime packages for Arm platforms may not yet support Python 3.12.)
  - Basic familiarity with PyTorch or TensorFlow.
  - An Arm64 device (e.g., Raspberry Pi or Android smartphone).
  - "[Android Studio](https://developer.android.com/studio) for building and deploying the Android application."

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
tools_software_languages:
  - Python
  - PyTorch
  - TensorFlow
  - ONNX
  - Android
  - Android Studio
  - Kotlin
  - Java

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
