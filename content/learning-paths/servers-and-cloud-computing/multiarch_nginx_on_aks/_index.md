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

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:35:04Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: d765afadfe5155f0ecd5bd08373fa12464b2ee5ebb1f8c7831039eb07eba8831
  summary_generated_at: '2026-06-02T04:31:12Z'
  summary_source_hash: d765afadfe5155f0ecd5bd08373fa12464b2ee5ebb1f8c7831039eb07eba8831
  faq_generated_at: '2026-06-03T01:35:04Z'
  faq_source_hash: d765afadfe5155f0ecd5bd08373fa12464b2ee5ebb1f8c7831039eb07eba8831
  summary: >-
    This Learning Path walks you through building a hybrid Azure Kubernetes Service (AKS) cluster
    with both Arm-based and x86 node pools on Linux, then deploying nginx using a multi-architecture
    image to each architecture. You authenticate with Azure CLI, create the cluster with two node
    pools, and verify access. You also create a small utility script to streamline kubectl operations
    and testing. The path adds a namespace and a shared ConfigMap with performance-optimized nginx
    settings, then creates architecture-specific deployments and LoadBalancer services. You validate
    that pods land on the intended nodes and use wrk to exercise traffic and compare behavior
    across architectures. Plan about 60 minutes to complete. Prerequisites are an Azure account
    and a local machine with jq, curl, wrk, Azure CLI, and kubectl installed.
  faqs:
  - question: What do I need before running the setup?
    answer: >-
      You need an Azure account and a local machine with jq, curl, wrk, Azure CLI, and kubectl
      installed. The path assumes a Linux environment.
  - question: How do I know my AKS cluster includes both x86 and Arm nodes?
    answer: >-
      During cluster creation, you provision two distinct node pools—one x86 and one Arm—and then
      verify connectivity. You will confirm that both node types are available from your AKS environment
      using the tools introduced in the steps.
  - question: Which files set up nginx on Intel, and what should I expect after applying them?
    answer: >-
      You use namespace.yaml and nginx-configmap.yaml along with the Intel-specific deployment
      manifest described in the steps. The result is an nginx deployment in a dedicated namespace
      and a load balancer service that exposes nginx to the Internet.
  - question: How is the Arm nginx deployment created and exposed?
    answer: >-
      Applying arm_nginx.yaml creates nginx-arm-deployment and nginx-arm-svc. It pulls a multi-architecture
      nginx image from DockerHub, schedules a pod on the Arm node, mounts the shared ConfigMap
      at /etc/nginx/nginx.conf, and exposes it via a load balancer service targeting pods with
      app: nginx-multiarch and arch: arm labels.
  - question: How do I compare performance between the x86 and Arm nginx instances?
    answer: >-
      Use the provided utility script and tools like wrk to send requests to each load-balanced
      service and observe results. Validate that both endpoints respond as expected, then compare
      behavior and performance across architectures.
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

