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

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:19:04Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 49b3f2b1464efb20f0c8fbcff46e9f30910d856567ca01c01dc348aa1c5740d1
  summary_generated_at: '2026-06-02T03:06:57Z'
  summary_source_hash: 49b3f2b1464efb20f0c8fbcff46e9f30910d856567ca01c01dc348aa1c5740d1
  faq_generated_at: '2026-06-03T00:19:04Z'
  faq_source_hash: 49b3f2b1464efb20f0c8fbcff46e9f30910d856567ca01c01dc348aa1c5740d1
  summary: >-
    This advanced Learning Path shows how to migrate a C application between Arm platforms using
    Kiro Arm SoC Migration Power. You install Kiro IDE on your local machine, enable the Migration
    Power, and use an Arm MCP server deployed as a Docker-based backend for Arm-specific guidance.
    You build and validate a sensor-monitor application on an AWS Graviton3 source platform, then
    follow an AI-guided workflow—discovery, architecture analysis, abstraction design, and platform-specific
    implementation—to target a Raspberry Pi 5. Finally, you validate on both platforms using testing
    recommendations for functional correctness, platform compatibility, hardware interaction,
    and performance comparison. Prerequisites include access to both platforms, C experience,
    Linux familiarity, and the ability to build with GCC and CMake. Estimated time is 60 minutes.
  faqs:
  - question: What do I need before running the migration workflow?
    answer: >-
      You need access to both source and target Arm platforms (for example, AWS Graviton3 and
      Raspberry Pi 5), working knowledge of C, familiarity with Linux development, and experience
      with GCC and CMake. Basic embedded or cloud deployment concepts are also assumed.
  - question: How do I set up Kiro and the required backend services?
    answer: >-
      Install Kiro IDE on your local machine, enable Kiro Arm SoC Migration Power, and run the
      Arm MCP server as a containerized backend using Docker. You also provision an AWS Graviton3
      instance to serve as the source platform for the example.
  - question: Which application and platforms are used in the example?
    answer: >-
      The example uses a sensor-monitor application. The migration demonstrates moving from AWS
      Graviton3 (Neoverse) to Raspberry Pi 5 (Cortex-A76), though the workflow applies to other
      Arm-to-Arm scenarios.
  - question: How do I know the analysis phase is working during migration?
    answer: >-
      The Migration Power highlights platform-specific and hardware-dependent code and guides
      abstraction boundaries. Use these findings to design and implement a hardware abstraction
      layer before adding platform-specific implementations.
  - question: What should I check to confirm the migration is successful?
    answer: >-
      Use the Power’s testing recommendations on both source and target platforms to verify functional
      correctness, confirm platform compatibility, validate hardware interaction, and compare
      performance characteristics. Migration is complete when these checks pass on both environments.
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

