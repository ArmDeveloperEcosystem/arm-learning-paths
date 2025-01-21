---
title: Build an Android chat app with Llama, KleidiAI, ExecuTorch, and XNNPACK 

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for software developers interested in learning how to build an Android chat app with Llama, KleidiAI, ExecuTorch, and XNNPACK.

learning_objectives: 
    - Set up an ExecuTorch development environment.
    - Describe how ExecuTorch uses KleidiAI kernels to accelerate performance on Arm-based platforms.
    - Describe how 4-bit groupwise PTQ quantization reduces model size without significantly sacrificing model accuracy.
    - Build and run Llama models using ExecuTorch on your development machine.
    - Build and run an Android Chat app with different Llama models using ExecuTorch on an Arm-based smartphone.
    

prerequisites:
    - An Apple M1/M2 development machine with Android Studio installed or a Linux machine with at least 16GB of RAM.
    - An Arm-powered smartphone with the i8mm feature running Android, with 16GB of RAM.
    - A USB cable to connect your smartphone to your development machine.
    - Android Debug Bridge (adb) installed on your device. Follow the steps in [adb](https://developer.android.com/tools/adb)  to install Android SDK Platform Tools. The adb tool is included in this package.
    - Java 17 JDK. Follow the steps in [Java 17 JDK](https://www.oracle.com/java/technologies/javase/jdk17-archive-downloads.html) to download and install JDK for host.
    - Python 3.10.

author_primary: Varun Chari, Pareena Verma

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
tools_software_languages:
    - Mobile
    - Java
    - C++
    - Python
operatingsystems:
    - macOS
    - Android


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
