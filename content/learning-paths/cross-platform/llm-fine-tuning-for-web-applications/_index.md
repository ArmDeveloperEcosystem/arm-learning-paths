---
title: LLM fine-tuning for web and mobile applications

draft: true
cascade:
    draft: true

minutes_to_complete: 60

who_is_this_for: This is an introductory topic for developers and data scientists new to fine-tuning large language models (LLMs) and looking to develop a fine-tuned LLM for web and mobile applications. 

learning_objectives: 
    - Learn the basics of large language models (LLMs) and how fine-tuning enhances model performance for specific use cases.
    - Understand full fine-tuning, parameter-efficient fine-tuning (e.g., LoRA, QLoRA, PEFT), and instruction-tuning.
    - Learn when to use different fine-tuning approaches based on model size, task complexity, and computational constraints.
    - Learn how to curate, clean, and preprocess domain-specific datasets for optimal fine-tuning.
    - Understand dataset formats, tokenization, and annotation techniques for improving model learning.
    - Implement fine-tuning with frameworks like Hugging Face Transformers and PyTorch.
    - Compile a Large Language Model (LLM) using ExecuTorch.
    - Learn how to deploy a fine-tuned model on a mobile device.
    - Describe techniques for running large language models in an mobile environment.

prerequisites:
    - An AWS Graviton4 instance. You can substitute any Arm based Linux computer. Refer to [Get started with Arm-based cloud instances](/learning-paths/servers-and-cloud-computing/csp/) for more information about cloud service providers offering Arm-based instances. 
    - An Android smartphone with the i8mm feature and 16GB of RAM.
    - Basic understanding of machine learning and deep learning. 
    - Familiarity with deep learning frameworks such as PyTorch and Hugging Face Transformers. 

author: Parichay Das

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Neoverse
    
tools_software_languages:
    - LLM
    - GenAI
    - Python
    - PyTorch
    - ExecuTorch
operatingsystems:
    - Linux
    - Windows

shared_path: true
shared_between:
    - servers-and-cloud-computing
    - mobile-graphics-and-gaming

further_reading:
     - resource:
        title: Hugging Face Documentation
        link: https://huggingface.co/docs
        type: documentation
     - resource:
        title: PyTorch Documentation
        link: https://pytorch.org/docs/stable/index.html
        type: documentation
   



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
