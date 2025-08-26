---
title: Build ONNX Runtime Generate() API
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Cross-compile the ONNX Runtime Generate() API for Android CPU

The Generate() API in ONNX Runtime is designed for text generation tasks using models like Phi-3. It implements the generative AI loop for ONNX models, including:
- pre- and post-processing
- inference with ONNX Runtime
- logits processing
- search and sampling
- KV cache management. 
You can learn more by reading the [ONNX Runtime generate() API page](https://onnxruntime.ai/docs/genai/).


### Clone onnxruntime-genai repo
Within your Windows PowerShell prompt, checkout the source repo:

```bash
C:\Users\$env:USERNAME
git clone https://github.com/microsoft/onnxruntime-genai
cd onnxruntime-genai
git checkout 5ba9fce5b52452a82b12ac343d941765c430d996
```

{{% notice Note %}}
You might be able to use later commits. These steps have been tested with the commit `5ba9fce5b52452a82b12ac343d941765c430d996`. This corresponds to ORT Gen API 0.9.0
{{% /notice %}}

### Build for Android CPU

Ninja generator is used to build on Windows for Android. Make sure you have set JAVA_HOME before running the following command:

```bash
python -m pip install requests 
python3.13 build.py --skip_wheel --build_java --android --android_home C:\Users\$env:USERNAME\AppData\Local\Android\Sdk --android_ndk_path C:\Users\$env:USERNAME\AppData\Local\Android\Sdk\ndk\27.3.13750724 --android_abi arm64-v8a --config Release
```

When the build is complete, confirm the shared library has been created:

```output
ls build\Android\Release\libonnxruntime-genai.so
ls build\Android\Release\src\java\build\android\outputs\aar\onnxruntime-genai-release.aar
```
