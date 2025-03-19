---
title: Vision LLM inference on Android with KleidiAI and MNN

minutes_to_complete: 30

who_is_this_for: This learning path is for developers who want to run Vision-Transformer (ViT) efficiently on an Android device.

learning_objectives:
    - Download the a Vision Large Language Model (LLM) from Hugging Face.
    - Convert the model to the Mobile Neural Network (MNN) framework.
    - Install an Android demo app with the model to run inference.
    - Compare performance benchmark with and without KleidiAI Arm optimized micro-kernels.


prerequisites:
    - A development machine with [Android Studio](https://developer.android.com/studio) installed.
    - A 64-bit Arm powered smartphone running Android with `i8mm` and `dotprod` supported.

author: Shuheng Deng

### Tags
skilllevels: Introductory
subjects: ML
armips:
    - Cortex-A
    - Cortex-X
tools_software_languages:
    - Android Studio
    - KleidiAI
operatingsystems:
    - Android



further_reading:
    - resource:
        title: "MNN : A UNIVERSAL AND EFFICIENT INFERENCE ENGINE"
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
