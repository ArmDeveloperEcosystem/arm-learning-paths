---
title: Deploy MySQL on Microsoft Azure Cobalt 100 processors

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers migrating MySQL applications from x86_64 to Arm.

learning_objectives:
    - Provision an Azure Arm64 virtual machine (VM) using the console, with Ubuntu Pro 24.04 LTS as the base image.
    - Deploy MySQL on the Ubuntu VM.
    - Perform MySQL baseline testing and benchmarking on Arm64 VMs.

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6)
    - Familiarity with relational databases and the basics of [MySQL](https://dev.mysql.com/doc/refman/8.0/en/introduction.html)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-01T19:36:26Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2a34346f8cd7954362d479429942c9b66c863f4470d3e7cdf49efbc6093c54cd
  summary_generated_at: '2026-10-01T19:36:26Z'
  summary_source_hash: 2a34346f8cd7954362d479429942c9b66c863f4470d3e7cdf49efbc6093c54cd
  faq_generated_at: '2026-10-01T19:36:26Z'
  faq_source_hash: 2a34346f8cd7954362d479429942c9b66c863f4470d3e7cdf49efbc6093c54cd
  summary: >-
    You'll deploy MySQL on an Arm64 Azure virtual machine powered by Cobalt 100, and establish a performance baseline.
    First, you'll provision an Ubuntu Pro 24.04 LTS Dpsv6 VM in the Azure portal, then install, secure,
    and validate MySQL. After creating sample data, you'll use `mysqlslap` to run read and write
    benchmarks. You'll interpret the reported timings, and capture results that you can use in later
    comparisons.
  faqs:
  - question: Which Azure VM size and image should I select?
    answer: >-
      Use a general-purpose Dpsv6 series instance based on Azure Cobalt 100, and choose Ubuntu
      Pro 24.04 LTS as the base image.
  - question: What do I need to connect to the VM after deployment?
    answer: >-
      Use the private SSH key that you downloaded when you created the VM, along with the administrator
      username and the VM's public IP address.
  - question: How do I confirm that MySQL is running before moving on?
    answer: >-
      Start MySQL and enable it to start on boot using the provided `systemctl` commands. Then, perform
      the functional validation to confirm queries run and users can authenticate.
  - question: What does mysql_secure_installation help me configure?
    answer: >-
      The interactive script helps you set a strong root password and remove anonymous users. It also helps disable
      remote root access, remove test databases, and reload the privilege tables.
  - question: What should I do before running mysqlslap, and what output should I expect?
    answer: >-
      Connect to MySQL and create the sample database and table before benchmarking. `mysqlslap`
      simulates multiple clients and reports timing statistics that you can use as your baseline.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Databases
platforms:
  - Microsoft Azure Cobalt

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
