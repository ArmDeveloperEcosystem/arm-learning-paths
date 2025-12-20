---
title: Deploy Gardener on Google Cloud C4A (Arm-based Axion VMs)

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

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers: Google Cloud

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
