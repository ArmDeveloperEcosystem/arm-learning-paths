---
title: Benchmarking the Gemma 2B Model using Android NDK r25 with i8mm
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Cross-compile the inference engine for CPU (Android)

Include support for i8mm instructionss

Note: Bazel does not natively support newer versions of NDK, it supports up to r21, which does not have support for i8mm instructions.

Google has released a workaround that lets us build the binary with NDK r25 (with support for i8mm instructions) using rules_android_sdk.

1) Modify the BUILD file to generate a static target, to make it easy to push it to the phone, simply add linkstatic = True, to mediapipe/tasks/cc/genai/inference/utils/xnn_utils/BUILD :

```

cc_test(

name = "llm_test",

srcs = [

"llm_test.cc",

],

linkstatic = True,

deps = [

":benchmark_weight_accessor",

":falcon",

":graph_builder",

":llm",

":llm_weights",

```

2) Download NDK r25:

```bash

cd /home/ubuntu/Android/Sdk/ndk-bundle/

wget https://dl.google.com/android/repository/android-ndk-r25c-linux.zip

unzip android-ndk-r25c-linux.zip

```

3) Add NDK bin folder to your PATH variable:

```bash

export PATH=$PATH:/home/ubuntu/Android/Sdk/ndk-bundle/android-ndk-r25c/toolchains/llvm/prebuilt/linux-x86_64/bin/

```

4) Modify the WORKSPACE file to add the path to Andoird NDK r25:

```bash

android_ndk_repository(name = "androidndk", api_level=30, path="/home/ubuntu/Android/Sdk/ndk-bundle/android-ndk-r25c")

android_sdk_repository(name = "androidsdk", path = "/home/ubuntu/Android/Sdk")

```

5) Modify the WORKSPACE file to modify the path to Android NDK r25 add the Starlark rules for integrating Bazel with the Android NDK:

```

workspace(name = "mediapipe")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# Protobuf expects an //external:python_headers target

bind(

name = "python_headers",

actual = "@local_config_python//:python_headers",

)

################### This is the added part

# Add binding rule for the toolchain, so the added rules and existing bazel rules can use the same reference,

bind(

name = "android/crosstool",

actual = "@androidndk//:toolchain",

)

################## Starlark rules

RULES_ANDROID_NDK_COMMIT= "010f4f17dd13a8baaaacc28ba6c8c2c75f54c68b"

RULES_ANDROID_NDK_SHA = "2ab6a97748772f289331d75caaaee0593825935d1d9d982231a437fb8ab5a14d"

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

http_archive(

name = "rules_android_ndk", url = "https://github.com/bazelbuild/rules_android_ndk/archive/%s.zip" % RULES_ANDROID_NDK_COMMIT,

sha256 = RULES_ANDROID_NDK_SHA,

strip_prefix = "rules_android_ndk-%s" % RULES_ANDROID_NDK_COMMIT,

)

load("@rules_android_ndk//:rules.bzl", "android_ndk_repository")

register_toolchains("@androidndk//:all")

################## End of the added part

```

6) Enable i8mm extension, this can be done by changing the following flag in .bazelrc :

build:android --linkopt=-lm

build:android --linkopt=-Wl,--gc-sections

# TODO: Remove this flag once we updated to NDK 25

###### the following flag should be changed to true:

build:android --define=xnn_enable_arm_i8mm=true

build:android_arm --config=android

build:android_arm --cpu=armeabi-v7a

7) Modify the benchmarking tool llm_test (mediapipe/tasks/cc/genai/inference/utils/xnn_utils/llm_test.cc) to run either the Encoder or Decoder on the Gemma 2B model, and change number of threads, if required as the following:

ABSL_FLAG( std::string, benchmark_method, "encode", // change to encode to run the encoder "The method to benchmark the latency, can be either 'decode', 'encode'."); ABSL_FLAG(std::string, model_type, "GEMMA_2B", "The type of model to benchmark, e.g. GEMMA_2B, FALCON_RW_1B"); ABSL_FLAG(int, num_threads, 4, "The number of threads to use"); // Number of threads can be changed here

8) Build llm_test

```bash

bazel build -c opt --config=android_arm64 mediapipe/tasks/cc/genai/inference/utils/xnn_utils:llm_test

```

9) Push the resulting binary to the phone

adb push bazel-bin/mediapipe/tasks/cc/genai/inference/utils/xnn_utils/llm_test /data/local/tmp/gen_ai

10) Run the binary on the phone:

```bash

./llm_test

```

Output should look like:

husky:/data/local/tmp/gen_ai $ ./llm_test

2024-05-15T04:03:11-05:00

Running ./llm_test

Run on (9 X 1704 MHz CPU s)

***WARNING*** CPU scaling is enabled, the benchmark real time measurements may be noisy and will incur extra overhead.

----------------------------------------------------------------------------------

Benchmark Time CPU Iterations UserCounters...

----------------------------------------------------------------------------------

BM_Llm_QCINT8/64 1413595825 ns 1405839235 ns 1 items_per_second=45.5244/s

BM_Llm_QCINT8/512 11338469203 ns 11291735706 ns 1 items_per_second=45.3429/s

BM_Llm_QCINT8/1024 30558027236 ns 30407135781 ns 1 items_per_second=33.6763/s

BM_Llm_Mixed_INT48/64 2314495607 ns 2291420478 ns 1 items_per_second=27.9303/s

BM_Llm_Mixed_INT48/512 10863001429 ns 10799244374 ns 1 items_per_second=47.4107/s

BM_Llm_Mixed_INT48/1024 22200514578 ns 22074653562 ns 1 items_per_second=46.388/s