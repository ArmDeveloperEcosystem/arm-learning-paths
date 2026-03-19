---
title: Run the chatbot on Android
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build the Llama runner binary for Android

Cross-compile the Llama runner to run on your Android phone using the steps below.

### Set the Android NDK path

Set the environment variable to point to the Android NDK:

```bash
export ANDROID_NDK=$ANDROID_HOME/ndk/29.0.14206865/
```

{{% notice Note %}}
Make sure `$ANDROID_NDK/build/cmake/android.toolchain.cmake` is available for CMake to cross-compile.
{{% /notice %}}

### Build ExecuTorch and associated libraries for Android with KleidiAI

Use `cmake` to cross-compile ExecuTorch, enabling the KleidiAI kernels for accelerated inference on Arm:

```bash
cmake -DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK/build/cmake/android.toolchain.cmake \
    -DANDROID_ABI=arm64-v8a \
    -DANDROID_PLATFORM=android-23 \
    -DEXECUTORCH_BUILD_EXTENSION_NAMED_DATA_MAP=ON \
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

{{% notice Note %}}
Starting with ExecuTorch version 0.7 beta, KleidiAI is enabled by default. The `-DEXECUTORCH_XNNPACK_ENABLE_KLEIDI=ON` option adds built-in support for KleidiAI kernels in ExecuTorch with XNNPACK.
{{% /notice %}}

### Build the Llama runner for Android

Use `cmake` to cross-compile the Llama runner:

```bash
cmake -DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK/build/cmake/android.toolchain.cmake \
    -DANDROID_ABI=arm64-v8a \
    -DANDROID_PLATFORM=android-23 \
    -DCMAKE_INSTALL_PREFIX=cmake-out-android \
    -DCMAKE_BUILD_TYPE=Release \
    -DPYTHON_EXECUTABLE=python \
    -DEXECUTORCH_BUILD_KERNELS_OPTIMIZED=ON \
    -DBUILD_TESTING=OFF \
    -Bcmake-out-android/examples/models/llama \
    examples/models/llama

cmake --build cmake-out-android/examples/models/llama -j16 --config Release
```

You should now have `llama_main` available for Android.

{{% notice Note %}}
If Gradle cannot find the Android SDK, add the `sdk.dir` path to `executorch/extension/android/local.properties`.
{{% /notice %}}

## Run the chatbot on Android via adb shell

You need an Arm-powered smartphone with the i8mm feature running Android, with at least 16GB of RAM. The steps below were tested on a Google Pixel 8 Pro.

### Connect your Android phone

Connect your phone to your computer using a USB cable.

Enable USB debugging on your Android device by following [Configure on-device developer options](https://developer.android.com/studio/debug/dev-options).

Once USB debugging is enabled, run:

```bash
adb devices
```

You should see your device listed to confirm it is connected.

### Copy the model, tokenizer, and runner binary to the phone

```bash
adb shell mkdir -p /data/local/tmp/llama
adb push llama3_1B_kv_sdpa_xnn_qe_4_64_1024_embedding_4bit.pte /data/local/tmp/llama/
adb push $HOME/.llama/checkpoints/Llama3.2-1B-Instruct/tokenizer.model /data/local/tmp/llama/
adb push cmake-out-android/examples/models/llama/llama_main /data/local/tmp/llama/
```

### Run the chatbot

The system prompt is where you define your chatbot's persona and behavior. The example below configures the model as a customer support assistant. Adapt the system prompt text to match your product or domain.

```bash
adb shell "cd /data/local/tmp/llama && ./llama_main \
  --model_path llama3_1B_kv_sdpa_xnn_qe_4_64_1024_embedding_4bit.pte \
  --tokenizer_path tokenizer.model \
  --prompt '<|start_header_id|>system<|end_header_id|>\nYou are a helpful customer support assistant. You answer questions about products, help with troubleshooting, and escalate issues politely when needed. Keep responses concise and friendly.<|eot_id|><|start_header_id|>user<|end_header_id|>\nMy order has not arrived yet. What should I do?<|eot_id|><|start_header_id|>assistant<|end_header_id|>' \
  --warmup=1 --cpu_threads=5"
```

The output is similar to:

```output
I tokenizers:regex.cpp:27] Registering override fallback regex
I 00:00:00.003288 executorch:main.cpp:87] Resetting threadpool with num threads = 5
I 00:00:00.006393 executorch:runner.cpp:44] Creating LLaMa runner: model_path=llama3_1B_kv_sdpa_xnn_qe_4_64_1024_embedding_4bit.pte, tokenizer_path=tokenizer.model
I 00:00:00.131486 executorch:llm_runner_helper.cpp:57] Loaded TikToken tokenizer
I 00:00:00.186538 executorch:llm_runner_helper.cpp:110] Metadata: use_sdpa_with_kv_cache = 1
I 00:00:00.186574 executorch:llm_runner_helper.cpp:110] Metadata: use_kv_cache = 1
I 00:00:00.186578 executorch:llm_runner_helper.cpp:110] Metadata: get_max_context_len = 1024
I 00:00:00.186584 executorch:llm_runner_helper.cpp:110] Metadata: get_max_seq_len = 1024
I 00:00:01.086570 executorch:text_llm_runner.cpp:89] Doing a warmup run...
I 00:00:02.264379 executorch:text_llm_runner.cpp:209] Warmup run finished!
I 00:00:02.264384 executorch:text_llm_runner.cpp:95] RSS after loading model: 1122.187500 MiB (0 if unsupported)
```

After the warmup, the model generates a response to the user query. The RSS figure confirms how much memory the model is using on the device.

You now have a Llama 3.2 1B customer support chatbot running entirely on-device on an Arm Android phone. In the next section, you will wrap this into an Android app with a full chat interface.
