---
title: Benchmark the Gemma 2B Model with KleidiAI
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Test inference engine performance with and without i8mm and KleidiAI

Recently Arm has created a set of micro-kernels called [KleidiAI](https://gitlab.arm.com/kleidi/kleidiai) that more efficiently use Arm's i8mm (8-bit integer matrix multiply) processor feature. Arm has worked with the Google AI Edge team to integrate KleidiAI into the MediaPipe framework through XNNPACK. These improvements increase the throughput of quantized LLMs running on Arm chips that contain the i8mm feature.

In this step, you will cross-compile an inference benchmarking executable with and without the i8mm build flag, which will demonstrate the performance gains achieved by using KleidiAI micro-kernels.

#### Check that your device has the i8mm feature

To test whether your phone chipset contains the i8mm feature, run:

```
adb shell cat /proc/cpuinfo | grep i8mm
```

If any lines are returned, then your phone has the i8mm capability.


#### Set up the build

You can choose either 'decode' or 'encode' as the method to benchmark latency. Encode in this context, refers to how many tokens are processed in a second. This affects the time to first token, which is the time needed to process the input from the user. Decode refers to how many tokens are generated in a second. These instructions use 'encode' to benchmark.

Modify the `mediapipe/tasks/cc/genai/inference/utils/xnn_utils/llm_test.cc` file to specify `encode` as the benchmarking method. 

Search for this line:

```
std::string, benchmark_method, "decode",
```

And replace with this line:

```
std::string, benchmark_method, "encode",
```

#### Build and run llm_test 

You can now build the `llm_test` executable. First, lets build it by including support for `i8mm` without KleidiAI micro-kernels:

```bash
bazel build -c opt --config=android_arm64 --define=xnn_enable_arm_i8mm=true --define=xnn_enable_kleidiai=false --dynamic_mode=off mediapipe/tasks/cc/genai/inference/utils/xnn_utils:llm_test
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
docker cp [container ID]:/home/ubuntu/mediapipe/bazel-bin/mediapipe/tasks/cc/genai/inference/utils/xnn_utils/llm_test .
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
2024-02-22T16:11:35-06:00
Running ./llm_test
Run on (9 X 1704 MHz CPU s)
***WARNING*** CPU scaling is enabled, the benchmark real time measurements may be noisy and will incur extra overhead.
--------------------------------------------------------------------------------------------------
Benchmark                                        Time             CPU   Iterations UserCounters...
--------------------------------------------------------------------------------------------------
BM_Llm_QCINT8/512/128/1/real_time        838363322 ns    829751099 ns            1 items_per_second=152.678/s
BM_Llm_QCINT8/512/128/4/real_time        841265137 ns    834988592 ns            1 items_per_second=152.152/s
BM_Llm_QCINT8/512/128/7/real_time        852055258 ns    841642618 ns            1 items_per_second=150.225/s
BM_Llm_QCINT8/512/128/14/real_time       860270793 ns    851762316 ns            1 items_per_second=148.79/s
BM_Llm_QCINT8/512/128/16/real_time       841513062 ns    833101183 ns            1 items_per_second=152.107/s
BM_Llm_QCINT8/512/128/28/real_time       864154582 ns    853668539 ns            1 items_per_second=148.122/s
BM_Llm_QCINT8/512/128/32/real_time       830871257 ns    825545782 ns            1 items_per_second=154.055/s
BM_Llm_QCINT8/512/128/48/real_time       854287110 ns    844283619 ns            1 items_per_second=149.833/s
BM_Llm_QCINT8/512/128/64/real_time       854422201 ns    843630972 ns            1 items_per_second=149.809/s
BM_Llm_Mixed_INT48/512/128/1/real_time   782606446 ns    759264361 ns            1 items_per_second=163.556/s
BM_Llm_Mixed_INT48/512/128/4/real_time   822570557 ns    796060223 ns            1 items_per_second=155.61/s
BM_Llm_Mixed_INT48/512/128/7/real_time   792235759 ns    775831486 ns            1 items_per_second=161.568/s
BM_Llm_Mixed_INT48/512/128/14/real_time  778684611 ns    761880662 ns            1 items_per_second=164.38/s
BM_Llm_Mixed_INT48/512/128/16/real_time  776865235 ns    759403033 ns            1 items_per_second=164.765/s
BM_Llm_Mixed_INT48/512/128/28/real_time  814798707 ns    791258841 ns            1 items_per_second=157.094/s
BM_Llm_Mixed_INT48/512/128/32/real_time  795295655 ns    764343419 ns            1 items_per_second=160.946/s
BM_Llm_Mixed_INT48/512/128/48/real_time  792191082 ns    771217878 ns            1 items_per_second=161.577/s
BM_Llm_Mixed_INT48/512/128/64/real_time  775814250 ns    756604293 ns            1 items_per_second=164.988/s
```

There is a bit of throughput variation that can happen in each iteration of this benchmark, if you want to run multiple times and get a coefficient of variation you can run it like this:

```bash
./llm_test --benchmark_repetitions=10
```

As you might expect, this will take ten times as long to run, but will give you some nice statistics about the aggregated iterations.

#### Build and run llm_test with i8mm and KleidiAI

You can now rebuild `llm_test`, but this time with the i8mm flag enabled:

```bash
bazel build -c opt --config=android_arm64 --define=xnn_enable_arm_i8mm=true --dynamic_mode=off mediapipe/tasks/cc/genai/inference/utils/xnn_utils:llm_test
```
{{% notice Note %}}
When you use "--define=xnn_enable_arm_i8mm=true", the use of KleidiAI micro-kernels is enabled by default. 
{{% /notice %}}


Perform the same steps as before to push the `llm_test` executable to the phone.

Again, run:

```bash
adb shell
cd /data/local/tmp/gen_ai
./llm_test
```

The output should look like this, with performance dramatically improved for the int4/int8 mixed benchmarks:

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

As you can see, by comparing this output to the output in the previous section, the performance improvements are noticeable in the mixed int4/int8 benchmarks. By taking advantage of the KleidiAI micro-kernels, you are able to increase the performance of the i8mm processor feature.

If you would like to learn more about KleidiAI Integration with MediaPipe, please see this [KleidiAI blog post](https://newsroom.arm.com/blog/kleidiai-integration-mediapipe).
