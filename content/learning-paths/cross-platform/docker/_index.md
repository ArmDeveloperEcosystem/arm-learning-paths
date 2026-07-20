---
title: Learn how to use Docker

description: Learn how to build, run, and share multi-architecture Docker images for Arm and x86 platforms using buildx, manifest, and remote builders.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for software developers who want to learn about Docker for the Arm architecture.

learning_objectives:
    -  Build, run, and share Docker images
    -  Perform multi-architecture builds using Docker buildx
    -  Use a remote server to build a Docker image for the Arm architecture
    -  Use Docker manifest for multi-architecture builds

prerequisites:
    - A Windows, macOS, or Linux computer with Docker installed, any architecture can be used
    - An Arm Linux server with Docker installed

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-02T19:19:58Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 058f779bc7dd9faef294a57f4524bf525046d757e21a287744825fb9b290935e
  summary_generated_at: '2026-07-02T19:19:58Z'
  summary_source_hash: 058f779bc7dd9faef294a57f4524bf525046d757e21a287744825fb9b290935e
  faq_generated_at: '2026-07-02T19:19:58Z'
  faq_source_hash: 058f779bc7dd9faef294a57f4524bf525046d757e21a287744825fb9b290935e
  summary: >-
    You'll build, run, and share Docker images that
    target Arm and x86. First, you'll confirm Docker is installed, then use `docker buildx` to
    create multi-architecture images. When emulation on a non-Arm machine is slow, you'll switch
    to a remote Arm builder over SSH using `docker context`. You'll also publish
    multi-architecture artifacts by assembling per-architecture images with the experimental
    `docker manifest` workflow. Finally, you'll verify results by inspecting architecture metadata in container
    registries. You'll understand when to choose `docker buildx` versus `docker manifest` and how
    to offload Arm builds to a remote server.
  faqs:
  - question: How do I know Docker is installed correctly before I start?
    answer: >-
      Run `docker run hello-world`. If Docker is installed, the command completes and confirms
      that the engine can run containers.
  - question: What should I see to confirm `docker buildx` is available?
    answer: >-
      Run `docker buildx --help`. You should see a usage message that begins with `Usage: docker
      buildx [OPTIONS] COMMAND`.
  - question: 'Which option should I use to create a multi-architecture image: `docker buildx` or `docker manifest`?'
    answer: >-
      Use `docker buildx` to build multi-architecture images directly. Use `docker manifest` when you prefer
      to build and test separate images per architecture first and combine them later. Note that
      `docker manifest` is experimental and not recommended for production.
  - question: What should I do if building Arm images on my non-Arm machine is slow?
    answer: >-
      Use a remote Arm server via `docker context` and SSH. Ensure Docker is installed on the remote
      Arm machine and that SSH access does not require a password.
  - question: How do I check that an image supports Arm after I push it?
    answer: >-
      Inspect the image in your container registry’s web interface. Registries such as Docker
      Hub and Amazon ECR Public list supported OS/ARCH values so you can verify arm64 is present.
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
    - Cortex-A
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
        title: Docker Documentation
        link: https://docs.docker.com
        type: documentation
    - resource:
        title: Docker buildx documentation
        link: https://docs.docker.com/engine/reference/commandline/buildx
        type: documentation
    - resource:
        title: Docker mainfest documentation
        link: https://docs.docker.com/engine/reference/commandline/manifest
        type: documentation
    - resource:
        title: Blog by Docker on buildx
        link: https://www.docker.com/blog/how-to-rapidly-build-multi-architecture-images-with-buildx
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
