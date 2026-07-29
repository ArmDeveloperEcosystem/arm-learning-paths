---
title: Learn about LLVM Machine Code Analyzer
description: Learn how to use llvm-mca with Compiler Explorer to analyze Arm assembly performance, estimate hardware resource pressure, and diagnose performance issues.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers who want to diagnose performance issues of Arm programs using LLVM Machine Code Analyzer (MCA) and Compiler Explorer.

learning_objectives:
    - Estimate the hardware resource pressure and the number of cycles taken to execute your code snippet using llvm-mca.
    - Describe how this estimate can help diagnose possible performance issues.
    - Use Compiler Explorer to run llvm-mca.

prerequisites:
    - Familiarity with Arm assembly.
    - LLVM version 16 or newer, which includes support for Neoverse V2.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-29T16:40:47Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c86322d497541344f92907315793ab990669aa08bef994b0ce9ff1e32a5ba055
  summary_generated_at: '2026-07-29T16:40:47Z'
  summary_source_hash: c86322d497541344f92907315793ab990669aa08bef994b0ce9ff1e32a5ba055
  faq_generated_at: '2026-07-29T16:40:47Z'
  faq_source_hash: c86322d497541344f92907315793ab990669aa08bef994b0ce9ff1e32a5ba055
  summary: >-
    Use LLVM Machine Code Analyzer (`llvm-mca`) to reason about Arm assembly performance. You analyze
    a short six-value sum to estimate cycles and resource pressure, identify bottlenecks, and relate
    the report to pipeline behavior. You also run `llvm-mca` in Compiler Explorer to compare compiler
    versions and apply the workflow to other Arm assembly fragments.
  faqs:
  - question: What result should I expect when I run `llvm-mca` on the `sum_test1.s` example?
    answer: >-
      `llvm-mca` prints estimated cycles and hardware resource pressure for the add instructions.
      Use those metrics to identify possible stalls and the most stressed resources.
  - question: How do I run `llvm-mca` inside Compiler Explorer?
    answer: >-
      Open [Compiler Explorer](https://godbolt.org), then select the `llvm-mca` tool integration to
      analyze your code. You can choose compilers and tools without installing them locally.
  - question: How do I know `llvm-mca` executed correctly on my snippet?
    answer: >-
      The report includes an estimated cycle count and a resource-usage breakdown without errors.
      If it is missing or incomplete, verify that the input matches the example and rerun the analysis.
  - question: What should I check before analyzing the Arm assembly example?
    answer: >-
      Save the provided instructions exactly as shown in `sum_test1.s`. Make sure the registers
      match the example so the analysis reflects the intended sequence.
  - question: Can I follow this path without installing LLVM locally?
    answer: >-
      Yes. Compiler Explorer includes `llvm-mca` and lets you try compiler versions in the browser.
      For Neoverse V2 support, use LLVM 16 or newer.
# END generated_summary_faq

author: Asher Dobrescu

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - Assembly
    - llvm-mca
    - Runbook

operatingsystems:
    - Linux
    - Windows
    - macOS

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - mobile-graphics-and-gaming

further_reading:
    - resource:
        title: Arm Neoverse V2 Software Optimization Guide
        link: https://developer.arm.com/documentation/109898/0300/?lang=en
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
