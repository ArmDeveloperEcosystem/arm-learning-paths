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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:34:59Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9a94219b689b8e22a175c6067c6bb6d139d6ad22f3aac77c78b6b38970d5a5eb
  summary_generated_at: '2026-06-01T21:03:46Z'
  summary_source_hash: 9a94219b689b8e22a175c6067c6bb6d139d6ad22f3aac77c78b6b38970d5a5eb
  faq_generated_at: '2026-06-02T21:34:59Z'
  faq_source_hash: 9a94219b689b8e22a175c6067c6bb6d139d6ad22f3aac77c78b6b38970d5a5eb
  summary: >-
    This Learning Path shows how to build multi-architecture Docker images for Arm and x86 using
    Docker Build Cloud, and automate the process with GitHub Actions. You will set up Docker Build
    Cloud as your builder, create Arm-only and multi-architecture images, and configure a GitHub
    repository with the required secrets so builds run in the cloud without instruction emulation.
    It is an introductory, hands-on path aimed at developers who need practical steps to produce
    images for multiple CPU architectures. Prerequisites are a computer with Docker installed
    (Windows, macOS, or Linux), a GitHub account, and a Docker Hub account. Estimated time to
    complete is about 30 minutes.
  faqs:
  - question: Do I need an Arm machine to follow this path?
    answer: >-
      No. You can use any computer with Docker installed on Windows, macOS, or Linux, and build
      for Arm and x86 using Docker Build Cloud without local emulation.
  - question: What do I need before running the builds?
    answer: >-
      You need Docker installed on your computer, a GitHub account, and a Docker Hub account.
      No other prerequisites are explicitly listed.
  - question: Which method for multi-architecture builds is used here?
    answer: >-
      The path explains common methods and focuses on using Docker Build Cloud as the builder
      to avoid instruction emulation. Emulation is noted as slow for complex builds, so the cloud
      builder is used instead.
  - question: How do I set up GitHub Actions for this build?
    answer: >-
      Create a new GitHub repository, add a workflow that uses Docker Build Cloud as the builder,
      and configure the required GitHub secrets referenced by the workflow. The steps guide you
      through creating the repository and setting up secrets.
  - question: What should I check if my GitHub Actions workflow fails early?
    answer: >-
      Verify that the required secrets referenced by the workflow are defined in the repository
      settings and that you are using the correct GitHub account. If you are also building locally,
      ensure Docker is installed and running.
# END generated_summary_faq

author: Jason Andrews

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

