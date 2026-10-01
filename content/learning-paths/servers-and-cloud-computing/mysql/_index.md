---
title: Learn how to deploy MySQL

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers who want to deploy MySQL on Arm.

learning_objectives: 
    - Learn about the various ways MySQL can be deployed.
    - Learn how to interact with a MySQL database using a MySQL client CLI tool.

prerequisites:
    - An Arm based instance from a cloud service provider, or an on-premise Arm server.
    - If you do not have an Arm node, the next section discusses some options.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-01T19:37:38Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 743cde2f666e32bdd9dd2c412037696d36fbe12c5d89d854b04102d9a74a05ec
  summary_generated_at: '2026-10-01T19:37:38Z'
  summary_source_hash: 743cde2f666e32bdd9dd2c412037696d36fbe12c5d89d854b04102d9a74a05ec
  faq_generated_at: '2026-10-01T19:37:38Z'
  faq_source_hash: 743cde2f666e32bdd9dd2c412037696d36fbe12c5d89d854b04102d9a74a05ec
  summary: >-
    Deploy MySQL on an Arm-based Linux system and verify that the database is ready to use. You
    review deployment options for bare-metal systems, cloud virtual machines, and managed SQL
    services before choosing an environment. You then follow the MySQL documentation to install
    and configure the server, connect with the MySQL client, and run basic SQL commands. A separate
    Learning Path covers performance tuning.
  faqs:
  - question: I already know how to deploy MySQL. Should I skip to the tuning content?
    answer: >-
      Yes. If you already know how to deploy a MySQL database, continue to the MySQL tuning Learning
      Path to improve the performance of an Arm-based MySQL server.
  - question: I already have an Arm server. Which deployment option should I use?
    answer: >-
      Use your existing Arm system and continue with the installation and check steps. You can
      skip the deployment options subsection; bare metal or an existing Arm-based VM both work.
  - question: What result should I expect after I install and check MySQL?
    answer: >-
      You should have a running MySQL server on an Arm-based Linux system. A successful connection
      with the MySQL client and the ability to issue basic SQL statements indicate that the setup
      is working.
  - question: Can I use a managed SQL service instead of installing MySQL myself?
    answer: >-
      Yes, managed SQL services on Arm are listed as deployment options. However, the hands-on
      hands-on verification assumes that you control an Arm instance where you install MySQL and
      interact with the command-line client.
  - question: I don’t have an Arm node. Where should I start?
    answer: >-
      Use one of the cloud options described in the deployment section, or see the Get started
      with Arm-based cloud instances Learning Path. Provision an Arm environment before you install
      MySQL.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Databases
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - SQL
    - MySQL

further_reading:
    - resource:
        title: MySQL Manual
        link: https://dev.mysql.com/doc/refman/8.0/en/installing.html
        type: documentation
    - resource:
        title: RDS
        link: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_GettingStarted.CreatingConnecting.MySQL.html
        type: documentation
    - resource:
        title: Ansible
        link: https://docs.ansible.com/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
