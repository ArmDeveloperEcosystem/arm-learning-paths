---
title: Demo - Audio transcription on Arm
overview: | 
  Insert helpful overview here.



demo_steps:
  - Record your voice (giving mic permissions to your browser).
  - Review and send to _________________insert technical thing here_____________.
  - Get transcription and view stats.


title_chatbot_area: Whisper Voice Demo

diagram: audio-pic-clearer.png
diagram_blowup: audio-pic.png

terms_and_conditions: demo-terms-and-conditions.txt


### Specific details to this demo
# ================================================================================
stats_description: The 'total time' for a whisper voice-to-text process refers to the complete duration taken from the moment the audio input is received until the final text output is generated. This includes several related times such as the 'pre-processing time', which is the time taken to prepare the audio data for transcription, the 'transcription time', which is the actual time spent converting the audio to text, and the 'post-processing time', which involves refining and formatting the transcribed text. Each of these stages contributes to the overall 'total time' and can vary depending on factors such as audio quality, length of the audio, and the efficiency of the transcription algorithm.

### FIXED, DO NOT MODIFY
# ================================================================================
demo_template_name: whisper_audio_demo   # allows the 'demo.html' partial to route to the correct Configuration and Demo/Stats sub partials for page render.
weight: 2                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


