---
title: Run Benchmark on Android phone
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build Llama runner binary for Android

Cross-compile Llama runner to run on Android using the steps below.

### 1. Set Android NDK

Set the environment variable to point to the Android NDK.

``` bash
export ANDROID_NDK=$ANDROID_HOME/ndk/28.0.12433566/
```

{{% notice Note %}}
Make sure you can confirm $ANDROID_NDK/build/cmake/android.toolchain.cmake is available for CMake to cross-compile.
{{% /notice %}}

### 2. Build ExecuTorch and associated libraries for Android with KleidiAI 

You are now ready to build ExecuTorch for Android by taking advantage of the performance optimization provided by the [KleidiAI](https://gitlab.arm.com/kleidi/kleidiai) kernels. 

Use `cmake` to cross-compile ExecuTorch:

``` bash
cmake -DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK/build/cmake/android.toolchain.cmake \
    -DANDROID_ABI=arm64-v8a \
    -DANDROID_PLATFORM=android-23 \
    -DCMAKE_INSTALL_PREFIX=cmake-out-android \
    -DEXECUTORCH_ENABLE_LOGGING=1 \
    -DCMAKE_BUILD_TYPE=Release \
    -DEXECUTORCH_BUILD_EXTENSION_DATA_LOADER=ON \
    -DEXECUTORCH_BUILD_EXTENSION_MODULE=ON \
    -DEXECUTORCH_BUILD_EXTENSION_TENSOR=ON \
    -DEXECUTORCH_BUILD_XNNPACK=ON \
    -DEXECUTORCH_BUILD_KERNELS_OPTIMIZED=ON \
    -DEXECUTORCH_BUILD_KERNELS_QUANTIZED=ON \
    -DEXECUTORCH_BUILD_KERNELS_CUSTOM=ON \
    -DEXECUTORCH_XNNPACK_ENABLE_KLEIDI=ON \
    -DXNNPACK_ENABLE_ARM_BF16=OFF \
    -Bcmake-out-android .

cmake --build cmake-out-android -j7 --target install --config Release
```
{{% notice Note %}}
Make sure you add -DEXECUTORCH_XNNPACK_ENABLE_KLEIDI=ON option to enable support for KleidiAI kernels in ExecuTorch with XNNPack.
{{% /notice %}}

### 3. Build Llama runner for android

Use `cmake` to cross-compile Llama runner:

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
    -DEXECUTORCH_USE_TIKTOKEN=ON \
    -Bcmake-out-android/examples/models/llama \
    examples/models/llama

cmake --build cmake-out-android/examples/models/llama -j16 --config Release
```

You should now have `llama_main` available for Android.

## Run on Android via adb shell

### 1. Connect your android phone

Connect your phone to your computer using a USB cable.

You need to enable USB debugging on your Android device. You can follow [Configure on-device developer options](https://developer.android.com/studio/debug/dev-options) to enable USB debugging.

Once you have enabled USB debugging and connected via USB, run:

```
adb devices
```

You should see your device listed to confirm it is connected.

### 2. Copy the model, tokenizer, and Llama runner binary to the phone

``` bash
adb shell mkdir -p /data/local/tmp/llama
adb push llama3_1B_kv_sdpa_xnn_qe_4_128_1024_embedding_4bit.pte /data/local/tmp/llama/
adb push $HOME/.llama/checkpoints/Llama3.2-1B/tokenizer.model /data/local/tmp/llama/
adb push cmake-out-android/examples/models/llama/llama_main /data/local/tmp/llama/
```


### 3. Run the model

Use the Llama runner to execute the model on the phone with the `adb` command:

``` bash
adb shell "cd /data/local/tmp/llama && ./llama_main --model_path llama3_1B_kv_sdpa_xnn_qe_4_128_1024_embedding_4bit.pte --tokenizer_path tokenizer.model --prompt "<|start_header_id|>system<|end_header_id|>\nYour name is Cookie. you are helpful, polite, precise, concise, honest, good at writing. You always give precise and brief answers up to 32 words<|eot_id|><|start_header_id|>user<|end_header_id|>\nHey Cookie! how are you today?<|eot_id|><|start_header_id|>assistant<|end_header_id|>" --warmup=1
```

The output should look something like this.

```
I 00:00:09.624421 executorch:stats.h:111] 	Prompt Tokens: 54    Generated Tokens: 73
I 00:00:09.624423 executorch:stats.h:117] 	Model Load Time:		3.464000 (seconds)
I 00:00:09.624425 executorch:stats.h:127] 	Total inference time:		2.871000 (seconds)		 Rate: 	25.426681 (tokens/second)
I 00:00:09.624427 executorch:stats.h:135] 		Prompt evaluation:	0.202000 (seconds)		 Rate: 	267.326733 (tokens/second)
I 00:00:09.624430 executorch:stats.h:146] 		Generated 73 tokens:	2.669000 (seconds)		 Rate: 	27.351068 (tokens/second)
I 00:00:09.624432 executorch:stats.h:154] 	Time to first generated token:	0.202000 (seconds)
I 00:00:09.624434 executorch:stats.h:161] 	Sampling time over 127 tokens:	0.110000 (seconds)
```

You have successfully run the llama 3.1 1B model on your Android smartphone with ExecuTorch using KleidiAI kernels.
