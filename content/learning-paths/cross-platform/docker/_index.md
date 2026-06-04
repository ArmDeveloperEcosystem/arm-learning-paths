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

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T21:34:19Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 058f779bc7dd9faef294a57f4524bf525046d757e21a287744825fb9b290935e
  summary_generated_at: '2026-06-01T21:03:24Z'
  summary_source_hash: 058f779bc7dd9faef294a57f4524bf525046d757e21a287744825fb9b290935e
  faq_generated_at: '2026-06-02T21:34:19Z'
  faq_source_hash: 058f779bc7dd9faef294a57f4524bf525046d757e21a287744825fb9b290935e
  summary: >-
    Follow this introductory path to build, run, and share Docker images that support both Arm
    and x86. You will validate your Docker setup, perform multi-architecture builds with Docker
    buildx, and use a remote Arm Linux server over SSH to offload Arm image builds when local
    emulation is slow. The path also covers creating multi-architecture images using Docker manifest
    (an experimental feature not recommended for production) and checking image architecture support
    in container registries. You can use a Windows, macOS, or Linux computer with Docker installed,
    plus access to an Arm Linux server with Docker. By the end, you will have practiced building
    and publishing images that run on Arm-based systems.
  faqs:
  - question: What do I need before running the steps?
    answer: >-
      Use a Windows, macOS, or Linux computer with Docker installed. For remote builds, you also
      need an Arm Linux server with Docker installed and reachable over SSH without a password.
  - question: How do I verify my Docker setup before starting builds?
    answer: >-
      Run docker run hello-world to confirm Docker is working. Then run docker buildx --help and
      expect a usage message beginning with 'Usage: docker buildx [OPTIONS] COMMAND'; if you see
      other output, install the most recent Docker version.
  - question: When should I use a remote Arm server for builds?
    answer: >-
      If building Arm images on a non-Arm machine is slow due to emulation, switch to a remote
      Arm server. Use docker context to target an Arm machine that has Docker installed and is
      accessible via passwordless SSH.
  - question: When should I use docker manifest in this workflow?
    answer: >-
      Use docker manifest when you have built separate images for each architecture and want to
      publish a single multi-architecture image. Note that docker manifest is an experimental
      feature and is not recommended for production use.
  - question: How do I check that an image is multi-architecture and supports Arm?
    answer: >-
      Inspect the image in your container registry. For example, Docker Hub shows supported OS/ARCH
      entries, and AWS ECR Public also lists the architectures.
# END generated_summary_faq

author: Jason Andrews

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

