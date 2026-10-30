---
title: Build an audio-to-audio pipeline on Arm with Compute Flow
description: Build and run an audio-to-audio pipeline as a Python application on your Arm-based device, combining Compute Flow bricks for speech recognition, translation, and speech synthesis

minutes_to_complete: 15

who_is_this_for: This is an introductory topic for developers who want to combine multiple AI models into a performant end-to-end AI applicaton running on an Arm-based CPU. 

learning_objectives:
    - Identify how Compute Flow bricks and manifests separate application code from model implementations.
    - Deploy an AI audio-to-audio translation pipline in Python with Compute Flow. 
    - Select the speech recognition model and verify the pipeline using the same application and recording.

prerequisites:
    - An Arm-based system such as an Apple® silicon Mac
    - Basic Python knowledge and familiarity with terminal commands
    - Internet access and at least 15 GB of available storage

author: Kieran Hejmadi

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: true

# Optional one-shot controls: set either field to true to regenerate just that
# generated section the next time the summary/FAQ tool runs. The tool resets
# them to false after a successful write.
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Introductory
subjects: ML
armips: []
tools_software_languages:
    - Compute Flow
    - Python
    - uv
operatingsystems:
    - macOS

### Cross-platform metadata only
shared_path: true
shared_between:
    - laptops-and-desktops

further_reading:
    - resource:
        title: Compute Flow source repository (public URL placeholder)
        link: https://github.com/ARM-software/compute-flow
        type: documentation
    - resource:
        title: Install uv
        link: https://docs.astral.sh/uv/getting-started/installation/
        type: documentation

# Publication checks: confirm the public repository and documentation URLs,
# and verify native dependency bundles are accessible from the public checkout.
# Source reference: Compute Flow 885a3466e33eb5e843cd55d1d0180e0bc292520a.
# Validated on macOS 26.6.2 arm64 with Python 3.12.6 and AppleClang 21.0.0.
# Both pipelines completed with the same script and input recording. WAV checks
# passed at 24 kHz: Parakeet output 9.36 s, Moonshine output 7.76 s.
# afplay exited successfully for both WAV files.
# Local validation used the certifi CA bundle and disabled discovery of an
# incompatible pre-installed llama.cpp package.

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
