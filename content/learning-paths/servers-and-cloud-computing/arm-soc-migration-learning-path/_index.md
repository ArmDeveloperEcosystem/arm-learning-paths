---
title: Migrate applications between Arm platforms with AI assistance

draft: true
cascade:
    draft: true
    
minutes_to_complete: 60

who_is_this_for: This is an advanced topic for developers migrating applications between Arm platforms using AI-assisted tooling with Kiro's Arm SoC Migration Power. You will learn a practical, repeatable migration workflow through an example that moves an application from the cloud to the edge — from AWS Graviton (Neoverse-based) to Raspberry Pi 5 (Cortex-A based).

learning_objectives:
    - Install and configure Kiro's Arm SoC Migration Power
    - Understand a structured migration workflow applicable across Arm platforms
    - Use AI-guided migration to identify platform-specific and hardware-dependent code
    - Create Hardware Abstraction Layers with Power assistance
    - Validate and verify migrations with automated analysis

prerequisites:
    - Access to a source and target Arm platforms (the example uses AWS Graviton3 and Raspberry Pi 5)
    - Basic understanding of C programming
    - Familiarity with embedded systems, Linux environments, or cloud computing concepts

author: Daniel Schleicher

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
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
        title: Kiro ARM SoC Migration Power Documentation
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
---
