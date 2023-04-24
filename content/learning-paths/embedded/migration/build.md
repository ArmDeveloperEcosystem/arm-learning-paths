---
# User change
title: "Native build" 

weight: 5 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

## Launch Docker container instance

To visualize the result, we need to set up X11 before building and pass some extra arguments when launching the Docker container:

```bash
sudo apt install -y x11-xserver-utils
xhost +local:*
docker run --rm -ti --net=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v $HOME/.Xauthority:/home/ubuntu/.Xauthority sobel_example
```

In the container:

```bash
sudo chown ubuntu:ubuntu ~/.Xauthority
```

## Build on aarch64



## Clone repository

```bash
git clone https://github.com/m3y54m/sobel-simd-opencv.git
cd sobel-simd-opencv
```

## Fix building options

If we try to build the application now, the compiler will report an issue with `-mavx` not being recognized on aarch64. This flags enables AVX SIMD instructions on x86_64 processors.

To fix this, let edit the `Makefile` to replace this flag with compiler options for Neoverse N1 processors on AVA and Graviton2:
```bash
sed -i "s/-mavx/-O2\ -march=armv8.2-a+fp16+rcpc+dotprod+crypto/g" src/CMakeLists.txt
```

## Enable NEON intrinsics

At this point, we would be able to build the pure C and OpenCV version of the algorithm but we fail to build the whole application because of SIMD AVX instrinsics.

Fortunately, we can enable NEON SIMD support on aarch64 without rewriting the application using [SIMD Everywhere](/learning-paths/server-and-cloud/intrinsics/simde):

```bash
git clone https://github.com/simd-everywhere/simde.git
```

We need to edit `src/CMakeLists.txt` to add the following:

```
# Add SIMDe options
include_directories(../simde)
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
set(CMAKE_CXX_EXTENSIONS OFF)
```

And `main.cpp` to include the SIMD Everywhere AVX headers:

```C
#define SIMDE_ENABLE_NATIVE_ALIASES
#ifdef __aarch64__
#include "simde/x86/avx.h"
#else
#warning AVX support is not available. Code will not compile
#endif
```

This can be done quickly with these two commands:

```bash
sed -i "28i # Add SIMDe options\ninclude_directories(../simde)\nset(CMAKE_CXX_STANDARD 14)\nset(CMAKE_CXX_STANDARD_REQUIRED ON)\nset(CMAKE_CXX_EXTENSIONS OFF)\n" src/CMakeLists.txt
sed -i "40i #define SIMDE_ENABLE_NATIVE_ALIASES\n#ifdef __aarch64__\n#include \"simde/x86/avx.h\"\n#else\n#warning AVX support is not available. Code will not compile\n#endif" src/main.cpp
```

## GCC

We are now able to build and run the application:

```bash
cmake -S src -B build
cd build/
make
./sobel_simd_opencv
```

## ACfL

If you are using the `armswdev/arm-compiler-for-linux` you can swich compiler to build the application. To do so, you need to edit `src/CMakeLists.txt` to add the following:

```
set(CMAKE_C_COMPILER "/opt/arm/arm-linux-compiler-23.04_Generic-AArch64_Ubuntu-22.04_aarch64-linux/bin/armclang")
set(CMAKE_CXX_COMPILER "/opt/arm/arm-linux-compiler-23.04_Generic-AArch64_Ubuntu-22.04_aarch64-linux/bin/armclang++")
```

This can be done quickly with these two commands:

```bash
$ sed -i "6i set(CMAKE_C_COMPILER\ \"/opt/arm/arm-linux-compiler-23.04_Ubuntu-22.04/bin/armclang\")" src/CMakeLists.txt
$ sed -i "7i set(CMAKE_CXX_COMPILER\ \"/opt/arm/arm-linux-compiler-23.04_Ubuntu-22.04/bin/armclang++\")\n" src/CMakeLists.txt
```

Then, rebuild the example with the same commands:

```bash
cmake -S src -B build
cd build/
make
./sobel_simd_opencv
```


## Summary

In this example we have illustrated key aspects of application porting:
- Start by building the application on the original architecture, investigate the system environment and check how the application is built. List all application dependencies.
- Try to replicate the original environment as much as possible on the target architecture.
- Plan what need work to complete the migration. Look out for non-portable compiler flags, architecture-specific intrinsics and third-party libraries.
  - As a general rule, always prefer using libraries instead of custom implementations. The porting work may have been done already!
- Perform the first stage of the migration with a similar setup than on the original architecture.
- Finally, iteratively update third-party libraries and tools to take advantage of the latest features of the target processor.

| Version | G++ 12.2.0 | ACfL 23.04 |
| ----------- | ----------- | ----------- |
| non-SIMD | | |
| SIMD | | |
| OpenCV | | |