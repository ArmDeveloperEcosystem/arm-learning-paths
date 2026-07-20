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
  generated_at: '2026-07-02T19:35:34Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3557d534c51f81839cc353ebbd600ec588a60197d2c27c9a58e97c25017d07e4
  summary_generated_at: '2026-07-02T19:35:34Z'
  summary_source_hash: 3557d534c51f81839cc353ebbd600ec588a60197d2c27c9a58e97c25017d07e4
  faq_generated_at: '2026-07-02T19:35:34Z'
  faq_source_hash: 3557d534c51f81839cc353ebbd600ec588a60197d2c27c9a58e97c25017d07e4
  summary: >-
    You'll build and publish multi-architecture container images with
    GitHub Actions using Arm-hosted runners. You'll compare common build options, including emulation
    and native builds assembled with a manifest, then run workflows on Arm-managed arm64 runners
    for public or private repositories. You'll create a repository, configure secrets for Docker
    Hub, and define a workflow that builds images for arm64 alongside amd64, then pushes a multi-architecture
    image. You'll also review available runner types for private repositories. After triggering
    a workflow and verifying that Docker Hub lists a manifest with arm64 and amd64 platforms, you'll confirm
    that the build and publication steps completed as intended.
  faqs:
  - question: How do I know the job ran on an Arm-hosted runner?
    answer: >-
      Check the Actions run details for the runner name or labels that indicate an Arm architecture
      and confirm the workflow selects the Arm-hosted runner. If the run shows a different runner,
      review the `runs-on` setting in the workflow.
  - question: I’m using a private repository and can’t select an Arm-hosted runner—what should
      I check?
    answer: >-
      Confirm the account uses a Team or Enterprise Cloud plan because private repositories
      require it for Arm-hosted runners. If it still doesn’t appear, review the repository or
      organization runner settings.
  - question: Which build approach does this path use for multiple architectures?
    answer: >-
      The path explains emulation and manifest-based builds, then uses Arm-hosted runners to perform
      native arm64 builds and assemble a multi-architecture image. The workflow relies on native Arm execution
      rather than instruction emulation for the arm64 build.
  - question: Where do I store credentials so the workflow can push images to Docker Hub?
    answer: >-
      Add the required registry credentials as repository secrets and reference them in the
      workflow. Without these secrets, the push step fails to authenticate.
  - question: What result should I expect after the workflow completes?
    answer: >-
      Expect a successful Actions run and a new image tag on Docker Hub with a multi-architecture
      manifest listing arm64 and amd64. If the platforms are missing, review the build logs
      to see which architecture jobs ran and which images were pushed.
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
