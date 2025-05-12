---
title: Build LiteRT with CMake
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## LiteRT

LiteRT (short for Lite Runtime), formerly known as TensorFlow Lite, is Google's high-performance runtime for on-device AI.

TODO: more on LiteRT or links? Reason why we will convert the model or is it clear?


## Build LiteRT libraries

Clone the repository and get the latest modules

```console
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
```console
export ANDROID_NDK=/home/$USER/Android/Sdk/ndk/25.1.8937393/
```

Configure the cmake build for Android including the correct android api and path to previously build flatbuffers directory
```console
cmake -DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK/build/cmake/android.toolchain.cmake -DANDROID_ABI=arm64-v8a -DTFLITE_HOST_TOOLS_DIR=../flatc-native-build/ ../tensorflow/lite/
cmake --build .
```




 







