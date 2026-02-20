---
title: Run Spark applications on Microsoft Azure Cobalt 100 processors

minutes_to_complete: 60

who_is_this_for: This is an advanced topic that introduces Spark deployment on Microsoft Azure Cobalt 100 (Arm-based) virtual machines. It is designed for developers migrating Spark applications from x86_64 to Arm.

learning_objectives: 
    - Provision an Azure Arm64 virtual machine using Azure console
    - Learn how to create an Azure Linux 3.0 Docker container
    - Deploy a Spark application inside an Azure Linux 3.0 Arm64-based Docker container or an Azure Linux 3.0 custom-image based Azure virtual machine
    - Run a suite of Spark benchmarks to understand and evaluate performance on the Azure Cobalt 100 virtual machine

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6)
    - A machine with [Docker](/install-guides/docker/) installed
    - Familiarity with distributed computing concepts and the [Apache Spark architecture](https://spark.apache.org/docs/latest/)

author: Pareena Verma

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - Apache Spark
    - Python
    - Docker
 
operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Azure Virtual Machines documentation
      link: https://learn.microsoft.com/en-us/azure/virtual-machines/
      type: documentation
  - resource:
      title: Azure Container Instances documentation
      link: https://learn.microsoft.com/en-us/azure/container-instances/
      type: documentation
  - resource:
      title: Docker overview
      link: https://docs.docker.com/get-started/overview/
      type: documentation
  - resource:
      title: Spark official website and documentation
      link: https://spark.apache.org/
      type: documentation
  - resource:
      title: Hadoop official website
      link: https://hadoop.apache.org/
      type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
