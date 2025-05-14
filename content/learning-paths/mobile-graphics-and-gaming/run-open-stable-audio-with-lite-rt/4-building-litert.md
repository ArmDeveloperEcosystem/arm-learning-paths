---
title: Build LiteRT
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## LiteRT

LiteRT (short for Lite Runtime), formerly known as TensorFlow Lite, is Google's high-performance runtime for on-device AI.

## Build LiteRT libraries

Clone the repository and get the latest modules

```console
cd $WORKSPACE
git clone https://github.com/tensorflow/tensorflow.git tensorflow_src
cd tensorflow_src
```

We will use a specific commit of tensorflow for build so you can checkout and set the `TF_SRC_PATH`:
```bash
git checkout 84dd28bbc29d75e6a6d917eb2998e4e8ea90ec56
export TF_SRC_PATH=$(pwd)
```

We can use `bazel` to build LiteRT libraries, first we use configure script to create a custom configuration for this:

You can now create a custom TFLite build for android:

Ensure the `ANDROID_NDK` variable is set to your previously installed Android NDK:
{{< tabpane code=true >}}
  {{< tab header="Linux">}}
export ANDROID_NDK=$WORKSPACE/android-ndk-r25b/
export PATH=$ANDROID_NDK/toolchains/llvm/prebuilt/linux-x86_64/bin/:$PATH
  {{< /tab >}}
  {{< tab header="MacOS">}}
export TF_CXX_FLAGS="-DTF_MAJOR_VERSION=0 -DTF_MINOR_VERSION=0 -DTF_PATCH_VERSION=0 -DTF_VERSION_SUFFIX=''"
export ANDROID_NDK=~/Library/Android/sdk/ndk/27.0.12077973/
export PATH=$PATH:$ANDROID_NDK/toolchains/llvm/prebuilt/darwin-x86_64/bin
export PATH=$PATH:~/Library/Android/sdk/cmdline-tools/latest/bin
  {{< /tab >}}
{{< /tabpane >}}

Set the TensorFlow version

```bash
export TF_CXX_FLAGS="-DTF_MAJOR_VERSION=0 -DTF_MINOR_VERSION=0 -DTF_PATCH_VERSION=0 -DTF_VERSION_SUFFIX=''"
```


Now you can configure TensorFlow. Here you can set the custom build parameters needed as follows:

```bash { output_lines = "2-14" }
python3 ./configure.py
Please specify the location of python. [Default is $WORKSPACE/bin/python3]:
Please input the desired Python library path to use. Default is [$WORKSPACE/lib/python3.10/site-packages]
Do you wish to build TensorFlow with ROCm support? [y/N]: n
Do you wish to build TensorFlow with CUDA support? [y/N]: n
Do you want to use Clang to build TensorFlow? [Y/n]: n
Would you like to interactively configure ./WORKSPACE for Android builds? [y/N]: y
Please specify the home path of the Android NDK to use. [Default is /home/user/Android/Sdk/ndk-bundle]: /home/user/Workspace/tools/ndk/android-ndk-r25b
Please specify the (min) Android NDK API level to use. [Available levels: [16, 17, 18, 19, 21, 22, 23, 24, 26, 27, 28, 29, 30, 31, 32, 33]] [Default is 21]: 30
Please specify the home path of the Android SDK to use. [Default is /home/user/Android/Sdk]:
Please specify the Android SDK API level to use. [Available levels: ['31', '33', '34', '35']] [Default is 35]:
Please specify an Android build tools version to use. [Available versions: ['30.0.3', '34.0.0', '35.0.0']] [Default is 35.0.0]:
```

Once the bazel configuration is complete, you can build TFLite as follows:
```console
bazel build -c opt --config android_arm64 //tensorflow/lite:libtensorflowlite.so \
    --define tflite_with_xnnpack=true \
    --define=xnn_enable_arm_i8mm=true \
    --define tflite_with_xnnpack_qs8=true \
    --define tflite_with_xnnpack_qu8=true
```

This will produce a `libtensorflowlite.so` shared library for android with XNNPack enabled, which we will use to build the example next.








