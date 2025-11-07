---
title: Deploy Apache Flink on Google Cloud C4A (Arm-based Axion VMs)

draft: true
cascade:
    draft: true
    
minutes_to_complete: 30

who_is_this_for: This learning path is intended for software developers deploying and optimizing Apache Flink workloads on Linux/Arm64 environments, specifically using Google Cloud C4A virtual machines powered by Axion processors.

learning_objectives:
  - Provision an Arm-based SUSE SLES virtual machine on Google Cloud (C4A with Axion processors)
  - Install Apache Flink on a SUSE Arm64 (C4A) instance
  - Validate Flink functionality by starting the Flink cluster and running a simple baseline job (e.g., WordCount) on the Arm64 VM
  - Benchmark Flink performance using internal JMH-based micro-benchmarks on Arm64 (Aarch64) architecture

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with [Apache Flink](https://flink.apache.org/) and its runtime environment

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Databases
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
      link:  https://nightlies.apache.org/flink/flink-docs-lts/
      type: documentation

  - resource:
      title: Flink Performance Tool
      link: https://github.com/apache/flink-benchmarks/tree/master?tab=readme-ov-file#flink-benchmarks
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
