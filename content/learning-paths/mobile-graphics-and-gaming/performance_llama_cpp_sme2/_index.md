---
title: Measure LLM inference performance with KleidiAI and SME2 on Android
description: Learn how to build llama.cpp with KleidiAI and SME2 support to profile and accelerate LLM inference performance on Android devices.
    
minutes_to_complete: 40

who_is_this_for: This is an advanced topic for software developers, performance engineers, and AI practitioners 

learning_objectives:
    - Build llama.cpp with KleidiAI and SME2 support
    - Profile LLM inference performance on Android
    - Understand how KleidiAI and SME2 accelerate LLM operators

prerequisites:
    - Knowledge of KleidiAI and SME2
    - A Linux host machine (x86_64 or aarch64) for building llama.cpp with the Arm GNU Toolchain
    - Git, CMake, and Android Debug Bridge (ADB) installed on your host machine
    - An Android device with Arm SME2 support for running and profiling the executable

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:02:40Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4962524245ec5e5e07d1207537208a22c2e9569f252f36d758c4f828d2104272
  summary_generated_at: '2026-06-02T02:55:26Z'
  summary_source_hash: 4962524245ec5e5e07d1207537208a22c2e9569f252f36d758c4f828d2104272
  faq_generated_at: '2026-06-03T00:02:40Z'
  faq_source_hash: 4962524245ec5e5e07d1207537208a22c2e9569f252f36d758c4f828d2104272
  summary: >-
    This advanced Learning Path shows you how to build a statically linked llama.cpp (llama-cli)
    with Arm KleidiAI and Scalable Matrix Extension 2 (SME2) to measure LLM inference performance
    on Android. You cross-compile on a Linux host (x86_64 or aarch64) using the Linux-hosted Arm
    GNU Toolchain and GCC 14.2 or later, then deploy to an SME2-capable Android device via ADB.
    Along the way you trace how acceleration flows from llama.cpp through the ggml-cpu backend
    into KleidiAI microkernels that can use SME2, I8MM, or DotProd, and learn how to verify that
    SME2 kernels are active. You then compare performance with SME2 enabled and disabled using
    a 3B-parameter GGUF model. Prerequisites include knowledge of KleidiAI and SME2, plus Git,
    CMake, and ADB.
  faqs:
  - question: What do I need before building and running this path?
    answer: >-
      You need a Linux host machine (x86_64 or aarch64), the Linux‑hosted Arm GNU Toolchain, Git,
      CMake, and ADB. You also need an Android device with Arm SME2 support and prior knowledge
      of KleidiAI and SME2.
  - question: Which compiler and target should I use to enable SME2 in llama.cpp?
    answer: >-
      Use the aarch64 GCC cross‑compile toolchain with the aarch64‑none‑linux‑gnu‑ prefix from
      the Linux‑hosted Arm GNU Toolchain. GCC version 14.2 or later is required for SME2, and
      the build produces a statically linked llama-cli.
  - question: How do I put the model and binary onto the Android device?
    answer: >-
      ADB is the recommended way to transfer files and open a shell on the device. Download the
      Llama-3.2-3B-Instruct-Q4_0.gguf model from Hugging Face using curl on your host, then use
      ADB to move both the model and the built binary to the device.
  - question: How do I verify that SME2 microkernels are being used during inference?
    answer: >-
      The steps show how to confirm SME2 microkernels are active and trace the selection path
      from llama.cpp through ggml‑cpu to KleidiAI. Follow the verification guidance when running
      on the SME2‑capable Android device.
  - question: What should I check if SME2 is not selected at runtime?
    answer: >-
      Verify the target Android device supports Arm SME2 and that you built with GCC 14.2+ and
      the SME2‑enabled configuration. If SME2 is unavailable, the KleidiAI integration may select
      I8MM or DotProd microkernels depending on hardware support.
# END generated_summary_faq

author: Zenon Zhilong Xiu

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Arm C1
tools_software_languages:
    - SME2
    - C++
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

