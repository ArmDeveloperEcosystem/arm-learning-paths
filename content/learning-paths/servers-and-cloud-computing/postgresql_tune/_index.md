---
title: Tune PostgreSQL performance on Arm-based platforms
description: Learn how to tune PostgreSQL configuration, Linux memory settings, and storage options to improve database performance on Arm-based platforms.

minutes_to_complete: 150

who_is_this_for: This Learning Path is for database administrators (DBAs) and software developers who want to optimize PostgreSQL performance on Arm-based platforms.

learning_objectives:
    - Configure PostgreSQL settings that affect connection handling, memory use, write-ahead logging, query planning, and concurrency.
    - Enable huge pages for PostgreSQL and size them for the shared memory area.
    - Evaluate storage, kernel, compiler, and library choices that can affect PostgreSQL performance.

prerequisites:
    - On-premises or cloud [installation of PostgreSQL](/learning-paths/servers-and-cloud-computing/postgresql/)
    - A repeatable PostgreSQL workload or benchmark that you can run before and after tuning

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-18T20:26:14Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1b0b89b63d7ba6c8b55708fa735e48bbdb0a1b706de1fb56f91d3f066f9f6d88
  summary_generated_at: '2026-11-18T20:26:14Z'
  summary_source_hash: 1b0b89b63d7ba6c8b55708fa735e48bbdb0a1b706de1fb56f91d3f066f9f6d88
  faq_generated_at: '2026-11-18T20:26:14Z'
  faq_source_hash: 1b0b89b63d7ba6c8b55708fa735e48bbdb0a1b706de1fb56f91d3f066f9f6d88
  summary: >-
    You'll evaluate PostgreSQL tuning choices on Arm-based Linux using repeatable measurements.
    First, you'll establish a baseline and review storage, kernel, compiler, and library
    considerations. Then, you'll examine PostgreSQL settings for memory, logging, planning, and
    concurrency. Finally, you'll test one change at a time with a representative workload or
    HammerDB, and compare the results before adopting a setting.
  faqs:
  - question: Which PostgreSQL configuration method should I use for persistent tuning changes in my environment?
    answer: >-
      Set parameters in `postgresql.conf` or with `ALTER SYSTEM`. For persistent tuning, use a
      method that you can review, version control, and apply consistently on restart. Reserve
      per-database, role, or session settings for scoped changes.
  - question: How should I design my measurements when I test a tuning change?
    answer: >-
      Treat tuning as a measurement process: change one parameter at a time, run a designed
      experiment, and compare profiles. You can also use automation or AI-assisted tools to
      explore a larger configuration space.
  - question: When should I use HammerDB TPROC-C versus my own workload?
    answer: >-
      Use HammerDB TPROC-C to compare your baseline with a tuned configuration under a
      repeatable workload. Also test with the SQL, data size, concurrency, and
      latency requirements of your application.
  - question: What should I check about my storage setup before I tune PostgreSQL parameters?
    answer: >-
      Compare the storage choices available to you before changing PostgreSQL parameters. Test
      their effects on throughput and latency with your workload.
  - question: How do I decide how many huge pages I need for PostgreSQL?
    answer: >-
      Size huge pages to cover the PostgreSQL shared memory area. Calculate the number you need
      from your shared memory configuration.
# END generated_summary_faq

author: Julio Suarez

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

test_images:
    - ubuntu:latest
test_maintenance: true

### Tags
skilllevels: Advanced
subjects: Databases
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - SQL
    - PostgreSQL
    - HammerDB
    - Runbook

further_reading:
    - resource:
        title: PostgreSQL documentation
        link: https://www.postgresql.org/docs/current/
        type: documentation
    - resource:
        title: PostgreSQL resource consumption settings
        link: https://www.postgresql.org/docs/current/runtime-config-resource.html
        type: documentation
    - resource:
        title: PostgreSQL write-ahead log settings
        link: https://www.postgresql.org/docs/current/runtime-config-wal.html
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
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
