---
title: Learn how to Tune PostgreSQL

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for software developers and DevOps professionals interested in optimizing PostgreSQL performance.

learning_objectives:
    - Tune PostgreSQL to increase performance

prerequisites:
    - Bare-metal or cloud [installation of PostgreSQL](/learning-paths/servers-and-cloud-computing/postgresql/)

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:52:41Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f30f7fb50000ae7ee28e46d7cbe4e73ba232c3daad2d559cfa41996d630cb936
  summary_generated_at: '2026-06-02T04:49:21Z'
  summary_source_hash: f30f7fb50000ae7ee28e46d7cbe4e73ba232c3daad2d559cfa41996d630cb936
  faq_generated_at: '2026-06-03T01:52:41Z'
  faq_source_hash: f30f7fb50000ae7ee28e46d7cbe4e73ba232c3daad2d559cfa41996d630cb936
  summary: >-
    This advanced Learning Path guides developers and DevOps engineers through tuning PostgreSQL
    on Linux, with relevance to Arm Neoverse-based servers and common cloud providers. You will
    review system considerations such as storage technology and file system selection (with xfs
    as a good starting point), apply PostgreSQL configuration changes via configuration files
    (including connection and prepared transaction settings), and measure their impact using HammerDB
    TPROC-C. The content emphasizes that tuning is workload-specific and should be validated with
    testing. A bare-metal or cloud installation of PostgreSQL is required, and you need a machine
    or cloud node with PostgreSQL installed and configured for the test steps. Estimated time
    to complete is about 30 minutes.
  faqs:
  - question: What do I need before running the tuning and tests?
    answer: >-
      You need a physical machine or a cloud node with PostgreSQL installed and configured. The
      prerequisite is a bare-metal or cloud installation of PostgreSQL.
  - question: How should I apply the provided PostgreSQL configuration parameters?
    answer: >-
      The parameters shown can be pasted directly into a PostgreSQL configuration file. The path
      references the Setting Parameters documentation for ways to set these values.
  - question: Which storage and file system options should I start with?
    answer: >-
      Storage technology and file system format can significantly impact performance. In general,
      locally attached SSDs perform best, but network-based storage can also perform well; xfs
      is a good start. You should study and experiment with options for your workload.
  - question: Do I need to use HammerDB if I already have a performance test?
    answer: >-
      No. Skip the HammerDB section if you already have a performance test methodology; otherwise,
      the path demonstrates testing with HammerDB TPROC-C.
  - question: Should I increase max_connections or max_prepared_transactions?
    answer: >-
      Increase these only if your use case requires high client connection counts or prepared
      transactions. The path notes that max_connections does not directly impact query performance
      but helps avoid rejecting client requests; test any changes.
# END generated_summary_faq

author: Julio Suarez

test_images:
    - ubuntu:latest
test_maintenance: true

### Tags
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
    - PostgreSQL
    - HammerDB
    - Runbook


further_reading:
    - resource:
        title: PostgreSQL documentation
        link: https://www.postgresql.org/
        type: documentation
    - resource:
        title: "PostgreSQL on ARM: default page size matters"
        link: https://dev.to/aws-heroes/postgresql-on-arm-default-page-size-matters-2n7a
        type: blog


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

