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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-30T21:46:38Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e77cd1373236f39f360afe6844d642fde290960ccdad26544ff1e3342f2a980c
  summary_generated_at: '2026-06-30T21:46:38Z'
  summary_source_hash: e77cd1373236f39f360afe6844d642fde290960ccdad26544ff1e3342f2a980c
  faq_generated_at: '2026-06-30T21:46:38Z'
  faq_source_hash: e77cd1373236f39f360afe6844d642fde290960ccdad26544ff1e3342f2a980c
  summary: >-
    You'll deploy ClickHouse on an Arm-based Google Cloud C4A virtual machine and assemble a streaming analytics pipeline. After exploring C4A (Neoverse-V2) instances, you'll provision a `c4a-standard-4` SUSE Linux VM, create
    a firewall rule to open TCP port 8123, and install ClickHouse alongside the Google Cloud CLI.
    Then, you'll set up Pub/Sub and required IAM so Apache Beam on Dataflow can stream events
    into ClickHouse. By the end, you'll validate end-to-end ingestion from Pub/Sub to ClickHouse and run
    baseline and analytical queries, capturing latency metrics (including p95) to evaluate ClickHouse
    behavior on Axion processors.
  faqs:
  - question: Which machine type should I choose for the VM in this path?
    answer: >-
      Select the `c4a-standard-4` machine type (4 vCPUs, 16 GB) in the Google Cloud console when
      creating the instance. This matches the configuration used in the steps.
  - question: Which firewall port needs to be opened for ClickHouse access?
    answer: >-
      Open inbound TCP port 8123 by creating a firewall rule in your VPC. This exposes the ClickHouse
      endpoint required by the path.
  - question: How do I verify Pub/Sub is ready before launching the pipeline?
    answer: >-
      Confirm that the logs-topic exists under **Pub/Sub → Topics** and keep encryption and retention
      at their defaults. Complete the IAM setup so Dataflow and the VM can access Pub/Sub.
  - question: Where should I install and use the Google Cloud CLI (gcloud) during this workflow?
    answer: >-
      Install the Arm64 Google Cloud CLI on the VM. Use it to authenticate
      to GCP, publish Pub/Sub messages, and submit Dataflow jobs.
  - question: What results should I record when validating and benchmarking ClickHouse?
    answer: >-
      Verify that events published to Pub/Sub arrive in ClickHouse and then run baseline and analytical
      queries. Capture query latency metrics, including p95.
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

