---
title: Migrate containers to Arm using KubeArchInspect

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for software developers who want to ensure containers running in a Kubernetes cluster support the Arm architecture.

description: Identify and migrate container images in a Kubernetes cluster to Arm-compatible versions using KubeArchInspect reports.

learning_objectives: 
    - Run KubeArchInspect to generate a report on the containers running in a Kubernetes cluster
    - Discover which images support the Arm architecture
    - Understand common reasons for an image not supporting Arm
    - Make configuration changes to upgrade images with Arm support

prerequisites:
    - A running Kubernetes cluster accessible with `kubectl`.

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:19:42Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 43e4e28b88b9721ca94457418f3b4887d0099017578a54da1db5fcdc11f4a122
  summary_generated_at: '2026-06-02T04:14:53Z'
  summary_source_hash: 43e4e28b88b9721ca94457418f3b4887d0099017578a54da1db5fcdc11f4a122
  faq_generated_at: '2026-06-03T01:19:42Z'
  faq_source_hash: 43e4e28b88b9721ca94457418f3b4887d0099017578a54da1db5fcdc11f4a122
  summary: >-
    Learn how to assess and migrate Kubernetes container images to Arm-compatible versions using
    KubeArchInspect. You will install KubeArchInspect on Linux, ensure kubectl is configured to
    your cluster, run kubearchinspect images to inventory running images, and generate a report
    by querying source registries for available architectures. You will analyze the results using
    clear indicators (arm64 supported, not available, available in newer version, or error) and
    make configuration changes to upgrade images that include Arm support. This introductory path
    targets developers who want to confirm Arm readiness for their workloads and can be applied
    to Kubernetes clusters, including those on major cloud providers. Prerequisite: a running
    Kubernetes cluster accessible with kubectl. Estimated time: 15 minutes.
  faqs:
  - question: What do I need before running KubeArchInspect?
    answer: >-
      You need a running Kubernetes cluster and kubectl configured to access it. Install kubearchinspect
      on a Linux environment. No other explicit prerequisites are listed.
  - question: Which command should I use to generate the image report?
    answer: >-
      Run: kubearchinspect images. This connects to your cluster and produces a report of images
      in use and their available architectures.
  - question: How does KubeArchInspect determine whether an image supports Arm?
    answer: >-
      It queries the image’s source registry and checks which architectures are available. The
      report highlights whether arm64 is present for each image.
  - question: How do I interpret the output symbols in the report?
    answer: >-
      A green tick (✅) means the image already supports arm64. A red cross (❌) means arm64 is
      not available; a blue up (🆙) indicates a newer version includes arm64; a red cross mark
      (🚫) signals an error occurred when checking the image, which may indicate a registry connectivity
      issue.
  - question: What should I do after running the report?
    answer: >-
      Use the results to plan configuration changes that upgrade images to versions with arm64
      support. Prioritize images marked with 🆙 for straightforward upgrades, and review ❌ entries
      to determine your next steps.
# END generated_summary_faq

author: Jason Andrews

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
tools_software_languages:
    - Kubernetes
    - Runbook

operatingsystems:
    - Linux


further_reading:
    - resource:
        title: Kubernetes documentation
        link: https://kubernetes.io/docs/home/
        type: documentation
    - resource:
        title: Amazon Elastic Kubernetes Service
        link: https://aws.amazon.com/eks/
        type: documentation
    - resource:
        title: Azure Kubernetes Service (AKS)
        link: https://learn.microsoft.com/en-us/azure/aks/
        type: documentation
    - resource:
        title: Arm workloads on GKE
        link: https://cloud.google.com/kubernetes-engine/docs/concepts/arm-on-gke
        type: documentation


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

