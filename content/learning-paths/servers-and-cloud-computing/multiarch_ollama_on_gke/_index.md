---
title: Run ollama on both arm64 and amd64 nodes, using the same multi-architecture container image on GKE.

minutes_to_complete: 30

who_is_this_for:  Ever considered running your Kubernetes (k8s) workloads on arm64, but didn't know what was involved?  If so, this learning path will show you how easy it is to run arm64 alone, or alongside amd64 node types.  You'll see how easy it is to migrate from homogenous amd64 k8s clusters, to a hybrid (arm64 and amd64) cluster with multi-architectural container images on GKE, specifically with the ollama application.  Once you see for yourself the price/performance advantages of running on arm64, the same knowledge can be applied to spinning up homogenous arm64 clusters, or migrating your clusters from amd64 to arm64. Although tutorial will be GKE-specific with ollama, the provided YAML will work with any deployment on any on any cloud.


learning_objectives:
  - Spin up a GKE cluster with an amd64.
  - Apply an ollama amd64-based Deployment and Service.
  - Add a new, Arm-based Axion node to the cluster.
  - Apply an ollama-arm64-based Deployment to the existing Service.
  - Issue queries to the arm64 and amd64 endpoints to witness performance first-hand.
  - Analyze price/performance advantages of running your workloads on Arm vs amd64.
  - Experiment further on your own by researching which existing, and future workloads could benefit most from single, or multi-architectural clusters.

prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/).
    - A computer with [Google Cloud CLI](/install-guides/gcloud) and [kubectl](/install-guides/kubectl/) installed.
    - The [GKE Cloud Plugin](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#gcloud)
    - The [curl](https://curl.se/) utility
    - The [jq](https://jqlang.org/) utility
    - The [stdbuf](https://www.gnu.org/software/coreutils/manual/html_node/stdbuf-invocation.html) utility

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
