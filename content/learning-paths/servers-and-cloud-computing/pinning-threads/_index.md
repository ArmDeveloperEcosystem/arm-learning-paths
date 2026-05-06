---
title: Optimize application performance with CPU affinity

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for developers, performance engineers, and system administrators looking to fine-tune the performance of their workload on many-core Arm-based systems.

learning_objectives: 
    - Pin threads to specific CPU cores using taskset and source code modifications
    - Measure cache performance improvements from thread pinning using perf
    - Evaluate performance trade-offs between throughput and latency consistency
    - Implement CPU affinity strategies for co-located workloads

prerequisites:
    - An Arm Linux system with four or more CPU cores
    - Experience with multi-threaded programming in C++ and Python
    - Understanding of build systems and computer architecture concepts
    - Familiarity with Linux command-line tools

generate_summary_faq: true

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:58Z'
  generator: template
  source_hash: 2fdb45e72a36eb114250486b88d603cc8687b9f6b44bb5bb656e25c37d9795a9
  summary: >-
    Optimize application performance with CPU affinity walks you through an end-to-end Arm software
    workflow. It is designed for developers, performance engineers, and system administrators
    looking to fine-tune the performance of their workload on many-core Arm-based systems. By
    the end, you will be able to pin threads to specific CPU cores using taskset and source code
    modifications, measure cache performance improvements from thread pinning using perf, and
    evaluate performance trade-offs between throughput and latency consistency. It focuses on
    tools and technologies such as C++, Python, taskset, perf, and Google Benchmark, Linux environments,
    Arm platforms including Neoverse, and cloud platforms such as AWS, Microsoft Azure, Google
    Cloud, and Oracle. The main steps cover Understand thread pinning and CPU affinity, Create
    a CPU-intensive program, Pin threads to cores with taskset, and Set CPU affinity in source
    code.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will pin threads to specific CPU cores using taskset and source code modifications,
      measure cache performance improvements from thread pinning using perf, and evaluate performance
      trade-offs between throughput and latency consistency.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for developers, performance engineers, and system administrators
      looking to fine-tune the performance of their workload on many-core Arm-based systems.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Arm Linux system with four or more
      CPU cores; Experience with multi-threaded programming in C++ and Python; Understanding of
      build systems and computer architecture concepts; Familiarity with Linux command-line tools.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including C++, Python, taskset, perf, and Google Benchmark,
      Linux environments, Arm platforms such as Neoverse, and cloud platforms such as AWS, Microsoft
      Azure, Google Cloud, and Oracle.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Understand thread pinning and CPU affinity, Create
      a CPU-intensive program, Pin threads to cores with taskset, and Set CPU affinity in source
      code.
# END generated_summary_faq

author: Kieran Hejmadi

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
tools_software_languages:
    - C++
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

