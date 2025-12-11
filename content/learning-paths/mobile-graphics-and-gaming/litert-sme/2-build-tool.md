---
title: Build the LiteRT benchmark tool
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build the LiteRT benchmark tool with KleidiAI and SME2 enabled

LiteRT provides a standalone performance measurement utility called `benchmark_model` for evaluating the performance of LiteRT models.

In this section, you will build two versions of the benchmark tool:
- With KleidiAI and Scalable Matrix Extension version 2 (SME2) enabled, which uses Arm-optimized micro-kernels
- Without KleidiAI and SME2, which provides baseline performance using NEON or SVE2 fallback

This comparison demonstrates the performance gains provided by SME2 acceleration.

First, clone the LiteRT repository:

```bash
cd $WORKSPACE
git clone https://github.com/google-ai-edge/LiteRT.git
```

Because LiteRT integrates KleidiAI through XNNPACK (an open-source library providing highly optimized neural-network operators), you must build LiteRT from source to enable SME2 micro-kernels.

Next, set up your Android build environment using Docker on your Linux development machine. Google provides a Dockerfile that installs the toolchain needed for TensorFlow Lite (TFLite)/LiteRT Android builds.

Download the Dockerfile:

```bash
wget https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/lite/tools/tflite-android.Dockerfile
```

Build the Docker image:

```bash
docker build . -t tflite-builder -f tflite-android.Dockerfile
```

The Docker image includes Bazel, Android Native Development Kit (NDK), CMake, toolchains, and Python required for cross-compiling Android binaries.

Now, install Android Software Development Kit (SDK) and NDK components inside the container.

Launch the Docker container:

```bash
docker run -it -v $PWD:/host_dir tflite-builder bash
```

Install Android platform tools:

```bash
sdkmanager \
  "build-tools;${ANDROID_BUILD_TOOLS_VERSION}" \
  "platform-tools" \
  "platforms;android-${ANDROID_API_LEVEL}"
```

Configure LiteRT build options inside your running container:

```bash
cd /host_dir/LiteRT
./configure
```

Use default values for all prompts except when asked:

```output
Would you like to interactively configure ./WORKSPACE for Android builds? [y/N]
```

Type `y` and press Enter.

LiteRT's configuration script will detect SDK and NDK paths, set toolchain versions, configure the Android Application Binary Interface (ABI) to arm64-v8a, and initialize Bazel workspace rules.

Now, you can build the benchmark tool with KleidiAI and SME2 enabled.

Enable XNNPACK, quantization paths, and SME2 acceleration:

```bash
export BENCHMARK_TOOL_PATH="litert/tools:benchmark_model"
export XNNPACK_OPTIONS="--define tflite_with_xnnpack=true \
--define=tflite_with_xnnpack_qs8=true \
--define=tflite_with_xnnpack_qu8=true \
--define=tflite_with_xnnpack_dynamic_fully_connected=true \
--define=xnn_enable_arm_sme=true \
--define=xnn_enable_arm_sme2=true \
--define=xnn_enable_kleidiai=true"
```

Build for Android:

```bash
bazel build -c opt --config=android_arm64 \
${XNNPACK_OPTIONS} "${BENCHMARK_TOOL_PATH}" \
--repo_env=HERMETIC_PYTHON_VERSION=3.12
```

This build enables the KleidiAI and SME2 micro-kernels integrated into XNNPACK and produces an Android binary at:

```output
bazel-bin/litert/tools/benchmark_model
```

## Build the LiteRT benchmark tool without KleidiAI (baseline comparison)

To compare the performance of the KleidiAI SME2 implementation against XNNPACK’s original implementation, build another version of the LiteRT benchmark tool without KleidiAI and SME2 enabled.

Set the build options to disable SME2 and KleidiAI:

```bash
export BENCHMARK_TOOL_PATH="litert/tools:benchmark_model"
export XNNPACK_OPTIONS="--define tflite_with_xnnpack=true \
--define=tflite_with_xnnpack_qs8=true \
--define=tflite_with_xnnpack_qu8=true \
--define=tflite_with_xnnpack_dynamic_fully_connected=true \
--define=xnn_enable_arm_sme=false \
--define=xnn_enable_arm_sme2=false \
--define=xnn_enable_kleidiai=false"
```

Then rebuild:

```bash
bazel build -c opt --config=android_arm64 \
${XNNPACK_OPTIONS} "${BENCHMARK_TOOL_PATH}" \
--repo_env=HERMETIC_PYTHON_VERSION=3.12
```

This build of the `benchmark_model` disables all SME2 micro-kernels and forces fallback to XNNPACK’s NEON or SVE2 kernels.

You can then use Android Debug Bridge (ADB) to push the benchmark tool to your Android device:

```bash
adb push bazel-bin/litert/tools/benchmark_model /data/local/tmp/
adb shell chmod +x /data/local/tmp/benchmark_model
```

You have now built both versions of the LiteRT benchmark tool. You are ready to benchmark and compare SME2-accelerated and baseline performance on your Arm-based Android device.
