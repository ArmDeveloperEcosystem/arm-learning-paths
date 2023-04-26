---
# User change
title: "Application porting" 

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# Application porting

First, we'll select some suitable target platforms, which are compatible with our porting analysis, to build and run the application we wish to migrate.
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

The application porting is now complete and next we'll put it all together and run the ported application on one of our target platforms.