---
title: Build a multi-architecture Kubernetes cluster with Arm and x86 nginx workloads on Azure AKS

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers who want to deploy multi-architecture Kubernetes workloads and compare `nginx` performance between x86 and Arm-based nodes in Azure Kubernetes Service (AKS) clusters.

learning_objectives:
    - Create a hybrid AKS cluster with both x86 and Arm64 nodes
    - Deploy `nginx` using multi-architecture container images across different node types
    - Verify `nginx` deployment and functionality on each architecture
    - Compare performance between x86 and Arm64 `nginx` instances
    - Learn techniques for deploying multi-architecture Kubernetes workloads
  

prerequisites:
    - An [Azure account](https://azure.microsoft.com/en-us/free/)
    - A local machine with [`jq`](https://jqlang.org/download/), [`curl`](https://curl.se/download.html), [`wrk`](https://github.com/wg/wrk), [Azure CLI](/install-guides/azure-cli/) and [`kubectl`](/install-guides/kubectl/) installed
   
author:
    - Geremy Cohen

### Tags
skilllevels: Introductory

subjects: Containers and Virtualization
cloud_service_providers: Microsoft Azure
    
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
      title: nginx - High Performance Load Balancer, Web Server, & Reverse Proxy
      link: https://nginx.org/
      type: documentation
  - resource:
      title: nginx Docker Hub
      link: https://hub.docker.com/_/nginx
      type: documentation
  - resource:
      title: Azure Kubernetes Service (AKS) documentation
      link: https://docs.microsoft.com/en-us/azure/aks/
      type: documentation
  - resource:
      title: Learn how to tune Nginx
      link: https://learn.arm.com/learning-paths/servers-and-cloud-computing/nginx_tune/
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
