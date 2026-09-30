---
title: Optimize performance using Link-Time Optimization with GCC
description: Learn how to apply link-time optimization with the GCC toolchain to improve application performance by optimizing across compilation units.

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for developers who want to improve application performance using link-time optimization (LTO) with the GCC toolchain.

learning_objectives:
    - Understand how LTO works and when to apply it.
    - Enable and configure LTO with GCC compiler flags.
    - Evaluate the performance and code size trade-offs of LTO.

prerequisites:
    - An Arm Linux system (cloud instance, on-premises hardware, or a virtual machine)
    - A recent version of the [GCC toolchain](/install-guides/gcc/)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T22:02:58Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f1d6655e9ac403bcb0de9db2d620919fe977cb84fb70df3dd41c07dd6833c946
  summary_generated_at: '2026-09-10T22:02:58Z'
  summary_source_hash: f1d6655e9ac403bcb0de9db2d620919fe977cb84fb70df3dd41c07dd6833c946
  faq_generated_at: '2026-09-10T22:02:58Z'
  faq_source_hash: f1d6655e9ac403bcb0de9db2d620919fe977cb84fb70df3dd41c07dd6833c946
  summary: >-
    You'll explore LTO with GCC on Arm Linux systems. First, you'll enable LTO with the `-flto` flag during compilation and linking, then inspect how GCC performs whole-program optimization. You'll compare runtime and binary size before and after LTO, using SPEC CPU2017 integer rate as a reference.
  faqs:
  - question: Do I need to pass -flto at both compile and link time?
    answer: >-
      Yes. Compile each translation unit with `-flto` and also pass `-flto` to the final link so that GCC
      performs whole‑program optimization.
  - question: How do I build a small program with LTO in one command?
    answer: >-
      Use a single `gcc` invocation that includes your optimization level and `-flto`. This compiles
      and links with LTO enabled in one step.
  - question: What should I expect from the linker when LTO is enabled?
    answer: >-
      Object files contain LTO information in special sections. The final link performs whole‑program
      optimization before generating machine code.
  - question: How do I know LTO was applied to my build?
    answer: >-
      Confirm that all compile steps and the final link included `-flto`. If `-flto` is missing from
      any step, the link won't perform whole‑program optimization.
  - question: How should I evaluate the impact of LTO on my application?
    answer: >-
      Compare runtime and binary size before and after enabling `-flto`. Refer to the SPEC
      CPU2017 integer rate as an example framework to understand potential performance changes.
# END generated_summary_faq

author: Victor Do Nascimento

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
