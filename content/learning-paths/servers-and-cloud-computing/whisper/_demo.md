---
title: Demo - Whisper Voice Audio transcription on Arm
overview: | 
  Insert helpful overview here.



demo_steps:
  - Record your voice, ensuring that your browser has microphone permissions enabled.
  - Review your recording and send to _________________insert technical thing here_____________.
  - Receive the transcription and view your statistics.


title_chatbot_area: Whisper Voice Demo

diagram: audio-pic-clearer.png
diagram_blowup: audio-pic.png

terms_and_conditions: demo-terms-and-conditions.txt


### Specific details to this demo
# ================================================================================
stats_description: The 'total time' for a Whisper voice-to-text process is the full duration from when the audio input is received until the final text output is generated. This includes 'pre-processing time' - the time taken to prepare the audio data for transcription; transcription time' - the actual time spent converting the audio to text; and Post-processing time' - the time spent refining and formatting the transcribed text. Each of these stages contributes to the overall 'total time' and can vary depending on factors such as audio quality, length of the audio, and the efficiency of the transcription algorithm.

### FIXED, DO NOT MODIFY
# ================================================================================
demo_template_name: whisper_audio_demo   # allows the 'demo.html' partial to route to the correct Configuration and Demo/Stats sub partials for page render.
weight: 2                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


