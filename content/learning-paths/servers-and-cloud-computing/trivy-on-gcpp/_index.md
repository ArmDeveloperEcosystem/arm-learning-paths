---
title: Scan multi-architecture containers with Trivy on Azure Cobalt 100

minutes_to_complete: 45

who_is_this_for: This learning path is for developers and DevOps engineers who want to integrate security scanning into CI/CD pipelines for multi-architecture container images.

learning_objectives:
    - Build and scan multi-architecture container images using Trivy on Azure Cobalt 100
    - Configure self-hosted GitHub Actions Arm runners for CI/CD pipelines
    - Enforce security gates in CI pipelines based on vulnerability severity

prerequisites:
    - A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6)
    - Docker installed and basic knowledge of containerization
    - Familiarity with CI/CD concepts
    - Basic knowledge of Linux command-line operations

author: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
cloud_service_providers: Microsoft Azure

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
      title: GitHub Actions Documentation
      link: https://docs.github.com/en/actions
      type: documentation
  - resource:
      title: Microsoft Azure Cobalt 100 Overview
      link: https://techcommunity.microsoft.com/blog/azurecompute/announcing-the-preview-of-new-azure-vms-based-on-the-azure-cobalt-100-processor/4146353
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---

Trivy is an open-source security scanner that helps detect vulnerabilities in container images, filesystems, and infrastructure configurations. When you integrate Trivy into your CI/CD pipelines, you can shift security left by identifying issues early in the development process. This Learning Path shows you how to build multi-architecture container images and scan them using Trivy on Azure Cobalt 100 Arm-based processors.

## Before you begin

Before you start, ensure you have:

- A [Microsoft Azure](https://azure.microsoft.com/) account with access to Cobalt 100 based instances (Dpsv6)
- Docker installed and basic knowledge of containerization
- Familiarity with CI/CD concepts
- Basic knowledge of Linux command-line operations

## What you'll learn

By the end of this Learning Path, you will be able to:

- Build and scan multi-architecture (amd64/arm64) container images using Trivy
- Configure self-hosted GitHub Actions Arm runners on Azure Cobalt 100
- Enforce automated security gates in CI/CD pipelines based on vulnerability severity
- Generate and analyze vulnerability reports for compliance and audit purposes
