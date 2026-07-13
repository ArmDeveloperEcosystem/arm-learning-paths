---
title: Deploy a mixed-placement AI shopping assistant on Google Kubernetes Engine with Axion-based compute

minutes_to_complete: 120
description: Deploy and validate an Online Boutique storefront on GKE on Arm, add an AI shopping assistant, and compare N4A and C4A placement for the assistant tier.
who_is_this_for: This is an advanced topic for cloud developers, platform engineers, and site reliability engineers who run applications on Google Kubernetes Engine (GKE) and want to place application tiers on the Axion-based machine series that fits each workload.

learning_objectives:
    - Deploy and validate an Online Boutique storefront on an N4A node pool
    - Build and push a `linux/arm64` container image, then add the AI shopping assistant to the storefront
    - Use Kustomize overlays to run the assistant on N4A first, then move it to C4A
    - Capture and compare benchmark summaries for the same assistant workload on N4A and C4A

prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/) with billing enabled
    - Access to a [GKE Standard cluster with Arm node pools](https://cloud.google.com/kubernetes-engine/docs/how-to/create-arm-clusters-nodes), including N4A and C4A node pools, with the Kubernetes Metrics API enabled
    - Permissions to get cluster credentials, deploy Kubernetes workloads and services, read pod logs and metrics, and create or use an Artifact Registry Docker repository
    - Cloud Shell or a Linux or macOS administrative workstation with Docker Buildx, `gcloud`, `kubectl`, `git`, `curl`, Python 3.10 or later, and `jq`
    - Basic familiarity with Docker, Kubernetes, Kustomize, and GKE

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-13T19:30:38Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: cdd45953e2784d3a6b0894fac600b6b03048b514493d6526709908f3049595cc
  summary_generated_at: '2026-07-13T19:30:38Z'
  summary_source_hash: cdd45953e2784d3a6b0894fac600b6b03048b514493d6526709908f3049595cc
  faq_generated_at: '2026-07-13T19:30:38Z'
  faq_source_hash: cdd45953e2784d3a6b0894fac600b6b03048b514493d6526709908f3049595cc
  summary: >-
    You'll deploy the Online Boutique storefront on Google Kubernetes
    Engine using Arm-based Axion nodes, validate a baseline on N4A, and add a gRPC-driven AI shopping
    assistant. You'll build and push a single `linux/arm64` container image to Artifact Registry, then
    use Kustomize overlays to run the assistant on N4A before moving only that tier to C4A. After
    reviewing the assistant’s sources and runtime dependencies, you'll confirm scheduling on the intended
    node pool and capture benchmark summaries to compare the same assistant workload across N4A
    and C4A. The end state is a mixed-placement deployment where the steady storefront remains
    on N4A and the burstier assistant runs on the selected pool.
  faqs:
  - question: How do I verify the cluster has both N4A and C4A node pools before I start?
    answer: >-
      Use `kubectl` to list nodes and confirm that both pools are present. The workflow assumes
      an `arm64` GKE Standard cluster with separate N4A and C4A pools.
  - question: What result should I expect after I apply the baseline overlay?
    answer: >-
      The storefront runs on N4A, and `shoppingassistantservice` isn't present. This is intentional
      because you'll build and deploy the assistant in later steps.
  - question: I’ve run this path before. What should I remove before I recreate the baseline?
    answer: >-
      Delete any existing assistant deployment and related service so the baseline reflects a
      storefront without the assistant. The steps show removing old assistant resources before
      creating the baseline.
  - question: Do I need different container images for N4A and C4A when I deploy the assistant?
    answer: >-
      No. You'll build one `linux/arm64` image targeted for Axion that'll run in either placement.
  - question: How do I confirm the assistant is scheduled on the intended node pool when I switch
      from N4A to C4A?
    answer: >-
      Check the node assigned to the assistant pod and verify it matches the target pool after
      applying the appropriate Kustomize overlay. Inspect pod logs and service reachability to
      confirm the tier is healthy before capturing benchmarks.
# END generated_summary_faq

author:
   - Rani Chowdary Mandepudi

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
cloud_service_providers:
  - Google Cloud
armips:
    - Neoverse-N3
    - Neoverse-V2
operatingsystems:
    - Linux
tools_software_languages:
    - Kubernetes
    - GKE
    - Docker
    - Kustomize
    - Python
    - Ollama
    - Gemma

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
        type: website
    - resource:
        title: Kustomize documentation
        link: https://kubectl.docs.kubernetes.io/references/kustomize/
        type: documentation
    - resource:
        title: Ollama documentation
        link: https://docs.ollama.com/
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

