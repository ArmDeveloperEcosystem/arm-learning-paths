---
title: Build a CI/CD pipeline with GitLab on Google Axion

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for DevOps professionals who are looking to build a CI/CD pipeline with GitLab on Google Axion based self-hosted GitLab runners. 

description: Learn how to build a GitLab CI/CD pipeline using Google Axion-based self-hosted runners.

learning_objectives: 
    - Create a Google Axion based GitLab self-hosted runner
    - Build a CI/CD pipeline with multi-architecture support
    - Build multi-architecture docker images using native GitLab runners on x86 and Arm
    - Automate the build and deployment of a multi-arch application with GitLab CI/CD

prerequisites:
    - A [Google Cloud account](https://console.cloud.google.com/). Create an account if needed.
    - A computer with [Google Cloud CLI](/install-guides/gcloud) and [kubectl](/install-guides/kubectl/)installed.
    - A valid GitLab account

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:39:28Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: af9eb1c426e1844e2fd20215b7012d95c1efaf737f1d7b5be828931528342316
  summary_generated_at: '2026-06-01T21:06:50Z'
  summary_source_hash: af9eb1c426e1844e2fd20215b7012d95c1efaf737f1d7b5be828931528342316
  faq_generated_at: '2026-06-02T21:39:28Z'
  faq_source_hash: af9eb1c426e1844e2fd20215b7012d95c1efaf737f1d7b5be828931528342316
  summary: >-
    This advanced Learning Path shows how to build a GitLab CI/CD pipeline on Google Cloud using
    Google Axion-based self-hosted runners. You will create a GitLab runner on Axion (Arm Neoverse)
    and pair it with a native x86 runner to build a multi-architecture application targeting arm64
    and amd64. Using GitLab CI/CD with Docker and Kubernetes on Linux, you will configure jobs
    that produce per-architecture images and combine them into a single multi-arch image with
    docker manifest, then automate build and deployment. Prerequisites include a Google Cloud
    account, Google Cloud CLI, kubectl, and a GitLab account. The estimated time to complete is
    about 30 minutes.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Google Cloud account, Google Cloud CLI and kubectl installed on your computer,
      and a valid GitLab account. The path targets Linux.
  - question: How do I know my Google Axion self-hosted runner is ready to run jobs?
    answer: >-
      After you register the runner, verify it appears in your GitLab project or group runner
      list with the executor you selected. Continue when it is listed and available for CI/CD
      jobs.
  - question: Which approach does the pipeline use to produce a multi-architecture image?
    answer: >-
      It uses docker manifest to join separate amd64 and arm64 images into a single multi-architecture
      image.
  - question: Do I need both x86 and Arm runners to build the images?
    answer: >-
      Yes. The objectives include building multi-architecture Docker images using native GitLab
      runners on x86 and Arm.
  - question: Where are the built images stored, and how can I validate the result?
    answer: >-
      You create a Docker repository in Google Artifact Registry and push images there as part
      of the pipeline. Validate by confirming the repository contains amd64 and arm64 images referenced
      by a manifest after a successful run.
# END generated_summary_faq

author: Pranay Bakre

### Tags
skilllevels: Advanced
subjects: Containers and Virtualization
cloud_service_providers:
  - Google Cloud

armips:
    - Neoverse

tools_software_languages:
    - Kubernetes
    - Docker
    - GitLab

operatingsystems:
    - Linux

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - embedded-and-microcontrollers

further_reading:
    - resource:
        title: Create Arm based clusters and node pools 
        link: https://cloud.google.com/kubernetes-engine/docs/how-to/create-arm-clusters-nodes
        type: documentation
    - resource:
        title: Configure cluster access to use kubectl
        link: https://cloud.google.com/kubernetes-engine/docs/how-to/cluster-access-for-kubectl
        type: documentation
    - resource:
        title: GKE documentation
        link: https://cloud.google.com/kubernetes-engine/docs
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

