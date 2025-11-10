---
title: Migrate x86 workloads to Arm on GKE with Google Axion

minutes_to_complete: 90

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
        title: Create standard clusters and node pools with Arm nodes 
        link: https://cloud.google.com/kubernetes-engine/docs/how-to/create-arm-clusters-nodes
        type: documentation
    
    



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
