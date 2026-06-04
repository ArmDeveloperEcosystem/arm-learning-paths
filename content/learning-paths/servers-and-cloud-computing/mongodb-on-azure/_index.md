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

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:33:04Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f270cfc90245c0090685fabf5cbebf62a714edbf34e1ea86c3df0bfbb4699ea4
  summary_generated_at: '2026-06-02T04:28:12Z'
  summary_source_hash: f270cfc90245c0090685fabf5cbebf62a714edbf34e1ea86c3df0bfbb4699ea4
  faq_generated_at: '2026-06-03T01:33:04Z'
  faq_source_hash: f270cfc90245c0090685fabf5cbebf62a714edbf34e1ea86c3df0bfbb4699ea4
  summary: >-
    This Learning Path shows how to run MongoDB on Arm-based Microsoft Azure Cobalt 100 virtual
    machines. You will provision a Dpsv6 instance using the Azure console with Ubuntu Pro 24.04
    LTS (Arm64), install MongoDB and mongosh, and validate the deployment. The steps include baseline
    checks such as service health, a quick storage test with fio, and CRUD verification, followed
    by monitoring database activity with mongotop and using mongostat for additional runtime metrics.
    By the end, you will have a working MongoDB setup on Cobalt 100 and initial observations from
    light benchmarking on Arm64. Prerequisites are an Azure account with access to Cobalt 100
    and familiarity with MongoDB architecture and Arm64 deployments.
  faqs:
  - question: What do I need before creating the Azure VM?
    answer: >-
      You need a Microsoft Azure account with access to Cobalt 100 (Dpsv6) instances. Familiarity
      with MongoDB architecture and deployment practices on Arm64 platforms is also expected.
  - question: Which Azure VM series and OS image should I select?
    answer: >-
      Use the Dpsv6 general-purpose series for the Arm-based Cobalt 100 processor. The path targets
      Ubuntu Pro 24.04 LTS (Arm64).
  - question: How do I verify that MongoDB was installed and is working?
    answer: >-
      Start mongod locally, check service health, and connect with mongosh to validate CRUD operations.
      Run a quick storage baseline with fio and perform light query, index, and concurrency checks.
  - question: How is access control handled during the exercises and how can I enable remote access
      later?
    answer: >-
      For this exercise, access control is disabled by default and mongod should remain bound
      to 127.0.0.1. To accept remote connections later, set --bind_ip (or bindIp in the config)
      and enable authorization.
  - question: How do I monitor MongoDB activity and what should be running first?
    answer: >-
      Use mongotop (and mongostat) to observe real-time activity, ensuring mongod is running locally
      and that the long_system_load.js script is generating traffic. The path includes benchmark
      results from Azure Arm64 VMs as a latency reference.
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

