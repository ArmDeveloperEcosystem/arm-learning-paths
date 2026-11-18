---
title: Deploy Apache Flink on Google Cloud C4A (Arm-based Axion VMs)
description: Learn how to install and configure Apache Flink on Google Cloud Axion C4A Arm64 instances and benchmark stream processing performance with Nexmark.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers deploying and optimizing Apache Flink workloads on Linux Arm64 environments, specifically using Google Cloud C4A virtual machines powered by Axion processors.

learning_objectives:
  - Provision an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion processors)
  - Install and configure Apache Flink on an Arm64 instance
  - Validate Flink functionality by starting the cluster and running a baseline job
  - Benchmark Flink performance using JMH-based microbenchmarks

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with [Apache Flink](https://flink.apache.org/) and its runtime environment

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T21:57:11Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b32948fd001ddb82835e29a8c35dfc86fbf0d135cacaacce7f00dcd51b1f7a39
  summary_generated_at: '2026-09-10T21:57:11Z'
  summary_source_hash: b32948fd001ddb82835e29a8c35dfc86fbf0d135cacaacce7f00dcd51b1f7a39
  faq_generated_at: '2026-09-10T21:57:11Z'
  faq_source_hash: b32948fd001ddb82835e29a8c35dfc86fbf0d135cacaacce7f00dcd51b1f7a39
  summary: >-
    You'll deploy Apache Flink on a Google Cloud C4A virtual machine powered by an Axion processor. First, you'll create an Arm64-based instance, install Java, configure Flink, and validate the services with a baseline job. Then, you'll build and run Flink microbenchmarks with Maven, using the results to confirm the cluster and review performance in the C4A environment.
  faqs:
  - question: Which C4A machine type should I use to match the steps?
    answer: >-
      Use the `c4a-standard-4` configuration (4 vCPUs, 16 GB memory) to keep your setup consistent with the examples.
  - question: What operating system and package manager should I use?
    answer: >-
      Use a SUSE Arm64-based virtual machine with `zypper` as the package manager.
  - question: Which Java version do I need for Flink on the virtual machine?
    answer: >-
      Install Java 17 (OpenJDK) and its development package using `zypper`.
  - question: Where should I place the Flink distribution on the virtual machine?
    answer: >-
      Download the official Flink distribution to `/opt`.
  - question: How do I verify that Flink is ready for benchmarking?
    answer: >-
      Run `jps` and confirm that `StandaloneSessionClusterEntrypoint` and `TaskManagerRunner` are
      running. Open `http://<VM_IP>:8081` to load the Flink Dashboard, then ensure the WordCount
      example runs successfully before starting the benchmarks.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: Performance and Architecture
platforms:
  - Google Axion

armips:
  - Neoverse

tools_software_languages:
  - Flink
  - Java
  - Maven

operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
  - resource:
      title: Google Cloud documentation
      link: https://cloud.google.com/docs
      type: documentation

  - resource:
      title: Flink documentation
      link: https://nightlies.apache.org/flink/flink-docs-lts/
      type: documentation

  - resource:
      title: Flink Performance Tool
      link: https://github.com/apache/flink-benchmarks/tree/master?tab=readme-ov-file#flink-benchmarks
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
