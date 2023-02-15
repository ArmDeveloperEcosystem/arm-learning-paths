---
title: Run x265 (H.265 codec) on Arm servers

description: Learn how to build and run x265 on Arm servers.

minutes_to_complete: 10

who_is_this_for: This is an introductory topic for software developers who want to build and run an x265 codec on Arm servers and measure performance.

learning_objectives:
    - Build x265 codec on Arm server
    - Run x265 codec on Arm server with the same video of various resolutions and encoding presets to measure the performance impact

prerequisites:
    - An [Arm based instance](/learning-paths/server-and-cloud/csp/) from an appropriate cloud service provider.

author_primary: Pareena Verma

### Tags
skilllevels: Introductory
subjects: Libraries
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - x265


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
