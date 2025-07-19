---
title: Conclusion
weight: 10


### FIXED, DO NOT MODIFY
layout: learningpathall
---

## Conclusion

Congratulations! You've completed the process of deploying the Arcee AFM-4.5B foundation model on AWS Graviton4.

Here’s a quick summary of what you accomplished, and how you can build on it.

## What you built

Using this Learning Path, you:

- **Launched a Graviton4-powered EC2 instance**: you set up a `c8g.4xlarge` instance running Ubuntu 24.04 LTS, leveraging AWS's latest Arm-based processors for optimal performance and cost efficiency.

- **Configured the development environment**: you installed Git, build tools, and Python packages required for machine learning workloads.

- **Built Llama.cpp from source**: you compiled the optimized inference engine specifically for the Arm64 architecture to maximize performance on Graviton4.

- **Downloaded and optimized AFM-4.5B**: you retrieved the 4.5-billion parameter Arcee Foundation Model and converted it to the GGUF format, and created  8-bit and 4-bit quantized versions to reduce memory usage and improve speed.

- **Ran inference and evaluation**: you tested the model through interactive sessions, API endpoints, and benchmarking tools to analyze speed, memory usage, and quality.

### Key performance insights

Your benchmarking results highlight the power of quantization and Arm-based inference:

- **Memory efficiency**: the 4-bit quantized model uses only ~4.4GB of RAM, compared to ~15GB for the full-precision model.
- **Speed improvements**: quantized models deliver 2-3x faster inference (40+ tokens/second vs 15-16 tokens/second).
- **Cost optimization**: reduced memory usage allows you to use smaller, more affordable EC2 instances.
- **Quality preservation**: The quantized models maintain strong perplexity scores, showing minimal degradation in output quality.

## The Graviton4 advantage

AWS Graviton4 processors, built on the Arm Neoverse-V2 architecture, offer a range of benefits for AI/ML workloads:
- Superior performance per watt compared to x86 alternatives
- Cost savings of 20-40% for compute-intensive workloads
- Optimized memory bandwidth and cache for large models.- Native Arm64 support for across modern machine learning frameworks


## Next Steps and Call to Action

Now that you have a fully functional AFM-4.5B deployment, here are some exciting ways to extend your learning:

**Production Deployment**
- Set up auto-scaling groups for high availability
- Implement load balancing for multiple model instances
- Add monitoring and logging with CloudWatch
- Secure your API endpoints with proper authentication

**Application Development**
- Build a web application using the llama-server API
- Create a chatbot or virtual assistant
- Develop content generation tools
- Integrate with existing applications via REST APIs

The combination of Arcee AI's efficient foundation models, Llama.cpp's optimized inference engine, and AWS Graviton4's powerful Arm processors creates a compelling platform for deploying production-ready AI applications. Whether you're building chatbots, content generators, or research tools, this stack provides the performance, cost efficiency, and flexibility needed for modern AI workloads.

For more information on Arcee AI and how we can help you build high-quality, secure, and cost-efficient AI, solution, please visit [www.arcee.ai](https://www.arcee.ai).

