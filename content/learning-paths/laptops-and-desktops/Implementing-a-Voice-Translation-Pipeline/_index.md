---
title: Implement a voice translation pipeline on Apple silicon 

description: Build an on-device English-to-Spanish voice translator on an Apple silicon Mac using Python, Sherpa-ONNX, Gemma 4 E2B, and LiteRT-LM.

minutes_to_complete: 45

who_is_this_for: This Learning Path is for Python developers who want to implement a voice translation pipeline locally on an Apple silicon Mac. You'll translate English speech into Spanish. You can select other supported target languages, but recognizing speech in another source language requires a different speech recognition model and configuration.

learning_objectives:
    - Prepare LiteRT-LM and a Gemma 4 model for local translation on an Apple silicon Mac.
    - Capture microphone input and transcribe English speech locally with Sherpa-ONNX.
    - Prompt Gemma 4 to translate the English transcript into Spanish.
    - Synthesize and play the Spanish translation with Supertonic 3 and Sherpa-ONNX.

prerequisites:
    - A Mac with Apple silicon running macOS 12 or later, with a microphone, speakers, at least 8 GB of memory, and 15 GB of free storage
    - Python 3.10 through 3.13
    - Internet access for dependency and model downloads

# START generated_summary_faq
generated_summary_faq:
  template_version: summary-faq-v3
  generated_at: '2026-10-15T18:08:06Z'
  generator: ai
  ai_assisted: true
  ai_review_required: true
  model: gpt-5
  prompt_template: summary-faq-v3
  source_hash: 7440bcab530ab4801097c8a94c7f82f5b33404e389c40090c8d74573c1dc7f28
  summary_generated_at: '2026-10-15T18:08:06Z'
  summary_source_hash: 7440bcab530ab4801097c8a94c7f82f5b33404e389c40090c8d74573c1dc7f28
  faq_generated_at: '2026-10-15T18:08:06Z'
  faq_source_hash: 7440bcab530ab4801097c8a94c7f82f5b33404e389c40090c8d74573c1dc7f28
  summary: >-
    You'll build a local English-to-Spanish voice translator on an Apple silicon Mac. First, you'll prepare
    Python and download the models. You'll then test microphone transcription with Sherpa-ONNX, text
    translation with Gemma 4 E2B and LiteRT-LM, and speech synthesis with Supertonic 3. Finally,
    you'll connect these stages in Gradio and verify the transcript, translation, spoken result, and
    offline operation.
#   faqs:
#   - question: How do I confirm that my microphone transcription works before adding translation?
#     answer: >-
#       Run `python stt.py` to record five seconds of audio. Confirm that the transcript contains the
#       words you spoke. If it's empty, check the selected microphone and your terminal's permission.
#   - question: How do I test Spanish translation before connecting the microphone?
#     answer: >-
#       Run `python translate.py Spanish` and enter a short English sentence at the prompt. You should
#       see the Spanish translation appear as Gemma generates it.
#   - question: How do I test text-to-speech and verify audio playback?
#     answer: >-
#       Run `python tts.py Spanish` and paste a Spanish sentence to synthesize and play speech. If you
#       don't hear audio, confirm that macOS has selected your intended output device.
#   - question: Which files should exist before launching the Gradio app?
#     answer: >-
#       Make sure `stt.py`, `translate.py`, `tts.py`, and `languages.py` are in your project directory.
#       Then create `app.py` to connect them to a local Gradio interface.
#   - question: Can I translate into a language other than Spanish?
#     answer: >-
#       Yes. Select another language listed in `LANGUAGES`. To add a new supported target language,
#       update `LANGUAGES` in `languages.py`. For a non-English source language, you need a different
#       speech recognition model and configuration.
# END generated_summary_faq

author: Sammy Sahnine

# New Learning Paths are opted in for the next manual generated summary/FAQ run.
# The generator resets this to false after a successful write.
generate_summary_faq: false

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
