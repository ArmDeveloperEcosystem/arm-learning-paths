---
# User change
title: "Overview" 

weight: 100 # 1 is first, 2 is second, etc.

# Do not modify these elements
layout: "learningpathall"
---

# Overview

This Learning Path introduces porting methodologies when migrating applications to Arm. As a practical example an `x86_64` application running in a Linux environment will be ported to `aarch64`. Emulation, remote hardware and physical hardware will be used to run the ported application on `aarch64`. Note: access to physical Arm hardware isn't a requirement.

## Porting methodology

When starting to migrate to Arm, some research will be necessary. It is important to understand the original platform environment used for developing, building and running the application which will be migrated. The questions below address some of these important aspects.
- What is the original platform architecture (e.g. x86_64)?
- Does the application use hardware acceleration (e.g. Nvidia GPU)?
- What OS does the application run on?
- How is the application deployed (e.g., bare metal or virtualized)?
- What is the application's source langage(s)?
- Is the application cross-compiled or built natively?
- What are the application's system dependencies? Does the application use external libraries?
- How is the application built (e.g. configuration) and which tools are used (e.g. compilers)?
- Are there any architecture specific functions or libraries?

These questions help draw a picture of the migration process to identify:
- the target platform configuration (e.g. hardware acceleration, OS, system dependencies),
- development tools (e.g. compilers),
- application requirements and configuration (e.g. compiler flags, third-party libraries).

In the next section we will analyze and answer these questions, which are applicable, based on an suitable example application.

# Application porting

A Sobel filter implementation was selected as the example application to port as it is an applicable embedded computer vision workload. The [Sobel SIMD OpenCV repo](https://github.com/m3y54m/sobel-simd-opencv/) is implemented in three different ways which makes it a great example candidate to show different aspects of porting. It is implemented in the following ways:
* Non-SIMD
  * pure C++ code
* SIMD 
  * `x86_64` intrinsics
* OpenCV
  * a computer vision library

The application is built on an `x86_64` machine and runs on CPU only, find additional details in the table below.

| OS | Compiler | Build tools | Programming language | Intrinsics | External libraries |
| --- | --- | --- | --- | --- | --- |
| Ubuntu 22.04.2 | GCC 11.3.0 | CMake 3.22.1 | C++14 | AVX | OpenCV 4.5.4 |

These bullets and table act as the starting point for the porting analysis.

## Analysis 

Using the original software and tool versions when porting an application isn't a requirement, however it is recommended as it will make the porting smoother. By looking at the [Sobel SIMD OpenCV repo](https://github.com/m3y54m/sobel-simd-opencv/) and with the questions from the previous section in mind start the analysis.

In `src/main.cpp`:
- the header file `x86intrin.h` isn't supported on `aarch64`
- the function `SobelSimd` has intrinsics prefixed with `_mm_` which aren't supported on `aarch64`

These intrinsics will need to be ported in the source code for the application to compile on `aarch64`.

In `src/CMakeLists.txt`:
```cmake
# Enable SIMD instructions for Intel Intrinsics
# https://software.intel.com/sites/landingpage/IntrinsicsGuide/
if(NOT WIN32)
    set(CMAKE_CXX_FLAGS "${CMAKE_CXX_FLAGS} -mavx")
endif()
```
  
The flag `-mavx` used with GCC is architecture-specific and only available on [x86_64](https://man7.org/linux/man-pages/man1/gcc.1.html) and will prevent the application from compiling entirely. Even though the application won't compile, no changes to the source code for the non-SIMD and OpenCV implementations will be necessary.

The table below outlines the migration analysis.
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
  * Arm's has three SIMD technologies
    * [NEON](https://developer.arm.com/documentation/den0018/a)
    * Scalable Vector Extension ([SVE](https://developer.arm.com/documentation/102131/0100/?lang=en))
    * Scalable Vector Extension version 2 ([SVE2](https://developer.arm.com/documentation/102340/0100/Introducing-SVE2?lang=en))

Next, we'll select some suitable target platforms to run the migrated application on.
* cross-platform (emulation)
  * this only requires installing QEMU on the original platform
* remote
  * AWS Graviton instances are easily accessible
* physical
  * Raspberry Pi 4 is a popular off-the-shelf single-board computer

We're now at a stage where the porting work can begin.

## <a name="compiler_options_porting"></a>Compiler options porting

There might be minor differences to the changes necessary depending on what we're migrating to.
The `armv8-a` compiler option will be used which will work across all the three platform targets. Compiler options can be tuned and optimized to achieve higher performance, however in this guide we'll keep it simple. Start by cloning the Sobel filter repository.

```bash
git clone https://github.com/m3y54m/sobel-simd-opencv.git
cd sobel-simd-opencv
```

In the `CMakeLists.txt` file, the `-mavx` compiler option needs to be replaced with `armv8-a` and we're also adding the optimization flag `-O2` (TODO: why?). This can be done by running the following command.
```bash
sed -i "s/-mavx/-O2\ -march=armv8-a/g" src/CMakeLists.txt
```

## <a name="x86_intrinsics_porting"></a>x86 intrinsics porting

To port the AVX intrinsics, we'll use SIMD Everywhere ([SIMDe](https://github.com/simd-everywhere/simde)). Start by cloning the SIMDe repository.
```bash
git clone https://github.com/simd-everywhere/simde.git
```

We wish to make the following changes to `CMakeLists.txt`.
```
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
```cpp
#define SIMDE_ENABLE_NATIVE_ALIASES
#ifdef __aarch64__
#include "simde/x86/avx.h"
#else
#warning AVX support is not available. Code will not compile
#endif
```

This can be done quickly with these two commands:

```bash
sed -i "40i #define SIMDE_ENABLE_NATIVE_ALIASES\n#ifdef __aarch64__\n#include \"simde/x86/avx.h\"\n#else\n#warning AVX support is not available. Code will not compile\n#endif" src/main.cpp
```

The porting of the application is now complete and next we'll create the development environment so the ported application can be compiled.

# Development environment

Two different development environments will be setup; one with GNU Compiler Collection ([GCC](https://gcc.gnu.org/)) and the other with Arm Compiler for Linux ([ACfL](https://developer.arm.com/Tools%20and%20Software/Arm%20Compiler%20for%20Linux)). For convenience, containers will be used to set up the development environments allowing us to compile and run the example application.

See [Docker Engine](https://learn.arm.com/install-guides/docker/docker-engine/) for instructions how to install Docker in your Linux environment.

Note: GCC compiler options are compatible with ACfL compiler options, i.e., they will use the same `CMakeLists.txt` file in this guide.

## GCC

Create a file named `Dockerfile` with the following content:

```
FROM ubuntu:22.04
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get -y install vim wget sudo git tar build-essential libopencv-dev cmake
RUN apt-get clean

ENV USER=ubuntu
RUN useradd --create-home -s /bin/bash -m $USER && echo "$USER:ubuntu" | chpasswd && adduser $USER sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

WORKDIR /home/ubuntu
USER ubuntu
```

This is our GCC development environment. The `Dockerfile` stays the same for cross-platform and native build of the Docker image, however the build command is slightly different.

### Cross-platform

The cross-platform build using `buildx` enables us to build an `aarch64` container on an `x86_64` machine. Once built, the cross-platform built container can be run on that same `x86_64` machine using QEMU, quite convenient! To build the container, run the following command:

```bash
docker buildx build --platform linux/aarch64 -t sobel_example .
```

### Native

For AWS Graviton instances and Raspberry Pi 4.

```bash
docker build -t sobel_example .
```

## ACfL

For AWS Graviton instances and Raspberry Pi 4.


The base container image already exists, only OpenCV needs to be installed inside.

```bash
docker pull armswdev/arm-compiler-for-linux
docker tag armswdev/arm-compiler-for-linux sobel_afcl_example
```

Now that we have our development environments defined we can compile and run the Sobel filter application.

# Application execution
To run the application on our new target platform, the following steps will be taken:
1. Launch the developer environment
2. Make porting modifications
3. Compile
4. Run

Depending on target platform and compiler, there will be slight differences in how to execute the application.

## QEMU

Start the Docker container on your `x86_64` machine and run the following command:
```bash
sudo apt install -y x11-xserver-utils
xhost +local:*
docker run -it --rm --platform linux/aarch64 --net=host -e DISPLAY=$DISPLAY -v /tmp/.X11-unix/:/tmp/.X11-unix/ -v $HOME/.Xauthority:/home/ubuntu/.Xauthority sobel_example /bin/bash
```

Then follow the instructions from
* [Compiler options porting](#compiler_options_porting)
* [x86 intrinsics porting](#x86_intrinsics_porting)

Finally, compile and run the application.
```bash
cmake -S src -B build
cd build/
make
./sobel_simd_opencv
```

Note: only the container is cross-compiled and the application is natively compiled as it is built inside the emulated `aarch64` environment.

## AWS Graviton

ssh with "-X" option for display forwarding

Graviton2
(t4g.medium, Ubuntu 22.04.2 LTS, 16GB storage)
Arm Neoverse N1
NEON 128b vector width

Graviton3
(c7g.medium, Ubuntu 22.04.2 LTS, 16GB storage)
Arm Neoverse V1
Scalable Vector Extension (SVE) 256b vector width

### GCC

### ACfL

## Raspberry Pi 4

Plugged in to display, connected to the internet, Docker installed

Now that we've run the application on all target platforms, let's take a look at the results.

# Results
A successful run will output execution time measurement results in the terminal for the three implementations and open four windows with images (as shown below) of the original, non-SIMD, SIMD and OpenCV images of a butterfly.

![Sobel filter#center](images/sobel_filter_output.jpg)

## QEMU
| | QEMU | | 
| --- | --- | --- |
| Compiler | GCC 11.3.0 |
| Non-SIMD | 1.00 |
| SIMD     | 0.29 |
| OpenCV   | 0.02 |

## Graviton

| | Graviton2 | | Graviton3 | |
| --- | --- | --- | --- | --- | --- | --- |
| Compiler | GCC 12.2.0 | ACfL 22.1 | GCC 12.2.0 | ACfL 22.1 |
| Non-SIMD | 1.0 | 1.0 | 1.7 | 1.8 |
| SIMD     | 3.4 | 3.8 | 5.8 | 6.7 |
| OpenCV   | 0.3 | 0.3 | 0.4 | 0.5 |

The results in the table above have been normalized to the _Graviton2 Non-SIMD_ value, giving the relative speed-up. The following conclusions can be drawn:
* Graviton3 runs the Sobel filter workload faster than Graviton2
* ACfL performs slighlty better than GCC for the _SIMD_ version of the Sobel filter

## Raspberry Pi 4

| | Raspberry Pi 4 | |
| --- | --- | --- |
| Compiler | GCC 12.2.0 | ACfL 22.1 |
| Non-SIMD |  |  |
| SIMD     |  |  |
| OpenCV   |  |  |
