---
title: Build an audio-to-audio pipeline on Arm with Compute Flow
description: Build and run an audio-to-audio pipeline as an application on your Arm-based device, combining Compute Flow bricks for speech recognition, translation, and speech synthesis

draft: true
cascade:
    draft: true
    
minutes_to_complete: 15

who_is_this_for: This is an introductory topic for developers who want to combine multiple AI models into a performant end-to-end AI application running on an Arm-based CPU.

learning_objectives:
    - Identify how Compute Flow bricks and manifests separate application code from model implementations.
    - Deploy an AI audio-to-audio translation pipeline with Compute Flow.
    - Select a speech recognition model and verify the pipeline using the same application and recording.

prerequisites:
    - An Arm-based system such as an Apple® silicon Mac, Arm-based Linux machine, or Android® phone.
    - Basic Python / C++ knowledge and familiarity with terminal commands
    - Internet access and at least 15 GB of available storage

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-30T19:19:38Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 4d713ef29d940b9043e743e78543b697ed42036d7557c4840126ee434003ac9d
  summary_generated_at: '2026-10-30T19:19:38Z'
  summary_source_hash: 4d713ef29d940b9043e743e78543b697ed42036d7557c4840126ee434003ac9d
  faq_generated_at: '2026-10-30T19:19:38Z'
  faq_source_hash: 4d713ef29d940b9043e743e78543b697ed42036d7557c4840126ee434003ac9d
  summary: >-
    You'll set up Compute Flow and use it to build an audio-to-audio pipeline on an Arm-based device. First, you'll learn about Compute Flow and bricks. Then, you'll create an application that connects speech-to-text, translation,
    and text-to-speech bricks. You'll start with the Parakeet model for speech-to-text. Then, you'll switch to Moonshine by installing its implementation and model, rebuilding, and selecting its
    manifest. Finally, you'll compare speech-to-text performance between the two models.
  # faqs:
  # - question: How do I know my Mac is using the Arm architecture?
  #   answer: >-
  #     Run `uname -m` in your terminal and confirm that the output is `arm64`.
  # - question: What should I do if Compute Flow reports missing dependencies?
  #   answer: >-
  #     Run `compute-flow check`, follow the suggested action for each missing dependency, and rerun
  #     `compute-flow check` to confirm the result. The check does not install dependencies or test
  #     whether a compiler can compile and link a program.
  # - question: Which option should I use to switch from Parakeet to Moonshine for speech recognition?
  #   answer: >-
  #     Install the Moonshine speech-to-text implementation and model, rebuild with
  #     `compute-flow build native`, then pass `moonshine_manifest_base_en.json` to your application
  #     or CLI. You can keep your Python script unchanged because both variants implement `stt.v1`.
  # - question: What result should I expect when the pipeline runs successfully?
  #   answer: >-
  #     You should see the transcription and translation in your terminal. The application saves
  #     synthesized audio to `translated_french.wav` by default, or to the path you provide with
  #     `--output`.
  # - question: How do I compare the two speech-to-text variants correctly?
  #   answer: >-
  #     Run the built speech-to-text CLI for both models on the same 9.963-second mono 16 kHz sample,
  #     changing only the manifest, and compare their total `run()` times. These sample timings do not
  #     assess transcription accuracy.
# END generated_summary_faq

author: Kieran Hejmadi

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: false

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
    - Linux
    - Android

### Cross-platform metadata only
shared_path: true
shared_between:
    - laptops-and-desktops
    - mobile-graphics-and-gaming
    - servers-and-cloud-computing

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
