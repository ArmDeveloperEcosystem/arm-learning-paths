---
title: Benchmarking MySQL with Sysbench

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for performance engineers who want to benchmark MySQL using Sysbench and optimize performance on Arm Linux systems.

learning_objectives:
    - Run Sysbench to benchmark a MySQL database server
    - Enable profile-guided optimization (PGO) for MySQL and examine the performance improvements

prerequisites:
    - Basic knowledge of [MySQL databases](https://www.mysql.com/)
    - Two Arm servers running Ubuntu 22.04, one for the MySQL server and the other for the Sysbench client

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-01T19:38:09Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 5fc0ba5fb5befc9ae9ba54e8d7734e5673c2e7a5b5c1eee6e6cdb181cad2de48
  summary_generated_at: '2026-10-01T19:38:09Z'
  summary_source_hash: 5fc0ba5fb5befc9ae9ba54e8d7734e5673c2e7a5b5c1eee6e6cdb181cad2de48
  faq_generated_at: '2026-10-01T19:38:09Z'
  faq_source_hash: 5fc0ba5fb5befc9ae9ba54e8d7734e5673c2e7a5b5c1eee6e6cdb181cad2de48
  summary: >-
    Build MySQL from source on an Arm Ubuntu 22.04 server and benchmark it from a second Arm Linux
    system. You configure the server, build `sysbench` with the required MySQL client libraries,
    and run baseline workloads. You then rebuild MySQL with GCC profile-guided optimization (PGO),
    first collecting profile data and then applying it. Finally, you repeat the workloads and
    compare the results with your baseline.
  faqs:
  - question: Can I use a different Linux distribution than Ubuntu 22.04 for this setup?
    answer: >-
      The instructions use Ubuntu 22.04 and note that other Linux distributions and Ubuntu versions
      might also work. If you use a different OS, expect to adapt package installation commands to
      match your environment.
  - question: Why do I need to build and install MySQL on the Sysbench client?
    answer: >-
      `sysbench` needs MySQL client libraries to build and run its MySQL tests. You only build
      and install MySQL on the client to provide these libraries; you do not configure or run
      the MySQL server on the client.
  - question: How much disk space do I need on the server and client?
    answer: >-
      Allocate at least 200 GB of disk space on the MySQL server system. Allocate at least 30
      GB on the Sysbench client system.
  - question: Which compiler should I use for PGO, and what builds does the process create?
    answer: >-
      The PGO section uses GCC. You create two additional MySQL installations: one built with
      profile generation to collect data and another rebuilt with profile use to apply that data.
  - question: How do I confirm that PGO changed performance?
    answer: >-
      Run the same `sysbench` workload on the baseline and profile-use builds, then compare their
      results. Keep the workload and environment consistent so the comparison is meaningful.
# END generated_summary_faq

author: Bolt Liu

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
    - MySQL
    - Sysbench

test_images:
    - ubuntu:22.04
test_link: null
test_maintenance: false

further_reading:
    - resource:
        title: MySQL documentation
        link: https://www.mysql.com/
        type: documentation
    - resource:
        title: Running MySQL on ARM
        link: https://mysqlonarm.github.io/Running-MySQL-on-ARM/
        type: documentation
    - resource:
        title: Learn how to deploy MySQL
        link: /learning-paths/servers-and-cloud-computing/mysql/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: learningpathall
learning_path_main_page: 'yes'
---
