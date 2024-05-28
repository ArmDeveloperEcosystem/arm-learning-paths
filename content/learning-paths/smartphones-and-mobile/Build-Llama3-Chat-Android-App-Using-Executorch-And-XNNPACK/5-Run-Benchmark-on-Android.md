---
title: Run Benchmark on Android phone
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build llama runner binary for Android

We need to cross compile llama runner to run on Android using following steps

### 1. Set Android NDK

``` bash
export ANDROID_NDK=<path-to-android-ndk>
```

{{% notice Note %}}
<path_to_android_ndk> is the root for the NDK, which is usually under ~/Library/Android/sdk/ndk/XX.Y.ZZZZZ for macOS, and contains NOTICE and README.md. We use <path_to_android_ndk>/build/cmake/android.toolchain.cmake for CMake to cross-compile.
{{% /notice %}}

### 2. Build executorch and associated libraries for android

``` bash
cmake -DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK/build/cmake/android.toolchain.cmake \
    -DANDROID_ABI=arm64-v8a \
    -DANDROID_PLATFORM=android-23 \
    -DCMAKE_INSTALL_PREFIX=cmake-out-android \
    -DCMAKE_BUILD_TYPE=Release \
    -DEXECUTORCH_BUILD_EXTENSION_MODULE=ON \
    -DEXECUTORCH_BUILD_EXTENSION_DATA_LOADER=ON \
    -DEXECUTORCH_ENABLE_LOGGING=1 \
    -DPYTHON_EXECUTABLE=python \
    -DEXECUTORCH_BUILD_XNNPACK=ON \
    -DEXECUTORCH_BUILD_KERNELS_OPTIMIZED=ON \
    -DEXECUTORCH_BUILD_KERNELS_QUANTIZED=ON \
    -DEXECUTORCH_BUILD_KERNELS_CUSTOM=ON \
    -Bcmake-out-android .

cmake --build cmake-out-android -j16 --target install --config Release
```

### 3. Build llama runner for android

``` bash
cmake  -DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK/build/cmake/android.toolchain.cmake \
    -DANDROID_ABI=arm64-v8a \
    -DANDROID_PLATFORM=android-23 \
    -DCMAKE_INSTALL_PREFIX=cmake-out-android \
    -DCMAKE_BUILD_TYPE=Release \
    -DPYTHON_EXECUTABLE=python \
    -DEXECUTORCH_BUILD_XNNPACK=ON \
    -DEXECUTORCH_BUILD_KERNELS_OPTIMIZED=ON \
    -DEXECUTORCH_BUILD_KERNELS_QUANTIZED=ON \
    -DEXECUTORCH_BUILD_KERNELS_CUSTOM=ON \
    -Bcmake-out-android/examples/models/llama2 \
    examples/models/llama2

cmake --build cmake-out-android/examples/models/llama2 -j16 --config Release
```

{{% notice Note %}}
For Llama3, add `-DEXECUTORCH_USE_TIKTOKEN=ON` option when building the llama runner.
{{% /notice %}}

## Run on Android via adb shell

*Pre-requisite*: Make sure you enable USB debugging via developer options on your phone.

### 1. Connect your android phone

### 2. Upload model, tokenizer and llama runner binary to phone

``` bash
adb shell mkdir -p /data/local/tmp/llama
adb push <model.pte> /data/local/tmp/llama/
adb push <tokenizer.bin> /data/local/tmp/llama/
adb push cmake-out-android/examples/models/llama2/llama_main /data/local/tmp/llama/
```

{{% notice Note %}}
For Llama3, you can pass the original `tokenizer.model` (without converting to `.bin` file).
{{% /notice %}}

### 3. Run model

``` bash
adb shell "cd /data/local/tmp/llama && ./llama_main --model_path <model.pte> --tokenizer_path <tokenizer.bin> --prompt \"Once upon a time\" --seq_len 120"
```
