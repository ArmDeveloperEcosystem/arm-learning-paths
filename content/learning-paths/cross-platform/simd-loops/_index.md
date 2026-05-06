---
title: Learn SVE and SME programming with SIMD Loops

description: Learn how to write high-performance SIMD code using the SIMD Loops project, with hands-on examples demonstrating SVE, SVE2, and SME2 features on Arm processors.

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for software developers who want to learn how to use the full range of features available in SVE, SVE2, and SME2 to improve software performance on Arm processors.

learning_objectives:
     - Improve SIMD code performance using Scalable Vector Extension (SVE) and Scalable Matrix Extension (SME)
     - Describe what SIMD Loops contains and how kernels are organized across scalar, Neon, SVE, SVE2, and SME2 variants
     - Build and run a selected kernel with the provided runner and validate correctness against the C reference
     - Choose the appropriate build target to compare Neon, SVE/SVE2, and SME2 implementations

prerequisites:
    - An AArch64 computer running Linux or macOS. You can use cloud instances, refer to [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp/) for a list of cloud service providers
    - Some familiarity with SIMD programming and Neon intrinsics
    - Recent toolchains that support SVE/SME (GCC 13+ or Clang 16+ recommended)

generate_summary_faq: true

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:54Z'
  generator: template
  source_hash: b1c43e1bf971db4582ca358c98dab2c7e6e047d6c79bfcc0db148bc575f33679
  summary: >-
    Learn how to write high-performance SIMD code using the SIMD Loops project, with hands-on
    examples demonstrating SVE, SVE2, and SME2 features on Arm processors. It is designed for
    software developers who want to learn how to use the full range of features available in SVE,
    SVE2, and SME2 to improve software performance on Arm processors. By the end, you will be
    able to improve SIMD code performance using Scalable Vector Extension (SVE) and Scalable Matrix
    Extension (SME), describe what SIMD Loops contains and how kernels are organized across scalar,
    Neon, SVE, SVE2, and SME2 variants, and build and run a selected kernel with the provided
    runner and validate correctness against the C reference. It focuses on tools and technologies
    such as C, CPP, GCC, Clang, and SME2, Linux and macOS environments, and Arm platforms including
    Neoverse and Cortex-A. The main steps cover About Single Instruction, Multiple Data loops,
    Using SIMD Loops, Code example, and Learning with SIMD Loops.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will improve SIMD code performance using Scalable Vector Extension (SVE) and Scalable
      Matrix Extension (SME), describe what SIMD Loops contains and how kernels are organized
      across scalar, Neon, SVE, SVE2, and SME2 variants, and build and run a selected kernel with
      the provided runner and validate correctness against the C reference. Learn how to write
      high-performance SIMD code using the SIMD Loops project, with hands-on examples demonstrating
      SVE, SVE2, and SME2 features on Arm processors.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for software developers who want to learn how to use the full
      range of features available in SVE, SVE2, and SME2 to improve software performance on Arm
      processors.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An AArch64 computer running Linux or
      macOS. You can use cloud instances, refer to [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp/)
      for a list of cloud service providers; Some familiarity with SIMD programming and Neon intrinsics;
      Recent toolchains that support SVE/SME (GCC 13+ or Clang 16+ recommended).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including C, CPP, GCC, Clang, and SME2, Linux and macOS environments,
      and Arm platforms such as Neoverse and Cortex-A.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around About Single Instruction, Multiple Data loops, Using
      SIMD Loops, Code example, and Learning with SIMD Loops.
# END generated_summary_faq

author:
    - Alejandro Martinez Vicente
    - Mohamad Najem

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
    - Cortex-A
operatingsystems:
    - Linux
    - macOS
tools_software_languages:
  - C
  - CPP
  - GCC
  - Clang
  - SME2
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - mobile-graphics-and-gaming
    - automotive

further_reading:
    - resource:
        title: SVE Programming Examples
        link: https://developer.arm.com/documentation/dai0548/latest
        type: documentation
    - resource:
        title: SIMD Loops Repository
        link: https://gitlab.arm.com/architecture/simd-loops
        type: documentation
    - resource:
        title: Scalable Vector Extensions Resources
        link: https://developer.arm.com/Architectures/Scalable%20Vector%20Extensions
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
        title: Compiler Intrinsics
        link: https://en.wikipedia.org/wiki/Intrinsic_function
        type: website
    - resource:
        title: ACLE - Arm C Language Extension
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

