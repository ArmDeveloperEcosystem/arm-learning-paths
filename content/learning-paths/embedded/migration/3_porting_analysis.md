---
# User change
title: "Porting analysis" 

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# Porting analysis 

A Sobel filter implementation was selected as the example application to port as it is an applicable embedded computer vision workload. The [Sobel SIMD OpenCV repo](https://github.com/m3y54m/sobel-simd-opencv/) is implemented in three different ways which makes it a great example candidate to show different aspects of porting. It is implemented in the following ways:
* Non-SIMD
  * pure C++ code
* SIMD 
  * `x86_64` intrinsics
* OpenCV
  * a computer vision library

The application is built on an `x86_64` machine and runs on CPU only, i.e., no hardware acceleration. Find additional details in the table below.

| OS | Compiler | Build tools | Programming language | Intrinsics | External libraries |
| --- | --- | --- | --- | --- | --- |
| Ubuntu 22.04.2 LTS | GCC 11.3.0 | CMake 3.22.1 | C++14 | AVX | OpenCV 4.5.4 |

These bullets and table act as the starting point for the porting analysis.

Using the original software and tool versions when porting an application isn't a requirement, however it is recommended as it will make the porting smoother. By looking at the [Sobel SIMD OpenCV repo](https://github.com/m3y54m/sobel-simd-opencv/) and with the questions from the previous section in mind start the analysis.

In `src/CMakeLists.txt`:
```output
# Enable SIMD instructions for Intel Intrinsics
# https://software.intel.com/sites/landingpage/IntrinsicsGuide/
if(NOT WIN32)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -mavx")
endif()
```
  
The flag `-mavx` used with GCC is architecture-specific. It is only available on [x86_64](https://man7.org/linux/man-pages/man1/gcc.1.html) and will prevent the application from compiling entirely. Even though the application won't compile, no changes to the source code for the non-SIMD and OpenCV implementations will be necessary.

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
| | `aarch64` compatible? | `aarch64` version | Comment |
| --- | --- | --- | --- |
| Ubuntu           | Yes | 22.04 LTS        | [Ubuntu for Arm](https://ubuntu.com/download/server/arm) |
| GCC              | Yes | 11.3.0 or 12.2.0 | GCC is the standard compiler for Ubuntu |
| CMake            | Yes | 3.22.1           | |
| Compiler options | No  | N/A              | needs to be modifed |
| C++              | Yes | 14               | |
| AVX              | No  | N/A              | intrinsics are architecture specific |
| OpenCV           | Yes | 4.5.4            | |

The following conclusions can be drawn:
* the compiler options need to be modified
  * see [aarch64 options](https://gcc.gnu.org/onlinedocs/gcc/AArch64-Options.html) for compatible compiler options
* the AVX intrinsics need to ported to utilize Arm SIMD intrinsics
  * Arm has three SIMD technologies
    * [NEON](https://developer.arm.com/documentation/den0018/a)
    * Scalable Vector Extension ([SVE](https://developer.arm.com/documentation/102131/0100/?lang=en))
    * Scalable Vector Extension version 2 ([SVE2](https://developer.arm.com/documentation/102340/0100/Introducing-SVE2?lang=en))