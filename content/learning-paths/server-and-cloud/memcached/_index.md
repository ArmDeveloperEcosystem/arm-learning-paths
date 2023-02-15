---
title: Run memcached on Arm servers and measure its performance

description: Learn how to install and measure the performance of memcached on Arm servers

minutes_to_complete: 10

who_is_this_for: This is an introductory topic for software developers who want to use memcached as their in-memory key-value store for mobile, web, gaming or e-Commerce applications.

learning_objectives:
    - Install and run memcached on your Arm-based cloud server
    - Use an open-source benchmark to test memcached performance

prerequisites:
    - An [Arm based instance](/learning-paths/server-and-cloud/csp/) from an appropriate cloud service provider.

author_primary: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Web
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - Memcached

### Test
test_images:
- ubuntu:latest
test_link: https://github.com/armflorentlebeau/arm-software-developers-ads/actions/runs/3540052189
test_maintenance: true
test_status:
- passed

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
