---
title: "Migrate x86-64 SIMD to Arm64"

minutes_to_complete: 30

description: Learn how to migrate x86-64 SIMD code to Arm64 by mapping Intel SSE/AVX to Arm Neon, SVE, and SME, with code examples and migration strategies using autovectorization or intrinsics.

who_is_this_for: This is an advanced topic for developers migrating vectorized (SIMD) code from x86-64 to Arm64.

learning_objectives:
     - Identify how Arm vector extensions including Neon, Scalable Vector Extension (SVE), and Scalable Matrix Extension (SME) map to vector extensions from other architectures
     - Plan a migration strategy using autovectorization, intrinsics, or library substitution
   

prerequisites:
    - Familiarity with vector extensions, SIMD programming, and compiler intrinsics
    - Access to Linux systems with Neon and SVE support

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:54:01Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 26450ae17f7ed4242c52456c2780ffce5fad36b56dfc4a8482e8f236f855e134
  summary_generated_at: '2026-06-01T21:21:21Z'
  summary_source_hash: 26450ae17f7ed4242c52456c2780ffce5fad36b56dfc4a8482e8f236f855e134
  faq_generated_at: '2026-06-02T21:54:01Z'
  faq_source_hash: 26450ae17f7ed4242c52456c2780ffce5fad36b56dfc4a8482e8f236f855e134
  summary: >-
    This advanced Learning Path shows how to migrate x86-64 SIMD code to Arm64 by mapping Intel
    SSE/AVX/AMX to Arm Neon, SVE, and SME. You review migration strategies using autovectorization,
    intrinsics, or library substitution, then work through a SAXPY kernel implemented in plain
    C and with vector extensions on both Arm (Neon, SVE) and x86 (AVX2, AVX-512). On a Linux system
    with Neon and SVE support, you build and run each version using GCC or Clang and observe how
    vector width influences throughput. The expected outcome is an understanding of how Arm vector
    extensions relate to x86 equivalents and a practical plan for porting existing SIMD code.
    No additional prerequisites are listed beyond those stated; estimated duration is about 30
    minutes.
  faqs:
  - question: What do I need before running the examples?
    answer: >-
      You should be comfortable with SIMD programming and compiler intrinsics, and have access
      to Linux systems with Neon and SVE support. GCC or Clang are used to build the examples.
  - question: Which compiler should I use to build the code?
    answer: >-
      Use GCC or Clang as listed in the Learning Path tools. The steps show how to build and run
      the Arm and x86 variants of the SAXPY example.
  - question: How do I map x86 SIMD intrinsics to Arm equivalents?
    answer: >-
      The overview explains how SSE, AVX, and AMX map to Arm Neon, SVE, and SME. Use this mapping
      to guide intrinsics substitution or decide when autovectorization or libraries are more
      appropriate.
  - question: What result should I expect when I run the SAXPY variants?
    answer: >-
      You will build and run C, Neon, SVE, AVX2, and AVX-512 versions of a SAXPY kernel that computes
      y[i] = a * x[i] + y[i]. The run results let you compare SIMD behavior and see how vector
      width affects throughput.
  - question: When should I use a library instead of writing intrinsics?
    answer: >-
      If a tuned library provides the operation (for example, BLAS for SAXPY), prefer the library.
      The intrinsics-based examples are provided for learning and comparison.
# END generated_summary_faq

author:
    - Jason Andrews

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - GCC
    - Clang

shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - mobile-graphics-and-gaming
    - automotive

further_reading:
    - resource:
        title: SVE programming examples
        link: https://developer.arm.com/documentation/dai0548/latest
        type: documentation
    - resource:
        title: Port code to Arm Scalable Vector Extension (SVE)
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
        title: Build adaptive libraries with multiversioning
        link: /learning-paths/cross-platform/function-multiversioning/
        type: website
    - resource:
        title: SME Programmer's Guide
        link: https://developer.arm.com/documentation/109246/latest
        type: documentation
    - resource:
        title: Compiler intrinsics (overview)
        link: https://en.wikipedia.org/wiki/Intrinsic_function
        type: website
    - resource:
        title: ACLE - Arm C Language Extensions
        link: https://github.com/ARM-software/acle
        type: website
    - resource:
        title: Application Binary Interface for the Arm Architecture (AAPCS64)
        link: https://github.com/ARM-software/abi-aa
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

