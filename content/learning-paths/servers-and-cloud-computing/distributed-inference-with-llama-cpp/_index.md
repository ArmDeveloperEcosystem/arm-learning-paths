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
    - Familiarity with the Learning Path [Deploy a Large Language Model (LLM) chatbot with llama.cpp using KleidiAI on Arm servers](/learning-paths/servers-and-cloud-computing/llama-cpu)
    - Familiarity with AWS

generate_summary_faq: true

rerun_summary: false
rerun_faqs: false

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T00:40:36Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 6ac0c7cf1ab4b3efa680acbf1e349b858bee5dc7992baf6689e1f293a83060a4
  summary_generated_at: '2026-06-02T03:33:12Z'
  summary_source_hash: 6ac0c7cf1ab4b3efa680acbf1e349b858bee5dc7992baf6689e1f293a83060a4
  faq_generated_at: '2026-06-03T00:40:36Z'
  faq_source_hash: 6ac0c7cf1ab4b3efa680acbf1e349b858bee5dc7992baf6689e1f293a83060a4
  summary: >-
    Learn to run distributed LLM inference with llama.cpp across multiple Arm-based AWS Graviton4
    instances on Linux. You will set up a master (main) host and worker nodes, download a Meta
    Llama 3.1 model, convert safetensors to a single GGUF file, quantize 16-bit weights to 4-bit,
    configure node coordination using llama.cpp’s distributed RPC feature, verify connectivity,
    and run the model across machines. This introductory path targets developers with some llama.cpp
    experience and familiarity with AWS. Prerequisites include three AWS c8g.4xlarge instances,
    Python 3 on each, and access to Meta’s gated repository with a Hugging Face token. The expected
    outcome is a working multi-node CPU inference run of a large quantized model.
  faqs:
  - question: What AWS resources do I need before starting?
    answer: >-
      You need three AWS c8g.4xlarge instances with at least 500 GB of EBS storage, running Linux.
      This path targets Arm-based AWS Graviton4.
  - question: Which model is used and how is it prepared?
    answer: >-
      The steps download Meta’s Llama 3.1 70B model, convert the safetensors files into a single
      GGUF file, and quantize the 16-bit GGUF weights to 4-bit. The resulting 4-bit GGUF file
      is what llama.cpp loads for inference.
  - question: How do I register worker nodes on the master node?
    answer: >-
      After setting up the workers, export the worker_ips environment variable on the master using
      entries like ip:50052. You can find each instance’s IP address in the AWS console.
  - question: How do I verify that the master can reach a worker node?
    answer: >-
      From the master node, run a telnet command to the worker’s IP on port 50052. If the backend
      server is set up correctly on the worker, you should see the backend server output.
  - question: What access and prior knowledge do I need to download and run the model?
    answer: >-
      You need Python 3 installed on each instance, access to Meta’s gated repository for the
      Llama 3.1 family, and a Hugging Face token. Familiarity with AWS and the Learning Path on
      deploying a llama.cpp chatbot using KleidiAI is also expected.
# END generated_summary_faq

author: 
    - Aryan Bhusari
    - Joe Stech

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

