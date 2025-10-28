---
title: From x86 to Arm on GKE - Build, Deploy, and Migrate with Google Axion
draft: true
cascade:
    draft: true

minutes_to_complete: 90

who_is_this_for: This learning path is for cloud, platform and SRE engineers operating Kubernetes on Google Cloud who need a prescriptive path to build multi‑arch images and migrate services from x86 to Arm (Google Axion) using production‑grade practices.

learning_objectives:

    - Build and publish Docker images that support both amd64 and arm64 with Docker Buildx and Artifact Registry.
    - Create a GKE Standard cluster with x86 (amd64) nodes and add an Arm (arm64) node pool using Axion-based C4A machine types.
    - Deploy to amd64 first, then migrate to arm64 using Kustomize overlays for safe, incremental rollout. 
    - Optionally automate builds and rollouts end-to-end  with Cloud Build and Skaffold.
    
prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/)with billing enabled. 
    - Cloud Shell access (recommended) to run all steps in the browser; no local setup required.
    - (Optional if not using Cloud Shell) A Linux/macOS workstation with Docker (Buildx enabled), kubectl, the Google Cloud CLI (gcloud), and Git.
    - Basic familiarity with Docker, Kubernetes, and gcloud.

author: 
   - Pranay Bakre
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

    
further_reading:
    - resource:
        title: GKE documentation
        link: https://cloud.google.com/kubernetes-engine/docs
        type: documentation
    -  resource:
        title: Create Arm based clusters and node pools 
        link: https://cloud.google.com/kubernetes-engine/docs/how-to/create-arm-clusters-nodes
        type: documentation
    
    



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
