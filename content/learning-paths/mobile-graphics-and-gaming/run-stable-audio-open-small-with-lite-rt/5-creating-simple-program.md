---
title: Create a simple program
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create and build a simple program

You'll now build a simple program that runs inference on all three submodules directly on an Android device.

The program takes a text prompt as input and generates an audio file as output.
```bash
cd $WORKSPACE/audio-stale-open-litert/app
mkdir build && cd build
```

Ensure the NDK path is set correctly and build with cmake:
```bash
cmake -DCMAKE_TOOLCHAIN_FILE=$NDK_PATH/build/cmake/android.toolchain.cmake \
      -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
      -DANDROID_ABI=arm64-v8a \
      -DTF_INCLUDE_PATH=$TF_SRC_PATH \
      -DTF_LIB_PATH=$TF_SRC_PATH/bazel-bin/tensorflow/lite \
      -DFLATBUFFER_INCLUDE_PATH=$TF_SRC_PATH/flatc-native-build/flatbuffers/include \
    ..

cmake --build . -j1
```

After the SAO example builds successfully, a binary file named `audiogen_main` is created.

Now use adb (Android Debug Bridge) to push the necessary files to the device:

```bash
adb shell
```

Create a directory for all the required resources:
```bash
cd /data/local/tmp
mkdir audiogen
exit
```
Push all necessary files into the `audiogen` folder on Android:
```bash
cd $WORKSPACE/audio-stale-open-litert/app/build
adb shell mkdir -p /data/local/tmp/app
adb push audiogen /data/local/tmp/app
adb push $LITERT_MODELS_PATH/conditioners.onnx /data/local/tmp/app
adb push $LITERT_MODELS_PATH/dit_model.tflite /data/local/tmp/app
adb push $LITERT_MODELS_PATH/autoencoder_model.tflite /data/local/tmp/app
adb push ${TF_SRC_PATH}/bazel-bin/tensorflow/lite/libtensorflowlite.so /data/local/tmp/app
```

Finally, run the program on your Android device:
```
adb shell
cd /data/local/tmp/app
chmod +x audiogen
LD_LIBRARY_PATH=. ./audiogen . "warm arpeggios on house beats 120BPM with drums effect" 4
```
