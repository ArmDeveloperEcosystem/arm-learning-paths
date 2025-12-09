---
title: Build the LiteRT benchmark tool
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Build the LiteRT benchmark tool with KleidiAI and SME2 enabled

LiteRT provides provides a standalone performance measurement utility called `benchmark_model` for evaluating the performance of LiteRT models. 

In this section, you will build two versions of the benchmark tool:
  * With KleidiAI + SME/SME2 enabled → uses Arm-optimized micro-kernels
  * Without KleidiAI + SME/SME2 → baseline performance (NEON/SVE2 fallback)
This comparison clearly demonstrates the gains provided by SME2 acceleration.

First, clone the LiteRT repository.

``` bash
cd $WORKSPACE
git clone https://github.com/google-ai-edge/LiteRT.git
```
Because LiteRT integrates KleidiAI through XNNPACK, you must build LiteRT from source to enable SME2 micro-kernels.

Next, set up your Android build environment using Docker on your Linux developement machine.
Google provides a Dockerfile that installs the toolchain needed for TFLite/LiteRT Android builds.

Download the Dockerfile:
``` bash
wget https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/lite/tools/tflite-android.Dockerfile
```
Build the Docker image:
```bash
docker build . -t tflite-builder -f tflite-android.Dockerfile
```
The Docker image includes Bazel, NDK, CMake, toolchains, and Python required for cross-compiling Android binaries.

You will now install Android SDK/NDK Components inside the Container.
Launch the docker container:
```bash
docker run -it -v $PWD:/host_dir tflite-builder bash
```
Install Android platform tools:
``` bash
sdkmanager \
  "build-tools;${ANDROID_BUILD_TOOLS_VERSION}" \
  "platform-tools" \
  "platforms;android-${ANDROID_API_LEVEL}"
```

Configure LiteRT Build Options inside your running container:

``` bash
cd /host_dir/LiteRT
./configure
```

Use default values for all the prompts except when prompted:
```output
Would you like to interactively configure ./WORKSPACE for Android builds? [y/N]
```
Type in `y`.

LiteRT's configuration script will detect SDK + NDK paths, set toolchain versions, configure Android ABI (arm64-v8a) and initialize Bazel workspace rules.

Now, you can build the benchmark tool with KleidiAI + SME2 Enabled.

Enable XNNPACK, quantization paths, and SME2 acceleration:
``` bash
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

This build enables the KleidiAI and SME2 micro-kernels integrated into XNNPACK and produces an Android binary under:

```output
bazel-bin/litert/tools/benchmark_model
```

### Build the LiteRT benchmark tool without KleidiAI (Baseline Comparison)

To compare the performance of KleidiAI SME2 implementation against XNNPACK’s original implementation, you can build another version of LiteRT benchmark tool without KleidiAI and SME2 enabled.

``` bash
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
This build of the `benchmark_model` disables all SME2 micro-kernels and forces fallback to XNNPACK’s NEON/SVE2 kernels.
You can then use ADB to push the benchmark tool to your Android device.

```bash
adb push bazel-bin/litert/tools/benchmark_model /data/local/tmp/
adb shell chmod +x /data/local/tmp/benchmark_model
```
