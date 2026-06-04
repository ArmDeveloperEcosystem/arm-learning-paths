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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:38:44Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3557d534c51f81839cc353ebbd600ec588a60197d2c27c9a58e97c25017d07e4
  summary_generated_at: '2026-06-01T21:06:27Z'
  summary_source_hash: 3557d534c51f81839cc353ebbd600ec588a60197d2c27c9a58e97c25017d07e4
  faq_generated_at: '2026-06-02T21:38:44Z'
  faq_source_hash: 3557d534c51f81839cc353ebbd600ec588a60197d2c27c9a58e97c25017d07e4
  summary: >-
    Learn to build and publish multi-architecture container images for arm64 and amd64 using GitHub
    Actions with Arm-hosted runners. This introductory path walks you through creating a repository,
    defining a workflow that runs on Arm-hosted runners, and configuring the secrets needed to
    automate deployment to Docker Hub. It also explains common build approaches for multi-architecture
    images, including instruction emulation and using a manifest across multiple machines, noting
    the performance drawback of emulation for complex builds. By the end, you will be able to
    build Arm images and multi-architecture images with GitHub Actions. A Linux environment, a
    GitHub account (Team or Enterprise Cloud for private repositories), and a Docker Hub account
    are required. Estimated time: 30 minutes.
  faqs:
  - question: What do I need before running the workflow?
    answer: >-
      You need a GitHub account and a Docker Hub account. For private repositories, a GitHub Team
      or Enterprise Cloud plan is required. No other explicit prerequisites are listed.
  - question: Do I need to provision my own machines to run Arm jobs?
    answer: >-
      No. Arm-hosted runners are managed by GitHub, so you do not need to provide a server. They
      are available for public and private repositories, with public repos on free plans subject
      to standard usage limits.
  - question: Which approach should I use to build multi-architecture images?
    answer: >-
      You can use instruction emulation or a manifest with multiple computers. Emulation is straightforward
      but can be slow for complex builds, while the manifest approach builds natively on each
      architecture. This Learning Path uses GitHub Actions with Arm-hosted runners as part of
      a multi-architecture workflow.
  - question: Can I use Arm-hosted runners in private repositories, and what runner types exist?
    answer: >-
      Yes, you can use them in private repositories with a Team or Enterprise Cloud plan. GitHub-hosted
      runners include standard and larger runners; larger runners let you adjust RAM, CPU count,
      and disk space, and offer options like a static IP and runner groups.
  - question: How do I run the workflow and publish images to Docker Hub?
    answer: >-
      Create a new GitHub repository, add a GitHub Actions workflow that targets Arm-hosted runners,
      and configure the repository secrets required by the workflow. The process builds images
      for arm64 and amd64 and automates deployment to Docker Hub.
# END generated_summary_faq

author: Jason Andrews

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

