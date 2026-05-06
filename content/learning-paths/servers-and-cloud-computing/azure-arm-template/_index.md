---
title: Deploy Arm-based Cobalt 100 VMs using Azure Resource Manager templates
description: Learn how to create and deploy Azure Resource Manager templates to provision Arm64-based Cobalt 100 virtual machines on Azure using the Azure CLI.

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for developers and DevOps engineers who want to automate the deployment of Arm-based Azure Cobalt 100 virtual machines using Azure Resource Manager templates.

learning_objectives:
    - Structure an Azure Resource Manager template with parameters, variables, and resources
    - Specify Arm64 architecture and Cobalt 100 Azure VM sizes
    - Deploy the template using Azure CLI and verify the deployment
    - Connect to your Cobalt 100 VM and validate the Arm64 architecture

prerequisites:
    - An Azure subscription with permissions to create resource groups, virtual machines, and networking resources
    - Azure CLI installed on your local machine - see the [Azure CLI install guide](/install-guides/azure-cli/)
    - An SSH key pair for authentication

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:56Z'
  generator: template
  source_hash: 1682c0527bb49c417263286e2aba7c82fb9a27fa315ecc6b9ca10978b69cc236
  summary: >-
    Learn how to create and deploy Azure Resource Manager templates to provision Arm64-based Cobalt
    100 virtual machines on Azure using the Azure CLI. It is designed for developers and DevOps
    engineers who want to automate the deployment of Arm-based Azure Cobalt 100 virtual machines
    using Azure Resource Manager templates. By the end, you will be able to structure an Azure
    Resource Manager template with parameters, variables, and resources, specify Arm64 architecture
    and Cobalt 100 Azure VM sizes, and deploy the template using Azure CLI and verify the deployment.
    It focuses on tools and technologies such as Azure CLI and JSON, Linux environments, Arm platforms
    including Neoverse, and cloud platforms such as Microsoft Azure. The main steps cover Getting
    started with Azure Resource Manager, Create the Azure Resource Manager template, Deploy the
    Azure Resource Manager template, and Connect to the Cobalt 100 VM and verify Arm64 architecture.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will structure an Azure Resource Manager template with parameters, variables, and resources,
      specify Arm64 architecture and Cobalt 100 Azure VM sizes, and deploy the template using
      Azure CLI and verify the deployment. Learn how to create and deploy Azure Resource Manager
      templates to provision Arm64-based Cobalt 100 virtual machines on Azure using the Azure
      CLI.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers and DevOps engineers who want to automate the
      deployment of Arm-based Azure Cobalt 100 virtual machines using Azure Resource Manager templates.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An Azure subscription with permissions
      to create resource groups, virtual machines, and networking resources; Azure CLI installed
      on your local machine - see the [Azure CLI install guide](/install-guides/azure-cli/); An
      SSH key pair for authentication.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Azure CLI and JSON, Linux environments, Arm platforms
      such as Neoverse, and cloud platforms such as Microsoft Azure.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Getting started with Azure Resource Manager, Create
      the Azure Resource Manager template, Deploy the Azure Resource Manager template, and Connect
      to the Cobalt 100 VM and verify Arm64 architecture.
# END generated_summary_faq

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers:
  - Microsoft Azure
armips:
    - Neoverse
tools_software_languages:
    - Azure CLI
    - JSON
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Azure Resource Manager documentation
        link: https://learn.microsoft.com/en-us/azure/azure-resource-manager/
        type: documentation
    - resource:
        title: Dpsv6 size series
        link: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/general-purpose/dpsv6-series
        type: documentation
    - resource:
        title: Deploy a Cobalt 100 virtual machine on Azure
        link: /learning-paths/servers-and-cloud-computing/cobalt/
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

