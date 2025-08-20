---
title: Review your AFM-4.5B deployment on Axion
weight: 10

### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Review your AFM-4.5B deployment on Google Cloud Axion

Congratulations! You have successfully deployed the [AFM-4.5B](https://huggingface.co/arcee-ai/AFM-4.5B) foundation model on Google Cloud Axion Arm64.  

Here’s a summary of what you built and how to extend it.

Using this Learning Path, you have:

- **Launched an Axion-powered Google Cloud instance** – you set up a `c4a` instance running Ubuntu 24.04 LTS, leveraging Arm-based compute for optimal price–performance.

- **Configured the development environment** – you installed tools and dependencies, including Git, build tools, and Python packages for machine learning workloads.

- **Built Llama.cpp from source** – you compiled the inference engine specifically for the Arm64 architecture to maximize performance on Axion.

- **Downloaded and optimized AFM-4.5B** – you retrieved the 4.5-billion-parameter Arcee Foundation Model, converted it to the GGUF format, and created quantized versions (8-bit and 4-bit) to reduce memory usage and improve speed.

- **Ran inference and evaluation** – you tested the model using interactive sessions and API endpoints, and benchmarked speed, memory usage, and model quality.

## Key performance insights

The benchmarking results demonstrate the power of quantization and Arm-based computing:

- **Memory efficiency** – the 4-bit model uses only ~3 GB of RAM compared to ~9 GB for the full-precision version
- **Speed improvements** – inference with Q4_0 is 2.5x faster (~60+ tokens/sec vs. 25 tokens/sec)
- **Cost optimization** – lower memory needs enable smaller, more affordable instances
- **Quality preservation** – the quantized models maintain strong perplexity scores, showing minimal quality loss

## Benefits of Google Cloud Axion Arm64

Google Cloud Axion processors, based on Arm Neoverse V2, provide:

- Better performance per watt than x86 alternatives  
- 20–40% cost savings for compute-intensive workloads  
- Optimized memory bandwidth and cache hierarchy for ML tasks  
- Native Arm64 support for modern machine learning frameworks  

## Next steps with AFM-4.5B on Axion

Now that you have a working deployment, you can extend it further.

**Production deployment**:  
- Add auto-scaling for high availability  
- Implement load balancing for multiple instances  
- Enable monitoring and logging with CloudWatch  
- Secure API endpoints with authentication  

**Application development**:  
- Build a web app with the `llama-server` API  
- Create a chatbot or assistant  
- Develop content generation tools  
- Integrate AFM-4.5B into existing apps via REST APIs  

Together, Arcee AI’s foundation models, Llama.cpp’s efficient runtime, and Google Cloud Axion provide a scalable, cost-efficient platform for AI.  

From chatbots and content generation to research tools, this stack delivers a balance of performance, cost, and developer control.  

For more information on Arcee AI, and how you can build high-quality, secure, and cost-efficient AI solutions, please visit [www.arcee.ai](https://www.arcee.ai).
