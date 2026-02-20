---
title: Deploy a Cobalt 100 Virtual Machine on Azure

minutes_to_complete: 10

who_is_this_for: This is an introductory topic for developers and DevOps engineers who want to deploy an Arm-based virtual machine on Azure and expose an application port to the internet.

learning_objectives:
    - Deploy an Arm-based Cobalt 100 virtual machine (VM) on Microsoft Azure
    - Connect to the Cobalt 100 VM using SSH
    - Configure an inbound TCP port in the associated Network Security Group (NSG)
    - Verify external connectivity to the newly-opened port

prerequisites:
    - A Microsoft Azure subscription with permissions to create virtual machines and networking resources
    - Basic familiarity with SSH

author: Joe Stech

### Tags
# Tagging metadata, see the Learning Path guide for the allowed values
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers:
  - Microsoft Azure
armips:
    - Neoverse
tools_software_languages:
    - Azure Portal
    - Azure CLI
operatingsystems:
    - Linux


further_reading:
    - resource:
        title: Azure Cobalt 100 VM documentation
        link: https://learn.microsoft.com/azure/virtual-machines/cobalt-100
        type: Documentation
    - resource:
        title: Azure Virtual Machines overview
        link: https://learn.microsoft.com/azure/virtual-machines/
        type: Documentation
    - resource:
        title: Configure Azure network security group rules
        link: https://learn.microsoft.com/azure/virtual-network/security-overview
        type: Documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
