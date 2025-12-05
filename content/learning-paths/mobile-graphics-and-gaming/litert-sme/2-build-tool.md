---
title: Build the LiteRT benchmark tool
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

### Build the LiteRT benchamrk tool with KleidiAI and SME2 enabled

LiteRT provides a tool called `benchmark_model` for evaluating the performance of LiteRT models. Use the following steps to build the LiteRT benchamrk tool.

First, clone the LiteRT repository.

``` bash
cd $WORKSPACE
git clone https://github.com/google-ai-edge/LiteRT.git
```

Then, set up build environment using Docker in your Linux developement machine.

``` bash
wget https://raw.githubusercontent.com/tensorflow/tensorflow/master/tensorflow/lite/tools/tflite-android.Dockerfile
docker build . -t tflite-builder -f tflite-android.Dockerfile
```

Inside the container, run the following commands to download Android tools and libraries to build LiteRT for Android.

``` bash
docker run -it -v $PWD:/host_dir tflite-builder bash
sdkmanager \
  "build-tools;${ANDROID_BUILD_TOOLS_VERSION}" \
  "platform-tools" \
  "platforms;android-${ANDROID_API_LEVEL}"
```

Inside the LiteRT source, run the script to configure the bazel paramters.

``` bash
cd /host_dir/LiteRT
./configure
```

You can keep all options at their default values except for:

`Would you like to interactively configure ./WORKSPACE for Android builds? [y/N]`

Type in `y`, then the script will automatically detect the necessary files set up in the sdkmanager command and configure them accordingly.

Now, you can build the benchmark tool with the following commands.

``` bash
export BENCHMARK_TOOL_PATH="litert/tools:benchmark_model"
export XNNPACK_OPTIONS="--define tflite_with_xnnpack=true \
--define=tflite_with_xnnpack_qs8=true \
--define=tflite_with_xnnpack_qu8=true \
--define=tflite_with_xnnpack_dynamic_fully_connected=true \
--define=xnn_enable_arm_sme=true \
--define=xnn_enable_arm_sme2=true \
--define=xnn_enable_kleidiai=true"

bazel build -c opt --config=android_arm64 \
${XNNPACK_OPTIONS} "${BENCHMARK_TOOL_PATH}" \
--repo_env=HERMETIC_PYTHON_VERSION=3.12
```

The above build enables the KleidiAI and SME2 micro-kernels integrated into XNNPACK.


### Build the LiteRT benchamrk tool without KleidiAI

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

bazel build -c opt --config=android_arm64 \
${XNNPACK_OPTIONS} "${BENCHMARK_TOOL_PATH}" \
--repo_env=HERMETIC_PYTHON_VERSION=3.12
```

The path to the compiled benchmark tool binary will be displayed in the build output.
You can then use ADB to push the benchmark tool to your Android device.
