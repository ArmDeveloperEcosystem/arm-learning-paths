---
title: Deploy Cassandra on a Google Axion C4A virtual machine
description: Learn how to install and configure Apache Cassandra on Google Cloud Axion C4A Arm64 instances and benchmark read/write performance using cassandra-stress.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers migrating Cassandra workloads from x86_64 to Arm-based servers, specifically on Google Cloud C4A virtual machines built on Axion processors.


learning_objectives:
  - Provision an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion processors)
  - Install and configure Apache Cassandra on a SUSE Arm64 (C4A) instance
  - Validate Cassandra functionality using CQLSH and baseline keyspace/table operations
  - Benchmark Cassandra performance using cassandra-stress for read and write workloads on Arm64 (Aarch64) architecture

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Familiarity with Cassandra architecture, replication, and [Cassandra partitioning and event-driven I/O](https://cassandra.apache.org/doc/stable/cassandra/architecture/)

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:56Z'
  generator: template
  source_hash: b8268d4df3b62aeb9943b750b436a936134d47745fa71db6cc08db8c84eb37be
  summary: >-
    Learn how to install and configure Apache Cassandra on Google Cloud Axion C4A Arm64 instances
    and benchmark read/write performance using cassandra-stress. It is designed for software developers
    migrating Cassandra workloads from x86_64 to Arm-based servers, specifically on Google Cloud
    C4A virtual machines built on Axion processors. By the end, you will be able to provision
    an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion processors), install
    and configure Apache Cassandra on a SUSE Arm64 (C4A) instance, and validate Cassandra functionality
    using CQLSH and baseline keyspace/table operations. It focuses on tools and technologies such
    as Apache Cassandra, Java, cqlsh, and cassandra-stress, Linux environments, Arm platforms
    including Neoverse, and cloud platforms such as Google Cloud. The main steps cover Get started
    with Cassandra on Google Axion C4A, Create a Google Axion C4A Arm virtual machine, Install
    Apache Cassandra, Test Cassandra baseline functionality, and Benchmark Cassandra performance.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion
      processors), install and configure Apache Cassandra on a SUSE Arm64 (C4A) instance, and
      validate Cassandra functionality using CQLSH and baseline keyspace/table operations. Learn
      how to install and configure Apache Cassandra on Google Cloud Axion C4A Arm64 instances
      and benchmark read/write performance using cassandra-stress.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for software developers migrating Cassandra workloads from
      x86_64 to Arm-based servers, specifically on Google Cloud C4A virtual machines built on
      Axion processors.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud Platform (GCP)](https://cloud.google.com/free)
      account with billing enabled; Familiarity with Cassandra architecture, replication, and
      [Cassandra partitioning and event-driven I/O](https://cassandra.apache.org/doc/stable/cassandra/architecture/).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Apache Cassandra, Java, cqlsh, and cassandra-stress,
      Linux environments, Arm platforms such as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Get started with Cassandra on Google Axion C4A, Create
      a Google Axion C4A Arm virtual machine, Install Apache Cassandra, Test Cassandra baseline
      functionality, and Benchmark Cassandra performance.
# END generated_summary_faq

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers:
  - Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Apache Cassandra
  - Java
  - cqlsh
  - cassandra-stress

operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
  - resource:
      title: Google Cloud documentation
      link: https://cloud.google.com/docs
      type: documentation

  - resource:
      title: Apache Cassandra documentation
      link: https://cassandra.apache.org/doc/latest/
      type: documentation

  - resource:
      title: Cassandra-stress documentation
      link: https://cassandra.apache.org/doc/4.0/cassandra/tools/cassandra_stress.html
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

