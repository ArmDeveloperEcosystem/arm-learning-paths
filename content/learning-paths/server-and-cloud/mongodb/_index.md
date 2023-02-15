---
title: Learn about MongoDB on Arm servers

description: Learn how to install and run MongoDB Community Edition on differet flavors of AWS EC2 instances powered by Arm64 achitecture

minutes_to_complete: 30   

who_is_this_for: This is an introductory topic for software developers using MongoDB as their database for mobile, IoT applications, content management, or real-time analytics on Arm servers.

learning_objectives: 
    - Install and run MongoDB on your 64-bit Arm AWS EC2 instance
    - Test MongoDB performance on your 64-bit Arm AWS EC2 instance using open-source tooling
    - Measure and compare the performance of MongoDB on Arm versus other architectures with Yahoo Cloud Serving Benchmark (YCSB)

prerequisites:
    - An [Arm based instance](/learning-paths/server-and-cloud/csp/) from an appropriate cloud service provider.

author_primary: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Databases
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - MongoDB
    - AWS EC2
    - cbuild
    - GCC
    - Snort

### Test
test_maintenance: true
test_images:
- mongo:latest
test_link: null
test_status:
- passed


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
