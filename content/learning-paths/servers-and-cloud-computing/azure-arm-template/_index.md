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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-26T17:41:45Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1682c0527bb49c417263286e2aba7c82fb9a27fa315ecc6b9ca10978b69cc236
  summary_generated_at: '2026-06-26T17:41:45Z'
  summary_source_hash: 1682c0527bb49c417263286e2aba7c82fb9a27fa315ecc6b9ca10978b69cc236
  faq_generated_at: '2026-06-26T17:41:45Z'
  faq_source_hash: 1682c0527bb49c417263286e2aba7c82fb9a27fa315ecc6b9ca10978b69cc236
  summary: >-
    In this Learning Path, you build an Azure Resource Manager (ARM) template to provision a Linux
    virtual machine on Azure Cobalt 100 Arm-based infrastructure. You define template sections
    for parameters, variables, resources, and outputs, select an `arm64`-capable VM size from
    the Dpsv6 series in a supported region, and deploy the template with the Azure CLI into a
    new resource group. After deployment, you retrieve the VM’s public IP, connect with SSH using
    the configured key, and validate the architecture on the instance using standard commands.
    By the end, you have a repeatable ARM template that creates a Cobalt 100 VM and associated
    networking ready for `arm64` development.
  faqs:
  - question: How do I confirm the Azure region I selected supports Cobalt 100 VM sizes?
    answer: >-
      Run `az vm list-skus` for the target region and filter for the Dpsv6 series. For example:
      `az vm list-skus --location eastus --size Standard_D --all --output table | grep "ps_v6"`.
  - question: Which VM size should I set in the template for a Cobalt 100 instance?
    answer: >-
      Choose a Dpsv6 series size returned by the SKU query for your region. The output example
      shows sizes such as `Standard_D16ps_v6`.
  - question: Where do I find the VM’s public IP address after deployment?
    answer: >-
      Use the value surfaced in the previous deployment step, often provided as a deployment output.
      You can also view the Public IP resource created in the resource group defined by the template.
  - question: What username should I use when connecting with SSH?
    answer: >-
      Use the admin username defined in your template’s parameters. The example uses `azureuser`;
      if your template specifies a different name, use that instead.
  - question: What output confirms the VM is running on `arm64`?
    answer: >-
      Run `uname -m` and expect `aarch64`. You can also run `lscpu` to see Arm 64-bit CPU details.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
