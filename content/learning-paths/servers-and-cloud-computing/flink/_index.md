---
title: Benchmark the performance of Flink on Arm servers
description: Learn how to install and run Apache Flink on Arm servers and benchmark stream processing performance using the Nexmark benchmark suite.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers using Flink
  as their stream processing and batch processing framework on Arm servers.

learning_objectives:
- Install and run Flink on an Arm server
- Benchmark the performance of Flink

prerequisites:
- An Arm based instance server from a cloud service provider.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T21:57:38Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: bb2a2c0e6df8eea4c67143a9382033a87257dd814b660b6b6629fa8afd989e82
  summary_generated_at: '2026-09-10T21:57:38Z'
  summary_source_hash: bb2a2c0e6df8eea4c67143a9382033a87257dd814b660b6b6629fa8afd989e82
  faq_generated_at: '2026-09-10T21:57:38Z'
  faq_source_hash: bb2a2c0e6df8eea4c67143a9382033a87257dd814b660b6b6629fa8afd989e82
  summary: >-
    You'll install Java and configure a standalone Apache Flink cluster on an Arm-based Linux server. First, you'll meet the Nexmark prerequisites, start Flink with the provided scripts, prepare the benchmark environment, and run selected queries. Next, you'll use the completed runs to verify that the cluster starts cleanly, and to understand how Java versions and script locations affect the workflow.
  faqs:
  - question: Which Java version should I use when I run Flink and Nexmark?
    answer: >-
      Flink requires JDK 11, and Nexmark requires JDK 1.8.x or higher. Use JDK 11 to satisfy both
      requirements.
  - question: Where should I run the Flink and Nexmark scripts?
    answer: >-
      Run the scripts on the master node. Use paths such as
      `~/flink-benchmark/flink-1.17.2/bin/start-cluster.sh` and
      `~/flink-benchmark/nexmark-flink/bin/setup_cluster.sh`.
  - question: Which configuration values must point to the Flink JobManager?
    answer: >-
      Set `jobmanager.rpc.address` in `flink-conf.yaml` and
      `nexmark.metric.reporter.host` in `nexmark.yaml` to the JobManager address. You can use
      the JobManager IP or the default `localhost:8081` when the components run on the same host.
  - question: What should I check about SSH before I run the scripts?
    answer: >-
      Ensure `sshd` is running because the Flink and Nexmark scripts use SSH to manage remote components.
      Start or enable the service before continuing.
  - question: How can I run specific Nexmark queries?
    answer: >-
      Pass a comma-separated query list to `run_query.sh`, such as
      `bash ~/flink-benchmark/nexmark-flink/bin/run_query.sh q1,q2`. The script runs the selected
      queries and reports their benchmark results.
# END generated_summary_faq

author: Ying Yu

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
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
- Flink
- Java
- Nexmark
- Runbook

further_reading:
    - resource:
        title: Flink Manual
        link: https://nightlies.apache.org/flink/flink-docs-stable/
        type: documentation
    - resource:
        title: Flink Performance Tool
        link: https://github.com/nexmark/nexmark#readme
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
