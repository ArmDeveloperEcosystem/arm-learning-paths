---
title: Migrate x86 workloads to Arm on Google Kubernetes Engine with Axion processors 

minutes_to_complete: 90
description: Learn how to create dual-architecture GKE clusters with arm64 and amd64 node pools, build multi-architecture Docker images, and migrate services to Google Axion processors.
who_is_this_for: This is an advanced topic for cloud, platform, and site reliability engineers who operate Kubernetes on Google Cloud and need to build multi-architecture images and migrate services from x86 to Arm using Google Axion processors.

learning_objectives:
    - Prepare Dockerfiles for multi-architecture builds by adding arm64 support.
    - Create a dual-architecture Google Kubernetes Engine (GKE) standard cluster with amd64 and arm64 node pools. 
    - Build and publish multi-architecture images to Artifact Registry using Docker Buildx.
    - Deploy a Kubernetes application on amd64, then migrate to arm64 using Kustomize overlays.
    - Automate builds and rollouts with Cloud Build and Skaffold.

prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/) with billing enabled
    - A local Linux or macOS computer with access to Google Cloud Shell, or Docker, Kubernetes CLI (`kubectl`), Google Cloud CLI (`gcloud`), and Git installed 
    - Basic familiarity with Docker, Kubernetes, and `gcloud`

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T22:07:20Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: f0dce02a5aa233f5eaf2f9c61b25399a7effb5d2be9d08465db6c0055095f696
  summary_generated_at: '2026-09-10T22:07:20Z'
  summary_source_hash: f0dce02a5aa233f5eaf2f9c61b25399a7effb5d2be9d08465db6c0055095f696
  faq_generated_at: '2026-09-10T22:07:20Z'
  faq_source_hash: f0dce02a5aa233f5eaf2f9c61b25399a7effb5d2be9d08465db6c0055095f696
  summary: >-
    You'll migrate a multi-service application from x86 to Arm on GKE. First, you'll create amd64 and arm64 node pools, update Dockerfiles, build multi-architecture images, and push them to Artifact Registry. Then, Kustomize overlays direct deployments to each architecture, allowing you to validate the application first on x86 and then on Arm.
  faqs:
  - question: How do I know the cluster has both amd64 and arm64 capacity before building images?
    answer: >-
      For the native GKE Buildx workflow, list your GKE nodes and check the architecture labels to
      confirm both amd64 and arm64 node pools are present and ready. You can then run each BuildKit
      pod on the matching architecture. If you choose Cloud Build, use its own runner with QEMU instead.
  - question: Which services need Dockerfile updates for multi-architecture builds?
    answer: >-
      Four services require small changes: `emailservice`, `recommendationservice`, `loadgenerator`,
      and `cartservice`. The edits ensure that the correct compiler headers and runtime libraries are
      included for each architecture.
  - question: Which build workflow avoids QEMU emulation?
    answer: >-
      Use the GKE-backed Buildx workflow. It runs separate BuildKit pods on the amd64 and arm64
      node pools, so each platform builds natively. The alternative Cloud Build workflow enables
      QEMU in its runner for cross-architecture builds.
  - question: How do I direct a deployment to Arm nodes and later switch from x86?
    answer: >-
      Use Kustomize overlays that select nodes by architecture and reference your Artifact Registry
      images. Apply the overlay for amd64 first, then apply the arm64 overlay to migrate the workload
      to Axion-based nodes.
  - question: What should I check if cluster creation fails due to networking?
    answer: >-
      GKE uses VPC-native (IP aliasing) and requires two secondary ranges on the subnet: one for
      Pods and one for Services. On the default VPC, these ranges are created automatically. For
      custom networks, verify both ranges exist before creating the cluster.
# END generated_summary_faq

author: 
   - Rani Chowdary Mandepudi

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
operatingsystems:
    - Linux
tools_software_languages:
    - Kubernetes
    - GKE
    - Skaffold
    - Cloud Build

further_reading:
    - resource:
        title: Google Kubernetes Engine documentation
        link: https://cloud.google.com/kubernetes-engine/docs
        type: documentation
    - resource:
        title: Create standard clusters and node pools with Arm nodes 
        link: https://cloud.google.com/kubernetes-engine/docs/how-to/create-arm-clusters-nodes
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
