---
title: Deploy RabbitMQ on Arm64 on Microsoft Azure and Google Cloud

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software engineers and platform engineers migrating messaging and event-driven workloads from x86_64 to Arm-based servers, specifically on Microsoft Azure Cobalt 100 Arm processors and Google Cloud C4A virtual machines powered by Axion processors. 

learning_objectives:
  - Provision Arm-based Linux virtual machines (VMs) on Google Cloud and Microsoft Azure.
  - Provision an Arm-based SUSE SLES VM on Google Cloud.
  - Install and configure RabbitMQ on SUSE SLES on Google Cloud and Ubuntu Pro 24.04 on Azure.
  - Build and configure required Erlang versions for RabbitMQ on Arm64.
  - Validate RabbitMQ deployments using baseline messaging and connectivity tests.
  - Implement practical RabbitMQ use cases such as event-driven processing and notification pipelines.

prerequisites:
  - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100-based instances (Dpsv6)
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic understanding of message queues and messaging concepts such as publishers and consumers
  - Familiarity with Linux command-line operations

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-19T16:00:22Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 952b6e5049d77bc49e9d51ffd3726f0a651623812d458923807ab59885e779af
  summary_generated_at: '2026-11-19T16:00:22Z'
  summary_source_hash: 952b6e5049d77bc49e9d51ffd3726f0a651623812d458923807ab59885e779af
  faq_generated_at: '2026-11-19T16:00:22Z'
  faq_source_hash: 952b6e5049d77bc49e9d51ffd3726f0a651623812d458923807ab59885e779af
  summary: >-
    You'll deploy and verify RabbitMQ on Arm-based Azure and Google Cloud VMs. First, you'll install
    Erlang and RabbitMQ on an Azure Cobalt VM, enable the management plugin, and check the
    service and versions. You'll then provision a Google Axion C4A VM, install RabbitMQ, and
    configure a VPC firewall rule for management access. Finally, you'll check broker
    connectivity and the management interface.
  faqs:
  - question: Which Azure virtual machine size should I use?
    answer: >-
      Select a Dpsv6 series VM backed by Azure Cobalt 100.
  - question: Which image should I use for the Azure virtual machine?
    answer: >-
      Use Ubuntu Pro 24.04 for Arm64.
  - question: How do I verify RabbitMQ on the Azure VM?
    answer: >-
      Run `sudo systemctl status rabbitmq` and check for `active (running)`.
  - question: How do I check the Erlang version on Azure?
    answer: >-
      Run `erl -eval` and check that the output reports Erlang/OTP 26.
  - question: How do I fix not being able to open the management interface on the Google Cloud VM?
    answer: >-
      Check that your VPC firewall rule allows inbound TCP port `15672` and that its target
      tag is applied to the VM. You can compare the rule with the `allow-tcp-15672` example.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: Databases
platforms:
  - Microsoft Azure Cobalt
  - Google Axion

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

