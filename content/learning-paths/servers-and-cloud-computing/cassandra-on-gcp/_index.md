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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-30T21:40:18Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b8268d4df3b62aeb9943b750b436a936134d47745fa71db6cc08db8c84eb37be
  summary_generated_at: '2026-06-30T21:40:18Z'
  summary_source_hash: b8268d4df3b62aeb9943b750b436a936134d47745fa71db6cc08db8c84eb37be
  faq_generated_at: '2026-06-30T21:40:18Z'
  faq_source_hash: b8268d4df3b62aeb9943b750b436a936134d47745fa71db6cc08db8c84eb37be
  summary: >-
    You'll deploy Apache Cassandra on Arm-based Google
    Cloud Axion C4A virtual machines and validating a working baseline before running simple workload
    tests. First, you'll create a `c4a-standard-4` instance in the Google Cloud console, install Cassandra
    on Ubuntu or SUSE, and satisfy the Java requirement. Then, you'll start Cassandra as a background
    service, with logs tailed to confirm “Startup complete,” followed by nodetool status to verify
    the node state. By the end, you'll benchmark using the built-in `cassandra-stress` utility
    to exercise write, read, and mixed operations on Arm64 to
    confirm Cassandra is operating correctly on Axion-based instances.
  faqs:
  - question: Which Google Cloud machine type should I choose for this setup?
    answer: >-
      Select the `c4a-standard-4` machine type (4 vCPUs, 16 GB memory) when creating the VM. This
      aligns with the example in the provisioning step.
  - question: How do I start Cassandra and confirm it is ready?
    answer: >-
      Start Cassandra with `cassandra -R` to run it in the background. Tail `~/cassandra/logs/system.log`
      and wait for the “Startup complete” message, then use `nodetool status` to check the node
      state.
  - question: What should I check in nodetool status before continuing?
    answer: >-
      Verify that `nodetool status` returns the node’s status and cluster information. Use this
      as a quick check that the service is responding before running any benchmarks.
  - question: Where is `cassandra-stress` located and how can I verify it’s installed?
    answer: >-
      `cassandra-stress` is in the tools/bin directory of your Cassandra installation. List the
      directory and confirm it appears, for example with `ls ~/cassandra/tools/bin | grep cassandra-stress`.
  - question: Which Java version does the installation use in this guide?
    answer: >-
      Cassandra requires a Java runtime. The example uses Java 17.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

