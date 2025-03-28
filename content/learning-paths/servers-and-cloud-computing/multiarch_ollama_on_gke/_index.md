---
title: Run Ollama's multi-arch container image on GKE with arm64 and amd64 nodes. 

minutes_to_complete: 30

who_is_this_for: This topic explains how developers can migrate a homogenous amd64 K8s cluster to a hybrid (arm64 and amd64) cluster using a multi-architecture container image on GKE. Ollama is the application used to demonstrate the migration. 


learning_objectives:
  - Spin up a GKE cluster with amd64 and arm64 nodes.
  - Apply Ollama amd64-based and arm64-based deployments and services using the same container image.
  - Ping, pull models, and make inferences to experience the performance of each architecture.

prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/).
    - A local computer with the [Google Cloud CLI](/install-guides/gcloud) and [kubectl](/install-guides/kubectl/) installed.
    - The [GKE Cloud Plugin](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#gcloud).
   

author:
    - Geremy Cohen

### Tags
skilllevels: Introductory

subjects: Containers and Virtualization
cloud_service_providers: Google Cloud
    
armips:
    - Neoverse

operatingsystems:
    - Linux
    - macOS

tools_software_languages:
    - LLM
    - Ollama
    - GenAI

further_reading:
  - resource:
      title: Ollama - Get up and running with large language models
      link: https://ollama.com/
      type: documentation
  - resource:
      title: Ollama API calls
      link: https://github.com/ollama/ollama/blob/main/docs/api.md
      type: documentation
  - resource:
      title: Dockerhub for Ollama
      link: https://hub.docker.com/r/ollama/ollama
      type: documentation
  - resource:
      title: Ollama build docs
      link: https://github.com/ollama/ollama/blob/main/docs/development.md
      type: documentation
  - resource:
      title: Getting started with Llama
      link: https://llama.meta.com/get-started
      type: documentation
  - resource:
      title: Prepare to deploy an Arm workload in a Standard cluster
      link: https://cloud.google.com/kubernetes-engine/docs/how-to/prepare-arm-workloads-for-deployment
      type: documentation
  - resource:
      title: Create an External Load Balancer 
      link: https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/
      type: documentation
  - resource:
      title: Install kubectl and configure cluster access on GKE
      link: https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl
      type: documentation

    




### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
