---
title: Deploy a .NET application on Microsoft Azure Cobalt 100 VMs
description: Learn how to configure a self-hosted GitHub runner on Azure Cobalt 100, create an AKS cluster with Terraform, and deploy a .NET application using GitHub Actions CI/CD.

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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:56Z'
  generator: template
  source_hash: b5bd3abde8d9dd3146e0f11f4819ac510417ad7f707b4d0970c02fd63801b358
  summary: >-
    Learn how to configure a self-hosted GitHub runner on Azure Cobalt 100, create an AKS cluster
    with Terraform, and deploy a .NET application using GitHub Actions CI/CD. It is designed for
    software developers who want to develop cloud-native applications using GitHub Actions and
    Azure Kubernetes Service (AKS), and run them on Microsoft Azure Cobalt 100 VMs. By the end,
    you will be able to configure an Azure Cobalt 100 VM as a self-hosted GitHub runner, create
    an AKS cluster with Arm-based Azure Cobalt 100 nodes using Terraform, and deploy a .NET application
    to AKS with GitHub Actions using the self-hosted Arm64-based runner. It focuses on tools and
    technologies such as .NET, Kubernetes, and Docker, Linux environments, Arm platforms including
    Neoverse, and cloud platforms such as Microsoft Azure. The main steps cover Background and
    Build and deploy a .NET application.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will configure an Azure Cobalt 100 VM as a self-hosted GitHub runner, create an AKS
      cluster with Arm-based Azure Cobalt 100 nodes using Terraform, and deploy a .NET application
      to AKS with GitHub Actions using the self-hosted Arm64-based runner. Learn how to configure
      a self-hosted GitHub runner on Azure Cobalt 100, create an AKS cluster with Terraform, and
      deploy a .NET application using GitHub Actions CI/CD.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for software developers who want to develop cloud-native applications
      using GitHub Actions and Azure Kubernetes Service (AKS), and run them on Microsoft Azure
      Cobalt 100 VMs.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A Microsoft Azure account.; A GitHub
      account.; A machine with [Terraform](/install-guides/terraform/),[Azure CLI](/install-guides/azure-cli),
      and [Kubectl](/install-guides/kubectl/) installed.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including .NET, Kubernetes, and Docker, Linux environments,
      Arm platforms such as Neoverse, and cloud platforms such as Microsoft Azure.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Background and Build and deploy a .NET application.
# END generated_summary_faq

author: Pranay Bakre

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - .NET
    - Kubernetes
    - Docker

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Developing Cloud-native Applications with New Arm Neoverse CSS-based Microsoft Azure Cobalt 100 Virtual Machines 
        link: https://newsroom.arm.com/blog/microsoft-azure-cobalt-100-vm
        type: blog
    - resource:
        title: AKS documentation
        link: https://docs.microsoft.com/en-us/azure/aks/
        type: documentation
    - resource:
        title: Azure Developer documentation
        link: https://docs.microsoft.com/en-us/azure/developer/
        type: documentation
    - resource:
        title: Kubernetes documentation
        link:  https://kubernetes.io/docs/home/
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

