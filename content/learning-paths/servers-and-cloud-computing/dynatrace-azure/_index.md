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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:44:58Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4ef29931bf19dc95bb586440796381725c271ef1b953dcf46d00ad9617eabbb1
  summary_generated_at: '2026-06-02T03:39:49Z'
  summary_source_hash: 4ef29931bf19dc95bb586440796381725c271ef1b953dcf46d00ad9617eabbb1
  faq_generated_at: '2026-06-03T00:44:58Z'
  faq_source_hash: 4ef29931bf19dc95bb586440796381725c271ef1b953dcf46d00ad9617eabbb1
  summary: >-
    This Learning Path shows how to monitor Azure Cobalt 100 Arm64 virtual machines with Dynatrace.
    You will create an Azure VM in the Dpsv6 series, install Dynatrace OneAgent on Ubuntu 24.04
    LTS Arm64, and configure Dynatrace ActiveGate as a secure gateway to the Dynatrace SaaS platform.
    You will open TCP port 9999 in the Azure Network Security Group to allow ActiveGate traffic,
    then verify host and application visibility by monitoring system resources, processes, and
    services, and validating with a sample NGINX workload. Prerequisites include an Azure account
    with access to Cobalt 100 instances, basic Linux command-line skills, SSH familiarity, and
    a basic understanding of cloud and monitoring concepts.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Microsoft Azure account with access to Cobalt 100 based instances (Dpsv6), basic
      Linux command-line skills, familiarity with SSH, and a basic understanding of cloud infrastructure
      and monitoring concepts. The path connects to a Dynatrace SaaS environment, but specific
      account details are not explicitly listed.
  - question: Which Azure VM type and operating system should I use?
    answer: >-
      Use a general-purpose VM in the Dpsv6 series running on Azure Cobalt 100 processors. The
      installation steps target Ubuntu 24.04 LTS Arm64.
  - question: How do I allow Dynatrace ActiveGate traffic to the VM?
    answer: >-
      Create a Network Security Group rule in the Azure Portal to allow inbound TCP traffic on
      port 9999. Apply the rule to the NSG attached to the VM’s network interface or subnet.
  - question: How do I know if OneAgent and ActiveGate are installed correctly?
    answer: >-
      After installation, OneAgent runs as a host monitoring agent, connects to your Dynatrace
      SaaS environment, and begins monitoring system processes and services automatically. ActiveGate
      runs as a system service, listens on port 9999, and communicates with Dynatrace.
  - question: What result should I expect when validating with the sample NGINX workload?
    answer: >-
      You should see NGINX detected in Dynatrace with process and service monitoring data from
      the Arm64 VM. This confirms that application monitoring is functioning through OneAgent
      and, if configured, via ActiveGate.
# END generated_summary_faq

author: Pareena Verma

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

