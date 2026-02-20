---
title: Run memcached on Arm servers and measure its performance

minutes_to_complete: 10

who_is_this_for: This is an introductory topic for developers who want to use memcached as their in-memory key-value store.


learning_objectives:
- Install and run memcached on your Arm-based cloud server
- Use an open-source benchmark to test memcached performance

prerequisites:
- An Arm based instance from an appropriate cloud service provider.

author: Pareena Verma

test_images:
- ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-learning-paths/actions/runs/4312122327
test_maintenance: true

### Tags
skilllevels: Introductory
subjects: Web
cloud_service_providers:
  - AWS
  - Oracle
armips:
- Neoverse
operatingsystems:
- Linux
tools_software_languages:
- Runbook
- Memcached

further_reading:
    - resource:
        title: Memcached Wiki
        link: https://github.com/memcached/memcached/wiki
        type: documentation
    - resource:
        title: Benchmarking memcached performance on AWS Graviton2 servers
        link: https://developer.arm.com/community/arm-community-blogs/b/servers-and-cloud-computing-blog/posts/accelerating-deep-packet-inspection-with-neon-on-arm-neoverse
        type: blog


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
