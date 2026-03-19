---
title: Build and run the Android chat app
weight: 7

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Overview

In this section, you will use the ExecuTorch Android demo application to run the customer support chatbot with a full chat interface on your phone.

## Build the Android Archive (AAR)

Set up the build environment:

- Open a terminal and navigate to the root directory of the `executorch` repository
- If you have not already done so, set the following environment variables:

    ```bash
    export ANDROID_NDK=$ANDROID_HOME/ndk/29.0.14206865/
    export ANDROID_ABI=arm64-v8a
    export ANDROID_SDK=$ANDROID_HOME
    ```

    {{% notice Note %}}
`<path_to_android_ndk>` is the root for the NDK, which is usually under `~/Library/Android/sdk/ndk/XX.Y.ZZZZZ` on macOS, and contains `NOTICE` and `README.md`. Make sure `<path_to_android_ndk>/build/cmake/android.toolchain.cmake` is available for CMake to cross-compile.
    {{% /notice %}}

Run the following command to set up the required JNI library:

```bash
sh scripts/build_android_library.sh
```

## Copy model files to the phone

Make sure the exported model and tokenizer are on your Android phone.

### Option 1: Using adb

Check if the files are already on the phone:

```bash
adb shell "ls -la /data/local/tmp/llama/"
```

If they are not present, copy them:

```bash
adb shell mkdir -p /data/local/tmp/llama
adb push llama3_1B_kv_sdpa_xnn_qe_4_64_1024_embedding_4bit.pte /data/local/tmp/llama/
adb push $HOME/.llama/checkpoints/Llama3.2-1B-Instruct/tokenizer.model /data/local/tmp/llama/
```

### Option 2: Using Android Studio

Use Android Studio's **Device Explorer** to browse the phone's filesystem and upload the files if they are not already present.

## Build the Android Package Kit

Clone the `executorch-examples` repository, which contains the LlamaDemo app:

```bash
git clone https://github.com/meta-pytorch/executorch-examples.git
```

### Option 1: Using Android Studio (recommended)

Build and launch the app:

- Open Android Studio and select **Open an existing Android Studio project**
- Navigate to and open `executorch-examples/llm/android/LlamaDemo`
- Run the app (**^R**). This builds and launches the app on your connected phone

### Option 2: Command line

```bash
pushd llm/android/LlamaDemo
./gradlew :app:installDebug
popd
```

## Configure the chatbot persona

Once the app is running, you can set a system prompt in the app's settings to configure it as a customer support assistant. Set the system prompt to something like:

```
You are a helpful customer support assistant. You answer questions about products, help with troubleshooting, and escalate issues politely when needed. Keep responses concise and friendly.
```

This gives the Llama model its role and behavioral guidelines for every conversation, without changing the underlying model weights.

## What you've learned and what's next

You have successfully:
- Built the ExecuTorch Android library with KleidiAI support
- Deployed the model and tokenizer to your Android device
- Built and launched a full-featured chat application
- Configured the app as a customer support assistant

You now have a fully functional on-device customer support chatbot running on an Arm Android phone using ExecuTorch and KleidiAI. All inference runs locally with no cloud dependency and no user data leaving the device. You can customize the system prompt to match your specific product or domain requirements.
