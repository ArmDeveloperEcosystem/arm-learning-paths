---
title: From x86 to Arm on GKE - Build, Deploy, and Migrate with Google Axion
draft: true
cascade:
    draft: true

minutes_to_complete: 90

who_is_this_for: This learning path is for cloud, platform, and SRE engineers operating Kubernetes on Google Cloud who need a prescriptive path to build multi‑architecture images and migrate services from x86 to Arm (Google Axion) using production‑grade practices.

learning_objectives:
    - Prepare Dockerfiles for multi-architecture builds (minimal, safe edits so services compile and run on amd64 & arm64).
    - Create a dual-architecture GKE Standard cluster with two node pools, amd64 and arm64 (Axion-based C4A).
    - Build and publish multi-architecture images to Artifact Registry using Docker Buildx (Kubernetes driver) - BuildKit pods run natively on both pools (no QEMU or extra build VMs).
    - Deploy to amd64 first, then migrate to arm64 using Kustomize overlays and progressive rollout.
    - Optionally automate builds and rollouts end-to-end with Cloud Build and Skaffold.
    
prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/) with billing enabled. 
    - Cloud Shell access (used as the control plane, includes gcloud, kubectl, and Docker Buildx).
    - (Optional if not using Cloud Shell) A Linux/macOS workstation with Docker (Buildx enabled), kubectl, the Google Cloud CLI (gcloud), and Git.
    - Basic familiarity with Docker, Kubernetes, and gcloud.

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
    -  resource:
        title: Create Arm-based clusters and node pools 
        link: https://cloud.google.com/kubernetes-engine/docs/how-to/create-arm-clusters-nodes
        type: documentation
    
    



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
