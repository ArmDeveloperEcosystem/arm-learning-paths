---
title: Optimize performance using Link-Time Optimization with GCC
description: Learn how to apply link-time optimization with the GCC toolchain to improve application performance by optimizing across compilation units.

    
minutes_to_complete: 15

who_is_this_for: This is an introductory topic for developers who want to improve application performance using link-time optimization (LTO) with the GCC toolchain.

learning_objectives:
    - Understand how link-time optimization (LTO) works and when to apply it
    - Enable and configure LTO with GCC compiler flags
    - Evaluate the performance and code size trade-offs of LTO

prerequisites:
    - An Arm Linux system (cloud instance, on-premises hardware, or a virtual machine)
    - A recent version of the [GCC toolchain](/install-guides/gcc/)

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:59:35Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2e53b87d4dc7a7d1984e3bbe035038a60e619aea2f5793cb3082f3b59084bbf9
  summary_generated_at: '2026-06-02T03:57:53Z'
  summary_source_hash: 2e53b87d4dc7a7d1984e3bbe035038a60e619aea2f5793cb3082f3b59084bbf9
  faq_generated_at: '2026-06-03T00:59:35Z'
  faq_source_hash: 2e53b87d4dc7a7d1984e3bbe035038a60e619aea2f5793cb3082f3b59084bbf9
  summary: >-
    This introductory Learning Path shows how to enable and use GCC link-time optimization (LTO)
    on an Arm Linux system to improve application performance by optimizing across compilation
    units. You will learn how LTO works, when to apply it, and how to build with -flto during
    both compilation and linking. The steps cover deploying LTO with GCC on Linux and evaluating
    performance and code size trade-offs, with context on standardized benchmarks that illustrate
    potential gains. Prerequisites are an Arm Linux environment (cloud, on-premises, or VM) and
    a recent GCC toolchain. After completing the path, you will be able to configure LTO in your
    builds and compare results against non-LTO builds.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Arm Linux system (cloud instance, on‑premises hardware, or a virtual machine)
      and a recent version of the GCC toolchain. No other prerequisites are explicitly listed.
  - question: Which GCC flags do I use to enable LTO?
    answer: >-
      Pass -flto during both compilation and linking. The examples also use -O2 alongside -flto.
  - question: Do I need to compile every translation unit with -flto?
    answer: >-
      Yes. In a stepwise build, compile each translation unit with -flto so the object files embed
      LTO information, and then link with -flto to trigger whole‑program optimization.
  - question: Can I build a small program with a single gcc command?
    answer: >-
      Yes. For small programs, the path notes you can simplify the build into a single gcc invocation
      that both compiles and links with -flto.
  - question: How should I evaluate the impact of LTO on my workload?
    answer: >-
      The path discusses evaluating performance and code size trade‑offs and references SPEC CPU2017
      integer rate as a standardized way to illustrate potential gains. Actual results will depend
      on your application.
# END generated_summary_faq

author: Victor Do Nascimento

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Neoverse
    - Cortex-A
tools_software_languages:
    - GCC
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: GCC Wiki Link-Time Optimization
        link: https://gcc.gnu.org/wiki/LinkTimeOptimization
        type: website
    - resource:
        title: Gentoo Wiki LTO
        link: https://wiki.gentoo.org/wiki/LTO
        type: website
    - resource:
        title: SPEC CPU 2017 Benchmark Suite
        link: https://www.spec.org/cpu2017/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

