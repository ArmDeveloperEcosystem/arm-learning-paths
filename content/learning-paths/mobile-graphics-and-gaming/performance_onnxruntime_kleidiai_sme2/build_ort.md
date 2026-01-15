---
title: Build ONNX Runtime with KleidiAI and SME2 for Android
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build ONNX Runtime and benchmark application with KleidiAI and SME2 support for Android

To run this on an Android device, you must cross-compile ORT using the Android NDK.

Prerequisites:
-	Android NDK: Version r26b or newer (r27+ recommended for latest SME2 toolchain support).
-	CMake & Ninja: Ensure these are in your system PATH.

### Build `onnxruntime`

First, clone the [ONNX Runtime](https://github.com/microsoft/onnxruntime). This learning path uses version `v1.23.2`:
```bash
git clone https://github.com/microsoft/onnxruntime.git onnxruntime.git
cd onnxruntime.git/
git checkout v1.23.2
```

Then run the following from the root of the ONNX Runtime repository (the `onnxruntime.git/` directory from the previous command):
```bash
./build.sh --android --android_sdk_path $ANDROID_NDK_HOME --android_ndk_path $ANDROID_NDK_HOME --android_abi arm64-v8a --android_api 27 --config RelWithDebInfo --build_shared_lib --cmake_extra_defines onnxruntime_USE_KLEIDIAI=ON --cmake_generator Ninja --parallel
```

Notes:
- The flag `onnxruntime_USE_KLEIDIAI=ON` triggers the inclusion of Arm KleidiAI kernels into the MLAS library.
- The build directory is `build/` by default. This can be overriden with the `--build_dir <path_to_your_build_directory>` commande line option to `build.sh`

## Profiling Performance with onnxruntime_perf_test
Once the build is complete, you will find the `libonnxruntime.so` shared library and `onnxruntime_perf_test` binary in your build directory.

`onnxruntime_perf_test` is essential for measuring latency and identifying bottlenecks of an ONNX model (named `<your_model>.onnx` hereafter). Note that `onnxruntime_perf_test` expects the ONNX model to come with some ancilliary files organized in some directory tree (input data for example).

### Step 1: Push files to Android Device
```bash
adb push <build_dir>/Android/RelWithDebInfo/onnxruntime_perf_test /data/local/tmp/
adb push <build_dir>/Android/RelWithDebInfo/libonnxruntime.so  /data/local/tmp/
```

### Step 2: Run the Performance Test
The `onnxruntime_perf_test` tool allows you to simulate inference and gather statistics. For example,
```bash
# Execute on the device
adb shell "/data/local/tmp/onnxruntime_perf_test -e cpu -m times  -r 20 -s -Z  -x 1 /data/local/tmp/<your_model>/<your_model>.onnx"
```

The command example set the arguments of the application as,
-	`-e cpu` specifies the provider as cpu provider
-	`-m times` specifies the test mode as “times”
-	`-r 20` specifies the repeated times as 20
-	`-Z` disallows thread from spinning during runs to reduce cpu usage
-	`-s` shows statistics result
-	`-x 1` sets the number of threads used to parallelize the execution within nodes as 1

You can try other arguments setting if you would like to.

### Step 3: Deep Dive into Operator Profiling
To see exactly how many milliseconds are spent on each operator, use the profiling flag `-p`.
```bash
adb shell "/data/local/tmp/onnxruntime_perf_test -p /data/local/tmp/profile.json -e cpu -m times  -r 5 -s -Z  -x 1 /data/local/tmp/<your model>/<your_model>.onnx"
adb pull /data/local/tmp/profile.json
```

The argument `-p` enables performance profiling during the benchmark run. When you provide this flag followed by a filename, ONNX Runtime will generate a JSON file containing a detailed trace of the model execution.
You can view the results by opening [perfetto tool]( https://ui.perfetto.dev/), and loading the generated JSON file. This allows you to see a visual timeline of which operations took the most time.
You also can convert the JSON file to a CSV sheet by creating a python script.
