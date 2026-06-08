---
title: Accelerate Matrix Multiplication Performance with SME2
description: Learn how to implement and optimize matrix multiplication using Arm's Scalable Matrix Extension 2 (SME2) with assembly and intrinsics, including benchmarking and validation on Arm hardware.

minutes_to_complete: 60

who_is_this_for: This Learning Path is an advanced topic for developers who want to accelerate the performance of matrix multiplication using Arm's Scalable Matrix Extension Version 2 (SME2).

learning_objectives:
    - Implement a baseline matrix multiplication kernel in C without SME2
    - Use SME2 assembly instructions to accelerate matrix multiplication performance
    - Use SME2 intrinsics to vectorize and optimize matrix multiplication
    - Compile code with SME2 intrinsics and assembly
    - Benchmark and validate SME2-accelerated matrix multiplication on Arm hardware or in a Linux-based emulation environment
    - Compare performance metrics between baseline and SME2-optimized implementations

prerequisites:
    - Working knowledge of Arm’s SVE and SME2 instruction sets
    - Intermediate proficiency with the C programming language and the Armv9-A assembly language
    - A computer running Linux, macOS, or Windows
    - Installations of Git, CMake and Ninja for project setup
    - A platform that supports SME2 - see the list of [devices with SME2 support](/learning-paths/cross-platform/multiplying-matrices-with-sme2/1-get-started/#devices) or an emulator to run code with SME2 instructions
    - Installation of Docker for SME2 emulation (if you don't have SME2 available)
    - Installation of Android Development Studio and adb (if you're targeting an Android phone with SME2 support)
    - Compiler support for SME2 instructions (for example, LLVM 18 or later with SME2 backend support)

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:48:10Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: eb01b77f36323331c080615edcbddbf8cb56cf005f2249f1ea309ab1dbec8616
  summary_generated_at: '2026-06-01T21:13:59Z'
  summary_source_hash: eb01b77f36323331c080615edcbddbf8cb56cf005f2249f1ea309ab1dbec8616
  faq_generated_at: '2026-06-02T21:48:10Z'
  faq_source_hash: eb01b77f36323331c080615edcbddbf8cb56cf005f2249f1ea309ab1dbec8616
  summary: >-
    This advanced Learning Path shows how to implement, build, and evaluate matrix multiplication
    using Arm’s Scalable Matrix Extension 2 (SME2) with both assembly and intrinsics. You will
    set up a development environment on Linux, macOS, or Windows and choose either native SME2
    hardware (demonstrated on macOS with an M4 chip or some Android phones) or a Linux-based emulation
    flow. After verifying your toolchain with CMake/Ninja and Clang/LLVM (LLVM 18+), you will
    create a vanilla C matmul as a correctness reference, then add SME2 intrinsics and assembly,
    learn how streaming mode and ZA state are handled via ACLE annotations, and benchmark and
    validate results. Prerequisites include working knowledge of SVE/SME2, intermediate C and
    Armv9-A assembly, Git, CMake, Ninja, and optionally Docker or Android Development Studio and
    adb.
  faqs:
  - question: What do I need before running the examples?
    answer: >-
      You need working knowledge of SVE and SME2, intermediate C and Armv9-A assembly skills,
      and a computer running Linux, macOS, or Windows. Install Git, CMake, Ninja, and a compiler
      with SME2 support (for example, LLVM 18+). For emulation, install Docker; for Android targets,
      install Android Studio and adb, and use a phone with SME2 support.
  - question: Should I use native SME2 hardware or an emulator?
    answer: >-
      Use native SME2 hardware when available for direct execution; this Learning Path demonstrates
      macOS with an M4 chip and some Android phones with SME2 support. If you lack SME2 hardware,
      use the Linux-based emulation option. iPhone and iPad are not covered by the instructions,
      even though they have SME2 support.
  - question: How do I verify my SME2 toolchain and environment are set up correctly?
    answer: >-
      Build the provided code examples with CMake to confirm the compiler, hardware (or emulator),
      and tools are working. For native builds, you may need to tell CMake which Clang to use
      if the system default is not suitable. A successful, error-free build indicates your environment
      is ready.
  - question: How do I use streaming mode and handle ZA state in SME?
    answer: >-
      Annotate the relevant functions to enable streaming mode as defined by the Arm C Language
      Extensions (ACLE). The compiler manages saving and restoring state, including ZA storage,
      when streaming-mode functions call each other. No manual state management is required.
  - question: How do I validate and benchmark the SME2-optimized matrix multiplication?
    answer: >-
      First implement the vanilla C matrix multiplication as a correctness reference. Then compile
      the SME2 intrinsics and assembly implementations and run benchmarks on SME2 hardware or
      in a Linux-based emulation environment. Compare the performance metrics to the baseline
      and confirm numerical results match.
# END generated_summary_faq

author: Arnaud de Grandmaison

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Arm C1
tools_software_languages:
    - C
    - Clang
    - LLVM
    - SME2

operatingsystems:
    - Linux
    - macOS
    - Windows
shared_path: true
shared_between:
    - laptops-and-desktops
    - mobile-graphics-and-gaming

further_reading:
    - resource:
        title: SVE Programming Examples
        link: https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://developer.arm.com/documentation/dai0548/latest/&ved=2ahUKEwisi76m-f2GAxUDSKQEHfyWClAQFnoECA4QAQ&usg=AOvVaw1YPQ-aQsHmumnZykaFxM0b
        type: documentation
    - resource:
        title: Port Code to Arm Scalable Vector Extension (SVE)
        link: /learning-paths/servers-and-cloud-computing/sve
        type: website
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
    - resource:
        title: Build adaptive libraries with multiversioning
        link: /learning-paths/cross-platform/function-multiversioning/
        type: website
    - resource:
        title: SME Programmer's Guide
        link: https://developer.arm.com/documentation/109246/latest
        type: documentation
    - resource:
        title: Matrix Multiplication
        link: https://en.wikipedia.org/wiki/Matrix_multiplication
        type: website
    - resource:
        title: Compiler Intrinsics
        link: https://en.wikipedia.org/wiki/Intrinsic_function
        type: website
    - resource:
        title: ACLE --- Arm C Language Extension
        link: https://github.com/ARM-software/acle
        type: website
    - resource:
        title: Application Binary Interface for the Arm Architecture
        link: https://github.com/ARM-software/abi-aa
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

