---
title: Convert uvprojx-based projects to csolution

minutes_to_complete: 10

who_is_this_for: This is a topic for users of µVision who want to migrate to the new project format (csolution) required by CMSIS-Toolbox.

learning_objectives: 
    - Import, convert, and build uvprojx-based projects in Keil Studio.
    - Convert uvprojx-based projects in µVision.
    - Convert and build uvprojx-based projects on the command line.

prerequisites:
    - Install [Keil Studio](/install-guides/keilstudio_vs/) on your machine.
    - Install [µVision](/install-guides/mdk/) on your machine.
    - Install [uv2csolution](https://arm-software.github.io/MDK-Toolbox/01_installation/) for the command line flow.
    - The &micro;Vision project must use Arm Compiler 6 as the default toolchain. Arm Compiler 5 is not supported.

author: Christopher Seidl

### Tags
skilllevels: Intermediate
subjects: Performance and Architecture
armips:
    - Cortex-M
tools_software_languages:
    - Keil MDK
    - CMSIS-Toolbox
operatingsystems:
    - Windows
    - Linux
    - macOS



further_reading:
    - resource:
        title: Keil Studio User's Guide
        link: https://developer.arm.com/documentation/108029/latest/
        type: documentation
    - resource:
        title: Introducing Keil MDK Version 6
        link: https://community.arm.com/arm-community-blogs/b/internet-of-things-blog/posts/keil-mdk-version-6
        type: blog
    - resource:
        title: keil.arm.com 
        link: https://keil.arm.com
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
