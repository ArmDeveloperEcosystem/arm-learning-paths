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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:35:55Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b9b2ed7f58611c9bc7e1867fe06700f3197eb095ddc62d91c00814021967cf72
  summary_generated_at: '2026-06-02T04:33:29Z'
  summary_source_hash: b9b2ed7f58611c9bc7e1867fe06700f3197eb095ddc62d91c00814021967cf72
  faq_generated_at: '2026-06-03T01:35:55Z'
  faq_source_hash: b9b2ed7f58611c9bc7e1867fe06700f3197eb095ddc62d91c00814021967cf72
  summary: >-
    This introductory Learning Path shows how to deploy MySQL on Arm-based Linux systems and interact
    with it using the MySQL client CLI. You will review common deployment options on Arm, including
    bare metal, cloud VMs, and managed SQL services from providers such as AWS, Microsoft Azure,
    Google Cloud, and Oracle. The practical steps focus on installing, configuring, and checking
    a MySQL instance, then running basic interactions from a CLI. Prerequisites include access
    to an Arm-based instance from a cloud service provider or an on-premise Arm server; if you
    do not have one, the path discusses options. Estimated time to complete is about 30 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need access to a Linux system on an Arm-based instance from a cloud provider or an on‑premise
      Arm server. No other explicit prerequisites are listed.
  - question: I don’t have an Arm node—what should I do?
    answer: >-
      The path discusses options to obtain Arm capacity, including Arm Cloud VMs and a separate
      learning path for getting started with Arm-based cloud instances. Cloud providers referenced
      include AWS, Microsoft Azure, Google Cloud, and Oracle.
  - question: Which deployment approach should I choose for MySQL on Arm?
    answer: >-
      This path introduces multiple options: bare metal, cloud VMs, and cloud providers’ SQL services.
      Choose based on your available infrastructure and whether you prefer managing MySQL yourself
      or using a managed service.
  - question: How do I know the installation worked?
    answer: >-
      The steps include checking the installation and interacting with the database using the
      MySQL client CLI tool. You should be able to connect and run simple SQL commands to validate
      the deployment.
  - question: Does this path cover performance tuning?
    answer: >-
      No. If you already know how to deploy MySQL and want to focus on performance, follow the
      separate “Learn how to Tune MySQL” learning path.
# END generated_summary_faq

author: Jason Andrews
### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
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

