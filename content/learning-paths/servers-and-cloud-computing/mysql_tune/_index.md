---
title: Tune MySQL performance on Arm-based platforms
description: Learn how to tune MySQL configuration, Linux memory settings, and storage options to improve database performance on Arm-based platforms.

minutes_to_complete: 30

who_is_this_for: This Learning Path is for database administrators (DBAs) and software developers who want to optimize MySQL performance on Arm-based platforms.

learning_objectives:
    - Configure MySQL settings that affect connection handling, memory usage, disk flush behavior, and concurrency.
    - Enable huge pages for MySQL and size them based on the InnoDB buffer pool.
    - Evaluate storage, kernel, compiler, and library choices that can affect MySQL performance.

prerequisites:
    - On-prem or cloud [installation of MySQL](https://dev.mysql.com/doc/refman/en/)
    - A repeatable MySQL workload or benchmark that you can run before and after tuning

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-26T21:28:59Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 19acf30951401ec15201ee8e387eb59f9248f627664bc693cf05928233bf2b6f
  summary_generated_at: '2026-06-26T21:28:59Z'
  summary_source_hash: 19acf30951401ec15201ee8e387eb59f9248f627664bc693cf05928233bf2b6f
  faq_generated_at: '2026-06-26T21:28:59Z'
  faq_source_hash: 19acf30951401ec15201ee8e387eb59f9248f627664bc693cf05928233bf2b6f
  summary: >-
    You'll learn how to use a measurement-driven approach to tune MySQL performance on Arm-based platforms.
    You'll explore system factors — storage technology and file systems,
    disk scheduling, kernel memory management, compiler, and library versions — that you can adjust. In addition, you'll learn about optimizable MySQL parameters related to connection
    handling, memory usage, disk flush behavior, and concurrency, and learn how to enable and
    size huge pages based on the InnoDB buffer pool. By the end, you'll know what parameters to update for running controlled experiments,
    and be able to make persistent configuration choices aligned with your workload.
  faqs:
  - question: How do I know a MySQL tuning change actually helped?
    answer: >-
      Run the same repeatable workload before and after the change and compare throughput, latency,
      and profiles. Change one parameter at a time or use a designed experiment so results are
      attributable to specific settings.
  - question: Should I set MySQL parameters in an option file or on the `mysqld` command line?
    answer: >-
      Use an option file for persistent tuning so changes are reviewable, version controlled,
      and applied on restart. The examples in the Learning Path target the `[mysqld]` group. Command-line flags are suitable
      for temporary tests.
  - question: Which storage option should I use when testing performance?
    answer: >-
      In general, locally attached SSD storage performs best, but network-based storage can also
      perform well. Test the storage technologies and file systems you have, and review disk scheduling
      behavior with your workload.
  - question: When should I look at kernel, compiler, or library choices instead of MySQL settings?
    answer: >-
      Evaluate them before or alongside MySQL tuning because operating system settings, kernel
      memory management, compiler choices, and library versions can affect throughput and latency.
      Treat them as part of the same performance experiment set.
  - question: How should I size huge pages for MySQL?
    answer: >-
      Enable huge pages for MySQL and size them based on the InnoDB buffer pool. This aligns page
      allocation with the primary memory consumer in typical MySQL deployments.
# END generated_summary_faq

author: Julio Suarez

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

skilllevels: Advanced
subjects: Databases
cloud_service_providers:
    - AWS
    - Microsoft Azure
    - Google Cloud
    - Oracle
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - SQL
    - MySQL
    - InnoDB
    - Runbook

test_images:
    - ubuntu:latest
test_link: null
test_maintenance: true

further_reading:
    - resource:
        title: MySQL Reference Manual
        link: https://dev.mysql.com/doc/refman/en/
        type: documentation
    - resource:
        title: InnoDB configuration parameters
        link: https://dev.mysql.com/doc/refman/en/innodb-parameters.html
        type: documentation
    - resource:
        title: Optimizing InnoDB disk I/O
        link: https://dev.mysql.com/doc/refman/en/optimizing-innodb-diskio.html
        type: documentation
    - resource:
        title: Linux HugeTLBpage documentation
        link: https://docs.kernel.org/admin-guide/mm/hugetlbpage.html
        type: documentation
    - resource:
        title: Migrating applications to Arm servers
        link: /learning-paths/servers-and-cloud-computing/migration/
        type: learning-path

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: learningpathall
learning_path_main_page: 'yes'
---
