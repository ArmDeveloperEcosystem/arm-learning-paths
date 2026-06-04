---
title: Deploy Apache Flink on Google Cloud C4A (Arm-based Axion VMs)
description: Learn how to install and configure Apache Flink on Google Cloud Axion C4A Arm64 instances and benchmark stream processing performance with Nexmark.
    
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers deploying and optimizing Apache Flink workloads on Linux/Arm64 environments, specifically using Google Cloud C4A virtual machines powered by Axion processors.

learning_objectives:
  - Provision an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion processors)
  - Install and configure Apache Flink on an Arm64 instance
  - Validate Flink functionality by starting the cluster and running a baseline job
  - Benchmark Flink performance using JMH-based microbenchmarks

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with [Apache Flink](https://flink.apache.org/) and its runtime environment

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:53:07Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: adcf2a1b8a4a77e5834e14a40e46e27b0cbe5e440fbf732a4366ce486d7fafb7
  summary_generated_at: '2026-06-02T03:51:50Z'
  summary_source_hash: adcf2a1b8a4a77e5834e14a40e46e27b0cbe5e440fbf732a4366ce486d7fafb7
  faq_generated_at: '2026-06-03T00:53:07Z'
  faq_source_hash: adcf2a1b8a4a77e5834e14a40e46e27b0cbe5e440fbf732a4366ce486d7fafb7
  summary: >-
    Learn how to deploy Apache Flink on Google Cloud C4A virtual machines powered by Axion processors
    (Arm Neoverse-V2) using a SUSE Linux Arm64 environment. You will provision a c4a-standard-4
    VM through the Google Cloud Console, install Java 17 and Flink, and validate your setup by
    starting the Flink cluster and running a baseline job. The path then guides you to install
    Maven and benchmark Flink using the official JMH-based flink-benchmarks suite, including the
    Remote Channel Throughput Benchmark. By the end, you will have a working Flink environment
    on Arm-based Google Cloud infrastructure and baseline microbenchmark results. Prerequisites
    are a GCP account with billing enabled and basic familiarity with Flink.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need a Google Cloud Platform account with billing enabled and basic familiarity with
      Apache Flink and its runtime. Sudo access on the VM is implied because the steps install
      packages and place files under system directories.
  - question: Which Google Cloud VM and OS should I create for the exercises?
    answer: >-
      Create an Axion C4A Arm instance, using the c4a-standard-4 machine type in the Google Cloud
      Console under Compute Engine > VM Instances. The steps assume a SUSE SLES Arm64 virtual
      machine.
  - question: Which Java version is required on the VM?
    answer: >-
      Install Java 17 (OpenJDK) along with the development package on the SUSE system. The steps
      use zypper to install java-17-openjdk and java-17-openjdk-devel.
  - question: Where should I install Flink and how do I confirm it works?
    answer: >-
      The path downloads and installs the official Flink distribution under /opt on the VM. You
      will validate the installation by starting the Flink cluster and running a baseline job
      to confirm the JobManager and TaskManager execute successfully.
  - question: Which benchmarks will I run and how are they executed?
    answer: >-
      You will clone the official apache/flink-benchmarks repository, build it with Maven, and
      run JMH-based microbenchmarks. The steps demonstrate running the Remote Channel Throughput
      Benchmark to assess Flink performance on the C4A instance.
# END generated_summary_faq

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - Google Cloud

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

