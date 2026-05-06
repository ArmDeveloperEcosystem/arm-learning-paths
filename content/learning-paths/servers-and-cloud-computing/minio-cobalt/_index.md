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

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:58Z'
  generator: template
  source_hash: 6c438573edec90b3aa4135ace38cd3ae604c58658c1949117ca80dbdd21394bd
  summary: >-
    Learn how to deploy and configure MinIO on an Azure Cobalt 100 virtual machine, benchmark
    object storage throughput, and validate S3 compatibility using the boto3 Python SDK. It is
    designed for developers, DevOps engineers, and platform engineers who want to deploy MinIO
    object storage on Microsoft Azure Cobalt 100 virtual machines. By the end, you will be able
    to provision an Azure Cobalt 100 virtual machine and deploy MinIO, benchmark MinIO storage
    throughput for large object transfers, and validate S3 API compatibility using the boto3 Python
    SDK. It focuses on tools and technologies such as MinIO, Python, and boto3, Linux environments,
    Arm platforms including Neoverse, and cloud platforms such as Microsoft Azure. The main steps
    cover Overview of Azure Cobalt 100 and MinIO, Create an Azure Cobalt 100 virtual machine,
    Open MinIO ports in the Azure Network Security Group, Install and configure MinIO on Azure
    Cobalt 100, and Benchmark MinIO storage performance on Azure Cobalt 100.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Azure Cobalt 100 virtual machine and deploy MinIO, benchmark MinIO
      storage throughput for large object transfers, and validate S3 API compatibility using the
      boto3 Python SDK. Learn how to deploy and configure MinIO on an Azure Cobalt 100 virtual
      machine, benchmark object storage throughput, and validate S3 compatibility using the boto3
      Python SDK.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers, DevOps engineers, and platform engineers who
      want to deploy MinIO object storage on Microsoft Azure Cobalt 100 virtual machines.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Microsoft Azure account](https://azure.microsoft.com/)
      with access to Cobalt 100-based instances (Dpsv6); Familiarity with SSH and remote server
      access; Basic understanding of cloud storage concepts.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including MinIO, Python, and boto3, Linux environments, Arm
      platforms such as Neoverse, and cloud platforms such as Microsoft Azure.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Overview of Azure Cobalt 100 and MinIO, Create an
      Azure Cobalt 100 virtual machine, Open MinIO ports in the Azure Network Security Group,
      Install and configure MinIO on Azure Cobalt 100, and Benchmark MinIO storage performance
      on Azure Cobalt 100.
# END generated_summary_faq

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

