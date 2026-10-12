---
title: Deploy a LLM-based vision chatbot with PyTorch and Hugging Face transformers on Google Axion processors

minutes_to_complete: 45

who_is_this_for: This Learning Path is for software developers and ML engineers who are interested in deploying a production-ready vision chatbot for their application with optimized performance on the Arm Architecture.

description: Build a production-ready vision chatbot on Google Axion using Streamlit, PyTorch, and Hugging Face Transformers with a quantized Llama 3.2-Vision model.

learning_objectives:
    - Build a frontend with Streamlit to input images and prompts.
    - Build the backend to download a Llama 3.2-Vision model, quantize it, and run it using PyTorch and Hugging Face Transformers.
    - Monitor and analyze inference on Arm CPUs.

prerequisites:
    - A Google Cloud Axion compute instance or [any Arm-based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider with at least 32 cores
    - Familiarity with REST APIs and web services
    - A basic understanding of Python and ML concepts
    - A basic understanding of Streamlit
    - A basic understanding of LLM fundamentals

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-09-15T21:26:34Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: acd41945ae84be42f98fbc61a4e1f153067d53e3d3992c38825b78b381d1d568
  summary_generated_at: '2026-09-15T21:26:34Z'
  summary_source_hash: acd41945ae84be42f98fbc61a4e1f153067d53e3d3992c38825b78b381d1d568
  faq_generated_at: '2026-09-15T21:26:34Z'
  faq_source_hash: acd41945ae84be42f98fbc61a4e1f153067d53e3d3992c38825b78b381d1d568
  summary: >-
    You'll build and deploy a vision-enabled chatbot with PyTorch, Transformers, and Streamlit on an Arm-based instance powered by Google Axion. First, you'll run a Flask backend that downloads and serves
    a quantized Llama 3.2-Vision model, then create a Streamlit frontend for image uploads
    and prompts. You'll configure firewall access, start both services on Ubuntu, and verify
    image-plus-text responses in the web app.
  faqs:
  - question: What result should I expect when both the backend and frontend are running?
    answer: >-
      Open the browser to the app. You'll see the title **LLM Vision Chatbot on Arm** with
      controls to upload an image and enter a prompt. After submitting, the page will display a generated
      text response that uses the image as context.
  - question: Which address should I use to open the web app?
    answer: >-
      Use `http://[your instance ip]:8501` in your browser. If the page doesn't load, allow inbound
      TCP traffic to port `8501` in your instance’s security rules.
  - question: How do I run the backend and frontend at the same time?
    answer: >-
      Start the backend script in one terminal with the virtual environment activated. Then, open a
      new terminal, activate the same environment, and start the Streamlit frontend.
  - question: What should I check if the frontend can't reach the backend?
    answer: >-
      Confirm that `backend.py` is running on port `5000` and that `frontend.py` uses
      `http://localhost:5000/v1/chat/completions`. For remote browser access, open the Streamlit
      frontend on port `8501`. The frontend connects to the backend locally.
  - question: How do I know that the model download and 4-bit quantization completed?
    answer: >-
      Start `backend.py` and wait for the Flask output showing that the server is running on port
      `5000`. The `backend.py` startup loads the Llama 3.2 Vision model and performs quantization
      before serving requests.
# END generated_summary_faq

author: Nobel Chowdary Mandepudi

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
armips:
    - Neoverse
subjects: ML
platforms:
  - Google Axion
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
