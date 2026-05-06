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

generate_summary_faq: true

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:58Z'
  generator: template
  source_hash: e473c0724855bbbc59481822130f7dc5e1684593527a6b5688939f84cd32963d
  summary: >-
    Benchmarking MySQL with Sysbench walks you through an end-to-end Arm software workflow. It
    is designed for performance engineers who want to benchmark MySQL using Sysbench and optimize
    performance on Arm Linux systems. By the end, you will be able to run Sysbench to benchmark
    a MySQL database server and enable profile-guided optimization (PGO) for MySQL and examine
    the performance improvements. It focuses on tools and technologies such as MySQL and Sysbench,
    Linux environments, Arm platforms including Neoverse, and cloud platforms such as AWS, Microsoft
    Azure, Google Cloud, and Oracle. The main steps cover Setup, configure, and run MySQL server,
    Build and run Sysbench, and Enable profile-guided optimization for MySQL.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will run Sysbench to benchmark a MySQL database server and enable profile-guided optimization
      (PGO) for MySQL and examine the performance improvements.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for performance engineers who want to benchmark MySQL using
      Sysbench and optimize performance on Arm Linux systems.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Basic knowledge of [MySQL databases](https://www.mysql.com/);
      Two Arm servers running Ubuntu 22.04, one for the MySQL server and the other for the Sysbench
      client.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including MySQL and Sysbench, Linux environments, Arm platforms
      such as Neoverse, and cloud platforms such as AWS, Microsoft Azure, Google Cloud, and Oracle.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Setup, configure, and run MySQL server, Build and
      run Sysbench, and Enable profile-guided optimization for MySQL.
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

