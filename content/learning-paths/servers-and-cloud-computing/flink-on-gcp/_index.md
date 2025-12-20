---
title: Deploy Apache Flink on Google Cloud C4A (Arm-based Axion VMs)
    
minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers deploying and optimizing Apache Flink workloads on Linux/Arm64 environments, specifically using Google Cloud C4A virtual machines powered by Axion processors.

learning_objectives:
  - Provision an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion processors)
  - Install and configure Apache Flink on an Arm64 instance
  - Validate Flink functionality by starting the cluster and running a baseline job
  - Benchmark Flink performance using JMH-based microbenchmarks

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with [Apache Flink](https://flink.apache.org/) and its runtime environment

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers: Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Flink
  - Java
  - Maven

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
      title: Flink documentation
      link: https://nightlies.apache.org/flink/flink-docs-lts/
      type: documentation

  - resource:
      title: Flink Performance Tool
      link: https://github.com/apache/flink-benchmarks/tree/master?tab=readme-ov-file#flink-benchmarks
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
