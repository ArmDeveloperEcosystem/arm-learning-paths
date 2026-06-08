---
title: Deploy PostgreSQL on Azure Cobalt 100 Arm64 virtual machines

minutes_to_complete: 30

who_is_this_for: This learning path is designed for developers, DevOps engineers, and platform engineers who want to deploy, manage, and optimize PostgreSQL databases on Arm-based cloud infrastructure.

learning_objectives:
    - Install and configure PostgreSQL on Azure Cobalt 100 Arm64 virtual machines
    - Deploy a relational database schema for transactional workloads
    - Execute analytical SQL queries on operational data
    - Benchmark PostgreSQL performance using pgbench
    - Monitor and optimize query performance using built-in PostgreSQL tools

prerequisites:
  - A [Microsoft Azure account](https://azure.microsoft.com/) with access to Cobalt 100 based instances (Dpsv6)
  - Basic knowledge of Linux command-line operations
  - Familiarity with SSH and remote server access
  - Basic understanding of databases and SQL

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:52:07Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 57827f45473867b3b5039a9cbca04d2c6d8a93e177ca0ab053999517389014b5
  summary_generated_at: '2026-06-02T04:48:52Z'
  summary_source_hash: 57827f45473867b3b5039a9cbca04d2c6d8a93e177ca0ab053999517389014b5
  faq_generated_at: '2026-06-03T01:52:07Z'
  faq_source_hash: 57827f45473867b3b5039a9cbca04d2c6d8a93e177ca0ab053999517389014b5
  summary: >-
    Deploy PostgreSQL on Arm-based Microsoft Azure Cobalt 100 virtual machines and validate it
    for transactional and analytical workloads in about 30 minutes. You will provision a Dpsv6
    VM, install PostgreSQL on Ubuntu 24.04 Pro Arm64, configure the service for remote access,
    and load a relational schema with transactional data. The path then runs analytical SQL queries,
    benchmarks using pgbench, and monitors query execution with built-in PostgreSQL tools such
    as pg_stat_statements. You will also add indexes and apply basic tuning for better query execution
    on Arm. Prerequisites include an Azure account with access to Cobalt 100 instances, basic
    Linux CLI skills, SSH familiarity, and a basic understanding of databases and SQL.
  faqs:
  - question: What do I need in Azure before creating the VM?
    answer: >-
      You need a Microsoft Azure account with access to Cobalt 100-based instances (Dpsv6). The
      path also assumes basic Linux, SSH, and SQL knowledge.
  - question: Which option should I use to provision the Cobalt 100 VM?
    answer: >-
      The path walks through creating the VM in the Azure Portal and targets general-purpose Dpsv6
      instances. You can also use the Azure CLI or an IaC tool, but the instructions focus on
      the Portal workflow.
  - question: How do I confirm PostgreSQL is installed and ready for connections?
    answer: >-
      At the end of the installation section, PostgreSQL is installed, running as a service, configured
      for remote access, and ready for application workloads. You can verify by connecting as
      the postgres user to the appdb database.
  - question: What schema and data are created before running queries?
    answer: >-
      The path creates a relational schema with two tables to simulate a transactional application
      and loads sample transactional data. You work in the appdb database and then run analytical
      SQL queries using the application user.
  - question: What should I expect after running the pgbench initialization, and how do I monitor
      queries?
    answer: >-
      Running pgbench -i -s 50 appdb creates standard benchmarking tables and loads data for testing,
      with output indicating the initialization steps. For monitoring and tuning, you use PostgreSQL
      built-in extensions such as pg_stat_statements and apply indexing techniques described in
      the path.
# END generated_summary_faq

author: Pareena Verma

description: Deploy PostgreSQL on Azure Cobalt 100 Arm64 virtual machines, load a relational schema with transactional data, and benchmark and optimize query performance using pgbench and pg_stat_statements.

### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - PostgreSQL
    - SQL
    - pgbench

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: PostgreSQL Official Website
      link: https://www.postgresql.org
      type: website
  - resource:
      title: PostgreSQL Documentation
      link: https://www.postgresql.org/docs/
      type: documentation
  - resource:
      title: pgbench Benchmarking Tool
      link: https://www.postgresql.org/docs/current/pgbench.html
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

