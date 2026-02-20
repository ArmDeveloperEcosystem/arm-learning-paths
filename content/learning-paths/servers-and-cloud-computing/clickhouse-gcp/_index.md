---
title: Build a real-time analytics pipeline with ClickHouse on Google Cloud Axion
    
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
