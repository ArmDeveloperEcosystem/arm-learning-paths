---
title: Run an LLM chatbot with rtp-llm on Arm-based servers

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who are interested in running a Large Language Model (LLM) with rtp-llm on Arm-based servers. 

learning_objectives:
    - Build rtp-llm on an Arm-based server.
    - Download a Qwen model from Hugging Face.
    - Run a Large Language Model with rtp-llm.

prerequisites:
    - Any Arm Neoverse N2-based or Arm Neoverse V2-based instance running Ubuntu 22.04 LTS from a cloud service provider or an on-premise Arm server. 
    - For the server, at least four cores and 16GB of RAM, with disk storage configured up to at least 32 GB. 

author_primary: Tianyu Li

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Neoverse
operatingsystems:
    - Linux
tools_software_languages:
    - LLM
    - GenAI
    - Python


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
