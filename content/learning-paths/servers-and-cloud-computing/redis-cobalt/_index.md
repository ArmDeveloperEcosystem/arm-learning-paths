---
title: Deploy Redis on Azure Cobalt 100 Arm64 virtual machines for real-time messaging and event processing
description: Learn how to install and configure Redis on an Azure Cobalt 100 Arm64 virtual machine, implement real-time messaging with Pub/Sub and Streams, and benchmark throughput and latency on Arm infrastructure.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers, DevOps engineers, and platform engineers who want to build real-time messaging systems and event-driven applications using Redis on Arm-based cloud environments.

learning_objectives:
    - Install and configure Redis on Azure Cobalt 100 Arm64 virtual machines
    - Implement real-time messaging using Redis Pub/Sub
    - Build event-driven pipelines using Redis Streams and consumer groups
    - Benchmark Redis performance and validate throughput and latency on Arm

prerequisites:
  - A [Microsoft Azure account](https://azure.microsoft.com/) with access to Cobalt 100 based instances (Dpsv6)
  - Basic knowledge of Linux command-line operations
  - Familiarity with SSH and remote server access
  - Basic understanding of databases, caching, and messaging systems

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:59:01Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9b306bc318491834d0d74dd75221b24081acc20dac7993ccdbd1cb40ba6158ac
  summary_generated_at: '2026-06-02T04:58:08Z'
  summary_source_hash: 9b306bc318491834d0d74dd75221b24081acc20dac7993ccdbd1cb40ba6158ac
  faq_generated_at: '2026-06-03T01:59:01Z'
  faq_source_hash: 9b306bc318491834d0d74dd75221b24081acc20dac7993ccdbd1cb40ba6158ac
  summary: >-
    Learn how to deploy Redis on Azure Cobalt 100 Arm64 virtual machines running Linux, then build
    and validate real-time messaging and event-driven processing on Arm. You will provision a
    Cobalt 100 VM in the Dpsv6 series (via the Azure Portal, with options to use the CLI or IaC),
    install and configure Redis, implement Pub/Sub for low-latency messaging, and use Redis Streams
    with consumer groups to create scalable pipelines. You will simulate workloads with Python
    and benchmark throughput and latency to validate performance on Arm-based infrastructure.
    Prerequisites include an Azure account with Cobalt 100 access, basic Linux and SSH skills,
    and familiarity with databases and messaging.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Microsoft Azure account with access to Cobalt 100 based instances (Dpsv6), basic
      Linux command-line skills, familiarity with SSH, and a basic understanding of databases,
      caching, and messaging systems.
  - question: Which Azure VM type and creation method should I use?
    answer: >-
      The Learning Path focuses on general-purpose Cobalt 100 Arm-based virtual machines in the
      Dpsv6 series. You can create the VM via the Azure Portal (used in this path), or use the
      Azure CLI or an infrastructure as code tool if that better fits your workflow.
  - question: How do I confirm I’m using an Arm-based Cobalt 100 VM?
    answer: >-
      During provisioning, ensure you select a Cobalt 100 Arm64 instance in the Dpsv6 series.
      The path targets an Arm-based Linux VM on Azure Cobalt 100.
  - question: Do I need Python, and where is it used?
    answer: >-
      Yes. Python is used to simulate workloads when validating and benchmarking Redis in the
      final section.
  - question: What result should I expect after completing the examples and benchmarks?
    answer: >-
      You will have Redis installed and running on a Cobalt 100 VM, with working Pub/Sub messaging
      and Streams using consumer groups. You will also collect throughput and latency measurements
      to validate Redis performance on Arm infrastructure.
# END generated_summary_faq

author: Pareena Verma

### Tags
### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - Redis
    - Python

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Redis Official Website
      link: https://redis.io
      type: website
  - resource:
      title: Redis Documentation
      link: https://redis.io/docs/
      type: documentation
  - resource:
      title: Redis Streams Introduction
      link: https://redis.io/docs/data-types/streams/
      type: documentation
  - resource:
      title: Azure Cobalt 100 processors
      link: https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

