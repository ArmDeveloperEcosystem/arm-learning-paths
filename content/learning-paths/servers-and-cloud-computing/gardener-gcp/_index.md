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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:58:45Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 85d3d64e0eb0c3cfa0eee29cf1e4199049a6dcbf69634e578dad2b5443ca2b7f
  summary_generated_at: '2026-06-02T03:57:32Z'
  summary_source_hash: 85d3d64e0eb0c3cfa0eee29cf1e4199049a6dcbf69634e578dad2b5443ca2b7f
  faq_generated_at: '2026-06-03T00:58:45Z'
  faq_source_hash: 85d3d64e0eb0c3cfa0eee29cf1e4199049a6dcbf69634e578dad2b5443ca2b7f
  summary: >-
    Learn how to provision a Google Cloud C4A virtual machine powered by Axion (Arm Neoverse-V2)
    and install Gardener on SUSE Linux Enterprise Server (Arm64). You will set up Gardener Local,
    deploy Garden, Seed, and Shoot clusters using Kubernetes in Docker (KinD), and validate functionality
    by deploying workloads into a Shoot cluster. The path uses tools including Kubernetes, Docker,
    KinD, Helm, and kube-bench, and includes baseline security benchmarking against CIS Kubernetes
    guidelines. Prerequisites are a Google Cloud account with billing enabled plus basic familiarity
    with Kubernetes and Docker. The steps focus on a c4a-standard-4 VM configuration suitable
    for running Gardener Local on Arm.
  faqs:
  - question: What do I need before creating the Axion C4A VM on Google Cloud?
    answer: >-
      You need a Google Cloud Platform account with billing enabled. Basic familiarity with Kubernetes
      and Docker is also assumed.
  - question: Which VM type and operating system does this path use for Gardener?
    answer: >-
      You will use a c4a-standard-4 instance (4 vCPUs, 16 GB memory) on Google Cloud C4A with
      SUSE Linux Enterprise Server. This configuration is sufficient for running Gardener Local
      with Garden, Seed, and Shoot clusters.
  - question: Do the Garden, Seed, and Shoot clusters run in the cloud or locally?
    answer: >-
      They run locally on the C4A VM using Kubernetes in Docker (KinD). The path deploys Garden,
      Seed, and Shoot clusters without requiring a separate managed Kubernetes service.
  - question: How do I point kubectl at the Gardener Local cluster to validate the setup?
    answer: >-
      Set the KUBECONFIG environment variable to $PWD/example/gardener-local/kind/local/kubeconfig.
      Then follow the verification steps to check cluster health and confirm Garden and Shoot
      resources report Ready states.
  - question: What should be ready before running kube-bench, and what output should I expect?
    answer: >-
      Ensure Gardener Local is running with Garden and Shoot clusters in Ready state and Docker
      is available. kube-bench will check the cluster against CIS Kubernetes benchmarks and produce
      a baseline security report.
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

