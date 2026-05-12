---
title: Deploy Apache Kafka on Arm-based Microsoft Azure Cobalt 100 virtual machines 

minutes_to_complete: 30   

who_is_this_for: This is an advanced topic for developers looking to migrate their Apache Kafka workloads from x86_64 to Arm-based platforms, specifically on Microsoft Azure Cobalt 100 (arm64) virtual machines.

description: Deploy Apache Kafka on Azure Cobalt 100 Arm virtual machines and benchmark message throughput performance.

learning_objectives: 
    - Provision an Azure Arm64 virtual machine using Azure console, with Ubuntu Pro 24.04 LTS as the base image
    - Deploy Kafka on an Ubuntu virtual machine
    - Perform Kafka baseline testing and benchmarking on Arm64 virtual machines

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6)
    - Basic understanding of Linux command line
    - Familiarity with the [Apache Kafka architecture](https://kafka.apache.org/) and deployment practices on Arm64 platforms

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:58Z'
  generator: template
  source_hash: d510dd43a485e1c2fac404ef9a2e00b5be2449b99b1095c9a1841cd2fcba9b0e
  summary: >-
    Deploy Apache Kafka on Azure Cobalt 100 Arm virtual machines and benchmark message throughput
    performance. It is designed for developers looking to migrate their Apache Kafka workloads
    from x86_64 to Arm-based platforms, specifically on Microsoft Azure Cobalt 100 (arm64) virtual
    machines. By the end, you will be able to provision an Azure Arm64 virtual machine using Azure
    console, with Ubuntu Pro 24.04 LTS as the base image, deploy Kafka on an Ubuntu virtual machine,
    and perform Kafka baseline testing and benchmarking on Arm64 virtual machines. It focuses
    on tools and technologies such as Kafka, Linux environments, Arm platforms including Neoverse,
    and cloud platforms such as Microsoft Azure. The main steps cover Overview, Create an Arm-based
    cloud virtual machine using Microsoft Cobalt 100 CPU, Install Kafka, Run baseline testing
    with Kafka on Azure Arm VM, and Benchmark with official Kafka tools.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Azure Arm64 virtual machine using Azure console, with Ubuntu Pro 24.04
      LTS as the base image, deploy Kafka on an Ubuntu virtual machine, and perform Kafka baseline
      testing and benchmarking on Arm64 virtual machines. Deploy Apache Kafka on Azure Cobalt
      100 Arm virtual machines and benchmark message throughput performance.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for developers looking to migrate their Apache Kafka workloads
      from x86_64 to Arm-based platforms, specifically on Microsoft Azure Cobalt 100 (arm64) virtual
      machines.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Microsoft Azure](https://azure.microsoft.com/)
      account with access to Cobalt 100 based instances (Dpsv6); Basic understanding of Linux
      command line; Familiarity with the [Apache Kafka architecture](https://kafka.apache.org/)
      and deployment practices on Arm64 platforms.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Kafka, Linux environments, Arm platforms such as
      Neoverse, and cloud platforms such as Microsoft Azure.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Overview, Create an Arm-based cloud virtual machine
      using Microsoft Cobalt 100 CPU, Install Kafka, Run baseline testing with Kafka on Azure
      Arm VM, and Benchmark with official Kafka tools.
# END generated_summary_faq

author: Pareena Verma

### Tags
skilllevels: Advanced
subjects: Storage
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - Kafka

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Kafka Manual
        link: https://kafka.apache.org/documentation/
        type: documentation
    - resource:
        title: Kafka Performance Tool
        link: https://codemia.io/knowledge-hub/path/use_kafka-producer-perf-testsh_how_to_set_producer_config_at_kafka_210-0820
        type: documentation
    - resource:        
        title: Kafka on Azure
        link: https://learn.microsoft.com/en-us/samples/azure/azure-quickstart-templates/kafka-ubuntu-multidisks/
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

