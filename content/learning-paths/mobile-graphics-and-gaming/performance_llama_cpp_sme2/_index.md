---
title: Measure LLM inference performance with KleidiAI and SME2 on Android
description: Learn how to build llama.cpp with KleidiAI and SME2 support to profile and accelerate LLM inference performance on Android devices.

minutes_to_complete: 40

who_is_this_for: This is an advanced topic for software developers, performance engineers, and AI practitioners 

learning_objectives:
    - Build llama.cpp with KleidiAI and SME2 support
    - Profile large language model (LLM) inference performance on Android
    - Understand how KleidiAI and SME2 accelerate LLM operators

prerequisites:
    - Knowledge of KleidiAI and SME2
    - A Linux host machine (x86_64 or aarch64) for building `llama.cpp` with the Arm GNU Toolchain
    - Git, CMake, and Android Debug Bridge (ADB) installed on your host machine
    - An Android device with Arm SME2 support for running and profiling the executable

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-17T22:13:18Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9e7bf9a27908bce1b6c3af5262ecc9b529426b8fdb575af08d8683389ef5c7e7
  summary_generated_at: '2026-08-17T22:13:18Z'
  summary_source_hash: 9e7bf9a27908bce1b6c3af5262ecc9b529426b8fdb575af08d8683389ef5c7e7
  faq_generated_at: '2026-08-17T22:13:18Z'
  faq_source_hash: 9e7bf9a27908bce1b6c3af5262ecc9b529426b8fdb575af08d8683389ef5c7e7
  summary: >-
    You'll build `llama.cpp` with KleidiAI and SME2, then measure LLM inference on Android. First, you'll cross-compile
    `llama-cli` for `aarch64`, deploy it with ADB, and run the Llama-3.2-3B-Instruct-Q4_0 model with
    SME2 enabled and disabled. Then, you'll trace acceleration through `ggml-cpu` into KleidiAI, and verify that
    SME2 microkernels are active before comparing the reported performance.
  faqs:
  - question: Which compiler and toolchain should I use to build with SME2?
    answer: >-
      Use the `aarch64` GCC cross-compile toolchain with the `aarch64-none-linux-gnu-` prefix from
      the Linux-hosted Arm GNU Toolchain. You need GCC version 14.2 or later to enable SME2.
  - question: How do I follow the build steps if I'm on macOS or Windows?
    answer: >-
      Run the commands in a Linux environment, such as a Linux VM, container, or a Linux development
      machine. The build uses the Linux-hosted Arm GNU Toolchain.
  - question: What files must be on the Android device before measuring performance?
    answer: >-
      Place the built `llama-cli` executable and the `Llama-3.2-3B-Instruct-Q4_0.gguf` model on the
      device.
  - question: How do I verify that the SME2 path is used during inference?
    answer: >-
      Follow the verification step that confirms SME2 microkernels are active. The `ggml-cpu` backend
      selects KleidiAI SME2 microkernels when the hardware supports them.
  - question: How should I compare runs with SME2 enabled and disabled?
    answer: >-
      Run the model on the Android device twice — once with SME2 enabled and once with
      it disabled. Compare the performance reported by `llama.cpp` from both runs.
# END generated_summary_faq

author: Zenon Zhilong Xiu

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Arm C1
tools_software_languages:
    - SME2
    - CPP
    - llama.cpp
operatingsystems:
    - Android
    - Linux

further_reading:
    - resource:
        title: Arm Scalable Matrix Extension introduction, part 1
        link: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction
        type: blog
    - resource:
        title: Arm Scalable Matrix Extension instructions, part 2
        link: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/arm-scalable-matrix-extension-introduction-p2
        type: blog
    - resource:
        title: Arm SME2 introduction, part 4
        link: https://developer.arm.com/community/arm-community-blogs/b/architectures-and-processors-blog/posts/part4-arm-sme2-introduction
        type: blog
    - resource:
        title: Profile llama.cpp performance with Arm Streamline and KleidiAI LLM kernels
        link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/llama_cpp_streamline/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
