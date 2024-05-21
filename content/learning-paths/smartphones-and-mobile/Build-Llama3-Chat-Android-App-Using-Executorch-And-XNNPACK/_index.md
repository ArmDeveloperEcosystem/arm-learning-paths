---
title: Build LLaMA Android chat app with ExecuTorch and XNNPACK 

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers interested in learning how to build LLaMA Android chat app with ExecuTorch.

learning_objectives: 
    - Setup ExecuTorch development environment
    - Understand how ExecuTorch uses XNNPACK kernels to accelerate performance on Arm based platorms
    - Understand how 4-bit groupwise PTQ quantization reduces model size without significantly sacrificing model accuracy
    - Build and run various LLaMA models using ExecuTorch on host machine
    - Build and run an Android Chat app with different LLaMA models using ExecuTorch on Arm based smartphone
    

prerequisites:
    - Apple M1/M2 development machine with Android Studio installed or a Linux machine with atleast 16GB of RAM
    - A 64-bit Arm powered smartphone running Android with 16GB of RAM
    - A USB cable to connect your smartphone to your development machine
    - Android Debug Bridge (adb) installed on your device. Follow the steps in [adb](https://developer.android.com/tools/adb)  to install Android SDK Platform Tools. The adb tool is included in this package.
    - Java 17 JDK. Follow the steps in [Java 17 JDK](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) to download and install JDK for host.
    - Python 3.10.

author_primary: Varun Chari

### Tags
skilllevels: Introductory
subjects: ML/AI
armips:
    - Cortex
tools_software_languages:
    - Mobile
    - Java
    - C++
    - Python
operatingsystems:
    - MacOS
    - Android


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
