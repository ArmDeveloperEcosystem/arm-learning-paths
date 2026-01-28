---
title: Deploy applications on Arm-based GKE using GitOps with Argo CD

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

author: Pareena Verma

##### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers: Google Cloud

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
