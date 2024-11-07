---
title: Overview
weight: 2

### FIXED, DO NOT MODIFY
layout: learningpathall
---
## Overview

Arm CPUs are widely used in traditional ML and AI use cases. In this Learning Path, you will learn how to run the generative AI inference-based use case of an LLM chatbot on an Arm-based CPU. You will do this by deploying the [Qwen2-0.5B-Instruct model](https://huggingface.co/Qwen/Qwen2-0.5B-Instruct) on your Arm-based CPU using `rtp-llm`.

[rtp-llm](https://github.com/alibaba/rtp-llm) is an open source C/C++ project developed by Alibaba that enables efficient LLM inference on a variety of hardware. 

You can use the instructions in this Learning Path for any Arm Neoverse N2-based or Arm Neoverse V2-based server running Ubuntu 22.04 LTS. To run this example, you require an Arm server instance with at least four cores and 16GB of RAM. Configure disk storage up to at least 32 GB. 

{{% notice Note %}}
This Learning Path has been tested on an Alibaba Cloud g8y.8xlarge instance and an AWS Graviton4 r8g.8xlarge instance.
{{% /notice %}}


 
