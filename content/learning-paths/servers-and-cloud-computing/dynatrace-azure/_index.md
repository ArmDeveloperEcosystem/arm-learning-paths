---
title: Monitor Azure Cobalt 100 Arm64 virtual machines using Dynatrace OneAgent
description: Learn how to deploy Dynatrace OneAgent on Azure Cobalt 100 Arm64 virtual machines and configure ActiveGate for secure infrastructure and application monitoring.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers, DevOps engineers, and platform engineers who want to implement infrastructure and application monitoring using Dynatrace on Arm-based cloud environments.

learning_objectives:
    - Deploy Dynatrace OneAgent on Azure Cobalt 100 Arm64 virtual machines
    - Configure Dynatrace ActiveGate for secure monitoring communication
    - Monitor system resources, processes, and services using Dynatrace
    - Validate application monitoring using a sample NGINX workload

prerequisites:
  - A [Microsoft Azure account](https://azure.microsoft.com/) with access to Cobalt 100 based instances (Dpsv6)
  - Basic knowledge of Linux command-line operations
  - Familiarity with SSH and remote server access
  - Basic understanding of cloud infrastructure and monitoring concepts

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-27T18:53:34Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4ef29931bf19dc95bb586440796381725c271ef1b953dcf46d00ad9617eabbb1
  summary_generated_at: '2026-07-27T18:53:34Z'
  summary_source_hash: 4ef29931bf19dc95bb586440796381725c271ef1b953dcf46d00ad9617eabbb1
  faq_generated_at: '2026-07-27T18:53:34Z'
  faq_source_hash: 4ef29931bf19dc95bb586440796381725c271ef1b953dcf46d00ad9617eabbb1
  summary: >-
    You'll deploy Dynatrace OneAgent on an Azure Cobalt 100 Arm64 virtual machine and configure
    Dynatrace ActiveGate for secure communication with Dynatrace SaaS. You'll provision a Dpsv6 VM,
    allow TCP port 9999 in its Network Security Group, install both components on Ubuntu 24.04 LTS,
    and validate monitoring with a sample NGINX workload. By the end, you'll have host-level visibility
    and a route for Dynatrace communication through ActiveGate.
  faqs:
  - question: Can I create the Cobalt 100 VM with the CLI or IaC instead of the Azure Portal?
    answer: >-
      Yes. There are several ways to create a Cobalt 100 VM, but this path uses the Azure Portal.
      Choose the method that best fits your workflow.
  - question: Which Azure VM series should I select for this walkthrough?
    answer: >-
      Use a general-purpose Dpsv6 series virtual machine based on Azure Cobalt 100. The steps
      focus on that series.
  - question: Which Linux image and architecture do I need for installing OneAgent and ActiveGate?
    answer: >-
      Use Ubuntu 24.04 LTS Arm64. Both Dynatrace OneAgent and ActiveGate operate natively on Arm64
      (aarch64).
  - question: Do I need to open any ports for ActiveGate, and where do I configure it?
    answer: >-
      Yes. Open TCP port 9999 in the Azure Network Security Group attached to the VM’s network
      interface or subnet to allow Dynatrace communication to ActiveGate.
  - question: How do I confirm that monitoring works, including the sample NGINX workload?
    answer: >-
      After installation, OneAgent connects to your Dynatrace SaaS environment and starts monitoring
      system processes and services. Deploy the sample NGINX workload and check that NGINX appears
      among the monitored processes and system metrics update.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - Dynatrace
    - NGINX
    - ActiveGate

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Dynatrace Official Website
      link: https://www.dynatrace.com
      type: website
  - resource:
      title: Dynatrace OneAgent documentation
      link: https://docs.dynatrace.com/docs/observe/infrastructure-monitoring/hosts/installation
      type: documentation
  - resource:
      title: Dynatrace ActiveGate documentation
      link: https://docs.dynatrace.com/docs/ingest-from/dynatrace-activegate
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
