---
armips:
- Neoverse
- Cortex-A
author_primary: Jason Andrews
description: Learn how to port architecture-specific intrinsics to Arm processors.
layout: learningpathall
learning_objectives:
- Describe what intrinsics are and how to find them in code.
- Evaluate options and use header-only libraries to port architecture-specific intrinsics
  to Arm.
learning_path_main_page: 'yes'
minutes_to_complete: 30
operatingsystems:
- Linux
prerequisites:
- Some understanding of SIMD concepts.
- An Arm based machine or [cloud instance](/learning-paths/servers-and-cloud-computing/csp/) running Ubuntu Linux.
- Optionally, an `x86_64` machine also running Ubuntu.
skilllevels: Advanced
subjects: Performance and Architecture
test_images:
- amd64/ubuntu:latest
- arm64v8/ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-learning-paths/actions/runs/4312122327
test_maintenance: true
test_status:
- passed
- passed
title: Porting architecture specific intrinsics
tools_software_languages:
  - Neon
  - SVE
  - Coding
  - Intrinsics

weight: 1
who_is_this_for: This is an advanced topic for software developers interested in porting
  architecture specific intrinsics to Arm processors.

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops
---
