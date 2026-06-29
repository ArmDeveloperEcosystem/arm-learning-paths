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

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-26T17:29:03Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 49b3f2b1464efb20f0c8fbcff46e9f30910d856567ca01c01dc348aa1c5740d1
  summary_generated_at: '2026-06-26T17:29:03Z'
  summary_source_hash: 49b3f2b1464efb20f0c8fbcff46e9f30910d856567ca01c01dc348aa1c5740d1
  faq_generated_at: '2026-06-26T17:29:03Z'
  faq_source_hash: 49b3f2b1464efb20f0c8fbcff46e9f30910d856567ca01c01dc348aa1c5740d1
  summary: >-
    You'll migrate a C application between Arm platforms using Kiro's Arm
    SoC Migration Power. First, you'll install Kiro, enable the Migration Power, and run the Arm MCP server
    as a containerized backend. Then, you'll build and validate the `sensor-monitor` application on an
    AWS Graviton3 source instance. The workflow proceeds through discovery, architecture analysis,
    abstraction design, and platform-specific implementation to separate hardware-dependent code
    behind a clear interface. You'll then build the migrated code for the target, such as Raspberry
    Pi 5, and validate it using the Power's testing recommendations to check functional behavior,
    platform compatibility, hardware interactions, and performance characteristics against the
    baseline.
  faqs:
  - question: Where should Kiro and the Arm MCP server run during setup?
    answer: >-
      Kiro runs locally on your development machine. The Migration Power uses the Arm MCP server
      deployed as a containerized backend using Docker, started as described in the setup step
      so Kiro can connect to it.
  - question: Where do I open and build the `sensor-monitor` application before migrating?
    answer: >-
      Open and inspect the project locally in Kiro, then build and validate it on the AWS Graviton3
      source instance. A successful baseline build and run on Graviton3 provides the reference
      behavior for migration.
  - question: How do I know the discovery phase has identified hardware-dependent code?
    answer: >-
      Use the Migration Power’s AI-guided analysis to review findings for platform-specific or
      hardware-dependent code paths. The analysis highlights areas to isolate behind an abstraction
      before porting.
  - question: What should the hardware abstraction layer include for this migration?
    answer: >-
      Define clear interfaces for hardware interactions and move platform-specific logic behind
      those interfaces. Provide target-specific implementations and use the existing build system
      to select the appropriate implementation per platform.
  - question: What results indicate the migration is validated on both platforms?
    answer: >-
      Both source and target builds should complete without platform-specific errors, and the
      application should pass functional checks and hardware interaction tests. Use the Power’s
      testing recommendations to confirm platform compatibility and compare performance characteristics
      against the source baseline.
# END generated_summary_faq

author: Daniel Schleicher

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

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
