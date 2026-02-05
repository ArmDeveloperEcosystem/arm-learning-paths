---
title: Deploy Arm-based Cobalt 100 VMs using Azure Resource Manager templates

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
