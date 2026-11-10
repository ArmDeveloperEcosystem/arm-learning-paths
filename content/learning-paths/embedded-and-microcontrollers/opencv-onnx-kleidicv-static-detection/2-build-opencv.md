---
title: "Build OpenCV with and without KleidiCV"
description: Compile two matching OpenCV installations on arm64 Linux to compare baseline preprocessing with the default KleidiCV configuration.

weight: 3

layout: "learningpathall"
---

## Check the arm64 environment

Confirm that the board runs a 64-bit Arm userspace:

```bash
uname -m
```

The expected output is:

```output
aarch64
```

Record the operating system, kernel, CPU topology, and CPU features:

```bash
cat /etc/os-release
uname -r
lscpu
```

Keep this information with your benchmark results. KleidiCV selects supported implementations for the available CPU features.

{{% notice Note %}}
The reference measurements described in this Learning Path were collected on a
[Radxa Orion O6](https://radxa.com/products/orion/o6/) running Debian 12.
The board has eight Cortex-A720 CPUs and four Cortex-A520 CPUs. You can use
another arm64 Linux system, but CPU topology, supported extensions, and
performance results will differ.
{{% /notice %}}

## Install the build tools

Install the compiler, CMake, Ninja, Git, and image codec development packages:

```bash
sudo apt update
sudo apt install -y \
    build-essential \
    ca-certificates \
    cmake \
    file \
    git \
    libjpeg-dev \
    libpng-dev \
    libtiff-dev \
    ninja-build \
    pkg-config \
    util-linux \
    wget
```

Record the compiler and CMake versions:

```bash
c++ --version
cmake --version
```

Use GCC 10 or later, or Clang 12 or later. If compilation exhausts memory, reduce the `--parallel` value in the build commands.

## Download OpenCV

Create a workspace and check out OpenCV 4.13.0:

```bash
mkdir -p ~/opencv-kleidicv-lab
cd ~/opencv-kleidicv-lab
git clone --branch 4.13.0 --depth 1 https://github.com/opencv/opencv.git
```

## Download KleidiCV 26.06

Clone the KleidiCV 26.06 release:

```bash
cd ~/opencv-kleidicv-lab
git clone --branch 26.06 --depth 1 \
    https://gitlab.arm.com/kleidi/kleidicv.git
```

Confirm the selected release:

```bash
git -C kleidicv describe --tags --exact-match
```

The expected output is:

```output
26.06
```

OpenCV 4.13.0 downloads KleidiCV 0.7.0 when `KLEIDICV_SOURCE_PATH` isn't provided. For the Learning Path, KleidiCV 26.06 is explicitly selected. This is because KleidiCV 26.06 supports the three-channel, arbitrary-ratio resize used by the letterbox stage.

Both builds use the same OpenCV source tree, compiler, and common CMake options. The intended difference is enabling KleidiCV with its default dispatch policy.

{{% notice Note %}}
Leave OpenCV 4.13.0 unpatched in both builds. The KleidiCV 26.06 OpenCV integration patch adds a `copyMakeBorder()` Hardware Acceleration Layer (HAL) hook that's absent from this OpenCV release. You'll compare preprocessing without that patch, so padding remains an OpenCV operation. Applying the patch creates a different test and requires new measurements.
{{% /notice %}}

## Build the baseline OpenCV installation

Configure a baseline OpenCV installation without KleidiCV:

```bash
cd ~/opencv-kleidicv-lab

cmake -S opencv -B build-baseline -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=$HOME/opencv-kleidicv-lab/install-baseline \
    -DBUILD_LIST=core,imgproc,imgcodecs,dnn \
    -DBUILD_EXAMPLES=OFF \
    -DBUILD_opencv_apps=OFF \
    -DBUILD_PERF_TESTS=OFF \
    -DBUILD_TESTS=OFF \
    -DBUILD_SHARED_LIBS=ON \
    -DWITH_IPP=OFF \
    -DWITH_OPENCL=OFF \
    -DWITH_KLEIDICV=OFF
```

Build and install the baseline:

```bash
cmake --build build-baseline --parallel "$(nproc)"
cmake --install build-baseline
```

List the installed OpenCV libraries:

```bash
find install-baseline/lib -maxdepth 1 -type l -name 'libopencv_*.so' \
    | sort
```

The expected output is:

```output
install-baseline/lib/libopencv_core.so
install-baseline/lib/libopencv_dnn.so
install-baseline/lib/libopencv_imgcodecs.so
install-baseline/lib/libopencv_imgproc.so
```

Confirm the baseline setting:

```bash
grep '^WITH_KLEIDICV' build-baseline/CMakeCache.txt
```

The expected output is:

```output
WITH_KLEIDICV:BOOL=OFF
```

## Build OpenCV with KleidiCV

Configure the second build with KleidiCV enabled. Leave its dispatch options at their defaults:

```bash
cd ~/opencv-kleidicv-lab

cmake -S opencv -B build-kleidicv-default -G Ninja \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_INSTALL_PREFIX=$HOME/opencv-kleidicv-lab/install-kleidicv-default \
    -DBUILD_LIST=core,imgproc,imgcodecs,dnn \
    -DBUILD_EXAMPLES=OFF \
    -DBUILD_opencv_apps=OFF \
    -DBUILD_PERF_TESTS=OFF \
    -DBUILD_TESTS=OFF \
    -DBUILD_SHARED_LIBS=ON \
    -DWITH_IPP=OFF \
    -DWITH_OPENCL=OFF \
    -DWITH_KLEIDICV=ON \
    -DKLEIDICV_SOURCE_PATH=$HOME/opencv-kleidicv-lab/kleidicv
```

Build and install it:

```bash
cmake --build build-kleidicv-default --parallel "$(nproc)"
cmake --install build-kleidicv-default
```

Confirm that KleidiCV is enabled:

```bash
grep '^WITH_KLEIDICV' build-kleidicv-default/CMakeCache.txt
```

The expected output is:

```output
WITH_KLEIDICV:BOOL=ON
```

Confirm that the KleidiCV libraries were built:

```bash
find build-kleidicv-default/3rdparty/lib -maxdepth 1 -type f \
    -name 'libkleidicv*.a' -printf '%f\n' | sort
```

The expected output is:

```output
libkleidicv.a
libkleidicv_hal.a
libkleidicv_thread.a
```

## What you've accomplished and what's next

You've created baseline and default KleidiCV 26.06 OpenCV installations from the same unpatched source. 

Next, you'll download the YOLOX model and a static test image.
