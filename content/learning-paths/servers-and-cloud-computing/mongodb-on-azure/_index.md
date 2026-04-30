---
title: Run MongoDB on Arm-based Azure Cobalt 100 instances

minutes_to_complete: 30   

who_is_this_for: This is an introductory topic for software developers who want to migrate MongoDB workloads to Arm-based platforms, with a focus on Microsoft Azure Cobalt 100 Arm64 instances.

description: Deploy MongoDB on Azure Cobalt 100 Arm virtual machines and benchmark database performance using mongotop and mongostat monitoring tools.

learning_objectives: 
    - Provision an Arm64-based Cobalt 100 virtual machine in Azure using Ubuntu Pro 24.04 LTS
    - Deploy MongoDB on the Cobalt 100 instance
    - Run baseline tests and performance benchmarks on MongoDB in the Arm64 environment

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 (Dpsv6) instances
    - Familiarity with the [MongoDB architecture](https://www.mongodb.com/) and deployment practices on Arm64 platforms

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:18Z'
  generator: template
  source_hash: f270cfc90245c0090685fabf5cbebf62a714edbf34e1ea86c3df0bfbb4699ea4
  summary: >-
    Deploy MongoDB on Azure Cobalt 100 Arm virtual machines and benchmark database performance
    using mongotop and mongostat monitoring tools. It is designed for software developers who
    want to migrate MongoDB workloads to Arm-based platforms, with a focus on Microsoft Azure
    Cobalt 100 Arm64 instances. By the end, you will be able to provision an Arm64-based Cobalt
    100 virtual machine in Azure using Ubuntu Pro 24.04 LTS, deploy MongoDB on the Cobalt 100
    instance, and run baseline tests and performance benchmarks on MongoDB in the Arm64 environment.
    It focuses on tools and technologies such as MongoDB, mongotop, and mongostat, Linux environments,
    Arm platforms including Neoverse, and cloud platforms such as Microsoft Azure. The main steps
    cover What are Cobalt 100 and MongoDB?, Create an Arm-based cloud virtual machine using Cobalt
    100, Install MongoDB and Mongosh, MongoDB Baseline Testing, and Monitor MongoDB with mongotop.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Arm64-based Cobalt 100 virtual machine in Azure using Ubuntu Pro 24.04
      LTS, deploy MongoDB on the Cobalt 100 instance, and run baseline tests and performance benchmarks
      on MongoDB in the Arm64 environment. Deploy MongoDB on Azure Cobalt 100 Arm virtual machines
      and benchmark database performance using mongotop and mongostat monitoring tools.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for software developers who want to migrate MongoDB workloads
      to Arm-based platforms, with a focus on Microsoft Azure Cobalt 100 Arm64 instances.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Microsoft Azure](https://azure.microsoft.com/)
      account with access to Cobalt 100 (Dpsv6) instances; Familiarity with the [MongoDB architecture](https://www.mongodb.com/)
      and deployment practices on Arm64 platforms.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including MongoDB, mongotop, and mongostat, Linux environments,
      Arm platforms such as Neoverse, and cloud platforms such as Microsoft Azure.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around What are Cobalt 100 and MongoDB?, Create an Arm-based
      cloud virtual machine using Cobalt 100, Install MongoDB and Mongosh, MongoDB Baseline Testing,
      and Monitor MongoDB with mongotop.
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
    - MongoDB
    - mongotop
    - mongostat

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: MongoDB Manual
        link: https://www.mongodb.com/docs/manual/
        type: documentation
    - resource:
        title: MongoDB Performance Tool
        link: https://github.com/idealo/mongodb-performance-test#readme
        type: documentation
    - resource:        
        title: MongoDB on Azure
        link: https://azure.microsoft.com/en-us/solutions/mongodb
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

