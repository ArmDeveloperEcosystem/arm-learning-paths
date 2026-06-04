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

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:22:28Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b5bd3abde8d9dd3146e0f11f4819ac510417ad7f707b4d0970c02fd63801b358
  summary_generated_at: '2026-06-02T03:10:03Z'
  summary_source_hash: b5bd3abde8d9dd3146e0f11f4819ac510417ad7f707b4d0970c02fd63801b358
  faq_generated_at: '2026-06-03T00:22:28Z'
  faq_source_hash: b5bd3abde8d9dd3146e0f11f4819ac510417ad7f707b4d0970c02fd63801b358
  summary: >-
    This Learning Path shows how to configure a self-hosted GitHub Actions Arm64 runner on an
    Azure Cobalt 100 VM, create an Arm-based Azure Kubernetes Service (AKS) cluster with Terraform,
    and deploy a .NET 8 web application using GitHub Actions CI/CD. You will work on Linux and
    use Azure CLI, kubectl, and Terraform to automate infrastructure and deployment on Microsoft’s
    Armv9 Neoverse-N2–based Cobalt 100 instances (Dpsv6/Dplsv6/Epsv6). By the end, you will have
    a running application on AKS triggered from a self-hosted runner. Prerequisites are a Microsoft
    Azure account, a GitHub account, and a machine with Terraform, Azure CLI, and kubectl installed.
    Estimated time to complete is about 60 minutes.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need a Microsoft Azure account, a GitHub account, and a machine with Terraform, Azure
      CLI, and kubectl installed. The procedures use Linux.
  - question: Which Azure Cobalt 100 VM series should I use for the runner or AKS nodes?
    answer: >-
      The path does not prescribe a specific series. Azure Cobalt 100 offers general-purpose Dpsv6
      and Dplsv6 VMs and a memory-optimized Epsv6 series; select from these in the steps as appropriate.
  - question: Can I use GitHub-hosted Arm64 runners instead of a self-hosted runner?
    answer: >-
      GitHub-hosted Arm64 runners are generally available for Team and Enterprise Cloud accounts.
      This path demonstrates using a self-hosted Arm64 runner on an Azure Cobalt 100 VM.
  - question: What does the Terraform configuration create?
    answer: >-
      An Azure Kubernetes Service (AKS) cluster with Arm-based Azure Cobalt 100 nodes. The cluster
      is the target environment for deploying the .NET application.
  - question: What should I expect after the GitHub Actions workflow runs?
    answer: >-
      The .NET 8-based web application is built and deployed to the AKS cluster using the self-hosted
      Arm64 runner. The steps guide you through the CI/CD pipeline to reach this state.
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

