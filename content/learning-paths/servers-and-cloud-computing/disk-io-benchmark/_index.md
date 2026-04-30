---
title: Microbenchmark storage performance with fio on Arm
description: Learn how to use fio to microbenchmark storage performance on Arm systems and monitor storage using iostat, iotop, and pidstat to identify bottlenecks.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers looking to optimize storage performance, reduce costs, identify bottlenecks, and evaluate storage options when migrating applications across platforms.

learning_objectives: 
    - Describe data flow through storage devices.
    - Monitor storage performance using tools like iostat, iotop, and pidstat.
    - Run fio to microbenchmark a block storage device.

prerequisites:
    - An [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an Arm Linux server.
    - Familiarity with Linux.

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:18Z'
  generator: template
  source_hash: a1ec216948e7cfd4fc52815196bb3b99ab4e76c9c756aa9e9a8e3216ef5e7ce4
  summary: >-
    Learn how to use fio to microbenchmark storage performance on Arm systems and monitor storage
    using iostat, iotop, and pidstat to identify bottlenecks. It is designed for developers looking
    to optimize storage performance, reduce costs, identify bottlenecks, and evaluate storage
    options when migrating applications across platforms. By the end, you will be able to describe
    data flow through storage devices, monitor storage performance using tools like iostat, iotop,
    and pidstat, and run fio to microbenchmark a block storage device. It focuses on tools and
    technologies such as bash and Runbook, Linux environments, Arm platforms including Neoverse,
    and cloud platforms such as AWS, Microsoft Azure, Google Cloud, and Oracle. The main steps
    cover Fundamentals of storage systems, Analyzing I/O behavior with real workloads, and Benchmarking
    block storage performance with fio.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will describe data flow through storage devices, monitor storage performance using tools
      like iostat, iotop, and pidstat, and run fio to microbenchmark a block storage device. Learn
      how to use fio to microbenchmark storage performance on Arm systems and monitor storage
      using iostat, iotop, and pidstat to identify bottlenecks.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers looking to optimize storage performance, reduce
      costs, identify bottlenecks, and evaluate storage options when migrating applications across
      platforms.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An [Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/)
      from a cloud service provider or an Arm Linux server.; Familiarity with Linux.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including bash and Runbook, Linux environments, Arm platforms
      such as Neoverse, and cloud platforms such as AWS, Microsoft Azure, Google Cloud, and Oracle.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Fundamentals of storage systems, Analyzing I/O behavior
      with real workloads, and Benchmarking block storage performance with fio.
# END generated_summary_faq

author: Kieran Hejmadi

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
tools_software_languages:
    - bash
    - Runbook
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Fio documentation
        link: https://fio.readthedocs.io/en/latest/fio_doc.html#running-fio
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

