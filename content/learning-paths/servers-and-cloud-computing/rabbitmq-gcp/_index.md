---
title: Deploy RabbitMQ on Arm64 Cloud Platforms (Azure and GCP)

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software engineers and platform engineers migrating messaging and event-driven workloads from x86_64 to Arm-based servers, specifically on Microsoft Azure Cobalt 100 Arm processors and Google Cloud C4A virtual machines powered by Axion processors. 

learning_objectives:
  - Provision Arm-based Linux virtual machines on Google Cloud (C4A with Axion processors) and Microsoft Azure (Cobalt 100)
  - Provision an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion processors)
  - Install and configure RabbitMQ on Arm64 Linux (SUSE SLES on GCP and Ubuntu Pro 24.04 on Azure)
  - Build and configure required Erlang versions for RabbitMQ on Arm64
  - Validate RabbitMQ deployments using baseline messaging and connectivity tests
  - Implement practical RabbitMQ use cases such as event-driven processing and notification pipelines on Arm-based infrastructure

prerequisites:
  - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100-based instances (Dpsv6).
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic understanding of message queues and messaging concepts (publishers, consumers)
  - Familiarity with Linux command-line operations

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:19Z'
  generator: template
  source_hash: b4392f1cf38fa1f3b6c633c7ae1e8d30a51ea8d4e635287586b084cb0d8a556b
  summary: >-
    Deploy RabbitMQ on Arm64 Cloud Platforms (Azure and GCP) walks you through an end-to-end Arm
    software workflow. It is designed for software engineers and platform engineers migrating
    messaging and event-driven workloads from x86_64 to Arm-based servers, specifically on Microsoft
    Azure Cobalt 100 Arm processors and Google Cloud C4A virtual machines powered by Axion processors.
    By the end, you will be able to provision Arm-based Linux virtual machines on Google Cloud
    (C4A with Axion processors) and Microsoft Azure (Cobalt 100), provision an Arm-based SUSE
    SLES virtual machine on Google Cloud (C4A with Axion processors), and install and configure
    RabbitMQ on Arm64 Linux (SUSE SLES on GCP and Ubuntu Pro 24.04 on Azure). It focuses on tools
    and technologies such as RabbitMQ, Erlang, Python, and pika, Linux environments, Arm platforms
    including Neoverse, and cloud platforms such as Microsoft Azure and Google Cloud. The main
    steps cover Learn about Arm-based cloud platforms for RabbitMQ, Create an Azure Cobalt 100
    virtual machine, Install RabbitMQ on Azure Cobalt 100, Validate RabbitMQ on Azure, and Create
    a firewall rule for RabbitMQ.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision Arm-based Linux virtual machines on Google Cloud (C4A with Axion processors)
      and Microsoft Azure (Cobalt 100), provision an Arm-based SUSE SLES virtual machine on Google
      Cloud (C4A with Axion processors), and install and configure RabbitMQ on Arm64 Linux (SUSE
      SLES on GCP and Ubuntu Pro 24.04 on Azure).
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for software engineers and platform engineers migrating messaging
      and event-driven workloads from x86_64 to Arm-based servers, specifically on Microsoft Azure
      Cobalt 100 Arm processors and Google Cloud C4A virtual machines powered by Axion processors.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Microsoft Azure](https://azure.microsoft.com/)
      account with access to Cobalt 100-based instances (Dpsv6).; A [Google Cloud Platform (GCP)](https://cloud.google.com/free)
      account with billing enabled; Basic understanding of message queues and messaging concepts
      (publishers, consumers); Familiarity with Linux command-line operations.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including RabbitMQ, Erlang, Python, and pika, Linux environments,
      Arm platforms such as Neoverse, and cloud platforms such as Microsoft Azure and Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Learn about Arm-based cloud platforms for RabbitMQ,
      Create an Azure Cobalt 100 virtual machine, Install RabbitMQ on Azure Cobalt 100, Validate
      RabbitMQ on Azure, and Create a firewall rule for RabbitMQ.
# END generated_summary_faq

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers:
  - Microsoft Azure
  - Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - RabbitMQ
  - Erlang
  - Python
  - pika

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
      title: Azure Virtual Machines documentation
      link: https://learn.microsoft.com/azure/virtual-machines/
      type: documentation    

  - resource:
      title: RabbitMQ documentation
      link: https://www.rabbitmq.com/documentation.html 
      type: documentation

  - resource:
      title: RabbitMQ Tutorials
      link: https://www.rabbitmq.com/getstarted.html
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

