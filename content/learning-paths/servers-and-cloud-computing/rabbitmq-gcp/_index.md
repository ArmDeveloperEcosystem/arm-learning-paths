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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:56:11Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b4392f1cf38fa1f3b6c633c7ae1e8d30a51ea8d4e635287586b084cb0d8a556b
  summary_generated_at: '2026-06-02T04:53:31Z'
  summary_source_hash: b4392f1cf38fa1f3b6c633c7ae1e8d30a51ea8d4e635287586b084cb0d8a556b
  faq_generated_at: '2026-06-03T01:56:11Z'
  faq_source_hash: b4392f1cf38fa1f3b6c633c7ae1e8d30a51ea8d4e635287586b084cb0d8a556b
  summary: >-
    Learn how to deploy RabbitMQ on Arm64 infrastructure across Microsoft Azure and Google Cloud.
    You will provision Arm-based Linux virtual machines on Azure Cobalt 100 (Dpsv6) and Google
    Cloud C4A with Axion processors, install RabbitMQ 4.2.0 with the required Erlang (OTP 26)
    on Ubuntu Pro 24.04 for Azure, and configure a SUSE SLES VM on GCP. The path covers baseline
    validation steps for RabbitMQ, including service and version checks, and setting up a GCP
    firewall rule to expose the management interface (TCP 15672). It targets engineers migrating
    messaging workloads and uses RabbitMQ, Erlang, Python, and pika. Prerequisites include Azure
    and GCP accounts, basic messaging concepts, and Linux command-line familiarity.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Microsoft Azure account with access to Cobalt 100-based Dpsv6 instances, a Google
      Cloud account with billing enabled, a basic understanding of message queuing concepts, and
      familiarity with Linux command-line operations.
  - question: Which Azure VM series and creation method does this path use?
    answer: >-
      The path uses Azure Cobalt 100 Dpsv6 instances and creates the VM through the Azure console.
      Other methods like the Azure CLI or IaC are mentioned but are not used in the walkthrough.
  - question: How do I verify RabbitMQ and Erlang after installation on Azure?
    answer: >-
      Check the service status with sudo systemctl status rabbitmq and confirm the Erlang runtime
      with the provided erl -eval command (OTP 26). The path also includes a step to confirm the
      installed RabbitMQ version.
  - question: How do I expose the RabbitMQ management interface on GCP?
    answer: >-
      Create a VPC firewall rule that allows TCP port 15672. In Google Cloud Console, go to VPC
      Network > Firewall > Create firewall rule, name it (for example, allow-tcp-15672), select
      your network, and allow ingress on TCP 15672.
  - question: What should I check if baseline validation fails?
    answer: >-
      Verify that the RabbitMQ service is running, confirm Erlang is OTP 26 using the provided
      command, and follow the RabbitMQ version check step. If accessing the management UI on GCP,
      ensure the firewall rule for TCP 15672 is correctly configured.
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

