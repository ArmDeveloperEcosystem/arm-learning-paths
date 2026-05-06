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

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:56Z'
  generator: template
  source_hash: c6106f21859f5a8e04bbd579db47c7177bb5371d4c7f306054e56e81ed9e89a1
  summary: >-
    Learn how to deploy and manage applications on Google Cloud GKE Arm64 clusters using Argo
    CD GitOps workflows with automated sync and self-healing on Axion processors. It is designed
    for developers and platform engineers who want hands-on experience implementing GitOps using
    Argo CD on Arm64-based Google Kubernetes Engine (GKE) clusters running on Google Axion (C4A)
    processors. By the end, you will be able to provision an Arm-based SUSE Linux Enterprise Server
    (SLES) virtual machine on Google Cloud (C4A with Axion processors), create and connect to
    a Google Kubernetes Engine (GKE) cluster running on Arm64 (Axion) nodes, and install and validate
    Argo CD on an Arm-based GKE cluster. It focuses on tools and technologies such as Argo CD,
    Kubernetes, kubectl, GKE, and Git, Linux environments, Arm platforms including Neoverse, and
    cloud platforms such as Google Cloud. The main steps cover Get started with Argo CD on Google
    Axion C4A (Arm-based), Create a Google Axion C4A virtual machine on Google Cloud, Prepare
    a GKE cluster for Argo CD deployments, Install and access Argo CD on Arm64 GKE, and Deploy
    applications using GitOps with Argo CD.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Arm-based SUSE Linux Enterprise Server (SLES) virtual machine on Google
      Cloud (C4A with Axion processors), create and connect to a Google Kubernetes Engine (GKE)
      cluster running on Arm64 (Axion) nodes, and install and validate Argo CD on an Arm-based
      GKE cluster. Learn how to deploy and manage applications on Google Cloud GKE Arm64 clusters
      using Argo CD GitOps workflows with automated sync and self-healing on Axion processors.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for developers and platform engineers who want hands-on experience
      implementing GitOps using Argo CD on Arm64-based Google Kubernetes Engine (GKE) clusters
      running on Google Axion (C4A) processors.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud Platform (GCP)](https://cloud.google.com/free)
      account with billing enabled; Basic familiarity with [Kubernetes concepts](https://kubernetes.io/docs/concepts/);
      Basic understanding of Git and GitHub workflows; Familiarity with basic Linux command-line
      usage.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Argo CD, Kubernetes, kubectl, GKE, and Git, Linux
      environments, Arm platforms such as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Get started with Argo CD on Google Axion C4A (Arm-based),
      Create a Google Axion C4A virtual machine on Google Cloud, Prepare a GKE cluster for Argo
      CD deployments, Install and access Argo CD on Arm64 GKE, and Deploy applications using GitOps
      with Argo CD.
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

