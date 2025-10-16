---
title: Android Integration
weight: 7 

### FIXED, DO NOT MODIFY
layout: learningpathall
---

####  Integration
Build the Llama Runner Binary for Android
Cross-compile the Llama Runner to enable execution on Android by following the steps outlined below.

#### Android NDK
Configure the environment variable to reference the Android NDK
```
export ANDROID_NDK=$ANDROID_HOME/ndk/28.0.12433566/
```

Ensure that $ANDROID_NDK/build/cmake/android.toolchain.cmake is accessible so CMake can perform cross-compilation.

#### Use KleidiAI to build ExecuTorch and the required libraries for Android deployment
build ExecuTorch for Android, leveraging the performance optimizations offered by [KleidiAI](https://gitlab.arm.com/kleidi/kleidiai) kernels

Use cmake to cross-compile ExecuTorch:
```
cmake -DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK/build/cmake/android.toolchain.cmake \
    -DANDROID_ABI=arm64-v8a \
    -DANDROID_PLATFORM=android-23 \
    -DCMAKE_INSTALL_PREFIX=cmake-out-android \
    -DEXECUTORCH_ENABLE_LOGGING=1 \
    -DCMAKE_BUILD_TYPE=Release \
    -DEXECUTORCH_BUILD_EXTENSION_DATA_LOADER=ON \
    -DEXECUTORCH_BUILD_EXTENSION_MODULE=ON \
    -DEXECUTORCH_BUILD_EXTENSION_TENSOR=ON \
    -DEXECUTORCH_BUILD_EXTENSION_FLAT_TENSOR=ON \
    -DEXECUTORCH_BUILD_XNNPACK=ON \
    -DEXECUTORCH_BUILD_KERNELS_OPTIMIZED=ON \
    -DEXECUTORCH_BUILD_KERNELS_QUANTIZED=ON \
    -DEXECUTORCH_BUILD_KERNELS_CUSTOM=ON \
    -DEXECUTORCH_BUILD_KERNELS_LLM=ON \
    -DEXECUTORCH_BUILD_EXTENSION_LLM_RUNNER=ON \
    -DEXECUTORCH_BUILD_EXTENSION_LLM=ON \
    -DEXECUTORCH_BUILD_EXTENSION_RUNNER_UTIL=ON \
    -DEXECUTORCH_XNNPACK_ENABLE_KLEIDI=ON \
    -DXNNPACK_ENABLE_ARM_BF16=OFF \
    -DBUILD_TESTING=OFF \
    -Bcmake-out-android .

cmake --build cmake-out-android -j7 --target install --config Release
```
Beginning with ExecuTorch version 0.7 beta, KleidiAI is enabled by default. The option -DEXECUTORCH_XNNPACK_ENABLE_KLEIDI=ON is active, providing built-in support for KleidiAI kernels within ExecuTorch when using XNNPack.

#### Build Llama runner for Android
```
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
    -DSUPPORT_REGEX_LOOKAHEAD=ON \
    -DBUILD_TESTING=OFF \
    -Bcmake-out-android/examples/models/llama \
    examples/models/llama

cmake --build cmake-out-android/examples/models/llama -j16 --config Release

```
Execute on Android using adb shell.
You will need an Arm-based Android smartphone with the i8mm feature and at least 16GB of RAM. The steps below were validated on a Google Pixel 8 Pro.
#### Create New Android Project
Open Android Studio → New Project → Empty Activity

#### Add ExecuTorch Runtime to build.gradle
```
dependencies {
    implementation files('libs/executorch.aar')
}
```

#### Android phone connection 
Connect your Android device to your computer using a USB cable.

Ensure that USB debugging is enabled on your device. You can follow the Configure on-device developer options guide to enable it.

After enabling USB debugging and connecting the device via USB, run the following command:
```
adb devices
```

#### model, tokenizer, and Llama runner
```
adb shell mkdir -p /data/local/tmp/llama
adb push llama3_1B_kv_sdpa_xnn_qe_4_64_1024_embedding_4bit.pte /data/local/tmp/llama/
adb push $HOME/.llama/checkpoints/Llama3.2-1B-Instruct/tokenizer.model /data/local/tmp/llama/
adb push cmake-out-android/examples/models/llama/llama_main /data/local/tmp/llama/

```

#### Model Running 
```
adb shell "cd /data/local/tmp/llama && ./llama_main --model_path llama3_1B_kv_sdpa_xnn_qe_4_64_1024_embedding_4bit.pte --tokenizer_path tokenizer.model --prompt '<|start_header_id|>system<|end_header_id|>\nYour name is Cookie. you are helpful, polite, precise, concise, honest, good at writing. You always give precise and brief answers up to 32 words<|eot_id|><|start_header_id|>user<|end_header_id|>\nHey Cookie! how are you today?<|eot_id|><|start_header_id|>assistant<|end_header_id|>' --warmup=1 --cpu_threads=5"
```