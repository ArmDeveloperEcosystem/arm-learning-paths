---
title: Add Arm nodes to your Azure Kubernetes Services cluster using a multi-architecture nginx container image 

draft: true
cascade:
    draft: true

minutes_to_complete: 60

who_is_this_for: This Learning Path is for developers who want to compare the performance of x64 and arm64 deployments by running nginx on a hybrid Azure Kubernetes Service (AKS) cluster using nginx's multi-architecture container image.  Once you've seen how easy it is to add arm64 nodes to an existing cluster, you'll be ready to explore arm64-based nodes for other workloads in your environment.


learning_objectives:
  - Create a hybrid AKS cluster with x64 and arm64 nodes.
  - Deploy nginx's multi-architecture container image, pods, and services to the AKS cluster. 
  - Smoke test nginx from each architecture in the cluster to verify proper installation.
  - Performance test against each architecture in the cluster to better understand performance.
  

prerequisites:
    - An [Azure account](https://azure.microsoft.com/en-us/free/).
    - A local machine with [jq](https://jqlang.org/download/), [curl](https://curl.se/download.html), [wrk](https://github.com/wg/wrk), [Azure CLI](/install-guides/azure-cli/) and [kubectl](/install-guides/kubectl/) installed.
   
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
    - macOS

tools_software_languages:
    - nginx
    - Web Server

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
