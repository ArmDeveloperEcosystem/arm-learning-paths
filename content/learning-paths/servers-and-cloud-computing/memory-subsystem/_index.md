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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-28T19:48:12Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6b479ae20842937f567651daaebe2327df73672b647382cef72d05a769e9d713
  summary_generated_at: '2026-09-28T19:48:12Z'
  summary_source_hash: 6b479ae20842937f567651daaebe2327df73672b647382cef72d05a769e9d713
  faq_generated_at: '2026-09-28T19:48:12Z'
  faq_source_hash: 6b479ae20842937f567651daaebe2327df73672b647382cef72d05a769e9d713
  summary: >-
    Characterize an Arm Linux server’s memory subsystem with the Arm System Characterization Tool
    (ASCT). You identify the CPU, cache, and Non-Uniform Memory Access (NUMA) topology, then measure
    cache and DRAM latency with pointer chasing. You profile single-core bandwidth across working
    sets and test multi-core scaling, saturation, and loaded latency. Finally, you compare systems
    to recognize latency plateaus, bandwidth limits, and shared-resource effects.
  faqs:
  - question: Which ASCT benchmarks should I run to cover latency and bandwidth?
    answer: >-
      Use `pointer-chase` for cache and memory latency. Run the single-core bandwidth sweep for
      per-core throughput, then use `peak-bandwidth` and `loaded-latency` to assess multi-core
      scaling and latency under bandwidth pressure.
  - question: What should I verify about the system topology before running benchmarks?
    answer: >-
      Confirm the core count, cluster layout, private and shared cache levels, and Non-Uniform Memory
      Access (NUMA) configuration. Use this baseline to interpret performance cliffs and bandwidth
      scaling.
  - question: What result should I expect from the pointer-chase latency test?
    answer: >-
      Look for stepwise latency increases as the working set exceeds L1, L2, any shared cache,
      and finally DRAM. Use the plateaus and jumps to estimate the effective latency of each level.
  - question: How should I compare results across Arm systems, such as different Graviton generations?
    answer: >-
      Run the same ASCT benchmarks with consistent settings and similar conditions on each system.
      Compare latency plateaus, bandwidth peaks, and multi-core scaling while accounting for differences
      in core topology and cache hierarchy.
  - question: What should I check if multi-core bandwidth does not increase as more cores are
      used?
    answer: >-
      Check whether the last-level cache, interconnect, or memory controllers have saturated. Verify
      that your benchmark uses the intended cores and NUMA nodes, review the topology, and examine
      `loaded-latency` for contention effects.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
