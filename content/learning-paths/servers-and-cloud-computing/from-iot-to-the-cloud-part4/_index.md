---
title: 'Use Infrastructure as Code and Pulumi to provision Azure resources'
description: Learn how to automate Azure resource deployment using Infrastructure as Code with Pulumi to provision Azure Container Instances for containerized applications.

minutes_to_complete: 30

who_is_this_for: 'This is an introductory topic for developers interested in learning how to automate their cloud deployments using the Infrastructure as Code (IaC).'

learning_objectives: 
    - Automate the deployment of all the Azure resources required to deploy a containerized application to the Azure Container Instance.
    - Set up Pulumi for Infrastructure as Code (IaC).
    - Automate the provisioning of the Azure resources.

prerequisites:
    - 'Azure subscription. Use this link to sign up for a free account: https://azure.microsoft.com/en-us/free/'
    - 'Visual Studio Code'
    - 'A free Pulumi account and Pulumi CLI (details provided in this learning path)'
    - 'Node.js (details provided in this learning path)'
    - 'Azure CLI (details provided in this learning path)'

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:56:53Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 1510c787979257e191196e13999e98c20ca24d0857f72075649c28520c74c576
  summary_generated_at: '2026-06-02T03:56:05Z'
  summary_source_hash: 1510c787979257e191196e13999e98c20ca24d0857f72075649c28520c74c576
  faq_generated_at: '2026-06-03T00:56:53Z'
  faq_source_hash: 1510c787979257e191196e13999e98c20ca24d0857f72075649c28520c74c576
  summary: >-
    Learn how to use Infrastructure as Code with Pulumi to automate Azure resource deployment
    on Windows. You will install and configure Node.js, the Pulumi CLI, and the Azure CLI, then
    create a Pulumi TypeScript project in Visual Studio Code. The path shows the Pulumi project
    structure and how to declare an Azure Resource Group and an Azure Container Instance that
    runs a sample container image. By the end, you will provision the required Azure resources
    with Pulumi. Prerequisites include an Azure subscription, Visual Studio Code, a free Pulumi
    account with the Pulumi CLI, Node.js, and the Azure CLI. No additional prerequisites are explicitly
    listed.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Windows environment, an Azure subscription (a free account link is provided),
      Visual Studio Code, a free Pulumi account with the Pulumi CLI, Node.js, and the Azure CLI.
      The setup step in the path provides installer links.
  - question: Which installers should I use on Windows?
    answer: >-
      Install Node.js for Arm64 using the MSI linked in the setup step, then install the Pulumi
      CLI and the Azure CLI using the Windows installers provided. Follow the path’s setup instructions
      in order.
  - question: Which Pulumi runtime and language does this path use?
    answer: >-
      The project uses TypeScript on Node.js with Pulumi’s Azure Native provider. You will edit
      index.ts to declare Azure resources.
  - question: After creating the Pulumi app, what should I see in the project?
    answer: >-
      Open the azure-aci folder in Visual Studio Code and expect a typical Node.js layout plus
      Pulumi.yaml. Pulumi.yaml contains the global project configuration such as name, runtime,
      and description.
  - question: What result should I expect after updating index.ts and deploying?
    answer: >-
      The Pulumi deployment provisions an Azure Resource Group and an Azure Container Instance
      using a sample ASP.NET Docker image. You should see these resources created in your Azure
      subscription.
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
    - TypeScript  
    - Docker    

operatingsystems:
    - Windows

further_reading:
    - resource:
        title: Infrastructure as code
        link: https://learn.microsoft.com/en-us/devops/deliver/what-is-infrastructure-as-code
        type: Documentation
    - resource:
        title: Pulumi
        link: https://www.pulumi.com
        type: Documentation
    - resource:
        title: Terraform
        link: https://www.terraform.io
        type: Documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

