---
title: Characterize the memory subsystem of an Arm Linux system using ASCT

description: Use ASCT to measure cache latency, streaming bandwidth, and coherency latency on Arm Neoverse systems, and compare results across Graviton generations.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for software developers and performance engineers who want to understand and characterize the CPU-side memory subsystem of Arm Linux systems.

learning_objectives:
    - Identify the core topology, cluster layout, and cache hierarchy of an Arm Linux system using standard tools
    - Measure cache and memory latency using a pointer-chase benchmark
    - Measure single-core and multi-core streaming bandwidth at each level of the memory hierarchy
    - Evaluate latency behavior under bandwidth pressure 
    - Compare results across Arm systems and draw conclusions

prerequisites:
    - Two or more Arm Linux systems with root or sudo access. The examples use AWS Graviton2 and Graviton4 instances, but other systems are possible
    - Arm System Characterization Tool (ASCT) installed on each system
    - A good understanding of CPU memory subsystems, including cache hierarchies, cache lines, and DRAM in the memory hierarchy

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:28:09Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d61c9ddcef1c7ffe12b3ee818852fb3f0a62a90cec451692c1186cf2c01de625
  summary_generated_at: '2026-06-02T04:21:33Z'
  summary_source_hash: d61c9ddcef1c7ffe12b3ee818852fb3f0a62a90cec451692c1186cf2c01de625
  faq_generated_at: '2026-06-03T01:28:09Z'
  faq_source_hash: d61c9ddcef1c7ffe12b3ee818852fb3f0a62a90cec451692c1186cf2c01de625
  summary: >-
    This advanced Learning Path shows how to characterize the CPU-side memory subsystem on Arm
    Neoverse-based Linux systems using the Arm System Characterization Tool (ASCT). You will identify
    CPU topology, cache hierarchy, and NUMA layout, then measure cache and memory latency with
    a pointer-chase benchmark. You will also measure single-core and multi-core streaming bandwidth
    across L1, L2, last-level cache, and DRAM, evaluate latency under bandwidth pressure, and
    examine coherency latency. Examples use AWS Graviton2 and Graviton4, but any two or more Arm
    Linux systems with ASCT installed and root or sudo access can be used. By the end, you can
    compare results across Arm systems and draw practical conclusions.
  faqs:
  - question: What do I need before running these tests?
    answer: >-
      You need two or more Arm Linux systems with root or sudo access, and ASCT installed on each
      system. The examples use AWS Graviton2 and Graviton4, but other Arm systems are possible.
      A good understanding of cache hierarchies and DRAM is assumed.
  - question: How do I identify core, cache, and NUMA topology on my system?
    answer: >-
      Use standard Linux tools to determine the CPU topology, cache hierarchy, and NUMA configuration
      before testing. This context helps you interpret where cache-level transitions and bandwidth
      limits should appear in the results.
  - question: Which ASCT benchmarks should I run to measure latency and bandwidth?
    answer: >-
      Run the pointer-chase benchmark to measure dependent-load latency at each level of the memory
      hierarchy. Use the single-core bandwidth sweep to measure per-core streaming bandwidth,
      then run the multi-core peak-bandwidth and loaded-latency benchmarks to characterize scaling
      and contention.
  - question: How do I know the latency and bandwidth measurements are reasonable?
    answer: >-
      Expect step-like increases in latency as working sets exceed L1, then L2, then LLC and fall
      into DRAM, and look for bandwidth plateaus consistent with each level. Pointer chasing defeats
      hardware prefetching and out-of-order execution, so the latency curves should reflect true
      dependent-load behavior.
  - question: How should I compare results across systems like Graviton2 and Graviton4?
    answer: >-
      Run the same ASCT benchmarks under similar conditions on each system, then compare latency
      curves, bandwidth sweeps, and the points where scaling saturates. Use these comparisons
      to draw conclusions about cache hierarchy behavior and shared-resource limits across generations.
# END generated_summary_faq

author: Jason Andrews

skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - ASCT
    - Perf
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Inside Nvidia GB10's Memory Subsystem, from the CPU Side
        link: https://chipsandcheese.com/p/inside-nvidia-gb10s-memory-subsystem
        type: blog
    - resource:
        title: Memory latency for application software developers
        link: /learning-paths/cross-platform/memory-latency/
        type: website
    - resource:
        title: Arm Neoverse N1 Software Optimization Guide
        link: https://developer.arm.com/documentation/109896/latest/
        type: documentation
    - resource:
        title: Arm Neoverse V2 Software Optimization Guide
        link: https://developer.arm.com/documentation/109898/latest/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

