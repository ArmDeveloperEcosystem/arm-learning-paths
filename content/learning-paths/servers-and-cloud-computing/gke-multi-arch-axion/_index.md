---
title: From x86 to Arm on GKE - Build, Deploy, and Migrate with Google Axion

draft: true
cascade:
    draft: true

minutes_to_complete: 90

who_is_this_for: This is an advanced topic for cloud, platform, and site reliability engineers operating Kubernetes on Google Cloud who need a prescriptive path to build multi-architecture images and migrate services from x86 to Arm using Google Axion processors.

learning_objectives:
    - Prepare Dockerfiles for multi-architecture builds by adding arm64 support
    - Create a dual-architecture GKE standard cluster with two node pools, amd64 and arm64
    - Build and publish multi-architecture images to Artifact Registry using Docker Buildx without using QEMU to emulate Arm instructions
    - Deploy a Kubernetes application amd64 first, then migrate to arm64 using Kustomize overlays and progressive rollout
    - Optionally automate builds and rollouts with Cloud Build and Skaffold
    
prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/) with billing enabled
    - A local Linux or macOS computer or Cloud Shell access with Docker, Kubernetes CLI (kubectl), Google Cloud CLI (gcloud), and Git installed
    - Basic familiarity with Docker, Kubernetes, and gcloud

author: 
   - Rani Chowdary Mandepudi

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
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
        title: GKE documentation
        link: https://cloud.google.com/kubernetes-engine/docs
        type: documentation
    - resource:
        title: Create Arm-based clusters and node pools 
        link: https://cloud.google.com/kubernetes-engine/docs/how-to/create-arm-clusters-nodes
        type: documentation
    
    



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
