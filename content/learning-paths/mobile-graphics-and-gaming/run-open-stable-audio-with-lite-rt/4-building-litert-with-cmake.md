---
title: Build LiteRT with CMake
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

Create flatbuffers directory and build
```console
mkdir flatc-native-build && cd flatc-native-build
cmake ../tensorflow/lite/tools/cmake/native_tools/flatbuffers
cmake --build .
```

You can now create a custom TFLite build for android:

```console
cd ..
mkdir tflite_build && cd tflite_build
```

Ensure the NDK_PATH is set to your previously installed Android NDK:

```bash
export PATH=$WORKSPACE/android-ndk-r25b/toolchains/llvm/prebuilt/linux-x86_64/bin/:$PATH
export ANDROID_NDK=$WORKSPACE/android-ndk-r25b/
```

Set the TensorFlow version

```bash
export TF_CXX_FLAGS="-DTF_MAJOR_VERSION=0 -DTF_MINOR_VERSION=0 -DTF_PATCH_VERSION=0 -DTF_VERSION_SUFFIX=''"
```

Configure the cmake build for Android including the correct android api and path to previously build flatbuffers directory:

```bash
cmake \
  -DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK/build/cmake/android.toolchain.cmake \
  -DANDROID_ABI=arm64-v8a \
  -DCMAKE_CXX_STANDARD=20 \
  -DTFLITE_HOST_TOOLS_DIR=../flatc-native-build/ \
  ../tensorflow/lite/
```

Finally, build the cmake project after you have configured it:

```bash
cmake --build . -j4
```











