---
title: Create an Arm-based Kubernetes cluster on Microsoft Azure Kubernetes Service

description: Learn how to automate the deployment of an Arm-based Kubernetes cluster on Azure AKS using Terraform and deploy a sample WordPress application as a workload.

minutes_to_complete: 60   

who_is_this_for: This is an advanced topic for software developers who want to deploy an Arm-based Kubernetes cluster using Azure Kubernetes Service (AKS).

learning_objectives: 
    - Automate the deployment of an Arm-based AKS cluster using Terraform
    - Install Wordpress on AKS as an example workload

prerequisites:
    - An Azure account
    - A machine with [Terraform](/install-guides/terraform/), [Azure CLI](/install-guides/azure-cli), and [Kubectl](/install-guides/kubectl/) installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-26T17:19:52Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 01c5cc8930650a8d81d67d4c48b62e0f9d7b1ebfc2d09a552e11046fb982fc52
  summary_generated_at: '2026-06-26T17:19:52Z'
  summary_source_hash: 01c5cc8930650a8d81d67d4c48b62e0f9d7b1ebfc2d09a552e11046fb982fc52
  faq_generated_at: '2026-06-26T17:19:52Z'
  faq_source_hash: 01c5cc8930650a8d81d67d4c48b62e0f9d7b1ebfc2d09a552e11046fb982fc52
  summary: >-
    You'll automate an Arm-based Azure Kubernetes Service (AKS) cluster deployment
    with Terraform and then deploy a WordPress example workload. You'll start by configuring AKS to use Azure
    Dpsv5 virtual machines based on Ampere Altra Arm processors by following Terraform-driven
    provisioning steps. After the cluster is available, you'll use a concise Kubernetes setup to run
    WordPress backed by MySQL by creating three manifests: `kustomization.yaml`, `mysql-deployment.yaml`,
    and `wordpress-deployment.yaml`. The result is a working application on an Arm-based AKS node
    pool, with a clear separation between cluster provisioning and workload deployment to support
    repeatable infrastructure-as-code workflows.
  faqs:
  - question: Can I run Terraform and `kubectl` from my laptop, or do I need an Azure VM?
    answer: >-
      You can use any computer with the required tools installed, including a desktop, laptop,
      or a virtual machine. The steps don't require running on an Azure VM.
  - question: How do I confirm the AKS cluster was created successfully before deploying workloads?
    answer: >-
      Verify that the AKS resource appears in the Azure portal and is reported as available. You
      can proceed after the cluster is up and reachable with your configured tooling.
  - question: How do I ensure the AKS node pool is Arm-based?
    answer: >-
      Configure the node pool in Terraform to use an Azure Dpsv5 VM size, which runs on Ampere
      Altra Arm-based processors. Confirm that the VM size in your configuration references a
      Dpsv5 option.
  - question: Which files do I need to create for the WordPress example?
    answer: >-
      Create `kustomization.yaml`, `mysql-deployment.yaml`, and `wordpress-deployment.yaml` exactly
      as shown in the Learning Path. The `kustomization.yaml` file includes a `secretGenerator` entry for
      a secret named `mysql-pass`.
  - question: What result should I expect after applying the WordPress manifests?
    answer: >-
      Kubernetes resources for MySQL and WordPress are created as defined in the YAML files. Continue
      after the deployment is reported as ready by your tooling and the resources appear as expected.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
