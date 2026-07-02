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
  generated_at: '2026-07-02T17:19:59Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 058f779bc7dd9faef294a57f4524bf525046d757e21a287744825fb9b290935e
  summary_generated_at: '2026-07-02T17:19:59Z'
  summary_source_hash: 058f779bc7dd9faef294a57f4524bf525046d757e21a287744825fb9b290935e
  faq_generated_at: '2026-07-02T17:19:59Z'
  faq_source_hash: 058f779bc7dd9faef294a57f4524bf525046d757e21a287744825fb9b290935e
  summary: >-
    This Learning Path guides learners through building, running, and sharing Docker images with
    a focus on Arm support and multi-architecture workflows. You validate a local Docker installation,
    then create and run a simple image. Next, use Docker buildx to produce images for multiple
    architectures from one build definition. When emulation is slow, configure a remote builder
    and direct builds to an Arm Linux server over SSH. The path also demonstrates assembling architecture-specific
    images into a single multi-architecture image using Docker manifest, and shows practical ways
    to verify Arm support by inspecting image metadata in common registries.
  faqs:
  - question: How do I confirm Docker is ready before building images?
    answer: >-
      Run the command docker run hello-world. You should see a confirmation message from the hello-world
      container; if not, install or start Docker and try again.
  - question: How do I check that Docker buildx is available?
    answer: >-
      Run docker buildx --help. The correct result is a usage message that begins with “Usage:
      docker buildx [OPTIONS] COMMAND”.
  - question: I did not get the expected buildx usage message. What should I do?
    answer: >-
      Install the most recent version of Docker and recheck docker buildx --help. Older versions
      may not include buildx or may not enable it by default.
  - question: Builds for Arm on my non-Arm machine are slow. What should I use instead?
    answer: >-
      Use docker context to target a remote Arm Linux server and run the build there. Ensure Docker
      is installed on the remote machine and that it is reachable over SSH without a password
      prompt.
  - question: How can I verify that an image includes Arm support after pushing it?
    answer: >-
      Inspect the image in the container registry. On Docker Hub, check the OS/ARCH list, and
      on AWS ECR Public the supported architectures are printed in the image details.
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

