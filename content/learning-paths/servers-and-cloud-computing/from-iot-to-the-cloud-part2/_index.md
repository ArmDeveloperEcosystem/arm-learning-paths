---
title: 'Deploy a containerized application using Azure Container Instances'
description: Learn how to create and run Docker containers on Azure Container Instances for Arm64-based containerized application deployment.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers interested in learning how to create and run a Docker container in Microsoft Azure using Azure Container Instances.

learning_objectives: 
    - Create Azure Container Instances.
    - Run a Docker container in Azure Container Instances.
    - Enable Admin in Azure Container Registry, which is required when you are deploying Docker containers from the Azure Container Registry.

prerequisites:
    - 'Azure subscription. Use this link to sign up for a free account: https://azure.microsoft.com/en-us/free/.'
    - 'Complete the [first learning path](/learning-paths/servers-and-cloud-computing/from-iot-to-the-cloud-part1) of this series.'  

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:55:15Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3823ad3df8ae868acfd59b5b5b541240624572fe739aaf2275185d5cd3578032
  summary_generated_at: '2026-06-02T03:54:18Z'
  summary_source_hash: 3823ad3df8ae868acfd59b5b5b541240624572fe739aaf2275185d5cd3578032
  faq_generated_at: '2026-06-03T00:55:15Z'
  faq_source_hash: 3823ad3df8ae868acfd59b5b5b541240624572fe739aaf2275185d5cd3578032
  summary: >-
    This introductory Learning Path shows how to create an Azure Container Instance (ACI) and
    run a Docker container on Microsoft Azure. You will provision ACI through the Azure Portal
    and Cloud Shell, enable the Admin account in Azure Container Registry (ACR) when deploying
    from ACR, and verify the containerized ASP.NET sample application by browsing to the instance’s
    public IP on port 8080. At the time of writing, ACI was not yet compatible with Arm64 Docker
    containers, so the steps use a sample image from the Microsoft Container Registry. Prerequisites
    are an active Azure subscription and completion of the first part of this series. The path
    can be followed from Linux or Windows.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need an active Azure subscription and you must complete the first learning path in this
      series. No other explicit prerequisites are listed.
  - question: Which container image should I use for Azure Container Instances in this path?
    answer: >-
      Use the sample ASP.NET application image from the Microsoft Container Registry: mcr.microsoft.com/dotnet/samples:aspnetapp.
      At the time of writing, Azure Container Instances was not yet compatible with arm64 Docker
      containers.
  - question: Where do I run the Azure CLI commands shown in the steps?
    answer: >-
      Open the Azure Portal and launch Cloud Shell using the icon in the top-right corner. Run
      the provided commands directly in Cloud Shell.
  - question: How do I enable and verify the Azure Container Registry Admin account?
    answer: >-
      Enable the Admin account in your Azure Container Registry because it is required by Azure
      Container Instances when deploying from ACR. In Cloud Shell, run az acr list -o table and
      check the ADMIN ENABLED column to confirm.
  - question: How do I access the running application and what port should I use?
    answer: >-
      In the Container Instance Overview tab, copy the public IP address and open it in a browser
      using port 8080 (for example, http://IP_ADDRESS:8080). If the deployment succeeded, the
      application should load in the browser.
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
    - ASP.NET Core    
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

