---
title: Deploy ClickHouse on Google Cloud C4A Arm virtual machines
    
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers deploying and optimizing ClickHouse on Arm-based Linux environments using Google Cloud C4A virtual machines powered by Axion processors, to evaluate ClickHouse performance and behaviour on Arm-based infrastructure.

learning_objectives:
  - Provision an Arm-based SUSE SLES virtual machine on Google Cloud using C4A instances powered by Axion processors
  - Install and start a ClickHouse server on a SUSE Arm64 (C4A) virtual machine
  - Verify ClickHouse functionality by connecting to the server and running basic insert and query operations
  - Run baseline ClickHouse performance tests to produce throughput and query latency results for evaluating Arm-based deployments on Google Cloud

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with [ClickHouse](https://clickhouse.com/)
  - An install guide on [how to get started with Google Cloud Platform](/install-guides/gcp/)

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
