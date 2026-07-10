---
title: Deploy applications on Arm-based GKE using GitOps with Argo CD
description: Learn how to deploy and manage applications on Google Cloud GKE Arm64 clusters using Argo CD GitOps workflows with automated sync and self-healing on Axion processors.

minutes_to_complete: 40

who_is_this_for: This is an introductory topic for developers and platform engineers who want hands-on experience implementing GitOps using Argo CD on Arm64-based Google Kubernetes Engine (GKE) clusters running on Google Axion (C4A) processors.

learning_objectives:
  - Provision an Arm-based SUSE Linux Enterprise Server (SLES) virtual machine on Google Cloud (C4A with Axion processors)
  - Create and connect to a Google Kubernetes Engine (GKE) cluster running on Arm64 (Axion) nodes
  - Install and validate Argo CD on an Arm-based GKE cluster
  - Understand Argo CD core components and GitOps architecture
  - Deploy a production-ready application using pure GitOps workflows
  - Enable automated sync, pruning, and self-healing with Argo CD
  - Verify application health and access to deployed services on GKE

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with [Kubernetes concepts](https://kubernetes.io/docs/concepts/)
  - Basic understanding of Git and GitHub workflows
  - Familiarity with basic Linux command-line usage

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-26T17:25:48Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c6106f21859f5a8e04bbd579db47c7177bb5371d4c7f306054e56e81ed9e89a1
  summary_generated_at: '2026-06-26T17:25:48Z'
  summary_source_hash: c6106f21859f5a8e04bbd579db47c7177bb5371d4c7f306054e56e81ed9e89a1
  faq_generated_at: '2026-06-26T17:25:48Z'
  faq_source_hash: c6106f21859f5a8e04bbd579db47c7177bb5371d4c7f306054e56e81ed9e89a1
  summary: >-
    You'll deploy applications on Arm-based Google Kubernetes Engine using
    GitOps with Argo CD on Google Cloud C4A instances built on Arm Neoverse V2 cores. Starting
    from a SUSE Linux `arm64` VM, you'll provision an `arm64` GKE environment and install Argo CD
    using official upstream manifests. You'll configure browser and CLI access, retrieve admin credentials,
    and define a Git-backed workflow that continuously reconciles Kubernetes resources. Then, you'll deploy
    a production-ready NGINX application from a GitHub repository with automated sync, pruning,
    and self-healing enabled. By the end, you'll validate application health and confirm
    service access on the `arm64` GKE cluster.
  faqs:
  - question: Do I need a specific Linux distribution on the VM used to manage the cluster?
    answer: >-
      Yes. The steps use a SUSE Linux `arm64` VM and rely on `zypper` for package management.
      Use an `arm64` SLES environment to match the commands shown.
  - question: How do I know `kubectl` is targeting the `arm64` GKE cluster before installing Argo
      CD?
    answer: >-
      Confirm the current Kubernetes context points to your intended GKE cluster and namespace.
      In the Google Cloud console, verify the node pool uses C4A machine types to ensure you are
      operating on Arm64 nodes.
  - question: What indicates that Argo CD installed and is accessible correctly?
    answer: >-
      The `argo-cd` namespace exists, core Argo CD pods report `Ready`, and the web UI is reachable
      in a browser. You should also be able to retrieve the initial admin credentials and authenticate
      with the Argo CD CLI.
  - question: Which repository setup does Argo CD use for the NGINX GitOps deployment?
    answer: >-
      Provide a GitHub repository you control and specify the repository URL and path when configuring
      Argo CD for the application. Argo CD then creates and syncs the Kubernetes resources from
      that path, and you should see the NGINX deployment and service in the cluster and in the
      Argo CD UI.
  - question: What should I expect after enabling automated sync, pruning, and self-healing in
      Argo CD?
    answer: >-
      Argo CD applies changes from Git automatically, removes resources that are no longer defined,
      and corrects drift from out-of-band edits. The application should report `Synced` and `Healthy`,
      and the resource list in Argo CD should match what’s in the repository.
# END generated_summary_faq

author: Pareena Verma

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

##### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers:
  - Google Cloud

armips:
  - Neoverse

tools_software_languages:
  - Argo CD
  - Kubernetes
  - kubectl
  - GKE
  - Git
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
      title: Argo CD documentation
      link: https://argo-cd.readthedocs.io/en/stable/ 
      type: documentation

  - resource:
      title: Kubernetes documentation
      link: https://kubernetes.io/docs/
      type: documentation

weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
