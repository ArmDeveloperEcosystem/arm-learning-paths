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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-04T22:09:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9fa0855615bffa32d54a2e4ec9cf61883d938b205a359e2a5d363d98412583eb
  summary_generated_at: '2026-08-04T22:09:54Z'
  summary_source_hash: 9fa0855615bffa32d54a2e4ec9cf61883d938b205a359e2a5d363d98412583eb
  faq_generated_at: '2026-08-04T22:09:54Z'
  faq_source_hash: 9fa0855615bffa32d54a2e4ec9cf61883d938b205a359e2a5d363d98412583eb
  summary: >-
    You build and run AI-powered camera pipelines that
    apply background blur, low-light enhancement, and temporal denoising on Arm systems with SME2.
    You clone the AI camera pipelines repository with Git and Git LFS, create a Docker-based build
    environment, and compile the applications. You then run the provided binaries to transform
    sample images and frames, producing output artifacts that can be inspected to validate each
    effect. You can run a benchmark mode for each pipeline to exercise the core processing loop and
    observe how KleidiCV and KleidiAI integrate on Arm while SME2 accelerates matrix-intensive
    operations common in real-time camera workloads.
  faqs:
  - question: What should I check before building the container?
    answer: >-
      Confirm you are on an Arm64 machine with SME2 support and that Git, Git LFS, and Docker
      are installed. The instructions have been tested on Ubuntu 24.04.
  - question: The repository path differs between steps. Which directory should I use?
    answer: >-
      Use the directory created by your git clone command. If a later command references a different
      path, adjust it to match your local clone location.
  - question: Where do I run the build versus the pipelines?
    answer: >-
      Build the applications inside the Docker container created from the provided Dockerfile.
      Then run the pipelines from the project directory as shown when applying transformations
      and benchmarks.
  - question: What result should I expect after running the background blur example?
    answer: >-
      The command writes a transformed image, such as test_output_cinematic_mode.png, based on
      the sample input in the resources directory. Verify the file is created and that the background
      is blurred in the output.
  - question: Which executables provide benchmark mode, and when should I use them?
    answer: >-
      Use the binaries cinematic_mode_benchmark, low_light_image_enhancement_benchmark, and neural_denoiser_temporal_benchmark_4K.
      They run the core processing loop in a hot loop to measure performance characteristics with
      KleidiCV and KleidiAI on Arm.
# END generated_summary_faq

author: Arnaud de Grandmaison

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
