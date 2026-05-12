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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:57Z'
  generator: template
  source_hash: cf981c67553824c7c57b6dda9c2953ac80926750676ac101e939f6bbff655ab5
  summary: >-
    Learn how to create dual-architecture GKE clusters with arm64 and amd64 node pools, build
    multi-architecture Docker images, and migrate services to Google Axion processors. It is designed
    for cloud, platform, and site reliability engineers who operate Kubernetes on Google Cloud
    and need to build multi-architecture images and migrate services from x86 to Arm using Google
    Axion processors. By the end, you will be able to prepare Dockerfiles for multi-architecture
    builds by adding arm64 support, create a dual-architecture GKE standard cluster with amd64
    and arm64 node pools, and build and publish multi-architecture images to Artifact Registry
    using Docker Buildx. It focuses on tools and technologies such as Kubernetes, GKE, Skaffold,
    and Cloud Build, Linux environments, Arm platforms including Neoverse, and cloud platforms
    such as Google Cloud. The main steps cover Explore the benefits of migrating microservices
    to Arm on GKE, Set up your environment, Create build-ready Dockerfiles for both architectures,
    Build and deploy multi-architecture images on GKE, and Prepare manifests and deploy on GKE.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will prepare Dockerfiles for multi-architecture builds by adding arm64 support, create
      a dual-architecture GKE standard cluster with amd64 and arm64 node pools, and build and
      publish multi-architecture images to Artifact Registry using Docker Buildx. Learn how to
      create dual-architecture GKE clusters with arm64 and amd64 node pools, build multi-architecture
      Docker images, and migrate services to Google Axion processors.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for cloud, platform, and site reliability engineers who operate
      Kubernetes on Google Cloud and need to build multi-architecture images and migrate services
      from x86 to Arm using Google Axion processors.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud account](https://console.cloud.google.com/)
      with billing enabled; A local Linux or macOS computer with Docker, Kubernetes CLI (kubectl),
      Google Cloud CLI (gcloud), and Git installed, or access to Google Cloud Shell; Basic familiarity
      with Docker, Kubernetes, and gcloud.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Kubernetes, GKE, Skaffold, and Cloud Build, Linux
      environments, Arm platforms such as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Explore the benefits of migrating microservices to
      Arm on GKE, Set up your environment, Create build-ready Dockerfiles for both architectures,
      Build and deploy multi-architecture images on GKE, and Prepare manifests and deploy on GKE.
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

