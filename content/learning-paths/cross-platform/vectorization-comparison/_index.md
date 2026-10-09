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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-29T16:52:20Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 26450ae17f7ed4242c52456c2780ffce5fad36b56dfc4a8482e8f236f855e134
  summary_generated_at: '2026-07-29T16:52:20Z'
  summary_source_hash: 26450ae17f7ed4242c52456c2780ffce5fad36b56dfc4a8482e8f236f855e134
  faq_generated_at: '2026-07-29T16:52:20Z'
  faq_source_hash: 26450ae17f7ed4242c52456c2780ffce5fad36b56dfc4a8482e8f236f855e134
  summary: >-
    You'll migrate vectorized code from x86-64 (SSE and AVX) to Arm by mapping features to Neon, SVE, and SME. You'll compare autovectorization,
    intrinsics, and library substitution. Then, you'll build a SAXPY kernel in plain C and with vector
    extensions on Arm and x86. You'll compare each result with a scalar reference and use vector width
    and throughput to choose an approach for your codebase.
  faqs:
  - question: 'Which migration approach should I pick: autovectorization, intrinsics, or a library?'
    answer: >-
      First check whether a tuned library provides the routine you need. If it does, prefer the
      library. Otherwise, try autovectorization first and use intrinsics when you need tighter control.
  - question: What result should I expect when I run the SAXPY variants?
    answer: >-
      Build and run the plain C and vectorized versions, then compare them across instruction sets.
      Their outputs match the scalar reference, and the measurements show how vector width affects
      throughput. Use those observations to inform your migration plan.
  - question: What should I do if my Arm hardware doesn't support SVE or SME?
    answer: >-
      Run the plain C and Neon versions supported by your hardware. SVE and SME sections need
      compatible systems, but the conceptual mapping still informs portability decisions.
  - question: Where do I find how SSE and AVX map to Neon, SVE, and SME?
    answer: >-
      The first section maps x86 SIMD extensions to Arm vector extensions. It highlights scalable
      vector length and matrix operations to guide code adaptation.
  - question: Can I use GCC or Clang to build the examples?
    answer: >-
      Yes. You can use either GCC or Clang to build the examples.
# END generated_summary_faq

author:
    - Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
