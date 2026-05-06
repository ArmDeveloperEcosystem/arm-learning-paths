---
title: Build a real-time analytics pipeline with ClickHouse on Google Cloud Axion
description: Learn how to deploy ClickHouse on Google Cloud Axion C4A processors and build a streaming ETL pipeline using Apache Beam, Dataflow, and Pub/Sub for real-time analytics.
    
minutes_to_complete: 50

who_is_this_for: This is an introductory topic for developers deploying and optimizing ClickHouse on Arm-based Linux environments using Google Cloud C4A virtual machines powered by Axion processors, to evaluate ClickHouse performance and behavior on Arm-based infrastructure.

learning_objectives:
  - Provision an Arm-based SUSE SLES virtual machine on Google Cloud using C4A (Axion processors)
  - Configure Google Cloud Pub/Sub for real-time log ingestion
  - Deploy and validate ClickHouse on a SUSE Linux Arm64 (Axion) VM
  - Build a streaming ETL pipeline using Apache Beam and Google Dataflow
  - Ingest real-time Pub/Sub data into ClickHouse using Dataflow
  - Validate end-to-end data flow from Pub/Sub to ClickHouse
  - Perform baseline and analytical query benchmarking on ClickHouse running on Arm64
  - Measure and report query latency (including p95) on Axion processors

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with [ClickHouse](https://clickhouse.com/)
  - Basic understanding of databases and SQL

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:57Z'
  generator: template
  source_hash: e77cd1373236f39f360afe6844d642fde290960ccdad26544ff1e3342f2a980c
  summary: >-
    Learn how to deploy ClickHouse on Google Cloud Axion C4A processors and build a streaming
    ETL pipeline using Apache Beam, Dataflow, and Pub/Sub for real-time analytics. It is designed
    for developers deploying and optimizing ClickHouse on Arm-based Linux environments using Google
    Cloud C4A virtual machines powered by Axion processors, to evaluate ClickHouse performance
    and behavior on Arm-based infrastructure. By the end, you will be able to provision an Arm-based
    SUSE SLES virtual machine on Google Cloud using C4A (Axion processors), configure Google Cloud
    Pub/Sub for real-time log ingestion, and deploy and validate ClickHouse on a SUSE Linux Arm64
    (Axion) VM. It focuses on tools and technologies such as ClickHouse, Apache Beam, Google Dataflow,
    Google Cloud Pub/Sub, and Python 3.11, Linux environments, Arm platforms including Neoverse,
    and cloud platforms such as Google Cloud. The main steps cover Get started with ClickHouse
    on Google Cloud C4A Arm virtual machines, Create a Firewall Rule on GCP, Create a Google Axion
    C4A Arm virtual machine on GCP, Set up GCP Pub/Sub and IAM for ClickHouse real-time analytics
    on Axion, and Install ClickHouse.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Arm-based SUSE SLES virtual machine on Google Cloud using C4A (Axion
      processors), configure Google Cloud Pub/Sub for real-time log ingestion, and deploy and
      validate ClickHouse on a SUSE Linux Arm64 (Axion) VM. Learn how to deploy ClickHouse on
      Google Cloud Axion C4A processors and build a streaming ETL pipeline using Apache Beam,
      Dataflow, and Pub/Sub for real-time analytics.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers deploying and optimizing ClickHouse on Arm-based
      Linux environments using Google Cloud C4A virtual machines powered by Axion processors,
      to evaluate ClickHouse performance and behavior on Arm-based infrastructure.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud Platform (GCP)](https://cloud.google.com/free)
      account with billing enabled; Basic familiarity with [ClickHouse](https://clickhouse.com/);
      Basic understanding of databases and SQL.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including ClickHouse, Apache Beam, Google Dataflow, Google
      Cloud Pub/Sub, and Python 3.11, Linux environments, Arm platforms such as Neoverse, and
      cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Get started with ClickHouse on Google Cloud C4A Arm
      virtual machines, Create a Firewall Rule on GCP, Create a Google Axion C4A Arm virtual machine
      on GCP, Set up GCP Pub/Sub and IAM for ClickHouse real-time analytics on Axion, and Install
      ClickHouse.
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
  - ClickHouse
  - Apache Beam
  - Google Dataflow
  - Google Cloud Pub/Sub
  - Python 3.11

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
      title: ClickHouse documentation
      link: https://clickhouse.com/docs/
      type: documentation

  - resource:
      title: ClickHouse benchmark documentation
      link: https://clickhouse.com/docs/operations/utilities/clickhouse-benchmark
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

