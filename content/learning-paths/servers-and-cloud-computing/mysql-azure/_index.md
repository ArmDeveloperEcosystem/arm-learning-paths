---
title: Deploy MySQL on Microsoft Azure Cobalt 100 processors

   
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers migrating MySQL applications from x86_64 to Arm.

learning_objectives:
    - Provision an Azure Arm64 virtual machine using Azure console, with Ubuntu Pro 24.04 LTS as the base image
    - Deploy MySQL on the Ubuntu virtual machine
    - Perform MySQL baseline testing and benchmarking on Arm64 virtual machines

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6)
    - Familiarity with relational databases and the basics of [MySQL](https://dev.mysql.com/doc/refman/8.0/en/introduction.html)

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:36:24Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b9bc1d1f965e4fdeeb9552d853330c201e00597829420c8a0397fa425c3231c4
  summary_generated_at: '2026-06-02T04:33:49Z'
  summary_source_hash: b9bc1d1f965e4fdeeb9552d853330c201e00597829420c8a0397fa425c3231c4
  faq_generated_at: '2026-06-03T01:36:24Z'
  faq_source_hash: b9bc1d1f965e4fdeeb9552d853330c201e00597829420c8a0397fa425c3231c4
  summary: >-
    Learn how to provision an Arm64 virtual machine on Microsoft Azure Cobalt 100 (Neoverse-N2)
    using the Azure Portal with Ubuntu Pro 24.04 LTS, deploy and secure MySQL, validate the service,
    and run baseline benchmarks with mysqlslap. Aimed at developers migrating MySQL applications
    from x86_64 to Arm, this introductory path focuses on Dpsv6 series VMs and walks through installation,
    configuration, and functional checks to confirm the database is ready for use. You will also
    perform baseline testing with mysqlslap to understand MySQL behavior on Azure Arm64. Prerequisites
    include an Azure account with access to Cobalt 100 instances (Dpsv6) and familiarity with
    relational databases and MySQL basics.
  faqs:
  - question: Which Azure VM size and base image should I use?
    answer: >-
      Use a general-purpose VM in the Dpsv6 series (Cobalt 100, Arm64) and select Ubuntu Pro 24.04
      LTS as the base image. The path provisions the VM via the Azure Portal.
  - question: Can I create the VM with Azure CLI or IaC instead of the Azure Portal?
    answer: >-
      Yes, Azure CLI and IaC are common alternatives, but this path demonstrates the Azure Portal
      workflow. If you prefer CLI or IaC, you can adapt the same choices (Dpsv6, Ubuntu Pro 24.04
      LTS), though those steps are not covered here.
  - question: What do I need before running the steps?
    answer: >-
      You need a Microsoft Azure account with access to Cobalt 100 based instances (Dpsv6). Familiarity
      with relational databases and the basics of MySQL is also expected.
  - question: How do I know MySQL started and is ready for use?
    answer: >-
      Start and enable MySQL using systemctl as shown in the validation step. Then perform the
      functional checks to confirm queries run, users can authenticate, and the environment is
      correctly configured for cloud workloads.
  - question: How do I benchmark MySQL in this setup, and what does mysqlslap measure?
    answer: >-
      Use the built-in mysqlslap tool to run baseline tests on the Azure Cobalt 100 (Arm64) VM.
      It simulates multiple clients and reports read/write throughput, query response times, and
      overall MySQL server performance under different workloads.
# END generated_summary_faq

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - MySQL
    - SQL
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
      title: MySQL Manual
      link: https://dev.mysql.com/doc/refman/8.0/en/installing.html
      type: documentation
  - resource:
      title: mysqlslap official website
      link: https://dev.mysql.com/doc/refman/8.4/en/mysqlslap.html
      type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

