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

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:34:45Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e77cd1373236f39f360afe6844d642fde290960ccdad26544ff1e3342f2a980c
  summary_generated_at: '2026-06-02T03:24:37Z'
  summary_source_hash: e77cd1373236f39f360afe6844d642fde290960ccdad26544ff1e3342f2a980c
  faq_generated_at: '2026-06-03T00:34:45Z'
  faq_source_hash: e77cd1373236f39f360afe6844d642fde290960ccdad26544ff1e3342f2a980c
  summary: >-
    Follow this introductory Learning Path to deploy ClickHouse on Arm-based Google Cloud Axion
    C4A virtual machines and build a real-time analytics pipeline. You will provision a SUSE Linux
    (Arm64) VM using the c4a-standard-4 type, configure a firewall rule for TCP 8123, and install
    ClickHouse and the Google Cloud CLI. You will create Pub/Sub resources (including a logs-topic)
    and IAM roles, then implement a streaming ETL with Apache Beam and run it on Google Dataflow
    to ingest events into ClickHouse. Finally, you will validate end-to-end ingestion and run
    baseline and analytical queries to measure and report latency, including p95, on Axion processors.
    Prerequisites are a GCP account with billing enabled and basic familiarity with ClickHouse
    and SQL.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Google Cloud Platform account with billing enabled. Basic familiarity with ClickHouse
      and a basic understanding of databases and SQL are also listed.
  - question: Which VM type and OS should I use on Google Cloud?
    answer: >-
      Use a Google Axion C4A instance with the c4a-standard-4 machine type (4 vCPUs, 16 GB memory).
      The VM runs SUSE SLES on Arm64.
  - question: Which network port must be opened for this setup?
    answer: >-
      Create a VPC firewall rule to allow inbound TCP traffic on port 8123. The steps guide you
      through doing this in the Google Cloud Console.
  - question: How should I configure Pub/Sub for ingestion?
    answer: >-
      Create a Pub/Sub topic named logs-topic using default settings. The path also covers setting
      up the required IAM so Dataflow and the VM can communicate with Pub/Sub.
  - question: What outcome should I expect after deployment and configuration?
    answer: >-
      You will ingest real-time data from Pub/Sub into ClickHouse using Dataflow and validate
      end-to-end data flow. You will also run baseline and analytical query benchmarks and measure
      query latency, including p95, on Axion processors.
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

