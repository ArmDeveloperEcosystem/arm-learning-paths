---
title: Optimize application performance with CPU affinity

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for developers, performance engineers, and system administrators looking to fine-tune the performance of their workload on many-core Arm-based systems.

learning_objectives: 
    - Pin threads to specific CPU cores using taskset and source code modifications.
    - Measure cache performance improvements from thread pinning using perf.
    - Evaluate performance trade-offs between throughput and latency consistency.
    - Implement CPU affinity strategies for co-located workloads.

prerequisites:
    - An Arm Linux system with four or more CPU cores
    - Experience with multi-threaded programming in C++ and Python
    - Understanding of build systems and computer architecture concepts
    - Familiarity with Linux command-line tools

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-18T20:24:03Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 380cac309a91373ac3e476167048a760f80d38a448c653f0540c117b5a887715
  summary_generated_at: '2026-11-18T20:24:03Z'
  summary_source_hash: 380cac309a91373ac3e476167048a760f80d38a448c653f0540c117b5a887715
  faq_generated_at: '2026-11-18T20:24:03Z'
  faq_source_hash: 380cac309a91373ac3e476167048a760f80d38a448c653f0540c117b5a887715
  summary: >-
    You'll control CPU placement for a workload on Arm-based Linux and measure the effects.
    First, you'll inspect CPU topology and build a CPU-intensive example. Then, you'll use `taskset`
    and source-level affinity to place processes and threads on selected cores. Finally, you'll
    compare pinned and unpinned runs, and use `perf` metrics to assess cache behavior and runtime
    stability.
  faqs:
  - question: How do I check whether my system uses a single NUMA node before pinning?
    answer: >-
      Run `lscpu | grep -i numa` and check the NUMA node count. 
  - question: Which cores should I choose when using taskset for the single-threaded benchmark?
    answer: >-
      On a uniform system, select an available core for your single-threaded test. For a
      multithreaded test, select the specific cores that you intend to dedicate to its threads.
  - question: How do I know that pinning with taskset actually changed behavior?
    answer: >-
      Compare unpinned and pinned runs for runtime stability and throughput. Use `perf` to
      collect cache metrics. Look for differences in cache references and misses between the
      two cases.
  - question: Where should I place source-level affinity calls?
    answer: >-
      Set affinity immediately after creating a thread or before it enters the hot path that
      does the critical work. Pin only the threads that you need to control. Leave the others managed
      by the scheduler.
  - question: What should I check if perf results don't show a clear difference after pinning?
    answer: >-
      Run enough iterations to reduce noise and ensure the system isn't under heavy background
      load. Verify that the chosen affinity mask targets cores that are online and available.
# END generated_summary_faq

author: Kieran Hejmadi

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
armips:
    - Neoverse
tools_software_languages:
    - CPP
    - Python
    - taskset
    - perf
    - Google Benchmark
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Taskset Manual  
        link: https://man7.org/linux/man-pages/man1/taskset.1.html
        type: documentation
    - resource:
        title: pthread_setaffinity_np Manual
        link: https://man7.org/linux/man-pages/man3/pthread_setaffinity_np.3.html
        type: documentation
    - resource:
        title: NUMA Deep Dive
        link: https://frankdenneman.nl/2016/07/07/numa-deep-dive-part-1-uma-numa/
        type: documentation
    - resource:
        title: Linux Scheduler Documentation
        link: https://www.kernel.org/doc/html/latest/scheduler/index.html
        type: documentation
    - resource:
        title: Get started with Arm-based cloud instances
        link: /learning-paths/servers-and-cloud-computing/csp/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

