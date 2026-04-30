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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-04-30T18:58:18Z'
  generator: template
  source_hash: 87e9d25d5fb1f45d126aa4ca2fa1e13d6a470f2bcdc70968aa4622790106e629
  summary: >-
    Learn how to install Helm on Google Cloud Axion C4A SUSE VMs and deploy applications like
    NGINX, PostgreSQL, and Redis using Helm charts. It is designed for This is an introductory
    topic intended for developers who want to get hands-on experience using Helm on Linux Arm64
    systems, specifically Google Cloud C4A virtual machines powered by Axion processors. By the
    end, you will be able to provision an Arm-based SUSE Linux Enterprise Server (SLES) virtual
    machine on Google Cloud (C4A with Axion processors), install and configure Helm and kubectl
    on a SUSE Arm64 (C4A) instance, and create and connect to a Google Kubernetes Engine (GKE)
    cluster running on Arm-based nodes. It focuses on tools and technologies such as Helm, Kubernetes,
    kubectl, GKE, and PostgreSQL, Linux environments, Arm platforms including Neoverse, and cloud
    platforms such as Google Cloud. The main steps cover Get started with Helm on Google Axion
    C4A (Arm-based), Create a Google Axion C4A virtual machine on Google Cloud, Install Helm,
    Validate Helm workflows on a Google Axion C4A virtual machine, and Prepare a GKE cluster for
    Helm deployments.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Arm-based SUSE Linux Enterprise Server (SLES) virtual machine on Google
      Cloud (C4A with Axion processors), install and configure Helm and kubectl on a SUSE Arm64
      (C4A) instance, and create and connect to a Google Kubernetes Engine (GKE) cluster running
      on Arm-based nodes. Learn how to install Helm on Google Cloud Axion C4A SUSE VMs and deploy
      applications like NGINX, PostgreSQL, and Redis using Helm charts.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic intended for developers who want to get hands-on experience
      using Helm on Linux Arm64 systems, specifically Google Cloud C4A virtual machines powered
      by Axion processors.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud Platform (GCP)](https://cloud.google.com/free)
      account with billing enabled; Basic familiarity with [Kubernetes concepts](https://kubernetes.io/docs/concepts/);
      Basic understanding of [Helm](https://helm.sh/docs/topics/architecture/) and Kubernetes
      manifests; Familiarity with basic Linux command-line usage.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Helm, Kubernetes, kubectl, GKE, and PostgreSQL,
      Linux environments, Arm platforms such as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Get started with Helm on Google Axion C4A (Arm-based),
      Create a Google Axion C4A virtual machine on Google Cloud, Install Helm, Validate Helm workflows
      on a Google Axion C4A virtual machine, and Prepare a GKE cluster for Helm deployments.
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
