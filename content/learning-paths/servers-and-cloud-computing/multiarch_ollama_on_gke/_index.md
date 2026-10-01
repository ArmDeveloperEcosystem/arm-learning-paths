---
title: Add Arm nodes to your GKE cluster using a multi-architecture Ollama container image 

minutes_to_complete: 30

who_is_this_for: This Learning Path is for developers who want to compare the performance of amd64 and arm64 deployments by running inferences on a hybrid Google Kubernetes Engine (GKE) cluster using an Ollama multi-architecture container image.

learning_objectives:
  - Create a hybrid GKE cluster with amd64 and arm64 nodes.
  - Deploy Ollama services for amd64 and arm64 architectures using a single multi-architecture container image.
  - Validate deployments by pinging, pulling models, and running inferences to compare architecture performance.

prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/)
    - A local machine with [Google Cloud CLI](/install-guides/gcloud/) and [kubectl](/install-guides/kubectl/) installed
    - The [GKE Cloud Plugin](https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl#gcloud) installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-01T19:36:03Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 524da8c0a000a03613c8fca09d0a78b8bb3fbe57a53fdaaaca79d4d7431bb44c
  summary_generated_at: '2026-10-01T19:36:03Z'
  summary_source_hash: 524da8c0a000a03613c8fca09d0a78b8bb3fbe57a53fdaaaca79d4d7431bb44c
  faq_generated_at: '2026-10-01T19:36:03Z'
  faq_source_hash: 524da8c0a000a03613c8fca09d0a78b8bb3fbe57a53fdaaaca79d4d7431bb44c
  summary: >-
    You'll build a hybrid GKE cluster that runs Ollama on amd64 and Arm nodes.
    First, you'll deploy Ollama to the initial amd64 pool, add an Arm node pool, and create a matching arm64
    deployment. Then, you'll use a multi-architecture service and a script to route requests. You'll 
    identify the pod and node that handled each call, load a model, and compare inference behavior
    across both architectures.
  faqs:
  - question: Which namespace should I use for all Kubernetes objects?
    answer: >-
      Use the `ollama` namespace created by applying `namespace.yaml`. All subsequent deployments
      and services are scoped to this namespace.
  - question: How do I verify that the initial amd64 deployment is ready before adding Arm nodes?
    answer: >-
      Confirm that the Ollama deployment and service for amd64 exist in the `ollama` namespace and
      report ready. Don't proceed until the pods are running and the service is available.
  - question: What values should I set when creating the Arm node pool?
    answer: >-
      Name the pool `arm64-pool`, set **Size** to **1**, and enable **Specify node locations** with
      **us-central1-a** selected. Follow the remaining on-screen options to add the Arm node pool.
  - question: How do I send a request without selecting an architecture and see which architecture handled
      it?
    answer: >-
      Run `./model_util.sh multiarch hello` to target the multi-architecture service. The response
      shows which pod served the request, including its deployment, node, and timestamp.
  - question: What should I check if requests always go to the same architecture?
    answer: >-
      Verify that both the amd64 and arm64 deployments are running and their services are available
      in the `ollama` namespace. If one deployment isn't ready, traffic routes to the available
      architecture.
# END generated_summary_faq

author:
    - Geremy Cohen

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory

subjects: Containers and Virtualization
platforms:
  - Google Axion

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
