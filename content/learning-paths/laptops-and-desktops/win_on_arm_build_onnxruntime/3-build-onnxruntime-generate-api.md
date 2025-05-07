---
title: Build ONNX Runtime Generate() API
weight: 4

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Build the ONNX Runtime Generate() API for Windows on Arm 

The Generate() API in ONNX Runtime is designed for text generation tasks using models like Phi-3. It implements the generative AI loop for ONNX models, including:
- Pre- and post-processing.
- Inference with ONNX Runtime (including logits processing).
- Search and sampling.
- KV cache management.

{{% notice Learning Tip %}}
You can learn more about this area by reading the [ONNX Runtime Generate() API documentation](https://onnxruntime.ai/docs/genai/).
{{% /notice %}}

In this section, you'll build the Generate() API from source.


### Clone the onnxruntime-genai repository
From your **Windows Developer Command Prompt for Visual Studio**, clone the repository and checkout the following tested commit:

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

### Build for Windows on Arm
The build script uses a --config argument, which supports the following options:
- ```Release``` builds release build.
- ```Debug``` builds binaries with debug symbols.
- ```RelWithDebInfo``` builds release binaries with debug info.

To build the `Release` variant of the ONNX Runtime Generate() API:

```bash
pip install requests
python build.py --config Release --skip_tests
```

### Verify the output

When the build is complete, confirm the ONNX Runtime Generate() API Dynamically Linked Library has been created:

```output
dir build\Windows\Release\Release\onnxruntime-genai.dll
```
