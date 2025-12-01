---
title: Deploy ClickHouse on Google Cloud C4A (Arm-based Axion VMs)

minutes_to_complete: 30

who_is_this_for: This learning path is intended for software developers deploying and optimizing ClickHouse on Linux/Arm64 environments, specifically using Google Cloud C4A virtual machines powered by Axion processors.

learning_objectives:
  - Provision an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion processors)
  - Install ClickHouse on a SUSE Arm64 (C4A) instance
  - Verify ClickHouse functionality by starting the server, connecting via client, and performing baseline data insertion and simple query tests on the Arm64 VM
  - Measure ClickHouse query performance (read, aggregation, and concurrent workloads) to evaluate throughput and latency on Arm64 (Aarch64)

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with [ClickHouse](https://clickhouse.com/)
author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Databases
cloud_service_providers: Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - ClickHouse
  - clickhouse-benchmark

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
