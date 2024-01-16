---
title: Memory Tagging Extension on Google Pixel 8

minutes_to_complete: 10

who_is_this_for: This is an introductory topic for developers interested in learning how to enable Arm's Memory Tagging Extension (MTE) on Google's Pixel 8 smartphone and also how to access a memory bug report.

learning_objectives: 
    - Enable MTE on your Google Pixel 8 smartphone
    - Understand how MTE works and learn how to make an application crash when it encounters a memory bug
    - Access the memory bug report
    - Interpret the memory bug report

prerequisites:
    - A Google Pixel 8 smartphone
    - A USB cable to connect your Google Pixel 8 to your desktop machine
    - Android Debug Bridge (adb) installed on your device. Follow the steps in https://developer.android.com/tools/adb to install Android SDK Platform Tools. The adb tool is included in this package.

author_primary: Roberto Lopez Mendez

### Tags
skilllevels: Introductory
subjects: Performance and Architecture
armips:
    - Cortex-A
tools_software_languages:
    - Memory Bug Report
operatingsystems:
    - Android


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
