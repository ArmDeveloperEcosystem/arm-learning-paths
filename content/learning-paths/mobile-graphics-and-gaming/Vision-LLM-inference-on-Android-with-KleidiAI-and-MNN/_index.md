---
title: Vision LLM inference on Android with KleidiAI and MNN

minutes_to_complete: 30

who_is_this_for: This is an advanced topic for Android developers who want to efficiently run Vision-Transformer (ViT) on an Android device.

learning_objectives:
    - Run ViT inference on an Android device with the [Qwen Vision 2B](https://huggingface.co/Qwen/Qwen2-VL-2B-Instruct) model using the MNN inference framework.
    - Download and Convert a Qwen Vision model from Hugging Face.

prerequisites:
    - A x86_64 development machine with [Android Studio](https://developer.android.com/studio) installed.
    - A 64-bit Arm powered smartphone running Android with i8mm/dotprod supported.

author: Shuheng Deng,Arm

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



### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
