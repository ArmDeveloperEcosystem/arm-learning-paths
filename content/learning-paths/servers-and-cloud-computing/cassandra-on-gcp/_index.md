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
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:28:19Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b8268d4df3b62aeb9943b750b436a936134d47745fa71db6cc08db8c84eb37be
  summary_generated_at: '2026-06-02T03:16:24Z'
  summary_source_hash: b8268d4df3b62aeb9943b750b436a936134d47745fa71db6cc08db8c84eb37be
  faq_generated_at: '2026-06-03T00:28:19Z'
  faq_source_hash: b8268d4df3b62aeb9943b750b436a936134d47745fa71db6cc08db8c84eb37be
  summary: >-
    Follow this introductory path to provision a Google Cloud Axion C4A Arm64 virtual machine,
    install Apache Cassandra with Java 17 on SUSE or Ubuntu, validate basic database operations,
    and benchmark read/write performance using cassandra-stress. You will create a C4A instance
    (the example uses c4a-standard-4), start Cassandra, confirm health via logs and nodetool,
    and use cqlsh for baseline keyspace/table operations before running cassandra-stress. This
    path targets developers moving Cassandra workloads to Arm on Google Cloud and takes about
    30 minutes. Prerequisites are a Google Cloud account with billing enabled and familiarity
    with Cassandra architecture, replication, and partitioning/event-driven I/O.
  faqs:
  - question: What do I need before provisioning the VM on Google Cloud?
    answer: >-
      You need a Google Cloud Platform account with billing enabled. Familiarity with Cassandra
      architecture, replication, and partitioning/event-driven I/O is expected.
  - question: Which Google Cloud machine type is used in this guide?
    answer: >-
      The steps use an Axion C4A instance with the c4a-standard-4 machine type (4 vCPUs, 16 GB
      memory) created from the Google Cloud Console.
  - question: Which Linux distributions does the installation cover?
    answer: >-
      The installation shows how to set up Cassandra on Ubuntu or SUSE Linux. The learning objectives
      emphasize SUSE on Arm64 (C4A).
  - question: How do I verify that Cassandra started correctly?
    answer: >-
      Start Cassandra in the background and check the system.log for the message “Startup complete.”
      Then run nodetool status to confirm the node is up before proceeding.
  - question: How do I confirm cassandra-stress is available and what does it test?
    answer: >-
      cassandra-stress is included in the Cassandra distribution under tools/bin; list that directory
      and check the tool’s help to confirm it’s present. It measures performance for write, read,
      and mixed workloads as used in this path.
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

