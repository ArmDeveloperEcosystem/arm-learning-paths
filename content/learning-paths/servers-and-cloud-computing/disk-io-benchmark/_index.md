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

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:39:53Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a1ec216948e7cfd4fc52815196bb3b99ab4e76c9c756aa9e9a8e3216ef5e7ce4
  summary_generated_at: '2026-06-02T03:32:18Z'
  summary_source_hash: a1ec216948e7cfd4fc52815196bb3b99ab4e76c9c756aa9e9a8e3216ef5e7ce4
  faq_generated_at: '2026-06-03T00:39:53Z'
  faq_source_hash: a1ec216948e7cfd4fc52815196bb3b99ab4e76c9c756aa9e9a8e3216ef5e7ce4
  summary: >-
    This introductory Learning Path shows how to monitor and microbenchmark storage on Arm-based
    Linux systems. You will review storage fundamentals and key workload attributes (IOPS, I/O
    size, throughput, read/write ratio, and access patterns), analyze a real workload using FFMPEG
    on an AWS t4g.medium (Graviton2) instance, and then install and run fio to benchmark SSD-based
    block devices. The steps use iostat, iotop, and pidstat to observe I/O behavior and identify
    bottlenecks. An example demonstrates attaching and identifying two AWS EBS volumes (io2 and
    gp2) before testing. Prerequisites are an Arm-based cloud instance or Arm Linux server and
    familiarity with Linux. Expected outcomes include describing data flow, monitoring storage
    activity, and running fio microbenchmarks.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Arm-based instance from a cloud service provider or an Arm Linux server, and
      familiarity with Linux. No other explicit prerequisites are listed.
  - question: Can I use a cloud provider other than AWS?
    answer: >-
      Yes. The prerequisite allows any Arm-based instance from a cloud service provider, but the
      example steps use AWS. Setup details for other providers are not explicitly listed.
  - question: Which instance type and example workload are used in the path?
    answer: >-
      The example uses an AWS t4g.medium (Graviton2) instance with two vCPUs and 4 GiB of memory.
      FFMPEG is used as a real workload to analyze I/O behavior.
  - question: Which block storage devices are benchmarked and how are they created?
    answer: >-
      Two SSD-based EBS volumes are used: an io2 volume (8 GiB, 400 provisioned IOPS, same Availability
      Zone as the instance) and a gp2 volume. They are created in the AWS Console and added to
      the EC2 instance before identifying them on the system.
  - question: How should I monitor and validate storage behavior while running fio?
    answer: >-
      Use iostat, iotop, and pidstat to observe activity and relate results to workload attributes
      such as IOPS, I/O size, throughput, read/write ratio, and random vs. sequential access.
      If results look incorrect or devices are missing, verify the volumes are in the same Availability
      Zone as the instance and properly attached.
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

