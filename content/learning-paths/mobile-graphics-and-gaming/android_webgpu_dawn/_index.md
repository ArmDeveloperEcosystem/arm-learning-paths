---
title: Build and profile a simple WebGPU Android Application
cascade:
minutes_to_complete: 90

who_is_this_for: This is an introductory topic for developers who are building GPU-based Android applications and are interested in experimenting with WebGPU. 

learning_objectives: 
    - Describe the benefits of WebGPU.
    - Describe the benefits of using Dawn.
    - Set up a WebGPU development environment.
    - Integrate Dawn in an Android Application.
    - Use Dawn WebGPU APIs in the application.
    - Describe the changes required to upgrade to WebGPU to render a simple 3D object.
    - Build and run a WebGPU Android Application.
    - Profile the application using Streamline.
    - Analyze the profiling data.
       
prerequisites:
    - Basic knowledge of graphics APIs and experience in developing Android graphics applications.
    - A development machine with Android Studio, Blender, and Arm Streamline installed.
    - An Android phone in developer mode.
    - Android Studio.
    - Arm Performance Studio.
    - Python 3.10 or later.

author:
    - Varun Chari
    - Albin Bernhardsson

### Tags
skilllevels: Advanced
subjects: Graphics
armips:
    - Cortex-A
tools_software_languages:
    - Java
    - Kotlin
    - CPP
    - Python
operatingsystems:
    - macOS
    - Linux
    - Windows
    - Android


further_reading:
    - resource:
        title: WebGPU example application
        link: https://github.com/varunchariArm/Android_DawnWebGPU
        type: website
    - resource:
        title: WebGPU working draft
        link: https://www.w3.org/TR/webgpu/
        type: website
    - resource:
        title: Dawn Github repository
        link: https://github.com/google/dawn
        type: website
    - resource:
        title: WebGPU API
        link: https://developer.mozilla.org/en-US/docs/Web/API/WebGPU_API
        type: website
    - resource:
        title: WebGPU fundamentals 2
        link: https://webgpufundamentals.org/
        type: website
    - resource:
        title: Learn WebGPU 
        link: https://eliemichel.github.io/LearnWebGPU/index.html
        type: website
    - resource:
        title: WebGPU examples 2
        link: https://github.com/samdauwe/webgpu-native-examples
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
