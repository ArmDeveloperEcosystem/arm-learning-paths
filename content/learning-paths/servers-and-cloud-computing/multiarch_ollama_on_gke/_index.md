---
title: Run ollama on both arm64 and amd64 nodes, using the same multi-architecture container image on GKE.

minutes_to_complete: 30

who_is_this_for:  This learning path will show you how easy it is to migrate from homogenous amd64 k8s clusters, to a hybrid (arm64 and amd64) cluster with multi-architectural container images on GKE.  Demonstrated with the ollama application, you'll see for yourself the price/performance advantages of running on arm64. Although tutorial will be GKE-specific with ollama, the provided YAML can act as a template for deployment on any on any multi-architectural application and cloud.


learning_objectives:
  - Spin up a GKE cluster with amd64 and arm64 nodes.
  - Apply ollama amd64-based and arm64-based Deployments and Services using the same container image.
  - Ping, pull models, and make inferences to experience each architectures' performance first-hand.
  - Experiment further on your own by researching which existing, and future workloads could benefit most from single, or multi-architectural clusters.

prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/).
    - A computer with [Google Cloud CLI](/install-guides/gcloud) and [kubectl](/install-guides/kubectl/) installed.
    - The [GKE Cloud Plugin](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#gcloud)
   

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
    - MacOs

tools_software_languages:
  - LLM
      - ollama
      - GenAI

further_reading:
  - resource:
      title: ollama - Get up and running with large language models
      link: https://ollama.com/
      type: documentation
  - resource:
      title: ollama API calls
      link: https://github.com/ollama/ollama/blob/main/docs/api.md
      type: documentation
  - resource:
      title: Dockerhub for Ollama
      link: https://hub.docker.com/r/ollama/ollama
      type: documentation
  - resource:
      title: ollama build docs
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
