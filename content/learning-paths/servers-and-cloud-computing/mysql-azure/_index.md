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

generate_summary_faq: true

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:58Z'
  generator: template
  source_hash: b9bc1d1f965e4fdeeb9552d853330c201e00597829420c8a0397fa425c3231c4
  summary: >-
    Deploy MySQL on Microsoft Azure Cobalt 100 processors walks you through an end-to-end Arm
    software workflow. It is designed for developers migrating MySQL applications from x86_64
    to Arm. By the end, you will be able to provision an Azure Arm64 virtual machine using Azure
    console, with Ubuntu Pro 24.04 LTS as the base image, deploy MySQL on the Ubuntu virtual machine,
    and perform MySQL baseline testing and benchmarking on Arm64 virtual machines. It focuses
    on tools and technologies such as MySQL, SQL, and Docker, Linux environments, Arm platforms
    including Neoverse, and cloud platforms such as Microsoft Azure. The main steps cover Overview,
    Create an Azure Cobalt 100 Arm64 virtual machine, Deploy MySQL on an Azure Arm64 virtual machine,
    Validate MySQL functionality on Azure Arm64, and Benchmark MySQL with mysqlslap.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Azure Arm64 virtual machine using Azure console, with Ubuntu Pro 24.04
      LTS as the base image, deploy MySQL on the Ubuntu virtual machine, and perform MySQL baseline
      testing and benchmarking on Arm64 virtual machines.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers migrating MySQL applications from x86_64 to
      Arm.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Microsoft Azure](https://azure.microsoft.com/)
      account with access to Cobalt 100 based instances (Dpsv6); Familiarity with relational databases
      and the basics of [MySQL](https://dev.mysql.com/doc/refman/8.0/en/introduction.html).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including MySQL, SQL, and Docker, Linux environments, Arm
      platforms such as Neoverse, and cloud platforms such as Microsoft Azure.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Overview, Create an Azure Cobalt 100 Arm64 virtual
      machine, Deploy MySQL on an Azure Arm64 virtual machine, Validate MySQL functionality on
      Azure Arm64, and Benchmark MySQL with mysqlslap.
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

