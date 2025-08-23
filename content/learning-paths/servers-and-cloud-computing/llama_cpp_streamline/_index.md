---
title: Use Streamline to analyze LLM running on CPU on llama.cpp

minutes_to_complete: 50

who_is_this_for: Engineers who want to learn LLM inference on CPU, engineers who want to proflie and optimize llama.cpp code.

learning_objectives: 
    - Be able to use Streamline to profile llama.cpp code
    - Learn the execution of LLM on CPU cores

prerequisites:
    - Understanding of llama.cpp
    - Understanding of transformer model
    - Knowledge of Streamline usage

author: Zenon(Zhilong) Xiu

### Tags
skilllevels: 4
subjects: PLACEHOLDER SUBJECT
armips:
    - Cortex-A
    - Neoverse
tools_software_languages:
    - Arm Streamline
    - C++
operatingsystems:
    - Linux
    - Android



further_reading:
    - resource:
        title: llama.cpp project
        link:  https://github.com/ggml-org/llama.cpp
        type:  source code
    - resource:
        title: Qwen1_5-0_5b-chat-q4_0.gguf 
        link: https://huggingface.co/Qwen/Qwen1.5-0.5B-Chat-GGUF/blob/main/qwen1_5-0_5b-chat-q4_0.gguf 
        type:  LLM model
    - resource:
        title: Arm Streamline User Guide 
        link: https://developer.arm.com/documentation/101816/9-7
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
