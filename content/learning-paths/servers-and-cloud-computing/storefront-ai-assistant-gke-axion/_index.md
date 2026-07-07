---
title: Build a mixed-placement AI shopping assistant on GKE with Axion

minutes_to_complete: 120
description: Deploy an AI shopping assistant for an Online Boutique storefront on GKE and compare N4A and C4A placement for the assistant tier.
who_is_this_for: This is an advanced topic for cloud developers, platform engineers, and site reliability engineers who run applications on Google Kubernetes Engine and want to place application tiers on the Axion-based machine series that fits each workload.

learning_objectives:
    - Explain why a storefront application and an AI assistant can have different workload profiles
    - Build and push a `linux/arm64` container image for the shopping assistant service
    - Use Kustomize overlays to run the assistant on N4A first, then move it to C4A
    - Capture and compare benchmark summaries for the same assistant workload on N4A and C4A

prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/) with billing enabled
    - Access to a [GKE Standard cluster with Arm node pools](https://cloud.google.com/kubernetes-engine/docs/how-to/create-arm-clusters-nodes), including an N4A node pool and a C4A node pool
    - Permission to create or use an [Artifact Registry Docker repository](https://cloud.google.com/artifact-registry/docs/docker/store-docker-container-images) in the same project
    - Access to Google Cloud Shell, or a local Linux or macOS terminal with `gcloud`, `kubectl`, `docker`, `git`, `jq`, and `python3`
    - Basic familiarity with Docker, Kubernetes, Kustomize, and Google Kubernetes Engine

author:
   - Rani Chowdary Mandepudi

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

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
    - Docker
    - Kustomize
    - Python
    - Ollama

further_reading:
    - resource:
        title: Google Kubernetes Engine documentation
        link: https://cloud.google.com/kubernetes-engine/docs
        type: documentation
    - resource:
        title: Create standard clusters and node pools with Arm nodes
        link: https://cloud.google.com/kubernetes-engine/docs/how-to/create-arm-clusters-nodes
        type: documentation
    - resource:
        title: Google Axion processors
        link: https://cloud.google.com/products/axion
        type: documentation
    - resource:
        title: Kustomize documentation
        link: https://kubectl.docs.kubernetes.io/references/kustomize/
        type: documentation
    - resource:
        title: Ollama documentation
        link: https://ollama.com/
        type: documentation
    - resource:
        title: Migrate x86 workloads to Arm on Google Kubernetes Engine with Axion processors
        link: /learning-paths/servers-and-cloud-computing/gke-multi-arch-axion/
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

Deploy an Online Boutique storefront on Google Kubernetes Engine (GKE), add an AI shopping assistant, and compare the same assistant workload on N4A and C4A node pools powered by Google Axion processors.

You start with the storefront on N4A, build the missing `shoppingassistantservice` image for `linux/arm64`, validate the assistant on N4A, and then move only the assistant tier to C4A. You finish by running the same fixed benchmark in both placements so you can compare request success, latency, and Kubernetes CPU telemetry.
