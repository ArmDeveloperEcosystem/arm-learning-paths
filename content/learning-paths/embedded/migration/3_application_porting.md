---
# User change
title: "Application porting" 

weight: 3 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# Application porting

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

## Analysis 

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

## Porting targets
Next, we'll select some suitable target platforms, which are compatible with our porting analysis, to build and run the application we wish to migrate.
* cross-platform (emulation)
  * requires installing [QEMU](https://www.qemu.org/) on the original `x86_64` platform
* remote hardware
  * [AWS EC2](https://aws.amazon.com/ec2/) are easily accessible
* physical hardware
  * [Raspberry Pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) is a popular off-the-shelf single-board computer

We're now at a stage where the porting work can begin.

## Compiler options porting

There might be minor differences to the changes necessary depending on what we're migrating to, however if we use `armv8-a` compiler option the application should compile and run on all the three platform targets we've selected. Compiler options should be tuned and optimized to achieve higher performance, but in this guide we'll keep it simple.

Start by cloning the Sobel filter repository.
```bash
git clone https://github.com/m3y54m/sobel-simd-opencv.git
cd sobel-simd-opencv
```

In the `CMakeLists.txt` file, the `-mavx` compiler option needs to be replaced with `armv8-a` and we're also adding the optimization flag `-O2` as it's recommended [when trasitioning to Arm](https://simd-everywhere.github.io/blog/2020/06/22/transitioning-to-arm-with-simde.html). This can be done by running the following command.
```bash
sed -i "s/-mavx/-O2\ -march=armv8-a/g" src/CMakeLists.txt
```

## x86 intrinsics porting

To port the AVX intrinsics, we'll use SIMD Everywhere ([SIMDe](https://github.com/simd-everywhere/simde)). Start by cloning the SIMDe repository.
```bash
git clone https://github.com/simd-everywhere/simde.git
```

We wish to make the following changes to `CMakeLists.txt`.
```output
# Add SIMDe options
include_directories(../simde)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
```

Which can be achieved by running the following command:
```bash
sed -i "28i # Add SIMDe options\ninclude_directories(../simde)\nset(CMAKE_CXX_STANDARD 14)\nset(CMAKE_CXX_STANDARD_REQUIRED ON)\nset(CMAKE_CXX_EXTENSIONS OFF)\n" src/CMakeLists.txt
```

And finally, we need to include SIMDe AVX headers in `main.cpp`.
```output
#define SIMDE_ENABLE_NATIVE_ALIASES
#ifdef __aarch64__
#include "simde/x86/avx.h"
#else
#warning AVX support is not available. Code will not compile
#endif
```

This can be done quickly with this command:
```bash
sed -i "40i #define SIMDE_ENABLE_NATIVE_ALIASES\n#ifdef __aarch64__\n#include \"simde/x86/avx.h\"\n#else\n#warning AVX support is not available. Code will not compile\n#endif" src/main.cpp
```

The porting of the application is now complete and next we'll create the development environment so the ported application can be compiled.