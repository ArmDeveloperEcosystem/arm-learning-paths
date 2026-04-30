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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:18Z'
  generator: template
  source_hash: adcf2a1b8a4a77e5834e14a40e46e27b0cbe5e440fbf732a4366ce486d7fafb7
  summary: >-
    Learn how to install and configure Apache Flink on Google Cloud Axion C4A Arm64 instances
    and benchmark stream processing performance with Nexmark. It is designed for developers deploying
    and optimizing Apache Flink workloads on Linux/Arm64 environments, specifically using Google
    Cloud C4A virtual machines powered by Axion processors. By the end, you will be able to provision
    an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion processors), install
    and configure Apache Flink on an Arm64 instance, and validate Flink functionality by starting
    the cluster and running a baseline job. It focuses on tools and technologies such as Flink,
    Java, and Maven, Linux environments, Arm platforms including Neoverse, and cloud platforms
    such as Google Cloud. The main steps cover Get started with Apache Flink on Google Axion C4A,
    Create a Google Axion C4A Arm virtual machine, Install Apache Flink, Test Flink baseline functionality,
    and Benchmark Flink performance.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion
      processors), install and configure Apache Flink on an Arm64 instance, and validate Flink
      functionality by starting the cluster and running a baseline job. Learn how to install and
      configure Apache Flink on Google Cloud Axion C4A Arm64 instances and benchmark stream processing
      performance with Nexmark.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers deploying and optimizing Apache Flink workloads
      on Linux/Arm64 environments, specifically using Google Cloud C4A virtual machines powered
      by Axion processors.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud Platform (GCP)](https://cloud.google.com/free)
      account with billing enabled; Basic familiarity with [Apache Flink](https://flink.apache.org/)
      and its runtime environment.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Flink, Java, and Maven, Linux environments, Arm
      platforms such as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Get started with Apache Flink on Google Axion C4A,
      Create a Google Axion C4A Arm virtual machine, Install Apache Flink, Test Flink baseline
      functionality, and Benchmark Flink performance.
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

