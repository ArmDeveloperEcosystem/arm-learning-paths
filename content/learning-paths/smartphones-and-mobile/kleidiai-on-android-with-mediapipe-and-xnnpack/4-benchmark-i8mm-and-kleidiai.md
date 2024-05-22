---
title: Benchmarking the Gemma 2B Model with added support for the int4 kernels in KleidiAI via XNNPACK
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Cross-compile the inference engine for CPU again, but this time use the KleidiAI optimizations

Clone XNNPACK and checkout a compatible commit:

```bash

cd ~/

git clone https://github.com/google/XNNPACK.git

cd XNNPACK

git checkout 5ecf0769c54cd224bd0026fe2c8d2ad6f3c4368a

```

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
    path = "$HOME/XNNPACK",
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


Run the updated binary on the phone via `adb shell`:

```bash
./llm_test
```

Witness the performance improvements!

```bash
husky:/data/local/tmp/gen_ai $ ./llm_test
2024-05-15T03:41:31-05:00
Running ./llm_test_kai
Run on (9 X 1704 MHz CPU s)
***WARNING*** CPU scaling is enabled, the benchmark real time measurements may be noisy and will incur extra overhead.
----------------------------------------------------------------------------------
Benchmark                        Time             CPU   Iterations UserCounters...
----------------------------------------------------------------------------------
BM_Llm_QCINT8/64        1871857667 ns   1859813962 ns            1 items_per_second=34.412/s
BM_Llm_QCINT8/512       11721255825 ns   11672066751 ns            1 items_per_second=43.8654/s
BM_Llm_QCINT8/1024      24350844942 ns   24253818321 ns            1 items_per_second=42.2202/s
BM_Llm_Mixed_INT48/64    766656373 ns    760775259 ns            1 items_per_second=84.1247/s
BM_Llm_Mixed_INT48/512  6898854740 ns   6859660724 ns            1 items_per_second=74.6393/s
BM_Llm_Mixed_INT48/1024 16913387133 ns   16810476974 ns            1 items_per_second=60.9144/s
```