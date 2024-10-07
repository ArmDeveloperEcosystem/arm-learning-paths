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
export ANDROID_NDK=~/Library/Android/sdk/ndk/27.0.12077973
```

{{% notice Note %}}
Make sure you can confirm $ANDROID_NDK/build/cmake/android.toolchain.cmake is available for CMake to cross-compile.
{{% /notice %}}

### 2. Build ExecuTorch and associated libraries for Android

Use `cmake` to cross-compile ExecuTorch:

``` bash
cmake -DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK/build/cmake/android.toolchain.cmake \
    -DANDROID_ABI=arm64-v8a \
    -DANDROID_PLATFORM=android-23 \
    -DCMAKE_INSTALL_PREFIX=cmake-out-android \
    -DCMAKE_BUILD_TYPE=Release \
    -DEXECUTORCH_BUILD_EXTENSION_MODULE=ON \
    -DEXECUTORCH_BUILD_EXTENSION_DATA_LOADER=ON \
    -DEXECUTORCH_BUILD_EXTENSION_RUNNER_UTIL=ON \
    -DEXECUTORCH_BUILD_EXTENSION_TENSOR=ON \
    -DEXECUTORCH_ENABLE_LOGGING=1 \
    -DPYTHON_EXECUTABLE=python \
    -DEXECUTORCH_BUILD_XNNPACK=ON \
    -DEXECUTORCH_BUILD_KERNELS_OPTIMIZED=ON \
    -DEXECUTORCH_BUILD_KERNELS_QUANTIZED=ON \
    -DEXECUTORCH_BUILD_KERNELS_CUSTOM=ON \
    -Bcmake-out-android .

cmake --build cmake-out-android -j16 --target install --config Release
```

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
    -DEXECUTORCH_BUILD_EXTENSION_MODULE=ON \
    -DEXECUTORCH_BUILD_EXTENSION_DATA_LOADER=ON \
    -DEXECUTORCH_BUILD_EXTENSION_TENSOR=ON \
    -DEXECUTORCH_BUILD_EXTENSION_RUNNER_UTIL=ON \
    -DEXECUTORCH_BUILD_KERNELS_QUANTIZED=ON \
    -DEXECUTORCH_BUILD_KERNELS_CUSTOM=ON \
    -Bcmake-out-android/examples/models/llama2 \
    examples/models/llama2

cmake --build cmake-out-android/examples/models/llama2 -j16 --config Release
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
adb push llama3.2_bl256_maxlen1024.pte /data/local/tmp/llama/
adb push $HOME/.llama/checkpoints/Llama3.2-1B/tokenizer.model /data/local/tmp/llama/
adb push cmake-out-android/examples/models/llama2/llama_main /data/local/tmp/llama/
```

{{% notice Note %}}
For Llama 2, you need to convert the `tokenizer.model` into a `.bin` file.
{{% /notice %}}

### 3. Run the model

Use the Llama runner to execute the model on the phone with the `adb` command:

``` bash
adb shell "cd /data/local/tmp/llama && ./llama_main --model_path llama3.2_bl256_maxlen1024.pte --tokenizer_path tokenizer.model --prompt \"Once upon a time\" --seq_len 120"
```

The output should look something like this.

```
I 00:00:00.014047 executorch:cpuinfo_utils.cpp:61] Reading file /sys/devices/soc0/image_version
I 00:00:00.014534 executorch:cpuinfo_utils.cpp:77] Failed to open midr file /sys/devices/soc0/image_version
I 00:00:00.014587 executorch:cpuinfo_utils.cpp:157] Number of efficient cores 4
I 00:00:00.014606 executorch:main.cpp:69] Resetting threadpool with num threads = 4
I 00:00:00.023634 executorch:runner.cpp:65] Creating LLaMa runner: model_path=llama3.2_bl256_maxlen1024.pte, tokenizer_path=tokenizer.model
I 00:00:03.949516 executorch:runner.cpp:94] Reading metadata from model
I 00:00:03.949598 executorch:runner.cpp:119] Metadata: get_vocab_size = 128256
I 00:00:03.949607 executorch:runner.cpp:119] Metadata: get_bos_id = 128000
I 00:00:03.949611 executorch:runner.cpp:119] Metadata: use_sdpa_with_kv_cache = 1
I 00:00:03.949614 executorch:runner.cpp:119] Metadata: get_n_eos = 1
I 00:00:03.949618 executorch:runner.cpp:119] Metadata: append_eos_to_prompt = 0
I 00:00:03.949621 executorch:runner.cpp:119] Metadata: get_max_seq_len = 1024
I 00:00:03.949624 executorch:runner.cpp:119] Metadata: enable_dynamic_shape = 1
I 00:00:03.949626 executorch:runner.cpp:119] Metadata: use_kv_cache = 1
I 00:00:03.949629 executorch:runner.cpp:119] Metadata: get_n_bos = 1
I 00:00:03.949632 executorch:runner.cpp:126] eos_id = 128009
I 00:00:03.949634 executorch:runner.cpp:126] eos_id = 128001
I 00:00:03.949702 executorch:runner.cpp:180] RSS after loading model: 1223.152344 MiB (0 if unsupported)
Once upon a timeI 00:00:04.050916 executorch:text_prefiller.cpp:53] Prefill token result numel(): 128256
,I 00:00:04.052155 executorch:runner.cpp:249] RSS after prompt prefill: 1223.152344 MiB (0 if unsupported)
 I was a business traveler, and I thought that a business trip was the greatest joy in the world.
I had a lovely time abroad in the States, which was, to me, the most wonderful thing in the world. And then I went back to my country to take care of my family and my business. It was the most wonderful thing in the world to me.
I 00:00:06.953141 executorch:runner.cpp:263] RSS after finishing text generation: 1223.152344 MiB (0 if unsupported)
I 00:00:06.954332 executorch:stats.h:97]        Prompt Tokens: 5    Generated Tokens: 114
I 00:00:06.954380 executorch:stats.h:103]       Model Load Time:                3.926000 (seconds)
I 00:00:06.954407 executorch:stats.h:113]       Total inference time:           3.003000 (seconds)           Rate:   37.962038 (tokens/second)
I 00:00:06.954446 executorch:stats.h:121]               Prompt evaluation:      0.102000 (seconds)           Rate:   49.019608 (tokens/second)
I 00:00:06.954477 executorch:stats.h:132]               Generated 114 tokens:   2.901000 (seconds)           Rate:   39.296794 (tokens/second)
I 00:00:06.954516 executorch:stats.h:140]       Time to first generated token:  0.102000 (seconds)
I 00:00:06.954551 executorch:stats.h:147]       Sampling time over 119 tokens:  0.143000 (seconds)

PyTorchObserver {"prompt_tokens":5,"generated_tokens":114,"model_load_start_ms":1727953984276,"model_load_end_ms":1727953988202,"inference_start_ms":1727953988203,"inference_end_ms":1727953991206,"prompt_eval_end_ms":1727953988305,"first_token_ms":1727953988305,"aggregate_sampling_time_ms":143,"SCALING_FACTOR_UNITS_PER_SECOND":1000}
```

You have successfully run a model on your Android smartphone.