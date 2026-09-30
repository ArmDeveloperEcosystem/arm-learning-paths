---
title: Deploy an application to Azure Kubernetes Service on Arm-based virtual machines
description: Learn how to create an Azure Kubernetes Service cluster with Arm64 virtual machines and deploy a containerized application to AKS.

minutes_to_complete: 45

who_is_this_for: This Learning Path is dedicated to developers interested in learning how to deploy applications to the Azure Kubernetes Cluster powered by arm64-based virtual machines.

learning_objectives: 
    - Create a Kubernetes cluster using the Azure Kubernetes Service (AKS).
    - Deploy a containerized application to AKS.

prerequisites:
    - An [Azure subscription](https://azure.microsoft.com/en-us/free/)
    - Completion of the [Deploy .NET applications to Arm virtual machines and Azure Container Registry](/learning-paths/servers-and-cloud-computing/from-iot-to-the-cloud-part1) and [Deploy a containerized application using Azure Container Instances](/learning-paths/servers-and-cloud-computing/from-iot-to-the-cloud-part2) Learning Paths

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T22:00:19Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 2b3da4a3eff7a7be18e2f18313488149430c85ecc943486e92668ce8a5e59a5e
  summary_generated_at: '2026-09-10T22:00:19Z'
  summary_source_hash: 2b3da4a3eff7a7be18e2f18313488149430c85ecc943486e92668ce8a5e59a5e
  faq_generated_at: '2026-09-10T22:00:19Z'
  faq_source_hash: 2b3da4a3eff7a7be18e2f18313488149430c85ecc943486e92668ce8a5e59a5e
  summary: >-
    You'll create an AKS cluster with Arm64-based nodes, connect it to Azure Container Registry, and deploy an application with Kubernetes manifests. Then, you'll retrieve credentials, use `kubectl` to manage the cluster, and expose the workload with a service. You can create the cluster manually or use Terraform.
  faqs:
  - question: How do I select an arm64 node size for the AKS cluster?
    answer: >-
      In the AKS creation wizard, open **Node pools**, select **Standard DS2_v2 (change)**, and
      choose **Manual** scaling. Set the node count to **1**, select **Choose a size**, choose
      **D2pds_v5**, and select **Select**.
  - question: How do I connect kubectl to the newly created cluster?
    answer: >-
      Open Azure Cloud Shell and run `az aks get-credentials -g rg-arm64 -n aks-people`.
  - question: What Kubernetes resources does the application manifest create?
    answer: >-
      The manifest defines a deployment and a service. The deployment creates the application pods, and
      the service exposes those pods for access within the cluster.
  - question: Where should my container images be hosted for this setup?
    answer: >-
      The cluster is created with integration to Azure Container Registry. Use that registry to
      host the images that are referenced by your deployment.
  - question: What should I check if kubectl can't reach the cluster after connecting?
    answer: >-
      Confirm that you ran `az aks get-credentials` in Cloud Shell with the correct resource group (`rg-arm64`)
      and cluster name (`aks-people`), then run `kubectl get nodes`. If the request fails, check the active
      kubeconfig context and your access to the cluster before retrying.
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
