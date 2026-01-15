---
title: Run Phi-3 on Windows on Arm using ONNX Runtime

minutes_to_complete: 60

who_is_this_for: This is an advanced topic for developers looking to build ONNX Runtime for Windows on Arm (WoA) and leverage the Generate() API to run Phi-3 inference with KleidiAI acceleration.

learning_objectives: 
    - Build ONNX Runtime and enable the Generate() API for Windows on Arm.
    - Run inference with a Phi-3 model using ONNX Runtime with KleidiAI acceleration.
prerequisites:
    - A Windows on Arm computer such as a Lenovo Thinkpad X13 running Windows 11, or a Windows on Arm [virtual machine](/learning-paths/cross-platform/woa_azure/).

author: Barbara Corriero

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
tools_software_languages:
    - Visual Studio
    - CPP
    - Python
    - Git
    - CMake
    - ONNX Runtime
operatingsystems:
    - Windows

further_reading:
    - resource:
        title: ONNX Runtime
        link: https://onnxruntime.ai/docs/
        type: documentation
    - resource:
        title: ONNX Runtime Generate() API
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
