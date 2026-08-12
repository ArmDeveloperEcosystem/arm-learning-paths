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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-12T20:04:05Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 34fd1ff3ec46b494a04dfb3e842ed4258153fabbed658eba77db0e3aeea3a25f
  summary_generated_at: '2026-08-12T20:04:05Z'
  summary_source_hash: 34fd1ff3ec46b494a04dfb3e842ed4258153fabbed658eba77db0e3aeea3a25f
  faq_generated_at: '2026-08-12T20:04:05Z'
  faq_source_hash: 34fd1ff3ec46b494a04dfb3e842ed4258153fabbed658eba77db0e3aeea3a25f
  summary: >-
    You'll create a containerized Arm embedded development environment with Docker. You'll prepare
    an Ubuntu-based Dockerfile containing Arm Compiler for Embedded and Fixed Virtual Platforms,
    then build the image and verify that the tools launch. You'll finish with a reusable environment
    for compiling Arm applications and running targets on FVPs without installing tools directly
    on the host.
  faqs:
  - question: Which base operating system should the Dockerfile use?
    answer: >-
      Use Ubuntu as the base for the Docker image, as specified in the instructions. The host can be
      Windows or a different Linux distribution.
  - question: Do I need to use sudo for Docker commands on Linux?
    answer: >-
      Many Linux setups require `sudo` because the Docker daemon runs as root. If you see a permission
      error, prepend `sudo` to the Docker command.
  - question: What files do I need to copy into the image before building?
    answer: >-
      Copy the installation packages you downloaded for Arm Compiler for Embedded and the Fixed
      Virtual Platforms (FVPs). Make sure the Dockerfile `COPY` paths match where those files are
      located.
  - question: How do I know the image is ready to use?
    answer: >-
      Start a container from the image and run the compiler and FVP executables. Confirm each
      executable launches and reports version information. If both start without errors, your environment is
      set up correctly.
  - question: Can I follow these steps on a Windows host?
    answer: >-
      Yes. The container runs Ubuntu, and the host can be Windows or Linux. Install the appropriate
      Docker edition for your platform before starting.
# END generated_summary_faq

author: Ronan Synnott

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
