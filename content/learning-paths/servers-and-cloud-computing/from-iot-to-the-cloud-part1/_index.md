---
title: 'Deploy .NET applications to Arm Virtual Machines and Container Registry in Microsoft Azure'

minutes_to_complete: 30

who_is_this_for: This learning path is for software developers interested in learning how to deploy .NET applications to Microsoft Azure using Arm64-powered Virtual Machines. You will also learn how to containerize .NET applications, and push Docker images to the Azure Container Registry.

learning_objectives: 
    - Create a Virtual Machine (VM) in Microsoft Azure.
    - Connect to the VM to install app dependencies, including SDK.
    - Create and run the .NET application.
    - Configure the network security group of the VM to expose the application over the Internet.
    - Provision of an Azure Container Registry.
    - Push a local Docker image to Azure Container Registry.

prerequisites:
    - 'A subscription to Azure. Use this link to sign up for a free account: https://azure.microsoft.com/en-us/free/'
    - 'Visual Studio Code: https://code.visualstudio.com/download' 
    - 'Docker Extension for Visual Studio Code: https://code.visualstudio.com/docs/containers/overview'
    - 'C# Extension for Visual Studio Code: https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp'
    - '[Install Docker on Arm64](/install-guides/docker/docker-desktop/)'

author: Dawid Borycki

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers:
  - Microsoft Azure

armips:
    - Neoverse
    
tools_software_languages:
    - .NET SDK
    - C#

operatingsystems:
    - Linux


further_reading:
    - resource:
        title: Terraform on Azure
        link: /learning-paths/servers-and-cloud-computing/azure-terraform/
        type: Tutorial
    - resource:
        title: Azure Virtual Machines with Ampere Altra Arm–based processors—generally available
        link: https://azure.microsoft.com/en-us/blog/azure-virtual-machines-with-ampere-altra-arm-based-processors-generally-available/
        type: Blog
    - resource:
        title: About Azure bastion
        link: https://learn.microsoft.com/en-us/azure/bastion/bastion-overview
        type: Documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
