---
title: Deploy a LLM-based Vision Chatbot with PyTorch and Hugging Face Transformers on Google Axion processors

minutes_to_complete: 45

who_is_this_for: This Learning Path is for software developers and ML engineers who are interested in deploying a production-ready vision chatbot for their application with optimized performance on the Arm Architecture.

description: Build a production-ready vision chatbot on Google Axion using Streamlit, PyTorch, and Hugging Face Transformers with a quantized Llama 3.2-Vision model.

learning_objectives:
    - Build a frontend with Streamlit to input images and prompts
    - Build the backend to download a Llama 3.2-Vision model, quantize it, and run it using PyTorch and Hugging Face Transformers
    - Monitor and analyze inference on Arm CPUs

prerequisites:
    - A Google Cloud Axion compute instance or [any Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider with at least 32 cores.
    - Familiarity with REST APIs and web services.
    - A basic understanding of Python and ML concepts.
    - A basic understanding of Streamlit.
    - A basic understanding of LLM fundamentals.

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-03T01:22:45Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 3e8307a5daf435c21f3cecff635ac51724a63ff9ea4307082d869601563b4204
  summary_generated_at: '2026-06-02T04:17:37Z'
  summary_source_hash: 3e8307a5daf435c21f3cecff635ac51724a63ff9ea4307082d869601563b4204
  faq_generated_at: '2026-06-03T01:22:45Z'
  faq_source_hash: 3e8307a5daf435c21f3cecff635ac51724a63ff9ea4307082d869601563b4204
  summary: >-
    This Learning Path shows how to deploy a production-ready, vision-enabled chatbot on Arm-based
    servers using Google Cloud Axion. You will build a Flask backend that downloads a Llama 3.2‑Vision
    model from Hugging Face, applies 4‑bit quantization, and serves inference with PyTorch and
    Transformers, and a Streamlit frontend that accepts images and text prompts. The instructions
    target Ubuntu 24.04 LTS and were tested on a Google Cloud c4a-standard-64 instance; an Arm
    server with at least 32 CPU cores is required. You will launch the web UI on port 8501 and
    monitor and analyze inference on Arm CPUs. Prerequisites include basic Python/ML, Streamlit,
    LLM fundamentals, and familiarity with REST and web services.
  faqs:
  - question: What do I need before running this Learning Path?
    answer: >-
      You need a Google Cloud Axion compute instance or any Arm-based instance with at least 32
      CPU cores. Familiarity with REST APIs and web services, basic Python and ML concepts, Streamlit,
      and LLM fundamentals is expected.
  - question: Which environment is targeted and what instance was used for testing?
    answer: >-
      The steps are tailored for Arm servers running Ubuntu 24.04 LTS. They were tested on a Google
      Cloud c4a-standard-64 instance.
  - question: Which model is used and how is it prepared for inference?
    answer: >-
      The backend downloads the Llama 3.2‑Vision model from Hugging Face and performs 4‑bit quantization.
      It then serves the model with PyTorch on Arm CPUs.
  - question: How do I access the web application once the services are running?
    answer: >-
      Open your browser to http://[your instance ip]:8501. On Google Cloud, you may need to allow
      inbound TCP traffic on port 8501 in your instance’s firewall rules.
  - question: What result should I expect to validate that inference is working?
    answer: >-
      From the Streamlit UI, upload an image and enter a text prompt; the app should return a
      generated text response that uses the image as context. The backend Flask service streams
      the model’s output to the frontend.
# END generated_summary_faq

author: Nobel Chowdary Mandepudi

### Tags
skilllevels: Advanced
armips:
    - Neoverse
subjects: ML
cloud_service_providers:
  - Google Cloud
operatingsystems:
    - Linux
tools_software_languages:
    - Python
    - PyTorch
    - Streamlit
    - Google Axion
   
further_reading:
    - resource:
        title: Getting started with Llama
        link: https://llama.meta.com/get-started
        type: documentation
    - resource:
        title: Hugging Face Documentation
        link: https://huggingface.co/docs
        type: documentation
    - resource:
        title: Democratizing Generative AI with CPU-based inference
        link: https://blogs.oracle.com/ai-and-datascience/post/democratizing-generative-ai-with-cpu-based-inference
        type: blog



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---

