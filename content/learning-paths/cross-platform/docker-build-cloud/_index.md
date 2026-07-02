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
  generated_at: '2026-07-02T17:19:21Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 9a94219b689b8e22a175c6067c6bb6d139d6ad22f3aac77c78b6b38970d5a5eb
  summary_generated_at: '2026-07-02T17:19:21Z'
  summary_source_hash: 9a94219b689b8e22a175c6067c6bb6d139d6ad22f3aac77c78b6b38970d5a5eb
  faq_generated_at: '2026-07-02T17:19:21Z'
  faq_source_hash: 9a94219b689b8e22a175c6067c6bb6d139d6ad22f3aac77c78b6b38970d5a5eb
  summary: >-
    This Learning Path shows how to build Arm and x86 container images as a single multi-architecture
    image using Docker Build Cloud. It contrasts emulation with native builds on separate machines
    and guides you to use a cloud builder to avoid local emulation for complex workloads. Learners
    configure Docker Build Cloud, target multiple platforms, and produce an image manifest that
    references architecture-specific variants. The path then adds continuous integration with
    GitHub Actions, using repository secrets and a workflow that invokes Docker Build Cloud as
    the builder. After completing the steps, you can trigger a cloud build and verify that the
    published image advertises both Arm and x86.
  faqs:
  - question: Can I run the build from a non-Arm machine?
    answer: >-
      Yes. You can drive the process from any architecture because the builds run on Docker Build
      Cloud rather than through local emulation.
  - question: What result should I expect after a successful Docker Build Cloud build?
    answer: >-
      Expect a pushed image that includes a manifest referencing separate Arm and x86 variants.
      Your container registry entry should list a multi-architecture image that can be pulled
      on either architecture.
  - question: How do I verify the image is multi-architecture?
    answer: >-
      Inspect the image manifest and confirm entries for both Arm and x86. You can also pull the
      same tag on an Arm system and an x86 system to confirm the correct variant is selected on
      each.
  - question: What should I configure in GitHub before running the workflow?
    answer: >-
      Create a repository and add the required repository secrets described in the steps so the
      workflow can authenticate and push images. Then commit the workflow file that uses Docker
      Build Cloud as the builder.
  - question: How do I confirm the workflow used Docker Build Cloud instead of emulation?
    answer: >-
      Check the GitHub Actions logs for the selected builder and the platforms built. If the logs
      show Docker Build Cloud as the builder and native builds per architecture, emulation was
      not used.
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

