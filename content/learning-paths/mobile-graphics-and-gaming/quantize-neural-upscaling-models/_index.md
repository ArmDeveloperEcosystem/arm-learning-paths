---
title: Quantize neural upscaling models with ExecuTorch
    
minutes_to_complete: 60

who_is_this_for: This is an advanced topic for ML developers who want to reduce latency and memory bandwidth by exporting INT8 models to the `.vgf` file format using the ExecuTorch Arm backend.

learning_objectives:
    - Explain when to use post-training quantization (PTQ) vs quantization-aware training (QAT)
    - Prepare and quantize a PyTorch model using TorchAO PT2E quantization APIs
    - Export the quantized model to TOSA and generate a model artifact with the ExecuTorch Arm backend
    - Validate the exported graph by visualizing it using Google's Model Explorer

prerequisites:
    - Basic PyTorch model training and evaluation experience
    - A development machine with Python 3.10+ and PyTorch installed that runs ExecuTorch

author:
- Richard Burton
- Annie Tallund

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Mali
tools_software_languages:
    - ExecuTorch
    - TorchAO
    - Vulkan
    - TOSA
    - NX
operatingsystems:
    - Linux
    - macOS
    - Windows

further_reading:
    - resource:
        title: Get started with neural graphics using ML Extensions for Vulkan
        link: /learning-paths/mobile-graphics-and-gaming/vulkan-ml-sample/
        type: learningpath
    - resource:
        title: Fine-tune neural graphics models with Model Gym
        link: /learning-paths/mobile-graphics-and-gaming/model-training-gym/
        type: learningpath
    - resource:
        title: Neural Graphics Development Kit
        link: https://developer.arm.com/mobile-graphics-and-gaming/neural-graphics
        type: website
    - resource:
        title: Arm neural technology in ExecuTorch 1.0
        link: https://developer.arm.com/community/arm-community-blogs/b/ai-blog/posts/arm-neural-technology-in-executorch-1-0
        type: website

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
