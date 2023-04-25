---
# User change
title: "Porting methodology" 

weight: 2 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# Methodology

## List application requirements and configuration

Before migrating to Arm, it is important to understand the original platform environment to build, run and develop the application.

- What OS does the application run on?
- Does the application run in a virtual machine or a software container?
- What is the application's source langage?
- Does the application use any intrinsics or assembly code?
- Is the application built natively or cross-compiled?
- What are the application's system dependencies? Does the application use external libraries?
- How is the application built (e.g. configuration) and which tools are used (e.g. compilers)?
- Does the application benefit from hardware acceleration (e.g. Nvidia GPU)?

These questions help draw a picture of the migration process to identify:

- the target platform configuration (e.g. hardware acceleration, OS, system dependencies),
- development tools (e.g. compilers),
- application requirements and configuration (e.g. compiler flags, third-party libraries that may need porting as well).

## Replicate setup

To minimize compatibility issues between software versions and facilitate the migration, it is important to replicate the same setup as much as possible.

To illustrate this, we are going to port [this edge detection application](https://github.com/m3y54m/sobel-simd-opencv.git) on an embedded Linux aarch64 system.

This application runs several implementations of the same algorithm:
- a pure C version
- a version with intrinsics to enable SIMD processing
- an OpenCV version

We have summarized our example's dependencies and configuration below:
 
* Build type: Native
* Source code: C++
* OS: Ubuntu 22.04

| | | Available in aarch64 system repository? |
| -- | -- | -- |
| Compiler | GNU GCC | [Yes](https://packages.ubuntu.com/jammy/g++) |
| External libraries | OpenCV | [Yes](https://packages.ubuntu.com/jammy/libopencv-dev) |
| Build toolchain | Cmake | [Yes](https://packages.ubuntu.com/jammy/cmake) |

We will describe how to set up our x86_64 and aarch64 systems in the next section. At this point, we foresee that building the application on aarch64 should not be a problem as the toolchain is available.

## Identify non-portable settings

Inspecting the building options and the source code of the application provides useful information. Look out for:
- assembly code - which will need to be rewritten,
- instrinsics - which can be ported with minimal changes using for example [SIMD Everywhere (SIMDe)](https://github.com/simd-everywhere/simde),
- build options - which may be architecture-specific.

Let's illustrate this with our example, in `src/main.cpp`:
- The header file `x86intrin.h` won't be available when building natively on aarch64.
- The function `SobelSimd` uses x86_64 intrinsics (prefixed with `_mm_`).

In `src/CMakeLists.txt`:

```cmake
# Enable SIMD instructions for Intel Intrinsics
# https://software.intel.com/sites/landingpage/IntrinsicsGuide/
if(NOT WIN32)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -mavx")
endif()
```
  
The flag `-mavx` used with GCC is architecture-specific, only available on [x86_64](https://man7.org/linux/man-pages/man1/gcc.1.html). This will prevent building the application entirely, even if the pure C version `SobelNonSimd` and the OpenCV version `SobelOpenCV` of the Sobel filter are portable.
