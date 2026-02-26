---
title: Migrate applications between Arm platforms using Kiro Arm SoC Migration Power
    
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
