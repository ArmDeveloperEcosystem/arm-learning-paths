---
title: Create a simple program
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create and build a simple program

We can now set up a simple program and build it with CMake. Firstly we will need flatbuffers

```console
git clone https://github.com/google/flatbuffers.git
cd flatbuffers
git checkout v24.3.25
```

https://git.research.arm.com/gen-ai/sai/audio-stale-open-litert/-/blob/main/runner/

```
cmake -DCMAKE_TOOLCHAIN_FILE=$ANDROID_NDK/build/cmake/android.toolchain.cmake .. \
      -DANDROID_ABI=arm64-v8a \
      -DANDROID_PLATFORM=android-26 \
      -DTF_INCLUDE_PATH=/home/$USER/workspace/tflite/tensorflow \
      -DTF_LIB_PATH=/home/$USER/workspace/tflite/tensorflow/bazel-bin/tensorflow/lite \
      -DFLATBUFFER_INCLUDE_PATH=/home/$USER/workspace/tflite/flatbuffers/include

 
cmake --build .

./build/audiogen_main 
```



