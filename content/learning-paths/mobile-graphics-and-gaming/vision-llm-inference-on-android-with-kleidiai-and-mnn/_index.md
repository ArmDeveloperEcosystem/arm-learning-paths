---
title: Vision LLM inference on Android with KleidiAI and MNN

minutes_to_complete: 30

who_is_this_for: This Learning Path is for developers who want to run Vision Transformers (ViT) efficiently on Android.

learning_objectives:
    - Download a Vision Large Language Model (LLM) from Hugging Face.
    - Convert the model to the Mobile Neural Network (MNN) framework.
    - Install an Android demo application using the model to run an inference.
    - Compare inference performance with and without KleidiAI Arm-optimized micro-kernels.


prerequisites:
    - A development machine with [Android Studio](https://developer.android.com/studio) installed.
    - A smartphone running Android with support for `i8mm` and `dotprod` instructions.

author:
    - Shuheng Deng
    - Yiyang Fan

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
tools_software_languages:
    - Android Studio
    - KleidiAI
operatingsystems:
    - Android



further_reading:
    - resource:
        title: "MNN: A Universal and Efficient Inference Engine"
        link: https://arxiv.org/pdf/2002.12418
        type: documentation
    - resource:
        title: MNN-Doc
        link: https://mnn-docs.readthedocs.io/en/latest/
        type: blog
    - resource:
        title: Vision transformer
        link: https://en.wikipedia.org/wiki/Vision_transformer
        type: website
    - resource:
        title: KleidiAI repository
        link: https://github.com/ARM-software/kleidiai
        type: documentation



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
