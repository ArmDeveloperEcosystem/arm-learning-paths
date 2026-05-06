---
title: Learn how to migrate an x86 application to multi-architecture with Arm-based on Google Axion Processor on GKE
description: Learn how to add Arm-based Google Axion nodes to an existing x86 GKE cluster and rebuild applications for multi-architecture support.

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for software developers who are looking to migrate their existing x86 containerized applications to Arm

learning_objectives: 
    - Add Arm-based nodes (Google Axion) to an existing x86-based GKE cluster
    - Rebuild an x86-based application to make it multi-arch and run on Arm
    - Learn how to add taints and tolerations to GKE clusters to schedule application pods on architecture specific nodes
    - Run a multi-arch application across multiple architectures on a single GKE cluster

prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/). Create an account if needed.
    - A computer with [Google Cloud CLI](/install-guides/gcloud) and [kubectl](/install-guides/kubectl/)installed.
    - An existing Google Kubernetes Engine (GKE) cluster with x86-based nodes

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:57Z'
  generator: template
  source_hash: 50715640292b60ea4216ee2211140c4212592a27356d628d945e83d9deb7fdcc
  summary: >-
    Learn how to add Arm-based Google Axion nodes to an existing x86 GKE cluster and rebuild applications
    for multi-architecture support. It is designed for software developers who are looking to
    migrate their existing x86 containerized applications to Arm. By the end, you will be able
    to add Arm-based nodes (Google Axion) to an existing x86-based GKE cluster, rebuild an x86-based
    application to make it multi-arch and run on Arm, and learn how to add taints and tolerations
    to GKE clusters to schedule application pods on architecture specific nodes. It focuses on
    tools and technologies such as Kubernetes and Runbook, Linux environments, Arm platforms including
    Neoverse, and cloud platforms such as Google Cloud. The main steps cover Build and deploy
    a multi-arch application on GKE.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will add Arm-based nodes (Google Axion) to an existing x86-based GKE cluster, rebuild
      an x86-based application to make it multi-arch and run on Arm, and learn how to add taints
      and tolerations to GKE clusters to schedule application pods on architecture specific nodes.
      Learn how to add Arm-based Google Axion nodes to an existing x86 GKE cluster and rebuild
      applications for multi-architecture support.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for software developers who are looking to migrate their existing
      x86 containerized applications to Arm.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud account](https://console.cloud.google.com/).
      Create an account if needed.; A computer with [Google Cloud CLI](/install-guides/gcloud)
      and [kubectl](/install-guides/kubectl/)installed.; An existing Google Kubernetes Engine
      (GKE) cluster with x86-based nodes.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Kubernetes and Runbook, Linux environments, Arm
      platforms such as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Build and deploy a multi-arch application on GKE.
# END generated_summary_faq

author: Pranay Bakre

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
cloud_service_providers:
  - Google Cloud

armips:
    - Neoverse

tools_software_languages:
    - Kubernetes
    - Runbook

operatingsystems:
    - Linux


further_reading:
    - resource:
        title: Create Arm based clusters and node pools 
        link: https://cloud.google.com/kubernetes-engine/docs/how-to/create-arm-clusters-nodes
        type: documentation
    - resource:
        title: Configure cluster access to use kubectl
        link: https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl
        type: documentation
    - resource:
        title: GKE documentation
        link: https://cloud.google.com/kubernetes-engine/docs
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

