---
title: Estimate neural accelerator (NX) performance with ML Inference Advisor

description: Use public MLIA packages and quantized MobileNet models to check Neural Technology compatibility, estimate NX performance, and compare model variants.

minutes_to_complete: 40

who_is_this_for: This Learning Path is for ML engineers and graphics developers who want to evaluate model compatibility and estimated performance for Arm Neural Technology before deployment.

learning_objectives:
    - Install the public MLIA Neural Technology plugin and discover its target profiles and backend
    - Download public quantized MobileNet models and convert them to TOSA
    - Check operator compatibility and interpret NX Performance Estimator reports
    - Compare model variants under the same target configuration and identify accuracy tradeoffs

prerequisites:
    - An Ubuntu 24.02 development machine
    - Basic familiarity with Python, command-line tools, and model deployment
    - (Optional) An NX-capable Android device

author: Annie Tallund

generate_summary_faq: true
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Mali
tools_software_languages:
    - MLIA
    - NX
    - Python
    - LiteRT
    - TOSA
    - VGF
operatingsystems:
    - Linux
    - Android

further_reading:
    - resource:
        title: MLIA Neural Technology package on PyPI
        link: https://pypi.org/project/mlia-neural-technology/
        type: documentation
    - resource:
        title: MLIA Neural Technology CLI and output documentation
        link: https://github.com/arm/mlia-neural-technology/tree/main/docs
        type: documentation
    - resource:
        title: Analyze Ethos-U models with MLIA
        link: /learning-paths/embedded-and-microcontrollers/analyze-ethos-u-models-with-mlia/
        type: learningpath
    - resource:
        title: TensorFlow MobileNet V1 pretrained model catalog
        link: https://github.com/tensorflow/models/blob/master/research/slim/nets/mobilenet_v1.md
        type: documentation
    - resource:
        title: Explore model artifacts with Model Explorer
        link: /learning-paths/cross-platform/explore-model-artifacts-with-model-explorer/
        type: learningpath
    - resource:
        title: Neural Statistics Vulkan capture layer
        link: https://github.com/arm/vulkan-layer-neural-statistics
        type: code

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1
layout: "learningpathall"
learning_path_main_page: "yes"
---
