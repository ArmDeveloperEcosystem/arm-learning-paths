---
title: Access remote computers with remote.it

description: a developers guide

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for software developers who want to use remote.it to access computers providing services such as SSH and VNC.

learning_objectives:
    - Install the target device software and create proxy connections
    - Understand and install desktop, mobile, and CLI software packages
    - Create peer to peer connections 
    - Automate tasks with the command line interface (CLI)

prerequisites:
    - A Windows, macOS, or Linux desktop or laptop computer 
    - A second computer running Linux and sharing services such as SSH and VNC

author_primary: Jason Andrews

### Tags
skilllevels: Introductory
subjects: CI-CD
armips:
    - Neoverse
    - Cortex-A
operatingsystems:
    - Linux
    - Windows
    - macOS
tools_software_languages:
    - remote.it
    - SSH
    - VNC

### Test
test_images:
- ubuntu:latest
test_maintenance: false

### Cross-platform metadata only
shared_path: true
shared_between:
    - server-and-cloud
    - desktop-and-laptop
    - embedded

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
