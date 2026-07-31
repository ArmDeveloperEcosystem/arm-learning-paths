---
title: Learn how to build and deploy a multi-architecture application on Amazon EKS
description: Learn how to use docker buildx and docker manifest to build and deploy multi-architecture container images with x86/amd64 and arm64 support on Amazon EKS.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for software developers who want to understand how to build and deploy a multi-architecture application with x86/amd64 and arm64-based container images on Amazon Elastic Kubernetes Service (EKS).

learning_objectives: 
    - Build x86/amd64 and arm64 container images with docker buildx and docker manifest
    - Understand the nuances of building a multi-architecture container image
    - Deploy a multi-arch container application across multiple architectures in a single Amazon EKS cluster

prerequisites:
    - An [AWS account](https://aws.amazon.com/). Create an account if needed.
    - A computer with [Amazon eksctl CLI](/install-guides/eksctl) and [kubectl](/install-guides/kubectl/)installed.
    - Docker installed on local computer [Docker](/install-guides/docker)

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-27T18:55:08Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: e32bdb090c422d1fb5bb1f9bd3af56c55fdf8989e6a7fe6a101e90dcb6f3eadd
  summary_generated_at: '2026-07-27T18:55:08Z'
  summary_source_hash: e32bdb090c422d1fb5bb1f9bd3af56c55fdf8989e6a7fe6a101e90dcb6f3eadd
  faq_generated_at: '2026-07-27T18:55:08Z'
  faq_source_hash: e32bdb090c422d1fb5bb1f9bd3af56c55fdf8989e6a7fe6a101e90dcb6f3eadd
  summary: >-
    You'll build `amd64` and `arm64` container images with Docker Buildx, publish a multi-architecture
    manifest, and deploy it to a hybrid Amazon EKS cluster. You'll configure Arm-based Graviton and
    x86 nodes, publish both variants under one image tag, and verify that Kubernetes selects the right
    image for each node. By the end, one deployment will run across both architectures in the cluster.
  faqs:
  - question: Which platforms should I target when I build the images?
    answer: >-
      Build two variants: `amd64` for x86 and `arm64` for Arm-based nodes powered by Graviton. These two images
      form the basis for your multi-architecture manifest.
  - question: When should I create the Docker manifest, and what should it include?
    answer: >-
      Create the manifest after you build the per-architecture images. It should reference both
      the `amd64` and `arm64` images under a single tag.
  - question: How do I know if my EKS cluster has both Arm and x86 nodes before I deploy?
    answer: >-
      Confirm that the cluster includes `arm64` and `amd64` node groups. Use `kubectl` to inspect
      node details and verify that both architectures are present.
  - question: What result should I expect when I deploy the multi-arch image to the cluster?
    answer: >-
      Kubernetes schedules pods onto either node type, and each node pulls the correct image variant
      from the multi-arch tag. You should see the same application running across both architectures.
  - question: What should I check if my workload only runs on one architecture?
    answer: >-
      Verify that the cluster includes both `arm64` and `amd64` nodes and that your manifest lists
      both image variants. Also check that your deployment uses the multi-architecture image tag, not
      an architecture-specific one.
# END generated_summary_faq

author: Pranay Bakre

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
cloud_service_providers:
  - AWS
armips:
    - Neoverse
tools_software_languages:
    - Kubernetes
    - Amazon EKS
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
