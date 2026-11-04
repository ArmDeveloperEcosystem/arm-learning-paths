---
title: Build and profile a YOLOX pipeline with KleidiCV on arm64
description: Build a YOLOX object detection pipeline on arm64 Linux and compare baseline and KleidiCV preprocessing and pipeline latency.

draft: true
cascade:
    draft: true

lastmod: 2026-10-29

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for C++ developers who want to deploy ONNX computer vision models and measure image-processing performance on arm64 Linux boards.

learning_objectives:
  - Build matching baseline and default KleidiCV versions of OpenCV
  - Deploy a YOLOX ONNX model and label objects in a static image
  - Compare image-operation, full preprocessing, and pipeline latency to distinguish local optimization from application-level improvement

prerequisites:
  - An arm64 development board running 64-bit Debian or Ubuntu
  - At least 12 GB of free storage for two OpenCV builds
  - GCC 10 or later, or Clang 12 or later
  - Familiarity with C++, CMake, and the Linux command line
  - Time for source downloads and two OpenCV compilations in addition to the 90-minute hands-on estimate

author: Jett Zhou

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: ML
armips:
  - Cortex-A
operatingsystems:
  - Linux
tools_software_languages:
  - OpenCV
  - ONNX
  - KleidiCV
  - C++
  - CMake

further_reading:
  - resource:
      title: OpenCV DNN module
      link: https://docs.opencv.org/4.x/d6/d0f/group__dnn.html
      type: documentation
  - resource:
      title: OpenCV Zoo YOLOX model
      link: https://github.com/opencv/opencv_zoo/tree/main/models/object_detection_yolox
      type: website
  - resource:
      title: Accelerate an OpenCV-based Android application with KleidiCV
      link: /learning-paths/mobile-graphics-and-gaming/android_opencv_kleidicv/
      type: website
  - resource:
      title: Profile ONNX model performance with SME2 using KleidiAI and ONNX Runtime
      link: /learning-paths/mobile-graphics-and-gaming/performance_onnxruntime_kleidiai_sme2/
      type: website
  - resource:
      title: KleidiCV repository
      link: https://gitlab.arm.com/kleidi/kleidicv
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
