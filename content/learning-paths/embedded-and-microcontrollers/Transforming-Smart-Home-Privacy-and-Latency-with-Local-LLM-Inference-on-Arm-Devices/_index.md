---
title: Build a Local GenAI Smart Home System on Arm SBC

minutes_to_complete: 30

who_is_this_for: Anyone who wants a private, cloud-free smart home powered by GenAI on Arm

learning_objectives:
  - "Deploy a local Large Language Model (LLM) for smart home control"
  - "Integrate natural language processing with GPIO control"
  - "Build and run everything on Arm-based single-board computers (no cloud required)"
  - "Optimize for speed, privacy, and offline operation"
prerequisites:
  - "Basic Python knowledge"
  - "A text editor (e.g., VS Code, Sublime, Notepad++)"
  - "An Arm-based single board computer (e.g., Raspberry Pi, Jetson Xavier AGX)"
  - "Basic electronic components such as LEDs, sensors (e.g., temperature), and actuators (e.g., relays or DC motors)"

author: "Fidel Makatia Omusilibwa"

### Tags
skilllevels: "Introductory"
subjects: "ML"
armips:
  - "Arm Cortex A"
tools_software_languages:
  - "Python"
  - "Ollama"
  - "VS Code or your preferred code editor"
  - "Jetson SDK (for NVIDIA Jetson SBC users)"
  - "(Optional) Docker"
operatingsystems:
  - "Windows , Linux, MacOS"

further_reading:
  - resource:
      title: "Advanced Edge AI on Arm with llama.cpp/ONXX"
      link: "https://github.com/fidel-makatia/EdgeAI_llamacpp"
      type: "source"
  - resource:
      title: "llama.cpp docummentation"
      link: "https://github.com/ggml-org/llama.cpp"
      type: "documentation"
  - resource:
      title: "Ollama documentation"
      link: "https://ollama.com/blog/python-javascript-libraries"
      type: "documentation"
  - resource:
      title: "ONNX  documentation"
      link: "https://github.com/onnx/tutorials"
      type: "documentation"
  - resource:
      title: "Jetson Xavier AGX  documentation"
      link: "https://developer.download.nvidia.com/embedded/L4T/r32-3-1_Release_v1.0/jetson_agx_xavier_developer_kit_user_guide.pdf?t=eyJscyI6IndlYnNpdGUiLCJsc2QiOiJkZXZlbG9wZXIubnZpZGlhLmNvbS9zZGstbWFuYWdlciJ9"
      type: "documentation"

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1 # _index.md always has weight of 1 to order correctly
layout: "learningpathall" # All files under learning paths have this same wrapper
learning_path_main_page: "yes" # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
