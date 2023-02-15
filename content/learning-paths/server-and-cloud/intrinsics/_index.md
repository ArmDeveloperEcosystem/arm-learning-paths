---
title: Porting Architecture Specific Intrinsics

description: Learn how to port architecture intrinsics to Arm Neoverse processors.

minutes_to_complete: 20

who_is_this_for: This is an advanced topic for software developers interested in porting architecture specific intrinics to Arm Neoverse processors.

learning_objectives:
    - Understand what intrinsics are and how to find them in code
    - Evaluate options and use header-only libraries to port architecture specific intrinics to Arm Neoverse

prerequisites:
    - An [Arm based instance](/learning-paths/server-and-cloud/csp/) from an appropriate cloud service provider.

author_primary: Jason Andrews

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:

### Test
test_images:
- amd64/ubuntu:latest
- arm64v8/ubuntu:latest
test_link: null
test_maintenance: true
test_status:
- passed
- passed

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
