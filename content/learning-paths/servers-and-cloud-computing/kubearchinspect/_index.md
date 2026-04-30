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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:18Z'
  generator: template
  source_hash: 43e4e28b88b9721ca94457418f3b4887d0099017578a54da1db5fcdc11f4a122
  summary: >-
    Identify and migrate container images in a Kubernetes cluster to Arm-compatible versions using
    KubeArchInspect reports. It is designed for software developers who want to ensure containers
    running in a Kubernetes cluster support the Arm architecture. By the end, you will be able
    to run KubeArchInspect to generate a report on the containers running in a Kubernetes cluster,
    discover which images support the Arm architecture, and understand common reasons for an image
    not supporting Arm. It focuses on tools and technologies such as Kubernetes and Runbook, Linux
    environments, Arm platforms including Neoverse, and cloud platforms such as AWS, Microsoft
    Azure, Google Cloud, and Oracle. The main steps cover Install KubeArchInspect, Run KubeArchInspect,
    and Analyze the results.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will run KubeArchInspect to generate a report on the containers running in a Kubernetes
      cluster, discover which images support the Arm architecture, and understand common reasons
      for an image not supporting Arm. Identify and migrate container images in a Kubernetes cluster
      to Arm-compatible versions using KubeArchInspect reports.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for software developers who want to ensure containers running
      in a Kubernetes cluster support the Arm architecture.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A running Kubernetes cluster accessible
      with `kubectl`.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Kubernetes and Runbook, Linux environments, Arm
      platforms such as Neoverse, and cloud platforms such as AWS, Microsoft Azure, Google Cloud,
      and Oracle.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Install KubeArchInspect, Run KubeArchInspect, and
      Analyze the results.
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

