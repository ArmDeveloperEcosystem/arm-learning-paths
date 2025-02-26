---
armips:
- Neoverse
author: Pareena Verma
layout: learningpathall
learning_objectives:
- Install and run lzbench with snappy and zstd
- Measure compression library performance running on 64-bit Arm AWS EC2 instance
learning_path_main_page: 'yes'
minutes_to_complete: 10
operatingsystems:
- Linux
prerequisites:
- An [Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from an appropriate
  cloud service provider.
skilllevels: Introductory
subjects: Libraries
test_images:
- ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-learning-paths/actions/runs/4312122327
test_maintenance: true
test_status:
- passed
title: Measure performance of compression libraries on Arm servers
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
        link: https://community.arm.com/arm-community-blogs/b/infrastructure-solutions-blog/posts/comparing-data-compression-algorithm-performance-on-aws-graviton2-342166113
        type: blog



weight: 1
who_is_this_for: This is an introductory topic for software developers using compression
  libraries on Arm servers.
---
