---
title: Deploy Alluxio on Azure Cobalt 100 Arm64 virtual machines for data orchestration and caching

description: Learn how to install and configure Alluxio on an Azure Cobalt 100 Arm64 virtual machine, integrate it with Apache Spark, enable data caching, and benchmark performance improvements for analytics workloads.

   
minutes_to_complete: 90

who_is_this_for: This is an introductory topic for developers, data engineers, and platform engineers who want to build high-performance data pipelines and analytics systems using Alluxio on Arm-based cloud environments.

learning_objectives:
    - Install and configure Alluxio on Azure Cobalt 100 Arm64 virtual machines
    - Configure data caching using Alluxio memory storage
    - Integrate Alluxio with Apache Spark for analytics workloads
    - Benchmark data access performance and understand caching benefits

prerequisites:
  - A [Microsoft Azure account](https://azure.microsoft.com/) with access to Cobalt 100 based instances (Dpsv6)
  - Basic knowledge of Linux command-line operations
  - Familiarity with SSH and remote server access
  - Basic understanding of data processing, storage systems, and caching concepts

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - Alluxio
    - Apache Spark
    - Java

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Alluxio Official Website
      link: https://www.alluxio.io/
      type: website
  - resource:
      title: Alluxio Documentation
      link: https://docs.alluxio.io/
      type: documentation
  - resource:
      title: Apache Spark Documentation
      link: https://spark.apache.org/docs/latest/
      type: documentation
  - resource:
      title: Azure Cobalt 100 processors
      link: https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
