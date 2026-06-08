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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:52:15Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 974d71b1ee968e3aeabe900bfdd52ae4fbfdd0ca7dea420e6c1fc01f5475e8c1
  summary_generated_at: '2026-06-02T03:50:28Z'
  summary_source_hash: 974d71b1ee968e3aeabe900bfdd52ae4fbfdd0ca7dea420e6c1fc01f5475e8c1
  faq_generated_at: '2026-06-03T00:52:15Z'
  faq_source_hash: 974d71b1ee968e3aeabe900bfdd52ae4fbfdd0ca7dea420e6c1fc01f5475e8c1
  summary: >-
    This Learning Path shows how to install and run Apache Flink on an Arm-based Linux server
    and benchmark its stream processing performance using the Nexmark suite. You will set up Java,
    configure a Flink Standalone Cluster, prepare the Nexmark environment (including Maven and
    SSH), and execute benchmark queries. The steps use common Linux tooling and Flink/Nexmark
    scripts to start the cluster, set up the benchmark, and run queries, with optional additional
    query runs. The target audience is developers using Flink on Arm servers. A prerequisite is
    an Arm-based instance from a cloud service provider. The estimated time to complete is about
    30 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Provision an Arm-based Linux instance from a cloud provider such as AWS, Microsoft Azure,
      Google Cloud, or Oracle. You will also need Java installed because Flink runs on the JVM.
  - question: Which Java version should I install for this setup?
    answer: >-
      Install a JDK 11, using either Oracle JDK or OpenJDK. Nexmark requires JDK 1.8+ tools, so
      JDK 11 satisfies both Flink and Nexmark needs.
  - question: What are the Nexmark setup requirements I must have in place?
    answer: >-
      You need a Flink standalone cluster, JDK 1.8.x or higher, and ssh with sshd running for
      the scripts that manage remote components. Maven must be installed, and any required environment
      variables for the scripts should be configured.
  - question: Where do I run the commands to start Flink and the benchmark?
    answer: >-
      Run them on the master node. Use these scripts in order: ~/flink-benchmark/flink-1.17.2/bin/start-cluster.sh,
      then ~/flink-benchmark/nexmark-flink/bin/setup_cluster.sh, and finally ~/flink-benchmark/nexmark-flink/bin/run_query.sh.
  - question: What should I check if the Nexmark scripts fail to start components?
    answer: >-
      Verify that sshd is running, Java is installed and available, and Maven is installed. Ensure
      the Flink standalone cluster is set up and any required environment variables for the scripts
      are defined.
# END generated_summary_faq

author: Ying Yu

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

