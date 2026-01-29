---
title: Deploy Cobalt 100 VMs with Azure Resource Manager templates

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for developers and DevOps engineers who want to automate the deployment of Arm-based Cobalt 100 virtual machines using Azure Resource Manager templates.

learning_objectives:
    - Understand Azure Resource Manager template structure and syntax
    - Create an Azure Resource Manager template for deploying Cobalt 100 virtual machines
    - Deploy an Arm-based Linux VM using the template with Azure CLI
    - Configure SSH authentication for secure access

prerequisites:
    - A Microsoft Azure account with permissions to create virtual machines and resource groups
    - An SSH key pair for authentication

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
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
