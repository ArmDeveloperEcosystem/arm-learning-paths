---
title: Implement a voice translation pipeline

description: Build an on-device English-to-Spanish voice translator on an Apple Silicon (aarch64) Mac using Python, Sherpa-ONNX, Gemma 4 E2B, and LiteRT-LM.

minutes_to_complete: 45

who_is_this_for: This Learning Path is for Python developers who want to implement a translation speech pipeline locally. Whilst we focus specifically on translating to Spanish, these steps are applicable to any other supported translation pair.

learning_objectives:
    - Prepare LiteRT-LM and a Gemma 4 model for local translation on an Apple Silicon Mac.
    - Capture microphone input and transcribe English speech locally with Sherpa-ONNX.
    - Prompt Gemma 4 to translate the English transcript into Spanish.
    - Synthesise and play the Spanish translation with Supertonic 3 and Sherpa-ONNX.

prerequisites:
    - An Apple Silicon Mac running macOS 12 or later, with a microphone, speakers, at least 8 GB of memory, and 15 GB of free storage
    - Python 3.10 through 3.13
    - Internet access for dependency and model downloads

author: Sammy Sahnine

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: true

# Optional one-shot controls: set either field to true to regenerate just that
# generated section the next time the summary/FAQ tool runs. The tool resets
# them to false after a successful write.
rerun_summary: false
rerun_faqs: false

### Tags
skilllevels: Advanced
subjects: ML
armips:
    - Cortex-A
tools_software_languages:
    - Python
    - Gradio
    - LiteRT-LM
    - Gemma 4
    - Sherpa-ONNX
    - Supertonic 3
operatingsystems:
    - macOS

further_reading:
    - resource:
        title: LiteRT-LM repository
        link: https://github.com/google-ai-edge/LiteRT-LM
        type: documentation
    - resource:
        title: Gemma 4 E2B for LiteRT-LM on Hugging Face
        link: https://huggingface.co/litert-community/gemma-4-E2B-it-litert-lm
        type: website
    - resource:
        title: Sherpa-ONNX real-time speech recognition from a microphone
        link: https://k2-fsa.github.io/sherpa/onnx/python/real-time-speech-recongition-from-a-microphone.html
        type: documentation
    - resource:
        title: Sherpa-ONNX Supertonic text-to-speech
        link: https://k2-fsa.github.io/sherpa/onnx/tts/supertonic.html
        type: documentation
    - resource:
        title: Gradio Audio component
        link: https://www.gradio.app/docs/gradio/audio
        type: documentation

### FIXED, DO NOT MODIFY
# ================================================================================
weight: 1                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---
