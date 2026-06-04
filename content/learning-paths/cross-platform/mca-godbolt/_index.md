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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:45:53Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c86322d497541344f92907315793ab990669aa08bef994b0ce9ff1e32a5ba055
  summary_generated_at: '2026-06-01T21:11:17Z'
  summary_source_hash: c86322d497541344f92907315793ab990669aa08bef994b0ce9ff1e32a5ba055
  faq_generated_at: '2026-06-02T21:45:53Z'
  faq_source_hash: c86322d497541344f92907315793ab990669aa08bef994b0ce9ff1e32a5ba055
  summary: >-
    This introductory Learning Path shows how to analyze Arm assembly performance with LLVM Machine
    Code Analyzer (llvm-mca) and Compiler Explorer. You will run llvm-mca on a small Arm assembly
    example that sums six values, interpret estimated cycles and hardware resource pressure, and
    use those metrics to diagnose a possible performance issue and improve the snippet. A brief
    background section introduces instruction scheduling and pipelines. The path is relevant to
    Arm cores such as Cortex-A and Neoverse, and notes that LLVM 16 or newer includes support
    for Neoverse V2. It can be followed on Linux, Windows, or macOS, and also via a browser using
    Compiler Explorer. Familiarity with Arm assembly is expected; no other explicit prerequisites
    are listed. Estimated time to complete is about 60 minutes.
  faqs:
  - question: Can I use llvm-mca without installing LLVM locally?
    answer: >-
      Yes. The path shows how to run llvm-mca in Compiler Explorer at godbolt.org, which provides
      llvm-mca as an online tool.
  - question: What do I need to run llvm-mca on my machine?
    answer: >-
      You need familiarity with Arm assembly and LLVM version 16 or newer. The path can be followed
      on Linux, Windows, or macOS.
  - question: What source code does the path analyze?
    answer: >-
      An Arm assembly snippet saved as sum_test1.s that computes the sum of six numbers using
      add instructions.
  - question: What output should I expect from llvm-mca, and how is it used?
    answer: >-
      Expect estimates of cycles and hardware resource pressure. The path explains the expected
      output and how to use these metrics to identify a potential performance issue in the example.
  - question: Which LLVM version includes support for Neoverse V2?
    answer: >-
      LLVM 16 or newer includes support for Neoverse V2, as noted in the prerequisites.
# END generated_summary_faq

author: Asher Dobrescu

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

