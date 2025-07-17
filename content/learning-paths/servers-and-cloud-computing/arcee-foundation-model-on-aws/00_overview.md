---
title: Overview
weight: 2
 
### FIXED, DO NOT MODIFY
layout: learningpathall
---

## The AFM-4.5B model

AFM-4.5B is a 4.5-billion-parameter foundation model that delivers strong accuracy, strict compliance, robust multilingual support, and high cost-efficiency. Trained on nearly 7 trillion tokens of clean, rigorously filtered data, it performs well across a wide range of languages, including Arabic, English, French, German, Hindi, Italian, Korean, Mandarin, Portuguese, Russian, and Spanish.

In this Learning Path, you'll deploy AFM-4.5B using [Llama.cpp](https://github.com/ggerganov/llama.cpp) on an Arm-based AWS Graviton4 instance. You’ll walk through the full workflow, from setting up your environment and compiling the runtime, to downloading, quantizing, and running inference on the model. You'll also evaluate model quality using perplexity, a common metric for measuring how well a language model predicts text.

This hands-on guide helps developers build cost-efficient, high-performance LLM applications on modern Arm server infrastructure using open-source tools and real-world deployment practices.

### LLM deployment workflow on Arm Graviton4

1. **Provision compute**  
   Launch an EC2 instance using a Graviton4-based instance type (for example, `c8g.4xlarge`).

2. **Set up your environment**  
   Install required build tools and dependencies (such as CMake, Python, and Git).

3. **Build the inference engine**  
   Clone the [Llama.cpp](https://github.com/ggerganov/llama.cpp) repository and compile the project for your Arm-based environment.

4. **Prepare the model**  
   Download the **AFM-4.5B** model files from Hugging Face and use Llama.cpp's quantization tools to reduce model size and optimize performance.

5. **Run inference**  
   Load the quantized model and run sample prompts using Llama.cpp.

6. **Evaluate model quality**  
   Calculate **perplexity** or use other metrics to assess model performance.

{{< notice Note>}}
You can reuse this deployment flow with other models supported by Llama.cpp by swapping out the model file and adjusting quantization settings.
{{< /notice >}}




