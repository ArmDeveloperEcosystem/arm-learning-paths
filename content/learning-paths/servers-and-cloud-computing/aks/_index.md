---
title: Create an Arm-based Kubernetes cluster on Microsoft Azure Kubernetes Service 

minutes_to_complete: 60   

who_is_this_for: This is an advanced topic for software developers who want to deploy an Arm-based Kubernetes cluster using Azure Kubernetes Service (AKS).

learning_objectives: 
    - Automate the deployment of an Arm-based AKS cluster using Terraform
    - Install Wordpress on AKS as an example workload

prerequisites:
    - An Azure account
    - A machine with [Terraform](/install-guides/terraform/), [Azure CLI](/install-guides/azure-cli), and [Kubectl](/install-guides/kubectl/) installed

author: Jason Andrews

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - Terraform
    - Kubernetes
    - WordPress
    - MySQL

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Azure Kubernetes Service on Arm based Ampere Altra processors
        link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/aks-on-arm-based-ampere
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
    - resource:
        title: Terraform Azure Providers documentation
        link: https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
