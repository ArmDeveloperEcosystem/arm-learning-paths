---
title: Deploy Gardener on Google Cloud C4A (Arm-based Axion VMs)
description: Learn how to install and configure Gardener Kubernetes management platform on Google Cloud Axion C4A SUSE Arm64 instances and deploy workload clusters.

minutes_to_complete: 50

who_is_this_for: This is an introductory topic for software developers deploying and optimizing Gardener workloads on Linux Arm64 environments, specifically using Google Cloud C4A virtual machines powered by Axion processors.

learning_objectives:
  - Provision an Arm-based SUSE Linux Enterprise Server (SLES) virtual machine on Google Cloud (C4A with Axion processors)
  - Install and configure Gardener on a SUSE Arm64 (C4A) instance
  - Deploy Garden, Seed, and Shoot clusters locally using Kubernetes in Docker (KinD)
  - Validate Gardener functionality by deploying workloads into a Shoot cluster
  - Perform baseline security benchmarking of Gardener-managed Kubernetes clusters using kube-bench on Arm64

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with [Kubernetes](https://kubernetes.io/)
  - Familiarity with container concepts ([Docker](https://www.docker.com/))

generate_summary_faq: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:57Z'
  generator: template
  source_hash: 85d3d64e0eb0c3cfa0eee29cf1e4199049a6dcbf69634e578dad2b5443ca2b7f
  summary: >-
    Learn how to install and configure Gardener Kubernetes management platform on Google Cloud
    Axion C4A SUSE Arm64 instances and deploy workload clusters. It is designed for software developers
    deploying and optimizing Gardener workloads on Linux Arm64 environments, specifically using
    Google Cloud C4A virtual machines powered by Axion processors. By the end, you will be able
    to provision an Arm-based SUSE Linux Enterprise Server (SLES) virtual machine on Google Cloud
    (C4A with Axion processors), install and configure Gardener on a SUSE Arm64 (C4A) instance,
    and deploy Garden, Seed, and Shoot clusters locally using Kubernetes in Docker (KinD). It
    focuses on tools and technologies such as Gardener, Kubernetes, Docker, KinD, and Helm, Linux
    environments, Arm platforms including Neoverse, and cloud platforms such as Google Cloud.
    The main steps cover Get started with Gardener on Google Axion C4A (Arm Neoverse-V2), Create
    a Google Axion C4A Arm virtual machine for Gardener, Install Gardener on your Arm-based SUSE
    VM, Verify Gardener cluster health and functionality, and Benchmark Gardener cluster security
    with kube-bench.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will provision an Arm-based SUSE Linux Enterprise Server (SLES) virtual machine on Google
      Cloud (C4A with Axion processors), install and configure Gardener on a SUSE Arm64 (C4A)
      instance, and deploy Garden, Seed, and Shoot clusters locally using Kubernetes in Docker
      (KinD). Learn how to install and configure Gardener Kubernetes management platform on Google
      Cloud Axion C4A SUSE Arm64 instances and deploy workload clusters.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for software developers deploying and optimizing Gardener
      workloads on Linux Arm64 environments, specifically using Google Cloud C4A virtual machines
      powered by Axion processors.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A [Google Cloud Platform (GCP)](https://cloud.google.com/free)
      account with billing enabled; Basic familiarity with [Kubernetes](https://kubernetes.io/);
      Familiarity with container concepts ([Docker](https://www.docker.com/)).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Gardener, Kubernetes, Docker, KinD, and Helm, Linux
      environments, Arm platforms such as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Get started with Gardener on Google Axion C4A (Arm
      Neoverse-V2), Create a Google Axion C4A Arm virtual machine for Gardener, Install Gardener
      on your Arm-based SUSE VM, Verify Gardener cluster health and functionality, and Benchmark
      Gardener cluster security with kube-bench.
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
  - Gardener
  - Kubernetes
  - Docker
  - KinD
  - Helm
  - kube-bench

operatingsystems:
  - Linux

# ================================================================================
#       FIXED, DO NOT MODIFY
# ================================================================================
further_reading:
  - resource:
      title: Gardener documentation
      link: https://gardener.cloud/
      type: documentation

  - resource:
      title: Gardener GitHub repository
      link: https://github.com/gardener/gardener
      type: documentation

  - resource:
      title: Kubernetes documentation
      link: https://kubernetes.io/docs/
      type: documentation

  - resource:
      title: kube-bench security benchmarking tool
      link: https://github.com/aquasecurity/kube-bench
      type: documentation
    
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

