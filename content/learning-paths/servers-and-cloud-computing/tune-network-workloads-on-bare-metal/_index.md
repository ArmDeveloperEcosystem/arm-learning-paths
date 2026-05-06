---
title: Tune network workloads on Arm-based bare-metal instances

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for engineers who want to tune the performance of network workloads on Arm Neoverse-based bare-metal instances.

learning_objectives: 
    - Set up Apache Tomcat and wrk2 to benchmark HTTP on an Arm Neoverse bare‑metal host
    - Establish a reproducible baseline baseline (file‑descriptor limits, logging, thread counts, fixed core set)
    - Tune NIC queue count to match available cores and measure impact
    - Improve NUMA locality by placing Tomcat on the NIC's NUMA node and aligning worker threads with cores
    - Compare IOMMU strict mode and IOMMU passthrough mode, and select the configuration that delivers the best performance for your workload

prerequisites:
    - An Arm Neoverse-based bare-metal server running Ubuntu 24.04 to run Apache Tomcat
    - Access to an x86_64 bare-metal server running Ubuntu 24.04 to run `wrk2`
    - Basic familiarity with Java applications

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:59Z'
  generator: template
  source_hash: 9f2b3f6c5e76ecb754de5c0fd84278ff71f71c5c7906acdc06911f2feff1f5fd
  summary: >-
    Tune network workloads on Arm-based bare-metal instances walks you through an end-to-end Arm
    software workflow. It is designed for engineers who want to tune the performance of network
    workloads on Arm Neoverse-based bare-metal instances. By the end, you will be able to set
    up Apache Tomcat and wrk2 to benchmark HTTP on an Arm Neoverse bare‑metal host, establish
    a reproducible baseline baseline (file‑descriptor limits, logging, thread counts, fixed core
    set), and tune NIC queue count to match available cores and measure impact. It focuses on
    tools and technologies such as Apache Tomcat, wrk2, and OpenJDK 21, Linux environments, and
    Arm platforms including Neoverse. The main steps cover Set up Tomcat, Establish baseline performance,
    Tune performance with NIC queue counts, NUMA-based tuning, and IOMMU-based tuning.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will set up Apache Tomcat and wrk2 to benchmark HTTP on an Arm Neoverse bare‑metal host,
      establish a reproducible baseline baseline (file‑descriptor limits, logging, thread counts,
      fixed core set), and tune NIC queue count to match available cores and measure impact.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for engineers who want to tune the performance of network workloads
      on Arm Neoverse-based bare-metal instances.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Arm Neoverse-based bare-metal server
      running Ubuntu 24.04 to run Apache Tomcat; Access to an x86_64 bare-metal server running
      Ubuntu 24.04 to run `wrk2`; Basic familiarity with Java applications.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Apache Tomcat, wrk2, and OpenJDK 21, Linux environments,
      and Arm platforms such as Neoverse.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Set up Tomcat, Establish baseline performance, Tune
      performance with NIC queue counts, NUMA-based tuning, and IOMMU-based tuning.
# END generated_summary_faq

author: Ying Yu, Ker Liu, Rui Chang

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
tools_software_languages:
    - Apache Tomcat
    - wrk2
    - OpenJDK 21
operatingsystems:
    - Linux

further_reading:
  - resource:
      title: OpenJDK Wiki 
      link: https://wiki.openjdk.org/
      type: documentation

  - resource:
      title: Apache Tomcat documentation
      link: https://tomcat.apache.org/tomcat-11.0-doc/index.html
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

