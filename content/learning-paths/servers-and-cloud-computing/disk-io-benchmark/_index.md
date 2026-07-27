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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-27T18:49:30Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a1ec216948e7cfd4fc52815196bb3b99ab4e76c9c756aa9e9a8e3216ef5e7ce4
  summary_generated_at: '2026-07-27T18:49:30Z'
  summary_source_hash: a1ec216948e7cfd4fc52815196bb3b99ab4e76c9c756aa9e9a8e3216ef5e7ce4
  faq_generated_at: '2026-07-27T18:49:30Z'
  faq_source_hash: a1ec216948e7cfd4fc52815196bb3b99ab4e76c9c756aa9e9a8e3216ef5e7ce4
  summary: >-
    You'll characterize storage on an Arm-based Linux system by analyzing a real workload and running
    comparable `fio` profiles. You'll identify I/O size, read/write mix, access pattern, target IOPS,
    and throughput, then attach SSD-backed devices and monitor them with `iostat`, `iotop`, and
    `pidstat`. By the end, you'll compare device behavior and interpret `fio` results alongside system
    metrics.
  faqs:
  - question: How do I know the additional volumes are attached correctly before running `fio`?
    answer: >-
      After attaching the volumes in the cloud console, the instance should expose two new block
      devices. Verify that the expected device identifiers are available so you can target them
      in tests.
  - question: Which `fio` job parameters should I choose to reflect my workload?
    answer: >-
      Base your job on the attributes you observed from the real workload: I/O size, read/write
      ratio, sequential versus random access, target IOPS, and throughput. Keep the profile consistent
      when comparing devices.
  - question: What should I look for in `fio` output to compare devices?
    answer: >-
      Focus on reported IOPS and throughput for the selected job profile. Compare those values
      across runs to see how each block device behaves under the same conditions.
  - question: When should I run `iostat`, `iotop`, and `pidstat` during this process?
    answer: >-
      Run them while the workload and `fio` jobs are active to observe device utilization and per-process
      activity. Use these observations to spot contention and guide the next test configuration.
  - question: Do I need to use the exact instance type shown in the example?
    answer: >-
      The example uses an Arm-based cloud instance to illustrate the workflow. You can follow
      the same steps on an Arm Linux server or another Arm-based instance.
# END generated_summary_faq

author: Kieran Hejmadi

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
