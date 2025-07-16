---
title: Overview
weight: 2
 
### FIXED, DO NOT MODIFY
layout: learningpathall
---

## The AFM-4.5B model

AFM-4.5B is a 4.5-billion-parameter foundation model that delivers strong accuracy, strict compliance, robust multilingual support, and high cost-efficiency. Trained on nearly 7 trillion tokens of clean, rigorously filtered data, it performs well across a wide range of languages, including Arabic, English, French, German, Hindi, Italian, Korean, Mandarin, Portuguese, Russian, and Spanish.

In this Learning Path, you'll deploy AFM-4.5B using [Llama.cpp](https://github.com/ggerganov/llama.cpp) on an Arm-based AWS Graviton4 instance. You’ll walk through the full workflow, from setting up your environment and compiling the runtime to downloading, quantizing, and running inference on the model. You'll also evaluate model quality using perplexity, a common metric for measuring how well a language model predicts text.

This hands-on guide helps developers build cost-efficient, high-performance LLM applications on modern Arm server infrastructure using open-source tools and real-world deployment practices.

## Deployment workflow: AFM-4.5B with Llama.cpp on AWS Graviton4

The steps below outline the full deployment pipeline you'll follow in this Learning Path:

1. Launch Arm-based EC2 instance (Graviton4: c8g)  
    ↓  
2. Install build dependencies (such as CMake and Python)  
    ↓  
3. Build Llama.cpp from source  
    ↓  
4. Download AFM-4.5B model files from Hugging Face  
    ↓  
5. Quantize the model using Llama.cpp tools  
    ↓  
6. Run inference using the quantized model  
    ↓  
7. Evaluate model quality using perplexity

{{< notice Tip >}}
You can reuse this deployment flow with other models supported by Llama.cpp by swapping out the model file and adjusting quantization settings.
{{< /notice >}}




