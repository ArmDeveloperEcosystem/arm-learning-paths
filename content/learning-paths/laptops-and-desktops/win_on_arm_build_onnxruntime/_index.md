---
title: Powering Phi-3 with ONNX Runtime & KleidiAI on Windows

minutes_to_complete: 60

who_is_this_for: A deep-dive for advanced developers looking to build ONNX Runtime on Windows ARM (WoA) and leverage the Generate() API to run Phi-3 inference with KleidiAI acceleration.

learning_objectives: 
    - Build ONNX Runtime and ONNX Runtime generate() API for Windows on ARM.
    - Run a Phi-3 model using ONNX Runtime on an Arm-based Windows laptop.

prerequisites:
    - A Windows on Arm computer such as the Lenovo Thinkpad X13 running Windows 11 or a Windows on Arm virtual machine

author: Barbara Corriero

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
    - Cortex-X
tools_software_languages:
    - Visual Studio IDE - 2022+ Community Version
    - C++
    - Python 3.10+
    - Git
    - CMake-3.28 or higher
operatingsystems:
    - Windows

further_reading:
    - resource:
        title: ONNX Runtime
        link: https://onnxruntime.ai/docs/
        type: documentation
    - resource:
        title: ONNX Runtime generate() API
        link: https://onnxruntime.ai/docs/genai/
        type: documentation
    - resource:
        title: Accelerating AI Developer Innovation Everywhere with New Arm Kleidi
        link: https://newsroom.arm.com/blog/arm-kleidi
        type: blog

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
