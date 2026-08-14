---
title: Build the Android Vulkan runtime
description: Install the host Vulkan SDK and compile the Android ExecuTorch runtime and Llama runner with Vulkan enabled.
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Install the host Vulkan SDK

The Android Vulkan build needs a host `glslc` to compile GLSL shaders to SPIR-V.

Install a recent LunarG Vulkan SDK on the Linux host:

```bash
sudo apt update
sudo apt install -y curl xz-utils
mkdir -p "$HOME/vulkan"
cd "$HOME/vulkan"

SDK_VERSION=$(curl -fsSL https://vulkan.lunarg.com/sdk/latest/linux.txt)
curl -fL -o vulkan_sdk.tar.xz \
  "https://sdk.lunarg.com/sdk/download/${SDK_VERSION}/linux/vulkan_sdk.tar.xz"
tar xf vulkan_sdk.tar.xz
source "$HOME/vulkan/$SDK_VERSION/setup-env.sh"
```

Validate that the host SDK is active:

```bash
which glslc
glslc --version
echo "$VULKAN_SDK"
```

The important requirement is that `which glslc` resolves to the host SDK, not to an incompatible Android NDK copy.

## Configure and build ExecuTorch for Android plus Vulkan

From the ExecuTorch checkout:

```bash
cd ~/executorch
source .venv/bin/activate
rm -rf cmake-out-android-so

cmake . \
  -DCMAKE_INSTALL_PREFIX=cmake-out-android-so \
  -DCMAKE_TOOLCHAIN_FILE="$ANDROID_NDK/build/cmake/android.toolchain.cmake" \
  -DANDROID_SUPPORT_FLEXIBLE_PAGE_SIZES=ON \
  --preset android-arm64-v8a \
  -DANDROID_PLATFORM=android-28 \
  -DPYTHON_EXECUTABLE="$(which python)" \
  -DCMAKE_BUILD_TYPE=Release \
  -DEXECUTORCH_PAL_DEFAULT=posix \
  -DEXECUTORCH_BUILD_LLAMA_JNI=OFF \
  -DEXECUTORCH_BUILD_EXTENSION_NAMED_DATA_MAP=ON \
  -DEXECUTORCH_BUILD_VULKAN=ON \
  -DEXECUTORCH_BUILD_TESTS=OFF \
  -B cmake-out-android-so

cmake --build cmake-out-android-so \
  -j4 \
  --target install \
  --config Release
```

`EXECUTORCH_BUILD_LLAMA_JNI=OFF` is intentional. The first attempt failed in the JNI target with:

```text
ld.lld: error: unable to find library -lextension_asr_runner
clang++: error: linker command failed with exit code 1
```

That failure came from `executorch_jni`, not from the Vulkan runtime itself. For the standalone `adb` plus `llama_main` flow, disabling JNI is the simpler fix.

## Build the Android `llama_main` runner

Build the example runner against the installed Android runtime:

```bash
cmake examples/models/llama \
  -DCMAKE_INSTALL_PREFIX=cmake-out-android-so \
  -DCMAKE_TOOLCHAIN_FILE="$ANDROID_NDK/build/cmake/android.toolchain.cmake" \
  -DANDROID_SUPPORT_FLEXIBLE_PAGE_SIZES=ON \
  -DEXECUTORCH_ENABLE_LOGGING=ON \
  -DANDROID_ABI=arm64-v8a \
  -DANDROID_PLATFORM=android-28 \
  -DCMAKE_BUILD_TYPE=Release \
  -DPYTHON_EXECUTABLE="$(which python)" \
  -B cmake-out-android-so/examples/models/llama

cmake --build cmake-out-android-so/examples/models/llama \
  -j4 \
  --config Release
```

Verify the output binary:

```bash
file cmake-out-android-so/examples/models/llama/llama_main
```

Expected shape:

```text
ELF 64-bit LSB pie executable, ARM aarch64, ... interpreter /system/bin/linker64
```
