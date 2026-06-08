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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:31:21Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6c438573edec90b3aa4135ace38cd3ae604c58658c1949117ca80dbdd21394bd
  summary_generated_at: '2026-06-02T04:26:22Z'
  summary_source_hash: 6c438573edec90b3aa4135ace38cd3ae604c58658c1949117ca80dbdd21394bd
  faq_generated_at: '2026-06-03T01:31:21Z'
  faq_source_hash: 6c438573edec90b3aa4135ace38cd3ae604c58658c1949117ca80dbdd21394bd
  summary: >-
    This Learning Path shows how to deploy a single-node, S3-compatible MinIO server on an Arm-based
    Azure Cobalt 100 virtual machine and verify it end to end. You will provision a Dpsv6 instance
    (Ubuntu 24.04), open MinIO ports 9000 and 9001 in the Azure Network Security Group, connect
    over SSH, and install and configure MinIO. You will generate a 1 GB test dataset, benchmark
    large-object upload throughput using MinIO tooling, and validate S3 API compatibility with
    the boto3 Python SDK. The path is introductory, takes about 30 minutes, and is intended for
    developers and platform/DevOps engineers with an Azure account, SSH familiarity, and basic
    cloud storage knowledge.
  faqs:
  - question: Which provisioning method, VM size, and OS are used in this path?
    answer: >-
      The steps use the Azure Portal to create an Arm-based Azure Cobalt 100 virtual machine from
      the Dpsv6 series. The architecture shows Ubuntu 24.04 as the OS for the VM. Other provisioning
      methods exist, but this path focuses on the Azure Portal workflow.
  - question: Which network ports must I open for MinIO, and where do I configure them?
    answer: >-
      Open TCP ports 9000 and 9001 in the Azure Network Security Group (NSG) attached to the VM’s
      network interface or subnet. You configure these rules in the Azure Portal under your VM’s
      Networking settings.
  - question: How do I connect to the Azure Cobalt 100 VM?
    answer: >-
      Use SSH with the private key you downloaded and the VM’s public IP address. For example:
      ssh -i <your-key>.pem azureuser@<VM-IP>.
  - question: How do I run the throughput benchmark and what result should I expect to see?
    answer: >-
      Create a 1 GB dataset with dd, then measure upload time using time mc cp --recursive dataset
      local/ as shown. dd prints record counts and the total bytes written; time reports the command’s
      duration. The path does not specify expected performance values.
  - question: How is S3 API compatibility validated in this path?
    answer: >-
      You use the Python boto3 SDK to interact with MinIO and confirm S3 compatibility. Ensure
      Python and boto3 are available, then run simple bucket and object operations as directed
      in the steps.
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

