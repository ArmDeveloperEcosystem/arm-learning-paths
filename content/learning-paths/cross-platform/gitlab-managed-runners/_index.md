---
title: Build a CI/CD pipeline using GitLab-hosted Arm runners


minutes_to_complete: 30

who_is_this_for: This is an introductory topic for DevOps engineers who want to build CI/CD pipelines on Arm-based infrastructure using GitLab-hosted runners.

description: Learn how to build GitLab CI/CD pipelines using GitLab-hosted Arm64 runners to containerize C applications, store images in GitLab Container Registry, and deploy on Arm infrastructure.

learning_objectives: 
    - Create a GitLab project with CI/CD configuration
    - Configure pipeline stages to use Arm64 runners
    - Build and containerize applications for Arm64 architecture
    - Store container images in GitLab Container Registry
    

prerequisites:
    - A GitLab account (free tier includes Arm64 runner access)

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:53Z'
  generator: template
  source_hash: a6ad703d9d894da06ed4aa3725fcc9006d70050cef3f0a3ef9a758bcf4523289
  summary: >-
    Learn how to build GitLab CI/CD pipelines using GitLab-hosted Arm64 runners to containerize
    C applications, store images in GitLab Container Registry, and deploy on Arm infrastructure.
    It is designed for DevOps engineers who want to build CI/CD pipelines on Arm-based infrastructure
    using GitLab-hosted runners. By the end, you will be able to create a GitLab project with
    CI/CD configuration, configure pipeline stages to use Arm64 runners, and build and containerize
    applications for Arm64 architecture. It focuses on tools and technologies such as GitLab,
    Docker, and C, Linux environments, Arm platforms including Neoverse, and cloud platforms such
    as Google Cloud. The main steps cover Build and use GitLab-hosted Arm runners for CI/CD, Create
    a GitLab project, Build and configure your Arm64 CI/CD pipeline, and Run pipeline and verify
    results.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will create a GitLab project with CI/CD configuration, configure pipeline stages to
      use Arm64 runners, and build and containerize applications for Arm64 architecture. Learn
      how to build GitLab CI/CD pipelines using GitLab-hosted Arm64 runners to containerize C
      applications, store images in GitLab Container Registry, and deploy on Arm infrastructure.
  - question: Who is this Learning Path for?
    answer: >-
      This is an introductory topic for DevOps engineers who want to build CI/CD pipelines on
      Arm-based infrastructure using GitLab-hosted runners.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: A GitLab account (free tier includes
      Arm64 runner access).
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including GitLab, Docker, and C, Linux environments, Arm platforms
      such as Neoverse, and cloud platforms such as Google Cloud.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Build and use GitLab-hosted Arm runners for CI/CD,
      Create a GitLab project, Build and configure your Arm64 CI/CD pipeline, and Run pipeline
      and verify results.
# END generated_summary_faq

author: Mohamed Ismail

### Tags
skilllevels: Introductory
subjects: CI-CD
cloud_service_providers:
  - Google Cloud

armips:
    - Neoverse

tools_software_languages:
    - GitLab
    - Docker
    - C

operatingsystems:
    - Linux

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - embedded-and-microcontrollers

further_reading:
    - resource:
        title: GitLab CI/CD documentation 
        link: https://docs.gitlab.com/ee/ci/
        type: documentation
    - resource:
        title: GitLab-hosted Arm runners
        link: https://docs.gitlab.com/ci/runners/hosted_runners/linux.html
        type: documentation
    - resource:
        title: Docker install guide
        link: https://learn.arm.com/install-guides/docker/
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

