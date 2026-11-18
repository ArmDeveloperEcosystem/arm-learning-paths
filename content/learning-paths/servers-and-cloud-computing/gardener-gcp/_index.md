---
title: Deploy Gardener on Google Cloud C4A (Arm-based Axion VMs)
description: Learn how to install and configure Gardener Kubernetes management platform on Google Cloud Axion C4A SUSE Arm64 instances and deploy workload clusters.

minutes_to_complete: 50

who_is_this_for: This is an introductory topic for software developers deploying and optimizing Gardener workloads on Linux Arm64 environments, specifically using Google Cloud C4A virtual machines (VMs) powered by Axion processors.

learning_objectives:
  - Provision an Arm-based SUSE Linux Enterprise Server (SLES) virtual machine on Google Cloud (C4A with Axion processors).
  - Install and configure Gardener on a SUSE Arm64 (C4A) instance.
  - Deploy Garden, Seed, and Shoot clusters locally using Kubernetes in Docker (KinD).
  - Validate Gardener functionality by deploying workloads into a Shoot cluster.
  - Perform baseline security benchmarking of Gardener-managed Kubernetes clusters using kube-bench on Arm64.

prerequisites:
  - A [Google Cloud Platform (GCP)](https://cloud.google.com/free) account with billing enabled
  - Basic familiarity with [Kubernetes](https://kubernetes.io/)
  - Familiarity with container concepts ([Docker](https://www.docker.com/))

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-10T22:02:24Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 68ba69768ef8058c5413b98fba7e4406a76ca14944acc6971c15b21ed068dd00
  summary_generated_at: '2026-09-10T22:02:24Z'
  summary_source_hash: 68ba69768ef8058c5413b98fba7e4406a76ca14944acc6971c15b21ed068dd00
  faq_generated_at: '2026-09-10T22:02:24Z'
  faq_source_hash: 68ba69768ef8058c5413b98fba7e4406a76ca14944acc6971c15b21ed068dd00
  summary: >-
    You'll deploy Gardener Local on an Arm-based Google Cloud C4A VM running SUSE Linux Enterprise Server. First, you'll install KinD and the required tools, bootstrap Garden, Seed, and Shoot clusters, and validate them with `kubectl`. Then, you'll deploy a workload and run `kube-bench` to record a baseline against CIS Kubernetes benchmarks.
  faqs:
  - question: Which C4A VM size should I use?
    answer: >-
      Use the `c4a-standard-4` machine type with 4 vCPUs and 16 GB of memory. It provides sufficient
      resources to run Gardener Local with Garden, Seed, and Shoot clusters.
  - question: Where do Gardener’s Garden, Seed, and Shoot clusters run?
    answer: >-
      The clusters run locally using Kubernetes in Docker (KinD) on the Arm64-based SUSE VM. This keeps all
      Gardener components on the single C4A host for evaluation.
  - question: How do I point kubectl to the right cluster context?
    answer: >-
      Export `KUBECONFIG` to the generated `kubeconfig`, for example: `$PWD/example/gardener-local/kind/local/kubeconfig`.
      After exporting, `kubectl` commands should connect to the intended cluster without authentication
      errors.
  - question: How do I know the clusters are healthy before deploying workloads?
    answer: >-
      Proceed when Garden and Shoot report `Ready` and the environment indicates healthy status
      for the KinD-based clusters. If readiness is pending, wait for controllers to finish reconciling.
  - question: What should I expect from running kube-bench?
    answer: >-
      `kube-bench` evaluates your cluster against CIS Kubernetes benchmarks and reports findings
      mapped to those controls. Use the results as a baseline to track configuration changes over
      time on the Arm64 environment.
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
