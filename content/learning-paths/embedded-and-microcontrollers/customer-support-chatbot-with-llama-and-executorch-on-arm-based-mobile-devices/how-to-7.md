---
title: Run, Testing and Benchmarking
weight: 8 

### FIXED, DO NOT MODIFY
layout: learningpathall
---

####  Build the Android (AAR)
You can use the Android demo application included in the ExecuTorch repository, [LlamaDemo](https://github.com/pytorch/executorch/tree/main/examples/android/LlamaDemo), to showcase local inference with ExecuTorch

Open a terminal and navigate to the root directory of the ExecuTorch repository.Then, set the following environment variables:

```bash
export ANDROID_NDK=$ANDROID_HOME/ndk/28.0.12433566/
export ANDROID_ABI=arm64-v8a
```
Run the following commands to set up the required JNI library:
```bash
pushd extension/android
./gradlew build
popd
pushd examples/demo-apps/android/LlamaDemo
./gradlew :app:setup
popd
```
Check if the files are available on the phone:
```bash
adb shell "ls -la /data/local/tmp/llama/"
```
If not, copy them:
```
adb shell mkdir -p /data/local/tmp/llama
adb push <model.pte> /data/local/tmp/llama/
adb push <tokenizer.bin> /data/local/tmp/llama/
```

#### Build the Android Package Kit using Android Studio
- Open Android Studio and choose Open an existing Android Studio project.
- Navigate to examples/demo-apps/android/LlamaDemo and open it.
- Run the app (^R) to build and launch it on your connected Android device.

#### Measure Inference Latency
-	adb shell am start -n com.example.chatbot/.MainActivity
-	adb shell dumpsys meminfo com.example.chatbot
