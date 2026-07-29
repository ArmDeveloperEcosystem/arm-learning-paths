---
title: Porting architecture specific intrinsics

description: Learn how to port architecture-specific intrinsics to Arm processors.

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for software developers interested in porting
  architecture specific intrinsics to Arm processors.

learning_objectives:
- Describe what intrinsics are and how to find them in code.
- Evaluate options and use header-only libraries to port architecture-specific intrinsics
  to Arm.

prerequisites:
- Some understanding of SIMD concepts.
- An Arm based machine or [cloud instance](/learning-paths/servers-and-cloud-computing/csp/) running Ubuntu Linux.
- Optionally, an `x86_64` machine also running Ubuntu.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-29T16:37:37Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ecf51d9a9085f95dedda9c0cfbfa4d6350d0f68d81b61f9461bc51070abd0b69
  summary_generated_at: '2026-07-29T16:37:37Z'
  summary_source_hash: ecf51d9a9085f95dedda9c0cfbfa4d6350d0f68d81b61f9461bc51070abd0b69
  faq_generated_at: '2026-07-29T16:37:37Z'
  faq_source_hash: ecf51d9a9085f95dedda9c0cfbfa4d6350d0f68d81b61f9461bc51070abd0b69
  summary: >-
    Port x64 SIMD code to Arm by identifying architecture-specific intrinsics and mapping them to
    Arm equivalents. You use `sse2neon` for SSE or MMX code, or SIMD Everywhere (SIMDe) when a project
    also contains AVX. You adjust headers, add the required shim or macros, rebuild on Arm, and use
    Porting Advisor for Graviton to locate intrinsics in larger repositories.
  faqs:
  - question: How do I know if my code uses architecture-specific intrinsics?
    answer: >-
      Look for function-like calls from SIMD headers tied to a specific instruction set architecture
      (ISA), such as SSE, MMX, or AVX on x64. These compiler-provided functions are not standard
      library APIs.
  - question: Which option should I use if my codebase mixes SSE and AVX?
    answer: >-
      Use SIMD Everywhere (SIMDe). SIMDe supports SSE, MMX, and AVX, while `sse2neon` targets SSE
      and MMX.
  - question: What changes do I need when applying `sse2neon`?
    answer: >-
      Adjust the SSE-specific headers for Arm, include `sse2neon.h`, and update the compiler flags
      for the Arm target. Then rebuild on an Arm-based platform.
  - question: What do I configure when using SIMDe?
    answer: >-
      Select the SIMDe header that matches your intrinsics, define the macro shown in the project
      documentation, and rebuild. SIMDe then maps the intrinsics to portable Arm implementations.
  - question: How can I scan a large repository for intrinsics before compiling?
    answer: >-
      Use Porting Advisor for Graviton to assess portability and locate intrinsics across the
      codebase. Install and run the tool, then review its report before editing the sources.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

test_images:
- amd64/ubuntu:latest
- arm64v8/ubuntu:latest
test_maintenance: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
- Neoverse
- Cortex-A
operatingsystems:
- Linux
tools_software_languages:
  - Neon
  - SVE
  - Intrinsics
  - Runbook

further_reading:
    - resource:
        title: Port with SSE2Neon and SIMDe
        link: https://developer.arm.com/documentation/102581/0200/Port-with-SSE2Neon-and-SIMDe
        type: documentation
    - resource:
        title: Neon Programmer's Guide
        link: https://developer.arm.com/documentation/den0018
        type: documentation
    - resource:
        title: Porting SSE to Neon, Are libraries the way forward?
        link: https://community.arm.com/arm-community-blogs/b/ai-and-ml-blog/posts/porting-sse-to-neon-are-libraries-the-way-forward
        type: blog
    - resource:
        title: Porting Advisor for Graviton, AWS Online Tech Talks
        link: https://youtu.be/Ya9Co04fszI
        type: video

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
