---
title: Deploy RabbitMQ on Arm64 Cloud Platforms (Azure & GCP)

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

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Databases

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
