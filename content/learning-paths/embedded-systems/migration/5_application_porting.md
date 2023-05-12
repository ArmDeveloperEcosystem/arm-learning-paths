---
# User change
title: "Application porting" 

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# Application porting

Based on the porting analysis you can start making changes to the source code and build options. This might be an iterative process. If the compilation fails, you can make modifications and then compile again.

The steps below assume that you are running all commands inside the `aarch64` GCC development container.

## Sobel filter

Start by cloning the Sobel filter repository.
```bash
git clone https://github.com/m3y54m/sobel-simd-opencv.git
cd sobel-simd-opencv
```

## x86 intrinsics porting

To port the AVX intrinsics, you can use SIMD Everywhere ([SIMDe](https://github.com/simd-everywhere/simde)). By using SIMDe you can keep the AVX intrinsics in the source code and the intrinsics will be replaced by NEON instructions. 

Start by cloning the SIMDe repository:

```bash
git clone https://github.com/simd-everywhere/simde.git
```

Here are the changes required in `CMakeLists.txt`:

```output
# Add SIMDe options
include_directories(../simde)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
```

Run the command below to make the changes: 

```bash
sed -i "28i # Add SIMDe options\ninclude_directories(../simde)\nset(CMAKE_CXX_STANDARD 14)\nset(CMAKE_CXX_STANDARD_REQUIRED ON)\nset(CMAKE_CXX_EXTENSIONS OFF)\n" src/CMakeLists.txt
```

Finally, you need to include SIMDe AVX headers in `main.cpp` like this:

```output
#define SIMDE_ENABLE_NATIVE_ALIASES
#ifdef __aarch64__
#include "simde/x86/avx.h"
#else
#warning AVX support is not available. Code will not compile
#endif
```

The changes can be made by running: 

```bash
sed -i "40i #define SIMDE_ENABLE_NATIVE_ALIASES\n#ifdef __aarch64__\n#include \"simde/x86/avx.h\"\n#else\n#warning AVX support is not available. Code will not compile\n#endif" src/main.cpp
```

## Compiler options porting

The `-mavx` compiler option needs to be removed. You can add the optimization flag `-O2` as it's recommended [when transitioning to Arm](https://simd-everywhere.github.io/blog/2020/06/22/transitioning-to-arm-with-simde.html). 

Below you can see the changes to make in `CMakeLists.txt`:

```output
# Enable SIMD instructions for Intel Intrinsics
# https://software.intel.com/sites/landingpage/IntrinsicsGuide/
if(NOT WIN32)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -O2")
endif()
```

Make the changes by running the following command:

```bash
sed -i "s/-mavx/-O2/g" src/CMakeLists.txt
```

{{% notice Note %}}
Compiler options should be tuned and optimized to achieve higher performance, but you can keep it simple for now as performance optimization comes at a later phase of the project.
{{% /notice %}}

Application porting is now complete. Go to the next section to compile and run the ported application.