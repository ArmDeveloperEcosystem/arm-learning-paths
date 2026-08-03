---
title: Memory latency for application software developers
description: Learn how to reduce memory latency impact in applications using cache alignment and prefetching techniques on Arm processors for improved performance.
minutes_to_complete: 40

who_is_this_for: This is an introductory topic for Arm developers who want to learn about memory latency and cache usage in application programming. 

learning_objectives: 
    - Explain the importance of memory latency and how to reduce its impact
    - Identify how cache alignment impacts performance
    - Use cache prefetching to improve performance

prerequisites:
    - An Arm computer running Linux with recent versions of Clang or GCC installed.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-29T16:42:44Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 72e5ffe5091311850d17f30ed3ab4bd7487cbbd862d0d8751cc73bd91fff00e2
  summary_generated_at: '2026-07-29T16:42:44Z'
  summary_source_hash: 72e5ffe5091311850d17f30ed3ab4bd7487cbbd862d0d8751cc73bd91fff00e2
  faq_generated_at: '2026-07-29T16:42:44Z'
  faq_source_hash: 72e5ffe5091311850d17f30ed3ab4bd7487cbbd862d0d8751cc73bd91fff00e2
  summary: >-
    You'll explore memory latency with a small C workload on Arm Linux. You'll modify the application in stages:
    add an allocator for locality, adjust structure layout and cache alignment, and add prefetching
    to bring data closer to the CPU. Then, you'll build and run each version. You'll compare relative runtime trends,
    choose an effective alignment, and tune the prefetch distance to overlap memory access with
    computation.
  faqs:
  - question: What should I check if my results differ from the sample output?
    answer: >-
      Differences are expected because processor and system details vary. Confirm that you built
      and ran the intended source file for each version, then compare relative changes rather than
      exact numbers.
  - question: How do I confirm the allocator changes in `memory-latency2.c` are being used?
    answer: >-
      Verify that the new allocator code is present and that you build `memory-latency2.c`. Run the
      program and confirm that it completes without the allocator error message from the source.
  - question: Which alignment or structure layout should I use for the node type?
    answer: >-
      Apply the changes shown in the steps, then test the provided alternatives and compare runtime
      behavior. Keep the version that performs better on your Arm system.
  - question: How far ahead should I prefetch in the loop?
    answer: >-
      Prefetch a few iterations ahead. Prefetching only the next iteration is often insufficient
      with typical RAM latency of about 100 ns. Adjust the distance empirically and keep the setting
      that improves runtime trends.
  - question: How do I know if cache alignment or prefetching helped?
    answer: >-
      Build each variant, run it under the same conditions, and compare runtimes or other observable
      behavior. A consistent improvement across multiple runs indicates that the change benefits
      your system.
# END generated_summary_faq

author: Konstantinos Margaritis

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - GCC
    - Clang
    - Runbook

operatingsystems:
    - Linux

shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - embedded-and-microcontrollers
    - mobile-graphics-and-gaming

further_reading:
    - resource:
        title: Write a Dynamic Memory Allocator
        link: /learning-paths/cross-platform/dynamic-memory-allocator/
        type: website
    - resource:
        title: Memory Latency
        link: https://en.algorithmica.org/hpc/cpu-cache/latency/
        type: website
    - resource:
        title: Latency Numbers Every Programmer Should Know
        link: https://gist.github.com/jboner/2841832?permalink_comment_id=4123064#gistcomment-4123064
        type: website
    - resource:
        title: Colin Scott's Interactive latencies page
        link: https://colin-scott.github.io/personal_website/research/interactive_latency.html
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
