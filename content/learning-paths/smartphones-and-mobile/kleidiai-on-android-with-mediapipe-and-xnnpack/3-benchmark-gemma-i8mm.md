---
title: Benchmarking the Gemma 2B Model using Android NDK r25 with i8mm
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Cross-compile the inference engine for CPU (Android)

In this section, you'll modify MediaPipe build files in order to compile the llm benchmarking executable with support for i8mm, Arm's 8-bit matrix multiply extensions.

This executable will not yet include the KleidiAI optimizations, which you will add in the next section.



Modify the xnn_utils BUILD file to generate a static target; simply add linkstatic = True to mediapipe/tasks/cc/genai/inference/utils/xnn_utils/BUILD. Instead of this:

```
cc_test(
    name = "llm_test",
    srcs = [
        "llm_test.cc",
    ],
    deps = [
```

replace with this:

```
cc_test(
    name = "llm_test",
    srcs = [
        "llm_test.cc",
    ],
    linkstatic = True,
    deps = [
```

Download NDK r25. Bazel only supports up to NDK r21, which does not have support for i8mm instructions. Google has released a workaround that lets us build the binary with NDK r25 (with support for i8mm instructions) by modifying the WORKSPACE file at the root of the MediaPipe repo to use `rules_android_ndk`.

```bash

cd /home/ubuntu/Android/Sdk/ndk-bundle/

wget https://dl.google.com/android/repository/android-ndk-r25c-linux.zip

unzip android-ndk-r25c-linux.zip

```

Add NDK bin folder to your PATH variable:

```bash

export PATH=$PATH:/home/ubuntu/Android/Sdk/ndk-bundle/android-ndk-r25c/toolchains/llvm/prebuilt/linux-x86_64/bin/

```

Modify the WORKSPACE file to add the path to Andoird NDK r25:

```bash

android_ndk_repository(name = "androidndk", api_level=30, path="/home/ubuntu/Android/Sdk/ndk-bundle/android-ndk-r25c")

android_sdk_repository(name = "androidsdk", path = "/home/ubuntu/Android/Sdk")

```

Modify the WORKSPACE file to modify the path to Android NDK r25 add the Starlark rules for integrating Bazel with the Android NDK. Instead of this snippet:

```
workspace(name = "mediapipe")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# Protobuf expects an //external:python_headers target
bind(
    name = "python_headers",
    actual = "@local_config_python//:python_headers",
)
```

Replace with this:

```
workspace(name = "mediapipe")

load("@bazel_tools//tools/build_defs/repo:http.bzl", "http_archive")

# Protobuf expects an //external:python_headers target
bind(
    name = "python_headers",
    actual = "@local_config_python//:python_headers",
)

# Add binding rule for the toolchain, so the added rules and existing bazel rules can use the same reference
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
```

Enable the i8mm extensions. This can be done by changing the xnn_enable_arm_i8mm flag in the .bazelrc file found in the root of the MediaPipe repo.

Change these lines:

```bash
# TODO: Remove this flag once we updated to NDK 25
build:android --define=xnn_enable_arm_i8mm=false
```

To these lines:

```bash
# TODO: Remove this flag once we updated to NDK 25
build:android --define=xnn_enable_arm_i8mm=true
```

Modify the benchmarking tool llm_test (mediapipe/tasks/cc/genai/inference/utils/xnn_utils/llm_test.cc) to specify `encode` as the benchmark method:

```
ABSL_FLAG( std::string, benchmark_method, "encode", // change to encode to run the encoder "The method to benchmark the latency, can be either 'decode', 'encode'.");
```

Build llm_test:

```bash

bazel build -c opt --config=android_arm64 mediapipe/tasks/cc/genai/inference/utils/xnn_utils:llm_test

```

Push the resulting binary to the phone:

```bash
adb push bazel-bin/mediapipe/tasks/cc/genai/inference/utils/xnn_utils/llm_test /data/local/tmp/gen_ai
```

Run the binary on the phone:

```bash

./llm_test

```

The output should look like this:

```bash
husky:/data/local/tmp/gen_ai $ ./llm_test
2024-05-15T04:03:11-05:00
Running ./llm_test
Run on (9 X 1704 MHz CPU s)
***WARNING*** CPU scaling is enabled, the benchmark real time measurements may be noisy and will incur extra overhead.
----------------------------------------------------------------------------------
Benchmark                        Time             CPU   Iterations UserCounters...
----------------------------------------------------------------------------------
BM_Llm_QCINT8/64        1413595825 ns   1405839235 ns            1 items_per_second=45.5244/s
BM_Llm_QCINT8/512       11338469203 ns   11291735706 ns            1 items_per_second=45.3429/s
BM_Llm_QCINT8/1024      30558027236 ns   30407135781 ns            1 items_per_second=33.6763/s
BM_Llm_Mixed_INT48/64   2314495607 ns   2291420478 ns            1 items_per_second=27.9303/s
BM_Llm_Mixed_INT48/512  10863001429 ns   10799244374 ns            1 items_per_second=47.4107/s
BM_Llm_Mixed_INT48/1024 22200514578 ns   22074653562 ns            1 items_per_second=46.388/s
```


