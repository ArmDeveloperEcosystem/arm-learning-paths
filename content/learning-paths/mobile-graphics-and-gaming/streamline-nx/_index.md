---
title: Get Started with profiling Arm Neural Technology workloads with Streamline

draft: true
cascade:
    draft: true

description: Profile your Android ML for Vulkan workload with the Arm Streamline GUI, then inspect NX activity, GPU timeline events, and graph-operation costs.

minutes_to_complete: 45

who_is_this_for: This Learning Path is for Android and graphics developers who want to profile their ML for Vulkan applications on the Mali Neural Accelerator using the Arm Streamline GUI.

learning_objectives:
    - Explain how neural accelerator (NX), Vulkan ML workloads, and GPU shader execution relate to a Streamline capture.
    - Prepare your debuggable Android workload for Streamline capture.
    - Collect and open a 30-second workload capture using the Streamline GUI.
    - Inspect NX activity and graph operations using Mali Timeline and Dispatch Graph Workloads.

prerequisites:
    - Your own debuggable Android app, already installed on the device, with a supported ML for Vulkan workload
    - An Android 11 or later device with NX-capable Mali G2 or later hardware, Mali DDK r56p0 or later, and USB debugging access
    - Basic familiarity with Android applications, Vulkan, and terminal commands
    - A Windows, macOS, or supported Linux host for Arm Performance Studio and Android SDK Platform Tools
    - A USB data cable to connect the Android device to your host or wireless debugging enabled

author:
    - Kieran Hejmadi
    - Amarbold Batzorig

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: true

# Optional one-shot controls: set either field to true to regenerate just that
# generated section the next time the summary/FAQ tool runs. The tool resets
# them to false after a successful write.
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: Graphics
armips:
    - Mali
tools_software_languages:
    - Arm Performance Studio
    - Streamline
    - Vulkan
    - NX
operatingsystems:
    - Android

further_reading:
    - resource:
        title: Arm Streamline 9.9 User Guide
        link: https://support.arm.com/documentation/101816/9-9
        type: documentation
    - resource:
        title: Install Arm Streamline
        link: /install-guides/streamline/
        type: documentation
    - resource:
        title: Install Arm Performance Studio
        link: /install-guides/ams/
        type: documentation
    - resource:
        title: Arm Neural Technology Playbook - Evaluate
        link: /learning-paths/mobile-graphics-and-gaming/neural-graphics-playbook-evaluate/
        type: learningpath
    - resource:
        title: Analyze Neural Frame Rate Upscaling using Project Moku
        link: /learning-paths/mobile-graphics-and-gaming/nfru-cases-study/
        type: learningpath
    - resource:
        title: Vulkan physical device driver properties
        link: https://docs.vulkan.org/refpages/latest/refpages/source/VkPhysicalDeviceDriverProperties.html
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
