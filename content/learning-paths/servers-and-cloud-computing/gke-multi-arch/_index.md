---
title: Learn how to migrate an x86 application to multi-architecture with Arm-based on Google Axion Processor on GKE
description: Learn how to add Arm-based Google Axion nodes to an existing x86 GKE cluster and rebuild applications for multi-architecture support.

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for software developers who are looking to migrate their existing x86 containerized applications to Arm

learning_objectives: 
    - Add Arm-based nodes powered by Google Axion to an existing x86-based Google Kubernetes Engine (GKE) cluster.
    - Rebuild an x86-based application to make it multi-arch and run on Arm.
    - Add taints and tolerations to GKE clusters to schedule application pods on architecture specific nodes.
    - Run a multi-arch application across multiple architectures on a single GKE cluster.

prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/)
    - A computer with [Google Cloud CLI](/install-guides/gcloud/) and [kubectl](/install-guides/kubectl/)installed
    - An existing GKE cluster with x86-based nodes

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T22:07:41Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c0d9ff6ae1aa155bc7f240a58ad1fb8800a4da5ac7b16224e5a0a1f3da1ccf6d
  summary_generated_at: '2026-09-10T22:07:41Z'
  summary_source_hash: c0d9ff6ae1aa155bc7f240a58ad1fb8800a4da5ac7b16224e5a0a1f3da1ccf6d
  faq_generated_at: '2026-09-10T22:07:41Z'
  faq_source_hash: c0d9ff6ae1aa155bc7f240a58ad1fb8800a4da5ac7b16224e5a0a1f3da1ccf6d
  summary: >-
    You'll extend an existing x86 GKE cluster with Arm capacity using Google Axion-based C4A nodes. First, you'll rebuild the application image for multiple architectures and configure taints and tolerations for scheduling. Then, you'll deploy workloads either to selected nodes or both architectures and verify that the multi-architecture image runs across the hybrid cluster.
  faqs:
  - question: Which GKE machine type should I use for the Arm-based nodes?
    answer: >-
      Use the C4A family of virtual machines. C4A is based on Google Axion with Armv9 Neoverse
      V2 CPUs.
  - question: How do I know my cluster now has both x86 and Arm nodes?
    answer: >-
      Use `kubectl` to inspect the node list and verify that C4A nodes are present alongside the
      existing x86 nodes. Check node details to confirm the architecture of each node.
  - question: When should I apply taints and tolerations?
    answer: >-
      Apply taints to architecture-specific nodes when you need to control where pods schedule.
      Add matching tolerations to pod specs so that workloads can target Arm or x86 nodes as intended.
  - question: Which image does each architecture-specific overlay deploy?
    answer: >-
      Apply the x86 overlay with the `x86-hello:v0.0.1` image or the Arm overlay with
      `arm-hello:v0.0.1`. Check the pod output to verify the reported CPU platform.
  - question: What should I check if pods don't schedule on the Arm nodes?
    answer: >-
      Verify that Arm-based C4A nodes are part of the cluster. Ensure taints and tolerations match,
      and confirm the image includes an Arm build. Resolve any mismatch before redeploying.
# END generated_summary_faq

author: Pranay Bakre

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
platforms:
  - Google Axion

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
