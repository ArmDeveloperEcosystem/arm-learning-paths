---
title: Create a simple program
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create and build a simple program

We now set up a simple program to run the inference on all three submodules on an Android device, this will take in a text prompt and generate an audio file.
You can clone the needed sample files as follows:
```bash
cd $WORKSPACE/audio-stale-open-litert/app
mkdir build && cd build
```

Create flatbuffers directory and build
```console
mkdir flatc-native-build && cd flatc-native-build
cmake ../tensorflow/lite/tools/cmake/native_tools/flatbuffers
cmake --build .
```

Ensure the NDK path is set correctly and build with cmake:
```bash
cmake -B build -DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK/build/cmake/android.toolchain.cmake \
	       -DANDROID_ABI=arm64-v8a -DANDROID_PLATFORM=android-26 \
 	       -DTF_INCLUDE_PATH=$WORKSPACE/tensorflow_src \
 	       -DTF_LIB_PATH=$WORKSPACE/tensorflow_src/audio-gen-build/tensorflow-lite/ \
 	       -DFLATBUFFER_INCLUDE_PATH=$WORKSPACE/tensorflow_src/flatc-native-build/flatbuffers/include

cmake --build build

```

Once the SAO example built sucessfully, this is a binary file named audiogen_main has been created, we will use adb (Android Debug Bridge) to push the needed example to the device:

```bash
adb shell
```

Create a directory for all neded resources:
```bash
cd /data/local/tmp
mkdir audiogen
```
Push all necessary files into newly created audiogen folder on Android.
```bash
cd sao_litert
adb push runner/build/audiogen_main /data/local/tmp/audiogen
adb push dit.tflite /data/local/tmp/audiogen
adb push autoencoder_model.tflite /data/local/tmp/audiogen
adb push conditioners_tflite/conditioners_float32.tflite /data/local/tmp/audiogen
```bash

Go into the shell again to run the simple program:
```adb shell

```

