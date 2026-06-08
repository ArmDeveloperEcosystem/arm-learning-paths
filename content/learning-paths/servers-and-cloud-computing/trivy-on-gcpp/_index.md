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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T02:13:05Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 13bba1dee1c948f8b751a71479a5106014a2c21dab6ce3968a08bed9e3363de1
  summary_generated_at: '2026-06-02T05:22:29Z'
  summary_source_hash: 13bba1dee1c948f8b751a71479a5106014a2c21dab6ce3968a08bed9e3363de1
  faq_generated_at: '2026-06-03T02:13:05Z'
  faq_source_hash: 13bba1dee1c948f8b751a71479a5106014a2c21dab6ce3968a08bed9e3363de1
  summary: >-
    This Learning Path guides you through building and scanning multi-architecture container images
    with Trivy on Microsoft Azure Cobalt 100 Arm64 virtual machines. You will provision a Dpsv6
    series VM via the Azure Portal, configure Docker Buildx, create a demo container, push a multi-architecture
    image to Docker Hub, install and verify Trivy on Ubuntu, run local vulnerability scans, and
    generate reports. It also covers configuring self-hosted GitHub Actions Arm runners and adding
    severity-based security gates to CI pipelines. Prerequisites include an Azure account with
    access to Cobalt 100 instances, Docker knowledge, familiarity with CI/CD and GitHub Actions
    runners, basic Linux command-line skills, and a Docker Hub account.
  faqs:
  - question: What do I need before starting this Learning Path?
    answer: >-
      You need a Microsoft Azure account with access to Cobalt 100 instances (Dpsv6), Docker installed
      with basic containerization knowledge, familiarity with CI/CD concepts and GitHub Actions
      runners, and basic Linux command-line skills. For the build and scan steps, ensure you have
      an Arm64 Ubuntu VM running on Cobalt 100 and a Docker Hub account.
  - question: Which Azure VM size and operating system should I use?
    answer: >-
      Use a general-purpose Dpsv6 series VM with the Arm-based Azure Cobalt 100 processor. The
      steps use an Arm64 Ubuntu VM.
  - question: Can I create the VM with Azure CLI or infrastructure as code instead of the Portal?
    answer: >-
      Yes, Azure CLI and IaC are common options. This Learning Path focuses on using the Azure
      Portal to create the Cobalt 100 VM.
  - question: How do I build a multi-architecture container image on the VM?
    answer: >-
      You will configure Docker Buildx for multi-architecture builds, create a demo container
      application, and push the resulting image to Docker Hub. The steps guide you through enabling
      Buildx and validating the build on the Arm64 VM.
  - question: What should I expect from Trivy scanning and how is it used in CI?
    answer: >-
      You will install and verify Trivy on the Arm64 VM, run local vulnerability scans, and generate
      reports with findings categorized by severity. In CI pipelines, you will configure self-hosted
      GitHub Actions Arm runners and enforce security gates based on vulnerability severity.
# END generated_summary_faq

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

