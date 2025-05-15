---
title: Build LiteRT
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## LiteRT

LiteRT (short for Lite Runtime), formerly known as TensorFlow Lite, is Google's high-performance runtime for on-device AI. Designed for low-latency, resource-efficient execution, LiteRT is optimized for mobile and embedded environments — making it a natural fit for Arm CPUs running models lite Stable Audio Open Small. You will build the runtime using the framework using the Bazel build tool.

## Build LiteRT libraries

Clone the repository and get the latest modules

```console
cd $WORKSPACE
git clone https://github.com/tensorflow/tensorflow.git tensorflow_src
cd tensorflow_src
```

Check out the specified commit of TensorFlow, and set the `TF_SRC_PATH`:
```bash
git checkout 84dd28bbc29d75e6a6d917eb2998e4e8ea90ec56
export TF_SRC_PATH=$(pwd)
```

A script is available to configure the `bazel` build environment. Run it to create a custom TFLite build for Android:

{{% notice Reminder %}}
Ensure the `NDK_PATH` variable is set to your previously installed Android NDK:
{{< tabpane code=true >}}
  {{< tab header="Linux">}}
export NDK_PATH=$WORKSPACE/android-ndk-r25b/
export PATH=$NDK_PATH/toolchains/llvm/prebuilt/linux-x86_64/bin/:$PATH
  {{< /tab >}}
  {{< tab header="MacOS">}}
export NDK_PATH=~/Library/Android/android-ndk-r25b
export PATH=$PATH:$NDK_PATH/toolchains/llvm/prebuilt/darwin-x86_64/bin
export PATH=$PATH:~/Library/Android/sdk/cmdline-tools/latest/bin
  {{< /tab >}}
{{< /tabpane >}}
{{% /notice  %}}

The configuration script is interactive. Run it using the command below, and use the table to set the parameters for this Learning Path use-case.

```bash
python3 ./configure.py
```

|Question|Input|
|---|---|
|Please specify the location of python. [Default is $WORKSPACE/bin/python3]:| Enter (default) |
|Please input the desired Python library path to use[$WORKSPACE/lib/python3.10/site-packages] | Enter |
|Do you wish to build TensorFlow with ROCm support? [y/N]|N (No)|
|Do you wish to build TensorFlow with CUDA support?|N|
|Do you want to use Clang to build TensorFlow? [Y/n]|N|
|Would you like to interactively configure ./WORKSPACE for Android builds? [y/N]|y (Yes) |
|Please specify the home path of the Android NDK to use. [Default is /home/user/Android/Sdk/ndk-bundle]| Enter |
|Please specify the (min) Android NDK API level to use. [Default is 21] | 27 |
|Please specify the home path of the Android SDK to use. [Default is /home/user/Android/Sdk]| Enter |
|Please specify the Android SDK API level to use.  [Default is 35]| Enter |
|Please specify an Android build tools version to use.  [Default is 35.0.0]| Enter |
|Do you wish to build TensorFlow with iOS support? [y/N]:| n |

Once the Bazel configuration is complete, you can build TFLite as follows:

```console
bazel build -c opt --config android_arm64 //tensorflow/lite:libtensorflowlite.so \
    --define tflite_with_xnnpack=true \
    --define=xnn_enable_arm_i8mm=true \
    --define tflite_with_xnnpack_qs8=true \
    --define tflite_with_xnnpack_qu8=true
```

The final step is to build flatbuffers used by the application:
```
cd $WORKSPACE/tensorflow_src
mkdir flatc-native-build && cd flatc-native-build
cmake ../tensorflow/lite/tools/cmake/native_tools/flatbuffers
cmake --build .
```

With flatbuffers and LiteRT built, you can now build the application for Android devices.








