---
title: Debugging with MTE on Google Pixel 8

minutes_to_complete: 20

who_is_this_for: This is an advanced topic for developers interested in learning how to debug applications in Android Studio running on Google Pixel 8 smartphone to detect memory safety bugs with Arm Memory Tagging Extension (MTE).

learning_objectives: 
    - Know common memory safety bugs in Android space
    - Understand Android MTE Test app implementing common memory bugs
    - Build MTE Test app in Android Studio
    - Enable/Disable MTE in the Android Manifest
    - Debug MTE Test app in Android Studio on Google Pixel 8 smartphone

prerequisites:
    - A Google Pixel 8 smartphone
    - A USB cable to connect your Google Pixel 8 to your desktop machine
    - Android Debug Bridge (adb) installed on your device. Follow the steps in https://developer.android.com/tools/adb to install Android SDK Platform Tools. The adb tool is included in this package.
    - Android Studio installed in your development environment
    - Android project with MTE Test app downloaded from [this repository](https://github.com/rlopez3d/mte_debug_app).
author_primary: Roberto Lopez Mendez

### Tags
skilllevels: Advanced
subjects: Performance and Architecture
armips:
    - Cortex-A
tools_software_languages:
    - Android Studio
    - Memory Tagging Extension
operatingsystems:
    - Android


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
