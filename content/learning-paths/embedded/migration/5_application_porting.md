---
# User change
title: "Application porting" 

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# Application porting

Based on the porting analysis we can start making changes to the source code and build options. This might be an iterative process; if the compilation fails, it provides useful information, we make modifications and then compile again.

The steps below assume that you're running all commands inside the `aarch64` GCC development container.

## Sobel filter

Start by cloning the Sobel filter repository.
```bash
git clone https://github.com/m3y54m/sobel-simd-opencv.git
cd sobel-simd-opencv
```

## x86 intrinsics porting

To port the AVX intrinsics, we'll use SIMD Everywhere ([SIMDe](https://github.com/simd-everywhere/simde)). By using SIMDe we can keep the AVX intrinsics in the source code as the intrinsics will be interpreted to NEON instructions. Start by cloning the SIMDe repository.
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

Which can be achieved by running the command below.
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

This can be done quickly with the command beneath.
```bash
sed -i "40i #define SIMDE_ENABLE_NATIVE_ALIASES\n#ifdef __aarch64__\n#include \"simde/x86/avx.h\"\n#else\n#warning AVX support is not available. Code will not compile\n#endif" src/main.cpp
```

## Compiler options porting

In the `CMakeLists.txt` file, the `-mavx` compiler option needs to be replaced with `armv8-a`. By using the `armv8-a` compiler option the application compiles on all `aarch64` hardware. We're also adding the optimization flag `-O2` as it's recommended [when trasitioning to Arm](https://simd-everywhere.github.io/blog/2020/06/22/transitioning-to-arm-with-simde.html).
```output
# Enable SIMD instructions for Intel Intrinsics
# https://software.intel.com/sites/landingpage/IntrinsicsGuide/
if(NOT WIN32)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O2 march=armv8-a")
endif()
```

 This can be done by running the following command.
```bash
sed -i "s/-mavx/-O2\ -march=armv8-a/g" src/CMakeLists.txt
```

Note: compiler options should be tuned and optimized to achieve higher performance, but in this guide we'll keep it simple as performance optimization comes at a later phase

The application porting is now complete and next we'll compile and run the ported application!