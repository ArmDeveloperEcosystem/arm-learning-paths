---
title: Build llama.cpp on the virtual SoC
weight: 3
layout: learningpathall
---

Run these commands in the **guest SSH shell**. This Learning Path was validated with llama.cpp **v1.0.0**, commit `b1b770d`. Official llama.cpp releases use semantic versioning (`vX.Y.Z`). Nightly tags use a build number (`bNNNN`). Pin the release to reproduce this exercise. If you choose a later version, review its release notes and check that the final inspection produces a result with both model files loaded. [Upstream versioning policy](https://github.com/ggml-org/ggml/discussions/1579) · [v1.0.0 release notes](https://github.com/ggml-org/llama.cpp/releases/tag/v1.0.0)

## Prepare the build tools

The validation guest had 16 vCPUs, 7.7 GiB RAM, and 16 GiB of free disk space before the build. Check that your image includes the compiler, Git, Make, wget, and the camera dependencies. Each command should find the requested tool or package.

```bash
command -v c++ git make wget python3 pkg-config flock v4l2-ctl gst-launch-1.0
pkg-config --modversion gstreamer-1.0 gstreamer-app-1.0 gstreamer-video-1.0 libjpeg
ls /usr/bin/virtualcam-listener.py
df -h /root
```

Use the ANA camera-enabled development image if the listener or development packages are missing. Install the AArch64 CMake distribution in your build directory for this shell.

```bash
mkdir -p /root/industrial-ai-build
cd /root/industrial-ai-build
wget https://github.com/Kitware/CMake/releases/download/v3.28.6/cmake-3.28.6-linux-aarch64.tar.gz
tar -xzf cmake-3.28.6-linux-aarch64.tar.gz
export PATH="$PWD/cmake-3.28.6-linux-aarch64/bin:$PATH"
cmake --version
```

## Build the inference server

Clone the tagged source and build the server on the guest. Six parallel compile jobs were used on the validation guest. Reduce the job count if memory is limited.

```bash
git clone --depth 1 --branch v1.0.0 https://github.com/ggml-org/llama.cpp.git
cd llama.cpp
cmake -S . -B build \
  -DCMAKE_BUILD_TYPE=Release \
  -DLLAMA_BUILD_IS_DEV=OFF \
  -DBUILD_SHARED_LIBS=ON \
  -DGGML_OPENMP=OFF \
  -DLLAMA_OPENSSL=OFF \
  -DLLAMA_USE_PREBUILT_UI=OFF
cmake --build build --target llama-server --parallel 6
```

Install the server and its shared libraries together where the demo launcher looks for them. Preserve the library symlinks.

```bash
runtime=/root/qwen/armv9/bin
mkdir -p "$runtime"
cp -a build/bin/llama-server build/bin/*.so* "$runtime/"
LD_LIBRARY_PATH="$runtime" "$runtime/llama-server" --version
```

The validation guest reported the following version. The build number can vary with the checkout history.

```text
version: 1.0.0 (build 1, commit b1b770d)
built with GNU 14.2.0 for Linux aarch64
```
