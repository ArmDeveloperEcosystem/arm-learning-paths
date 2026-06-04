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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:15:11Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 01c5cc8930650a8d81d67d4c48b62e0f9d7b1ebfc2d09a552e11046fb982fc52
  summary_generated_at: '2026-06-02T03:03:59Z'
  summary_source_hash: 01c5cc8930650a8d81d67d4c48b62e0f9d7b1ebfc2d09a552e11046fb982fc52
  faq_generated_at: '2026-06-03T00:15:11Z'
  faq_source_hash: 01c5cc8930650a8d81d67d4c48b62e0f9d7b1ebfc2d09a552e11046fb982fc52
  summary: >-
    This Learning Path shows how to automate the creation of an Arm-based Azure Kubernetes Service
    (AKS) cluster using Terraform and then deploy a WordPress example workload backed by MySQL.
    You will target Azure Dpsv5 virtual machines featuring Ampere Altra Arm-based processors and
    use the Azure CLI and kubectl alongside Terraform. The steps include provisioning the AKS
    cluster and applying three Kubernetes manifests (kustomization.yaml, mysql-deployment.yaml,
    and wordpress-deployment.yaml) adapted from the Kubernetes WordPress tutorial. Prerequisites
    are an Azure account and a machine with Terraform, Azure CLI, and kubectl installed; the instructions
    target a Linux environment. By the end, you will have a running AKS cluster and a deployed
    WordPress example.
  faqs:
  - question: What do I need before running the Terraform deployment?
    answer: >-
      You need an Azure account and a machine with Terraform, Azure CLI, and kubectl installed.
      The Learning Path assumes these tools are ready before you start.
  - question: Which Azure VM series is used for Arm-based AKS nodes in this path?
    answer: >-
      The path uses the Azure Dpsv5 Virtual Machine series featuring Ampere Altra Arm-based processors.
      AKS can run on this series to provide Arm-based compute.
  - question: Can I run the setup steps from my local computer or a virtual machine?
    answer: >-
      Yes. Any computer with the required tools installed can be used, including your desktop,
      laptop, or a virtual machine.
  - question: What files do I create to deploy the WordPress example?
    answer: >-
      You will create three Kubernetes YAML files: kustomization.yaml, mysql-deployment.yaml,
      and wordpress-deployment.yaml. These are modified from the Kubernetes WordPress Tutorial.
  - question: How do I know I’m ready to deploy WordPress to the cluster?
    answer: >-
      You should have an AKS cluster already running from the previous topic. Once the cluster
      is provisioned, proceed to create the YAML files and deploy the example workload.
# END generated_summary_faq

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

