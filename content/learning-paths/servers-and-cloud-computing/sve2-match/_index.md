---
title: Accelerate search performance with SVE2 MATCH on Arm servers
description: Implement and benchmark scalar and SVE2 MATCH multi-key searches on an Arm server to compare their performance.

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for database developers, performance engineers, and anyone optimizing data processing workloads on Arm-based cloud instances.

learning_objectives:
  - Understand the purpose and function of SVE2 MATCH instructions.
  - Implement a search algorithm using both scalar and SVE2-based MATCH approaches.
  - Benchmark and compare performance between scalar and vectorized implementations.
  - Analyze speedups and efficiency gains on Arm Neoverse-based instances with SVE2.

prerequisites:
- Access to an [AWS Graviton, Google Axion, or Azure Cobalt 100 virtual machine](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an Arm AGI CPU platform.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-12T18:24:16Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a1d9b96368e80c5e98b1fc56c1abfbdbd04a0ef6e3e49e04ecfe355602932741
  summary_generated_at: '2026-10-12T18:24:16Z'
  summary_source_hash: a1d9b96368e80c5e98b1fc56c1abfbdbd04a0ef6e3e49e04ecfe355602932741
  faq_generated_at: '2026-10-12T18:24:16Z'
  faq_source_hash: a1d9b96368e80c5e98b1fc56c1abfbdbd04a0ef6e3e49e04ecfe355602932741
  summary: >-
    You'll implement and benchmark scalar and SVE2 MATCH multi-key searches for 8-bit and 16-bit
    arrays on an Arm server. First, you'll learn how MATCH compares vector elements with search keys.
    Then, you'll write scalar, vectorized, and unrolled search functions. Finally, you'll add a benchmark harness,
    compile the program, and compare latency, throughput, and speedups at different hit rates.
#   faqs:
#   - question: What should I check before building and running the code?
#     answer: >-
#       You need an Arm-based instance with SVE2 support or an Arm AGI CPU platform running Ubuntu
#       24.04. You also need a GCC compiler with SVE support.
#   - question: Where do I add the scalar and SVE2 MATCH implementations?
#     answer: >-
#       You add the search functions to `sve2_match_demo.c`, then append the benchmark harness after
#       those functions.
#   - question: What does a successful search return?
#     answer: >-
#       You get `1` when any array element matches any key, and `0` otherwise.
#   - question: What result should I expect from the benchmark harness?
#     answer: >-
#       You compare latency, throughput, and speedups for the scalar, SVE2 MATCH, and unrolled SVE2
#       MATCH implementations.
#   - question: How do I change the benchmark’s hit rate?
#     answer: >-
#       You pass a hit probability as the third argument to `./sve2_match_demo`, after the array
#       length and iteration count.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
platforms:
  - Arm AGI CPU
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
armips:
- Neoverse
operatingsystems:
- Linux
tools_software_languages:
- SVE2
- Neon
- Runbook

further_reading:
    - resource:
        title: Accelerate multi-token search in strings with SVE2 SVMATCH instruction
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/multi-token-search-strings-svmatch-instruction
        type: blog
    - resource:
        title: Arm SVE2 Programming Guide
        link: https://developer.arm.com/documentation/102340/latest/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

