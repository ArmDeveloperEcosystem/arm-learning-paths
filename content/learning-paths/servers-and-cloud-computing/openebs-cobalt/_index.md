---
title: Deploy OpenEBS on Azure Cobalt 100 Arm64 virtual machines for Kubernetes-native persistent storage

draft: true
cascade:
    draft: true

description: Learn how to install and configure OpenEBS LocalPV on an Azure Cobalt 100 Arm64 virtual machine using K3s Kubernetes, provision persistent storage dynamically, deploy stateful applications, and validate persistent storage functionality.
   
minutes_to_complete: 60

who_is_this_for: This is an introductory topic for DevOps engineers, platform engineers, cloud-native developers, and Kubernetes administrators who want to deploy lightweight Kubernetes-native persistent storage on Arm-based cloud infrastructure.

learning_objectives:
    - Install and configure K3s Kubernetes on Azure Cobalt 100 Arm64 virtual machines
    - Deploy OpenEBS LocalPV using Helm
    - Configure Kubernetes storage classes and Persistent Volume Claims (PVCs)
    - Deploy and validate stateful Kubernetes workloads with persistent storage

prerequisites:
  - A [Microsoft Azure account](https://azure.microsoft.com/) with access to Cobalt 100 based instances (Dpsv6)
  - Basic knowledge of Linux command-line operations
  - Familiarity with SSH and remote server access
  - Basic understanding of Kubernetes concepts and containerized applications

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - Kubernetes
    - K3s
    - OpenEBS
    - Helm

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: OpenEBS Official Website
      link: https://openebs.io/
      type: website
  - resource:
      title: OpenEBS Documentation
      link: https://openebs.io/docs
      type: documentation
  - resource:
      title: K3s Documentation
      link: https://docs.k3s.io/
      type: documentation
  - resource:
      title: Kubernetes Documentation
      link: https://kubernetes.io/docs/
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
