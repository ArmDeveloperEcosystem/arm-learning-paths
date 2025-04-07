---
title: Build ONNX Runtime Generate() API
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Compile the ONNX Runtime Generate() API for Windows ARM64 CPU

The Generate() API in ONNX Runtime is designed for text generation tasks using models like Phi-3. It implements the generative AI loop for ONNX models, including:
- pre- and post-processing
- inference with ONNX Runtime- logits processing
- search and sampling
- KV cache management.

You can learn more by reading the [ONNX Runtime Generate() API page](https://onnxruntime.ai/docs/genai/).

In this page you will learn how to build the Generate API() from source (C/C++ build).


### Clone onnxruntime-genai Repo
Within your Windows Developer Command Prompt for Visual Studio, checkout the source repo:

```bash
cd C:\Users\%USERNAME%
cd repos\lp
git clone https://github.com/microsoft/onnxruntime-genai
cd onnxruntime-genai
git checkout b2e8176c99473afb726d364454dc827d2181cbb2
```

{{% notice Note %}}
You might be able to use later commits. These steps have been tested with the commit `b2e8176c99473afb726d364454dc827d2181cbb2`.
{{% /notice %}}

### Build for Windows ARM64 CPU
The build command below has a ---config argument, which takes the following options:
- ```Release``` builds release build
- ```Debug``` builds binaries with debug symbols
- ```RelWithDebInfo``` builds release binaries with debug info

Below are the instruction to build ```Release```:
```bash
python build.py --config Release --skip_tests
```

When the build is complete, confirm the ONNX Runtime Generate() API Dynamic Link Library has been created:

```output
dir build\Windows\Release\Release\onnxruntime-genai.dll
```
