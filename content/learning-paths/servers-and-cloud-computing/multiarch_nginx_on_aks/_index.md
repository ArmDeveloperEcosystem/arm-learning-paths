---
title: Build a multi-architecture Kubernetes cluster running nginx on Azure AKS

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers who want to deploy multi-architecture Kubernetes workloads and compare nginx performance between x86 and Arm-based nodes in Azure Kubernetes Service (AKS) clusters.

learning_objectives:
    - Create a hybrid AKS cluster with both x86 and Arm64 nodes
    - Deploy nginx using multi-architecture container images across different node types
    - Verify nginx deployment and functionality on each architecture
    - Compare performance between x86 and Arm64 nginx instances
    - Learn techniques for deploying multi-architecture Kubernetes workloads
  

prerequisites:
    - An [Azure account](https://azure.microsoft.com/en-us/free/)
    - A local machine with [`jq`](https://jqlang.org/download/), [`curl`](https://curl.se/download.html), [`wrk`](https://github.com/wg/wrk), [Azure CLI](/install-guides/azure-cli/), and [`kubectl`](/install-guides/kubectl/) installed
   

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:18Z'
  generator: template
  source_hash: d765afadfe5155f0ecd5bd08373fa12464b2ee5ebb1f8c7831039eb07eba8831
  summary: >-
    Build a multi-architecture Kubernetes cluster running nginx on Azure AKS walks you through
    an end-to-end Arm software workflow. It is designed for developers who want to deploy multi-architecture
    Kubernetes workloads and compare nginx performance between x86 and Arm-based nodes in Azure
    Kubernetes Service (AKS) clusters. By the end, you will be able to create a hybrid AKS cluster
    with both x86 and Arm64 nodes, deploy nginx using multi-architecture container images across
    different node types, and verify nginx deployment and functionality on each architecture.
    It focuses on tools and technologies such as nginx, Web Server, Azure, and Kubernetes, Linux
    environments, Arm platforms including Neoverse, and cloud platforms such as Microsoft Azure.
    The main steps cover Start your journey with Arm and x86 nginx workloads on a single Kubernetes
    cluster, Create the AKS cluster, Create the test utility, Deploy nginx on Intel x86, and Deploy
    nginx on Arm.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will create a hybrid AKS cluster with both x86 and Arm64 nodes, deploy nginx using multi-architecture
      container images across different node types, and verify nginx deployment and functionality
      on each architecture.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers who want to deploy multi-architecture Kubernetes
      workloads and compare nginx performance between x86 and Arm-based nodes in Azure Kubernetes
      Service (AKS) clusters.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An [Azure account](https://azure.microsoft.com/en-us/free/);
      A local machine with [`jq`](https://jqlang.org/download/), [`curl`](https://curl.se/download.html),
      [`wrk`](https://github.com/wg/wrk), [Azure CLI](/install-guides/azure-cli/), and [`kubectl`](/install-guides/kubectl/)
      installed.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including nginx, Web Server, Azure, and Kubernetes, Linux
      environments, Arm platforms such as Neoverse, and cloud platforms such as Microsoft Azure.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Start your journey with Arm and x86 nginx workloads
      on a single Kubernetes cluster, Create the AKS cluster, Create the test utility, Deploy
      nginx on Intel x86, and Deploy nginx on Arm.
# END generated_summary_faq

author:
    - Geremy Cohen

### Tags
skilllevels: Introductory

subjects: Containers and Virtualization
cloud_service_providers:
  - Microsoft Azure
    
armips:
    - Neoverse

operatingsystems:
    - Linux

tools_software_languages:
    - nginx
    - Web Server
    - Azure
    - Kubernetes

further_reading:
  - resource:
      title: nginx website
      link: https://nginx.org/
      type: website
  - resource:
      title: nginx on Docker Hub
      link: https://hub.docker.com/_/nginx
      type: documentation
  - resource:
      title: Azure Kubernetes Service (AKS) documentation
      link: https://docs.microsoft.com/en-us/azure/aks/
      type: documentation
  - resource:
      title: Learn how to deploy nginx [Arm Learning Path]
      link: /learning-paths/servers-and-cloud-computing/nginx/
      type: documentation
  - resource:
      title: Learn how to tune nginx [Arm Learning Path]
      link: /learning-paths/servers-and-cloud-computing/nginx_tune/
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

