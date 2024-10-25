---
title: Run a benchmark on an Android phone
weight: 5

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Run a Phi-3 model on your Android phone

You can now prepare and run a Phi-3-mini model on your Android smartphone, and view performance metrics:

### Build model runner

First, cross-compile the model runner to run on Android using the commands below:

``` bash
cd onnxruntime-genai
copy src\ort_genai.h examples\c\include\
copy src\ort_genai_c.h examples\c\include\
cd examples\c
mkdir build
cd build
```
Run the `cmake` command as shown:

```bash
cmake -DCMAKE_TOOLCHAIN_FILE=C:\Users\$env:USERNAME\AppData\Local\Android\Sdk\ndk\27.0.12077973\build\cmake\android.toolchain.cmake -DANDROID_ABI=arm64-v8a -DANDROID_PLATFORM=android-27 -DCMAKE_BUILD_TYPE=Release -G "Ninja" ..
ninja
```

After successful build, a binary program called `phi3` will be created.

### Prepare Phi-3-mini model

Phi-3 ONNX models are hosted on HuggingFace. You can download the Phi-3-mini model by using the `huggingface-cli` command:

``` bash
pip install huggingface-hub[cli]
huggingface-cli download microsoft/Phi-3-mini-4k-instruct-onnx --include cpu_and_mobile/cpu-int4-rtn-block-32-acc-level-4/* --local-dir .
```
This command downloads the model into a folder called `cpu_and_mobile`.

The Phi-3-mini (3B) model has a short (4k) context version and a long (128k) context version. The long context version can accept much longer prompts and produce longer output text, but it does consume more memory. In this learning path, you will use the short context version, which is quantized to 4-bits.


### Run on Android via adb shell

#### Connect your Android phone
Connect your phone to your computer using a USB cable. 

You need to enable USB debugging on your Android device. You can follow [Configure on-device developer options](https://developer.android.com/studio/debug/dev-options) to do this.

Once you have enabled USB debugging and connected via USB, run:

```
adb devices
```

You should see your device listed to confirm it is connected. 

#### Copy the runner binary and the model files to the phone

``` bash
adb push cpu-int4-rtn-block-32-acc-level-4 /data/local/tmp
adb push .\phi3 /data/local/tmp
adb push onnxruntime-genai\build\Android\Release\libonnxruntime-genai.so /data/local/tmp
adb push onnxruntime\build\Windows\Release\libonnxruntime.so /data/local/tmp
```

#### Run the model

Use the runner to execute the model on the phone with the `adb` command:

``` bash
adb shell
cd /data/local/tmp
chmod 777 phi3
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/data/local/tmp
./phi3 cpu-int4-rtn-block-32-acc-level-4
```

This will allow the runner program to load the model. It will then prompt you to input the text prompt to the model. After you enter your input prompt, the text output by the model will be displayed. On completion, performance metrics similar to those shown below should be displayed:

```
Prompt length: 64, New tokens: 931, Time to first: 1.79s, Prompt tokens per second: 35.74 tps, New tokens per second: 6.34 tps
```

You have successfully run the Phi-3 model on your Android smartphone powered by Arm.
