---
title: Benchmark the Gemma 2B Model using Android NDK r25 with and without KleidiAI
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Test inference engine performance with and without i8mm and KleidiAI

Recently Arm has created a set of micro-kernels called "KleidiAI" that more efficiently use Arm's i8mm (8-bit integer matrix multiply) processor feature. These improvements increase the throughput of quantized LLMs running on Arm chips that contain the i8mm feature.

In this step, you will cross-compile an inference benchmarking executable with and without the i8mm build flag, which will give you an understanding of the performance gains attained by using KleidiAI micro-kernels.

#### Check that your device has the i8mm feature

To test whether your phone chipset contains the i8mm feature, run

```
adb shell cat /proc/cpuinfo | grep i8mm
```

If any lines are returned, then your phone has the i8mm capability.


#### Set up the build

Download Android NDK r25. Mediapipe only supports up to NDK r21, which does not have support for i8mm instructions. Google has released a workaround that lets us build the binary with NDK r25 (with support for i8mm instructions) by modifying the WORKSPACE file at the root of the MediaPipe repo to use `rules_android_ndk`.

```bash

cd $HOME/Android/Sdk/ndk-bundle/

wget https://dl.google.com/android/repository/android-ndk-r25c-linux.zip

unzip android-ndk-r25c-linux.zip

```

Add NDK bin folder to your PATH variable:

```bash

export PATH=$PATH:$HOME/Android/Sdk/ndk-bundle/android-ndk-r25c/toolchains/llvm/prebuilt/linux-x86_64/bin/

```

Modify the Mediapipe WORKSPACE file to add the path to Android NDK r25:

```bash

android_ndk_repository(name = "androidndk", api_level=30, path="/home/ubuntu/Android/Sdk/ndk-bundle/android-ndk-r25c")

android_sdk_repository(name = "androidsdk", path = "/home/ubuntu/Android/Sdk")

```

{{% notice Note %}}
The functions above require absolute paths, so if your `$HOME` directory is not `/home/ubuntu`, change `/home/ubuntu` to your home directory instead.
{{% /notice %}}

Modify the Mediapipe WORKSPACE file to add the Starlark rules for integrating Bazel with Android NDK.

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

Modify the `mediapipe/tasks/cc/genai/inference/utils/xnn_utils/llm_test.cc` file to specify `encode` as the benchmarking method.

Search for this line:

```
std::string, benchmark_method, "decode",
```

And replace with this line:

```
std::string, benchmark_method, "encode",
```
#### Build and run llm_test without i8mm and KleidiAI

```bash
bazel build -c opt --config=android_arm64 --dynamic_mode=off mediapipe/tasks/cc/genai/inference/utils/xnn_utils:llm_test
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

Run the binary on the phone via `adb shell`:

```bash
adb shell
cd /data/local/tmp/gen_ai
./llm_test
```

The output should look like this:

```bash
husky:/data/local/tmp/gen_ai $ ./llm_test
2024-02-21T20:17:09-06:00
Running ./llm_test
Run on (9 X 1704 MHz CPU s)
***WARNING*** CPU scaling is enabled, the benchmark real time measurements may be noisy and will incur extra overhead.
--------------------------------------------------------------------------------------------------
Benchmark                                        Time             CPU   Iterations UserCounters...
--------------------------------------------------------------------------------------------------
BM_Llm_QCINT8/512/128/1/real_time       1003557414 ns    987891597 ns            1 items_per_second=127.546/s
BM_Llm_QCINT8/512/128/4/real_time       1032959636 ns   1015699095 ns            1 items_per_second=123.916/s
BM_Llm_QCINT8/512/128/7/real_time       1048154704 ns   1031147568 ns            1 items_per_second=122.119/s
BM_Llm_QCINT8/512/128/14/real_time      1093941773 ns   1076049151 ns            1 items_per_second=117.008/s
BM_Llm_QCINT8/512/128/16/real_time      1045623292 ns   1037152577 ns            1 items_per_second=122.415/s
BM_Llm_QCINT8/512/128/28/real_time      1059079712 ns   1044604110 ns            1 items_per_second=120.86/s
BM_Llm_QCINT8/512/128/32/real_time      1087658611 ns   1077976514 ns            1 items_per_second=117.684/s
BM_Llm_QCINT8/512/128/48/real_time      1087161580 ns   1078361074 ns            1 items_per_second=117.738/s
BM_Llm_QCINT8/512/128/64/real_time      1072282227 ns   1060130805 ns            1 items_per_second=119.372/s
BM_Llm_Mixed_INT48/512/128/1/real_time  1155142457 ns   1114548822 ns            1 items_per_second=110.809/s
BM_Llm_Mixed_INT48/512/128/4/real_time  1130182496 ns   1095820501 ns            1 items_per_second=113.256/s
BM_Llm_Mixed_INT48/512/128/7/real_time  1167092530 ns   1128940055 ns            1 items_per_second=109.674/s
BM_Llm_Mixed_INT48/512/128/14/real_time 1165201458 ns   1145621858 ns            1 items_per_second=109.852/s
BM_Llm_Mixed_INT48/512/128/16/real_time 1173947022 ns   1125000126 ns            1 items_per_second=109.034/s
BM_Llm_Mixed_INT48/512/128/28/real_time 1147032837 ns   1104482669 ns            1 items_per_second=111.592/s
BM_Llm_Mixed_INT48/512/128/32/real_time 1138706178 ns   1095870886 ns            1 items_per_second=112.408/s
BM_Llm_Mixed_INT48/512/128/48/real_time 1188765625 ns   1160558175 ns            1 items_per_second=107.675/s
BM_Llm_Mixed_INT48/512/128/64/real_time 1189585776 ns   1136016289 ns            1 items_per_second=107.6/s
```

There is a bit of throughput variation that can happen in each iteration of this benchmark, if you want to run multiple times and get a coefficient of variation you can run it like this:

```bash
./llm_test --benchmark_repetitions=10
```

As you might expect, this will take ten times as long to run, but will give you some nice statistics about the aggregated iterations.

#### Build and run llm_test with i8mm and KleidiAI

Rebuild llm_test but this time with the i8mm flag enabled:

```bash
bazel build -c opt --config=android_arm64 --define=xnn_enable_arm_i8mm=true --dynamic_mode=off mediapipe/tasks/cc/genai/inference/utils/xnn_utils:llm_test
```
{{% notice Note %}}
When you use "--define=xnn_enable_arm_i8mm=true", the use of KleidiAI micro-kernels is enabled by default. 
{{% /notice %}}


Perform the same steps as before to push the `llm_test` executable to the phone.

Again, run

```bash
adb shell
cd /data/local/tmp/gen_ai
./llm_test
```

The output should look like this, with performance dramatically improved in the int4/int8 mixed benchmarks:

```bash
husky:/data/local/tmp/gen_ai $ ./llm_test
2024-02-21T20:22:24-06:00
Running ./llm_test
Run on (9 X 1704 MHz CPU s)
***WARNING*** CPU scaling is enabled, the benchmark real time measurements may be noisy and will incur extra overhead.
--------------------------------------------------------------------------------------------------
Benchmark                                        Time             CPU   Iterations UserCounters...
--------------------------------------------------------------------------------------------------
BM_Llm_QCINT8/512/128/1/real_time        878131633 ns    869451284 ns            1 items_per_second=145.764/s
BM_Llm_QCINT8/512/128/4/real_time        861170695 ns    850807124 ns            1 items_per_second=148.635/s
BM_Llm_QCINT8/512/128/7/real_time        844140096 ns    837621854 ns            1 items_per_second=151.634/s
BM_Llm_QCINT8/512/128/14/real_time       833818278 ns    827093253 ns            1 items_per_second=153.511/s
BM_Llm_QCINT8/512/128/16/real_time       825771973 ns    819266606 ns            1 items_per_second=155.006/s
BM_Llm_QCINT8/512/128/28/real_time       906640219 ns    895908902 ns            1 items_per_second=141.181/s
BM_Llm_QCINT8/512/128/32/real_time       815335613 ns    809224814 ns            1 items_per_second=156.991/s
BM_Llm_QCINT8/512/128/48/real_time       939988810 ns    925805136 ns            1 items_per_second=136.172/s
BM_Llm_QCINT8/512/128/64/real_time       867672364 ns    861572060 ns            1 items_per_second=147.521/s
BM_Llm_Mixed_INT48/512/128/1/real_time   649379069 ns    643777214 ns            1 items_per_second=197.111/s
BM_Llm_Mixed_INT48/512/128/4/real_time   639673380 ns    633901237 ns            1 items_per_second=200.102/s
BM_Llm_Mixed_INT48/512/128/7/real_time   625728760 ns    620227580 ns            1 items_per_second=204.561/s
BM_Llm_Mixed_INT48/512/128/14/real_time  630814657 ns    624941732 ns            1 items_per_second=202.912/s
BM_Llm_Mixed_INT48/512/128/16/real_time  616205852 ns    610839353 ns            1 items_per_second=207.723/s
BM_Llm_Mixed_INT48/512/128/28/real_time  622859253 ns    617623170 ns            1 items_per_second=205.504/s
BM_Llm_Mixed_INT48/512/128/32/real_time  628669597 ns    622151198 ns            1 items_per_second=203.605/s
BM_Llm_Mixed_INT48/512/128/48/real_time  631355876 ns    626120761 ns            1 items_per_second=202.738/s
BM_Llm_Mixed_INT48/512/128/64/real_time  633293213 ns    628101344 ns            1 items_per_second=202.118/s
```

And as in the previous section, if you want to run multiple times and get a coefficient of variation you can run it like this:

```bash
./llm_test --benchmark_repetitions=10
```

As you can see by comparing this output to the output in the previous section, these performance improvements are only noticeable in the mixed int4/int8 benchmarks. These improvements are due to more efficient use of the Arm i8mm instructions when using int4 quantization, by packing two int4 weights into a single 8-bit memory space. This allows KleidiAI to get more performance out of the i8mm processor feature.

If you'd like to learn more about KleidiAI, please check out the [KleidiAI announcement blog post](https://newsroom.arm.com/blog/arm-kleidi).
