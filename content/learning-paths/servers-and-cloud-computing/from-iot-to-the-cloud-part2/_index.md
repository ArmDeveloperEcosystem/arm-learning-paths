---
title: Deploy a containerized application using Azure Container Instances
description: Learn how to create and run Docker containers on Azure Container Instances for Arm64-based containerized application deployment.

minutes_to_complete: 30

who_is_this_for: This Learning Path is an introductory topic for developers interested in creating and running a Docker container in Microsoft Azure using Azure Container Instances (ACI).

learning_objectives: 
    - Create a container instance on ACI.
    - Run a Docker container in ACI.
    - Enable Admin in Azure Container Registry (ACR), which is required when you're deploying Docker containers from the ACR.

prerequisites:
    - An [Azure subscription](https://azure.microsoft.com/en-us/free/)
    - Completion of the [Deploy .NET applications to Arm virtual machines and Azure Container Registry](/learning-paths/servers-and-cloud-computing/from-iot-to-the-cloud-part1) Learning Path

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T21:59:50Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 64dda5e172cd25a25cb8b75a22d2472eab2e99ab9ac646617832d9ff91bc9296
  summary_generated_at: '2026-09-10T21:59:50Z'
  summary_source_hash: 64dda5e172cd25a25cb8b75a22d2472eab2e99ab9ac646617832d9ff91bc9296
  faq_generated_at: '2026-09-10T21:59:50Z'
  faq_source_hash: 64dda5e172cd25a25cb8b75a22d2472eab2e99ab9ac646617832d9ff91bc9296
  summary: >-
    You'll create an instance in ACI, run a sample ASP.NET container, and verify connectivity on port `8080`. Then, you'll inspect the public IP, use Azure Cloud Shell to check the container registry, and enable the ACR Admin account required for registry-based deployment. 
  faqs:
  - question: Which container image should I use to create the first instance?
    answer: >-
      Use the Microsoft sample ASP.NET image: `mcr.microsoft.com/dotnet/samples:aspnetapp`.
  - question: How do I find the public IP and verify the application is running?
    answer: >-
      Open the **Overview** tab of the **aspnet-sample** container instance and copy the public IP address.
      Paste the IP into a browser with port `8080` (for example, IP:8080) and check that the page
      loads.
  - question: What should I check if the browser doesn't load the app on port 8080?
    answer: >-
      Confirm that the container instance has finished provisioning and is running. Verify that you're
      using the correct Public IP and port 8080.
  - question: How do I confirm that my registry is ready for deployment?
    answer: >-
      In Azure Cloud Shell, run `az acr list -o table` and check the `ADMIN ENABLED` column. If it's not enabled, turn on the admin account in the registry settings before deploying to ACI.
  - question: Can I deploy an arm64 container image to ACI?
    answer: >-
      At the time covered by this Learning Path, ACI is described as incompatible with `arm64`
      Docker containers. Use the provided Microsoft sample image to validate the ACI workflow, and
      check the current Azure documentation if you need to confirm the service's present capabilities.
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
    - aspnetcore    
    - Docker
operatingsystems:
    - Linux
    - Windows

further_reading:
    - resource:
        title: Docker
        link: https://www.docker.com
        type: Documentation
    - resource:
        title: Azure Container Registry
        link: https://learn.microsoft.com/en-GB/azure/container-registry/container-registry-concepts
        type: Documentation
    - resource:
        title: Azure Container Instances
        link: https://learn.microsoft.com/en-us/azure/container-instances/
        type: Documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
