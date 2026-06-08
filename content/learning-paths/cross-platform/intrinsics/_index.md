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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:42:32Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: ecf51d9a9085f95dedda9c0cfbfa4d6350d0f68d81b61f9461bc51070abd0b69
  summary_generated_at: '2026-06-01T21:08:20Z'
  summary_source_hash: ecf51d9a9085f95dedda9c0cfbfa4d6350d0f68d81b61f9461bc51070abd0b69
  faq_generated_at: '2026-06-02T21:42:32Z'
  faq_source_hash: ecf51d9a9085f95dedda9c0cfbfa4d6350d0f68d81b61f9461bc51070abd0b69
  summary: >-
    This advanced Learning Path shows how to migrate C/C++ code that relies on architecture-specific
    intrinsics from x64 to Arm. You will learn how to identify intrinsics in your source, understand
    how compilers expose them, and use header-only libraries to rebuild and run on Arm processors.
    The path demonstrates two approaches: mapping SSE intrinsics to Neon with sse2neon, and using
    SIMD Everywhere (SIMDe) for broader coverage, including AVX. It also introduces Porting Advisor
    for Graviton to locate intrinsics in large codebases. The target environment is Ubuntu Linux
    on an Arm-based machine or cloud instance; an x86_64 Ubuntu system is optional. By the end,
    you will have code that compiles and runs on Arm.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need some understanding of SIMD concepts and access to an Arm-based machine or cloud
      instance running Ubuntu Linux. Optionally, have an x86_64 Ubuntu machine available.
  - question: How do I find architecture-specific intrinsics in a large code base?
    answer: >-
      Use the background in this path to spot intrinsics in source and run Porting Advisor for
      Graviton to assess portability and locate intrinsics. Porting Advisor is a command line
      tool available on Linux, Windows, and macOS, and the example assumes you run it as an executable
      in your PATH.
  - question: 'Which option should I use to port x86 intrinsics: sse2neon or SIMDe?'
    answer: >-
      If your code uses MMX or SSE, you can use either sse2neon or SIMDe. If it contains AVX,
      use SIMDe.
  - question: What changes are required when porting with sse2neon?
    answer: >-
      Adjust SSE-specific header usage for the Arm build, include sse2neon.h to map intrinsics
      to Neon, and update your g++ compiler flags for the Arm architecture. This approach can
      get many C/C++ applications compiling and running on an appropriate Arm platform.
  - question: What are the high-level steps to use SIMD Everywhere (SIMDe)?
    answer: >-
      Select the correct SIMDe header using the SIMDEverywhere wiki table, define the required
      SIMDe configuration macro as shown in the steps, and build for Arm. SIMDe is a header-only
      library intended to make intrinsic-based code portable across architectures.
# END generated_summary_faq

author: Jason Andrews

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

