---
title: Run a local LLM chatbot on a Raspberry Pi 5 

description: Learn how to install the Python version of llama.cpp on a Raspberry Pi 5, download an LLM from Hugging Face, assess memory and performance, and run the model using Python bindings.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for anyone interested in running a local Large Language Model on a Raspberry Pi 5.

learning_objectives:
    - Install the Python version of llama.cpp on your Raspberry Pi 5.
    - Download an LLM from Hugging Face. 
    - Assess LLM memory size and performance.
    - Run the LLM on your Raspberry Pi 5 using Python bindings for llama.cpp.

prerequisites:
    - A Raspberry Pi 5 running Raspberry Pi OS.

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-08-12T20:10:40Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 30b304e77487fc1e8ac6fc5baaee6d8e4cf2c27898b319f230ca425994313645
  summary_generated_at: '2026-08-12T20:10:40Z'
  summary_source_hash: 30b304e77487fc1e8ac6fc5baaee6d8e4cf2c27898b319f230ca425994313645
  faq_generated_at: '2026-08-12T20:10:40Z'
  faq_source_hash: 30b304e77487fc1e8ac6fc5baaee6d8e4cf2c27898b319f230ca425994313645
  summary: >-
    You'll run a local chatbot on a Raspberry Pi 5 with 64-bit Raspberry Pi OS. You'll install
    the Python bindings for `llama.cpp`, choose a model that fits available memory, and download
    it from Hugging Face. You'll load the model, generate responses, and verify interactive inference
    directly on the Arm Linux device.
  faqs:
  - question: Which Raspberry Pi 5 model should I use for this chatbot?
    answer: >-
      The 8 GB RAM Raspberry Pi 5 model is preferred for exploring an LLM. Smaller memory configurations
      may restrict which model you can run.
  - question: How do I know my Raspberry Pi OS installation is 64-bit?
    answer: >-
      Check your system information to confirm the operating system and kernel report a 64-bit
      build. If not, reinstall Raspberry Pi OS using the 64-bit image.
  - question: Can I follow these steps on another Arm Linux computer?
    answer: >-
      Yes. The instructions apply to other Arm Linux systems with minor modifications where Raspberry
      Pi–specific steps appear.
  - question: How do I choose a Hugging Face model that will run on my Pi?
    answer: >-
      Compare the model’s size to your available memory and leave headroom for the operating system
      and Python runtime. Select a model that fits comfortably within your RAM, then assess performance.
  - question: What result should I expect when I run the chatbot?
    answer: >-
      A Python script loads the chosen model and generates text responses in your terminal. If
      it starts and responds to prompts, your setup is working.
# END generated_summary_faq

author: Jason Andrews

generate_summary_faq: false
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
operatingsystems:
    - Linux
tools_software_languages:
    - LLM
    - Generative AI
    - Raspberry Pi
    - Python
    - Hugging Face

further_reading:
    - resource:
        title: Practical AI for the Raspberry Pi
        link: https://github.com/ee292d/labs
        type: website
    - resource:
        title: Hugging Face Documentation
        link: https://huggingface.co/docs
        type: documentation
    - resource: 
        title: Python Bindings for llama.cpp
        link: https://github.com/abetlen/llama-cpp-python
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
