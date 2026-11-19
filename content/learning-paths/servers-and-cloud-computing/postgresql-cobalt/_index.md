---
title: Deploy PostgreSQL on Azure Cobalt 200 Arm64 virtual machines

minutes_to_complete: 30

who_is_this_for: This learning path is designed for developers, DevOps engineers, and platform engineers who want to deploy, manage, and optimize PostgreSQL databases on Arm-based cloud infrastructure.

learning_objectives:
    - Install and configure PostgreSQL on Azure Cobalt 200 Arm64 virtual machines.
    - Deploy a relational database schema for transactional workloads.
    - Execute analytical SQL queries on operational data.
    - Benchmark PostgreSQL performance using pgbench.
    - Monitor and optimize query performance using built-in PostgreSQL tools.

prerequisites:
  - A [Microsoft Azure account](https://azure.microsoft.com/) with access to Cobalt 200-based instances (Dpsv7)
  - Basic knowledge of Linux command-line operations
  - Familiarity with SSH and remote server access
  - Basic understanding of databases and SQL

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-11-18T20:25:42Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: cea96a5447df4e23b499140de911456ca3c6b2fa72c62651ee9bc7dd329842bc
  summary_generated_at: '2026-11-18T20:25:42Z'
  summary_source_hash: cea96a5447df4e23b499140de911456ca3c6b2fa72c62651ee9bc7dd329842bc
  faq_generated_at: '2026-11-18T20:25:42Z'
  faq_source_hash: cea96a5447df4e23b499140de911456ca3c6b2fa72c62651ee9bc7dd329842bc
  summary: >-
    You'll deploy PostgreSQL on an Azure Cobalt 200-based VM and examine its performance. First, you'll
    create the VM, install PostgreSQL, and configure a database user. Then, you'll create tables,
    load sample data, and run analytical queries. Finally, you'll benchmark with `pgbench`, inspect
    statement statistics, add indexes, and compare query behavior after tuning.
  faqs:
  - question: Which Azure VM option should I use for this deployment?
    answer: >-
      Use the `Standard_D4ps_v7` VM in the Dpsv7 series on Azure Cobalt 200. 
  - question: How do I verify PostgreSQL is running after installation?
    answer: >-
      Connect locally using `psql` as the postgres superuser. If the `psql` prompt opens without
      errors, the service is running.
  - question: What result should I expect after creating the schema and loading data?
    answer: >-
      Check that your `customers` and `orders` tables contain the sample data, and that the
      analytical queries run without errors. Connect as the application user to validate access.
  - question: What does running pgbench initialization change in my database?
    answer: >-
      Run `pgbench` initialization to prepare its benchmark dataset. It recreates the
      `pgbench_*` tables in your target database. Leave `psql` with `\q` before running the
      command in the VM terminal.
  - question: How do I decide which indexes to add when tuning?
    answer: >-
      Use PostgreSQL built-in monitoring, such as `pg_stat_statements`, to identify statements that are high-latency or run frequently. Create indexes on relevant columns, then rerun the
      queries or `pgbench` to compare results.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

description: Deploy PostgreSQL on Azure Cobalt 200 Arm64 virtual machines, load a relational schema with transactional data, and benchmark and optimize query performance using pgbench and pg_stat_statements.

### Tags
skilllevels: Introductory
subjects: Databases
platforms:
  - Microsoft Azure Cobalt

armips:
    - Neoverse

tools_software_languages:
    - PostgreSQL
    - SQL
    - pgbench
    - Azure Cobalt 200

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
      title: Azure Cobalt 200 processors
      link: https://azure.microsoft.com/en-us/blog/new-azure-cobalt-200-vms-deliver-50-performance-improvement-fully-optimized-for-modern-agentic-ai-workloads/
      type: documentation
### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

