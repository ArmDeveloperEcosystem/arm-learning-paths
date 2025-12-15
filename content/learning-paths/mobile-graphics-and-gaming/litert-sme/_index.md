---
title: Accelerate LiteRT Models on Android with KleidiAI and SME2

minutes_to_complete: 45

who_is_this_for: This is an advanced topic for developers looking to leverage Arm's Scalable Matrix Extension 2 (SME2) instructions to accelerate LiteRT model inference on Android.

learning_objectives: 
- Understand how KleidiAI integrates with LiteRT
- Build the LiteRT benchmark tool and enable XNNPACK and KleidiAI with SME2 support in LiteRT
- Create LiteRT models that can be accelerated by SME2 through KleidiAI
- Use the benchmark tool to evaluate and validate the SME2 acceleration performance of LiteRT models

prerequisites:
- An Arm64 Linux development machine 
- An Android device that supports Arm SME2 architecture features - see this [list of devices with SME2 support](/learning-paths/cross-platform/multiplying-matrices-with-sme2/1-get-started/#devices)

author: Jiaming Guo

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
    - Cortex-X
tools_software_languages:
    - C
    - Python
operatingsystems:
    - Android



further_reading:
    - resource:
        title: LiteRT model optimization
        link: https://ai.google.dev/edge/litert/models/model_optimization
        type: website
    - resource:
        title: Convert Pytorch model to LiteRT model
        link: https://ai.google.dev/edge/litert/models/pytorch_to_tflite
        type: website
    - resource:
        title: LiteRT repository
        link: https://github.com/google-ai-edge/LiteRT?tab=readme-ov-file#1--i-have-a-pytorch-model
        type: website



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
