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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-02T17:57:09Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a6ad703d9d894da06ed4aa3725fcc9006d70050cef3f0a3ef9a758bcf4523289
  summary_generated_at: '2026-07-02T17:57:09Z'
  summary_source_hash: a6ad703d9d894da06ed4aa3725fcc9006d70050cef3f0a3ef9a758bcf4523289
  faq_generated_at: '2026-07-02T17:57:09Z'
  faq_source_hash: a6ad703d9d894da06ed4aa3725fcc9006d70050cef3f0a3ef9a758bcf4523289
  summary: >-
    This Learning Path shows how to build a GitLab CI/CD workflow that targets GitLab-hosted Arm64
    runners. You create a GitLab project, add a .gitlab-ci.yml that selects the Arm64 runner tag,
    build and containerize a small C application, and push the image to the GitLab Container Registry.
    You then run the pipeline from the GitLab UI, inspect job logs, and verify the execution environment
    with lscpu to confirm Arm64. The result is a repeatable pipeline that builds and stores Arm64
    container images using managed runners, so you can focus on your code and configuration rather
    than maintaining runner infrastructure.
  faqs:
  - question: Do I need to install or manage runners for this workflow?
    answer: >-
      No. GitLab-hosted runners are available for any project without additional setup, including
      Arm64 runners.
  - question: How do I confirm that my job executed on Arm64?
    answer: >-
      Open the job log and check the lscpu output. The reported architecture confirms the job
      ran on an Arm64 environment.
  - question: Where should I place the CI/CD configuration?
    answer: >-
      Add a .gitlab-ci.yml file at the root of your project. This file defines stages and selects
      the Arm64 runner tag.
  - question: What should I check if the pipeline does not start or stays pending?
    answer: >-
      Verify that .gitlab-ci.yml is committed to the repository and that jobs reference the Arm64
      runner tag. Then re-run the pipeline from Build > Pipelines.
  - question: Where is the container image stored after the build?
    answer: >-
      The image is pushed to the GitLab Container Registry for your project. After the job completes,
      check the project’s registry to confirm the image is available.
# END generated_summary_faq

author: Mohamed Ismail

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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

