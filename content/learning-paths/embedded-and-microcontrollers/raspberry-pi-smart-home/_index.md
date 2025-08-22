---
title: Build a Privacy-First LLM Smart Home on Raspberry Pi 5

minutes_to_complete: 45

who_is_this_for: This is an introductory topic for edge AI developers, Raspberry Pi hobbyists, and software engineers who want to build privacy-first smart home assistants. You’ll learn how to run large language models (LLMs) locally on the Raspberry Pi 5 using Ollama, control GPIO-connected devices, and deploy a web-based assistant without relying on cloud services.

learning_objectives:
  - Understand how the Arm architecture enables efficient, private, and responsive LLM inference
  - Run a smart home assistant on Raspberry Pi 5 with local LLM integration
  - Wire and control physical devices (for example, LEDs) using Raspberry Pi GPIO pins
  - Deploy and interact with a local language model using Ollama
  - Launch and access a web-based dashboard for device control

prerequisites:
  - An Arm-based single board computer (for example, Raspberry Pi 5 running Raspberry Pi OS)
  - Electronic components (breadboard, LEDs, resistors, jumper wires) for GPIO testing
  - Familiarity with Python programming, Raspberry Pi GPIO pinout, and basic electronics

author: Fidel Makatia Omusilibwa

skilllevels: Introductory
subjects: ML
armips:
  - Cortex-A
tools_software_languages:
  - Python
  - Ollama
  - gpiozero
  - lgpio
  - FastAPI
  - Raspberry Pi
operatingsystems:
  - Linux

further_reading:
  - resource:
      title: Raspberry Pi 5 Smart Home Assistant with EdgeAI
      link: https://github.com/fidel-makatia/EdgeAI_Raspi5
      type: source
  - resource:
      title: Ollama Python/JavaScript Libraries
      link: https://ollama.com/blog/python-javascript-libraries
      type: documentation
  - resource:
      title: gpiozero Documentation for Raspberry Pi
      link: https://gpiozero.readthedocs.io/en/stable/
      type: documentation
  - resource:
      title: lgpio Library for Raspberry Pi 5
      link: https://abyz.me.uk/lg/lgpio.html
      type: documentation
  - resource:
      title: Raspberry Pi 5 Official Documentation
      link: https://www.raspberrypi.org/documentation/computers/raspberry-pi.html
      type: documentation
  - resource:
      title: Ollama Model Library
      link: https://ollama.com/library
      type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1 # _index.md always has weight of 1 to order correctly
layout: "learningpathall" # All files under learning paths have this same wrapper
learning_path_main_page: "yes" # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
