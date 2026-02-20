---
title: Scan multi-architecture containers with Trivy on Azure Cobalt 100

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for developers and DevOps engineers who want to integrate security scanning into CI/CD pipelines for multi-architecture container images.

learning_objectives:
    - Build and scan multi-architecture container images using Trivy on Azure Cobalt 100
    - Configure self-hosted GitHub Actions Arm runners for CI/CD pipelines
    - Enforce security gates in CI pipelines based on vulnerability severity

prerequisites:
  - A [Microsoft Azure account](https://azure.microsoft.com/) with access to Cobalt 100 based instances (Dpsv6)
  - Docker installed and basic knowledge of containerization
  - Familiarity with CI/CD concepts
  - Basic knowledge of Linux command-line operations
  - Familiarity with GitHub Actions runners

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers: 
    - Microsoft Azure

armips:
    - Neoverse

tools_software_languages:
    - Trivy
    - Docker
    - GitHub Actions
    - YAML

operatingsystems:
    - Linux

further_reading:
  - resource:
      title: Trivy Official Website
      link: https://trivy.dev
      type: website
  - resource:
      title: Trivy GitHub Repository
      link: https://github.com/aquasecurity/trivy
      type: website
  - resource:
      title: Docker Official Documentation
      link: https://docs.docker.com/
      type: documentation
  - resource:
      title: GitHub Actions runners
      link: https://docs.github.com/en/actions/hosting-your-own-runners
      type: documentation
  - resource:
      title: Azure Cobalt 100 processors
      link: https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
