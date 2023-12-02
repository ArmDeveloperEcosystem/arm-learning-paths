---
title: Porting Your Applications to Arm64 Using Arm64EC

minutes_to_complete: 90

who_is_this_for: This learning path is for developers, who want to learn how to port their solutions to Arm64 using Arm64EC. In this learning path you will build a Qt-based Python application with C/C++-based DLL dependencies. This architecture mimics a typical scenario of using Python and Qt for rapid UI prototyping and DLLs for computation-intense work. 

learning_objectives:
    - Build a Qt-based Python desktop application
    - Create C/C++ dependencies and use them in the Qt-based Python app
    - Learn how to gradually port the C/C++ to Arm64 using Arm64EC.

prerequisites:
    - A Windows on Arm computer such as [Windows Dev Kit 2023](https://learn.microsoft.com/en-us/windows/arm/dev-kit), Lenovo Thinkpad X13s running Windows 11 or Windows on Arm[virtual machine](/learning-paths/cross-platform/woa_azure/).
    - Any code editor, we recommend using [Visual Studio Code for Arm64](https://code.visualstudio.com/docs/?dv=win32arm64user).
    - Visual Studio 2022 with Arm build tools. [Refer to this guide for the installation steps](https://developer.arm.com/documentation/102528/0100/Install-Visual-Studio).
    
author_primary: Dawid Borycki

### Tags
skilllevels: Introductory
subjects: Migration to Arm
armips:
    - Cortex-A
operatingsystems:
    - Windows
tools_software_languages:
    - C/C++
    - Qt    

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
