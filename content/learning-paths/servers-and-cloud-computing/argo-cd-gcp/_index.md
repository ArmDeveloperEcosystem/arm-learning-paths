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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:17:35Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: c6106f21859f5a8e04bbd579db47c7177bb5371d4c7f306054e56e81ed9e89a1
  summary_generated_at: '2026-06-02T03:05:29Z'
  summary_source_hash: c6106f21859f5a8e04bbd579db47c7177bb5371d4c7f306054e56e81ed9e89a1
  faq_generated_at: '2026-06-03T00:17:35Z'
  faq_source_hash: c6106f21859f5a8e04bbd579db47c7177bb5371d4c7f306054e56e81ed9e89a1
  summary: >-
    Learn how to deploy and manage applications on Arm-based Google Kubernetes Engine (GKE) using
    Argo CD and GitOps. You will provision an Arm-based SUSE Linux Enterprise Server VM on a Google
    Axion C4A instance, create and connect to a GKE cluster running on Arm64 nodes, and install
    Argo CD using official manifests. The path covers configuring browser and CLI access, deploying
    a production-ready NGINX application from a Git repository, and enabling automated sync, pruning,
    and self-healing. By the end, you will verify application health and access to services on
    GKE. Prerequisites include a GCP account with billing enabled, basic Kubernetes and Git/GitHub
    knowledge, and Linux CLI familiarity.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      You need a Google Cloud Platform (GCP) account with billing enabled and basic familiarity
      with Kubernetes, Git/GitHub workflows, and Linux command-line usage. The path uses a SUSE
      Linux Arm64 VM that you provision on Google Cloud as part of the steps.
  - question: Which Google Cloud VM and OS are used for the setup host?
    answer: >-
      The example provisions a Google Axion C4A VM using the c4a-standard-4 machine type (4 vCPUs,
      16 GB memory) running SUSE Linux Enterprise Server (SLES) for Arm64. This VM is used to
      prepare and interact with the GKE environment.
  - question: What type of GKE cluster should I create for this path?
    answer: >-
      Create a production-ready Arm64 GKE cluster running on Axion (C4A) nodes to support GitOps
      deployments with Argo CD. The steps guide you to prepare the cluster from the SLES Arm64
      VM.
  - question: How do I know Argo CD is installed and accessible?
    answer: >-
      Argo CD is installed using the official upstream manifests into a dedicated namespace. You
      should be able to access the Argo CD UI in a browser, retrieve the admin credentials, and
      authenticate with the Argo CD CLI.
  - question: What repository do I need for the GitOps deployment?
    answer: >-
      You need a GitHub repository to store the GitOps manifests; an empty repository is sufficient
      to start. Argo CD continuously reconciles the cluster to match the desired state defined
      in this repo.
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

