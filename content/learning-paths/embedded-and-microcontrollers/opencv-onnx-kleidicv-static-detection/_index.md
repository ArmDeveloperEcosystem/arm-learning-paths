---
title: Build an OpenCV YOLOX pipeline to benchmark KleidiCV preprocessing
description: Build a YOLOX object detection pipeline on arm64 Linux and compare baseline and KleidiCV preprocessing and pipeline latency.

lastmod: 2026-10-29

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for C++ developers who want to deploy ONNX computer vision models and measure image-processing performance on arm64 Linux boards.

learning_objectives:
  - Build matching baseline and default KleidiCV versions of OpenCV.
  - Deploy a YOLOX ONNX model and label objects in a static image.
  - Compare image-operation, full preprocessing, and pipeline latency to distinguish local optimization from application-level improvement.

prerequisites:
  - An arm64 development board running 64-bit Debian or Ubuntu
  - At least 12 GB of free storage for two OpenCV builds
  - GCC 10 or later, or Clang 12 or later
  - Familiarity with C++, CMake, and the Linux command line
  - Time for source downloads and two OpenCV compilations in addition to the 90-minute hands-on estimate

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-10T16:55:52Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 74c7b4d380778aa07890ae0ccc5f32e115036eb03330526762ed19038d07797c
  summary_generated_at: '2026-11-10T16:55:52Z'
  summary_source_hash: 74c7b4d380778aa07890ae0ccc5f32e115036eb03330526762ed19038d07797c
  faq_generated_at: '2026-11-10T16:55:52Z'
  faq_source_hash: 74c7b4d380778aa07890ae0ccc5f32e115036eb03330526762ed19038d07797c
  summary: >-
    You'll build a YOLOX static-image detection pipeline on an arm64 Linux board and compare
    preprocessing with and without KleidiCV. First, you'll identify the pipeline stages, then build
    matching OpenCV installations and prepare the model, labels, and image. You'll compile and run the
    C++ application against both builds. Finally, you'll check its detections, and benchmark image operations, full
    preprocessing, and in-memory pipeline latency under consistent conditions.
  # faqs:
  # - question: How do I know I’m running a 64-bit Arm userspace before building?
  #   answer: >-
  #     Run `uname -m`. The expected output is `aarch64`.
  # - question: Where should I place the YOLOX model and the test image?
  #   answer: >-
  #     Store them in the `static-detection` directory created earlier under your working folder.
  #     Use the downloaded filenames shown in the guide so the example application can find them.
  # - question: What system information should I record with my benchmark results?
  #   answer: >-
  #     Record `/etc/os-release`, the kernel from `uname -r`, and `lscpu` output for topology and CPU
  #     features. KleidiCV selects implementations based on available CPU features, so you need this
  #     context to compare runs.
  # - question: How should I prepare the board for consistent timing measurements?
  #   answer: >-
  #     Close unnecessary applications and allow the board to cool before each run. Keep the board and
  #     operating system, OpenCV source and compiler, release build configuration, model and image,
  #     warm-up and measured iteration counts, OpenCV thread count, CPU affinity, and CPU frequency
  #     governor consistent.
  # - question: How do I compare baseline and KleidiCV performance results?
  #   answer: >-
  #     Keep the inputs and common build settings the same, with KleidiCV enabled only in the second
  #     OpenCV build. Compare image-operation, full preprocessing, and end-to-end timings to separate
  #     local preprocessing gains from overall pipeline changes.
# END generated_summary_faq

author: Jett Zhou

generate_summary_faq: false
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
