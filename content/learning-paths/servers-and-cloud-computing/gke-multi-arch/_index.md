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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:05:07Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 50715640292b60ea4216ee2211140c4212592a27356d628d945e83d9deb7fdcc
  summary_generated_at: '2026-06-02T04:02:44Z'
  summary_source_hash: 50715640292b60ea4216ee2211140c4212592a27356d628d945e83d9deb7fdcc
  faq_generated_at: '2026-06-03T01:05:07Z'
  faq_source_hash: 50715640292b60ea4216ee2211140c4212592a27356d628d945e83d9deb7fdcc
  summary: >-
    This Learning Path shows how to extend an existing x86-based Google Kubernetes Engine (GKE)
    cluster with Arm-based Google Axion nodes and rebuild an x86 application for multi-architecture
    support. You will add C4A virtual machine nodes (based on Google Axion with Armv9 Neoverse
    V2 CPUs), rebuild your container to run on Arm, and use Kubernetes taints and tolerations
    to schedule pods on architecture-specific nodes. The path targets Linux and uses Google Cloud
    with Kubernetes tooling, including the Google Cloud CLI and kubectl. By the end, you will
    run a multi-arch application across both Arm and x86 within a single GKE cluster and validate
    placement through scheduling controls.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Google Cloud account, Google Cloud CLI, kubectl installed on your local machine,
      and an existing Google Kubernetes Engine (GKE) cluster with x86-based nodes.
  - question: Which VM type should I use for the Arm-based node pool?
    answer: >-
      Use the C4A family of virtual machines. These nodes are based on Google Axion, built using
      the Armv9 Neoverse V2 CPU.
  - question: How do I rebuild my existing x86 application for multi-architecture?
    answer: >-
      The path guides you to rebuild your container image so it supports both Arm and x86. You
      then deploy the new multi-arch image to the hybrid GKE cluster.
  - question: How will I control which pods run on Arm versus x86 nodes?
    answer: >-
      You will add taints to the Arm-based nodes and apply matching tolerations to your workloads
      so only compatible pods schedule there. The steps show how to configure these settings for
      architecture-specific placement.
  - question: How do I know the application is running on the intended architecture?
    answer: >-
      Use kubectl to inspect pod placement and confirm pods are scheduled onto Arm-based nodes
      and x86 nodes as configured. The path explains the checks to perform after deployment.
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

