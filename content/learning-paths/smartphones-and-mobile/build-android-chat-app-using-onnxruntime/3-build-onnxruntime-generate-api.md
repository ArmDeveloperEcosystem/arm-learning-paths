---
title: Build ONNX Runtime Generate() API
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Cross-compile the ONNX Runtime generate() API for Android CPU

The Generate() API in ONNX Runtime is designed for text generation tasks using models like Phi-3. It implements the generative AI loop for ONNX models, including pre and post processing, inference with ONNX Runtime, logits processing, search and sampling, and KV cache management. You can learn more by reading the [ONNX Runtime generate() API page](https://onnxruntime.ai/docs/genai/).


### Clone onnxruntime-genai repo
Open up a Windows Powershell prompt and checkout the source repo:

```bash
C:\Users\$env:USERNAME
git clone https://github.com/microsoft/onnxruntime-genai
cd onnxruntime-genai
git checkout 1e4d289502a61265c3b07efb17d8796225bb0b7f
```

{{% notice Note %}}
You might be able to use later commits. These steps have been tested with the commit `1e4d289502a61265c3b07efb17d8796225bb0b7f`.
{{% /notice %}}

### Build for Android CPU

The Ninja generator needs to be used to build on Windows for Android.

```bash
 
 # Example
python3.11 build.py --build_java --android --android_home C:\Users\$env:USERNAME\AppData\Local\Android\Sdk --android_ndk_path C:\Users\$env:USERNAME\AppData\Local\Android\Sdk\ndk\27.0.12077973 --android_abi arm64-v8a --config Release

```

When the build is complete, confirm the shared library has been created:

```
ls build\Android\Release\onnxruntime-genai.so
```
