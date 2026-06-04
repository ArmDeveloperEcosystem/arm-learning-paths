---
title: Accelerate Denoising, Background Blur and Low-Light Camera Effects with SME2

description: Learn how to build and optimize AI-powered camera pipeline applications on Arm Linux using KleidiAI, KleidiCV, and SME2 to accelerate denoising, background blur, and low-light effects.

minutes_to_complete: 30

who_is_this_for: This introductory topic is for mobile and computer-vision developers, camera pipeline engineers, and performance-minded practitioners who want to optimize real-time camera effects on Arm using KleidiAI and KleidiCV.

learning_objectives:
    - Build and run AI-powered camera pipeline applications
    - Use SME2 to improve the performance of real-time camera pipelines

prerequisites:
    - A computer running Arm Linux or macOS with Docker installed

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T23:39:57Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: dee181248ecc8cb40e3ad76642fdb216cbf1e7610dde2f2605ba04f111b8926a
  summary_generated_at: '2026-06-02T02:40:04Z'
  summary_source_hash: dee181248ecc8cb40e3ad76642fdb216cbf1e7610dde2f2605ba04f111b8926a
  faq_generated_at: '2026-06-02T23:39:57Z'
  faq_source_hash: dee181248ecc8cb40e3ad76642fdb216cbf1e7610dde2f2605ba04f111b8926a
  summary: >-
    Build and run AI-powered camera pipeline applications on Arm using SME2 with KleidiAI and
    KleidiCV. You will clone the ai-camera-pipelines repository with Git LFS, build a Docker container,
    compile the C++ pipelines, apply background blur, denoising, and low-light effects, and run
    provided benchmark binaries to exercise the hot loop and observe improvements from KleidiCV
    and KleidiAI. The steps target an Arm64 system with SME2 support, with instructions tested
    on Ubuntu 24.04. Prerequisites list a computer running Arm Linux or macOS with Docker installed,
    plus Git and Git LFS. After completing the path, you can build, run, and benchmark these real-time
    camera effects.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Use an Arm64 machine with SME2 support; the instructions were tested on Ubuntu 24.04. The
      prerequisites list a computer running Arm Linux or macOS with Docker installed, plus Git
      and Git LFS.
  - question: Which repository do I clone and why is Git LFS required?
    answer: >-
      Clone git.gitlab.arm.com/kleidi/kleidi-examples/ai-camera-pipelines.git. Git LFS is needed
      to fetch the large files referenced by the project.
  - question: How do I build the container used to compile the pipelines?
    answer: >-
      Build the Docker image from docker/Dockerfile with tag ai-camera-pipelines, passing the
      build args DOCKERHUB_MIRROR=docker.io and CI_UID=$(id -u), targeting the docker/ directory.
      Then start a shell in the container to compile the pipelines as shown in the steps.
  - question: How do I run a background blur or other effect and verify success?
    answer: >-
      Create a Python virtual environment, install numpy, opencv-python, pillow, and torch, then
      run the provided binaries from the bin directory. For background blur, run cinematic_mode
      with resources/test_input.png and expect an output image like test_output_cinematic_mode.png.
  - question: How do I run benchmarks and what result should I expect?
    answer: >-
      Use the benchmark executables: cinematic_mode_benchmark, low_light_image_enhancement_benchmark,
      and neural_denoiser_temporal_benchmark_4K. They run the core processing loop multiple times
      and demonstrate improvements enabled by KleidiCV (OpenCV kernels on Arm) and KleidiAI (LiteRT+XNNPack
      inference micro-kernels).
# END generated_summary_faq

author: Arnaud de Grandmaison

test_images:
    - ubuntu:latest
test_maintenance: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Arm C1
tools_software_languages:
    - CPP
    - Docker
    - SME2
operatingsystems:
    - Linux
    - macOS

further_reading:
    - resource:
        title: Accelerate Generative AI Workloads Using KleidiAI
        link: /learning-paths/cross-platform/kleidiai-explainer
        type: website
    - resource:
        title: LLM Inference on Android with KleidiAI, MediaPipe, and XNNPACK
        link: /learning-paths/mobile-graphics-and-gaming/kleidiai-on-android-with-mediapipe-and-xnnpack/
        type: website
    - resource:
        title: Vision LLM Inference on Android with KleidiAI and MNN
        link: /learning-paths/mobile-graphics-and-gaming/vision-llm-inference-on-android-with-kleidiai-and-mnn/
        type: website
    - resource:
        title: TensorFlow Lite is now LiteRT
        link: https://developers.googleblog.com/en/tensorflow-lite-is-now-litert/
        type: blog
    - resource:
        title: Introducing the Scalable Matrix Extension for the Armv9-A Architecture
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/scalable-matrix-extension-armv9-a-architecture
        type: website
    - resource:
        title: Arm Scalable Matrix Extension (SME) Introduction (Part 1)
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction
        type: blog
    - resource:
        title: Arm Scalable Matrix Extension (SME) Introduction (Part 2)
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction-p2
        type: blog
    - resource:
        title: (Part 3) Matrix-matrix multiplication. Neon, SVE, and SME compared
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/matrix-matrix-multiplication-neon-sve-and-sme-compared
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has a weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

