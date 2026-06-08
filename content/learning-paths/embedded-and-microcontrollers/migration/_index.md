---
title: Migrating x86_64 workloads to aarch64

description: Learn the software migration methodology for porting Linux workloads from x86_64 to aarch64, including using Arm compilers, porting compiler intrinsics, and deploying applications in containers.

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for embedded software developers looking at migrating Linux workloads to aarch64.

learning_objectives: 
    - Understand software migration methodology
    - Use different Arm compilers and libraries
    - Port applications containing compiler intrinsics

prerequisites:
    - Introductory understanding of software containers
    - Knowledge about building workflows
    - Access to an aarch64 or x86_64 machine running Linux

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:32:21Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 81a15ff0d5579be9529a8c9c444be57521ebc48bbf5234f042f5a47a8a709b5c
  summary_generated_at: '2026-06-01T21:45:31Z'
  summary_source_hash: 81a15ff0d5579be9529a8c9c444be57521ebc48bbf5234f042f5a47a8a709b5c
  faq_generated_at: '2026-06-02T22:32:21Z'
  faq_source_hash: 81a15ff0d5579be9529a8c9c444be57521ebc48bbf5234f042f5a47a8a709b5c
  summary: >-
    This advanced Learning Path guides you through migrating an x86_64 Linux application to aarch64
    using a practical porting methodology. You will set up an aarch64 GCC development environment
    in a Docker container on a Linux host, analyze a Sobel filter workload implemented as non-SIMD
    C++, x86_64 intrinsics, and OpenCV, and iteratively port code to Arm, including translating
    intrinsics to Neon using SIMDe. You will build and run the application and evaluate console
    timing results and image outputs. Emulation, remote hardware, or physical Arm hardware can
    be used; physical hardware is not required. Prerequisites include introductory container knowledge,
    familiarity with build workflows, and access to an aarch64 or x86_64 Linux machine. The path
    also introduces using Arm compilers and libraries.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an introductory understanding of software containers, knowledge about building
      workflows, and access to a Linux machine on either aarch64 or x86_64. This is an advanced
      topic aimed at developers migrating Linux workloads.
  - question: Can I complete this Learning Path without physical Arm hardware?
    answer: >-
      Yes. Physical Arm hardware is not required; you can use emulation or remote hardware to
      run the aarch64 application.
  - question: Which compiler and environment should I use for the port?
    answer: >-
      The example uses GCC and recommends matching the original GCC version when possible. Set
      up an aarch64 GCC development container with Docker and run all build and test commands
      inside that container.
  - question: How should I handle x86 SIMD intrinsics during the port?
    answer: >-
      Use SIMD Everywhere (SIMDe) to port AVX intrinsics. This enables keeping a single source
      base while targeting aarch64.
  - question: What result should I expect when I run the ported application?
    answer: >-
      The program prints execution time measurements in microseconds for the non-SIMD, SIMD, and
      OpenCV implementations, and opens four image windows including the original and processed
      outputs. The example runs on CPU only (no hardware acceleration).
# END generated_summary_faq

author: Kasper Mecklenburg

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - GCC
    - Arm Compiler for Linux
    - Docker
    - Neon

further_reading:
    - resource:
        title: Porting architecture specific intrinsics
        link: /learning-paths/cross-platform/intrinsics/
        type: blog
    - resource:
        title: SIMD-everywhere repository
        link: https://github.com/simd-everywhere/simde
        type: website
    - resource:
        title: Migrating applications to Arm servers
        link: /learning-paths/servers-and-cloud-computing/migration
        type: blog
    - resource:
        title: Port Code to Arm Scalable Vector Extension (SVE)
        link: /learning-paths/servers-and-cloud-computing/sve/
        type: blog

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # Indicates this should be surfaced when looking for related content. Only set for _index.md of learning path content.
# ================================================================================

# Prereqs
---

