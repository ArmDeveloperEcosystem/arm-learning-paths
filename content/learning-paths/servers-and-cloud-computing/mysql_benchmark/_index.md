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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:37:09Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e473c0724855bbbc59481822130f7dc5e1684593527a6b5688939f84cd32963d
  summary_generated_at: '2026-06-02T04:34:09Z'
  summary_source_hash: e473c0724855bbbc59481822130f7dc5e1684593527a6b5688939f84cd32963d
  faq_generated_at: '2026-06-03T01:37:09Z'
  faq_source_hash: e473c0724855bbbc59481822130f7dc5e1684593527a6b5688939f84cd32963d
  summary: >-
    This Learning Path shows how to benchmark MySQL on Arm Linux using Sysbench and apply profile-guided
    optimization (PGO) with GCC. You will build, configure, and run a MySQL server on one Arm
    server running Ubuntu 22.04, then build and run Sysbench on a second Arm Linux system. On
    the client, you also build and install MySQL to provide the libraries required by Sysbench.
    You will run Sysbench against the server, rebuild MySQL to generate and then use profile data,
    and examine the resulting performance changes. Prerequisites include basic MySQL knowledge
    and access to two Arm servers (200 GB disk on the server, 30 GB on the client).
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need two Arm servers running Ubuntu 22.04: one for the MySQL server and one for the
      Sysbench client. Ensure at least 200 GB of free disk space on the server and 30 GB on the
      client. Basic knowledge of MySQL is also required.
  - question: Which packages should I install to build MySQL on Ubuntu 22.04?
    answer: >-
      Install: git, make, automake, libtool, bison, pkg-config, cmake, g++, openssl, libssl-dev,
      libncurses5-dev, libtirpc-dev, rpcsvc-proto, libaio-dev, libssl-dev. These packages are
      used to build, install, and run the MySQL server from source.
  - question: Why do I need to build MySQL on the Sysbench client as well?
    answer: >-
      Sysbench requires MySQL libraries to build and run the MySQL tests. On the client system
      you only build and install MySQL to provide these libraries; you do not configure or run
      the MySQL server there.
  - question: Can I use a different Linux distribution or Ubuntu version?
    answer: >-
      The steps assume Ubuntu 22.04 on Arm, but other Linux distributions and Ubuntu versions
      may also work. The path does not list specific adjustments for other distributions.
  - question: How is PGO applied to MySQL in this path, and which compiler is used?
    answer: >-
      The path uses GCC to apply PGO: first rebuild MySQL with profile generation to collect data,
      then rebuild with profile use to apply the collected profiles. The initial installation
      referenced is at /home/mysql/mysql_install_8.0.33, and the PGO workflow creates two additional
      installations (one for profile collection and one for profile use).
# END generated_summary_faq

author: Bolt Liu

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

