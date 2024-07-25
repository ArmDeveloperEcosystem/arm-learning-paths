---
title: Run the Gemma 2B model using MediaPipe with XNNPACK
weight: 3

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Cross-compile the inference engine for Android CPU

Now that you have your environment set up correctly, you can build the inference engine. This executable can run an LLM model on an Android device. It produces an output, given an initial prompt.

Build the inference tool using this command:

```bash

bazel build --cxxopt=-DABSL_FLAGS_STRIP_NAMES=0 -c opt --config=android_arm64 --define=xnn_enable_arm_i8mm=true mediapipe/tasks/cc/genai/inference/c:llm_inference_engine_cpu_main

```

When the build is complete, confirm the binary has been created:

```
ls bazel-bin/mediapipe/tasks/cc/genai/inference/c/llm_inference_engine_cpu_main
```


## Run the inference engine on your Android device

Firstly, you need to enable USB debugging on your Android device. Please follow [the official Android documentation on developer options](https://developer.android.com/studio/debug/dev-options) to enable USB debugging.

Once you have enabled USB debugging and connected via USB, run:

```
adb devices
```

From your local environment, ensure that your Android device is properly connected. 

If you see the following output (with a unique device ID in place of XXXXXXXXXXXXXX), then your device is ready:

```
List of devices attached
XXXXXXXXXXXXXX	device
```

Push the binary to the phone using ADB:

```bash
adb push bazel-bin/mediapipe/tasks/cc/genai/inference/c/llm_inference_engine_cpu_main /data/local/tmp/gen_ai
```

{{% notice Note %}}
If you are building from a Docker container, you must first copy the inference engine executable from your docker container to your local disk. First find the container ID of your running container by running:

```
docker ps
```

And then replace `[container ID]` in this command with your running container ID:

```
docker cp [container ID]:/home/ubuntu/mediapipe/bazel-bin/mediapipe/tasks/cc/genai/inference/c/llm_inference_engine_cpu_main .
```

You can then run:

```
adb push llm_inference_engine_cpu_main /data/local/tmp/gen_ai
```

To push the binary to your phone.
{{% /notice %}}

Download the Gemma 4-bit model from [Kaggle](https://www.kaggle.com/models/google/gemma/frameworks/tfLite/variations/gemma-2b-it-cpu-int4). This step cannot be done from the command line, since Google requires a sign-off on its consent form before releasing model weights.

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
./llm_inference_engine_cpu_main --model_path <path_to_gemma-2b-it-cpu-int4.bin>
```

The default behavior of this executable is to prompt the LLM to "write an email". The output you see should be a unique generated email that starts like this:

```output
husky:/data/local/tmp/gen_ai $ ./llm_inference_engine_cpu_main
WARNING: All log messages before absl::InitializeLog() is called are written to STDERR
I0000 00:00:1716392408.424383   13298 llm_inference_engine_cpu_main.cc:131] Prompt: Write an email
normalizer.cc(52) LOG(INFO) precompiled_charsmap is empty. use identity normalization.
I0000 00:00:1716392408.565851   13298 llm_inference_engine_cpu_main.cc:159] PredictAsync
I0000 00:00:1716392408.566016   13298 llm_inference_engine_cpu_main.cc:174] DeleteSession
▁to▁your▁colleagues,▁informing▁them▁of▁the▁upcoming▁company-wide▁meeting.

**Subject:▁Important▁Company-Wide▁Meeting**

Dear▁Colleagues,

...
```
