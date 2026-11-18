---
title: Migrate containers to Arm using KubeArchInspect

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for software developers who want to ensure containers running in a Kubernetes cluster support the Arm architecture.

description: Identify and migrate container images in a Kubernetes cluster to Arm-compatible versions using KubeArchInspect reports.

learning_objectives: 
    - Run KubeArchInspect to generate a report on the containers running in a Kubernetes cluster.
    - Discover which images support the Arm architecture.
    - Understand common reasons for an image not supporting Arm.
    - Make configuration changes to upgrade images with Arm support.

prerequisites:
    - A running Kubernetes cluster accessible with `kubectl`

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-15T21:23:35Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 17fe703c2cb52d231024812a5b3b91a070abb199405bdc39092e3286736e3e72
  summary_generated_at: '2026-09-15T21:23:35Z'
  summary_source_hash: 17fe703c2cb52d231024812a5b3b91a070abb199405bdc39092e3286736e3e72
  faq_generated_at: '2026-09-15T21:23:35Z'
  faq_source_hash: 17fe703c2cb52d231024812a5b3b91a070abb199405bdc39092e3286736e3e72
  summary: >-
    You'll use KubeArchInspect to assess Kubernetes workloads for Arm migration. First, you'll scan a
    live cluster and review a report that maps container images to the architectures
    advertised by their registries. Then, you'll identify images with arm64 support, images that need
    newer tags, and images that can't be checked. You'll update selected workloads and re-run
    the scan to verify Arm-compatible images.
  faqs:
  - question: How do I run the scan against my cluster?
    answer: >-
      Ensure that `kubectl` is configured to connect to your cluster, then run `kubearchinspect images`.
      The tool connects to the cluster and inspects the images that it finds.
  - question: What does the report show and how do I read it?
    answer: >-
      The report lists each image with its name, tag, and a status symbol. A green tick (✅) means that arm64 support
      is present, and a red cross (❌)  means that arm64 isn't available. A blue up symbol (🆙) means that a newer tag adds arm64, and a red cross mark (🚫) indicates
      an error occurred while checking the image.
  - question: What should I do when a line shows the blue up indicator?
    answer: >-
      Update your Kubernetes configuration to use the newer image tag that includes arm64 support.
      Re-run `kubearchinspect images` to confirm the status changes to a green tick.
  - question: What should I check if an image shows a red cross?
    answer: >-
      Review the source registry for alternative tags or a different image that provides arm64.
      If no tags or images are available, note that the current image doesn't support Arm and plan accordingly.
  - question: What should I do if a line shows a red cross mark?
    answer: >-
      Rerun the scan and verify that the image reference is valid and can be queried at its source
      registry. If the issue persists, investigate access to the registry for that image.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
platforms:
  - AWS Graviton
  - Microsoft Azure Cobalt
  - Google Axion
  - Oracle Cloud Infrastructure (OCI) Ampere Compute
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
