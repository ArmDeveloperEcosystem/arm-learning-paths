---
title: Build ONNX Runtime with KleidiAI and SME2 for Android
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build ONNX Runtime with KleidiAI and SME2 for Android

To run this on an Android device, you need to cross-compile ONNX Runtime using the Android NDK.

Before you begin, verify that you have:
- Android NDK version r26b or newer (r27 or later is recommended for the latest SME2 toolchain support)
- CMake and Ninja installed and available in your system PATH

## Build onnxruntime

First, clone the [ONNX Runtime](https://github.com/microsoft/onnxruntime). This Learning Path uses version `v1.23.2`:
```bash
git clone https://github.com/microsoft/onnxruntime.git onnxruntime.git
cd onnxruntime.git/
git checkout v1.23.2
```

Build ONNX Runtime with KleidiAI support enabled. The build script configures cross-compilation for Android arm64-v8a, enables shared library output, and activates KleidiAI integration through the `onnxruntime_USE_KLEIDIAI=ON` flag. Run the following from the root of the ONNX Runtime repository (the `onnxruntime.git/` directory from the previous command):
```bash
./build.sh --android --android_sdk_path $ANDROID_NDK_HOME --android_ndk_path $ANDROID_NDK_HOME --android_abi arm64-v8a --android_api 27 --config RelWithDebInfo --build_shared_lib --cmake_extra_defines onnxruntime_USE_KLEIDIAI=ON --cmake_generator Ninja --parallel
```

{{% notice Note %}}
- The flag `onnxruntime_USE_KLEIDIAI=ON` triggers the inclusion of Arm KleidiAI kernels into the MLAS library.
- The build directory is `build/` by default. This can be overridden with the `--build_dir <path_to_your_build_directory>` command line option to `build.sh`.
{{% /notice %}}

## Profile model performance with onnxruntime_perf_test

Once the build is complete, you will find the `libonnxruntime.so` shared library and `onnxruntime_perf_test` binary in your build directory.

`onnxruntime_perf_test` is essential for measuring latency and identifying bottlenecks of an ONNX model (named `<your_model>.onnx` hereafter). Note that `onnxruntime_perf_test` expects the ONNX model to come with some ancilliary files organized in some directory tree (input data for example).

## Push files to Android device

Transfer the benchmark binary and shared library to your Android device:

```bash
adb push <build_dir>/Android/RelWithDebInfo/onnxruntime_perf_test /data/local/tmp/
adb push <build_dir>/Android/RelWithDebInfo/libonnxruntime.so  /data/local/tmp/
```

## Run the performance test

The `onnxruntime_perf_test` tool simulates inference and gathers statistics. Run a benchmark with 20 iterations:
```bash
# Execute on the device
adb shell "/data/local/tmp/onnxruntime_perf_test -e cpu -m times  -r 20 -s -Z  -x 1 /data/local/tmp/<your_model>/<your_model>.onnx"
```
### Command options explained

The benchmark command uses several flags to control execution:

- `-e cpu`: Use the CPU execution provider
- `-m times`: Run in timing mode to measure latency
- `-r 20`: Repeat the test 20 times for consistent results
- `-Z`: Prevent thread spinning to reduce CPU usage
- `-s`: Display statistics after the run
- `-x 1`: Use a single thread for parallel execution within nodes

You can adjust these settings based on your performance testing needs.

## Deep dive into operator profiling

To see exactly how many milliseconds each operator consumes, use the profiling flag `-p`. This generates a JSON trace file:
```bash
adb shell "/data/local/tmp/onnxruntime_perf_test -p /data/local/tmp/profile.json -e cpu -m times  -r 5 -s -Z  -x 1 /data/local/tmp/<your model>/<your_model>.onnx"
adb pull /data/local/tmp/profile.json
```

The `-p` flag enables performance profiling during the benchmark run. When you provide this flag followed by a filename, ONNX Runtime generates a JSON file containing a detailed trace of model execution.

You can view the results by opening [perfetto tool](https://ui.perfetto.dev/) and loading the generated JSON file. This shows a visual timeline of which operations took the most time. You can also convert the JSON file to a CSV sheet by creating a Python script.
