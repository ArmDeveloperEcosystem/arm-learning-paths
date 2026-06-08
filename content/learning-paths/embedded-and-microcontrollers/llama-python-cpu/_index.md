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

generate_summary_faq: false

rerun_summary: true
rerun_faqs: true

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-06-02T22:30:54Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: aa6252610c0603acfdfc8d4555bb7da93cbdd5b9d92ba140c5dc5f63d23e2b07
  summary_generated_at: '2026-06-01T21:44:40Z'
  summary_source_hash: aa6252610c0603acfdfc8d4555bb7da93cbdd5b9d92ba140c5dc5f63d23e2b07
  faq_generated_at: '2026-06-02T22:30:54Z'
  faq_source_hash: aa6252610c0603acfdfc8d4555bb7da93cbdd5b9d92ba140c5dc5f63d23e2b07
  summary: >-
    This introductory Learning Path guides you through running a local LLM chatbot on a Raspberry
    Pi 5. You install the Python version of llama.cpp on Raspberry Pi OS (64-bit), download a
    model from Hugging Face, assess model memory size and performance, and run the model using
    Python bindings. The 8GB RAM Raspberry Pi 5 is preferred for exploring an LLM, and with minor
    modifications the approach can be adapted to other Arm Linux computers. By the end, you will
    have a working local chatbot and a basic understanding of its resource and performance characteristics
    on this device. Estimated time to complete is about 30 minutes. No additional prerequisites
    are explicitly listed beyond a Raspberry Pi 5 running Raspberry Pi OS.
  faqs:
  - question: How should I prepare the SD card and which Raspberry Pi OS build should I choose?
    answer: >-
      Use Raspberry Pi Imager as recommended in the Raspberry Pi documentation to prepare the
      SD card. Install the 64-bit version of Raspberry Pi OS for this Learning Path.
  - question: Do I need the 8GB RAM Raspberry Pi 5 model?
    answer: >-
      The 8GB RAM Raspberry Pi 5 model is preferred for exploring an LLM. The Learning Path requires
      a Raspberry Pi 5 running Raspberry Pi OS.
  - question: Can I follow these steps on another Arm Linux computer?
    answer: >-
      Yes, the instructions can be used on any Arm Linux computer with minor modifications. The
      Learning Path focuses on Raspberry Pi 5 as the primary target.
  - question: Where do I obtain the model and how is it executed?
    answer: >-
      You will download an LLM from Hugging Face. It is run using the Python version of llama.cpp
      through its Python bindings.
  - question: What result should I expect after completing the steps, and how long will it take?
    answer: >-
      In about 30 minutes, you will have a local LLM chatbot running on your Raspberry Pi 5 using
      Python. You will also assess the model’s memory size and performance on your device.
# END generated_summary_faq

author: Jason Andrews

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

