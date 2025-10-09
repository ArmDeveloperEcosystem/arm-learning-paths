---
title: Add Arm nodes to your AKS cluster using a multi-architecture nginx container image 

minutes_to_complete: 30

who_is_this_for: This Learning Path is for developers who want to compare the performance of amd64 and arm64 deployments by running nginx on a hybrid AKS cluster using a multi-architecture container image.

learning_objectives:
  - Create a hybrid AKS cluster with amd64 and arm64 nodes.
  - Deploy nginx services for amd64 and arm64 architectures using a single multi-architecture container image.
  - Validate deployments by testing nginx responses to compare architecture performance.

prerequisites:
    - An [Azure account](https://azure.microsoft.com/en-us/free/).
    - A local machine with [Azure CLI](/install-guides/azure-cli/) and [kubectl](/install-guides/kubectl/) installed.
   
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
      title: Create an External Load Balancer 
      link: https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
