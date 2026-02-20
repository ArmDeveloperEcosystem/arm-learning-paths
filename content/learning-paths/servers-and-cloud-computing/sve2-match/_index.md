---
title: Accelerate search performance with SVE2 MATCH on Arm servers

    
minutes_to_complete: 20

who_is_this_for: This is an introductory topic for database developers, performance engineers, and anyone optimizing data processing workloads on Arm-based cloud instances.


learning_objectives:
  - Understand the purpose and function of SVE2 MATCH instructions.
  - Implement a search algorithm using both scalar and SVE2-based MATCH approaches.
  - Benchmark and compare performance between scalar and vectorized implementations.
  - Analyze speedups and efficiency gains on Arm Neoverse-based instances with SVE2.

prerequisites:
- Access to an [AWS Graviton4, Google Axion, or Azure Cobalt 100 virtual machine](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider.

author: Pareena Verma


### Tags
skilllevels: Introductory
subjects: Performance and Architecture
cloud_service_providers:
  - AWS
  - Microsoft Azure
  - Google Cloud
armips:
- Neoverse
operatingsystems:
- Linux
tools_software_languages:
- SVE2
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
