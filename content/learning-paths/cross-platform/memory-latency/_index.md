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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:47:00Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 72e5ffe5091311850d17f30ed3ab4bd7487cbbd862d0d8751cc73bd91fff00e2
  summary_generated_at: '2026-06-01T21:12:22Z'
  summary_source_hash: 72e5ffe5091311850d17f30ed3ab4bd7487cbbd862d0d8751cc73bd91fff00e2
  faq_generated_at: '2026-06-02T21:47:00Z'
  faq_source_hash: 72e5ffe5091311850d17f30ed3ab4bd7487cbbd862d0d8751cc73bd91fff00e2
  summary: >-
    Learn practical ways to reduce the impact of memory latency on Arm processors by experimenting
    with cache alignment and prefetching in C. You will build and run an example, then create
    a second version by copying memory-latency1.c to memory-latency2.c, introducing an allocator,
    adjusting data structure alignment, and adding prefetching to observe effects on execution.
    The path targets Linux on Arm systems, including Cortex-A and Neoverse, and uses GCC or Clang.
    Results will vary by processor and system, which is expected and part of the learning. Prerequisite:
    an Arm computer running Linux with a recent GCC or Clang. Estimated time to complete: about
    40 minutes.
  faqs:
  - question: What do I need before running the examples?
    answer: >-
      You need an Arm computer running Linux with recent versions of Clang or GCC installed. No
      other prerequisites are explicitly listed.
  - question: What should I expect after copying memory-latency1.c to memory-latency2.c?
    answer: >-
      You will have a modified C program that introduces a simple allocator and related bookkeeping.
      Use it to compare behavior against the original and observe how allocation affects latency.
  - question: How do I know whether the cache alignment change had an effect?
    answer: >-
      Rebuild and run the updated program and compare results with the previous version. Focus
      on relative differences on your system rather than exact numbers.
  - question: How far ahead should I prefetch in the loop?
    answer: >-
      Prefetch a few iterations ahead; prefetching only the next iteration is not sufficient.
      The path notes typical RAM latency around 100 ns, so bring data closer earlier.
  - question: What should I check if my results differ from the sample output?
    answer: >-
      This is expected because results depend on the processor and system you use. Focus on the
      trend between versions, and note that the learning applies to any Arm processor.
# END generated_summary_faq

author: Konstantinos Margaritis

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

