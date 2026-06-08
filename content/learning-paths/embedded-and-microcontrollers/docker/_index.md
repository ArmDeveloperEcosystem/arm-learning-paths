---
title: Prepare Docker image for Arm embedded development

description: Learn how to create a Dockerfile, build a Docker image with Arm Compiler for Embedded and Fixed Virtual Platforms, and test the containerized Arm development environment.

minutes_to_complete: 30   

who_is_this_for: This is an introductory topic for embedded software developers new to Docker.

learning_objectives: 
    - Create and understand a Dockerfile
    - Build Docker image
    - Test the image

prerequisites:

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:19:02Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: a4b522c46c68d3c6f5c4af7c76b00c7bde48bb638147c201376bc19a4de79cca
  summary_generated_at: '2026-06-01T21:39:09Z'
  summary_source_hash: a4b522c46c68d3c6f5c4af7c76b00c7bde48bb638147c201376bc19a4de79cca
  faq_generated_at: '2026-06-02T22:19:02Z'
  faq_source_hash: a4b522c46c68d3c6f5c4af7c76b00c7bde48bb638147c201376bc19a4de79cca
  summary: >-
    Build a containerized Arm embedded development environment by creating a Dockerfile, constructing
    an Ubuntu-based Docker image that includes Arm Compiler for Embedded and a library of Fixed
    Virtual Platforms (FVPs), and testing the image. This introductory path is aimed at embedded
    software developers new to Docker and focuses on a basic build-and-run setup for bare-metal
    development. The host machine can be Windows or Linux, and Linux users may need sudo for Docker
    commands. Before starting, install Docker for your host and download the installation packages
    you will copy into the image. By the end, you will have a tested Docker image suitable for
    running compiler and FVP tasks.
  faqs:
  - question: What do I need before running docker build?
    answer: >-
      Install Docker for your host platform and download the installation packages for Arm Compiler
      for Embedded and the Fixed Virtual Platforms you plan to include. These files are copied
      into the image during the build.
  - question: Which host operating systems can I use to follow this path?
    answer: >-
      You can use Windows or Linux as the host. On Linux, you may need to prefix Docker commands
      with sudo because the Docker daemon runs as root.
  - question: What base operating system does the container use?
    answer: >-
      The Docker image uses Ubuntu as the operating system inside the container.
  - question: What will the resulting Docker image contain?
    answer: >-
      It will contain Arm Compiler for Embedded and a library of Fixed Virtual Platforms (FVPs).
      This provides a basic build and run environment for Arm embedded development.
  - question: How do I know the image works after the build?
    answer: >-
      The steps include testing the containerized environment. You should be able to run the container
      and exercise the compiler and FVPs without errors.
# END generated_summary_faq

author: Ronan Synnott

### Tags
skilllevels: Introductory
subjects: Containers and Virtualization
armips:
    - Cortex-A
    - Cortex-R
    - Cortex-M
    - Neoverse
operatingsystems:
    - Baremetal
tools_software_languages:
    - Docker
    - Arm Development Studio
    - Arm Compiler for Embedded
    - Arm Fast Models


further_reading:
    - resource:
        title: Docker documentation
        link: https://docs.docker.com
        type: documentation
    - resource:
        title: Learn how to use Docker
        link: /learning-paths/cross-platform/docker/
        type: website


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

