---
title: Deploy Alluxio on Azure Cobalt 100 Arm64 virtual machines for data orchestration and caching

description: Learn how to install and configure Alluxio on an Azure Cobalt 100 Arm64 virtual machine, integrate it with Apache Spark, enable data caching, and benchmark performance improvements for analytics workloads.

minutes_to_complete: 90

who_is_this_for: This is an introductory topic for developers, data engineers, and platform engineers who want to build high-performance data pipelines and analytics systems using Alluxio on Arm-based cloud environments.

learning_objectives:
    - Install and configure Alluxio on Azure Cobalt 100 Arm64 virtual machines
    - Configure data caching using Alluxio memory storage
    - Integrate Alluxio with Apache Spark for analytics workloads
    - Benchmark data access performance and understand caching benefits

prerequisites:
  - A [Microsoft Azure account](https://azure.microsoft.com/) with access to Cobalt 100 based instances (Dpsv6)
  - Basic knowledge of Linux command-line operations
  - Familiarity with SSH and remote server access
  - Basic understanding of data processing, storage systems, and caching concepts

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-26T17:21:44Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a518336582a04b9bd5646608eeec314ec70fc6f5121299677d21ddb8819dcb85
  summary_generated_at: '2026-06-26T17:21:44Z'
  summary_source_hash: a518336582a04b9bd5646608eeec314ec70fc6f5121299677d21ddb8819dcb85
  faq_generated_at: '2026-06-26T17:21:44Z'
  faq_source_hash: a518336582a04b9bd5646608eeec314ec70fc6f5121299677d21ddb8819dcb85
  summary: >-
    You'll deploy Alluxio on an Arm-based virtual machine powered by Azure Cobalt 100
    and use it as a data orchestration and caching layer for Apache Spark. After creating a Dpsv6
    VM, you'll enable the Alluxio Web UI by adding an inbound rule for TCP port 19999 in the Azure
    Network Security Group. You'll install and configure Alluxio with local storage and memory-backed
    caching, then install Apache Spark under `/opt` and configure Spark to read through Alluxio.
    The hands-on work concludes with read workloads comparing uncached and cached access that you can use to interpret the impact of in-memory caching on analytics tasks.
  faqs:
  - question: Which Azure VM size should I select for this setup?
    answer: >-
      Use a general-purpose VM in the Dpsv6 series to run on Azure Cobalt 100 Arm-based processors.
      The creation steps focus on this series.
  - question: How do I allow access to the Alluxio Web UI from the internet?
    answer: >-
      Add an inbound rule for TCP port 19999 in the Azure Network Security Group (NSG). You can attach the NSG to the VM’s network interface or its subnet.
  - question: How can I confirm the Alluxio Web UI is reachable after opening the port?
    answer: >-
      After creating the NSG rule for port 19999, browse to the VM’s public IP using that port
      to load the Alluxio Web UI. If it doesn't load, verify the NSG is correctly attached and
      the rule allows inbound traffic.
  - question: What preparation should I do on the VM before installing Alluxio?
    answer: >-
      Update the package index, apply available updates, and install basic tools such as `wget`,
      `curl`, and `tar`. These tools download and extract the required software.
  - question: Where should Apache Spark be installed and how is it used with Alluxio?
    answer: >-
      Install Apache Spark and place it under `/opt` as shown in the Learning Path. Spark is then configured
      to read through Alluxio, so frequently accessed data can be cached in memory.
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
    - Alluxio
    - Apache Spark
    - Java

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Alluxio Official Website
      link: https://www.alluxio.io/
      type: website
  - resource:
      title: Alluxio Documentation
      link: https://docs.alluxio.io/
      type: documentation
  - resource:
      title: Apache Spark Documentation
      link: https://spark.apache.org/docs/latest/
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
