---
title: Build a Privacy-First LLM Smart Home on Raspberry Pi 5

minutes_to_complete: 45

who_is_this_for: Anyone who wants a private, cloud-free smart home powered by GenAI on Arm

learning_objectives:
  - "Deploy a local Large Language Model (LLM) for smart home control"
  - "Integrate natural language processing with GPIO control"
  - "Build and run everything on Arm-based single-board computers (no cloud required)"
  - "Optimize for speed, privacy, and offline operation"
  - "Create an interactive web dashboard for smart home control"
prerequisites:
  - "Basic Python knowledge"
  - "A text editor (e.g., VS Code, Sublime, Notepad++)"
  - "An Arm-based single board computer (e.g., Raspberry Pi 5 with at least 8GB RAM)"
  - "Basic electronic components such as LEDs, sensors, and relays"
  - "Basic understanding of GPIO pins and electronics"

author: "Fidel Makatia Omusilibwa"

### Tags
skilllevels: "Introductory"
subjects: "ML"
armips:
  - "Arm Cortex A"
tools_software_languages:
  - "Python"
  - "Ollama"
  - "gpiozero"
  - "lgpio"
  - "FastAPI"
  - "VS Code or your preferred code editor"
  - "Raspberry Pi OS (64-bit)"
operatingsystems:
  - "Windows , Linux, MacOS"

further_reading:
  - resource:
      title: "Raspberry Pi 5 Smart Home Assistant with EdgeAI"
      link: "https://github.com/fidel-makatia/EdgeAI_Raspi5"
      type: "source"
  - resource:
      title: "Ollama Python/JavaScript Libraries"
      link: "https://ollama.com/blog/python-javascript-libraries"
      type: "documentation"
  - resource:
      title: "gpiozero Documentation for Raspberry Pi"
      link: "https://gpiozero.readthedocs.io/en/stable/"
      type: "documentation"
  - resource:
      title: "lgpio Library for Raspberry Pi 5"
      link: "https://abyz.me.uk/lg/lgpio.html"
      type: "documentation"
  - resource:
      title: "Raspberry Pi 5 Official Documentation"
      link: "https://www.raspberrypi.org/documentation/computers/raspberry-pi.html"
      type: "documentation"
  - resource:
      title: "Ollama Model Library"
      link: "https://ollama.com/library"
      type: "documentation"

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1 # _index.md always has weight of 1 to order correctly
layout: "learningpathall" # All files under learning paths have this same wrapper
learning_path_main_page: "yes" # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
