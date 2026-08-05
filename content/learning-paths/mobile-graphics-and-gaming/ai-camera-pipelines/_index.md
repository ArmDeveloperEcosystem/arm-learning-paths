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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-05T14:50:01Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9fa0855615bffa32d54a2e4ec9cf61883d938b205a359e2a5d363d98412583eb
  summary_generated_at: '2026-08-05T14:50:01Z'
  summary_source_hash: 9fa0855615bffa32d54a2e4ec9cf61883d938b205a359e2a5d363d98412583eb
  faq_generated_at: '2026-08-05T14:50:01Z'
  faq_source_hash: 9fa0855615bffa32d54a2e4ec9cf61883d938b205a359e2a5d363d98412583eb
  summary: >-
    You'll clone the AI camera pipelines repository, fetch assets with Git Large File System (LFS), and build the projects
    in Docker. You'll compile SME2-enabled pipelines with KleidiCV and KleidiAI, then run background
    blur, low-light enhancement, and temporal denoising on sample inputs. Finally, you'll run the applications and benchmark binaries, and verify that expected output
    images are generated.
  faqs:
  - question: Where should I run the Docker build and which files does it use?
    answer: >-
      Run `docker build` from the repository root, specifying `-f docker/Dockerfile` with the build
      context set to `docker/`. The build uses the provided Dockerfile and scripts under the `docker/`
      directory.
  - question: How do I fetch the large files after cloning the repository?
    answer: >-
      From inside the cloned repository, run `git lfs install` followed by `git lfs pull`. The commands download
      the required large assets referenced by Git LFS.
  - question: Where do I build the pipelines and where are the binaries placed?
    answer: >-
      Start a shell in the Docker container and build the pipelines there. You can find the compiled
      executables in the project’s `bin/` directory.
  - question: What result should I expect after running the background blur pipeline?
    answer: >-
      The pipeline reads the specified input image and writes a transformed image to the output
      path you provide, for example test_output_cinematic_mode.png. Verify that the output file
      is created without errors.
  - question: How do I use the benchmark mode and what indicates it worked?
    answer: >-
      Run the provided benchmark executables in `bin/`: `cinematic_mode_benchmark`,
      `low_light_image_enhancement_benchmark`, and `neural_denoiser_temporal_benchmark_4K`. The executables run the core loop multiple times. A
      successful run completes without errors and allows you to observe behavior on your system.
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
