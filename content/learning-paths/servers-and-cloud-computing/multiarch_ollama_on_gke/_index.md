---
title: Add Arm nodes to your GKE cluster using a multi-architecture Ollama container image 

minutes_to_complete: 30

who_is_this_for: This Learning Path is for developers who want to compare the performance of amd64 and arm64 deployments by running inferences on a hybrid GKE cluster using an Ollama multi-architecture container image.


learning_objectives:
  - Create a hybrid GKE cluster with amd64 and arm64 nodes.
  - Deploy Ollama services for amd64 and arm64 architectures using a single multi-architecture container image.
  - Validate deployments by pinging, pulling models, and running inferences to compare architecture performance.

prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/).
    - A local machine with [Google Cloud CLI](/install-guides/gcloud/) and [kubectl](/install-guides/kubectl/) installed.
    - The [GKE Cloud Plugin](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#gcloud) installed.
   

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:35:29Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: cd31c217eaeab6faad263728c446ee188cd9d542904d87ae7bfd5120713dfaa4
  summary_generated_at: '2026-06-02T04:32:13Z'
  summary_source_hash: cd31c217eaeab6faad263728c446ee188cd9d542904d87ae7bfd5120713dfaa4
  faq_generated_at: '2026-06-03T01:35:29Z'
  faq_source_hash: cd31c217eaeab6faad263728c446ee188cd9d542904d87ae7bfd5120713dfaa4
  summary: >-
    This Learning Path shows how to extend a Google Kubernetes Engine (GKE) cluster with Arm-based
    nodes and deploy Ollama using a single multi-architecture container image. You begin with
    an amd64 node running an Ollama Deployment and Service, then add an arm64 node pool and mirror
    the deployment to form a hybrid cluster. You create the Kubernetes namespace, apply architecture-specific
    services, and exercise a multi-architecture service that can route to either backend. You
    validate by pinging the service, pulling models, and running LLM inferences while observing
    which pod and node serve requests. Prerequisites are a Google Cloud account, gcloud, kubectl,
    and the GKE Cloud Plugin on Linux or macOS.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Google Cloud account and a local machine with the Google Cloud CLI, kubectl,
      and the GKE Cloud Plugin installed. The steps target Linux and macOS.
  - question: How is the initial amd64 deployment organized in Kubernetes?
    answer: >-
      You create an ollama namespace, then deploy an Ollama Deployment and Service for amd64.
      This simulates an existing cluster before adding Arm nodes.
  - question: What settings should I use when adding the Arm node pool?
    answer: >-
      In the GKE console, select the ollama-on-multiarch cluster, choose Add node pool, name it
      arm64-pool, set Size to 1, and specify the us-central1-a location. Follow the step guidance
      to complete node settings.
  - question: How do I verify that requests can reach either architecture in the hybrid cluster?
    answer: >-
      Use the provided script: ./model_util.sh multiarch hello. The response includes the pod
      and deployment that handled the request, and repeating the command may route to different
      pods.
  - question: How do I compare amd64 and arm64 behavior and performance in this setup?
    answer: >-
      Validate by pinging services, pulling models, and running inferences on both the amd64 and
      arm64 deployments. Use the multiarch service to observe request routing or target each architecture’s
      service to compare results.
# END generated_summary_faq

author:
    - Geremy Cohen

### Tags
skilllevels: Introductory

subjects: Containers and Virtualization
cloud_service_providers:
  - Google Cloud
    
armips:
    - Neoverse

operatingsystems:
    - Linux
    - macOS

tools_software_languages:
    - LLM
    - Ollama
    - Generative AI

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

