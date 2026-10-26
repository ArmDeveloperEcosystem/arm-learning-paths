---
title: 'Use Infrastructure as Code and Pulumi to provision Azure resources'
description: Learn how to automate Azure resource deployment using Infrastructure as Code with Pulumi to provision Azure Container Instances for containerized applications.

minutes_to_complete: 30

who_is_this_for: This Learning Path is an introductory topic for developers interested in automating their cloud deployments using Infrastructure as Code (IaC).

learning_objectives: 
    - Automate the deployment of all the Azure resources required to deploy a containerized application to the Azure Container Instance.
    - Set up Pulumi for Infrastructure as Code (IaC).
    - Automate the provisioning of the Azure resources.

prerequisites:
    - An [Azure account](https://azure.microsoft.com/en-us/free/)
    - Visual Studio Code
    - A free Pulumi account 

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T22:01:03Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 622019349aacd1aaec13bbf7991b56ead8f572210a7dda0fc1bac25a7287f58d
  summary_generated_at: '2026-09-10T22:01:03Z'
  summary_source_hash: 622019349aacd1aaec13bbf7991b56ead8f572210a7dda0fc1bac25a7287f58d
  faq_generated_at: '2026-09-10T22:01:03Z'
  faq_source_hash: 622019349aacd1aaec13bbf7991b56ead8f572210a7dda0fc1bac25a7287f58d
  summary: >-
    You'll use Pulumi on Windows to provision Azure Container Instances with TypeScript. First, you'll install the tooling, initialize a project, and inspect its configuration files. Then, you'll edit `index.ts` to define an Azure resource group and container group, and apply the program to create the resources. You can use the same code to update or destroy the deployment.
  faqs:
  - question: Which folder should I open in Visual Studio Code to work on the project?
    answer: >-
      Open the `azure-aci` directory and run `code .` from that folder. This loads
      the TypeScript project and its Pulumi files in Visual Studio Code.
  - question: What files should I see to confirm that the Pulumi TypeScript project is set up?
    answer: >-
      You should see `Pulumi.yaml` and a Node.js layout with `package.json` and `node_modules`.
      The program entry point `index.ts` is where you'll define Azure resources.
  - question: What do I change in `index.ts`?
    answer: >-
      Replace the original contents with the provided code that imports `@pulumi/azure-native/resources`
      and `@pulumi/azure-native/containerinstance`, creates a resource group named `rg-arm64-iac`,
      and defines a container group using the sample image `mcr.microsoft.com/dotnet/samples:aspnetapp`.
      Save the file before running the deployment.
  - question: How do I know that the deployment worked?
    answer: >-
      After Pulumi applies the changes, a new resource group named `rg-arm64-iac` and a container instance are created in your subscription. You can confirm that the deployment worked by checking the resource group
      and container instance in the Azure Portal.
  - question: Do I need to build or push a Docker image?
    answer: >-
      No. The example uses the public image `mcr.microsoft.com/dotnet/samples:aspnetapp` referenced
      in `index.ts`, so no local image build or registry push is required.
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
