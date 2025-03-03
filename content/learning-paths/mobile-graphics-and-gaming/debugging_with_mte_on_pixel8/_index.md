---
title: Debug with MTE on Google Pixel 8

minutes_to_complete: 20

who_is_this_for: This is an advanced topic for developers interested in learning how to use the Arm Memory Tagging Extension (MTE) to detect memory safety bugs with Android Studio on a Google Pixel 8 smartphone. 

learning_objectives: 
    - Recognize common memory safety bugs in Android applications.
    - Describe how you can use an Android MTE Test app to implement common memory bugs. 
    - Build the MTE Test app in Android Studio.
    - Enable and disable MTE in the Android Manifest.
    - Debug the MTE Test app in Android Studio on a Google Pixel 8 smartphone.

prerequisites:
    - A Google Pixel 8 smartphone.
    - Android Studio installed on your development computer.
    - A USB cable to connect your computer to your Google Pixel 8.
    - Android Debug Bridge (adb) installed on your device. If needed, follow the steps in the [Android Debug Bridge](https://developer.android.com/tools/adb) documentation.

author: Roberto Lopez Mendez

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


further_reading:
    - resource:
        title: MTE User Guide for Android OS
        link: https://developer.arm.com/documentation/108035/latest/
        type: documentation
    - resource:
        title: Arm Memory Tagging Extension
        link: https://developer.android.com/ndk/guides/arm-mte
        type: website
    - resource:
        title: AArch64 TAGGED ADDRESS ABI
        link: https://www.kernel.org/doc/Documentation/arm64/tagged-address-abi.rst
        type: documentation
    - resource:
        title: Enhanced Security Through MTE
        link: https://community.arm.com/arm-community-blogs/b/architectures-and-processors-blog/posts/enhanced-security-through-mte
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
