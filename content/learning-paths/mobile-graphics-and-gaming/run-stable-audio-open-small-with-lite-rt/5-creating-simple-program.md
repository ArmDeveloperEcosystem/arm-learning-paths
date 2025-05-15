---
title: Create a simple program
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create and build a simple program

As a final step, you'll now build a simple program that runs inference on all three submodules directly on an Android device.

The program takes a text prompt as input and generates an audio file as output.

```bash
cd $WORKSPACE/ML-examples/kleidiai-examples/audiogen/app
mkdir build && cd build
```

Ensure the NDK path is set correctly and build with `cmake`:

```bash
cmake -DCMAKE_TOOLCHAIN_FILE=$NDK_PATH/build/cmake/android.toolchain.cmake \
      -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
      -DANDROID_ABI=arm64-v8a \
      -DTF_INCLUDE_PATH=$TF_SRC_PATH \
      -DTF_LIB_PATH=$TF_SRC_PATH/bazel-bin/tensorflow/lite \
      -DFLATBUFFER_INCLUDE_PATH=$TF_SRC_PATH/flatc-native-build/flatbuffers/include \
    ..

make -j
```
After the example application builds successfully, a binary file named `audiogen` is created.

A SentencePiece model is a type of subword tokenizer which is used by the audiogen application, you’ll need to download the *spiece.model* file from:

```bash
cd $WORKSPACE
wget https://huggingface.co/google-t5/t5-base/tree/main
```

Verify this model was downloaded to your `WORKSPACE`.

```text
ls $WORKSPACE/spiece.model
```

Connect your Android device to your development machine using a cable. adb (Android Debug Bridge) is available as part of the Android SDK. You should see your device on running the following command.

```bash
adb devices
```

```output
<DEVICE ID>     device
```

Note that you may have to approve the connection on your phone for this to work. Now, use `adb` to push all necessary files into the `audiogen` folder on Android device:

```bash
cd $WORKSPACE/ML-examples/kleidiai-examples/audiogen/app/build
adb shell mkdir -p /data/local/tmp/app
adb push audiogen /data/local/tmp/app
adb push $LITERT_MODELS_PATH/conditioners_float32.tflite /data/local/tmp/app
adb push $LITERT_MODELS_PATH/dit_model.tflite /data/local/tmp/app
adb push $LITERT_MODELS_PATH/autoencoder_model.tflite /data/local/tmp/app
adb push $WORKSPACE/spiece.model /data/local/tmp/app
adb push ${TF_SRC_PATH}/bazel-bin/tensorflow/lite/libtensorflowlite.so /data/local/tmp/app
```

Start a new shell to access the device's system from your development machine:

```bash
adb shell
```

Finally, run the program on your Android device. Play around with the advice from [Download the model](../2-testing-model) section.

```bash
cd /data/local/tmp/app
LD_LIBRARY_PATH=. ./audiogen . "warm arpeggios on house beats 120BPM with drums effect" 4
exit
```

The successful execution of the app will create `output.wav` of your chosen audio defined by the prompt, you can pull it back to your host machine and enjoy!

```bash
adb pull /data/local/tmp/app/output.wav
```

You should now have gained hands-on experience running the Stable Audio Open Small model with LiteRT on Arm-based devices. This includes setting up the environment, optimizing the model for on-device inference, and understanding how efficient runtimes like LiteRT make low-latency generative AI possible at the edge. You’re now better equipped to explore and deploy AI-powered audio applications on mobile and embedded platforms.