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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:46:43Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e32bdb090c422d1fb5bb1f9bd3af56c55fdf8989e6a7fe6a101e90dcb6f3eadd
  summary_generated_at: '2026-06-02T03:43:01Z'
  summary_source_hash: e32bdb090c422d1fb5bb1f9bd3af56c55fdf8989e6a7fe6a101e90dcb6f3eadd
  faq_generated_at: '2026-06-03T00:46:43Z'
  faq_source_hash: e32bdb090c422d1fb5bb1f9bd3af56c55fdf8989e6a7fe6a101e90dcb6f3eadd
  summary: >-
    This Learning Path shows how to build and deploy a multi-architecture container application
    for x86/amd64 and arm64 on Amazon EKS using docker buildx and docker manifest. You will create
    a hybrid EKS cluster with both x86 and Arm-based (Graviton) nodes, then build images for each
    architecture and understand the key nuances of multi-arch container builds. The environment
    assumes Linux, and you need an AWS account plus eksctl, kubectl, and Docker installed locally.
    By the end, you will have deployed a multi-arch application to a single EKS cluster that can
    run across both architectures. The topic is advanced and is designed for developers targeting
    multi-arch Kubernetes on AWS.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need an AWS account and a Linux machine with eksctl, kubectl, and Docker installed.
      No other prerequisites are explicitly listed.
  - question: Which tools are used to build multi-architecture images, and where do I run them?
    answer: >-
      You will use docker buildx and docker manifest. These are run with your local Docker installation.
  - question: How is the Amazon EKS cluster set up for multiple architectures?
    answer: >-
      You create a hybrid EKS cluster that includes both x86/amd64 and Arm-based (Graviton) nodes.
      This lets you run workloads across both architectures in a single cluster.
  - question: What result should I expect after deployment?
    answer: >-
      A multi-architecture container application runs on a single Amazon EKS cluster that supports
      both arm64 and amd64. The image you build is suitable for both architectures using a multi-arch
      manifest.
  - question: What should I check if the application only runs on one node type?
    answer: >-
      Confirm that you built images for both amd64 and arm64 and that your docker manifest includes
      both. Also verify your EKS cluster has both x86 and Arm-based (Graviton) nodes available.
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

