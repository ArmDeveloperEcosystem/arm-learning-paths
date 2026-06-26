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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-26T18:33:18Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: b5bd3abde8d9dd3146e0f11f4819ac510417ad7f707b4d0970c02fd63801b358
  summary_generated_at: '2026-06-26T18:33:18Z'
  summary_source_hash: b5bd3abde8d9dd3146e0f11f4819ac510417ad7f707b4d0970c02fd63801b358
  faq_generated_at: '2026-06-26T18:33:18Z'
  faq_source_hash: b5bd3abde8d9dd3146e0f11f4819ac510417ad7f707b4d0970c02fd63801b358
  summary: >-
    In this Learning Path, you set up a self-hosted GitHub Actions runner on an Azure Cobalt 100
    VM and use it to build a .NET 8 web application for `arm64`. With Terraform, you create an
    Azure Kubernetes Service (AKS) cluster backed by Cobalt 100-based nodes, then use a GitHub
    Actions workflow to deploy the application to the cluster. Along the way, you select an appropriate
    Cobalt 100 VM series for the runner, confirm the runner is available to execute jobs, and
    validate that the workload targets the Arm-based AKS nodes. The result is a working CI/CD
    path from source to a running application on Azure Cobalt 100 infrastructure.
  faqs:
  - question: Which Azure Cobalt 100 VM series should I use for the self-hosted runner?
    answer: >-
      Azure Cobalt 100 offers general-purpose Dpsv6/Dplsv6 and memory-optimized Epsv6 series.
      Choose based on your build and deployment needs; this Learning Path does not prescribe a specific
      size.
  - question: Do I have to use a self-hosted runner, or can I use GitHub-hosted `arm64` runners?
    answer: >-
      GitHub-hosted `arm64` runners are generally available for Team and Enterprise Cloud accounts.
      If your account qualifies, you can use hosted `arm64` runners instead of a self-hosted runner.
  - question: How do I know the self-hosted GitHub Actions runner is ready before triggering the
      workflow?
    answer: >-
      Confirm the runner is installed on the Azure Cobalt 100 VM and appears online in GitHub.
      Do not start the workflow until the runner reports an available status.
  - question: What result should I expect after applying the Terraform configuration?
    answer: >-
      Terraform creates an AKS cluster with node pools based on Azure Cobalt 100. This cluster
      is then targeted by the GitHub Actions workflow that deploys the .NET application.
  - question: How can I verify the .NET application is running on Arm-based nodes in AKS?
    answer: >-
      Check that the deployed workload is scheduled onto the AKS node pool created for Azure Cobalt
      100. Seeing pods running on that pool indicates the application is using `arm64` nodes as
      intended.
# END generated_summary_faq

author: Pranay Bakre

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
