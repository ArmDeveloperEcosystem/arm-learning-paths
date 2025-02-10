---
title: Porting architecture specific intrinsics

description: Learn how to port architecture-specific intrinsics to Arm processors.

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for software developers interested in porting
  architecture specific intrinsics to Arm processors.

learning_objectives:
- Describe what intrinsics are and how to find them in code.
- Evaluate options and use header-only libraries to port architecture-specific intrinsics
  to Arm.

prerequisites:
- Some understanding of SIMD concepts.
- An Arm based machine or [cloud instance](/learning-paths/servers-and-cloud-computing/csp/) running Ubuntu Linux.
- Optionally, an `x86_64` machine also running Ubuntu.

author: Jason Andrews

test_images:
- amd64/ubuntu:latest
- arm64v8/ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-learning-paths/actions/runs/4312122327
test_maintenance: true

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
- Neoverse
- Cortex-A
operatingsystems:
- Linux
tools_software_languages:
  - Neon
  - SVE
  - Coding
  - Intrinsics

further_reading:
    - resource:
        title: Port with SSE2Neon and SIMDe
        link: https://developer.arm.com/documentation/102581/0200/Port-with-SSE2Neon-and-SIMDe
        type: documentation
    - resource:
        title: Neon Programmer's Guide
        link: https://developer.arm.com/documentation/den0018
        type: documentation
    - resource:
        title: Porting SSE to Neon, Are libraries the way forward?
        link: https://community.arm.com/arm-community-blogs/b/ai-and-ml-blog/posts/porting-sse-to-neon-are-libraries-the-way-forward
        type: blog
    - resource:
        title: Porting Advisor for Graviton, AWS Online Tech Talks
        link: https://youtu.be/Ya9Co04fszI
        type: video

### Cross-platform metadata only
shared_path: true
shared_between:
    - servers-and-cloud-computing
    - laptops-and-desktops

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
