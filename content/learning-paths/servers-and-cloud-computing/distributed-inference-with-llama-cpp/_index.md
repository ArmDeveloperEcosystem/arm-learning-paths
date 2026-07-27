---
title: Run distributed inference with llama.cpp on Arm-based AWS Graviton4 instances
description: Run distributed LLM inference with llama.cpp across multiple AWS Graviton4 instances, covering multi-node setup, coordination, and performance trade-offs.

minutes_to_complete: 30

who_is_this_for: This introductory topic is for developers with some experience using llama.cpp who want to learn how to run distributed inference on Arm-based servers.

learning_objectives: 
    - Set up a main host and worker nodes with llama.cpp
    - Run a large quantized model (for example, Llama 3.1 405B) with distributed CPU inference on Arm machines

prerequisites:
    - Three AWS c8g.4xlarge instances with at least 500 GB of EBS storage
    - Python 3 installed on each instance
    - Access to Meta's gated repository for the Llama 3.1 model family and a Hugging Face token to download models
    - Familiarity with the Learning Path [Deploy a Large Language Model (LLM) chatbot with llama.cpp using KleidiAI on Arm servers](/learning-paths/servers-and-cloud-computing/llama-cpu/)
    - Familiarity with AWS

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-07-27T18:50:08Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3d6c5f380d7f7b4436573d6b432a42f267747d6a45c9ffca759c2048b7a94230
  summary_generated_at: '2026-07-27T18:50:08Z'
  summary_source_hash: 3d6c5f380d7f7b4436573d6b432a42f267747d6a45c9ffca759c2048b7a94230
  faq_generated_at: '2026-07-27T18:50:08Z'
  faq_source_hash: 3d6c5f380d7f7b4436573d6b432a42f267747d6a45c9ffca759c2048b7a94230
  summary: >-
    You'll run distributed CPU inference with llama.cpp on AWS Graviton4 instances. You'll convert
    Meta's Llama 3.1 70B safetensors shards to one GGUF file, quantize the weights to 4-bit, configure
    worker RPC backends and a master through a comma-separated `worker_ips` list, and verify
    connectivity with `telnet`. You'll then launch distributed inference across the Arm servers.
  faqs:
  - question: How do I pass the worker node addresses to the master?
    answer: >-
      Export the `worker_ips` environment variable with a comma-separated list of `host:port` entries,
      for example, `172.31.110.11:50052,172.31.110.12:50052`. Run this on the master node before
      starting inference.
  - question: How do I verify the master can reach a worker before running a distributed job?
    answer: >-
      From the master, run `telnet <worker_ip> 50052`. A successful connection confirms that the
      backend server on the worker is reachable.
  - question: Which model format should I use with llama.cpp in this path?
    answer: >-
      Convert Meta’s safetensors files for Llama 3.1 70B to a single GGUF file, then quantize
      to 4-bit GGUF. Use the quantized GGUF for inference.
  - question: How do I confirm the quantization step worked?
    answer: >-
      The process should create a new 4-bit GGUF weights file that is smaller than the 16-bit GGUF.
      Use this 4-bit file for the distributed run.
  - question: How many nodes are used in the example and what roles do they serve?
    answer: >-
      The example uses three AWS Graviton4 instances: one master node and two worker nodes. The
      master coordinates inference while the workers run the RPC backend.
# END generated_summary_faq

author: 
    - Aryan Bhusari
    - Joe Stech

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
cloud_service_providers:
  - AWS
armips:
    - Neoverse
tools_software_languages:
    - LLM
    - Generative AI
    - AWS
operatingsystems:
    - Linux

further_reading:
    - resource:
        title: llama.cpp RPC server code
        link: https://github.com/ggml-org/llama.cpp/tree/master/tools/rpc
        type: Code

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
