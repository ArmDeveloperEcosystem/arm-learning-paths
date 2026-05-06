---
title: Migrate applications between Arm platforms using Kiro Arm SoC Migration Power
description: Learn how to migrate C applications between Arm platforms using Kiro's AI-assisted tooling to identify hardware dependencies and implement abstraction layers for cross-platform compatibility.

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for experienced developers who need to migrate applications between Arm-based platforms using AI-assisted tooling. You will work through a structured, repeatable migration workflow using Kiro Arm SoC Migration Power, moving an application from AWS Graviton3 (Neoverse) to Raspberry Pi 5 (Cortex-A). The techniques apply broadly to cloud-to-edge and cross-architecture migrations across the Arm ecosystem.

learning_objectives:
   - Install and configure Kiro Arm SoC Migration Power
   - Apply a structured migration workflow across Arm platforms
   - Identify platform-specific and hardware-dependent code using AI-guided analysis
   - Implement hardware abstraction layers to isolate platform-specific dependencies
   - Validate and verify the migrated application using automated analysis

prerequisites:
    - Access to both source and target Arm platforms (for example, AWS Graviton3 and Raspberry Pi 5)
    - Working knowledge of C programming
    - Familiarity with Linux development environments and basic embedded or cloud deployment concepts
    - Experience building applications with GCC and CMake

generate_summary_faq: true

# rerun_summary: false
# rerun_faqs: false
# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v1
  generated_at: '2026-05-06T17:17:56Z'
  generator: template
  source_hash: 49b3f2b1464efb20f0c8fbcff46e9f30910d856567ca01c01dc348aa1c5740d1
  summary: >-
    Learn how to migrate C applications between Arm platforms using Kiro's AI-assisted tooling
    to identify hardware dependencies and implement abstraction layers for cross-platform compatibility.
    It is designed for experienced developers who need to migrate applications between Arm-based
    platforms using AI-assisted tooling. You will work through a structured, repeatable migration
    workflow using Kiro Arm SoC Migration Power, moving an application from AWS Graviton3 (Neoverse)
    to Raspberry Pi 5 (Cortex-A). The techniques apply broadly to cloud-to-edge and cross-architecture
    migrations across the Arm ecosystem. By the end, you will be able to install and configure
    Kiro Arm SoC Migration Power, apply a structured migration workflow across Arm platforms,
    and identify platform-specific and hardware-dependent code using AI-guided analysis. It focuses
    on tools and technologies such as Kiro, AWS EC2, GCC, C, and CMake, Linux environments, Arm
    platforms including Neoverse and Cortex-A, and cloud platforms such as AWS, Microsoft Azure,
    Google Cloud, and Oracle. The main steps cover Install Arm SoC Migration Power, Develop on
    source platform, Migrate using Arm SoC Migration Power, and Validate migration with testing.
  faqs:
  - question: What will you accomplish in this Learning Path?
    answer: >-
      You will install and configure Kiro Arm SoC Migration Power, apply a structured migration
      workflow across Arm platforms, and identify platform-specific and hardware-dependent code
      using AI-guided analysis. Learn how to migrate C applications between Arm platforms using
      Kiro's AI-assisted tooling to identify hardware dependencies and implement abstraction layers
      for cross-platform compatibility.
  - question: Who is this Learning Path for?
    answer: >-
      This is an advanced topic for experienced developers who need to migrate applications between
      Arm-based platforms using AI-assisted tooling. You will work through a structured, repeatable
      migration workflow using Kiro Arm SoC Migration Power, moving an application from AWS Graviton3
      (Neoverse) to Raspberry Pi 5 (Cortex-A). The techniques apply broadly to cloud-to-edge and
      cross-architecture migrations across the Arm ecosystem.
  - question: What do you need before you start?
    answer: >-
      Before you start, make sure you have the following: Access to both source and target Arm
      platforms (for example, AWS Graviton3 and Raspberry Pi 5); Working knowledge of C programming;
      Familiarity with Linux development environments and basic embedded or cloud deployment concepts;
      Experience building applications with GCC and CMake.
  - question: Which tools, languages, or platforms does it cover?
    answer: >-
      It covers tools and languages including Kiro, AWS EC2, GCC, C, and CMake, Linux environments,
      Arm platforms such as Neoverse and Cortex-A, and cloud platforms such as AWS, Microsoft
      Azure, Google Cloud, and Oracle.
  - question: How is the Learning Path structured?
    answer: >-
      The Learning Path is organized around Install Arm SoC Migration Power, Develop on source
      platform, Migrate using Arm SoC Migration Power, and Validate migration with testing.
# END generated_summary_faq

author: Daniel Schleicher

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
    - Neoverse
    - Cortex-A
operatingsystems:
    - Linux
tools_software_languages:
    - Kiro
    - AWS EC2
    - GCC
    - C
    - CMake

further_reading:
    - resource:
        title: Kiro Arm SoC Migration Power Documentation
        link: https://kiro.dev/powers/arm-soc-migration
        type: documentation
    - resource:
        title: AWS Graviton Technical Guide
        link: https://aws.amazon.com/ec2/graviton/
        type: documentation
    - resource:
        title: Raspberry Pi 5 Documentation
        link: https://www.raspberrypi.com/documentation/
        type: documentation
    - resource:
        title: Arm Architecture Reference
        link: https://developer.arm.com/documentation
        type: documentation
    - resource:
        title: BCM2712 Peripherals Datasheet
        link: https://datasheets.raspberrypi.com/bcm2712/bcm2712-peripherals.pdf
        type: documentation

### FIXED, DO NOT MODIFY
weight: 1
layout: learningpathall
learning_path_main_page: "yes"
---

