---
title: Run Spark applications on Microsoft Azure Cobalt 100 processors

minutes_to_complete: 60

who_is_this_for: This is an advanced topic that introduces Spark deployment on Microsoft Azure Cobalt 100 (Arm-based) virtual machines. It is designed for developers migrating Spark applications from x86_64 to Arm.

learning_objectives: 
    - Provision an Azure Arm64 virtual machine using Azure console
    - Learn how to create an Azure Linux 3.0 Docker container
    - Deploy a Spark application inside an Azure Linux 3.0 Arm64-based Docker container or an Azure Linux 3.0 custom-image based Azure virtual machine
    - Run a suite of Spark benchmarks to understand and evaluate performance on the Azure Cobalt 100 virtual machine

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6)
    - A machine with [Docker](/install-guides/docker/) installed
    - Familiarity with distributed computing concepts and the [Apache Spark architecture](https://spark.apache.org/docs/latest/)

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:19Z'
  generator: template
  source_hash: 009f2219f1b949be39b4a1dd43a5e4c1ceb5bb273d9a11c3c155315160d593ac
  summary: >-
    Run Spark applications on Microsoft Azure Cobalt 100 processors walks you through an end-to-end
    Arm software workflow. It is designed for This is an advanced topic that introduces Spark
    deployment on Microsoft Azure Cobalt 100 (Arm-based) virtual machines. It is designed for
    developers migrating Spark applications from x86_64 to Arm. By the end, you will be able to
    provision an Azure Arm64 virtual machine using Azure console, learn how to create an Azure
    Linux 3.0 Docker container, and deploy a Spark application inside an Azure Linux 3.0 Arm64-based
    Docker container or an Azure Linux 3.0 custom-image based Azure virtual machine. It focuses
    on tools and technologies such as Apache Spark, Python, and Docker, Linux environments, Arm
    platforms including Neoverse, and cloud platforms such as Microsoft Azure. The main steps
    cover Getting started with Microsoft Azure Cobalt 100, Azure Linux 3.0, and Apache Spark,
    Create an Azure Cobalt 100 Arm64 virtual machine, Set up an Azure Linux 3.0 environment, Install
    Apache Spark on Azure Cobalt 100 processors, and Validate Apache Spark on Azure Cobalt 100
    Arm64 VMs.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Azure Arm64 virtual machine using Azure console, learn how to create
      an Azure Linux 3.0 Docker container, and deploy a Spark application inside an Azure Linux
      3.0 Arm64-based Docker container or an Azure Linux 3.0 custom-image based Azure virtual
      machine.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic that introduces Spark deployment on Microsoft Azure Cobalt 100
      (Arm-based) virtual machines. It is designed for developers migrating Spark applications
      from x86_64 to Arm.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Microsoft Azure](https://azure.microsoft.com/)
      account with access to Cobalt 100 based instances (Dpsv6); A machine with [Docker](/install-guides/docker/)
      installed; Familiarity with distributed computing concepts and the [Apache Spark architecture](https://spark.apache.org/docs/latest/).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Apache Spark, Python, and Docker, Linux environments,
      Arm platforms such as Neoverse, and cloud platforms such as Microsoft Azure.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Getting started with Microsoft Azure Cobalt 100, Azure
      Linux 3.0, and Apache Spark, Create an Azure Cobalt 100 Arm64 virtual machine, Set up an
      Azure Linux 3.0 environment, Install Apache Spark on Azure Cobalt 100 processors, and Validate
      Apache Spark on Azure Cobalt 100 Arm64 VMs.
# END generated_summary_faq

author: Pareena Verma

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - Apache Spark
    - Python
    - Docker
 
operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Azure Virtual Machines documentation
      link: https://learn.microsoft.com/en-us/azure/virtual-machines/
      type: documentation
  - resource:
      title: Azure Container Instances documentation
      link: https://learn.microsoft.com/en-us/azure/container-instances/
      type: documentation
  - resource:
      title: Docker overview
      link: https://docs.docker.com/get-started/overview/
      type: documentation
  - resource:
      title: Spark official website and documentation
      link: https://spark.apache.org/
      type: documentation
  - resource:
      title: Hadoop official website
      link: https://hadoop.apache.org/
      type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

