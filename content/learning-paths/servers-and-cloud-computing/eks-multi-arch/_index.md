---
title: Learn how to build and deploy a multi-architecture application on Amazon EKS

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for software developers who want to understand how to build and deploy a multi-architecture application with x86/amd64 and arm64-based container images on Amazon EKS

learning_objectives: 
    - Build x86/amd64 and arm64 container images with docker buildx and docker manifest
    - Understand the nuances of building a multi-architecture container image
    - Deploy a multi-arch container application across multiple architectures in a single Amazon EKS cluster

prerequisites:
    - An [AWS account](https://aws.amazon.com/). Create an account if needed.
    - A computer with [Amazon eksctl CLI](/install-guides/eksctl) and [kubectl](/install-guides/kubectl/)installed.
    - Docker installed on local computer [Docker](/install-guides/docker)

author: Pranay Bakre

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
cloud_service_providers:
  - AWS
armips:
    - Neoverse
tools_software_languages:
    - Kubernetes
    - AWS Elastic Kubernetes Service (EKS)
operatingsystems:
    - Linux


further_reading:
    - resource:
        title: EKS documentation
        link: https://aws.amazon.com/eks/
        type: documentation
    - resource:
        title: Amazon Elastic Container Registry
        link: https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html?pg=ln&sec=hs
        type: documentation




### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
