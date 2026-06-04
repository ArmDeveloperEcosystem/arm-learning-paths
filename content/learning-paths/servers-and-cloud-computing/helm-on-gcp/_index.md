---
title: Install and validate Helm on Google Cloud C4A Arm-based VMs
description: Learn how to install Helm on Google Cloud Axion C4A SUSE VMs and deploy applications like NGINX, PostgreSQL, and Redis using Helm charts.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic intended for developers who want to get hands-on experience using Helm on Linux Arm64 systems, specifically Google Cloud C4A virtual machines powered by Axion processors.


learning_objectives:
  - Provision an Arm-based SUSE Linux Enterprise Server (SLES) virtual machine on Google Cloud (C4A with Axion processors)
  - Install and configure Helm and kubectl on a SUSE Arm64 (C4A) instance
  - Create and connect to a Google Kubernetes Engine (GKE) cluster running on Arm-based nodes
  - Deploy PostgreSQL, Redis, and NGINX on GKE using official Helm charts
  - Validate Helm workflows by performing install, upgrade, rollback, and uninstall operations
  - Verify application readiness and service access for PostgreSQL, Redis, and NGINX on GKE
  - Observe Helm behavior under concurrent CLI operations on an Arm64-based Kubernetes cluster

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with [Kubernetes concepts](https://kubernetes.io/docs/concepts/)
  - Basic understanding of [Helm](https://helm.sh/docs/topics/architecture/) and Kubernetes manifests
  - Familiarity with basic Linux command-line usage
    

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:08:45Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 87e9d25d5fb1f45d126aa4ca2fa1e13d6a470f2bcdc70968aa4622790106e629
  summary_generated_at: '2026-06-02T04:06:17Z'
  summary_source_hash: 87e9d25d5fb1f45d126aa4ca2fa1e13d6a470f2bcdc70968aa4622790106e629
  faq_generated_at: '2026-06-03T01:08:45Z'
  faq_source_hash: 87e9d25d5fb1f45d126aa4ca2fa1e13d6a470f2bcdc70968aa4622790106e629
  summary: >-
    Follow this introductory, hands-on path to install and validate Helm on Arm-based Google Cloud
    Axion C4A virtual machines running SUSE Linux Enterprise Server. You will provision a C4A
    instance, install Docker, kubectl, Helm, and KinD, and verify Helm workflows on a local Arm64
    Kubernetes cluster. Next, you create and connect to a Google Kubernetes Engine (GKE) cluster
    on Arm-based nodes and deploy PostgreSQL, Redis, and NGINX using official Helm charts. You
    will perform install, upgrade, rollback, and uninstall operations, check application readiness
    and service access, and observe Helm behavior under concurrent CLI operations. Prerequisites
    include a GCP account with billing enabled and basic familiarity with Kubernetes, Helm, and
    the Linux command line.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Google Cloud Platform account with billing enabled, basic familiarity with Kubernetes
      concepts, a basic understanding of Helm and Kubernetes manifests, and comfort with the Linux
      command line.
  - question: Which Google Cloud machine type is used for the C4A VM in this path?
    answer: >-
      The steps use the c4a-standard-4 machine type, which provides 4 vCPUs and 16 GB of memory.
  - question: Which tools are installed on the SUSE Arm64 VM to prepare for Helm testing?
    answer: >-
      You install Docker, kubectl, Helm, and KinD, and enable the SUSE Containers Module. This
      setup lets you create and verify a local Kubernetes cluster for validating Helm workflows.
  - question: How do I confirm that Helm and the chart repository are set up correctly?
    answer: >-
      Add the Bitnami chart repository and run a repository update. You should see output indicating
      that "bitnami" was added and the repositories were successfully updated.
  - question: What is deployed to GKE, and how does that differ from the local KinD cluster?
    answer: >-
      On GKE you deploy PostgreSQL, Redis, and NGINX using official Helm charts, and verify readiness
      and service access. The earlier KinD-based cluster is used only for local validation before
      targeting GKE; verify kubectl availability with the command kubectl version -.
# END generated_summary_faq

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers:
  - Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Helm
  - Kubernetes
  - kubectl
  - GKE
  - PostgreSQL
  - Redis
  - NGINX
    
operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
  - resource:
      title: Google Cloud documentation
      link: https://cloud.google.com/docs
      type: documentation

  - resource:
      title: Helm documentation
      link: https://helm.sh/docs/
      type: documentation

  - resource:
      title: Kubernetes documentation
      link: https://kubernetes.io/docs/
      type: documentation

  - resource:
      title: Bitnami Helm Charts
      link: https://github.com/bitnami/charts
      type: documentation    

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

Helm is the package manager for Kubernetes, simplifying application deployment and lifecycle management. Google Axion C4A instances, powered by Arm Neoverse-V2 processors, provide an efficient platform for running Kubernetes workloads.

In this Learning Path, you learn how to install and configure Helm on a Google Cloud C4A virtual machine, create Kubernetes clusters, and deploy applications using both official and custom Helm charts. You validate Helm's core functionality and explore deployment patterns for PostgreSQL, Redis, and NGINX on Arm-based infrastructure.

By the end of this Learning Path, you'll have practical experience with Helm on Arm64 systems and understand how to deploy cloud-native applications on Google's Axion processors.
