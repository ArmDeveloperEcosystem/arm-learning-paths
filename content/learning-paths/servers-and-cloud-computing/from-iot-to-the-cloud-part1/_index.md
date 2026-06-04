---
title: 'Deploy .NET applications to Arm Virtual Machines and Container Registry in Microsoft Azure'
description: Learn how to create an Arm64 Azure VM, install .NET SDK, containerize .NET applications, and push Docker images to Azure Container Registry.

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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:54:23Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 94866800acca2c5f9cd89f76f972af1a343aad5777b6844d49fac09eb764f580
  summary_generated_at: '2026-06-02T03:53:58Z'
  summary_source_hash: 94866800acca2c5f9cd89f76f972af1a343aad5777b6844d49fac09eb764f580
  faq_generated_at: '2026-06-03T00:54:23Z'
  faq_source_hash: 94866800acca2c5f9cd89f76f972af1a343aad5777b6844d49fac09eb764f580
  summary: >-
    This introductory path shows how to deploy a .NET application on Arm64 in Microsoft Azure.
    You will create a Linux Arm64 virtual machine, connect over SSH using Azure Cloud Shell, install
    the .NET 7 SDK and git, then build and run the app. You will configure the VM’s network security
    group to expose the application over the Internet. Next, you will containerize the People.WebApp
    with a Dockerfile in Visual Studio Code and push the resulting image to Azure Container Registry.
    Prerequisites include an Azure subscription, Visual Studio Code with the Docker and C# extensions,
    and Docker on Arm64. By the end, you have a running app and an image stored in ACR.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Azure subscription, Visual Studio Code with the Docker and C# extensions, and
      Docker installed on an Arm64 system. These prerequisites are listed so you can build the
      app locally and containerize it before pushing to Azure Container Registry.
  - question: How do I connect to the VM and which IP address should I use?
    answer: >-
      Connect over SSH using Azure Cloud Shell from the portal. Always use the public IP address
      of your own VM shown in the Azure portal and not the sample IP provided in the tutorial
      text.
  - question: Which SDK and tools are installed on the VM to build the app?
    answer: >-
      You install the .NET 7 SDK using the dotnet-install.sh script and also install git to clone
      the application sources. These are used to build and run the .NET application on the VM.
  - question: How will the application be accessible from the internet?
    answer: >-
      You will configure the VM’s network security group to expose the application. This step
      opens access so the running app can be reached externally.
  - question: Where should I build the Docker image and how is it published to Azure?
    answer: >-
      You can containerize the People.WebApp using Visual Studio Code on a Windows on Arm device
      (via WSL) or on the previously created VM, then push the local Docker image to Azure Container
      Registry. The application sources are cloned from https://github.com/dawidborycki/People.WebApp.git.
# END generated_summary_faq

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

