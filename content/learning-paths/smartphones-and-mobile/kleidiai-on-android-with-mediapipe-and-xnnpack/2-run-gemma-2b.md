---
title: Running the Gemma 2B model using Google MediaPipe with XNNPACK
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Cross-compile the inference engine for CPU (Android)

Now that you have your environment set up correctly, it's time to build the inference engine. This executable can run an LLM model on an Android device, it will produce an output, given an initial prompt.

Before building, add the model path in mediapipe/tasks/cc/genai/inference/c/llm_inference_engine_cpu_main.cc in the default value of that argument as shown:

Note: This hack is because there seems to be an issue/bug when building the argument parser

ABSL_FLAG(std::optional<std::string>, model_path, "./model.bin", "Path to the tflite model file.");

Build the inference tool using this command:

```bash

bazel build -c opt --config=android_arm64 mediapipe/tasks/cc/genai/inference/c:llm_inference_engine_cpu_main

```

Note: The output binary can be found in this path: bazel-bin/mediapipe/tasks/cc/genai/inference/c/llm_inference_engine_cpu_main

Running inference engine for CPU (Android)

1) Push the resulted binary to the phone using ADB:

adb push bazel-bin/mediapipe/tasks/cc/genai/inference/c/llm_inference_engine_cpu_main /data/local/tmp/gen_ai 2) Download gemma 4-bit model from kaggle and push to the phone

tar -xf archive.tar.gz adb push gemma-2b-it-cpu-int4.bin /data/local/tmp/gen_ai

3) Run the binary in the phone as follows:

$ ./llm_inference_engine_cpu_main Output should look like: Section 2: Benchmark the Gemma 2B model

IMAGE HERE:
![example image alt-text#center](example-picture.png "Figure 1. Example image caption")
