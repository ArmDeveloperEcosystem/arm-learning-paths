---
title: Deploy MinIO on Azure Cobalt 100

description: Learn how to deploy and configure MinIO on an Azure Cobalt 100 virtual machine, benchmark object storage throughput, and validate S3 compatibility using the boto3 Python SDK.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers, DevOps engineers, and platform engineers who want to deploy MinIO object storage on Microsoft Azure Cobalt 100 virtual machines.

learning_objectives:
    - Provision an Azure Cobalt 100 virtual machine and deploy MinIO
    - Benchmark MinIO storage throughput for large object transfers
    - Validate S3 API compatibility using the boto3 Python SDK
    - Store and retrieve AI/ML datasets and model artifacts using MinIO

prerequisites:
  - A [Microsoft Azure account](https://azure.microsoft.com/) with access to Cobalt 100-based instances (Dpsv6)
  - Familiarity with SSH and remote server access
  - Basic understanding of cloud storage concepts

generate_summary_faq: true

author: Jason Andrews

### Tags
skilllevels: Introductory
subjects: Databases 
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - MinIO
    - Python
    - boto3

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: MinIO Documentation
      link: https://min.io/docs/minio/linux/index.html
      type: documentation
  - resource:
      title: MinIO GitHub Repository
      link: https://github.com/minio/minio
      type: documentation
  - resource:
      title: Azure Cobalt 100 processors
      link: https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353
      type: documentation
  - resource:
      title: Deploy a Cobalt 100 virtual machine on Azure
      link: /learning-paths/servers-and-cloud-computing/cobalt/
      type: learning-path

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
