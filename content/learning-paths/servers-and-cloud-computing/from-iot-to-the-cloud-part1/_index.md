---
title: Deploy .NET applications to Arm virtual machines and Azure Container Registry
description: Learn how to create an Arm64 Azure VM, install .NET SDK, containerize .NET applications, and push Docker images to Azure Container Registry.

minutes_to_complete: 30

who_is_this_for: This Learning Path is for software developers interested in learning how to deploy .NET applications to Microsoft Azure using Arm64-powered virtual machines (VMs). You'll also learn how to containerize .NET applications, and push Docker images to the Azure Container Registry.

learning_objectives: 
    - Create a VM in Microsoft Azure.
    - Connect to the VM to install app dependencies, including SDK.
    - Create and run the .NET application.
    - Configure the network security group of the VM to expose the application over the Internet.
    - Provision of an Azure Container Registry.
    - Push a local Docker image to Azure Container Registry.

prerequisites:
    - A subscription to [Azure](https://azure.microsoft.com/en-us/free/)
    - The [Visual Studio Code](https://code.visualstudio.com/download) code editor
    - The Docker extension for [Visual Studio Code](https://code.visualstudio.com/docs/containers/overview)
    - The C# extension for [Visual Studio Code](https://marketplace.visualstudio.com/items?itemName=ms-dotnettools.csharp)
    - An Arm64 installation of [Docker](/install-guides/docker/docker-desktop/)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T21:58:31Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 12f49d91f2248be0a45d531e675d2d0d83af5d3d2e7be62dd50511161997644b
  summary_generated_at: '2026-09-10T21:58:31Z'
  summary_source_hash: 12f49d91f2248be0a45d531e675d2d0d83af5d3d2e7be62dd50511161997644b
  faq_generated_at: '2026-09-10T21:58:31Z'
  faq_source_hash: 12f49d91f2248be0a45d531e675d2d0d83af5d3d2e7be62dd50511161997644b
  summary: >-
    You'll deploy a .NET application on an Arm64-based Azure VM and publish its container image to Azure Container Registry. First, you'll create the VM, connect through Azure Cloud Shell, install the SDK, and run the sample application. Then, you'll containerize the application with Docker and provision a registry so that you can push the image for later deployment.
  faqs:
  - question: How do I connect to the VM without installing an SSH client?
    answer: >-
      Use Azure Cloud Shell from the Azure Portal. SSH to the VM using its public IP address.
  - question: After running the .NET SDK install script, where is the SDK installed?
    answer: >-
      The script installs .NET SDK 7 under the `.dotnet` folder in your home directory on the VM.
  - question: Which repository should I clone for the sample application?
    answer: >-
      Clone the People.WebApp repository from [GitHub](https://github.com/dawidborycki/People.WebApp.git)
      using `git`.
  - question: How do I build the Docker image for the sample application?
    answer: >-
      From the `People.WebApp` folder, run `sudo docker build -t people.webapp:v1 .`. The `-t` flag
      assigns the image name and tag, while `.` sets the current folder as the build context.
  - question: What should I check if the app isn't reachable from the Internet?
    answer: >-
      Verify the VM’s network security group is configured to expose the application. After updating
      the rule, test access using the VM’s public IP address.
# END generated_summary_faq

author: Dawid Borycki

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
platforms:
  - Microsoft Azure Cobalt

armips:
    - Neoverse

tools_software_languages:
    - dotnet
    - csharp

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
