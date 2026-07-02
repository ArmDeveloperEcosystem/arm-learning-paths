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
  generated_at: '2026-07-02T19:00:04Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7a84bfc0dd8ed40a760526ab220113200aa01d3e745b7dc7b77767c6258e8874
  summary_generated_at: '2026-07-02T19:00:04Z'
  summary_source_hash: 7a84bfc0dd8ed40a760526ab220113200aa01d3e745b7dc7b77767c6258e8874
  faq_generated_at: '2026-07-02T19:00:04Z'
  faq_source_hash: 7a84bfc0dd8ed40a760526ab220113200aa01d3e745b7dc7b77767c6258e8874
  summary: >-
    You'll create a Google Axion-based self-hosted GitLab Runner
    and wire it into a GitLab CI/CD pipeline that produces a multi-architecture container image.
    First, you'll register the runner, choose an executor that fits your environment, and confirm it is
    available to your project. Then, you'll configure the pipeline to build architecture-specific images
    on native runners for Arm and x86, push them to a container registry, and assemble a
    single multi-architecture image using the `docker manifest` approach. You'll then trigger
    a pipeline, see jobs land on the intended runners, and verify that the published image advertises
    both arm64 and amd64 in its manifest.
  faqs:
  - question: How do I know the Axion-based runner registered correctly?
    answer: >-
      Check the project or group’s Runners page in GitLab and confirm the runner shows as online.
      Run a test pipeline and verify the job log lists the expected runner and executor.
  - question: Which executor should I use for the self-hosted runner?
    answer: >-
      Choose the executor that matches how you want jobs to run in your environment. For example,
      use a Docker-based executor to run containerized jobs or a Kubernetes executor to schedule
      jobs on a cluster.
  - question: How are multi-architecture images built in this path?
    answer: >-
      You'll use `docker manifest` to join separate architecture-specific images into a single
      multi-architecture image. You'll build images for arm64 and amd64 on native runners, then create
      a manifest that references both.
  - question: What result should I expect after the manifest step completes?
    answer: >-
      You should have a single image tag that represents a manifest list containing entries for
      arm64 and amd64. When inspected in your registry, it shows both architectures under the
      same tag.
  - question: Can I mix GitLab-hosted and self-managed runners in the same pipeline?
    answer: >-
      Yes. You can use both types of runners and route specific jobs to the intended runner type
      through your CI configuration so architecture-specific jobs run on the correct machines.
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
