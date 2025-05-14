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
{{< tabpane code=true >}}
  {{< tab header="Linux">}}
export PATH=$WORKSPACE/android-ndk-r25b/toolchains/llvm/prebuilt/linux-x86_64/bin/:$PATH
export ANDROID_NDK=$WORKSPACE/android-ndk-r25b/
  {{< /tab >}}
  {{< tab header="MacOS">}}
nano ~/.zshrc
export PATH=$PATH:~/Library/Android/sdk/ndk/27.0.12077973/toolchains/llvm/prebuilt/darwin-x86_64/bin
export PATH=$PATH:~/Library/Android/sdk/cmdline-tools/latest/bin
source ~/.zshrc
  {{< /tab >}}
{{< /tabpane >}}

Set the TensorFlow version

```bash
export TF_CXX_FLAGS="-DTF_MAJOR_VERSION=0 -DTF_MINOR_VERSION=0 -DTF_PATCH_VERSION=0 -DTF_VERSION_SUFFIX=''"
```

Configure the cmake build for Android including the correct android api and path to previously build flatbuffers directory:

{{< tabpane code=true >}}
  {{< tab header="Android">}}
```console
cmake \
  -DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK/build/cmake/android.toolchain.cmake \
  -DANDROID_ABI=arm64-v8a \
  -DCMAKE_CXX_STANDARD=20 \
  -DTFLITE_HOST_TOOLS_DIR=../flatc-native-build/ \
  ../tensorflow/lite/
cmake --build .
```
  {{< /tab >}}
  {{< tab header="MacOS">}}
cmake -DCMAKE_C_FLAGS="${TF_CXX_FLAGS}" -DCMAKE_CXX_FLAGS="${TF_CXX_FLAGS}" -DTFLITE_HOST_TOOLS_DIR=../flatc-native-build/ ../tensorflow_src/tensorflow/lite/examples/minimal
cmake --build .
  {{< /tab >}}
{{< /tabpane >}}

Finally, build the cmake project after you have configured it:

```bash
cmake --build . -j4
```











