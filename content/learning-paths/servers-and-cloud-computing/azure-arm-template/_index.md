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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:21:51Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1682c0527bb49c417263286e2aba7c82fb9a27fa315ecc6b9ca10978b69cc236
  summary_generated_at: '2026-06-02T03:09:38Z'
  summary_source_hash: 1682c0527bb49c417263286e2aba7c82fb9a27fa315ecc6b9ca10978b69cc236
  faq_generated_at: '2026-06-03T00:21:51Z'
  faq_source_hash: 1682c0527bb49c417263286e2aba7c82fb9a27fa315ecc6b9ca10978b69cc236
  summary: >-
    Learn how to automate the provisioning of Arm64-based Azure Cobalt 100 virtual machines using
    Azure Resource Manager (ARM) templates and the Azure CLI. You will author a JSON template
    with parameters, variables, resources, and outputs to define a Linux VM, networking, security
    settings, and SSH access. The path shows how to specify Arm64 and choose a Cobalt 100 VM size,
    deploy the template to a resource group, and verify the VM by connecting over SSH and checking
    uname -m for aarch64. Prerequisites include an Azure subscription with sufficient permissions,
    the Azure CLI installed, and an SSH key pair. By the end, you can reproducibly deploy a Cobalt
    100 VM and validate the Arm64 environment.
  faqs:
  - question: What do I need before running the template?
    answer: >-
      You need an Azure subscription with permissions to create resource groups, virtual machines,
      and networking resources, the Azure CLI installed, and an SSH key pair. These are the only
      explicit prerequisites listed.
  - question: Which Azure region and VM size should I use for Cobalt 100?
    answer: >-
      Create a resource group in your preferred region, then query available VM SKUs in that region
      and filter for the Dpsv6 series to find Cobalt 100 sizes. The Learning Path shows an az
      vm list-skus command and grep filter you can run to confirm availability.
  - question: How is the ARM template structured and how do I customize it?
    answer: >-
      The template is organized into $schema, contentVersion, parameters, variables, resources,
      and outputs. You customize deployments by defining inputs in parameters, computing values
      in variables, and specifying resources that include the VM, networking, security settings,
      and SSH authentication.
  - question: How do I get the VM’s public IP to connect over SSH?
    answer: >-
      Use the public IP address recorded during the deployment step or retrieve it from your template
      outputs. The path then uses that IP with your SSH key to connect.
  - question: What result should I expect after deployment, and how do I verify Arm64?
    answer: >-
      You should have a Linux VM powered by Cobalt 100 with its networking and SSH access configured
      in your resource group. After connecting via SSH, run uname -m and expect aarch64; lscpu
      will show additional CPU details.
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

