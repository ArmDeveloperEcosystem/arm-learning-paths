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

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:49:12Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2fdb45e72a36eb114250486b88d603cc8687b9f6b44bb5bb656e25c37d9795a9
  summary_generated_at: '2026-06-02T04:47:41Z'
  summary_source_hash: 2fdb45e72a36eb114250486b88d603cc8687b9f6b44bb5bb656e25c37d9795a9
  faq_generated_at: '2026-06-03T01:49:12Z'
  faq_source_hash: 2fdb45e72a36eb114250486b88d603cc8687b9f6b44bb5bb656e25c37d9795a9
  summary: >-
    This advanced Learning Path teaches you how to control where your workloads run on many-core
    Arm-based Linux systems by setting CPU affinity for processes and threads. You will pin threads
    to specific cores using taskset and source-level changes in C++ and Python, create a single-threaded
    Python benchmark and C++ examples, and use perf (and Google Benchmark where applicable) to
    measure cache behavior and compare default scheduling with pinned execution. You will also
    evaluate throughput versus latency consistency and apply CPU affinity strategies for co-located
    workloads. The path runs on any Arm Linux system with four or more CPU cores; an example uses
    an AWS Graviton 3 m7g.4xlarge with Ubuntu 24.04 LTS, and you will check NUMA topology with
    lscpu. Prerequisites are explicitly listed.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Arm Linux system with four or more CPU cores. Experience with multi-threaded
      C++ and Python, build systems, computer architecture concepts, and familiarity with Linux
      command-line tools is expected.
  - question: Do I have to use the AWS Graviton3 instance mentioned in the setup?
    answer: >-
      No. The steps work on any Arm Linux system with four or more cores; the AWS Graviton3 m7g.4xlarge
      on Ubuntu 24.04 LTS (Neoverse V1) is provided as an example.
  - question: How do I check whether my system has a single NUMA node before choosing cores?
    answer: >-
      Run lscpu | grep -i numa. On the example m7g.4xlarge instance, all 16 cores are reported
      in the same NUMA node.
  - question: How do I validate that thread pinning changed behavior?
    answer: >-
      Compare runs before and after pinning using the provided benchmarks and use perf to measure
      cache performance differences. Use the results to assess throughput and latency consistency
      trade-offs.
  - question: When is thread pinning most useful in this Learning Path?
    answer: >-
      Pinning is presented as a fine-tuning technique for workloads that aim to consume as many
      CPU cycles as possible while co-located with other workloads. Use it when you want more
      consistent execution by constraining where threads run.
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

