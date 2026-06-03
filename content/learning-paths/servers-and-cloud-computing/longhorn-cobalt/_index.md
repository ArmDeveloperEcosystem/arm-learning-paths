---
title: Deploy Longhorn on Arm64 Azure virtual machines powered by Azure Cobalt 100 for Kubernetes persistent storage
    
description: Learn how to install and configure Longhorn on an Arm64 Azure virtual machine powered by Azure Cobalt 100, deploy Kubernetes persistent storage using Longhorn on K3s, create persistent volumes, and benchmark storage performance for cloud-native workloads.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers, DevOps engineers, platform engineers, and Kubernetes administrators who want to deploy persistent storage for Kubernetes workloads using Longhorn on Arm-based cloud infrastructure.

learning_objectives:
    - Install and configure K3s Kubernetes on Arm64 Azure virtual machines powered by Azure Cobalt 100
    - Install and configure Longhorn distributed block storage on Arm64
    - Create and manage Kubernetes persistent volumes using Longhorn
    - Benchmark Kubernetes storage performance using fio

prerequisites:
  - A [Microsoft Azure account](https://azure.microsoft.com/) with access to Cobalt 100 based instances (Dpsv6)
  - Basic knowledge of Linux command-line operations
  - Familiarity with SSH and remote server access
  - Basic understanding of Kubernetes and containerized workloads

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - Longhorn
    - Kubernetes
    - K3s
    - fio

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Longhorn Official Website
      link: https://longhorn.io/
      type: website
  - resource:
      title: Longhorn Documentation
      link: https://longhorn.io/docs/
      type: documentation
  - resource:
      title: K3s Documentation
      link: https://docs.k3s.io/
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
