---
title: Measure performance of compression libraries on Arm servers

minutes_to_complete: 10

who_is_this_for: This is an introductory topic for software developers using compression
  libraries on Arm servers.


learning_objectives:
- Install and run lzbench with snappy and zstd
- Measure compression library performance running on 64-bit Arm AWS EC2 instance

prerequisites:
- An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from an appropriate
  cloud service provider.

author: Pareena Verma

test_images:
- ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-learning-paths/actions/runs/4312122327
test_maintenance: true

### Tags
skilllevels: Introductory
subjects: Libraries
cloud_service_providers:
  - AWS
  - Oracle
armips:
- Neoverse
operatingsystems:
- Linux
tools_software_languages:
- snappy
- Runbook

further_reading:
    - resource:
        title: Lzbench source
        link: https://github.com/inikep/lzbench
        type: documentation
    - resource:
        title: Comparing data compression algorithm performance on Arm servers
        link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/comparing-data-compression-algorithm-performance-on-aws-graviton2-342166113
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
