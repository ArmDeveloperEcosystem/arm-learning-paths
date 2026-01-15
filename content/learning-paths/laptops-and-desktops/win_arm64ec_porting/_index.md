---
title: Port Applications to Arm64 using Arm64EC

minutes_to_complete: 90

who_is_this_for: This is an introductory topic for developers who want to learn how to port their applications to Arm64 using Arm64EC. 

learning_objectives:
    - Build a Qt-based Python desktop application
    - Create C/C++ dependencies and use them in the Qt-based Python app
    - Learn how to port the C/C++ based dependencies to Arm64 using Arm64EC

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13s running Windows 11 or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).
    - Any code editor. [Visual Studio Code for Arm64](https://code.visualstudio.com/docs/?dv=win32arm64user) is suitable.
    - Visual Studio 2022 with Arm build tools. [Refer to this guide for the installation steps](https://developer.arm.com/documentation/102528/0100/Install-Visual-Studio).
    
author: Dawid Borycki

### Tags
skilllevels: Introductory
subjects: Migration to Arm
armips:
    - Cortex-A
operatingsystems:
    - Windows
tools_software_languages:
    - C
    - CPP
    - Qt    

further_reading:
    - resource:
        title: Arm64EC - Build and port apps for native performance on Arm
        link: https://learn.microsoft.com/en-us/windows/arm/arm64ec
        type: documentation
    - resource:
        title: Visual Studio on Arm-powered devices
        link: https://learn.microsoft.com/en-us/visualstudio/install/visual-studio-on-arm-devices?view=vs-2022
        type: documentation
    - resource:
        title: Load x64 Plug-ins (like VSTs) from your Arm Code using Arm64EC
        link: https://devblogs.microsoft.com/windows-music-dev/load-x64-plug-ins-like-vsts-from-your-arm-code-using-arm64ec/
        type: blog    


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
