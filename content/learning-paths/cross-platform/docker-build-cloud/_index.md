---
title: Build multi-architecture container images with Docker Build Cloud

description: Learn how to build multi-architecture Docker images for Arm and x86 using Docker Build Cloud, with GitHub Actions automation for faster builds without emulation.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers who want to learn how to use Docker Build Cloud.

learning_objectives:
    - Build Arm images and multi-architecture images with Docker Build Cloud
    - Use GitHub Actions to automate image builds

prerequisites:
    - A computer with Docker installed. This can be Windows, macOS, or Linux. Any architecture can be used. 
    - A GitHub account
    - A Docker Hub account

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-02T19:21:37Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9a94219b689b8e22a175c6067c6bb6d139d6ad22f3aac77c78b6b38970d5a5eb
  summary_generated_at: '2026-07-02T19:21:37Z'
  summary_source_hash: 9a94219b689b8e22a175c6067c6bb6d139d6ad22f3aac77c78b6b38970d5a5eb
  faq_generated_at: '2026-07-02T19:21:37Z'
  faq_source_hash: 9a94219b689b8e22a175c6067c6bb6d139d6ad22f3aac77c78b6b38970d5a5eb
  summary: >-
    You'll build multi-architecture container images for Arm and x86
    using Docker Build Cloud and then automate those builds with GitHub Actions. You'll compare
    common approaches for multi-architecture builds and configure Docker Build Cloud as the builder
    to avoid relying on instruction emulation. Then, you'll create a GitHub repository,
    add a workflow that targets multiple architectures, and set required secrets so the workflow
    can run unattended. You'll trigger a cloud-backed build and see logs that confirm
    Arm and x86 variants were produced through the configured pipeline.
  faqs:
  - question: Which option should I use to build multi-architecture images without relying on
      emulation?
    answer: >-
      Use Docker Build Cloud as the builder. Emulation can be slow, so
      you'll configure cloud-backed builds instead.
  - question: How do I know the image actually targets both Arm and x86?
    answer: >-
      Check the build or workflow logs for the listed target platforms and verify the image manifest
      with Docker tooling. You should see entries for both Arm and x86.
  - question: What should I check if the GitHub Actions workflow fails due to missing credentials?
    answer: >-
      Confirm that all required secrets are added in the repository settings and that the workflow
      references them by the correct names. Update the secret names or values to match the workflow.
  - question: Do I need to create a new GitHub repository for this workflow?
    answer: >-
      The steps use a new repository to get started, but you can use an existing one. Ensure the
      workflow file and required secrets are added to whichever repository you choose.
  - question: How can I confirm the workflow used Docker Build Cloud instead of local emulation?
    answer: >-
      Review the workflow configuration and logs to see that the selected builder is Docker Build
      Cloud. Ensure the builder is set before the build step runs.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Docker

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
    - embedded-and-microcontrollers

further_reading:
    - resource:
        title: Docker Build Cloud
        link: https://docs.docker.com/build/cloud/
        type: documentation
    - resource:
        title: Introducing Docker Build Cloud - A New Solution to Speed Up Build Times and Improve Developer Productivity
        link: https://www.docker.com/blog/introducing-docker-build-cloud/
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
