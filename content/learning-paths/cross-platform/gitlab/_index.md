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
    - A computer with [Google Cloud CLI](/install-guides/gcloud/) and [kubectl](/install-guides/kubectl/)installed.
    - A valid GitLab account

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-02T18:07:57Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7a84bfc0dd8ed40a760526ab220113200aa01d3e745b7dc7b77767c6258e8874
  summary_generated_at: '2026-07-02T18:07:57Z'
  summary_source_hash: 7a84bfc0dd8ed40a760526ab220113200aa01d3e745b7dc7b77767c6258e8874
  faq_generated_at: '2026-07-02T18:07:57Z'
  faq_source_hash: 7a84bfc0dd8ed40a760526ab220113200aa01d3e745b7dc7b77767c6258e8874
  summary: >-
    This Learning Path guides you through building a GitLab CI/CD pipeline that uses a Google
    Axion-based self-hosted runner to produce a multi-architecture container image. You configure
    a runner on Google Cloud to execute arm64 jobs natively, pair it with an amd64 runner, and
    define pipeline stages that build per-architecture images. The workflow then uses the docker
    manifest approach to assemble those images under a single tag and publish them to a container
    registry. By the end, learners integrate native Arm and x86 builds in one pipeline and produce
    a manifest-listed image that pulls the correct variant on each platform.
  faqs:
  - question: Which runner should I use for the arm64 build stage?
    answer: >-
      Use the self-hosted GitLab Runner on Google Axion to run arm64 jobs natively. Other architecture
      builds can run on an x86 or GitLab-hosted runner.
  - question: Should I use Docker Buildx or docker manifest for the multi-arch image here?
    answer: >-
      Use docker manifest as specified in the path. You build separate images per architecture
      and then create a manifest to publish a single multi-architecture tag.
  - question: What result should I expect after the manifest step completes?
    answer: >-
      You should have one image reference that represents both arm64 and amd64 variants. Pulling
      that tag on each platform selects the matching architecture image.
  - question: Where are the images published during the pipeline?
    answer: >-
      They are pushed to a Docker repository you create on Google Cloud. The manifest-listed tag
      points to the architecture-specific images stored there.
  - question: Can I proceed if I only have one architecture runner available?
    answer: >-
      You can build and push a single-architecture image, but the multi-architecture tag requires
      images for each target architecture. Add the missing runner to complete the manifest-listed
      image.
# END generated_summary_faq

author: Pranay Bakre

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

