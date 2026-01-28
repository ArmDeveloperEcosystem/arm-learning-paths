---
title: Secure Multi-Architecture Containers with Trivy on Azure Cobalt 100 (Arm64)

minutes_to_complete: 45

who_is_this_for: This learning path is designed for developers and DevOps engineers who want to integrate security scanning into CI/CD pipelines for multi-architecture container images.

learning_objectives:
    - Provision an Azure Arm64 virtual machine using Azure console, with Ubuntu Pro 24.04 LTS as the base image
    - Build multi-architecture (amd64/arm64) container images for Azure Cobalt 100
    - Install and configure Trivy on Arm64 Ubuntu systems
    - Scan container images for vulnerabilities locally and in CI
    - Configure self-hosted GitHub Actions Arm runners
    - Enforce security gates in CI/CD pipelines based on vulnerability severity
    - Generate and analyze JSON reports for compliance and audit purposes

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
