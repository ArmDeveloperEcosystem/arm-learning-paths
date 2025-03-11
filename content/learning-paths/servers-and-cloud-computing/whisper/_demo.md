---
title: Demo - Audio transcription on Arm
overview: | 
  This Learning Path shows you how to use a c8g.8xlarge AWS Graviton4 instance powered by an Arm Neoverse CPU to build a simple Transcription-as-a-Service server.

  This architecture is suitable for businesses looking to deploy the latest Generative AI technologies with audio transcription capabilities using their existing CPU compute capacity and deployment pipelines. This demo provides speech recognition using the `whisper-large-v3-turbo model`, deployed using the Hugging Face Transformers framework.

  Record audio from your browser to interact with the Whisper model and send it to be transcribed to see the performance for yourself. Note that no recorded audio is saved on our servers at any point. 
  
  After running the demo you can follow the Learning Path to build your own Generative AI service on Arm Neoverse.


demo_steps:
  - Record your voice (give microphone permissions to your browser).
  - Review and send the audio file to the sever for transcription.
  - Recieve transcribed output and view stats.


title_chatbot_area: Whisper Voice Demo

diagram: audio-pic-clearer.png
diagram_blowup: audio-pic.png

terms_and_conditions: demo-terms-and-conditions.txt


### Specific details to this demo
# ================================================================================
stats_description: |
  The 'total time' for a whisper voice-to-text process refers to the complete duration taken from the moment the audio input is received until the final text output is generated. This includes several related times such as the 'pre-processing time', which is the time taken to prepare the audio data for transcription, the 'transcription time', which is the actual time spent converting the audio to text, and the 'post-processing time', which involves refining and formatting the transcribed text. Each of these stages contributes to the overall 'total time' and can vary depending on factors such as audio quality, length of the audio, and the efficiency of the transcription algorithm.

### FIXED, DO NOT MODIFY
# ================================================================================
demo_template_name: whisper_audio_demo   # allows the 'demo.html' partial to route to the correct Configuration and Demo/Stats sub partials for page render.
weight: 2                       # _index.md always has weight of 1 to order correctly
layout: "learningpathall"       # All files under learning paths have this same wrapper
learning_path_main_page: "yes"  # This should be surfaced when looking for related content. Only set for _index.md of learning path content.
---


