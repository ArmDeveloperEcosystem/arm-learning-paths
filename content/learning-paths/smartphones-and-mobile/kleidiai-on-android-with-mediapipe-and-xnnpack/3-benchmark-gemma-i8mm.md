---
title: Benchmarking the Gemma 2B Model using Android NDK r25 with i8mm
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Cross-compile the inference engine for CPU (Android)

In this section, you'll modify MediaPipe build files in order to compile the llm benchmarking executable with support for i8mm, Arm's 8-bit matrix multiply extensions.

#### Ensure that your device has the i8mm feature

To test whether your phone chipset contains the i8mm feature, run

```
adb shell cat /proc/cpuinfo | grep i8mm
```

If any lines are returned, then your phone has the i8mm capability.


#### Setting up the build

Modify the xnn_utils BUILD file to generate a static target; simply add linkstatic = True to mediapipe/tasks/cc/genai/inference/utils/xnn_utils/BUILD.

First search for these lines:

```
cc_test(
    name = "llm_test",
    srcs = [
        "llm_test.cc",
    ],
```

Add `linkstatic = True` right after that section like this:

```
cc_test(
    name = "llm_test",
    srcs = [
        "llm_test.cc",
    ],
    linkstatic = True,
```

Download NDK r25. Bazel only supports up to NDK r21, which does not have support for i8mm instructions. Google has released a workaround that lets us build the binary with NDK r25 (with support for i8mm instructions) by modifying the WORKSPACE file at the root of the MediaPipe repo to use `rules_android_ndk`.

```bash

cd $HOME/Android/Sdk/ndk-bundle/

wget https://dl.google.com/android/repository/android-ndk-r25c-linux.zip

unzip android-ndk-r25c-linux.zip

```

Add NDK bin folder to your PATH variable:

```bash

export PATH=$PATH:$HOME/Android/Sdk/ndk-bundle/android-ndk-r25c/toolchains/llvm/prebuilt/linux-x86_64/bin/

```

Modify the WORKSPACE file to add the path to Android NDK r25:

```bash

android_ndk_repository(name = "androidndk", api_level=30, path="/home/ubuntu/Android/Sdk/ndk-bundle/android-ndk-r25c")

android_sdk_repository(name = "androidsdk", path = "/home/ubuntu/Android/Sdk")

```

{{% notice Note %}}
The functions above require absolute paths, so if your `$HOME` directory is not `/home/ubuntu`, change `/home/ubuntu` to your home directory instead.
{{% /notice %}}

Modify the WORKSPACE file to add the Starlark rules for integrating Bazel with the Android NDK.

First search for:

```
bind(
    name = "python_headers",
    actual = "@local_config_python//:python_headers",
)
```

Replace the lines above with this expanded version:

```

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

Modify the benchmarking tool llm_test (mediapipe/tasks/cc/genai/inference/utils/xnn_utils/llm_test.cc) to specify `encode` as the benchmark method.

Search for this line:

```
std::string, benchmark_method, "decode",
```

And replace with this line:

```
std::string, benchmark_method, "encode",
```

#### Build and run llm_test

```bash

bazel build -c opt --config=android_arm64 mediapipe/tasks/cc/genai/inference/utils/xnn_utils:llm_test

```

Push the resulting binary to the phone:

```bash
adb push bazel-bin/mediapipe/tasks/cc/genai/inference/utils/xnn_utils/llm_test /data/local/tmp/gen_ai
```

{{% notice Note %}}
As before, if you are building from a Docker container, you must first copy the executable from your docker container to your local disk. First find the container ID of your running container by running:

```
docker ps
```

And then replace `[container ID]` in this command with your running container ID:

```
docker cp [container ID]:/home/ubuntu/mediapipe/bazel-bin/mediapipe/tasks/cc/genai/inference/c/llm_test .
```

You can then run

```
adb push llm_test /data/local/tmp/gen_ai
```

To push the binary to your phone.
{{% /notice %}}

Run the binary on the phone:

```bash

./llm_test

```

The output should look like this:

```bash
husky:/data/local/tmp/gen_ai $ ./llm_test
2024-05-28T10:34:30-05:00
Running ./llm_test
Run on (9 X 1704 MHz CPU s)
***WARNING*** CPU scaling is enabled, the benchmark real time measurements may be noisy and will incur extra overhead.
--------------------------------------------------------------------------------------------
Benchmark                                  Time             CPU   Iterations UserCounters...
--------------------------------------------------------------------------------------------
BM_Llm_QCINT8/64/real_time         411403402 ns    407854860 ns            2 items_per_second=155.565/s
BM_Llm_QCINT8/512/real_time       3809387860 ns   3777971777 ns            1 items_per_second=134.405/s
BM_Llm_QCINT8/1024/real_time      9701028244 ns   9591731686 ns            1 items_per_second=105.556/s
BM_Llm_Mixed_INT48/64/real_time    485577962 ns    479829162 ns            2 items_per_second=131.802/s
BM_Llm_Mixed_INT48/512/real_time  3931756309 ns   3877452842 ns            1 items_per_second=130.222/s
BM_Llm_Mixed_INT48/1024/real_time 8480229904 ns   8363190776 ns            1 items_per_second=120.751/s
```

There is a bit of throughput variation that can happen in each iteration of this benchmark, if you want to run multiple times and get a coefficient of variation you can run it like this:

```bash
```bash
./llm_test --benchmark_repetitions=10
```

As you might expect, this will take ten times as long to run, but will give you some nice statistics about the aggregated iterations.