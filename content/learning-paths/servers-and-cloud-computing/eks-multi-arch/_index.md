---
title: Learn how to build and deploy a multi-architecture application on Amazon EKS
description: Learn how to use docker buildx and docker manifest to build and deploy multi-architecture container images with x86/amd64 and arm64 support on Amazon EKS.

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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:18Z'
  generator: template
  source_hash: e32bdb090c422d1fb5bb1f9bd3af56c55fdf8989e6a7fe6a101e90dcb6f3eadd
  summary: >-
    Learn how to use docker buildx and docker manifest to build and deploy multi-architecture
    container images with x86/amd64 and arm64 support on Amazon EKS. It is designed for software
    developers who want to understand how to build and deploy a multi-architecture application
    with x86/amd64 and arm64-based container images on Amazon EKS. By the end, you will be able
    to build x86/amd64 and arm64 container images with docker buildx and docker manifest, understand
    the nuances of building a multi-architecture container image, and deploy a multi-arch container
    application across multiple architectures in a single Amazon EKS cluster. It focuses on tools
    and technologies such as Kubernetes and AWS Elastic Kubernetes Service (EKS), Linux environments,
    Arm platforms including Neoverse, and cloud platforms such as AWS. The main steps cover Build
    and deploy a multi-arch application on Amazon EKS.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will build x86/amd64 and arm64 container images with docker buildx and docker manifest,
      understand the nuances of building a multi-architecture container image, and deploy a multi-arch
      container application across multiple architectures in a single Amazon EKS cluster. Learn
      how to use docker buildx and docker manifest to build and deploy multi-architecture container
      images with x86/amd64 and arm64 support on Amazon EKS.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for software developers who want to understand how to build and
      deploy a multi-architecture application with x86/amd64 and arm64-based container images
      on Amazon EKS.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: An [AWS account](https://aws.amazon.com/).
      Create an account if needed.; A computer with [Amazon eksctl CLI](/install-guides/eksctl)
      and [kubectl](/install-guides/kubectl/)installed.; Docker installed on local computer [Docker](/install-guides/docker).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Kubernetes and AWS Elastic Kubernetes Service (EKS),
      Linux environments, Arm platforms such as Neoverse, and cloud platforms such as AWS.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Build and deploy a multi-arch application on Amazon
      EKS.
# END generated_summary_faq

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

