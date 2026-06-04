---
title: 'Deploy an application to Azure Kubernetes Service'
description: Learn how to create an Azure Kubernetes Service cluster with Arm64 virtual machines and deploy a containerized application to AKS.

minutes_to_complete: 45

who_is_this_for: This learning path is dedicated to developers interested in learning how to deploy applications to the Azure Kubernetes Cluster powered by arm64-based virtual machines.

learning_objectives: 
    - Create a Kubernetes cluster using the Azure Kubernetes Service.
    - Deploy a containerized application to the Azure Kubernetes Service.

prerequisites:
    - 'Azure subscription. Use this link to sign up for a free account: https://azure.microsoft.com/en-us/free/.'
    - 'Complete the [first](/learning-paths/servers-and-cloud-computing/from-iot-to-the-cloud-part1) and [second](/learning-paths/servers-and-cloud-computing/from-iot-to-the-cloud-part2) learning paths of this series.'
  

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:55:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a3347a62c3322d88b80fc7848fa5ee1d92ee86333c2a21891b958286f8b70935
  summary_generated_at: '2026-06-02T03:55:07Z'
  summary_source_hash: a3347a62c3322d88b80fc7848fa5ee1d92ee86333c2a21891b958286f8b70935
  faq_generated_at: '2026-06-03T00:55:54Z'
  faq_source_hash: a3347a62c3322d88b80fc7848fa5ee1d92ee86333c2a21891b958286f8b70935
  summary: >-
    This introductory Learning Path shows how to create an Azure Kubernetes Service (AKS) cluster
    backed by arm64-based virtual machines, connect to it, and deploy a containerized application.
    You will provision the cluster in the Azure Portal with integration to Azure Container Registry,
    then use Azure Cloud Shell and kubectl to access and manage it. Deployment is driven by Kubernetes
    YAML that defines a Deployment and a Service. Tools listed include Docker, Kubernetes, and
    ASP.NET Core, targeting Linux. Prerequisites are an active Azure subscription and completion
    of the first and second parts of this series. By the end, you will have an AKS cluster on
    Arm64 with an application running on it.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an Azure subscription and you must complete the first and second learning paths
      in this series. No other explicit prerequisites are listed.
  - question: How do I connect to the AKS cluster once it’s created?
    answer: >-
      Open Azure Cloud Shell and run: az aks get-credentials -g rg-arm64 -n aks-people. After
      the command completes, manage the cluster with kubectl.
  - question: Where do the container images for deployment come from?
    answer: >-
      The cluster is created with integration to Azure Container Registry. Images stored in that
      registry are available to the cluster for deployment as shown in this path.
  - question: What result should I expect after applying the Kubernetes YAML?
    answer: >-
      The Deployment creates one or more Pods, and the Service exposes the application. You should
      see the Pods running and the Service present in the cluster.
  - question: What should I check if kubectl commands fail after connecting?
    answer: >-
      Confirm you ran az aks get-credentials in Azure Cloud Shell and used the correct resource
      group and cluster name (for example, rg-arm64 and aks-people). If issues persist, re-run
      the command and try again from Cloud Shell as shown in the path.
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
    - Kubernetes

operatingsystems:
    - Linux

further_reading:
    - resource:
        title: Kubernetes
        link: https://kubernetes.io
        type: Documentation
    - resource:
        title: Azure Kubernetes Service
        link: https://azure.microsoft.com/en-us/products/kubernetes-service#overview
        type: Documentation
    - resource:
        title: kubectl Cheat Sheet
        link: https://kubernetes.io/docs/reference/kubectl/cheatsheet/
        type: Documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

