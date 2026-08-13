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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-12T20:11:15Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6740299c0690e346b3bb518b458e1e277c4c339e30954f10be722594e20dda29
  summary_generated_at: '2026-08-12T20:11:15Z'
  summary_source_hash: 6740299c0690e346b3bb518b458e1e277c4c339e30954f10be722594e20dda29
  faq_generated_at: '2026-08-12T20:11:15Z'
  faq_source_hash: 6740299c0690e346b3bb518b458e1e277c4c339e30954f10be722594e20dda29
  summary: >-
    You'll migrate an x86_64 Linux Sobel-filter application to aarch64 through a structured porting
    workflow. First, you'll create an aarch64 GCC container, adjust source and build options, replace x86_64
    intrinsics with SIMD Everywhere (SIMDe), and compile with CMake. Then, you'll run each implementation,
    compare execution times and images, and validate through emulation or remote Arm hardware.
  faqs:
  - question: Which development environment should I use to build for aarch64 on my x86_64 host?
    answer: >-
      Use an aarch64 GCC development container on your x86_64 machine. Aim to match the original
      GCC version when possible, and run the build steps inside that container.
  - question: Where do I get the example application and from which directory do I build?
    answer: >-
      Clone the [GitHub repository](https://github.com/m3y54m/sobel-simd-opencv.git) and change into
      that directory. Follow the provided CMake commands to configure src into a build directory
      and then build from there.
  - question: How should I port the x86_64 SIMD intrinsics in the project?
    answer: >-
      Use SIMDe to replace the AVX intrinsics so the code compiles for `aarch64`.
      Make source and build option changes iteratively until the project compiles in the aarch64
      container.
  - question: What result should I expect after I run the application?
    answer: >-
      The program prints execution times in microseconds for the non-SIMD, SIMD, and OpenCV implementations.
      It also opens four windows showing the original image and outputs from each implementation.
  - question: Do I need physical Arm hardware to follow this Learning Path?
    answer: >-
      No. You can run and validate the port using emulation or remote hardware. Physical Arm
      hardware isn't required.
# END generated_summary_faq

author: Kasper Mecklenburg

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
