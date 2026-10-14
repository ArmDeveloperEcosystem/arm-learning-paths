---
title: Getting Started with Compute Flow
description: Connect speech recognition, translation, and speech synthesis with Compute Flow on your Apple silicon Mac, then replace a model without changing your Python application.

minutes_to_complete: 30

who_is_this_for: This is an introductory topic for developers who want to combine multiple AI models into a performant end-to-end AI applicaton running on an Arm CPU.

learning_objectives:
    - Explain how Compute Flow bricks and manifests separate application code from model implementations
    - Run a local Python pipeline that translates English speech into French speech
    - Replace the speech recognition model and verify the pipeline using the same application and recording

prerequisites:
    - An Apple silicon Mac running macOS
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

further_reading:
    - resource:
        title: Compute Flow source repository (public URL placeholder)
        link: https://github.com/ARM-software/ComputeFlow
        type: documentation
    - resource:
        title: Compute Flow application development guide (public URL placeholder)
        link: https://github.com/ARM-software/ComputeFlow/blob/main/docs/howto/developing_apps_with_compute_flow.md
        type: documentation
    - resource:
        title: Compute Flow speech translation example (public URL placeholder)
        link: https://github.com/ARM-software/ComputeFlow/blob/main/docs/examples/python/audio_to_audio_translation.md
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
