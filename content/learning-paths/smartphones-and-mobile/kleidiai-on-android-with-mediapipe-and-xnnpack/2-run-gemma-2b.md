---
title: Running the Gemma 2B model using Google MediaPipe with XNNPACK
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Cross-compile the inference engine for CPU (Android)

Now that you have your environment set up correctly, it's time to build the inference engine. This executable can run an LLM model on an Android device, it will produce an output, given an initial prompt.

Before building, add the model path in `mediapipe/tasks/cc/genai/inference/c/llm_inference_engine_cpu_main.cc` as the default value of the model_path argument. Search for:

```
ABSL_FLAG(std::optional<std::string>, model_path, std::nullopt,
```
 
and replace with

```
ABSL_FLAG(std::optional<std::string>, model_path, "./gemma-2b-it-cpu-int4.bin",
```
 
This adds the gemma model file (that you will download in a moment) to the default model path.

{{% notice Note %}}
This modification is necessary due to an argument parsing bug in the inference executable.
{{% /notice %}}

Build the inference tool using this command:

```bash

bazel build -c opt --config=android_arm64 mediapipe/tasks/cc/genai/inference/c:llm_inference_engine_cpu_main

```

When the build is complete, confirm the binary has been created:

`ls bazel-bin/mediapipe/tasks/cc/genai/inference/c/llm_inference_engine_cpu_main`


## Running the inference engine on your Android device

Push the binary to the phone using ADB:

```bash
adb push bazel-bin/mediapipe/tasks/cc/genai/inference/c/llm_inference_engine_cpu_main /data/local/tmp/gen_ai
```

Download the Gemma 4-bit model from [kaggle here](https://www.kaggle.com/models/google/gemma/frameworks/tfLite/variations/gemma-2b-it-cpu-int4). This step cannot be done from the command line, since Google requires a sign-off on its consent form before releasing model weights.

Once the model is downloaded, untar it and push it to the device with adb:

```bash
tar -xf archive.tar.gz
adb push gemma-2b-it-cpu-int4.bin /data/local/tmp/gen_ai
```

Connect to your Android device:

```
adb shell
```

Run the binary:

```bash
cd /data/local/tmp/gen_ai
./llm_inference_engine_cpu_main
```

The default behavior of this executable is to prompt the LLM to "Write an email". The output you see should be a unique generated email.