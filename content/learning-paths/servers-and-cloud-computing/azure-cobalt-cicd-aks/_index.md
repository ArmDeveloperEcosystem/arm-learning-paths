---
title: Deploy a .NET application on Microsoft Azure Cobalt 100 VMs

minutes_to_complete: 60   

who_is_this_for: This is an advanced topic for software developers who want to develop cloud-native applications using GitHub Actions and Azure Kubernetes Service (AKS), and run them on Microsoft Azure Cobalt 100 VMs.

learning_objectives: 
    - Configure an Azure Cobalt 100 VM as a self-hosted GitHub runner.
    - Create an AKS cluster with Arm-based Azure Cobalt 100 nodes using Terraform.
    - Deploy a .NET application to AKS with GitHub Actions using the self-hosted Arm64-based runner.

prerequisites:
    - A Microsoft Azure account. 
    - A GitHub account.
    - A machine with [Terraform](/install-guides/terraform/),[Azure CLI](/install-guides/azure-cli), and [Kubectl](/install-guides/kubectl/) installed.

author_primary: Pranay Bakre

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
cloud_service_providers: Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - .NET
    - Kubernetes
    - Docker

operatingsystems:
    - Linux

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
