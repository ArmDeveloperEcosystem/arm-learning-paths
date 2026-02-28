---
title: Accelerate Bitmap Scanning with NEON and SVE Instructions on Arm servers

minutes_to_complete: 20

who_is_this_for: This is an introductory topic for database developers, performance engineers, and anyone interested in optimizing data processing workloads on Arm-based cloud instances.


learning_objectives:
  - Understand bitmap scanning operations in database systems
  - Implement bitmap scanning with scalar, NEON, and SVE instructions
  - Compare performance between different implementations
  - Measure performance improvements on Graviton4 instances

prerequisites:
- An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from an appropriate
  cloud service provider.

author: Pareena Verma


### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
  - Oracle
armips:
- Neoverse
operatingsystems:
- Linux
tools_software_languages:
- SVE
- NEON
- Runbook

further_reading:
    - resource:
        title: Accelerate multi-token search in strings with SVE2 SVMATCH instruction
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/multi-token-search-strings-svmatch-instruction
        type: blog
    - resource:
        title: Arm SVE2 Programming Guide
        link: https://developer.arm.com/documentation/102340/latest/
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
