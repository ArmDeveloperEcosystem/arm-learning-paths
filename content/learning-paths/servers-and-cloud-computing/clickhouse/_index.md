---
title: Measure performance of ClickHouse on Arm servers
description: Learn how to install ClickHouse on Arm-based cloud instances and measure database performance using ClickBench to determine appropriate instance configurations.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for software developers who want to use ClickHouse on Arm-based cloud instances.

learning_objectives:
    - Learn how to install and measure ClickHouse performance
    - Determine the appropriate instance configuration needed for your workloads

prerequisites:
    - An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider or an on-premise Arm server.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-30T21:47:22Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 0d1390198cf2f0e87f509c5269fc2405cffcb2e57311024150d47e60a3273178
  summary_generated_at: '2026-06-30T21:47:22Z'
  summary_source_hash: 0d1390198cf2f0e87f509c5269fc2405cffcb2e57311024150d47e60a3273178
  faq_generated_at: '2026-06-30T21:47:22Z'
  faq_source_hash: 0d1390198cf2f0e87f509c5269fc2405cffcb2e57311024150d47e60a3273178
  summary: >-
    You'll install ClickHouse on an Arm-based cloud instance, load the
    ClickBench web-analytics dataset, and run ClickBench to measure query latency. You'll execute
    the benchmark on an Arm server, observe per‑query timings, and repeat runs across candidate
    instance sizes to compare results. By collecting consistent measurements
    and interpreting the output, you can make instance sizing decisions for analytical workloads
    on Arm. By the end, you'll have a set
    of ClickBench results that indicate how configuration choices influence query latency for
    the provided dataset.
  faqs:
  - question: What should I verify on the instance before starting the benchmark?
    answer: >-
      Use an Arm server or Arm-based cloud instance with a recent Ubuntu for Arm and enough storage
      for the web-analytics dataset. Check available disk space before starting the data load.
  - question: Which dataset is used and how much storage should I plan for?
    answer: >-
      The benchmark uses the ClickBench web-analytics dataset. The exact size is not listed here,
      so allocate sufficient storage and monitor free space during import.
  - question: How do I know ClickHouse is ready to run ClickBench?
    answer: >-
      Complete the installation, start ClickHouse, and follow the steps to confirm it accepts
      connections. Proceed when the setup reports the dataset is loaded and the required tables
      are available.
  - question: What result should I expect after running ClickBench?
    answer: >-
      ClickBench reports per‑query latency measurements and a summary of timings for the workload.
      Use these outputs as the basis for comparing configurations.
  - question: How should I compare different instance configurations?
    answer: >-
      Run the same ClickBench workload on each Arm-based instance with the same ClickHouse settings
      and dataset. Compare the resulting latencies to choose a configuration that fits your workload
      needs.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
tools_software_languages:
    - ClickHouse
    - ClickBench
operatingsystems:
    - Linux

test_images:
- ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-learning-paths/actions/runs/4312122327
test_maintenance: true

further_reading:
    - resource:
        title: ClickHouse Documentation
        link: https://clickhouse.com/docs/en/home/
        type: documentation
    - resource:
        title: ClickBench source repository
        link: https://github.com/ClickHouse/ClickBench/#readme
        type: documentation
    - resource:
        title: Improve ClickHouse performance on Arm-based AWS Graviton3 servers
        link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/improve-clickhouse-performance-up-to-26-by-using-aws-graviton3
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

