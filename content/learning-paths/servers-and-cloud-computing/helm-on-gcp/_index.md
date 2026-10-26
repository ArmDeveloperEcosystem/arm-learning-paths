---
title: Install and validate Helm on Google Cloud C4A Arm-based VMs
description: Learn how to install Helm on Google Cloud Axion C4A SUSE VMs and deploy applications like NGINX, PostgreSQL, and Redis using Helm charts.

minutes_to_complete: 60

who_is_this_for: This is an introductory topic intended for developers who want to get hands-on experience using Helm on Linux Arm64 systems, specifically Google Cloud C4A virtual machines (VMs) powered by Axion processors.

learning_objectives:
  - Provision an Arm-based SUSE Linux Enterprise Server (SLES) VM on Google Cloud (C4A with Axion processors).
  - Install and configure Helm and kubectl on a SUSE Arm64 (C4A) instance.
  - Create and connect to a Google Kubernetes Engine (GKE) cluster running on Arm-based nodes.
  - Deploy PostgreSQL, Redis, and NGINX on GKE using official Helm charts.
  - Validate Helm workflows by performing install, upgrade, rollback, and uninstall operations.
  - Verify application readiness and service access for PostgreSQL, Redis, and NGINX on GKE.
  - Observe Helm behavior under concurrent CLI operations on an Arm64-based Kubernetes cluster.

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with [Kubernetes concepts](https://kubernetes.io/docs/concepts/)
  - Basic understanding of [Helm](https://helm.sh/docs/topics/architecture/) and Kubernetes manifests
  - Familiarity with basic Linux command-line usage

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-15T21:15:22Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 68dd3fded09896a3b3ced1a118adeeaad8494c1b14693988e61e377f52bad76a
  summary_generated_at: '2026-09-15T21:15:22Z'
  summary_source_hash: 68dd3fded09896a3b3ced1a118adeeaad8494c1b14693988e61e377f52bad76a
  faq_generated_at: '2026-09-15T21:15:22Z'
  faq_source_hash: 68dd3fded09896a3b3ced1a118adeeaad8494c1b14693988e61e377f52bad76a
  summary: >-
    You'll install and validate Helm on an Arm-based Google Axion C4A VM running
    SUSE Linux, then deploy charts to GKE. First, you'll prepare the SUSE environment and use a local
    KinD cluster to practice adding repositories, installing, upgrading, rolling back, and
    uninstalling charts. Then, you'll deploy PostgreSQL, Redis, and NGINX on GKE and verify that
    the pods and services respond as configured.
  faqs:
  - question: Which C4A machine type should I use?
    answer: >-
      Use the `c4a-standard-4` machine type, which provides 4 vCPUs and 16 GB of memory.
  - question: How do I verify that kubectl is installed correctly before working with GKE?
    answer: >-
      Run `kubectl version --client` to confirm that the client is installed. A `Client Version` and
      `Kustomize Version` in the output confirm the installation.
  - question: What output should I expect after adding the Bitnami Helm repository?
    answer: >-
      Run `helm repo add bitnami https://charts.bitnami.com/bitnami` and then `helm repo update`.
      Expect a message that the repository was added, followed by a successful update from the
      Bitnami chart repository.
  - question: When should I use the local KinD cluster versus GKE?
    answer: >-
      Use the KinD-based local cluster to validate Helm installation and core workflows on the
      SUSE VM. Move to GKE to deploy PostgreSQL, Redis, and NGINX as services on a managed Kubernetes
      environment.
  - question: How do I know that the Helm deployments are ready to use?
    answer: >-
      Run `helm list`, `kubectl get pods`, and `kubectl get svc`. The Helm release should report
      `deployed`, the pods should report `Running`, and the services should be listed. If a pod is
      `Pending`, wait 30 to 60 seconds for the images to download and retry.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
platforms:
  - Google Axion

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
