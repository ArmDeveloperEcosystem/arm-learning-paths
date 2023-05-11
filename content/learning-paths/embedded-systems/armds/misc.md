---
# User change
title: Other compilers and project types

weight: 4 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Use a different compiler version than the default

Development Studio installs with the latest [Arm Compiler for Embedded](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded) version available at the time of its release. It may be that you need to use a specific compiler version for your project (particularly common if the [Arm Compiler for Embedded FuSa](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Embedded%20FuSa) is needed).

Refer to the [Arm Compiler for Embedded install guide](/install-guides/armclang/) to learn how to install different versions of the compiler.

To change the compiler version used for a project, right-click on the project, and select `Properties` (or from the menu, select `Project > Properties`), then `C/C++ Build > Tool Chain Editor`, and select the appropriate compiler version from the `Current toolchain` pulldown. Click `Apply and Close`, and rebuild the project.

## Import an example CMSIS project

[CMSIS](https://developer.arm.com/tools-and-software/embedded/cmsis) is a vendor-independent abstraction layer for microcontrollers that are based on Arm Cortex processors.

Cortex-M users can import projects from the library of CMSIS Packs. It is generally recommended to use [Keil MDK](https://www2.keil.com/mdk5) for such projects, which has more robust support for such packs.

For more information, see the Development Studio [documentation](https://developer.arm.com/documentation/101469/latest/Migrating-from-DS-5-to-Arm-Development-Studio/CMSIS-Packs).
