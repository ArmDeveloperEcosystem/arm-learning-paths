---
title: Migrate x86 workloads to Arm on Google Kubernetes Engine with Axion processors 

minutes_to_complete: 90
description: Learn how to create dual-architecture GKE clusters with arm64 and amd64 node pools, build multi-architecture Docker images, and migrate services to Google Axion processors.
who_is_this_for: This is an advanced topic for cloud, platform, and site reliability engineers who operate Kubernetes on Google Cloud and need to build multi-architecture images and migrate services from x86 to Arm using Google Axion processors.

learning_objectives:
    - Prepare Dockerfiles for multi-architecture builds by adding arm64 support
    - Create a dual-architecture GKE standard cluster with amd64 and arm64 node pools 
    - Build and publish multi-architecture images to Artifact Registry using Docker Buildx
    - Deploy a Kubernetes application on amd64, then migrate to arm64 using Kustomize overlays
    - Automate builds and rollouts with Cloud Build and Skaffold
    
prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/) with billing enabled
    - A local Linux or macOS computer with Docker, Kubernetes CLI (kubectl), Google Cloud CLI (gcloud), and Git installed, or access to Google Cloud Shell
    - Basic familiarity with Docker, Kubernetes, and gcloud

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:05:58Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: cf981c67553824c7c57b6dda9c2953ac80926750676ac101e939f6bbff655ab5
  summary_generated_at: '2026-06-02T04:03:32Z'
  summary_source_hash: cf981c67553824c7c57b6dda9c2953ac80926750676ac101e939f6bbff655ab5
  faq_generated_at: '2026-06-03T01:05:58Z'
  faq_source_hash: cf981c67553824c7c57b6dda9c2953ac80926750676ac101e939f6bbff655ab5
  summary: >-
    This advanced Learning Path walks you through migrating a microservices application from x86
    to Arm on Google Kubernetes Engine using multi-architecture container images and Google Axion
    processors. You will prepare Dockerfiles for arm64, create a dual-architecture GKE standard
    cluster with separate amd64 and arm64 node pools, and build and publish images to Artifact
    Registry with Docker Buildx. You will deploy Online Boutique on amd64 and migrate to arm64
    using Kustomize overlays, with optional automation using Cloud Build and Skaffold. Prerequisites
    include a billing-enabled Google Cloud account and a Linux or macOS environment with Docker,
    kubectl, gcloud, and Git installed, or access to Cloud Shell. Estimated time to complete is
    about 90 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Google Cloud account with billing enabled and either a local Linux or macOS system
      with Docker, kubectl, gcloud, and Git installed, or access to Google Cloud Shell. Basic
      familiarity with Docker, Kubernetes, and gcloud is expected.
  - question: Which GKE cluster configuration and networking are used?
    answer: >-
      You will create a GKE standard cluster with two node pools: one amd64 and one arm64. GKE
      uses VPC-native (IP aliasing) with two secondary ranges for Pods and Services; for the default
      VPC these ranges are created automatically.
  - question: Which Online Boutique services require Dockerfile changes for multi-architecture
      builds?
    answer: >-
      Four services need updates: emailservice, recommendationservice, loadgenerator, and cartservice.
      The changes ensure the correct compiler headers and runtime libraries are present for each
      architecture.
  - question: How are the multi-architecture images built and published?
    answer: >-
      Images are built with Docker Buildx on the cluster using separate BuildKit pods per architecture,
      so no QEMU emulation is required. The resulting multi-architecture images are pushed to
      Google Artifact Registry.
  - question: How do I deploy on amd64 first and then migrate to Arm?
    answer: >-
      Update the base Kubernetes manifests to reference your Artifact Registry images, then create
      Kustomize overlays that select nodes by CPU architecture. Deploy to the amd64 node pool
      first, then apply the arm64 overlay to migrate to the Arm node pool.
# END generated_summary_faq

author: 
   - Rani Chowdary Mandepudi

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
cloud_service_providers:
  - Google Cloud
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

