---
title: Run Apache Spark SQL workloads on Azure Cobalt 100 Arm64 using Gluten and Velox for accelerated analytics

draft: true
cascade:
    draft: true

minutes_to_complete: 120

who_is_this_for: This is an intermediate topic for data engineers, platform engineers, and developers who want to build and optimize high-performance Spark SQL workloads using native execution engines on Arm-based cloud environments.

learning_objectives:
  - Install and configure Hadoop, Spark, and Hive on Azure Cobalt 100 Arm64 virtual machines
  - Build and integrate Gluten with the Velox backend for native query execution
  - Configure Spark SQL for columnar and vectorized execution
  - Generate and load TPC-DS datasets for benchmarking
  - Run Spark SQL workloads and compare performance between vanilla Spark and Gluten + Velox

prerequisites:
  - A [Microsoft Azure account](https://azure.microsoft.com/) with access to Cobalt 100 based instances (Dpsv6)
  - Basic knowledge of Linux command-line operations
  - Familiarity with SSH and remote server access
  - Basic understanding of distributed systems and Apache Spark

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
  - Apache Spark
  - Hadoop
  - Hive
  - Gluten
  - Velox


operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Apache Spark Documentation
      link: https://spark.apache.org/docs/latest/
      type: documentation
  - resource:
      title: Gluten Project (Apache Incubator)
      link: https://github.com/apache/incubator-gluten
      type: documentation
  - resource:
      title: Velox Execution Engine
      link: https://github.com/facebookincubator/velox
      type: documentation
  - resource:
      title: TPC-DS Benchmark Overview
      link: https://www.tpc.org/tpcds/
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
