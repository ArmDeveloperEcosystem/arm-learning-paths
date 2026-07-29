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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-29T16:43:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: eb01b77f36323331c080615edcbddbf8cb56cf005f2249f1ea309ab1dbec8616
  summary_generated_at: '2026-07-29T16:43:54Z'
  summary_source_hash: eb01b77f36323331c080615edcbddbf8cb56cf005f2249f1ea309ab1dbec8616
  faq_generated_at: '2026-07-29T16:43:54Z'
  faq_source_hash: eb01b77f36323331c080615edcbddbf8cb56cf005f2249f1ea309ab1dbec8616
  summary: >-
    Start with a baseline C matrix-multiplication kernel, then build SME2-accelerated versions with
    intrinsics and assembly on supported Arm hardware or an emulator. You verify the toolchain with
    CMake, learn how SME streaming mode and ZA state work through Arm C Language Extensions, and
    implement a row-major reference kernel. You then benchmark SME2 versions and validate them against
    the baseline.
  faqs:
  - question: 'Which setup should I use: native SME2 hardware or emulation?'
    answer: >-
      Use native SME2 hardware if you have a supported device, such as a Mac with an M4 chip or
      some Android phones. Otherwise, use the emulation option and check the setup section's device
      list for native support.
  - question: CMake is finding the wrong Clang; what should I do?
    answer: >-
      Point CMake to the intended Clang when configuring the project. The system default might not
      support SME2, so select the compiler explicitly as described in the environment check.
  - question: How do I verify the environment is ready before continuing?
    answer: >-
      Build the examples in `code-examples/learning-paths/cross-platform/multiplying-matrices-with-sme2`
      using CMake. A successful build and run confirms that the toolchain, compiler, and hardware
      or emulator are configured correctly.
  - question: When should I enable streaming mode, and do I need to handle ZA state myself?
    answer: >-
      Enable streaming mode on functions that use SME features by applying the appropriate Arm C
      Language Extensions. The compiler manages streaming transitions and ZA save and restore, so
      you do not implement those operations manually.
  - question: What result should I expect from the baseline C matrix multiplication?
    answer: >-
      The baseline row-major implementation computes the reference output matrix. Keep that result
      and compare it with the intrinsics and assembly versions during benchmarking and validation.
# END generated_summary_faq

author: Arnaud de Grandmaison

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
