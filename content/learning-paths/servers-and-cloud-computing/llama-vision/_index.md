---
title: Deploy a LLM based Vision Chatbot with PyTorch and Hugging Face Transformers on Google Axion processors

minutes_to_complete: 45

who_is_this_for: This Learning Path is for software developers, ML engineers, and those who are interested to deploy production-ready vision chatbot for their application with optimized performance on Arm Architecture.

learning_objectives:
    - Download PyTorch and Torch AO.
    - Install required dependencies
    - Build frontend with Streamlit to input image and prompt.
    - Build backend to download the Llama 3.2 Vision model, Quantize and run it using PyTorch and Transformers.
    - Monitor and analyze inference on Arm CPUs.

prerequisites:
    - A Google Cloud Axion compute instance or [any Arm based instance](/learning-paths/servers-and-cloud-computing/csp/) from a cloud service provider with atleast 32 cores.
    - Basic understanding of Python and ML concepts.
    - Familiarity with REST APIs and web services.
    - Basic knowledge on Streamlit.
    - Understanding of LLM fundamentals.

author: Nobel Chowdary Mandepudi

### Tags
skilllevels: Advanced
armips:
    - Neoverse
subjects: ML
operatingsystems:
    - Linux
tools_software_languages:
    - Python
    - PyTorch
    - Streamlit
    - Google Axion
    - Demo

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
