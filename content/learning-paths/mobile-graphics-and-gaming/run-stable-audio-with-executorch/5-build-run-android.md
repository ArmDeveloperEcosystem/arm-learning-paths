---
title: Build and run on Android
weight: 6

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you will cross-compile the audio generation application for Android and run it on an Android device with an Arm CPU.

## Set up the environment

Start a fresh virtual environment:

```bash
cd $WORKSPACE/ML-examples/kleidiai-examples/audiogen-et/
python3.10 -m venv android-venv
source android-venv/bin/activate
```

If you haven't already installed ExecuTorch, install it now:

```bash
pip install executorch==1.0.0
```

## Set model path

Set the `EXECUTORCH_MODELS_PATH` environment variable to the directory containing your exported ExecuTorch models:

```bash
export EXECUTORCH_MODELS_PATH=$WORKSPACE/ML-examples/kleidiai-examples/audiogen-et
```

## Download and install Android NDK

Download Android NDK r27c for your host platform. Navigate to the `app` directory first:

```bash
cd app
```

{{< tabpane code=true >}}
  {{< tab header="Linux">}}
wget https://dl.google.com/android/repository/android-ndk-r27c-linux.zip
unzip android-ndk-r27c-linux.zip
  {{< /tab >}}
  {{< tab header="macOS">}}
curl https://dl.google.com/android/repository/android-ndk-r27c-darwin.zip -o android-ndk-r27c-darwin.zip
unzip android-ndk-r27c-darwin.zip
  {{< /tab >}}
{{< /tabpane >}}

Set the `NDK_PATH` environment variable to the extracted NDK directory:

```bash
export NDK_PATH=$(pwd)/android-ndk-r27c
```

If you extracted the NDK to a different directory, update `NDK_PATH` accordingly.

## Build the application for Android

Create a build directory and navigate into it:

```bash
mkdir android-build && cd android-build
```

Run CMake with the Android toolchain configuration:

```bash
cmake -DCMAKE_TOOLCHAIN_FILE=$NDK_PATH/build/cmake/android.toolchain.cmake -DANDROID_ABI=arm64-v8a ..
```

This command configures the build to use the Android NDK toolchain and target the arm64-v8a architecture.

Build the application:

```bash
make -j8
```

The build process creates an `audiogen` executable for Android in the `android-build` directory.

## Transfer files to Android device

Use `adb` to transfer the application and model files to your Android device.

Create a directory on the device:

```bash
adb shell mkdir -p /data/local/tmp/app
```

Push the application executable:

```bash
adb push audiogen /data/local/tmp/app
```

Push the three model files:

```bash
adb push $EXECUTORCH_MODELS_PATH/dit_model.pte /data/local/tmp/app
adb push $EXECUTORCH_MODELS_PATH/autoencoder_model.pte /data/local/tmp/app
adb push $EXECUTORCH_MODELS_PATH/conditioners_model.pte /data/local/tmp/app
```

## Download and transfer the tokenizer model

Download the SentencePiece tokenizer model:

{{< tabpane code=true >}}
  {{< tab header="Linux">}}
wget https://huggingface.co/google-t5/t5-base/resolve/main/spiece.model
adb push spiece.model /data/local/tmp/app
  {{< /tab >}}
  {{< tab header="macOS">}}
curl -L https://huggingface.co/google-t5/t5-base/resolve/main/spiece.model -o spiece.model
adb push spiece.model /data/local/tmp/app
  {{< /tab >}}
{{< /tabpane >}}

## Run the application on Android

Connect to your Android device using `adb`:

```bash
adb shell
```

Navigate to the application directory:

```bash
cd /data/local/tmp/app
```

Run the `audiogen` application with an example prompt:

```bash
./audiogen -m . -p "warm arpeggios on house beats 120BPM with drums effect" -t 4
```

The arguments are:
- Model Path (`-m`): Directory containing the models and tokenizer (`.` for current directory)
- Prompt (`-p`): Text description of the desired audio
- CPU Threads (`-t`): Number of CPU threads to use (adjust based on your device)

The application generates audio based on your prompt.

## Retrieve the generated audio

Exit the `adb shell` by typing `exit`, then pull the generated audio file from the device:

```bash
adb pull /data/local/tmp/app/warm_arpeggios_on_house_beats_120bpm_with_drums_effect_99.wav
```

You can now play the audio file on your Android phone.

You can now experiment with different prompts to generate various audio samples on your Android device. The application uses ExecuTorch with XNNPack and Arm KleidiAI optimizations to deliver efficient inference on Arm CPUs.

Try different prompts such as:
- "ambient piano melody with soft strings 80BPM"
- "energetic drum and bass beat 170BPM"
- "guitar riff with distortion 110BPM rock style"

The Stable Audio Open Small model works best with clear, descriptive prompts that include musical elements, tempo, and atmosphere.

## Summary

You have successfully deployed the Stable Audio Open Small model on Android using ExecuTorch. Throughout this Learning Path, you converted the three model submodules (Conditioners, DiT, and AutoEncoder) to ExecuTorch format, built an optimized audio generation application, and ran it on an Arm-based Android device. The application leverages ExecuTorch with XNNPack and Arm KleidiAI to deliver efficient on-device audio generation, enabling real-time text-to-audio synthesis without requiring cloud connectivity. You can now integrate this capability into mobile applications or continue exploring audio generation with different prompts and configurations.
