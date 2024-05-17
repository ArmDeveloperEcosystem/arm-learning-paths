---
title: Speeding up Gemma AI execution on Android with KleidiAI, MediaPipe, and XNNPACK

minutes_to_complete: 10

who_is_this_for: Android developers who want to efficiently run LLMs on-device.

learning_objectives:
    - Install prerequisites to cross-compiling new inference engines for Android.
    - Run (and benchmark) the Gemma 2B model using the Google MediaPipe ML framework, with XNNPACK as the primative provider.
    - Add KleidiAI's int4 kernels to XNNPACK, and benchmark the results.

prerequisites:
    - You will need an x86_64 Linux machine running Ubuntu. This is the host machine to build the binaries on.
    - You will need an Android Phone with support for i8mm (tested on Pixel 8 Pro)

author_primary: Pareena Verma, Joe Stech

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - PLACEHOLDER IP A
    - PLACEHOLDER IP B
tools_software_languages:
    - PLACEHOLDER TOOL OR SOFTWARE C
    - PLACEHOLDER TOOL OR SOFTWARE D
operatingsystems:
    - Linux, MacOS


### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
