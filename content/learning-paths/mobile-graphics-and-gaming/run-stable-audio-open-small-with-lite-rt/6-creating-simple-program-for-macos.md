---
title: Create a simple program for macOS target
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Create and build a simple program

As a final step, you’ll build a simple program that runs inference on all three submodules directly on a macOS device.

The program takes a text prompt as input and generates an audio file as output.

```bash
cd $WORKSPACE/ML-examples/kleidiai-examples/audiogen/app
mkdir build && cd build
```

Ensure the NDK path is set correctly and build with `cmake`:

```bash
cmake -DCMAKE_POLICY_VERSION_MINIMUM=3.5 \
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
wget https://huggingface.co/google-t5/t5-base/resolve/main/spiece.model
```

Verify this model was downloaded to your `WORKSPACE`.

```text
ls $WORKSPACE/spiece.model
```

Copy the shared LiteRT dynamic library to the $LITERT_MODELS_PATH.
```bash
cp $TF_SRC_PATH/bazel-bin/tensorflow/lite/libtensorflowlite.so $LITERT_MODELS_PATH/
```

From there, you can then run the audiogen application, which requires just three input arguments:

* **Model Path:** The directory containing your LiteRT models and spiece.model files
* **Prompt:** A text description of the desired audio (e.g., warm arpeggios on house beats 120BPM with drums effect)
* **CPU Threads:** The number of CPU threads to use (e.g., 4)

Play around with the advice from [Download and test the model](../2-testing-model) section.

```bash
cd $WORKSPACE
./build/audiogen $LITERT_MODELS_PATH "warm arpeggios on house beats 120BPM with drums effect" 4
```

You can now pull the generated `output.wav` back to your host machine and listen to the result.

```bash
adb pull /data/local/tmp/app/output.wav
```

You should now have gained hands-on experience running the Stable Audio Open Small model with LiteRT on Arm-based devices. This includes setting up the environment, optimizing the model for on-device inference, and understanding how efficient runtimes like LiteRT make low-latency generative AI possible at the edge. You’re now better equipped to explore and deploy AI-powered audio applications on mobile and embedded platforms.
