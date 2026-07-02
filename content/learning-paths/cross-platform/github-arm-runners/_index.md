---
title: Build multi-architecture container images with GitHub Arm-hosted runners

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers who want to learn how to use Arm-hosted runners for GitHub Actions jobs. 

description: Learn how to use GitHub Actions with Arm-hosted runners to build multi-architecture container images for arm64 and amd64 platforms and automate deployment to Docker Hub.

learning_objectives:
    - Build Arm images and multi-architecture images with Arm-hosted runners.
    - Use GitHub Actions to automate image builds.

prerequisites:
    - A GitHub account (a Team or Enterprise Cloud plan is required for private repositories).
    - A Docker Hub account.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-02T17:56:18Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3557d534c51f81839cc353ebbd600ec588a60197d2c27c9a58e97c25017d07e4
  summary_generated_at: '2026-07-02T17:56:18Z'
  summary_source_hash: 3557d534c51f81839cc353ebbd600ec588a60197d2c27c9a58e97c25017d07e4
  faq_generated_at: '2026-07-02T17:56:18Z'
  faq_source_hash: 3557d534c51f81839cc353ebbd600ec588a60197d2c27c9a58e97c25017d07e4
  summary: >-
    This Learning Path shows how to build and publish multi-architecture container images targeting
    arm64 and amd64 using GitHub Actions with Arm-hosted runners. It starts by comparing build
    options—emulation with Docker buildx versus native builds coordinated through an image manifest—so
    you can select an approach that fits project complexity. Learners configure Arm-hosted runners
    for public or private repositories, choose between standard and larger runner types, and create
    a workflow that runs on Arm hardware. The path then covers creating a repository, adding secrets
    for Docker Hub, and triggering the workflow to produce and push images. On completion, learners
    can run a build and see the resulting multi-architecture image published to Docker Hub.
  faqs:
  - question: Which build option should I use for multi-architecture images?
    answer: >-
      Use emulation with Docker buildx for simplicity, but expect slower performance for complex
      builds. For faster native builds, create images per architecture and publish a manifest
      that references them.
  - question: Can I use Arm-hosted runners in public and private repositories?
    answer: >-
      Yes. Arm-hosted runners are available for public repositories on the free plan, subject
      to standard usage limits. For private repositories, a Team or Enterprise Cloud plan is required.
  - question: 'Which GitHub-hosted runner type should I choose: standard or larger?'
    answer: >-
      Use standard runners for general workloads. Choose larger runners if you need to control
      RAM, CPU, and disk space, or if you require options such as a static IP address or runner
      groups.
  - question: What secrets do I need to push images to Docker Hub?
    answer: >-
      Add repository secrets that provide Docker Hub credentials as referenced by the workflow
      file. Make sure the secret names match the workflow and that the job logs show successful
      authentication before the push steps.
  - question: How do I verify the result is a multi-architecture image on Docker Hub?
    answer: >-
      After the workflow completes, check the image in Docker Hub and inspect the manifest to
      confirm entries for arm64 and amd64. If only one architecture is listed, review the workflow
      steps that build and publish each architecture.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: CI-CD
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - GitHub
    - Docker
    - Runbook
### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - embedded-and-microcontrollers

further_reading:
    - resource:
        title: Linux arm64 hosted runners now available for free in public repositories
        link: https://github.blog/changelog/2025-01-16-linux-arm64-hosted-runners-now-available-for-free-in-public-repositories-public-preview/
        type: documentation
    - resource:
        title: Using GitHub-hosted runners
        link: https://docs.github.com/en/actions/using-github-hosted-runners
        type: documentation
    - resource:
        title: Arm64 on GitHub Actions Powering faster, more efficient build systems
        link: https://github.blog/2024-06-03-arm64-on-github-actions-powering-faster-more-efficient-build-systems/
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

