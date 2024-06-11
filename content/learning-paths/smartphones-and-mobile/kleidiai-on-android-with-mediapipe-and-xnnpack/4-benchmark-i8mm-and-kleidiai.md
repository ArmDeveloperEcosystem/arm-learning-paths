---
title: Benchmarking the Gemma 2B Model with added support for the int4 kernels in KleidiAI via XNNPACK
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Cross-compile the inference engine for CPU again, but this time use the KleidiAI optimizations

Recently Arm has created a set of micro-kernels called "KleidiAI" that more efficiently use Arm's i8mm (8-bit integer matrix multiply) processor feature. These improvements will increase the throughput of quantized LLMs running on Arm chips that contain the i8mm feature.

To build the KleidiAI optimizations into your applications, first clone XNNPACK and checkout a compatible commit:

```bash

cd ~/

git clone https://github.com/google/XNNPACK.git

cd XNNPACK

git checkout 5ecf0769c54cd224bd0026fe2c8d2ad6f3c4368a

```

TODO: REMOVE THESE PATCH INSTRUCTIONS WHEN KLEIDIAI HAS BEEN MERGED

Apply kleidiAI patch:

```bash

git apply kleidiai_prototype.patch -v

```

Apply MediaPipe patch:

```bash

cd ~/mediapipe

git apply mediapipe_change.patch -v

```

Now update the XNNPack repo being used by Bazel in your WORKSPACE file:

Replace

```bash
http_archive(
    name = "XNNPACK",
    # `curl -L <url> | shasum -a 256`
    sha256 = "179a680ef85deb5380b850f2551b214e00835c232f5b197dedf7c011a6adf5a6",
    strip_prefix = "XNNPACK-2fe25b859581a34e77b48b06c640ac1a5a58612e",
    url = "https://github.com/google/XNNPACK/archive/2fe25b859581a34e77b48b06c640ac1a5a58612e.zip",
)
```

With:

```bash
local_repository(
    name = "XNNPACK",
    path = "../XNNPACK",
    repo_mapping = {"@com_google_benchmark": "@google_benchmark"}
)
```

Changing the path to the path of your patched XNNPACK repo.


Rebuild llm_test with these changes:

```bash
bazel build -c opt --config=android_arm64 mediapipe/tasks/cc/genai/inference/utils/xnn_utils:llm_test
```

Push the resulted binary to the phone using ADB:


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

Run the updated binary on the phone via `adb shell`:

```bash
./llm_test
```

Witness the performance improvements!

```bash
husky:/data/local/tmp/gen_ai $ ./llm_test
2024-05-28T10:27:27-05:00
Running ./llm_test
Run on (9 X 1704 MHz CPU s)
***WARNING*** CPU scaling is enabled, the benchmark real time measurements may be noisy and will incur extra overhead.
--------------------------------------------------------------------------------------------
Benchmark                                  Time             CPU   Iterations UserCounters...
--------------------------------------------------------------------------------------------
BM_Llm_QCINT8/64/real_time         435261231 ns    431100073 ns            2 items_per_second=147.038/s
BM_Llm_QCINT8/512/real_time       4351431155 ns   4311715132 ns            1 items_per_second=117.662/s
BM_Llm_QCINT8/1024/real_time      9629629440 ns   9532388833 ns            1 items_per_second=106.338/s
BM_Llm_Mixed_INT48/64/real_time    350508464 ns    346436742 ns            2 items_per_second=182.592/s
BM_Llm_Mixed_INT48/512/real_time  3184487632 ns   3155323312 ns            1 items_per_second=160.779/s
BM_Llm_Mixed_INT48/1024/real_time 6848890710 ns   6748597814 ns            1 items_per_second=149.513/s
```

And as in the previous section, if you want to run multiple times and get a coefficient of variation you can run it like this:

```bash
```bash
./llm_test --benchmark_repetitions=10
```

As you can see by comparing this output to the output in the previous section, these performance improvements are only noticeable in the mixed int4/int8 benchmarks. These improvements are due to more efficient use of the Arm i8mm instructions when using int4 quantization, by packing two int4 weights into a single 8-bit memory space. This allows KleidiAI to get more performance out of the i8mm processor feature.

If you'd like to learn more about KleidiAI, please check out the (KleidiAI announcement blog post)[https://newsroom.arm.com/blog/arm-kleidi].