---
title: Conclusion
weight: 10


### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Conclusion

Congratulations! You have completed the process of deploying the Arcee AFM-4.5B foundation model on AWS Graviton4.

Here’s a summary of what you built and how you can expand on your knowledge.

## What you built

Using this Learning Path, you have:

- **Launched a Graviton4-powered EC2 instance** – you set up a `c8g.4xlarge` instance running Ubuntu 24.04 LTS, leveraging Arm-based compute for optimal price–performance.

- **Configured the development environment** – you installed essential tools and dependencies, including Git, build tools, and Python packages for machine learning workloads.

- **Built Llama.cpp from source** – you compiled the inference engine specifically for the Arm64 architecture to maximize performance on Graviton4.

- **Downloaded and optimized AFM-4.5B** – you retrieved the 4.5-billion-parameter Arcee Foundation Model, converted it to the GGUF format, and created quantized versions (8-bit and 4-bit) to reduce memory usage and improve speed.

- **Ran inference and evaluation** – you tested the model using interactive sessions and API endpoints, and benchmarked speed, memory usage, and model quality.

## Key performance insights

The benchmarking results demonstrate the power of quantization and Arm-based computing:

- **Memory efficiency** – the 4-bit model uses only ~4.4 GB of RAM compared to ~15 GB for the full-precision version.
- **Speed improvements** – inference with Q4_0 is 2–3x faster (40+ tokens/sec vs. 15–16 tokens/sec).
- **Cost optimization** – lower memory needs enable smaller, more affordable instances.
- **Quality preservation** – the quantized models maintain strong perplexity scores, showing minimal quality loss.

## The Graviton4 advantage

AWS Graviton4 processors, built on the Arm Neoverse-V2 architecture, provide:

- Superior performance per watt compared to x86 alternatives
- Cost savings of 20–40% for compute-intensive workloads
- Optimized memory bandwidth and cache hierarchy for AI/ML workloads
- Native Arm64 support for modern machine learning frameworks

## Next steps for deploying AFM-4.5B on Arm

Now that you have a fully functional AFM-4.5B deployment, here are some ways to extend your learning:

**Production deployment**
- Set up auto-scaling groups for high availability
- Implement load balancing for multiple model instances
- Add monitoring and logging with CloudWatch
- Secure your API endpoints with proper authentication

**Application development**
- Build a web application using the `llama-server` API
- Create a chatbot or virtual assistant
- Develop content generation tools
- Integrate with existing applications via REST APIs

Together, Arcee AI’s foundation models, Llama.cpp’s efficient runtime, and Graviton4’s compute capabilities give you everything you need to build scalable, production-grade AI applications. From chatbots and content generation to research tools, this stack strikes a balance between performance, cost, and developer control.

For more information on Arcee AI and how you can build high-quality, secure, and cost-efficient AI solutions, please visit www.arcee.ai.
