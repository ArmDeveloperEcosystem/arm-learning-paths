---
# User change
title: "Porting analysis" 

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# Porting analysis 

A Sobel filter implementation is used as the example application as it is an applicable embedded computer vision workload. The [Sobel SIMD OpenCV repo](https://github.com/m3y54m/sobel-simd-opencv/) is implemented in three different ways which makes it a great example candidate to show different aspects of porting. 

It is implemented in the following ways:
* Non-SIMD
  * pure C++ code
* SIMD 
  * `x86_64` intrinsics
* OpenCV
  * a computer vision library

The application builds and runs on an `x86_64` machine. The application runs on CPU only (no hardware acceleration). 

You will follow the porting methodology and gather information about the application.

|                      |                       | version          |
| -------------------- | --------------------- | ---------------- |
| Programming language | C++                   |                  |
| OS                   | Ubuntu                | 22.04 LTS        |
| Compiler             | GCC                   | 11.3.0           |
| Build tools          | CMake                 | 3.22.1           |
| External libraries   | OpenCV                | 4.5.4            |

This table is the starting point for the porting analysis.

Using the original software and tool versions when porting an application isn't a requirement, however it is recommended as it will make the porting smoother. By looking at the Sobel filter code and with the questions from the previous section in mind, you can start the porting analysis.

In [src/CMakeLists.txt#L12](https://github.com/m3y54m/sobel-simd-opencv/blob/master/src/CMakeLists.txt#L12):
```output
# Enable SIMD instructions for Intel Intrinsics
# https://software.intel.com/sites/landingpage/IntrinsicsGuide/
if(NOT WIN32)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -mavx")
endif()
```
  
The flag `-mavx` used with GCC is architecture-specific. It is only available on [x86_64](https://man7.org/linux/man-pages/man1/gcc.1.html) and will prevent the application from compiling. Even though the application won't compile, no changes to the source code for the non-SIMD and OpenCV implementations are necessary.

In [src/main.cpp#L26](https://github.com/m3y54m/sobel-simd-opencv/blob/master/src/main.cpp#L26):
```output
/* GCC-compatible compiler, targeting x86/x86-64 */
#include <x86intrin.h>
```

The header file `x86intrin.h` isn't supported on `aarch64`.

In [src/main.cpp#L253](https://github.com/m3y54m/sobel-simd-opencv/blob/master/src/main.cpp#L253):
```output
p1 = _mm_loadu_si128((__m128i *)(inputPointer + i * width + j));
p2 = _mm_loadu_si128((__m128i *)(inputPointer + i * width + j + 1));
p3 = _mm_loadu_si128((__m128i *)(inputPointer + i * width + j + 2));
```

The lines of code above is just a snippet from the function `SobelSimd` which has intrinsics prefixed with `_mm_`. These aren't supported on `aarch64` and will need to be ported for the application to compile on `aarch64`.

The table below summarizes the migration analysis.
| | version | available on Arm | Comment |
| --- | --- | --- | --- |
| Ubuntu                | 22.04 LTS        | Yes | [Ubuntu for Arm](https://ubuntu.com/download/server/arm) |
| GCC                   | 11.3.0           | Yes | |
| CMake                 | 3.22.1           | Yes | |
| OpenCV                | 4.5.4            | Yes | |
| Compiler option -mavx | N/A              | No  | x86-specific |
| AVX intrinsics        | N/A              | No  | x86-specific |

You can draw the following conclusions:
* The compiler options need to be modified
  * see [aarch64 options](https://gcc.gnu.org/onlinedocs/gcc/AArch64-Options.html) for compatible compiler options
* The AVX intrinsics need to ported to utilize Arm SIMD intrinsics
  * Arm has three SIMD technologies
    * [NEON](https://developer.arm.com/documentation/den0018/a)
    * Scalable Vector Extension ([SVE](https://developer.arm.com/documentation/102131/0100/?lang=en))
    * Scalable Vector Extension version 2 ([SVE2](https://developer.arm.com/documentation/102340/0100/Introducing-SVE2?lang=en))